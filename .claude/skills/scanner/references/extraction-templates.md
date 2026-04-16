# Extraction Templates

Defines what structured data to extract per document type and which state file to write to.

---

## Insurance Documents → `workspace/insurance-state.json`

### General Insurance Policy Template

All insurance documents share this base structure:

```json
{
  "provider": "string — insurance company name",
  "policy_number": "string — Versicherungsscheinnummer",
  "type": "string — category from taxonomy (e.g., haftpflicht, bu, rechtsschutz)",
  "product_name": "string — specific product name if visible",
  "annual_premium": "number — yearly cost in EUR",
  "payment_frequency": "string — monthly/quarterly/semi-annual/annual",
  "who_covered": "string — single/family/partner",
  "start_date": "string — YYYY-MM-DD",
  "end_date": "string or null — YYYY-MM-DD, null if ongoing",
  "source_document": "string — file path of the scanned document",
  "scanned_at": "string — ISO timestamp"
}
```

### Haftpflicht (Personal Liability)

Additional fields:
```json
{
  "coverage_amount_personal": "number — Personenschaeden coverage in EUR",
  "coverage_amount_property": "number — Sachschaeden coverage in EUR",
  "coverage_amount_financial": "number — Vermoegensschaeden coverage in EUR",
  "deductible": "number or null — Selbstbeteiligung in EUR",
  "includes_key_loss": "boolean — Schluesselversicherung included",
  "includes_rental_property_damage": "boolean — Mietsachschaeden included",
  "includes_foreign_coverage": "boolean — Auslandsschutz included"
}
```

### BU (Disability Insurance)

Additional fields:
```json
{
  "monthly_benefit": "number — monthly BU-Rente in EUR",
  "coverage_until_age": "number — e.g., 67",
  "waiting_period_months": "number — Karenzzeit in months",
  "abstract_referral": "boolean — abstrakte Verweisung (true = worse for insured)",
  "nachversicherungsgarantie": "boolean — option to increase without new health check",
  "dynamic_increase_pct": "number or null — annual premium/benefit increase percentage"
}
```

### Rechtsschutz (Legal Protection)

Additional fields:
```json
{
  "coverage_areas": ["array — e.g., privat, beruf, verkehr, wohnen"],
  "deductible": "number — Selbstbeteiligung in EUR",
  "waiting_period_months": "number — for certain coverage areas",
  "includes_mediation": "boolean"
}
```

### Hausrat (Household Contents)

Additional fields:
```json
{
  "insured_sum": "number — Versicherungssumme in EUR",
  "apartment_size_sqm": "number — apartment size used for calculation",
  "includes_bicycle_theft": "boolean — Fahrraddiebstahl included",
  "includes_elemental_damage": "boolean — Elementarschaeden (flood, earthquake)",
  "includes_glass_breakage": "boolean — Glasbruch included"
}
```

### KFZ (Motor Vehicle)

Additional fields:
```json
{
  "vehicle": "string — make and model",
  "license_plate": "string — Kennzeichen",
  "coverage_type": "string — haftpflicht/teilkasko/vollkasko",
  "sf_class": "string — Schadenfreiheitsklasse",
  "deductible_teilkasko": "number or null — in EUR",
  "deductible_vollkasko": "number or null — in EUR"
}
```

### Krankenversicherung (Health Insurance)

Additional fields:
```json
{
  "gkv_or_pkv": "string — GKV or PKV",
  "monthly_premium": "number — monthly premium in EUR",
  "zusatzbeitrag_pct": "number or null — GKV additional contribution rate",
  "basisbeitrag_annual": "number or null — PKV tax-deductible base contribution",
  "employer_subsidy": "number or null — Arbeitgeberzuschuss annual"
}
```

### Zahnzusatz (Dental Supplementary)

Additional fields:
```json
{
  "coverage_zahnersatz_pct": "number — coverage for crowns, bridges, implants",
  "coverage_zahnbehandlung_pct": "number — coverage for treatments",
  "coverage_kieferorthopaedie_pct": "number or null",
  "annual_max_benefit": "number or null — annual cap in EUR",
  "waiting_period_months": "number"
}
```

