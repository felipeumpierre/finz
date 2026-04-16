"""Resolve EUR price for a (coin, timestamp) using cache → manual → Binance klines → CoinGecko."""
from __future__ import annotations

import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Optional

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/{coin_id}/history"
BINANCE_KLINES_URL = "https://api.binance.com/api/v3/klines"

# CoinGecko coin id map (used only if COINGECKO_API_KEY is set)
SYMBOL_TO_CG_ID = {
    "BTC": "bitcoin", "ETH": "ethereum", "XRP": "ripple", "BNB": "binancecoin",
    "SOL": "solana", "ADA": "cardano", "DOT": "polkadot", "USDT": "tether",
    "USDC": "usd-coin", "BUSD": "binance-usd", "SAND": "the-sandbox",
    "GALA": "gala", "FTM": "fantom", "ANKR": "ankr", "PEPE": "pepe",
    "SHIB": "shiba-inu", "MATIC": "matic-network", "LINK": "chainlink",
    "ONE": "harmony", "DAR": "mines-of-dalarnia", "PERP": "perpetual-protocol",
    "OP": "optimism", "MINA": "mina-protocol", "MEME": "memecoin",
    "NTRN": "neutron-3", "BETH": "binance-eth", "BNSOL": "binance-staked-sol",
}

# Stablecoins pegged 1:1 to USD — use EURUSDT inverse as proxy
USD_STABLECOINS = {"USDT", "USDC", "BUSD", "DAI", "TUSD", "FDUSD"}

# Max candles per Binance klines request
_BINANCE_MAX_CANDLES = 1000


