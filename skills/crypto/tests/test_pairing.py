from decimal import Decimal
from scripts.schemas import NormalizedRow
from scripts.pairing import pair_composite_rows

def _r(id_, op, coin, change, ts="2021-05-13T23:00:23+02:00", src="binance"):
    return NormalizedRow(
        id=id_, source=src, timestamp=ts, raw_operation=op,
        coin=coin, change=Decimal(change), account="Spot",
    )

def test_pairs_binance_buy_sell_fee_into_one_trade():
    rows = [
        _r("bnc-1", "Fee", "BTC", "-0.00000978"),
        _r("bnc-2", "Buy", "BTC", "0.009783"),
        _r("bnc-3", "Sell", "EUR", "-399.98"),
    ]
    classifications = {"bnc-1": "fee_standalone", "bnc-2": "trade_buy_leg", "bnc-3": "trade_sell_leg"}
    paired = pair_composite_rows(rows, classifications, fiat_coins={"EUR"})
    assert len(paired) == 1
    tx = paired[0]
    assert tx.classified_as == "trade_buy"
    assert tx.asset_in.coin == "BTC"
    assert tx.asset_in.amount == Decimal("0.009783")
    assert tx.asset_out.coin == "EUR"
    assert tx.asset_out.amount == Decimal("399.98")
    assert tx.fee.coin == "BTC"
    assert tx.fee.amount == Decimal("0.00000978")
    assert tx.eur_value_at_time == Decimal("399.98")

def test_pairs_binance_convert_both_crypto_legs():
    rows = [
        _r("bnc-1", "Binance Convert", "BNB", "0.05"),
        _r("bnc-2", "Binance Convert", "BTC", "-0.001"),
    ]
    classifications = {"bnc-1": "crypto_swap_leg", "bnc-2": "crypto_swap_leg"}
    paired = pair_composite_rows(rows, classifications, fiat_coins={"EUR"})
    assert len(paired) == 1
    tx = paired[0]
    assert tx.classified_as == "crypto_swap"
    assert tx.asset_in.coin == "BNB"
    assert tx.asset_out.coin == "BTC"

def test_passes_through_non_composite_rows():
    rows = [_r("bnc-1", "Simple Earn Flexible Interest", "XRP", "0.1")]
    classifications = {"bnc-1": "income_receipt"}
    paired = pair_composite_rows(rows, classifications, fiat_coins={"EUR"})
    assert len(paired) == 1
    tx = paired[0]
    assert tx.classified_as == "income_receipt"
    assert tx.asset_in.coin == "XRP"
    assert tx.asset_in.amount == Decimal("0.1")

def test_unpaired_leg_becomes_issue_input():
    rows = [_r("bnc-1", "Buy", "BTC", "0.1")]
    classifications = {"bnc-1": "trade_buy_leg"}
    paired = pair_composite_rows(rows, classifications, fiat_coins={"EUR"})
    assert len(paired) == 1
    assert "unpaired_trade_leg" in paired[0].notes