### Unfall (Accident)

Additional fields:
```json
{
  "grundsumme": "number — base invalidity sum in EUR",
  "progression_pct": "number — e.g., 225, 350, 500",
  "death_benefit": "number or null — Todesfallleistung in EUR",
  "hospital_daily_benefit": "number or null — Krankenhaustagegeld in EUR"
}
```

### Reise (Travel)

Additional fields:
```json
{
  "coverage_type": "string — kranken/ruecktritt/gepaeck/kombi",
  "coverage_region": "string — worldwide/europe",
  "max_trip_duration_days": "number — e.g., 56"
}
```

### Risikoleben (Term Life)

Additional fields:
```json
{
  "insured_sum": "number — Versicherungssumme / Todesfallleistung in EUR",
  "beneficiary": "string — Bezugsberechtigter name or relationship",
  "is_crossed": "boolean — kreuzweise (couple insures each other)"
}
```

### Writing to insurance-state.json

The insurance state file has this structure:

```json
{
  "last_updated": "ISO timestamp",
  "policies": [
    { "...all fields from template above..." }
  ]
}
```

When adding a new policy:
1. Check if a policy with the same provider + policy_number already exists
2. If yes, warn the user and ask whether to update or keep both
3. If no, append to the policies array
4. Always update `last_updated`

---

## Investment Documents → `workspace/portfolio-state.json`

### Jahresabrechnung / Ertraegnisaufstellung (Annual Statement)

```json
{
  "broker": "string — broker or bank name",
  "statement_type": "string — jahresabrechnung/ertraegnisaufstellung",
  "tax_year": "number — e.g., 2025",
  "total_portfolio_value": "number or null — year-end value in EUR",
  "positions": [
    {
      "isin": "string",
      "name": "string — security name",
      "quantity": "number",
      "value_year_end": "number — value at statement date in EUR",
      "purchase_value": "number or null — total cost basis in EUR"
    }
  ],
  "dividends_total": "number — total dividends/distributions in EUR",
  "realized_gains": "number — realized capital gains in EUR",
  "realized_losses": "number — realized capital losses in EUR",
  "vorabpauschale": "number or null — advance lump sum in EUR",
  "freistellungsauftrag_used": "number — amount of Sparerpauschbetrag used in EUR",
  "freistellungsauftrag_total": "number — total Freistellungsauftrag at this broker in EUR",
  "taxes_withheld": {
    "kapitalertragsteuer": "number",
    "solidaritaetszuschlag": "number",
    "kirchensteuer": "number or null"
  },
  "source_document": "string — file path",
  "scanned_at": "string — ISO timestamp"
}
```

### Depotauszug (Portfolio Statement)

```json
{
  "broker": "string",
  "statement_date": "string — YYYY-MM-DD",
  "total_value": "number — total portfolio value in EUR",
  "positions": [
    {
      "isin": "string",
      "name": "string",
      "quantity": "number",
      "current_value": "number — value at statement date in EUR",
      "purchase_value": "number or null"
    }
  ],
  "source_document": "string",
  "scanned_at": "string"
}
```

### Kaufabrechnung (Trade Confirmation)

```json
{
  "broker": "string",
  "trade_date": "string — YYYY-MM-DD",
  "settlement_date": "string — YYYY-MM-DD",
  "direction": "string — buy/sell",
  "isin": "string",
  "security_name": "string",
  "quantity": "number",
  "price_per_unit": "number — in EUR",
  "total_amount": "number — in EUR",
  "fees": "number — commissions and fees in EUR",
  "exchange": "string or null — e.g., Xetra, Tradegate",
  "source_document": "string",
  "scanned_at": "string"
}
```

### Dividendenmitteilung (Dividend Notification)

```json
{
  "broker": "string",
  "payment_date": "string — YYYY-MM-DD",
  "isin": "string",
  "security_name": "string",
  "gross_amount": "number — in EUR",
  "withholding_tax_foreign": "number or null — Quellensteuer in EUR",
  "kapitalertragsteuer": "number",
  "solidaritaetszuschlag": "number",
  "kirchensteuer": "number or null",
  "net_amount": "number — in EUR",
  "source_document": "string",
  "scanned_at": "string"
}
```