class PriceResolver:
    class MissingPriceError(Exception):
        def __init__(self, coin: str, date: str):
            super().__init__(f"No EUR price available for {coin} on {date}")
            self.coin = coin
            self.date = date

    def __init__(self, cache_dir: Path, http_client, manual_prices: Optional[list[dict]] = None):
        self.cache_dir = Path(cache_dir)
        self.http_client = http_client
        self.manual = {(m["coin"], m["date"]): Decimal(str(m["eur_price"])) for m in (manual_prices or [])}

    @staticmethod
    def _date_only(ts: str) -> str:
        return datetime.fromisoformat(ts).date().isoformat()

    def _cache_path(self, coin: str, date: str) -> Path:
        return self.cache_dir / coin / f"{date}.json"

    def _write_cache(self, coin: str, date: str, eur: Decimal) -> None:
        p = self._cache_path(coin, date)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps({"eur": format(eur, "f")}))

    # ------------------------------------------------------------------
    # Bulk prefetch: one API call per (coin, symbol) range instead of
    # one call per (coin, date). Call this before the processing loop.
    # ------------------------------------------------------------------

    def prefetch(self, needed: list[tuple[str, str]]) -> None:
        """Pre-populate cache for all (coin, date) pairs not already cached.

        Groups by coin, then fetches all needed dates in bulk via Binance
        klines (up to 1000 candles per request).  Falls back to per-date
        fetch for any dates still missing after the bulk pass.
        """
        if self.http_client is None:
            return

        # Filter to uncached pairs
        missing: list[tuple[str, str]] = [
            (c, d) for c, d in needed
            if (c, d) not in self.manual and not self._cache_path(c, d).exists()
        ]
        if not missing:
            return

        # Group dates by effective Binance symbol
        # For each coin we need to know what symbol(s) to fetch
        coin_dates: dict[str, set[str]] = defaultdict(set)
        for coin, date in missing:
            coin_dates[coin].add(date)

        total_coins = len(coin_dates)
        print(f"[prefetch] {len(missing)} (coin,date) pairs across {total_coins} coins", file=sys.stderr)

        # Fetch EURUSDT once per unique date (needed for USDT-path fallback)
        all_dates: set[str] = {d for _, d in missing}
        eurusdt_rates: dict[str, Optional[Decimal]] = {}
        self._bulk_fetch_symbol("EURUSDT", all_dates, eurusdt_rates)

        def usdt_eur(date: str) -> Optional[Decimal]:
            rate = eurusdt_rates.get(date)
            if rate is None or rate == 0:
                return None
            return Decimal("1") / rate

        for i, (coin, dates) in enumerate(coin_dates.items(), 1):
            # Uncached dates only (may have been filled by a previous coin's EURUSDT fetch)
            dates_needed = {d for d in dates if not self._cache_path(coin, d).exists()}
            if not dates_needed:
                continue

            print(f"[prefetch] {i}/{total_coins} {coin} ({len(dates_needed)} dates)", file=sys.stderr)

            if coin in USD_STABLECOINS or coin in ("BETH", "BNSOL"):
                # Resolve via proxy
                proxy = "ETH" if coin == "BETH" else ("SOL" if coin == "BNSOL" else None)
                if proxy:
                    proxy_prices: dict[str, Optional[Decimal]] = {}
                    self._bulk_fetch_symbol(f"{proxy}EUR", dates_needed, proxy_prices)
                    for d in dates_needed:
                        if proxy_prices.get(d) is not None:
                            self._write_cache(coin, d, proxy_prices[d])
                else:
                    # USD stablecoin
                    for d in dates_needed:
                        eur = usdt_eur(d)
                        if eur is not None:
                            self._write_cache(coin, d, eur)
                continue

            # Try direct EUR pair
            eur_prices: dict[str, Optional[Decimal]] = {}
            self._bulk_fetch_symbol(f"{coin}EUR", dates_needed, eur_prices)
            still_missing = {d for d in dates_needed if eur_prices.get(d) is None}

            for d, price in eur_prices.items():
                if price is not None:
                    self._write_cache(coin, d, price)

            # Fallback: COIN/USDT × 1/EURUSDT for remaining dates
            if still_missing:
                usdt_prices: dict[str, Optional[Decimal]] = {}
                self._bulk_fetch_symbol(f"{coin}USDT", still_missing, usdt_prices)
                for d, price in usdt_prices.items():
                    if price is not None:
                        eur = usdt_eur(d)
                        if eur is not None:
                            self._write_cache(coin, d, price * eur)

        print("[prefetch] done", file=sys.stderr)

    def _bulk_fetch_symbol(
        self, symbol: str, dates: set[str], out: dict[str, Optional[Decimal]]
    ) -> None:
        """Fetch daily closes for `symbol` across all needed dates and store in `out`."""
        if not dates:
            return
        sorted_dates = sorted(dates)
        start_dt = datetime.fromisoformat(sorted_dates[0]).replace(tzinfo=timezone.utc)
        end_dt = datetime.fromisoformat(sorted_dates[-1]).replace(tzinfo=timezone.utc) + timedelta(days=1)
        start_ms = int(start_dt.timestamp() * 1000)
        end_ms = int(end_dt.timestamp() * 1000)

        candles: list[list] = []
        cursor_ms = start_ms
        while cursor_ms < end_ms:
            for attempt in range(4):
                try:
                    resp = self.http_client.get(
                        BINANCE_KLINES_URL,
                        params={"symbol": symbol, "interval": "1d",
                                "startTime": cursor_ms, "endTime": end_ms,
                                "limit": _BINANCE_MAX_CANDLES},
                        timeout=15,
                    )
                    if resp.status_code in (429, 418):
                        time.sleep(5 * (2 ** attempt))
                        continue
                    if resp.status_code != 200:
                        return  # symbol doesn't exist on Binance
                    batch = resp.json()
                    if not batch or isinstance(batch, dict):
                        return
                    candles.extend(batch)
                    cursor_ms = batch[-1][0] + 86_400_000  # advance by one day
                    break
                except Exception:
                    if attempt == 3:
                        return
                    time.sleep(2)
            else:
                return  # rate limit retries exhausted

        # Map open-time → close price
        candle_map: dict[str, Decimal] = {}
        for c in candles:
            open_ms = c[0]
            candle_date = datetime.fromtimestamp(open_ms / 1000, tz=timezone.utc).date().isoformat()
            candle_map[candle_date] = Decimal(str(c[4]))  # close price

        for d in dates:
            out[d] = candle_map.get(d)  # None if not found (delisted / not yet listed)

    # ------------------------------------------------------------------
    # Per-date fallback (used when prefetch wasn't called or missed a date)
    # ------------------------------------------------------------------

    def _binance_daily_close(self, symbol: str, date: str) -> Optional[Decimal]:
        try:
            start_dt = datetime.fromisoformat(date).replace(tzinfo=timezone.utc)
            end_dt = start_dt + timedelta(days=1)
            start_ms = int(start_dt.timestamp() * 1000)
            end_ms = int(end_dt.timestamp() * 1000)
            params = {"symbol": symbol, "interval": "1d", "startTime": start_ms, "endTime": end_ms, "limit": 1}
            for attempt in range(3):
                resp = self.http_client.get(BINANCE_KLINES_URL, params=params, timeout=10)
                if resp.status_code in (429, 418):
                    time.sleep(5 * (2 ** attempt))
                    continue
                if resp.status_code != 200:
                    return None
                data = resp.json()
                if not data or isinstance(data, dict):
                    return None
                return Decimal(str(data[0][4]))
            return None
        except Exception:
            return None

    def _usdt_eur_rate(self, date: str) -> Optional[Decimal]:
        eurusdt = self._binance_daily_close("EURUSDT", date)
        if eurusdt is None or eurusdt == 0:
            return None
        return Decimal("1") / eurusdt

    def _fetch_binance(self, coin: str, date: str) -> Optional[Decimal]:
        if self.http_client is None:
            return None
        if coin in USD_STABLECOINS:
            return self._usdt_eur_rate(date)
        if coin == "BETH":
            return self._fetch_binance("ETH", date)
        if coin == "BNSOL":
            return self._fetch_binance("SOL", date)
        eur = self._binance_daily_close(f"{coin}EUR", date)
        if eur is not None:
            return eur
        coin_usdt = self._binance_daily_close(f"{coin}USDT", date)
        if coin_usdt is None:
            return None
        usdt_eur = self._usdt_eur_rate(date)
        if usdt_eur is None:
            return None
        return coin_usdt * usdt_eur

    def _fetch_coingecko(self, coin: str, date: str) -> Optional[Decimal]:
        if self.http_client is None:
            return None
        api_key = os.environ.get("COINGECKO_API_KEY")
        if not api_key:
            return None
        coin_id = SYMBOL_TO_CG_ID.get(coin)
        if not coin_id:
            return None
        d = datetime.fromisoformat(date).strftime("%d-%m-%Y")
        url = COINGECKO_URL.format(coin_id=coin_id)
        try:
            resp = self.http_client.get(
                url,
                params={"date": d, "localization": "false"},
                headers={"x-cg-demo-api-key": api_key},
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
            return Decimal(str(data["market_data"]["current_price"]["eur"]))
        except Exception:
            return None

    def resolve(self, coin: str, timestamp: str) -> Decimal:
        date = self._date_only(timestamp)
        if (coin, date) in self.manual:
            return self.manual[(coin, date)]
        cache = self._cache_path(coin, date)
        if cache.exists():
            return Decimal(json.loads(cache.read_text())["eur"])
        fetched = self._fetch_binance(coin, date) or self._fetch_coingecko(coin, date)
        if fetched is not None:
            self._write_cache(coin, date, fetched)
            return fetched
        raise self.MissingPriceError(coin, date)
