from decimal import Decimal
from scripts.schemas import ClassifiedTx, AssetAmount
from scripts.transfer_matcher import match_cross_exchange_transfers, TransferMatch

def _tx(id_, source, cat, coin, amt, ts):
    io = AssetAmount(coin=coin, amount=Decimal(amt))
    return ClassifiedTx(
        id=id_, source=source, timestamp=ts,
        raw_operation="Deposit" if cat == "external_in" else "Withdraw",
        classified_as=cat,
        asset_in=io if cat == "external_in" else None,
        asset_out=io if cat == "external_out" else None,
    )

def test_matches_exact_amount_within_48h():
    txs = [
        _tx("cb-1", "coinbase", "external_out", "XRP", "199", "2021-05-12T20:50:00+00:00"),
        _tx("bnc-1", "binance", "external_in", "XRP", "199", "2021-05-12T19:18:45+00:00"),
    ]
    matches = match_cross_exchange_transfers(txs)
    assert len(matches.matches) == 1
    m = matches.matches[0]
    assert m.from_tx_id == "cb-1"
    assert m.to_tx_id == "bnc-1"
    assert m.confidence > 0.9

def test_matches_with_small_amount_delta_under_half_percent():
    txs = [
        _tx("cb-1", "coinbase", "external_out", "BTC", "1.0", "2021-05-12T00:00:00+00:00"),
        _tx("bnc-1", "binance", "external_in", "BTC", "0.997", "2021-05-12T01:00:00+00:00"),  # 0.3% fee
    ]
    matches = match_cross_exchange_transfers(txs)
    assert len(matches.matches) == 1

def test_no_match_over_48h():
    txs = [
        _tx("cb-1", "coinbase", "external_out", "BTC", "1.0", "2021-05-10T00:00:00+00:00"),
        _tx("bnc-1", "binance", "external_in", "BTC", "1.0", "2021-05-15T00:00:00+00:00"),
    ]
    matches = match_cross_exchange_transfers(txs)
    assert matches.matches == []
    assert len(matches.unmatched_incoming) == 1

def test_ambiguous_when_multiple_candidates():
    txs = [
        _tx("cb-1", "coinbase", "external_out", "BTC", "1.0", "2021-05-12T00:00:00+00:00"),
        _tx("cb-2", "coinbase", "external_out", "BTC", "1.0", "2021-05-12T00:30:00+00:00"),
        _tx("bnc-1", "binance", "external_in", "BTC", "1.0", "2021-05-12T01:00:00+00:00"),
    ]
    matches = match_cross_exchange_transfers(txs)
    assert len(matches.ambiguous) == 1

def test_amount_delta_over_1pct_no_match():
    txs = [
        _tx("cb-1", "coinbase", "external_out", "BTC", "1.0", "2021-05-12T00:00:00+00:00"),
        _tx("bnc-1", "binance", "external_in", "BTC", "1.05", "2021-05-12T01:00:00+00:00"),
    ]
    matches = match_cross_exchange_transfers(txs)
    assert matches.matches == []
