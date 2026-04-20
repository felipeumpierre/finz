"""Tests for pair_key-based grouping and eur_value_hint propagation."""
from __future__ import annotations

from decimal import Decimal
from scripts.pairing import pair_composite_rows
from scripts.schemas import NormalizedRow


def _leg(rid, coin, change, pk, ts="2023-10-22T18:32:04+00:00", hint=Decimal("7.907")):
    return NormalizedRow(
        id=rid, source="crypto_com", timestamp=ts, raw_operation="crypto_exchange",
        coin=coin, change=Decimal(str(change)), eur_value_hint=hint, pair_key=pk,
    )


def test_pair_key_collapses_two_legs_into_one_swap():
    rows = [
        _leg("cdc-000000-out", "USDT", "-8.566829", "cdc-swap-000000"),
        _leg("cdc-000000-in",  "APT",  "1.392",     "cdc-swap-000000"),
    ]
    classifications = {r.id: "crypto_swap_leg" for r in rows}
    out = pair_composite_rows(rows, classifications, fiat_coins={"EUR", "USD"})
    assert len(out) == 1
    tx = out[0]
    assert tx.classified_as == "crypto_swap"
    assert tx.asset_out.coin == "USDT"
    assert tx.asset_out.amount == Decimal("8.566829")
    assert tx.asset_in.coin == "APT"
    assert tx.asset_in.amount == Decimal("1.392")
    # eur_value_hint from the legs must flow through to eur_value_at_time
    assert tx.eur_value_at_time == Decimal("7.907")


def test_pair_key_different_keys_do_not_cross_mix():
    rows = [
        _leg("a-out", "USDT", "-1", "swap-A"),
        _leg("a-in",  "APT",   "1", "swap-A"),
        _leg("b-out", "CRO",  "-2", "swap-B", ts="2023-10-22T18:05:59+00:00"),
        _leg("b-in",  "USDT",  "2", "swap-B", ts="2023-10-22T18:05:59+00:00"),
    ]
    classifications = {r.id: "crypto_swap_leg" for r in rows}
    out = pair_composite_rows(rows, classifications, fiat_coins={"EUR", "USD"})
    assert len(out) == 2
