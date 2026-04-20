import json
from decimal import Decimal
from pathlib import Path
import scripts.crypto_ingest as ci
from scripts.price_resolver import PriceResolver, SYMBOL_TO_ID

class FakeHttp:
    """CoinGecko stub with deterministic prices."""
    PRICES = {("BTC", "2021-08-01"): 35000, ("BTC", "2021-07-01"): 30000, ("ETH", "2021-05-01"): 2000, ("ETH", "2022-06-01"): 1500}
    def get(self, url, params=None, timeout=None):
        coin_id = url.split("/")[-2]
        coin = next((k for k, v in SYMBOL_TO_ID.items() if v == coin_id), coin_id.upper())
        d = params["date"]  # DD-MM-YYYY
        parts = d.split("-")
        iso_date = f"{parts[2]}-{parts[1]}-{parts[0]}"
        price = self.PRICES.get((coin, iso_date), 1000)
        class R:
            status_code = 200
            def raise_for_status(self): pass
            def json(self_): return {"market_data": {"current_price": {"eur": price}}}
        return R()

def test_end_to_end_mini(tmp_path, fixtures_dir, monkeypatch):
    ws = tmp_path / "workspace"
    ws.mkdir()
    import httpx
    monkeypatch.setattr(httpx, "Client", lambda *a, **kw: FakeHttp())
    ci._collected_disposals = []
    ci.run(binance_paths=[fixtures_dir / "binance_mini.csv"],
           coinbase_paths=[fixtures_dir / "coinbase_mini.csv"], workspace=ws)
    ledger = json.loads((ws / "crypto-ledger.json").read_text())
    summary = json.loads((ws / "crypto-summary.json").read_text())
    assert len(ledger["sources"]) == 2
    assert summary["ingest_stats"]["transactions_after_pairing"] >= 6
    assert len(ledger["disposals"]) == 2
    btc_disposal = next(d for d in ledger["disposals"] if d["coin"] == "BTC")
    assert btc_disposal["tax_treatment"] == "tax_free_long_term"
    eth_disposal = next(d for d in ledger["disposals"] if d["coin"] == "ETH")
    assert eth_disposal["tax_treatment"] == "tax_free_long_term"
    assert len(ledger["income_events"]) == 1
    assert ledger["income_events"][0]["paragraph"] == "§22 Nr.3 EStG"
