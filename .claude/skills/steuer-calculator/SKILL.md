---
name: steuer-calculator
description: >
  Estimate German income tax liability and optimize filing strategy. Use this skill after income
  and deduction data have been captured (via steuer-intake and steuer-deductions). It calculates
  estimated Einkommensteuer, compares Zusammenveranlagung vs. Einzelveranlagung, runs the
  Günstigerprüfung for Kindergeld vs. Kinderfreibetrag, and produces a summary. Trigger when the
  user asks about how much tax they owe, their expected refund (Steuererstattung), or wants to
  compare filing strategies.
---

# Steuer Calculator — Tax Estimation & Optimization

This skill takes the structured income and deduction data from the previous skills and produces a tax estimate. It compares filing strategies and identifies optimization opportunities.

## Important Caveats

- This is an **estimate**, not a binding calculation. The actual Steuerbescheid from the Finanzamt is definitive.
- Tax law changes frequently. All numeric parameters (Grundfreibetrag, brackets, caps, Kindergeld, Kinderfreibetrag, §35a caps, Soli Freigrenze, Altersvorsorge-Höchstbetrag, etc.) are kept in `references/tax-parameters.md`. All §32a polynomial coefficients are in `references/st32a-coefficients.md`. **Never hardcode numbers in calculation code — always read them from the reference files.**
- For complex situations (foreign income, crypto, separation, losses from previous years), recommend a Steuerberater.

## Tax Calculation Steps

### Step 1: Determine zu versteuerndes Einkommen (Taxable Income)

For each person (and jointly if Zusammenveranlagung):

```
  Bruttoarbeitslohn (from Lohnsteuerbescheinigung)
+ Freelance profit (Gewinn aus selbständiger Arbeit)
+ Other income (Vermietung, Kapital, Sonstige)
= Summe der Einkünfte

- Altersentlastungsbetrag (if applicable, for persons born before 1975)
- Entlastungsbetrag für Alleinerziehende (if applicable)
= Gesamtbetrag der Einkünfte

- Sonderausgaben (see below)
- Außergewöhnliche Belastungen (above zumutbare Belastung)
- Verlustabzug (if applicable)
= Einkommen

- Kinderfreibeträge (if Günstigerprüfung favors it)
- Härteausgleich (if applicable)
= zu versteuerndes Einkommen (zvE)
```

### Step 2: Calculate Sonderausgaben

**Vorsorgeaufwendungen (Pension & Insurance)**

Altersvorsorge (gesetzliche RV + berufsständische Versorgung + Rürup):
- 100% of contributions deductible up to the Höchstbetrag (since 2023).
- Year-specific Höchstbetrag values: see `references/tax-parameters.md` (section "Altersvorsorge-Höchstbetrag — §10 Abs. 3 EStG").
- For employees, add employer + employee RV contributions together; then subtract the employer share per §10 Abs. 3 Satz 5 EStG.

Sonstige Vorsorgeaufwendungen (health, care, disability, liability, term life):
- Kranken- und Pflegeversicherung (Basisabsicherung) is fully deductible regardless of cap.
- Other insurance categories share a cap that differs for employees (with tax-free KV subsidy) vs. self-employed. Values: see `references/tax-parameters.md` (section "Sonstige Vorsorgeaufwendungen cap").
- For most employees the cap is already exhausted by KV/PV Basisabsicherung, so additional private insurance rarely adds deductible amount.

**Other Sonderausgaben**
- Kirchensteuer: fully deductible (§10 Abs. 1 Nr. 4 EStG).
- Spenden: up to 20% of Gesamtbetrag der Einkünfte (§10b EStG).
- Kinderbetreuungskosten: deductible share and per-child cap changed in 2025 — see `references/tax-parameters.md` (section "Kinderbetreuungskosten").
- Ausbildungskosten (Erstausbildung): up to 6,000 EUR (§10 Abs. 1 Nr. 7 EStG).
- Riester: Sonderausgabenabzug up to 2,100 EUR (§10a EStG); Finanzamt runs a Günstigerprüfung against the Zulagenförderung automatically.

If none of these exceed the Sonderausgaben-Pauschbetrag (see `references/tax-parameters.md`), the Pauschbetrag applies. In practice, Vorsorgeaufwendungen alone almost always exceed it.

### Step 3: Calculate Außergewöhnliche Belastungen

First, determine the **zumutbare Belastung** (reasonable burden threshold):

The threshold is calculated in tiers based on Gesamtbetrag der Einkünfte:

| Income tier | No children, single | No children, married | 1-2 children | 3+ children |
|---|---|---|---|---|
| Up to 15,340€ | 5% | 4% | 2% | 1% |
| 15,341€ – 51,130€ | 6% | 5% | 3% | 1% |
| Over 51,130€ | 7% | 6% | 4% | 2% |

The threshold is calculated progressively (each tier applies only to the income within that range).

Only the portion of außergewöhnliche Belastungen exceeding this threshold is deductible.