### Writing to portfolio-state.json

```json
{
  "last_updated": "ISO timestamp",
  "brokers": [
    {
      "name": "string",
      "annual_statements": [],
      "portfolio_statements": [],
      "trades": [],
      "dividends": []
    }
  ]
}
```

When adding data:
1. Group by broker — find or create the broker entry
2. Append to the appropriate array within that broker
3. For annual statements, check if one for the same year already exists — warn if so
4. Always update `last_updated`

---

## Tax / Income / Official Documents → `workspace/tax-state.json`

### Lohnsteuerbescheinigung

Extract into the existing `persons[].employers[]` structure as defined by the steuer-intake skill. Fields:

```json
{
  "employer_name": "string",
  "period": "string — e.g., 01.01.2025-31.12.2025",
  "tax_class": "string — I/II/III/IV/V/VI",
  "kinderfreibetraege": "number",
  "church_member": "boolean",
  "church_tax_rate_pct": "number or null",
  "brutto": "number — Zeile 3 Bruttoarbeitslohn",
  "lohnsteuer": "number",
  "soli": "number",
  "kirchensteuer": "number",
  "rv_an": "number — employee pension contribution",
  "av_an": "number — employee unemployment contribution",
  "kv_an": "number — employee health insurance contribution",
  "pv_an": "number — employee care insurance contribution",
  "rv_ag": "number — employer pension contribution",
  "ag_zuschuss_kv_pv": "number — employer health/care subsidy",
  "pauschal_fahrtkosten_ag": "number",
  "bav": "number — employer bAV contribution"
}
```

### Steuerbescheid (Tax Assessment)

```json
{
  "tax_year": "number",
  "finanzamt": "string",
  "steuernummer": "string",
  "assessed_einkommensteuer": "number",
  "assessed_soli": "number",
  "assessed_kirchensteuer": "number or null",
  "zve": "number — zu versteuerndes Einkommen",
  "refund_or_payment": "number — positive = refund, negative = Nachzahlung",
  "assessment_date": "string — YYYY-MM-DD",
  "source_document": "string",
  "scanned_at": "string"
}
```

### Vorauszahlungsbescheid (Prepayment Assessment)

```json
{
  "finanzamt": "string",
  "steuernummer": "string",
  "applicable_from": "string — YYYY-MM-DD",
  "quarterly_payments": {
    "q1_mar": "number",
    "q2_jun": "number",
    "q3_sep": "number",
    "q4_dec": "number"
  },
  "source_document": "string",
  "scanned_at": "string"
}
```

### Gehaltsabrechnung (Payslip)

```json
{
  "employer": "string",
  "month": "string — YYYY-MM",
  "brutto": "number",
  "netto": "number",
  "lohnsteuer": "number",
  "soli": "number",
  "kirchensteuer": "number or null",
  "rv": "number",
  "av": "number",
  "kv": "number",
  "pv": "number",
  "sonderzahlungen": "number or null — bonuses, holiday pay",
  "source_document": "string",
  "scanned_at": "string"
}
```

### Nebenkostenabrechnung (Service Charge Statement)

```json
{
  "property_address": "string",
  "period": "string — e.g., 01.01.2025-31.12.2025",
  "total_nebenkosten": "number",
  "nachzahlung_or_guthaben": "number — positive = Guthaben (credit), negative = Nachzahlung",
  "haushaltsnahe_dienstleistungen": "number or null — tax-deductible portion (20% up to 4000 EUR credit)",
  "handwerkerleistungen": "number or null — tax-deductible portion (20% up to 1200 EUR credit)",
  "breakdown": {
    "heizkosten": "number or null",
    "wasser": "number or null",
    "muellabfuhr": "number or null",
    "hausmeister": "number or null",
    "other": "number or null"
  },
  "source_document": "string",
  "scanned_at": "string"
}
```

