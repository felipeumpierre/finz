from decimal import Decimal
from scripts.parsers.binance import parse_binance_csv, is_binance_csv

def test_detects_binance_header(fixtures_dir):
    assert is_binance_csv(fixtures_dir / "binance_sample.csv") is True

def test_parses_rows(fixtures_dir):
    rows = parse_binance_csv(fixtures_dir / "binance_sample.csv")
    assert len(rows) == 9
    first = rows[0]
    assert first.source == "binance"
    assert first.raw_operation == "Deposit"
    assert first.coin == "XRP"
    assert first.change == Decimal("199")
    assert first.account == "Spot"

def test_ids_are_stable_and_unique(fixtures_dir):
    rows = parse_binance_csv(fixtures_dir / "binance_sample.csv")
    ids = [r.id for r in rows]
    assert len(set(ids)) == len(ids)
    assert all(i.startswith("bnc-") for i in ids)

def test_timestamp_iso_with_tz(fixtures_dir):
    rows = parse_binance_csv(fixtures_dir / "binance_sample.csv")
    assert rows[0].timestamp == "2021-05-12T21:18:45+02:00"

def test_change_preserved_as_decimal_string(fixtures_dir):
    rows = parse_binance_csv(fixtures_dir / "binance_sample.csv")
    fee = next(r for r in rows if r.raw_operation == "Fee")
    assert fee.change == Decimal("-0.00000978")

def test_rejects_non_binance_file(tmp_path):
    bad = tmp_path / "x.csv"
    bad.write_text("a,b,c\n1,2,3\n")
    assert is_binance_csv(bad) is False
