"""Binance Transaction History CSV parser.

Binance exports use this header (tz is embedded in the filename, not the CSV):
  User ID,Time,Account,Operation,Coin,Change,Remark

Time is 'YY-MM-DD HH:MM:SS' in Europe/Berlin (the export declared tz).
"""
from __future__ import annotations

import csv
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

from scripts.schemas import NormalizedRow

BINANCE_HEADER = ["User ID", "Time", "Account", "Operation", "Coin", "Change", "Remark"]
BERLIN = ZoneInfo("Europe/Berlin")


def is_binance_csv(path: Path) -> bool:
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return False
    return header == BINANCE_HEADER


def _parse_time(s: str) -> str:
    dt = datetime.strptime(s, "%y-%m-%d %H:%M:%S").replace(tzinfo=BERLIN)
    return dt.isoformat()


def parse_binance_csv(path: Path) -> list[NormalizedRow]:
    out: list[NormalizedRow] = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            out.append(NormalizedRow(
                id=f"bnc-{idx:06d}",
                source="binance",
                timestamp=_parse_time(row["Time"]),
                raw_operation=row["Operation"],
                coin=row["Coin"],
                change=Decimal(row["Change"]),
                account=row["Account"],
                remark=row.get("Remark", "") or "",
            ))
    return out