### Kindergeld-Bescheid

```json
{
  "kindergeldnummer": "string",
  "monthly_amount_per_child": "number",
  "number_of_children": "number",
  "effective_date": "string — YYYY-MM-DD",
  "familienkasse": "string",
  "source_document": "string",
  "scanned_at": "string"
}
```

### Elterngeld-Bescheid

```json
{
  "monthly_amount": "number",
  "benefit_type": "string — basiselterngeld/elterngeld_plus/partnerschaftsbonus",
  "bezugszeitraum": "string — e.g., Lebensmonate 3-14",
  "bemessungsgrundlage": "number or null — income basis for calculation",
  "source_document": "string",
  "scanned_at": "string"
}
```

### Finanzamt Correspondence

```json
{
  "finanzamt": "string",
  "date": "string — YYYY-MM-DD",
  "steuernummer": "string or null",
  "subject": "string — brief description of the letter's purpose",
  "deadline": "string or null — YYYY-MM-DD if a response deadline is mentioned",
  "amounts_mentioned": ["array of numbers or null"],
  "action_required": "boolean",
  "source_document": "string",
  "scanned_at": "string"
}
```

### Writing to tax-state.json

When writing tax-related data:
1. Load the existing `workspace/tax-state.json`
2. For Lohnsteuerbescheinigungen, merge into the `persons[].employers[]` array following the steuer-intake schema
3. For Steuerbescheide and other tax documents, add to a `tax_documents` array at the root level (create if missing)
4. For Gehaltsabrechnungen, add to an `income_records` array (create if missing)
5. For Nebenkostenabrechnungen, add the haushaltsnahe/Handwerker amounts to the `deductions` section if applicable
6. For official documents (Kindergeld, Elterngeld, Finanzamt), add to an `official_documents` array (create if missing)
7. Always update `last_updated`
8. Never overwrite existing data — merge and append

---

## Banking Documents → `workspace/bank-state.json`

### Categorize-Rollup-Present-Correct Flow (Kontoauszug and Kreditkartenabrechnung)

These two document types require an additional categorization step after the standard classify-approve flow. After reading all transactions:

**Step 1 — Categorize each transaction:**

Match each transaction's description/Verwendungszweck against the following, in priority order:
1. Learned patterns from `bank-state.json` > `category_corrections` (highest priority — user-confirmed)
2. Insurance provider names from `insurance-state.json` > `policies[].provider` → `versicherungen`
3. Own-account IBANs from `bank-state.json` > `accounts[].iban` → `ueberweisungen_intern`
4. Credit card lump payment patterns (e.g., "DEUTSCHE BANK KREDITKARTE", "ING KREDITKARTE") → `kreditkarte`
5. Known merchant patterns (see below) → assigned category

**Known merchant patterns (default, not exhaustive):**

| Category | Pattern examples |
|----------|-----------------|
| `lebensmittel` | REWE, EDEKA, LIDL, ALDI, PENNY, NETTO, KAUFLAND, REAL, BIO COMPANY |
| `transport` | BVG, DB BAHN, DEUTSCHE BAHN, TIER, LIME, BIRD, MVV, HVV, FLIXBUS |
| `restaurants` | LIEFERANDO, WOLT, DELIVEROO, UBER EATS, restaurant names |
| `kinderbetreuung` | KITA, KINDERGARTEN, KINDER, JUGENDAMT |
| `gesundheit` | APOTHEKE, PHARMACY, ARZT, ZAHNARZT, OPTIKER |
| `kleidung` | ZALANDO, H&M, NEW YORKER, ZARA, C&A, PRIMARK, ABOUT YOU |
| `haushalt` | IKEA, DM, ROSSMANN, MUELLER, OBI, BAUHAUS, HORNBACH |
| `abos_subscriptions` | NETFLIX, SPOTIFY, AMAZON PRIME, AMAZON*, DISNEY, APPLE.COM, URBAN SPORTS |
| `freizeit` | cinema names, EVENTIM, TICKETMASTER, sport shops |
| `miete` | landlord name from profile, BUWOG, VONOVIA, DEUTSCHE WOHNEN |