### Step 4: Apply the German Income Tax Formula

The Einkommensteuer is calculated using the formula defined in §32a EStG. The formula changes annually — use the correct year's coefficients.

- Grundfreibetrag and the 42% / 45% thresholds per year: `references/tax-parameters.md` (section "Grundfreibetrag" and "Top-rate thresholds").
- Full polynomial coefficients (Progressionszone 1, Progressionszone 2, Proportionalzone 1, Reichensteuer) per year: `references/st32a-coefficients.md`.

The five-zone structure is stable across years (Nullzone → Progressionszone 1 quadratic in `y` → Progressionszone 2 quadratic in `z` → 42% linear → 45% linear). Only the coefficients and threshold values change annually. Round `zvE` down to full euros before applying the formula; round the result down to full euros (§32a Abs. 1 Sätze 5–6 EStG).

For **Zusammenveranlagung**, apply the Splittingverfahren:
1. Add both spouses' zvE together
2. Divide by 2
3. Apply the single-person tariff to the halved amount
4. Multiply the result by 2

This is the core advantage of Zusammenveranlagung — it benefits couples with unequal incomes.

**Solidaritätszuschlag**: 5.5% of assessed Einkommensteuer, charged only above a Freigrenze and phased in via a Milderungszone above that. The Freigrenze changes annually — see `references/tax-parameters.md` (section "Solidaritätszuschlag Freigrenze"). For TY 2025 it was raised substantially compared to 2024 via the Steuerfortentwicklungsgesetz; do not use pre-2025 values.

**Kirchensteuer**: 8% (Bayern, Baden-Württemberg) or 9% (all other 14 Bundesländer) of assessed Einkommensteuer. Table: `references/tax-parameters.md` (section "Kirchensteuer rate"). Kirchensteuer paid is itself a Sonderausgabe (§10 Abs. 1 Nr. 4 EStG).

### Step 5: Calculate Steuerermäßigungen (Direct Tax Reductions)

These reduce the final tax bill directly (not the taxable income). All three sub-sections of §35a EStG apply 20% of qualifying costs up to a per-category cap. Exact caps and scope: `references/tax-parameters.md` (section "§35a caps — haushaltsnahe Dienstleistungen & Handwerker").

- §35a Abs. 1 — Minijob household employment
- §35a Abs. 2 — Haushaltsnahe Dienstleistungen, sozialversicherungspflichtige Haushaltsbeschäftigung, Pflege/Betreuung
- §35a Abs. 3 — Handwerkerleistungen (labour cost only; no materials)

The caps are per Haushalt, not per person — Zusammenveranlagung does not double them.

### Step 6: Günstigerprüfung — Kindergeld vs. Kinderfreibetrag

The Finanzamt automatically checks which is better (§31 EStG), but we should estimate the outcome for the summary.

- Kindergeld monthly amounts per year: `references/tax-parameters.md` (section "Kindergeld"). Annual amount = 12 × monthly.
- Kinderfreibetrag + BEA-Freibetrag (combined per child, both parents): `references/tax-parameters.md` (section "Kinderfreibetrag + BEA-Freibetrag").

The calculation:
1. Estimate the tax savings if the combined-per-child Kinderfreibetrag is deducted from zvE (re-run §32a on the reduced zvE).
2. Compare against annual Kindergeld received.
3. Whichever is larger wins. If Kinderfreibetrag wins, the net additional benefit vs. Kindergeld is added to the refund; the already-paid Kindergeld is offset against the tax savings (Hinzurechnung).

Rule of thumb (only a rough indicator, always run the actual numbers from the reference table for the filing year): Kinderfreibetrag tends to be more favourable once joint zvE is in the upper 40% marginal-rate range or above.

### Step 7: Compare Filing Strategies

**Zusammenveranlagung vs. Einzelveranlagung**

Calculate the tax for both scenarios:

1. **Zusammenveranlagung**: Combined income, Splitting, shared deductions
2. **Einzelveranlagung**: Each spouse files separately, each claims their own deductions

Present the comparison:

```
═══ Filing Strategy Comparison: Tax Year 2025 ═══

ZUSAMMENVERANLAGUNG (Joint Filing)
  Combined zvE:                    85,000.00 €
  Einkommensteuer (Splitting):     15,836.00 €
  Solidaritätszuschlag:                 0.00 €
  Kirchensteuer:                    1,425.24 €
  ─────────────────────────────────
  Total tax:                       17,261.24 €
  Already paid (Lohnsteuer etc.):  19,500.00 €
  §35a reductions:                    -840.00 €
  ═════════════════════════════════
  ESTIMATED REFUND:                 3,078.76 €

EINZELVERANLAGUNG (Separate Filing)
  Max zvE:                         55,000.00 €
  Max ESt:                         12,777.00 €
  Erika zvE:                       30,000.00 €
  Erika ESt:                        4,590.00 €
  ─────────────────────────────────
  Combined tax:                    17,367.00 €
  Already paid:                    19,500.00 €
  §35a reductions:                    -840.00 €
  ═════════════════════════════════
  ESTIMATED REFUND:                 2,973.00 €

  → RECOMMENDATION: Zusammenveranlagung saves ~105.76 € more

  Note: Einzelveranlagung can be beneficial in special cases:
  - One spouse has Progressionsvorbehalt income (Elterngeld, ALG I)
  - One spouse has high außergewöhnliche Belastungen
  - One spouse has losses that could be carried forward
```

