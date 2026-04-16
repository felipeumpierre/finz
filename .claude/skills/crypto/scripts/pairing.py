"""Collapse Binance composite rows (same-timestamp Buy/Sell/Fee) into single ClassifiedTx.

Handles:
  trade_buy_leg + trade_sell_leg + optional fee_standalone (same timestamp)
     -> ClassifiedTx(classified_as="trade_buy" | "trade_sell")
  crypto_swap_leg x 2 (same timestamp, one positive, one negative)
     -> ClassifiedTx(classified_as="crypto_swap")
  crypto_swap_leg x N (N negatives + 1 positive — dust exchange / BNB sweep)
     -> N * ClassifiedTx(classified_as="crypto_swap"), each disposing one
        negative leg and receiving a proportional share of the positive leg

Non-composite classifications pass through as ClassifiedTx directly.

Orphan legs (no counterpart) are classified by sign:
  - positive amount -> external_in (treated as an unexplained acquisition at FMV)
  - negative amount -> external_out (treated as an unexplained disposal at FMV)
They retain a `unpaired_trade_leg` note for audit trail.
"""
from __future__ import annotations

from collections import defaultdict
from decimal import Decimal
from typing import Iterable

from scripts.schemas import AssetAmount, ClassifiedTx, NormalizedRow

LEG_CATEGORIES = {"trade_buy_leg", "trade_sell_leg", "crypto_swap_leg", "fee_standalone"}


def _non_composite(row: NormalizedRow, classified_as: str) -> ClassifiedTx:
    is_positive = row.change > 0
    asset = AssetAmount(coin=row.coin, amount=abs(row.change))
    return ClassifiedTx(
        id=row.id,
        source=row.source,
        timestamp=row.timestamp,
        raw_operation=row.raw_operation,
        classified_as=classified_as,
        asset_in=asset if is_positive else None,
        asset_out=asset if not is_positive else None,
        eur_value_at_time=row.eur_value_hint,
        price_source="exchange_reported" if row.eur_value_hint is not None else None,
    )


def _orphan_leg(row: NormalizedRow) -> ClassifiedTx:
    """Classify a truly-unpaired leg by sign, avoiding the misleading 'airdrop' label."""
    classified_as = "external_in" if row.change > 0 else "external_out"
    tx = _non_composite(row, classified_as)
    tx.notes.append("unpaired_trade_leg")
    return tx


def pair_composite_rows(
    rows: Iterable[NormalizedRow],
    classifications: dict[str, str],
    fiat_coins: set[str],
) -> list[ClassifiedTx]:
    rows = list(rows)
    passthrough: list[NormalizedRow] = []
    pair_key_groups: dict[str, list[NormalizedRow]] = defaultdict(list)
    ts_groups: dict[str, list[NormalizedRow]] = defaultdict(list)

    for r in rows:
        cat = classifications.get(r.id, "")
        if cat not in LEG_CATEGORIES:
            passthrough.append(r)
            continue
        if r.pair_key:
            pair_key_groups[r.pair_key].append(r)
        else:
            ts_groups[r.timestamp].append(r)

    out: list[ClassifiedTx] = []
    for r in passthrough:
        out.append(_non_composite(r, classifications[r.id]))

    for pk, group in pair_key_groups.items():
        # For pair_key groups we bypass timestamp-based grouping; all members are
        # one logical composite transaction (a Crypto.com swap row).
        ts = group[0].timestamp
        out.extend(_pair_group(group, classifications, fiat_coins, ts))

    for ts, group in ts_groups.items():
        out.extend(_pair_group(group, classifications, fiat_coins, ts))

    out.sort(key=lambda t: t.timestamp)
    return out