If no pattern matches → assign `sonstiges`.

**Step 2 — Roll up into monthly category totals:**

Sum all debit transactions per category for the statement period. Exclude `ueberweisungen_intern` and `kreditkarte` from expense totals (they are internal movements, not real spending).

**Step 3 — Present categorized summary to user:**

```
Kontoauszug — Deutsche Bank, December 2025
47 transactions | Opening: 3,100.00 | Closing: 3,420.50

Category              |  Amount  | Txns | Notes
----------------------+----------+------+------------------
Miete                 | 1,200.00 |    1 |
Lebensmittel          |   520.00 |   12 |
Kinderbetreuung       |   450.00 |    1 |
Restaurants           |   210.00 |    8 |
Versicherungen        |   180.00 |    3 | Learned
Abos/Subscriptions    |    95.00 |    4 |
Transport             |    85.00 |    6 |
Haushalt              |    65.00 |    2 |
Freizeit              |    90.00 |    3 |
Gesundheit            |    35.00 |    1 |
Kleidung              |   120.00 |    2 |
Kreditkarte           |   850.00 |    1 | excluded from total
Intern (own accounts) |     0.00 |    0 | excluded from total
Sonstiges             |   829.50 |    4 |
─────────────────────────────────────────
Total expenses        | 3,879.50

Uncategorized (sonstiges) — please review:
  - "PAYPAL MUSTERMANN"  →  45.00 EUR — what category?
  - "AMAZON EU SARL"     →  89.50 EUR — what category?
  - "UNBEKANNT GMBH"     → 120.00 EUR — what category?
  - "SONSTIGER POSTEN"   → 575.00 EUR — what category?
```

**Step 4 — User corrects uncategorized items:**

For each item the user assigns a category to:
1. Record a correction in `bank-state.json` > `category_corrections`:
   ```json
   {
     "bank": "Deutsche Bank",
     "original_category": "sonstiges",
     "corrected_to": "kinderbetreuung",
     "pattern": "KITA SONNENSCHEIN",
     "corrected_at": "2026-04-12T00:00:00Z"
   }
   ```
2. Re-categorize that transaction and update the rollup totals
3. These patterns are applied automatically on all future scans

**Step 5 — Write to bank-state.json:**

Add a `monthly_summaries` entry (or update if already exists for that month) under the matching account.

---

### Kontoauszug (Bank Statement)

```json
{
  "bank": "string — bank name",
  "owner": "string — account holder name",
  "iban": "string — account IBAN",
  "account_type": "string — girokonto/tagesgeld/festgeld",
  "statement_period": "string — e.g., 2025-12-01 to 2025-12-31",
  "statement_number": "string or null — Auszug Nr.",
  "opening_balance": "number — in EUR",
  "closing_balance": "number — in EUR",
  "monthly_summary": {
    "month": "string — YYYY-MM",
    "total_income": "number — sum of all credit transactions in EUR",
    "total_expenses": "number — sum of all debit transactions excluding ueberweisungen_intern and kreditkarte",
    "savings": "number — total_income minus total_expenses",
    "categories": {
      "miete": "number",
      "lebensmittel": "number",
      "transport": "number",
      "versicherungen": "number",
      "abos_subscriptions": "number",
      "restaurants": "number",
      "kinderbetreuung": "number",
      "gesundheit": "number",
      "kleidung": "number",
      "haushalt": "number",
      "freizeit": "number",
      "kreditkarte": "number — excluded from expense total",
      "ueberweisungen_intern": "number — excluded from expense total",
      "sonstiges": "number"
    },
    "corrections": ["array — user corrections applied during this scan"],
    "source_document": "string — file path"
  },
  "source_document": "string — file path",
  "scanned_at": "string — ISO timestamp"
}
```

### Zinsbescheinigung (Interest Certificate)

