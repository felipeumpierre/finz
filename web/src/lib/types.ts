// All types derived from real workspace/*.json shapes (2026-04 state).
// Fields we don't render are omitted. Unknown/variable fields use `unknown` or `Record<string, unknown>`.

// ---------- profile.json ----------

export interface Profile {
  last_updated: string;
  family_status: 'married' | 'single' | string;
  married_since?: string;
  persons: ProfilePerson[];
  children: ProfileChild[];
  address: {
    street: string;
    city: string;
    postal_code: string;
    bundesland: string;
  };
  risk_context?: Record<string, unknown>;
  pension?: { current_value?: number; contract_name?: string } | null;
  filing_status?: 'zusammenveranlagung' | 'einzelveranlagung' | string;
}

export interface ProfilePerson {
  name: string;
  role: 'primary' | 'spouse' | string;
  dob: string;
  nationality: string;
  tax_class?: number;
  gross_annual_salary?: number;
  employer?: string;
  employment_type?: string;
}

export interface ProfileChild {
  name: string;
  dob: string;
  nationality: string;
}

// ---------- cash-state.json ----------

export interface CashState {
  last_updated: string;
  accounts: CashAccount[];
}

export interface CashAccount {
  bank: string;
  owner: string;
  iban?: string;
  account_type: 'girokonto' | 'tagesgeld' | 'festgeld' | string;
  product?: string;
  status: 'active' | 'closed' | string;
  balances: CashBalance[];
  interest?: CashInterestEntry[];
  annual_summaries?: CashAnnualSummary[];
  monthly_summaries?: CashMonthlySummary[];
  linked_credit_cards?: CashCreditCard[];
}

export interface CashBalance {
  date: string;
  balance: number;
  source?: string;
}

export interface CashInterestEntry {
  year: number;
  total_interest_earned: number;
  interest_rate_pct: number;
  tax_withheld?: {
    kapitalertragsteuer?: number;
    solidaritaetszuschlag?: number;
  };
  notes?: string;
}

export interface CashAnnualSummary {
  year: number;
  total_income: number;
  total_expenses: number;
  net_savings: number;
  category_totals?: Record<string, number>;
  monthly_breakdown?: Record<string, { income: number; expenses: number }>;
}

export interface CashMonthlySummary {
  month: string;
  opening_balance?: number;
  closing_balance?: number;
  total_income: number;
  total_expenses: number;
  savings: number;
  categories?: Record<string, number>;
}

export interface CashCreditCard {
  provider: string;
  card_number_last4?: string;
  card_type?: string;
  card_fee_monthly?: number;
  annual_statements?: Array<{
    year: number;
    total_charges: number;
    net_spending: number;
    category_totals?: Record<string, number>;
  }>;
}

// ---------- portfolio-state.json ----------

export interface PortfolioState {
  last_updated: string;
  brokers: Broker[];
  tax_year_summary?: {
    sparerpauschbetrag_used?: number;
    foreign_broker_income?: number;
  };
}

export interface Broker {
  name: string;
  owner: string;
  type: 'german_bank' | 'german_broker' | 'foreign_broker' | 'foreign_broker_crypto' | string;
  country?: string;
  annual_statements?: Array<Record<string, unknown>>;
  portfolio_snapshots?: PortfolioSnapshot[];
  positions_year_end?: BrokerPosition[];
  annual_snapshots?: Array<Record<string, unknown>>;
}

export interface PortfolioSnapshot {
  date: string;
  total_value: number;
  cash_eur?: number;
  cash_usd?: number;
  positions: BrokerPosition[];
}

export interface BrokerPosition {
  isin?: string;
  name: string;
  quantity?: number;
  qty?: number;
  price?: number;
  price_usd?: number;
  price_eur?: number;
  value?: number;
  value_eur?: number;
  currency?: string;
  type?: string;
}

// ---------- insurance-state.json ----------

export interface InsuranceState {
  last_updated: string;
  policies: InsurancePolicy[];
  audit_results?: {
    gaps?: InsuranceGap[];
  };
}

export interface InsurancePolicy {
  provider: string;
  policy_number?: string | null;
  type: string;
  product_name?: string;
  annual_premium?: number;
  payment_frequency?: 'monthly' | 'annual' | string;
  monthly_premium?: number;
  who_covered?: string;
  start_date?: string | null;
  end_date?: string | null;
  tax_deductible_portion_annual?: number;
  co_insured?: string;
}

export interface InsuranceGap {
  type: string;
  severity: 'critical' | 'important' | 'nice_to_have' | string;
  recommendation: string;
}

// ---------- tax-state.json ----------

export interface TaxState {
  tax_year: number;
  last_updated: string;
  filing_status?: 'Zusammenveranlagung' | 'Einzelveranlagung' | string;
  phases_completed?: string[];
  persons?: TaxPerson[];
  deductions?: Record<string, unknown>;
  capital_income?: Record<string, unknown>;
}

export interface TaxPerson {
  name: string;
  role: string;
  employers?: Array<{
    employer_name: string;
    brutto: number;
    lohnsteuer: number;
  }>;
  freelance_income?: {
    revenue?: number;
    profit?: number;
  };
}

// ---------- crypto-summary.json ----------

export interface CryptoSummary {
  schema_version: number;
  generated_at: string;
  ingest_stats?: Record<string, unknown>;
  yearly_tax_summary?: Record<string, CryptoYearlyTax>;
  holdings?: CryptoHolding[];
}

export interface CryptoYearlyTax {
  sect_23_gain_eur: string | number;
  sect_23_loss_eur: string | number;
  sect_23_net_eur: string | number;
  sect_23_taxable_eur: string | number;
  sect_22_3_income_eur: string | number;
  sect_22_3_taxable_eur: string | number;
  needs_correction?: boolean;
  reason?: string;
  estimated_back_tax_eur?: string | number | null;
}

export interface CryptoHolding {
  symbol: string;
  name?: string;
  quantity: number;
  value_eur?: number;
  price_eur?: number;
  oldest_lot_date?: string;
}