### Step 8: Produce Summary

Generate a comprehensive summary document:

```
═══ STEUERERKLÄRUNG 2025 — ESTIMATE SUMMARY ═══
═══ Max & Erika Mustermann                   ═══

FILING STATUS: Zusammenveranlagung (recommended)
CHILDREN: 1 (Kinderfreibetrag applies — saves 947€ vs. Kindergeld)

INCOME
  Max — Employment:                 65,000.00 €
  Max — Freelance:                   8,000.00 €
  Erika — Employment:              38,000.00 €
  ─────────────────────────────────
  Total Income:                   111,000.00 €

DEDUCTIONS
  Max — Werbungskosten:             3,810.00 €
  Erika — Werbungskosten:          1,230.00 € (Pauschbetrag)
  Vorsorgeaufwendungen:            14,200.00 €
  Sonderausgaben:                   3,952.32 €
  Kinderbetreuung (2/3):            2,400.00 €
  ─────────────────────────────────
  Total Deductions:                25,592.32 €

TAX CALCULATION
  zu versteuerndes Einkommen:      85,407.68 €
  Einkommensteuer (Splitting):     15,920.00 €
  Solidaritätszuschlag:                 0.00 €
  Kirchensteuer:                    1,432.80 €
  minus §35a Ermäßigungen:           -840.00 €
  ─────────────────────────────────
  Final Tax:                       16,512.80 €

ALREADY PAID
  Lohnsteuer (both):               19,152.00 €
  Kirchensteuer (both):             1,352.32 €
  Soli (both):                          0.00 €
  Freelance Vorauszahlungen:        1,200.00 €
  ─────────────────────────────────
  Total Paid:                      21,704.32 €

  ═══════════════════════════════════
  ESTIMATED REFUND:       ~5,191.52 €
  ═══════════════════════════════════

OPTIMIZATION NOTES
  ✓ Zusammenveranlagung is optimal (saves ~106€ vs. Einzelveranlagung)
  ✓ Kinderfreibetrag applies (saves ~947€ vs. Kindergeld alone)
  ✓ §35a fully utilized
  ⚠ Consider Riester for Erika — could save up to ~600€ additional
  ⚠ Check if Erika's commute is actually >15km (even a few km more adds up)
```

## Implementation Notes

When implementing the actual tax formula, **always pull the coefficients from `references/st32a-coefficients.md` for the filing year**. Do not inline numbers. Coefficients are year-specific and wrong by construction if mixed across years.

The general shape for any year:

```python
import math

def einkommensteuer(zve, coeffs):
    """
    zvE -> ESt for a single person, per §32a EStG.
    For Splittingverfahren: call einkommensteuer(combined_zvE / 2, coeffs) * 2.

    `coeffs` must be loaded from references/st32a-coefficients.md for the correct
    tax year. Required fields: grundfreibetrag, p1_upper, p42_start, p1_a, p2_start,
    p2_a, p2_b, p2_c, p42_b, p45_b.
    """
    zve = math.floor(zve)  # §32a Abs. 1 Satz 5 EStG
    if zve <= coeffs["grundfreibetrag"]:
        tax = 0
    elif zve <= coeffs["p1_upper"]:
        y = (zve - coeffs["grundfreibetrag"]) / 10000
        tax = (coeffs["p1_a"] * y + 1400) * y
    elif zve <= coeffs["p42_start"] - 1:
        z = (zve - coeffs["p2_start"]) / 10000
        tax = (coeffs["p2_a"] * z + 2397) * z + coeffs["p2_c"]
    elif zve <= 277825:
        tax = 0.42 * zve - coeffs["p42_b"]
    else:
        tax = 0.45 * zve - coeffs["p45_b"]
    return math.floor(tax)  # §32a Abs. 1 Satz 6 EStG
```

The concrete coefficient sets for TY 2023, 2024, 2025 and 2026 are given verbatim in `references/st32a-coefficients.md`. When a new tax year is released, add it to that file first (sourced to the BMF LStH/EStH for that year) before running estimates.

## Output

After presenting the summary, suggest next steps:

1. "Gather the documents from the checklist (see steuer-documents output)"
2. "You can file via ELSTER (elster.de) — it's free"
3. "Or take this summary to a Steuerberater or Lohnsteuerhilfeverein"
4. "Filing deadline: July 31 of the following year (or end of February two years later with a Steuerberater)"
5. "Would you like me to generate a detailed breakdown you can save?"
