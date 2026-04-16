from decimal import Decimal
from scripts.fifo import FifoEngine, AcquisitionEvent, DisposalEvent

D = Decimal

def test_simple_full_consumption_short_term_gain():
    e = FifoEngine()
    e.acquire(AcquisitionEvent(
        event_id="a1", coin="BTC", wallet="binance",
        amount=D("1"), cost_basis_eur=D("1000"),
        acquired_at="2022-01-01T00:00:00+00:00", source="trade",
    ))
    disposal = e.dispose(DisposalEvent(
        event_id="d1", coin="BTC", wallet="binance",
        amount=D("1"), proceeds_eur=D("1500"),
        timestamp="2022-06-01T00:00:00+00:00",
    ))
    assert disposal.gain_eur == D("500")
    assert disposal.tax_treatment == "taxable_short_term"
    assert disposal.holding_period_days == 151

def test_long_term_tax_free_after_1_year():
    e = FifoEngine()
    e.acquire(AcquisitionEvent(
        event_id="a1", coin="BTC", wallet="binance",
        amount=D("1"), cost_basis_eur=D("1000"),
        acquired_at="2021-01-01T00:00:00+00:00", source="trade",
    ))
    disposal = e.dispose(DisposalEvent(
        event_id="d1", coin="BTC", wallet="binance",
        amount=D("1"), proceeds_eur=D("2000"),
        timestamp="2022-01-02T00:00:00+00:00",
    ))
    assert disposal.tax_treatment == "tax_free_long_term"
    assert disposal.gain_eur == D("1000")

def test_partial_consumption_across_multiple_lots():
    e = FifoEngine()
    e.acquire(AcquisitionEvent(event_id="a1", coin="BTC", wallet="binance", amount=D("0.5"), cost_basis_eur=D("500"), acquired_at="2022-01-01T00:00:00+00:00", source="trade"))
    e.acquire(AcquisitionEvent(event_id="a2", coin="BTC", wallet="binance", amount=D("1.0"), cost_basis_eur=D("1500"), acquired_at="2022-02-01T00:00:00+00:00", source="trade"))
    d = e.dispose(DisposalEvent(event_id="d1", coin="BTC", wallet="binance", amount=D("1.2"), proceeds_eur=D("2400"), timestamp="2022-06-01T00:00:00+00:00"))
    # Consumes 0.5 from a1 (cost 500) + 0.7 from a2 (cost 1500 * 0.7 = 1050) = 1550 total basis
    # Gain = 2400 - 1550 = 850
    assert d.gain_eur == D("850")
    assert len(d.lots_consumed) == 2
    assert d.lots_consumed[0].lot_id == "lot-a1"
    assert d.lots_consumed[0].amount == D("0.5")
    assert d.lots_consumed[1].amount == D("0.7")

def test_cross_exchange_transfer_preserves_acquired_at():
    e = FifoEngine()
    e.acquire(AcquisitionEvent(event_id="a1", coin="XRP", wallet="coinbase", amount=D("199"), cost_basis_eur=D("100"), acquired_at="2020-01-01T00:00:00+00:00", source="trade"))
    e.transfer(coin="XRP", from_wallet="coinbase", to_wallet="binance", amount=D("199"))
    # Later dispose from binance
    d = e.dispose(DisposalEvent(event_id="d1", coin="XRP", wallet="binance", amount=D("199"), proceeds_eur=D("200"), timestamp="2021-06-01T00:00:00+00:00"))
    # >1 year from original 2020-01-01 acquisition → tax-free
    assert d.tax_treatment == "tax_free_long_term"

def test_lots_are_ordered_fifo_by_acquired_at():
    e = FifoEngine()
    e.acquire(AcquisitionEvent(event_id="a2", coin="BTC", wallet="binance", amount=D("1"), cost_basis_eur=D("2000"), acquired_at="2022-02-01T00:00:00+00:00", source="trade"))
    e.acquire(AcquisitionEvent(event_id="a1", coin="BTC", wallet="binance", amount=D("1"), cost_basis_eur=D("1000"), acquired_at="2022-01-01T00:00:00+00:00", source="trade"))
    d = e.dispose(DisposalEvent(event_id="d1", coin="BTC", wallet="binance", amount=D("1"), proceeds_eur=D("1500"), timestamp="2022-06-01T00:00:00+00:00"))
    # Oldest first — a1 (1000 basis) consumed → 500 gain
    assert d.gain_eur == D("500")
    assert d.lots_consumed[0].lot_id == "lot-a1"
