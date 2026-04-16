"""Yearly §23 and §22 Nr.3 aggregation with Freigrenze application.

Freigrenze (not Freibetrag): if below threshold → 0 taxable; if at/above → ALL taxable.
"""
from __future__ import annotations

from collections import defaultdict
from decimal import Decimal
from typing import Iterable

from scripts.schemas import Disposal, IncomeEvent, YearlyTaxSummary

FREIGRENZE_23: dict[int, Decimal] = {
    2021: Decimal("600"), 2022: Decimal("600"), 2023: Decimal("600"),
    2024: Decimal("1000"), 2025: Decimal("1000"), 2026: Decimal("1000"),
}
FREIGRENZE_22_3 = Decimal("256")  # per year, constant through 2025


def _f23(year: int) -> Decimal:
    return FREIGRENZE_23.get(year, Decimal("1000"))


def aggregate_yearly(disposals: Iterable[Disposal], incomes: Iterable[IncomeEvent]) -> dict[str, YearlyTaxSummary]:
    by_year_gain: dict[int, Decimal] = defaultdict(lambda: Decimal("0"))
    by_year_loss: dict[int, Decimal] = defaultdict(lambda: Decimal("0"))
    all_disposal_years: set[int] = set()
    for d in disposals:
        all_disposal_years.add(d.tax_year)
        if d.tax_treatment != "taxable_short_term":
            continue
        if d.gain_eur >= 0:
            by_year_gain[d.tax_year] += d.gain_eur
        else:
            by_year_loss[d.tax_year] += d.gain_eur  # negative

    by_year_income: dict[int, Decimal] = defaultdict(lambda: Decimal("0"))
    for i in incomes:
        by_year_income[i.tax_year] += i.eur_value_at_receipt

    all_years = set(by_year_gain) | set(by_year_loss) | set(by_year_income) | all_disposal_years
    out: dict[str, YearlyTaxSummary] = {}
    for y in sorted(all_years):
        gain = by_year_gain[y]
        loss = by_year_loss[y]
        net = gain + loss
        fg = _f23(y)
        taxable_23 = Decimal("0") if net <= fg else net   # Freigrenze: at/below threshold → all tax-free

        inc = by_year_income[y]
        taxable_22 = Decimal("0") if inc <= FREIGRENZE_22_3 else inc

        needs = (taxable_23 > 0) or (taxable_22 > 0)
        reason = ""
        if not needs:
            reason = "Both §23 and §22 Nr.3 below Freigrenze"

        out[str(y)] = YearlyTaxSummary(
            sect_23_gain_eur=gain,
            sect_23_loss_eur=loss,
            sect_23_net_eur=net,
            freigrenze_eur=fg,
            sect_23_taxable_eur=taxable_23,
            sect_22_3_income_eur=inc,
            sect_22_3_freigrenze_eur=FREIGRENZE_22_3,
            sect_22_3_taxable_eur=taxable_22,
            needs_correction=needs,
            reason=reason,
        )
    return out
