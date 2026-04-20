"""Pydantic models for all crypto-engine JSON state files.

All monetary amounts are Decimal; serialization emits strings for round-trip safety.
"""
from __future__ import annotations

from decimal import Decimal
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field

# ---- Common ------------------------------------------------------------------

class _Base(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        json_encoders={Decimal: lambda v: format(v, "f")},
    )


class AssetAmount(_Base):
    coin: str
    amount: Decimal


# ---- Input-stage -------------------------------------------------------------

class NormalizedRow(_Base):
    """One row from an exchange CSV after format normalization, before classification."""
    id: str
    source: Literal["binance", "coinbase", "crypto_com"]
    timestamp: str                    # ISO 8601 with timezone
    raw_operation: str
    coin: str
    change: Decimal
    account: Optional[str] = None     # Binance-only: Spot, Pool, etc.
    remark: str = ""
    eur_value_hint: Optional[Decimal] = None   # exchange-reported EUR value (e.g. Crypto.com Native Amount)
    pair_key: Optional[str] = None             # explicit pairing token for same-row swap legs


# ---- Classification-stage ----------------------------------------------------

TaxCategory = Literal[
    "trade_buy",
    "trade_sell",
    "crypto_swap",
    "income_receipt",
    "non_taxable_transfer",
    "external_in",
    "external_out",
    "internal_transfer",
    "fiat_movement",
    "airdrop_pending_review",
    "migration_pending_review",
    "fee_standalone",
]


class ClassifiedTx(_Base):
    id: str
    source: str
    timestamp: str
    raw_operation: str
    classified_as: TaxCategory
    asset_in: Optional[AssetAmount] = None
    asset_out: Optional[AssetAmount] = None
    fee: Optional[AssetAmount] = None
    eur_value_at_time: Optional[Decimal] = None
    price_source: Optional[str] = None
    tax_event: Optional[Literal["acquisition", "disposal", "income", "non_taxable"]] = None
    notes: list[str] = Field(default_factory=list)


# ---- Ledger entities ---------------------------------------------------------

class Lot(_Base):
    lot_id: str
    coin: str
    wallet: str
    acquired_at: str
    amount_original: Decimal
    amount_remaining: Decimal
    cost_basis_eur: Decimal
    cost_basis_source: Literal[
        "trade", "income_receipt", "swap_incoming", "external_matched",
        "external_conservative", "external_user_override", "exchange_reported",
    ]
    fully_consumed_by: list[str] = Field(default_factory=list)
    holding_period_ends: str
    flags: list[str] = Field(default_factory=list)


class LotConsumption(_Base):
    lot_id: str
    amount: Decimal
    cost_basis_eur: Decimal


class Disposal(_Base):
    id: str
    timestamp: str
    coin: str
    amount: Decimal
    proceeds_eur: Decimal
    lots_consumed: list[LotConsumption]
    gain_eur: Decimal
    holding_period_days: int
    tax_treatment: Literal["tax_free_long_term", "taxable_short_term"]
    tax_year: int
    paragraph: str


class IncomeEvent(_Base):
    id: str
    timestamp: str
    coin: str
    amount: Decimal
    eur_value_at_receipt: Decimal
    category: str
    paragraph: str
    tax_year: int
    creates_lot: str


class CrossExchangeTransfer(_Base):
    from_side: dict = Field(alias="from")
    to_side: dict = Field(alias="to")
    match_confidence: float
    matched_on: list[str]

    model_config = ConfigDict(populate_by_name=True, extra="forbid")


class Issue(_Base):
    id: str
    severity: Literal["info", "warning", "error"]
    kind: str
    transaction_id: Optional[str] = None
    message: str
    suggested_action: Optional[str] = None


class Source(_Base):
    exchange: Literal["binance", "coinbase", "crypto_com"]
    file: str
    sha256: str
    rows: int
    ingested_at: str
    range: dict  # {"from": iso, "to": iso}


# ---- Aggregation -------------------------------------------------------------

class YearlyTaxSummary(_Base):
    sect_23_gain_eur: Decimal
    sect_23_loss_eur: Decimal
    sect_23_net_eur: Decimal
    freigrenze_eur: Decimal
    sect_23_taxable_eur: Decimal
    sect_22_3_income_eur: Decimal
    sect_22_3_freigrenze_eur: Decimal
    sect_22_3_taxable_eur: Decimal
    needs_correction: bool
    reason: str = ""
    estimated_back_tax_eur: Optional[Decimal] = None
    estimated_interest_eur: Optional[Decimal] = None


# ---- Top-level state files ---------------------------------------------------

class CryptoLedger(_Base):
    schema_version: int = 1
    last_updated: str
    sources: list[Source]
    transactions: list[ClassifiedTx]
    lots: list[Lot]
    disposals: list[Disposal]
    income_events: list[IncomeEvent]
    cross_exchange_transfers: list[CrossExchangeTransfer]
    issues: list[Issue]


class HoldingsSummary(_Base):
    coin: str
    amount: Decimal
    eur_value_now: Optional[Decimal] = None
    unrealized_gain_eur: Optional[Decimal] = None
    lots_summary: dict


class CryptoSummary(_Base):
    schema_version: int = 1
    generated_at: str
    ingest_stats: dict
    yearly_tax_summary: dict[str, YearlyTaxSummary]
    current_holdings: list[HoldingsSummary]
    issues: list[Issue]
    decisions_pending: int
    decisions_resolved: int
    totals_across_years: dict
    optimizations: list[dict]


class Decisions(_Base):
    schema_version: int = 1
    decisions: list[dict] = Field(default_factory=list)
    manual_prices: list[dict] = Field(default_factory=list)
    external_basis_overrides: list[dict] = Field(default_factory=list)
