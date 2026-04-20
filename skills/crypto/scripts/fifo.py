"""FIFO lot engine per (coin, wallet). German tax: >1 year holding = tax-free (§23 EStG)."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Optional

from scripts.schemas import Lot, LotConsumption, Disposal


@dataclass
class AcquisitionEvent:
    event_id: str
    coin: str
    wallet: str
    amount: Decimal
    cost_basis_eur: Decimal
    acquired_at: str
    source: str  # "trade" | "income_receipt" | "swap_incoming" | "external_matched" | "external_conservative" | "external_user_override"


@dataclass
class DisposalEvent:
    event_id: str
    coin: str
    wallet: str
    amount: Decimal
    proceeds_eur: Decimal
    timestamp: str


class FifoEngine:
    def __init__(self):
        self.lots: dict[tuple[str, str], list[Lot]] = defaultdict(list)
        self._lot_counter = 0

    def acquire(self, ev: AcquisitionEvent) -> Lot:
        acquired = datetime.fromisoformat(ev.acquired_at)
        holding_end = (acquired + timedelta(days=365)).isoformat()
        lot = Lot(
            lot_id=f"lot-{ev.event_id}",
            coin=ev.coin,
            wallet=ev.wallet,
            acquired_at=ev.acquired_at,
            amount_original=ev.amount,
            amount_remaining=ev.amount,
            cost_basis_eur=ev.cost_basis_eur,
            cost_basis_source=ev.source,
            holding_period_ends=holding_end,
        )
        self.lots[(ev.coin, ev.wallet)].append(lot)
        self.lots[(ev.coin, ev.wallet)].sort(key=lambda l: (l.acquired_at, l.lot_id))
        return lot

    def transfer(self, coin: str, from_wallet: str, to_wallet: str, amount: Decimal) -> None:
        """Move up to `amount` of oldest lots from one wallet to another, preserving acquired_at."""
        remaining = amount
        src = self.lots[(coin, from_wallet)]
        moved: list[Lot] = []
        i = 0
        while remaining > 0 and i < len(src):
            lot = src[i]
            if lot.amount_remaining <= 0:
                i += 1
                continue
            take = min(lot.amount_remaining, remaining)
            if take == lot.amount_remaining:
                moved.append(lot)
                src.pop(i)
            else:
                # split
                new_lot = Lot(**{**lot.model_dump(),
                                 "lot_id": lot.lot_id + "-s",
                                 "amount_original": take,
                                 "amount_remaining": take})
                lot.amount_original -= take
                lot.amount_remaining -= take
                moved.append(new_lot)
                i += 1
            remaining -= take
        for m in moved:
            m.wallet = to_wallet
            self.lots[(coin, to_wallet)].append(m)
        self.lots[(coin, to_wallet)].sort(key=lambda l: (l.acquired_at, l.lot_id))

    def dispose(self, ev: DisposalEvent) -> Disposal:
        queue = self.lots[(ev.coin, ev.wallet)]
        remaining = ev.amount
        consumed: list[LotConsumption] = []
        total_basis = Decimal("0")
        disposal_at = datetime.fromisoformat(ev.timestamp)
        treatment_flags: set[str] = set()
        oldest_acquired: Optional[datetime] = None

        for lot in queue:
            if remaining <= 0:
                break
            if lot.amount_remaining <= 0:
                continue
            take = min(lot.amount_remaining, remaining)
            basis_for_take = lot.cost_basis_eur * (take / lot.amount_original)
            consumed.append(LotConsumption(
                lot_id=lot.lot_id, amount=take, cost_basis_eur=basis_for_take,
            ))
            lot.amount_remaining -= take
            total_basis += basis_for_take
            remaining -= take
            acq = datetime.fromisoformat(lot.acquired_at)
            if oldest_acquired is None or acq < oldest_acquired:
                oldest_acquired = acq
            holding_end = datetime.fromisoformat(lot.holding_period_ends)
            if disposal_at > holding_end:
                treatment_flags.add("long")
            else:
                treatment_flags.add("short")
            if lot.amount_remaining == 0:
                lot.fully_consumed_by.append(ev.event_id)

        if remaining > 0:
            raise ValueError(
                f"Cannot dispose {ev.amount} {ev.coin} from {ev.wallet}: short by {remaining}"
            )

        # Treatment: if ANY consumed lot was short-term, disposal is short-term.
        # (Conservative; tool notes mixed-lot cases for user review.)
        treatment = "taxable_short_term" if "short" in treatment_flags else "tax_free_long_term"
        days = (disposal_at - oldest_acquired).days if oldest_acquired else 0
        paragraph = (
            "§23 EStG (>1 year holding)" if treatment == "tax_free_long_term"
            else "§23 EStG (<1 year holding)"
        )
        tax_year = disposal_at.year

        return Disposal(
            id=f"disposal-{ev.event_id}",
            timestamp=ev.timestamp,
            coin=ev.coin,
            amount=ev.amount,
            proceeds_eur=ev.proceeds_eur,
            lots_consumed=consumed,
            gain_eur=ev.proceeds_eur - total_basis,
            holding_period_days=days,
            tax_treatment=treatment,
            tax_year=tax_year,
            paragraph=paragraph,
        )
