from decimal import Decimal
from scripts.schemas import (
    NormalizedRow, ClassifiedTx, Lot, Disposal, IncomeEvent,
    Source, Issue, CrossExchangeTransfer, YearlyTaxSummary,
    CryptoLedger, CryptoSummary, Decisions,
)

def test_normalized_row_requires_core_fields():
    row = NormalizedRow(
        id="bnc-1",
        source="binance",
        timestamp="2021-05-13T23:00:23+02:00",
        raw_operation="Buy",
        coin="BTC",
        change=Decimal("0.009783"),
        remark="",
    )
    assert row.source == "binance"
    assert row.change == Decimal("0.009783")

def test_classified_tx_roundtrip():
    tx = ClassifiedTx(
        id="bnc-1",
        source="binance",
        timestamp="2021-05-13T23:00:23+02:00",
        raw_operation="Buy",
        classified_as="trade_buy",
        asset_in={"coin": "BTC", "amount": Decimal("0.009783")},
        asset_out={"coin": "EUR", "amount": Decimal("399.98")},
        fee={"coin": "BTC", "amount": Decimal("0.00000978")},
        eur_value_at_time=Decimal("399.98"),
        price_source="binance_csv_fiat_pair",
        tax_event="acquisition",
    )
    d = tx.model_dump(mode="json")
    assert d["asset_in"]["amount"] == "0.009783"  # Decimal serialized as string

def test_lot_defaults():
    lot = Lot(
        lot_id="lot-btc-1",
        coin="BTC",
        wallet="binance",
        acquired_at="2021-05-13T23:00:23+02:00",
        amount_original=Decimal("1"),
        amount_remaining=Decimal("1"),
        cost_basis_eur=Decimal("100"),
        cost_basis_source="trade",
        holding_period_ends="2022-05-13T23:00:23+02:00",
    )
    assert lot.fully_consumed_by == []

def test_crypto_summary_required_sections():
    summary = CryptoSummary(
        schema_version=1,
        generated_at="2026-04-13T00:00:00Z",
        ingest_stats={"rows_binance": 0, "rows_coinbase": 0, "transactions_after_pairing": 0, "classified_counts": {}},
        yearly_tax_summary={},
        current_holdings=[],
        issues=[],
        decisions_pending=0,
        decisions_resolved=0,
        totals_across_years={"estimated_back_tax_eur": "0", "estimated_interest_eur": "0", "years_needing_correction": []},
        optimizations=[],
    )
    assert summary.schema_version == 1