def _pair_group(
    group: list[NormalizedRow],
    classifications: dict[str, str],
    fiat_coins: set[str],
    ts: str,
) -> list[ClassifiedTx]:
    buys = [r for r in group if classifications[r.id] == "trade_buy_leg"]
    sells = [r for r in group if classifications[r.id] == "trade_sell_leg"]
    fees = [r for r in group if classifications[r.id] == "fee_standalone"]
    swaps = [r for r in group if classifications[r.id] == "crypto_swap_leg"]

    results: list[ClassifiedTx] = []

    # Trade: one buy + one sell (+ optional fee)
    if len(buys) == 1 and len(sells) == 1:
        buy, sell = buys[0], sells[0]
        sell_is_fiat = sell.coin in fiat_coins
        buy_is_fiat = buy.coin in fiat_coins
        if sell_is_fiat and not buy_is_fiat:
            classified = "trade_buy"
            eur_value = abs(sell.change)
        elif buy_is_fiat and not sell_is_fiat:
            classified = "trade_sell"
            eur_value = abs(buy.change)
        else:
            classified = "crypto_swap"
            eur_value = None

        fee = None
        if fees:
            f = fees[0]
            fee = AssetAmount(coin=f.coin, amount=abs(f.change))

        tx = ClassifiedTx(
            id=buy.id,
            source=buy.source,
            timestamp=ts,
            raw_operation=buy.raw_operation,
            classified_as=classified,
            asset_in=AssetAmount(coin=buy.coin, amount=abs(buy.change)),
            asset_out=AssetAmount(coin=sell.coin, amount=abs(sell.change)),
            fee=fee,
            eur_value_at_time=Decimal(eur_value) if eur_value is not None else None,
            price_source="binance_csv_fiat_pair" if eur_value is not None else None,
            tax_event="acquisition" if classified == "trade_buy" else "disposal" if classified == "trade_sell" else None,
        )
        results.append(tx)
        return results

    # Swap: exactly two legs (one in, one out)
    if len(swaps) == 2:
        incoming = next((r for r in swaps if r.change > 0), None)
        outgoing = next((r for r in swaps if r.change < 0), None)
        if incoming and outgoing:
            # If both legs carry an exchange-reported EUR value, trust it.
            hint = None
            if incoming.eur_value_hint is not None and outgoing.eur_value_hint is not None:
                if incoming.eur_value_hint == outgoing.eur_value_hint:
                    hint = incoming.eur_value_hint
            tx = ClassifiedTx(
                id=incoming.id,
                source=incoming.source,
                timestamp=ts,
                raw_operation=incoming.raw_operation,
                classified_as="crypto_swap",
                asset_in=AssetAmount(coin=incoming.coin, amount=incoming.change),
                asset_out=AssetAmount(coin=outgoing.coin, amount=abs(outgoing.change)),
                eur_value_at_time=hint,
                price_source="exchange_reported" if hint is not None else None,
                tax_event="disposal",
            )
            results.append(tx)
            return results

    # Dust exchange: N negatives + 1 positive (typical "Small Assets Exchange BNB" pattern).
    # Emit N separate crypto_swap transactions; each disposes one negative leg and receives
    # an equal share of the positive leg. Exact split is arbitrary — tax-wise what matters
    # is that each disposal is priced at FMV and the total acquisition equals the positive amount.
    if len(swaps) >= 3:
        positives = [r for r in swaps if r.change > 0]
        negatives = [r for r in swaps if r.change < 0]
        if len(positives) == 1 and len(negatives) >= 2:
            pos = positives[0]
            n = len(negatives)
            per_share = pos.change / Decimal(n)
            accumulated = Decimal("0")
            for idx, neg in enumerate(negatives):
                # Give the last leg any rounding remainder to keep totals exact
                if idx == n - 1:
                    share = pos.change - accumulated
                else:
                    share = per_share
                    accumulated += share
                tx = ClassifiedTx(
                    id=neg.id,
                    source=neg.source,
                    timestamp=ts,
                    raw_operation=neg.raw_operation,
                    classified_as="crypto_swap",
                    asset_in=AssetAmount(coin=pos.coin, amount=share),
                    asset_out=AssetAmount(coin=neg.coin, amount=abs(neg.change)),
                    tax_event="disposal",
                )
                tx.notes.append("dust_exchange_split")
                results.append(tx)
            return results

    # Orphan legs: emit each classified by sign so tax treatment is correct (acquisition
    # for positive, disposal for negative), without the misleading 'airdrop' label.
    for r in group:
        cat = classifications[r.id]
        if cat.endswith("_leg") and cat != "fee_standalone":
            results.append(_orphan_leg(r))
        else:
            results.append(_non_composite(r, cat))
    return results
