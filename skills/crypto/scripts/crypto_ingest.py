"""Crypto ingest pipeline CLI.

Usage:
  python -m scripts.crypto_ingest --mode=initial \
    --binance workspace/resources/crypto/binance/*.csv \
    --coinbase workspace/resources/crypto/coinbase/*.csv \
    --workspace workspace/

  python -m scripts.crypto_ingest --mode=apply-decisions --workspace workspace/
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

import httpx

from scripts.aggregator import aggregate_yearly
from scripts.classifier import Classifier
from scripts.fifo import AcquisitionEvent, DisposalEvent, FifoEngine
from scripts.pairing import pair_composite_rows
from scripts.parsers.binance import parse_binance_csv, is_binance_csv
from scripts.parsers.coinbase import parse_coinbase_csv, is_coinbase_csv
from scripts.parsers.crypto_com import parse_crypto_com_csv, is_crypto_com_csv
from scripts.price_resolver import PriceResolver
from scripts.schemas import (
    ClassifiedTx, CrossExchangeTransfer, Decisions, IncomeEvent, Issue, Source,
)
from scripts.summarizer import build_ledger, build_summary, write_json
from scripts.transfer_matcher import match_cross_exchange_transfers


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_decisions(workspace: Path) -> Decisions:
    p = workspace / "crypto-decisions.json"
    if p.exists():
        return Decisions.model_validate_json(p.read_text())
    return Decisions()


def _save_decisions(workspace: Path, d: Decisions) -> None:
    (workspace / "crypto-decisions.json").write_text(d.model_dump_json(indent=2))


def run(binance_paths: list[Path], coinbase_paths: list[Path],
        cryptocom_paths: list[Path], workspace: Path) -> None:
    global _collected_disposals
    _collected_disposals = []

    classifier = Classifier.load_default()
    decisions = _load_decisions(workspace)
    cache_dir = workspace / "cache" / "prices"
    prices = PriceResolver(cache_dir=cache_dir, http_client=httpx.Client(),
                           manual_prices=decisions.manual_prices)

    # 1. Parse + track sources
    sources: list[Source] = []
    rows = []
    for p in binance_paths:
        if not is_binance_csv(p):
            print(f"Skipping non-Binance file: {p}", file=sys.stderr)
            continue
        parsed = parse_binance_csv(p)
        rows.extend(parsed)
        sources.append(Source(
            exchange="binance", file=str(p), sha256=_sha256(p),
            rows=len(parsed), ingested_at=datetime.now(timezone.utc).isoformat(),
            range={"from": parsed[0].timestamp if parsed else "", "to": parsed[-1].timestamp if parsed else ""},
        ))
    for p in coinbase_paths:
        if not is_coinbase_csv(p):
            continue
        parsed = parse_coinbase_csv(p)
        rows.extend(parsed)
        sources.append(Source(
            exchange="coinbase", file=str(p), sha256=_sha256(p),
            rows=len(parsed), ingested_at=datetime.now(timezone.utc).isoformat(),
            range={"from": parsed[0].timestamp if parsed else "", "to": parsed[-1].timestamp if parsed else ""},
        ))
    for p in cryptocom_paths:
        if not is_crypto_com_csv(p):
            print(f"Skipping non-Crypto.com file: {p}", file=sys.stderr)
            continue
        parsed = parse_crypto_com_csv(p)
        rows.extend(parsed)
        sources.append(Source(
            exchange="crypto_com", file=str(p), sha256=_sha256(p),
            rows=len(parsed), ingested_at=datetime.now(timezone.utc).isoformat(),
            range={"from": parsed[0].timestamp if parsed else "", "to": parsed[-1].timestamp if parsed else ""},
        ))

    # 2. Classify
    classifications = {r.id: classifier.classify(r).classified_as for r in rows}

    # 3. Pair composites
    paired = pair_composite_rows(rows, classifications, classifier.fiat_coins)

    # 3b. Apply user decisions for airdrop / migration / classification overrides.
    #     Each decision: {"transaction_id": "...", "classify_as": "...", "reason": "..."}
    if decisions.decisions:
        tx_by_id = {t.id: t for t in paired}
        for d in decisions.decisions:
            tid = d.get("transaction_id")
            new_cls = d.get("classify_as")
            if tid and new_cls and tid in tx_by_id:
                tx_by_id[tid].classified_as = new_cls
                reason = d.get("reason", "")
                if reason:
                    tx_by_id[tid].notes.append(f"user_decision:{reason}")

    # 4. Match cross-exchange transfers
    match_result = match_cross_exchange_transfers(paired)
    transfers = [
        CrossExchangeTransfer(
            **{
                "from": {"id": m.from_tx_id},
                "to": {"id": m.to_tx_id},
                "match_confidence": m.confidence,
                "matched_on": ["coin", "amount±0.5%", "time<48h"],
            }
        ) for m in match_result.matches
    ]

    # 5. Build issues from matcher + user decisions
    issues: list[Issue] = []
    for uid in match_result.unmatched_incoming:
        issues.append(Issue(
            id=f"iss-unmatched-{uid}",
            severity="warning",
            kind="unmatched_deposit",
            transaction_id=uid,
            message=f"Deposit {uid} has no matching external withdrawal.",
            suggested_action="Apply conservative basis, provide manual override, or match from other export.",
        ))
    for amb in match_result.ambiguous:
        issues.append(Issue(
            id=f"iss-ambig-{amb['incoming_id']}",
            severity="warning",
            kind="ambiguous_transfer",
            transaction_id=amb["incoming_id"],
            message=f"Multiple candidates for incoming: {amb['candidates']}",
            suggested_action="Pick the correct outgoing transaction.",
        ))
    for tx in paired:
        if tx.classified_as == "airdrop_pending_review":
            issues.append(Issue(
                id=f"iss-airdrop-{tx.id}", severity="info",
                kind="airdrop_classification", transaction_id=tx.id,
                message=f"Airdrop {(tx.asset_in or tx.asset_out).amount} {(tx.asset_in or tx.asset_out).coin} — was a Leistung required?",
                suggested_action="Classify as §22 Nr.3 income or zero-basis §23 lot.",
            ))
        elif tx.classified_as == "migration_pending_review":
            issues.append(Issue(
                id=f"iss-migration-{tx.id}", severity="info",
                kind="token_migration", transaction_id=tx.id,
                message=f"Token migration {tx.asset_in.coin} — 1:1 rebrand or new token?",
                suggested_action="Classify as non_taxable_transfer or income_receipt.",
            ))

    # 6. Bulk-prefetch all needed (coin, date) prices before the processing loop.
    #    This uses one Binance klines range-request per coin instead of one per day,
    #    avoiding per-request rate limits.
    _price_needed_cats = {
        "trade_buy", "trade_sell", "crypto_swap",
        "income_receipt", "external_in", "external_out",
    }
    prefetch_pairs: list[tuple[str, str]] = []
    for tx in paired:
        if tx.classified_as not in _price_needed_cats:
            continue
        if tx.asset_in and tx.eur_value_at_time is None:
            prefetch_pairs.append((tx.asset_in.coin, PriceResolver._date_only(tx.timestamp)))
        if tx.asset_out and tx.eur_value_at_time is None:
            prefetch_pairs.append((tx.asset_out.coin, PriceResolver._date_only(tx.timestamp)))
    prices.prefetch(list(set(prefetch_pairs)))

    # 7. Resolve prices for events needing them (income + crypto_swap + external_in)
    priced_incomes: list[IncomeEvent] = []
    fifo = FifoEngine()
    matched_to_by_incoming = {m.to_tx_id: m.from_tx_id for m in match_result.matches}
    id_to_tx = {t.id: t for t in paired}

    # Process in chronological order
    paired_sorted = sorted(paired, key=lambda t: t.timestamp)

    _needs_asset_in = {"trade_buy", "crypto_swap", "income_receipt", "external_in", "airdrop_pending_review", "migration_pending_review"}
    _needs_asset_out = {"trade_sell", "external_out"}

    for tx in paired_sorted:
        # Guard: skip malformed transactions missing a required asset leg
        if tx.classified_as in _needs_asset_in and tx.asset_in is None:
            issues.append(Issue(
                id=f"iss-malformed-{tx.id}", severity="warning",
                kind="malformed_transaction", transaction_id=tx.id,
                message=f"{tx.classified_as} transaction has no asset_in (op: {tx.raw_operation})",
                suggested_action="Check raw CSV row — may be a misclassified outgoing amount.",
            ))
            continue
        if tx.classified_as in _needs_asset_out and tx.asset_out is None:
            issues.append(Issue(
                id=f"iss-malformed-{tx.id}", severity="warning",
                kind="malformed_transaction", transaction_id=tx.id,
                message=f"{tx.classified_as} transaction has no asset_out (op: {tx.raw_operation})",
                suggested_action="Check raw CSV row — may be a misclassified incoming amount.",
            ))
            continue
        try:
            if tx.classified_as == "trade_buy":
                if tx.eur_value_at_time is not None:
                    cost_basis = tx.eur_value_at_time
                else:
                    cost_basis = prices.resolve(tx.asset_in.coin, tx.timestamp) * tx.asset_in.amount
                fifo.acquire(AcquisitionEvent(
                    event_id=tx.id, coin=tx.asset_in.coin, wallet=tx.source,
                    amount=tx.asset_in.amount,
                    cost_basis_eur=cost_basis,
                    acquired_at=tx.timestamp,
                    source="exchange_reported" if tx.price_source == "exchange_reported" else "trade",
                ))
            elif tx.classified_as == "trade_sell":
                if tx.eur_value_at_time is not None:
                    proceeds = tx.eur_value_at_time
                else:
                    proceeds = prices.resolve(tx.asset_out.coin, tx.timestamp) * tx.asset_out.amount
                d = fifo.dispose(DisposalEvent(
                    event_id=tx.id, coin=tx.asset_out.coin, wallet=tx.source,
                    amount=tx.asset_out.amount, proceeds_eur=proceeds,
                    timestamp=tx.timestamp,
                ))
                _collected_disposals.append(d)
            elif tx.classified_as == "crypto_swap":
                # Prefer exchange-reported EUR if present, otherwise resolve.
                if tx.eur_value_at_time is not None:
                    eur_value = tx.eur_value_at_time
                else:
                    eur_value = prices.resolve(tx.asset_in.coin, tx.timestamp) * tx.asset_in.amount
                if tx.asset_out:
                    d = fifo.dispose(DisposalEvent(
                        event_id=tx.id + "-out", coin=tx.asset_out.coin, wallet=tx.source,
                        amount=tx.asset_out.amount, proceeds_eur=eur_value,
                        timestamp=tx.timestamp,
                    ))
                    _collected_disposals.append(d)
                fifo.acquire(AcquisitionEvent(
                    event_id=tx.id + "-in", coin=tx.asset_in.coin, wallet=tx.source,
                    amount=tx.asset_in.amount, cost_basis_eur=eur_value,
                    acquired_at=tx.timestamp, source="swap_incoming",
                ))
            elif tx.classified_as == "income_receipt":
                if tx.eur_value_at_time is not None:
                    eur = tx.eur_value_at_time
                else:
                    eur = prices.resolve(tx.asset_in.coin, tx.timestamp) * tx.asset_in.amount
                year = datetime.fromisoformat(tx.timestamp).year
                lot = fifo.acquire(AcquisitionEvent(
                    event_id=tx.id, coin=tx.asset_in.coin, wallet=tx.source,
                    amount=tx.asset_in.amount, cost_basis_eur=eur,
                    acquired_at=tx.timestamp, source="income_receipt",
                ))
                priced_incomes.append(IncomeEvent(
                    id=tx.id, timestamp=tx.timestamp,
                    coin=tx.asset_in.coin, amount=tx.asset_in.amount,
                    eur_value_at_receipt=eur, category=tx.raw_operation.lower().replace(" ", "_"),
                    paragraph="§22 Nr.3 EStG", tax_year=year, creates_lot=lot.lot_id,
                ))
            elif tx.classified_as == "external_in":
                # Matched? Transfer basis from source exchange
                if tx.id in matched_to_by_incoming:
                    # handled when we reach the matching withdraw — skip
                    pass
                else:
                    override = next((o for o in decisions.external_basis_overrides if o["transaction_id"] == tx.id), None)
                    if override:
                        fifo.acquire(AcquisitionEvent(
                            event_id=tx.id, coin=tx.asset_in.coin, wallet=tx.source,
                            amount=tx.asset_in.amount, cost_basis_eur=Decimal(str(override["cost_basis_eur"])),
                            acquired_at=override["acquired_at"], source="external_user_override",
                        ))
                    else:
                        eur = prices.resolve(tx.asset_in.coin, tx.timestamp) * tx.asset_in.amount
                        fifo.acquire(AcquisitionEvent(
                            event_id=tx.id, coin=tx.asset_in.coin, wallet=tx.source,
                            amount=tx.asset_in.amount, cost_basis_eur=eur,
                            acquired_at=tx.timestamp, source="external_conservative",
                        ))
            elif tx.classified_as == "external_out":
                # If matched to an incoming on another exchange: transfer the lots
                matching_incoming = next((k for k, v in matched_to_by_incoming.items() if v == tx.id), None)
                if matching_incoming:
                    incoming_tx = id_to_tx[matching_incoming]
                    fifo.transfer(
                        coin=tx.asset_out.coin,
                        from_wallet=tx.source,
                        to_wallet=incoming_tx.source,
                        amount=tx.asset_out.amount,
                    )
                else:
                    # Withdrawal to an unknown external wallet — dispose at FMV (conservative)
                    try:
                        eur = prices.resolve(tx.asset_out.coin, tx.timestamp) * tx.asset_out.amount
                        d = fifo.dispose(DisposalEvent(
                            event_id=tx.id, coin=tx.asset_out.coin, wallet=tx.source,
                            amount=tx.asset_out.amount, proceeds_eur=eur, timestamp=tx.timestamp,
                        ))
                        _collected_disposals.append(d)
                        issues.append(Issue(
                            id=f"iss-extwith-{tx.id}", severity="warning",
                            kind="unmatched_withdrawal", transaction_id=tx.id,
                            message="External withdrawal treated conservatively as disposal at FMV.",
                            suggested_action="Provide destination wallet info to override treatment.",
                        ))
                    except PriceResolver.MissingPriceError as e:
                        issues.append(Issue(
                            id=f"iss-price-{tx.id}", severity="error",
                            kind="missing_price", transaction_id=tx.id,
                            message=str(e), suggested_action="Provide manual price via decisions file.",
                        ))
            # Other classifications (non_taxable_transfer, internal_transfer, fiat_movement): no-op
        except PriceResolver.MissingPriceError as e:
            issues.append(Issue(
                id=f"iss-price-{tx.id}", severity="error", kind="missing_price",
                transaction_id=tx.id, message=str(e),
                suggested_action="Provide manual price via decisions file.",
            ))
        except ValueError as e:
            issues.append(Issue(
                id=f"iss-fifo-{tx.id}", severity="warning", kind="fifo_short_position",
                transaction_id=tx.id, message=str(e),
                suggested_action="Provide source wallet/exchange for this withdrawal or check CSV completeness.",
            ))

    # Flatten lots
    all_lots = [l for lots in fifo.lots.values() for l in lots]

    yearly = aggregate_yearly(_collected_disposals, priced_incomes)

    ledger = build_ledger(
        sources=sources, transactions=paired, lots=all_lots,
        disposals=_collected_disposals, incomes=priced_incomes,
        transfers=transfers, issues=issues,
    )
    summary = build_summary(
        ledger=ledger, yearly=yearly,
        decisions_pending=sum(1 for i in issues if i.severity != "info" or i.kind in ("airdrop_classification", "token_migration")),
        decisions_resolved=len(decisions.decisions),
    )
    write_json(workspace / "crypto-ledger.json", ledger)
    write_json(workspace / "crypto-summary.json", summary)

    print(json.dumps({
        "rows_total": sum(s.rows for s in sources),
        "transactions": len(paired),
        "disposals": len(_collected_disposals),
        "income_events": len(priced_incomes),
        "issues": len(issues),
        "years_flagged": summary.totals_across_years["years_needing_correction"],
    }, indent=2))


# Disposals are collected in a module-global because fifo.dispose returns them.
# Reset on each run() call.
_collected_disposals: list = []


def main() -> int:
    global _collected_disposals
    _collected_disposals = []

    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["initial", "apply-decisions"], default="initial")
    ap.add_argument("--binance", nargs="*", default=[])
    ap.add_argument("--coinbase", nargs="*", default=[])
    ap.add_argument("--cryptocom", nargs="*", default=[])
    ap.add_argument("--workspace", required=True)
    args = ap.parse_args()

    ws = Path(args.workspace)
    run(
        binance_paths=[Path(p) for p in args.binance],
        coinbase_paths=[Path(p) for p in args.coinbase],
        cryptocom_paths=[Path(p) for p in args.cryptocom],
        workspace=ws,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
