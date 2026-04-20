from decimal import Decimal
from scripts.parsers.coinbase import parse_coinbase_csv, is_coinbase_csv

def test_detects_coinbase_header(fixtures_dir):
    assert is_coinbase_csv(fixtures_dir / "coinbase_sample.csv") is True

def test_parses_buy(fixtures_dir):
    rows = parse_coinbase_csv(fixtures_dir / "coinbase_sample.csv")
    buy = next(r for r in rows if r.raw_operation == "Buy")
    assert buy.coin == "BTC"
    assert buy.change == Decimal("0.01")
    assert buy.source == "coinbase"

def test_send_preserved_as_negative(fixtures_dir):
    rows = parse_coinbase_csv(fixtures_dir / "coinbase_sample.csv")
    send = next(r for r in rows if r.raw_operation == "Send")
    assert send.change == Decimal("-199.00000000")

def test_receive_preserved_as_positive(fixtures_dir):
    rows = parse_coinbase_csv(fixtures_dir / "coinbase_sample.csv")
    recv = next(r for r in rows if r.raw_operation == "Receive")
    assert recv.change == Decimal("0.5")

def test_sell_preserved_as_negative(fixtures_dir):
    rows = parse_coinbase_csv(fixtures_dir / "coinbase_sample.csv")
    sell = next(r for r in rows if r.raw_operation == "Sell")
    assert sell.change == Decimal("-0.005")

def test_ids_have_cb_prefix(fixtures_dir):
    rows = parse_coinbase_csv(fixtures_dir / "coinbase_sample.csv")
    assert all(r.id.startswith("cb-") for r in rows)

def test_timestamp_preserves_utc(fixtures_dir):
    rows = parse_coinbase_csv(fixtures_dir / "coinbase_sample.csv")
    assert rows[0].timestamp.endswith("+00:00") or rows[0].timestamp.endswith("Z")
