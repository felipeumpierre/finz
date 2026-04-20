"""Match Coinbase Withdraw ↔ Binance Deposit into cross-exchange transfers.

Criteria:
  - same coin
  - amount within ±0.5% (covers network fees)
  - from.timestamp within [to.timestamp - 48h, to.timestamp]
  - single unambiguous candidate
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Iterable

from scripts.schemas import ClassifiedTx

MAX_AMOUNT_DELTA = Decimal("0.02")     # 2% — covers network fees, slippage, rounding
MAX_TIME_DELTA = timedelta(days=7)     # cross-exchange transfers can take days to finalize


@dataclass
class TransferMatch:
    from_tx_id: str
    to_tx_id: str
    confidence: float


@dataclass
class MatchResult:
    matches: list[TransferMatch] = field(default_factory=list)
    ambiguous: list[dict] = field(default_factory=list)
    unmatched_incoming: list[str] = field(default_factory=list)


def _parse(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


def _amount_delta_pct(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        return Decimal("Infinity")
    return abs(a - b) / b


def match_cross_exchange_transfers(txs: Iterable[ClassifiedTx]) -> MatchResult:
    incoming = [t for t in txs if t.classified_as == "external_in"]
    outgoing = [t for t in txs if t.classified_as == "external_out"]
    result = MatchResult()
    used_out: set[str] = set()

    for i in incoming:
        if i.asset_in is None:
            result.unmatched_incoming.append(i.id)
            continue
        coin_in = i.asset_in.coin
        amt_in = i.asset_in.amount
        t_in = _parse(i.timestamp)

        candidates = []
        for o in outgoing:
            if o.id in used_out:
                continue
            if o.asset_out is None:
                continue
            if o.asset_out.coin != coin_in:
                continue
            t_out = _parse(o.timestamp)
            time_diff = abs(t_in - t_out)
            if time_diff > MAX_TIME_DELTA:
                continue
            delta = _amount_delta_pct(o.asset_out.amount, amt_in)
            if delta > MAX_AMOUNT_DELTA:
                continue
            time_score = 1.0 - (time_diff.total_seconds() / MAX_TIME_DELTA.total_seconds())
            amt_score = 1.0 - float(delta) / float(MAX_AMOUNT_DELTA)
            confidence = 0.5 * time_score + 0.5 * amt_score
            candidates.append((o, confidence))

        if len(candidates) == 1:
            o, conf = candidates[0]
            result.matches.append(TransferMatch(from_tx_id=o.id, to_tx_id=i.id, confidence=conf))
            used_out.add(o.id)
        elif len(candidates) > 1:
            result.ambiguous.append({
                "incoming_id": i.id,
                "candidates": [c[0].id for c in candidates],
            })
        else:
            result.unmatched_incoming.append(i.id)

    return result
