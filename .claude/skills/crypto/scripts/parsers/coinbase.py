"""Coinbase Transaction History CSV parser.

Header (fields that matter):
  ID, Timestamp, Transaction Type, Asset, Quantity Transacted, ...

Timestamp is ISO 8601 UTC. Send/Sell signs are inferred from transaction type.
"""
from __future__ import annotations

import csv
from decimal import Decimal
from datetime import datetime
from pathlib import Path

from scripts.schemas import NormalizedRow

REQUIRED_HEADERS = {"ID", "Timestamp", "Transaction Type", "Asset", "Quantity Transacted"}
NEGATIVE_OPS = {"Send", "Sell", "Withdrawal", "Convert (from)", "Paid"}


def _find_header_row(path: Path) -> int:
    """Return the 0-based line index of the actual column header row.

    Coinbase exports have 0–2 preamble rows (e.g. 'Transactions', 'User,...')
    before the real header.  We scan up to 5 rows to find the one that
    contains all REQUIRED_HEADERS.
    """
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i >= 5:
                break
            if REQUIRED_HEADERS.issubset(set(row)):
                return i
    return -1


def is_coinbase_csv(path: Path) -> bool:
    return _find_header_row(path) >= 0


def _normalize_iso(s: str) -> str:
    s = s.strip().replace("Z", "+00:00").replace(" UTC", "+00:00")
    dt = datetime.fromisoformat(s)
    return dt.isoformat()


def parse_coinbase_csv(path: Path) -> list[NormalizedRow]:
    header_row = _find_header_row(path)
    out: list[NormalizedRow] = []
    with open(path, newline="", encoding="utf-8") as f:
        for _ in range(header_row):
            f.readline()  # skip preamble lines
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            qty = Decimal(row["Quantity Transacted"])
            op = row["Transaction Type"]
            if op in NEGATIVE_OPS:
                qty = -qty
            out.append(NormalizedRow(
                id=f"cb-{idx:06d}",
                source="coinbase",
                timestamp=_normalize_iso(row["Timestamp"]),
                raw_operation=op,
                coin=row["Asset"],
                change=qty,
                account=None,
                remark=row.get("Notes", "") or "",
            ))
    return out
