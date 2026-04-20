from decimal import Decimal
from scripts.schemas import Disposal, IncomeEvent, LotConsumption
from scripts.aggregator import aggregate_yearly, FREIGRENZE_23, FREIGRENZE_22_3

def _disp(year, gain, treatment="taxable_short_term"):
    return Disposal(
        id=f"d-{year}-{gain}",
        timestamp=f"{year}-06-01T00:00:00+00:00",
        coin="BTC", amount=Decimal("1"),
        proceeds_eur=Decimal("1000") + Decimal(gain),
        lots_consumed=[LotConsumption(lot_id="l", amount=Decimal("1"), cost_basis_eur=Decimal("1000"))],
        gain_eur=Decimal(gain),
        holding_period_days=100,
        tax_treatment=treatment, tax_year=year,
        paragraph="§23 EStG",
    )

def _inc(year, eur):
    return IncomeEvent(
        id=f"i-{year}-{eur}",
        timestamp=f"{year}-03-15T00:00:00+00:00",
        coin="XRP", amount=Decimal("1"),
        eur_value_at_receipt=Decimal(eur),
        category="simple_earn_interest",
        paragraph="§22 Nr.3 EStG",
        tax_year=year, creates_lot="lot-x",
    )

def test_freigrenze_2022_at_600_not_met():
    s = aggregate_yearly([_disp(2022, "500")], [])
    assert s["2022"].sect_23_taxable_eur == Decimal("0")
    assert s["2022"].needs_correction is False

def test_freigrenze_2022_at_600_just_exceeded():
    s = aggregate_yearly([_disp(2022, "601")], [])
    assert s["2022"].sect_23_taxable_eur == Decimal("601")  # all, not just 1
    assert s["2022"].needs_correction is True

def test_freigrenze_2024_at_1000():
    s = aggregate_yearly([_disp(2024, "999")], [])
    assert s["2024"].sect_23_taxable_eur == Decimal("0")

def test_long_term_not_taxable():
    s = aggregate_yearly([_disp(2023, "5000", treatment="tax_free_long_term")], [])
    assert s["2023"].sect_23_net_eur == Decimal("0")   # excluded from §23 calc
    assert s["2023"].needs_correction is False

def test_losses_offset_gains_within_year():
    s = aggregate_yearly([_disp(2023, "1000"), _disp(2023, "-400")], [])
    assert s["2023"].sect_23_net_eur == Decimal("600")
    assert s["2023"].sect_23_taxable_eur == Decimal("0")   # below 600 Freigrenze

def test_sect_22_3_freigrenze_256():
    s = aggregate_yearly([], [_inc(2023, "200")])
    assert s["2023"].sect_22_3_taxable_eur == Decimal("0")
    s2 = aggregate_yearly([], [_inc(2023, "257")])
    assert s2["2023"].sect_22_3_taxable_eur == Decimal("257")

def test_year_needs_correction_only_if_either_freigrenze_breached():
    s = aggregate_yearly([_disp(2022, "500")], [_inc(2022, "200")])
    assert s["2022"].needs_correction is False
    s2 = aggregate_yearly([_disp(2022, "500")], [_inc(2022, "300")])
    assert s2["2022"].needs_correction is True
