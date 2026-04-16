"""Unit tests for the Crypto.com parser."""
from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import pytest

from scripts.parsers.crypto_com import is_crypto_com_csv, parse_crypto_com_csv

FIXTURE = Path(__file__).parent / "fixtures" / "crypto_com" / "sample.csv"
CDC_HEADER = (
    "Timestamp (UTC),Transaction Description,Currency,Amount,To Currency,"
    "To Amount,Native Currency,Native Amount,Native Amount (in USD),"
    "Transaction Kind,Transaction Hash"
)


def _write(tmp: Path, body: str) -> Path:
    p = tmp / "t.csv"
    p.write_text(body)
    return p


def test_is_crypto_com_csv_positive(tmp_path):
    p = _write(tmp_path, CDC_HEADER + "\n")
    assert is_crypto_com_csv(p) is True


def test_is_crypto_com_csv_rejects_binance(tmp_path):
    p = _write(tmp_path, "User ID,Time,Account,Operation,Coin,Change,Remark\n")
    assert is_crypto_com_csv(p) is False


def test_is_crypto_com_csv_rejects_empty(tmp_path):
    p = _write(tmp_path, "")
    assert is_crypto_com_csv(p) is False


PURCHASE_ROW = (
    CDC_HEADER + "\n"
    "2021-04-14 05:58:36,Bought XRP,XRP,150.0,,,EUR,243.65,287.9662339565,crypto_purchase,\n"
)


def test_parse_crypto_purchase(tmp_path):
    p = _write(tmp_path, PURCHASE_ROW)
    rows = parse_crypto_com_csv(p)
    assert len(rows) == 1
    r = rows[0]
    assert r.source == "crypto_com"
    assert r.raw_operation == "crypto_purchase"
    assert r.coin == "XRP"
    assert r.change == Decimal("150.0")
    assert r.eur_value_hint == Decimal("243.65")
    assert r.pair_key is None
    assert r.timestamp.startswith("2021-04-14T05:58:36")
    assert r.timestamp.endswith("+00:00")


WITHDRAW_ROW = (
    CDC_HEADER + "\n"
    "2021-05-09 15:37:24,Withdraw XRP,XRP,-200.0,,,EUR,245.42,290.058,crypto_withdrawal,HASHABC\n"
)


def test_parse_crypto_withdrawal(tmp_path):
    p = _write(tmp_path, WITHDRAW_ROW)
    rows = parse_crypto_com_csv(p)
    assert len(rows) == 1
    r = rows[0]
    assert r.coin == "XRP"
    assert r.change == Decimal("-200.0")
    assert r.eur_value_hint == Decimal("245.42")
    assert "HASHABC" in r.remark
    assert r.pair_key is None


SWAP_ROW = (
    CDC_HEADER + "\n"
    "2023-10-22 18:32:04,USDT > APT,USDT,-8.566829,APT,1.392,EUR,7.907,9.345,crypto_exchange,\n"
)


def test_parse_crypto_exchange_emits_two_legs(tmp_path):
    p = _write(tmp_path, SWAP_ROW)
    rows = parse_crypto_com_csv(p)
    assert len(rows) == 2
    out_leg = next(r for r in rows if r.change < 0)
    in_leg = next(r for r in rows if r.change > 0)
    assert out_leg.coin == "USDT"
    assert out_leg.change == Decimal("-8.566829")
    assert in_leg.coin == "APT"
    assert in_leg.change == Decimal("1.392")
    assert out_leg.pair_key is not None
    assert out_leg.pair_key == in_leg.pair_key
    assert out_leg.eur_value_hint == Decimal("7.907")
    assert in_leg.eur_value_hint == Decimal("7.907")
    assert out_leg.timestamp == in_leg.timestamp


DEPOSIT_ROW = (
    CDC_HEADER + "\n"
    "2022-01-15 10:00:00,Deposit BTC,BTC,0.5,,,EUR,20000,22000,crypto_deposit,TXHASH1\n"
)
EARN_ROW = (
    CDC_HEADER + "\n"
    "2022-02-01 00:00:00,Earn Interest,CRO,1.234,,,EUR,0.50,0.55,crypto_earn_interest_paid,\n"
)
UNKNOWN_ROW = (
    CDC_HEADER + "\n"
    "2022-03-01 00:00:00,Mystery,FOO,5,,,EUR,10,11,supercharger_deposit,\n"
)
NON_EUR_ROW = (
    CDC_HEADER + "\n"
    "2022-04-01 00:00:00,Bought XRP,XRP,10,,,USD,8,8,crypto_purchase,\n"
)


def test_parse_crypto_deposit(tmp_path):
    rows = parse_crypto_com_csv(_write(tmp_path, DEPOSIT_ROW))
    assert len(rows) == 1
    assert rows[0].change == Decimal("0.5") and rows[0].eur_value_hint == Decimal("20000")


def test_parse_earn_interest(tmp_path):
    rows = parse_crypto_com_csv(_write(tmp_path, EARN_ROW))
    assert len(rows) == 1
    assert rows[0].change == Decimal("1.234")
    assert rows[0].raw_operation == "crypto_earn_interest_paid"


def test_parse_unknown_kind_passes_through(tmp_path):
    rows = parse_crypto_com_csv(_write(tmp_path, UNKNOWN_ROW))
    assert len(rows) == 1
    assert rows[0].raw_operation == "supercharger_deposit"


def test_parse_non_eur_native_drops_hint(tmp_path):
    rows = parse_crypto_com_csv(_write(tmp_path, NON_EUR_ROW))
    assert len(rows) == 1
    assert rows[0].eur_value_hint is None
