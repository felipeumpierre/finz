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
- Tax law changes frequently. Always verify current rates, thresholds, and rules for the relevant tax year.
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

Altersvorsorge (Rentenversicherung + Rürup):
- Deductible: Beiträge × applicable percentage (100% since 2023)
- Maximum: 27,566€ per person (2025, check current year)
- Employee + employer RV contributions count toward this

Sonstige Vorsorgeaufwendungen (Health, disability, liability insurance):
- Kranken- und Pflegeversicherung (Basisabsicherung): fully deductible
- Other insurance: deductible within a cap of 1,900€ (employees) or 2,800€ (self-employed)
- The cap is usually already exhausted by KV/PV Basisabsicherung for most employees

**Other Sonderausgaben**
- Kirchensteuer: fully deductible
- Spenden: up to 20% of Gesamtbetrag der Einkünfte
- Kinderbetreuungskosten: 2/3 of costs, max 4,000€ per child
- Ausbildungskosten (Erstausbildung): up to 6,000€
- Riester: Sonderausgabenabzug up to 2,100€ (compare with Zulagenförderung)

If none of these exceed the Sonderausgaben-Pauschbetrag (36€ single / 72€ married), the Pauschbetrag applies. In practice, Vorsorgeaufwendungen alone almost always exceed this.

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

The Einkommensteuer is calculated using the formula defined in §32a EStG. The formula changes annually — use the correct year's formula.

**2025 Tax Brackets (approximate — verify for the specific tax year):**

| Taxable Income (zvE) | Tax Rate |
|---|---|
| Up to 12,096€ | 0% (Grundfreibetrag) |
| 12,097€ – 17,443€ | 14% – ~24% (progressive zone 1) |
| 17,444€ – 66,760€ | ~24% – 42% (progressive zone 2) |
| 66,761€ – 277,825€ | 42% |
| Over 277,825€ | 45% (Reichensteuer) |

For **Zusammenveranlagung**, apply the Splitting-Verfahren:
1. Add both spouses' zvE together
2. Divide by 2
3. Apply the tax formula to the halved amount
4. Multiply the result by 2

This is the core advantage of Zusammenveranlagung — it benefits couples with unequal incomes.

**Solidaritätszuschlag**: 5.5% of Einkommensteuer, but with a Freigrenze (since 2021):
- Single: no Soli if ESt ≤ 18,130€ (approximately, verify current threshold)
- Married/joint: no Soli if ESt ≤ 36,260€
- Above the threshold, Soli phases in gradually (Milderungszone)

**Kirchensteuer**: 8% (Bayern, Baden-Württemberg) or 9% (all other Bundesländer) of Einkommensteuer

### Step 5: Calculate Steuerermäßigungen (Direct Tax Reductions)

These reduce the final tax bill directly (not the taxable income):

- **Haushaltsnahe Beschäftigungsverhältnisse** (§35a Abs. 1): 20% of costs, max 510€
- **Haushaltsnahe Dienstleistungen** (§35a Abs. 2): 20% of labor costs, max 4,000€
- **Handwerkerleistungen** (§35a Abs. 3): 20% of labor costs, max 1,200€

Total §35a cap: 5,710€ combined

### Step 6: Günstigerprüfung — Kindergeld vs. Kinderfreibetrag

The Finanzamt automatically checks which is better (§31 EStG), but we should estimate:

- **Kindergeld 2025**: 255€/month per child (verify current amount) = 3,060€/year per child
- **Kinderfreibetrag 2025**: 6,612€ per child (Kinderfreibetrag) + 2,928€ (BEA-Freibetrag) = 9,540€ per child

The tax savings from the Kinderfreibetrag depend on the marginal tax rate:
- At 42% marginal rate: 9,540€ × 42% = ~4,007€ tax savings → Kinderfreibetrag is better
- At 25% marginal rate: 9,540€ × 25% = ~2,385€ tax savings → Kindergeld (3,060€) is better

Rule of thumb: For joint income above ~85,000€ zvE, the Kinderfreibetrag tends to be more advantageous.

If Kinderfreibetrag is better, the Finanzamt deducts the Kindergeld received from the tax savings. The difference is the net additional benefit.

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

When implementing the actual tax formula, use the official §32a EStG formula for the relevant year. The formula uses polynomial equations for the progressive zones. Here's the general structure (verify values for the specific year):

```python
def einkommensteuer_2025(zve):
    """Calculate ESt for a single person's zvE. For Splitting, pass zvE/2 and multiply result by 2."""
    if zve <= 12096:
        return 0
    elif zve <= 17443:
        y = (zve - 12096) / 10000
        return int((922.98 * y + 1400) * y)
    elif zve <= 66760:
        z = (zve - 17443) / 10000
        return int((181.19 * z + 2397) * z + 1025.38)
    elif zve <= 277825:
        return int(0.42 * zve - 10636.31)
    else:
        return int(0.45 * zve - 18971.06)
```

**Note:** These coefficients are approximate and for illustration. Always verify the exact formula from the official Einkommensteuergesetz for the filing year. The Bundesministerium der Finanzen publishes the exact parameters.

## Output

After presenting the summary, suggest next steps:

1. "Gather the documents from the checklist (see steuer-documents output)"
2. "You can file via ELSTER (elster.de) — it's free"
3. "Or take this summary to a Steuerberater or Lohnsteuerhilfeverein"
4. "Filing deadline: July 31 of the following year (or end of February two years later with a Steuerberater)"
5. "Would you like me to generate a detailed breakdown you can save?"
