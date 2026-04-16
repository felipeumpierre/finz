"""End-to-end: ingest the Crypto.com sample CSV and verify ledger shape."""
from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path

import pytest

from scripts.crypto_ingest import run

FIXTURE = Path(__file__).parent / "fixtures" / "crypto_com" / "sample.csv"


def test_cryptocom_sample_end_to_end(tmp_path, monkeypatch):
    # Prevent any network call via PriceResolver — all rows should use eur_value_hint.
    from scripts import price_resolver as pr
    def _no_net(*a, **kw):
        raise AssertionError("PriceResolver should not be called when eur_value_hint is present")
    monkeypatch.setattr(pr.PriceResolver, "_fetch_from_network", _no_net, raising=False)

    ws = tmp_path
    (ws / "cache" / "prices").mkdir(parents=True)
    run(binance_paths=[], coinbase_paths=[], cryptocom_paths=[FIXTURE], workspace=ws)

    ledger = json.loads((ws / "crypto-ledger.json").read_text())
    summary = json.loads((ws / "crypto-summary.json").read_text())

    # 10 CSV rows -> 4 swaps + 4 purchases + 2 withdrawals = 10 ClassifiedTx
    assert len(ledger["transactions"]) == 10

    # 4 swap disposals + 2 withdrawal disposals (SHIB, XRP) = 6 disposals
    assert len(ledger["disposals"]) == 6

    # All lots from trade_buy must use exchange_reported cost basis
    buy_lots = [l for l in ledger["lots"] if l["cost_basis_source"] == "exchange_reported"]
    assert len(buy_lots) >= 4  # XRP x2, DOGE, SHIB purchases

    # Years with activity
    years = set(summary["yearly_tax_summary"].keys())
    assert {"2021", "2023"}.issubset(years)

    # No income events in this fixture
    assert ledger["income_events"] == []