```json
{
  "bank": "string — bank name",
  "owner": "string — account holder name",
  "iban": "string or null — if shown",
  "year": "number — tax year e.g. 2025",
  "total_interest_earned": "number — Zinsertraege in EUR",
  "interest_rate_pct": "number or null — if shown",
  "tax_withheld": {
    "kapitalertragsteuer": "number — in EUR",
    "solidaritaetszuschlag": "number — in EUR",
    "kirchensteuer": "number or null — in EUR"
  },
  "freistellungsauftrag_used": "number — amount of Sparerpauschbetrag used at this bank in EUR",
  "source_document": "string — file path",
  "scanned_at": "string — ISO timestamp"
}
```

### Kontoabschluss (Account Closing Statement)

```json
{
  "bank": "string — bank name",
  "owner": "string — account holder name",
  "iban": "string or null — if shown",
  "period": "string — e.g., Q4 2025 or 2025-10-01 to 2025-12-31",
  "fees_charged": "number — Kontofuehrungsgebuehren in EUR",
  "interest_credited": "number — in EUR",
  "closing_balance": "number — in EUR",
  "source_document": "string — file path",
  "scanned_at": "string — ISO timestamp"
}
```

### Tagesgeld-Auszug (Savings Account Statement)

```json
{
  "bank": "string — bank name",
  "owner": "string — account holder name",
  "iban": "string or null — if shown",
  "account_type": "tagesgeld",
  "statement_period": "string — e.g., 2025-12-01 to 2025-12-31",
  "balance": "number — closing balance in EUR",
  "interest_rate_pct": "number — annual interest rate as percentage",
  "interest_earned_period": "number — interest earned in this statement period in EUR",
  "source_document": "string — file path",
  "scanned_at": "string — ISO timestamp"
}
```

### Kreditkartenabrechnung (Credit Card Statement)

```json
{
  "bank": "string — issuing bank name",
  "owner": "string — cardholder name",
  "card_number_last4": "string — last 4 digits of card number",
  "card_type": "string — Visa/Mastercard",
  "linked_iban": "string or null — Girokonto IBAN the balance is debited to",
  "statement_period": "string — e.g., 2025-12-01 to 2025-12-31",
  "debit_date": "string or null — YYYY-MM-DD when total is debited to Girokonto",
  "total_charged": "number — Gesamtbetrag in EUR",
  "monthly_summary": {
    "month": "string — YYYY-MM",
    "categories": {
      "miete": "number",
      "lebensmittel": "number",
      "transport": "number",
      "versicherungen": "number",
      "abos_subscriptions": "number",
      "restaurants": "number",
      "kinderbetreuung": "number",
      "gesundheit": "number",
      "kleidung": "number",
      "haushalt": "number",
      "freizeit": "number",
      "sonstiges": "number"
    },
    "corrections": ["array — user corrections applied during this scan"],
    "source_document": "string — file path"
  },
  "source_document": "string — file path",
  "scanned_at": "string — ISO timestamp"
}
```

### Writing to bank-state.json

```json
{
  "last_updated": "ISO timestamp",
  "accounts": [
    {
      "bank": "string",
      "owner": "string",
      "iban": "string",
      "account_type": "string — girokonto/tagesgeld/festgeld",
      "status": "string — active/closed/transitioning",
      "linked_credit_cards": [],
      "balances": [],
      "interest": [],
      "monthly_summaries": []
    }
  ],
  "category_corrections": []
}
```

When adding data:
1. Find the matching account by IBAN (or bank + owner + account_type if IBAN not available)
2. If no matching account exists, create a new entry in the `accounts` array
3. For Kontoauszug: add or update the `monthly_summaries` entry for the statement month; update `balances` with the closing balance
4. For Zinsbescheinigung: add or update the `interest` entry for the tax year
5. For Kontoabschluss: add closing balance to `balances`; record fees and interest
6. For Tagesgeld-Auszug: update `balances` and add interest to the `interest` entry for the year
7. For Kreditkartenabrechnung: find the linked account by IBAN, add or update `linked_credit_cards[].monthly_statements`
8. Append new `category_corrections` from user corrections — never remove existing ones
9. Always update `last_updated`
10. Never overwrite existing data — merge and append
