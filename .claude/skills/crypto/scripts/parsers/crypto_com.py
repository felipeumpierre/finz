"""Crypto.com Transaction History CSV parser.

Timestamps are UTC and stored as ISO 8601 with offset.
Swap rows (Transaction Kind = crypto_exchange) pack both legs into a single CSV row;
we emit two NormalizedRows sharing a pair_key so pairing.py collapses them.

When Native Currency == EUR, Native Amount is attached as `eur_value_hint`
(trusted as exchange-reported cost basis).
"""
from __future__ import annotations

import csv
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

from scripts.schemas import NormalizedRow

CDC_HEADER = [
    "Timestamp (UTC)", "Transaction Description", "Currency", "Amount",
    "To Currency", "To Amount", "Native Currency", "Native Amount",
    "Native Amount (in USD)", "Transaction Kind", "Transaction Hash",
]
UTC = ZoneInfo("UTC")


def is_crypto_com_csv(path: Path) -> bool:
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            header = next(reader, None)
    except (FileNotFoundError, StopIteration, OSError):
        return False
    return header == CDC_HEADER


def _parse_time(s: str) -> str:
    dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)
    return dt.isoformat()


def _eur_hint(row: dict) -> Decimal | None:
    if row.get("Native Currency") == "EUR" and row.get("Native Amount"):
        try:
            return Decimal(row["Native Amount"])
        except Exception:
            return None
    return None


def parse_crypto_com_csv(path: Path) -> list[NormalizedRow]:
    out: list[NormalizedRow] = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            if not row.get("Timestamp (UTC)"):
                continue  # skip blank trailing lines
            kind = row["Transaction Kind"]
            ts = _parse_time(row["Timestamp (UTC)"])
            rid = f"cdc-{idx:06d}"
            hint = _eur_hint(row)

            if kind == "crypto_purchase":
                out.append(NormalizedRow(
                    id=rid, source="crypto_com", timestamp=ts,
                    raw_operation=kind, coin=row["Currency"],
                    change=Decimal(row["Amount"]),
                    account=None,
                    remark=row.get("Transaction Description", "") or "",
                    eur_value_hint=hint,
                ))
                continue

            if kind == "crypto_withdrawal":
                amount = Decimal(row["Amount"])
                if amount > 0:
                    amount = -amount
                tx_hash = row.get("Transaction Hash", "") or ""
                desc = row.get("Transaction Description", "") or ""
                remark = f"{desc} tx:{tx_hash}".strip() if tx_hash else desc
                out.append(NormalizedRow(
                    id=rid, source="crypto_com", timestamp=ts,
                    raw_operation=kind, coin=row["Currency"],
                    change=amount, account=None, remark=remark,
                    eur_value_hint=hint,
                ))
                continue

            if kind == "crypto_exchange":
                pk = f"cdc-swap-{idx:06d}"
                # outgoing leg
                out_amount = Decimal(row["Amount"])
                if out_amount > 0:
                    out_amount = -out_amount
                out.append(NormalizedRow(
                    id=f"{rid}-out", source="crypto_com", timestamp=ts,
                    raw_operation=kind, coin=row["Currency"],
                    change=out_amount, account=None,
                    remark=row.get("Transaction Description", "") or "",
                    eur_value_hint=hint, pair_key=pk,
                ))
                # incoming leg
                in_amount = Decimal(row["To Amount"])
                if in_amount < 0:
                    in_amount = -in_amount
                out.append(NormalizedRow(
                    id=f"{rid}-in", source="crypto_com", timestamp=ts,
                    raw_operation=kind, coin=row["To Currency"],
                    change=in_amount, account=None,
                    remark=row.get("Transaction Description", "") or "",
                    eur_value_hint=hint, pair_key=pk,
                ))
                continue

            # Generic single-row emit for known and unknown kinds alike.
            # The classifier (via taxonomy YAML) decides tax treatment;
            # unknown kinds fall through to `airdrop_pending_review`.
            amount_str = row.get("Amount") or "0"
            try:
                amount = Decimal(amount_str)
            except Exception:
                amount = Decimal("0")
            out.append(NormalizedRow(
                id=rid, source="crypto_com", timestamp=ts,
                raw_operation=kind, coin=row["Currency"],
                change=amount, account=None,
                remark=row.get("Transaction Description", "") or "",
                eur_value_hint=hint,
            ))
    return out
