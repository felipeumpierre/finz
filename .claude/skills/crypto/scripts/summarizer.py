"""Assemble crypto-ledger.json (full) and crypto-summary.json (digest) from pipeline outputs."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Iterable

from scripts.schemas import (
    ClassifiedTx, CryptoLedger, CryptoSummary, Disposal, HoldingsSummary,
    IncomeEvent, Issue, Lot, Source, YearlyTaxSummary, CrossExchangeTransfer,
)

NOW = lambda: datetime.now(timezone.utc).isoformat()


def _dec_str(x: Decimal) -> str:
    return format(x, "f")


def build_ledger(
    sources: list[Source],
    transactions: list[ClassifiedTx],
    lots: list[Lot],
    disposals: list[Disposal],
    incomes: list[IncomeEvent],
    transfers: list[CrossExchangeTransfer],
    issues: list[Issue],
) -> CryptoLedger:
    return CryptoLedger(
        schema_version=1,
        last_updated=NOW(),
        sources=sources,
        transactions=transactions,
        lots=lots,
        disposals=disposals,
        income_events=incomes,
        cross_exchange_transfers=transfers,
        issues=issues,
    )


def _current_holdings(lots: list[Lot]) -> list[HoldingsSummary]:
    by_coin: dict[str, list[Lot]] = defaultdict(list)
    for lot in lots:
        if lot.amount_remaining > 0:
            by_coin[lot.coin].append(lot)

    now = datetime.now(timezone.utc)
    out: list[HoldingsSummary] = []
    for coin, lots_ in by_coin.items():
        total = sum((l.amount_remaining for l in lots_), Decimal("0"))
        tax_free = sum(
            (l.amount_remaining for l in lots_
             if datetime.fromisoformat(l.holding_period_ends) <= now),
            Decimal("0"),
        )
        taxable = total - tax_free
        future = [l.holding_period_ends for l in lots_
                  if datetime.fromisoformat(l.holding_period_ends) > now]
        next_milestone = min(future) if future else None
        out.append(HoldingsSummary(
            coin=coin,
            amount=total,
            lots_summary={
                "tax_free_now": _dec_str(tax_free),
                "taxable_now": _dec_str(taxable),
                "next_milestone_date": next_milestone,
            },
        ))
    out.sort(key=lambda h: h.coin)
    return out


def build_summary(
    ledger: CryptoLedger,
    yearly: dict[str, YearlyTaxSummary],
    decisions_pending: int,
    decisions_resolved: int,
) -> CryptoSummary:
    counts = Counter(t.classified_as for t in ledger.transactions)
    rows_binance = next((s.rows for s in ledger.sources if s.exchange == "binance"), 0)
    rows_coinbase = next((s.rows for s in ledger.sources if s.exchange == "coinbase"), 0)

    holdings = _current_holdings(ledger.lots)

    years_needing = [int(y) for y, s in yearly.items() if s.needs_correction]
    estimated_back = sum((s.estimated_back_tax_eur or Decimal("0") for s in yearly.values()), Decimal("0"))
    estimated_int = sum((s.estimated_interest_eur or Decimal("0") for s in yearly.values()), Decimal("0"))

    optimizations: list[dict] = []
    for y, s in yearly.items():
        if not s.needs_correction:
            optimizations.append({"kind": "year_needs_no_correction", "year": int(y), "reason": s.reason})
    for h in holdings:
        if h.lots_summary.get("next_milestone_date"):
            optimizations.append({
                "kind": "holding_period_milestone",
                "coin": h.coin,
                "next_tax_free_date": h.lots_summary["next_milestone_date"],
            })

    return CryptoSummary(
        schema_version=1,
        generated_at=NOW(),
        ingest_stats={
            "rows_binance": rows_binance,
            "rows_coinbase": rows_coinbase,
            "transactions_after_pairing": len(ledger.transactions),
            "classified_counts": dict(counts),
        },
        yearly_tax_summary=yearly,
        current_holdings=holdings,
        issues=ledger.issues,
        decisions_pending=decisions_pending,
        decisions_resolved=decisions_resolved,
        totals_across_years={
            "estimated_back_tax_eur": _dec_str(estimated_back),
            "estimated_interest_eur": _dec_str(estimated_int),
            "years_needing_correction": sorted(years_needing),
        },
        optimizations=optimizations,
    )


def write_json(path: Path, model) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(model.model_dump_json(indent=2, by_alias=True))
