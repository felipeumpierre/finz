---
name: steuer-deductions
description: >
  Interactive interview skill to help identify all tax-deductible expenses for a German
  Einkommensteuererklärung. Use this skill after income data has been captured (via steuer-intake)
  and the user needs help figuring out what they can deduct. Covers Werbungskosten, Sonderausgaben,
  außergewöhnliche Belastungen, haushaltsnahe Dienstleistungen, Handwerkerleistungen,
  Vorsorgeaufwendungen, Kinderbetreuungskosten, and more. Trigger when the user asks about deductions,
  absetzbar, Werbungskosten, what they can claim, or how to reduce their tax burden.
---

# Steuer Deductions — Interactive Expense Interview

This skill conducts a structured but conversational interview to uncover all deductible expenses. The goal is to be thorough without being overwhelming — ask one category at a time, explain what qualifies, and give concrete examples so the user can identify expenses they might not have thought of.

## Interview Principles

- **One category at a time.** Don't dump all categories at once.
- **Lead with examples.** Instead of "Do you have Werbungskosten?", ask "Did you commute to an office? Buy work equipment? Pay for training courses?"
- **Explain thresholds.** Many deductions only matter above certain amounts (e.g., Werbungskosten above the 1,230€ Pauschbetrag). Tell the user early so they can gauge whether it's worth itemizing.
- **Track running totals.** After each category, show what's been captured so far.
- **Both spouses.** If filing jointly, ask about each person's expenses separately — Werbungskosten are person-specific.

## Deduction Categories

### 1. Werbungskosten (Work-Related Expenses) — Anlage N

The Arbeitnehmer-Pauschbetrag is 1,230€ (as of 2023+). Only worth itemizing if total Werbungskosten exceed this.

Ask about each subcategory:

**Entfernungspauschale (Commuting)**
- Distance from home to primary workplace (einfache Entfernung in km)
- Number of working days actually commuted (not home office days)
- Formula: first 20 km × 0.30€ × days + remaining km × 0.38€ × days
- Important: Check Zeile 18 of Lohnsteuerbescheinigung — if employer paid pauschal Fahrtkostenzuschuss, this reduces the deduction
- Public transport: If Jobticket cost exceeds Entfernungspauschale, the higher amount can be claimed
- Ask: "How far is your workplace from home? How many days per week did you go in (vs. home office)?"

**Home Office (Homeoffice-Pauschale)**
- 6€ per day worked from home, max 1,260€/year (210 days)
- Since 2023, no separate room required for the Pauschale
- If a dedicated room exists (häusliches Arbeitszimmer), full costs may be deductible instead — but stricter requirements
- Ask: "How many days did you work from home? Do you have a dedicated room used exclusively for work?"

**Work Equipment (Arbeitsmittel)**
- Computer, laptop, monitor, desk, chair, software, tools
- Items under 800€ net (952€ gross) can be deducted immediately
- Items over 800€ net must be depreciated (e.g., laptop over 3 years — but since 2021, digital assets can be written off in one year per BMF letter)
- Partial private use: estimate work-use percentage (common: 50-90% for a personal laptop)
- Ask: "Did you buy any work equipment — computer, desk, office chair, software, tools? Even if you also use them privately, a portion may be deductible."

**Professional Development (Fort- und Weiterbildung)**
- Course fees, seminar costs, exam fees
- Travel costs to training locations
- Study materials, textbooks
- Must be related to current or intended future employment
- Ask: "Did you attend any courses, seminars, or training? Buy professional books or subscriptions?"

**Professional Memberships & Unions**
- Gewerkschaftsbeiträge (union dues)
- Berufsverbände (professional associations)
- Ask: "Are you a member of a union or professional association?"

**Work-Related Travel (Dienstreisen)**
- If not reimbursed by employer: travel costs, hotel, Verpflegungsmehraufwand (meal allowances)
- Verpflegungspauschale: 14€ for 8-24h absence, 28€ for 24h+ absence
- Ask: "Did you have business trips that your employer didn't fully reimburse?"

**Application Costs (Bewerbungskosten)**
- If the user applied for jobs: postage, printing, travel to interviews
- Flat rate often accepted: ~8.50€ per written application, ~15€ per online application (varies by Finanzamt)
- Ask: "Did you apply for any jobs this year?"

**Double Household (Doppelte Haushaltsführung)**
- If maintaining a second household for work: rent (up to 1,000€/month), one trip home per week
- Complex rules about "eigener Hausstand" — flag for Steuerberater if applicable
- Ask: "Do you maintain a second home because your workplace is far from your family home?"

### 2. Sonderausgaben (Special Expenses) — Anlage Vorsorgeaufwand & Others

**Vorsorgeaufwendungen (Insurance & Pension)**
Most of these are already on the Lohnsteuerbescheinigung. Additional items:
- Private health insurance (Krankenversicherung) and long-term care (Pflegeversicherung) — Basisabsicherung is fully deductible
- Supplementary insurance: Zahnzusatzversicherung, Auslandskrankenversicherung — limited deductibility
- Rürup-Rente (Basisrente) contributions
- Riester contributions (with Anlage AV for Zulagenberechnung)
- Berufsunfähigkeitsversicherung, Unfallversicherung, Haftpflichtversicherung
- Ask: "Do you have any private insurance beyond what's covered by your employer? Riester or Rürup pension? Disability insurance?"

**Kirchensteuer**
- Already captured from Lohnsteuerbescheinigung — automatically deductible as Sonderausgabe
- If additionally paid directly (e.g., on capital gains), capture that too

**Spenden und Mitgliedsbeiträge (Donations)**
- Donations to recognized charitable organizations (must have Zuwendungsbestätigung)
- Political party contributions (special rules, partially as direct tax reduction)
- Up to 20% of total income is deductible
- Ask: "Did you make any donations this year? To charities, political parties, churches, disaster relief?"

**Ausbildungskosten (Education)**
- First degree/Erstausbildung: up to 6,000€ as Sonderausgaben
- Second degree/Zweitausbildung: fully deductible as Werbungskosten (see above)
- Ask: "Are you or your spouse currently studying or in training?"

### 3. Kinder (Children) — Anlage Kind

One Anlage Kind per child. Capture:

- **Name, date of birth, tax ID** (Steuer-IdNr) of each child
- **Kindergeld received**: Amount and recipient (determines who gets Kinderfreibetrag if applicable)
- **Kinderbetreuungskosten** (childcare costs for children under 14):
  - Kita, Tagesmutter, Au-pair, Babysitter, Hort
  - 2/3 of costs deductible, max 4,000€ per child per year
  - Must be paid by bank transfer (not cash!)
  - Ask: "How much did you pay for childcare — Kita, babysitter, after-school care?"
- **School fees** (Schulgeld) for private schools: 30% deductible, max 5,000€
- **Entlastungsbetrag für Alleinerziehende**: if applicable (single parent in Steuerklasse II)
- **Child's own income**: Relevant if child is over 18 and still eligible

### 4. Außergewöhnliche Belastungen (Extraordinary Burdens) — Mantelbogen

These are deductible above a threshold (zumutbare Belastung) that depends on income, marital status, and number of children (typically 1-7% of income).

- **Medical expenses** not covered by insurance: glasses, dental work, hearing aids, therapies, medications (with prescription), hospital stays
- **Disability** (Behinderung): Pauschbetrag based on degree of disability (Grad der Behinderung), or actual costs
- **Care costs** (Pflege): Costs for caring for a dependent, Pflege-Pauschbetrag
- **Funeral costs**: If estate doesn't cover them, up to ~7,500€
- **Divorce costs**: No longer deductible since 2013 (common misconception)
- Ask: "Did you have significant medical expenses not covered by insurance? Does anyone in the family have a disability? Did you care for a dependent?"

### 5. Haushaltsnahe Dienstleistungen & Handwerkerleistungen — Mantelbogen

These are direct tax reductions (Steuerermäßigung), not deductions from income — very valuable!

**Haushaltsnahe Dienstleistungen (§35a Abs. 2 EStG)**
- Cleaning service, gardening, pet sitting, elder care at home
- 20% of labor costs deductible from tax, max 4,000€ tax reduction
- Must be invoiced and paid by bank transfer
- Ask: "Do you have a cleaning service, gardener, or anyone who helps in your household?"

**Haushaltsnahe Beschäftigungsverhältnisse (§35a Abs. 1 EStG)**
- Minijob in household (e.g., cleaning on Minijob basis): 20%, max 510€
- Sozialversicherungspflichtige Beschäftigung: 20%, max 4,000€

**Handwerkerleistungen (§35a Abs. 3 EStG)**
- Renovations, repairs, maintenance IN or AT the household
- 20% of labor costs (not materials!), max 1,200€ tax reduction
- Examples: painter, plumber, electrician, chimney sweep, IT technician for home network
- Nebenkostenabrechnung: portion of Handwerker and haushaltsnahe Leistungen from the landlord's utility bill is deductible!
- Ask: "Did you have any craftsmen or repair work done at home? Do you rent — if so, check your Nebenkostenabrechnung for Handwerker and Hausmeister costs."

### 6. Freelance / Self-Employment Deductions

If the user had freelance income (captured in steuer-intake), relevant deductions include:

- Home office costs (may already be claimed under Werbungskosten — cannot double-claim)
- Professional equipment and software
- Travel to clients
- Professional insurance (Berufshaftpflicht)
- Advertising/marketing costs
- Phone and internet (business-use portion)
- Accounting software or Steuerberater fees for the business portion
- Ask: "For your freelance work, what expenses did you have? Equipment, travel, software, insurance?"

## After the Interview

### Compile and Summarize

Present all captured deductions in a clear overview:

```
═══ Deductions Summary: Max & Erika Mustermann — Tax Year 2025 ═══

MAX — Werbungskosten:
  Entfernungspauschale (25km × 210 days):    1,950.00 €
  Home Office (45 days × 6€):                  270.00 €
  Laptop (80% work use):                       960.00 €
  Professional training:                       450.00 €
  Union dues:                                  180.00 €
  ─────────────────────────────────────────
  Total Werbungskosten:                      3,810.00 €
  vs. Pauschbetrag (1,230€):              +  2,580.00 € benefit

ERIKA — Werbungskosten:
  Entfernungspauschale (15km × 220 days):      990.00 €
  Home Office (0 days):                          0.00 €
  ─────────────────────────────────────────
  Total Werbungskosten:                        990.00 €
  vs. Pauschbetrag (1,230€):                 Pauschbetrag is higher, no itemization needed

JOINT — Sonderausgaben:
  Kirchensteuer (from LStB):                 1,352.32 €
  Donations:                                   500.00 €
  Riester (Max):                             2,100.00 €

JOINT — Kinder:
  Kinderbetreuungskosten:                    3,600.00 €
    → Deductible (2/3, max 4,000€):          2,400.00 €

JOINT — Haushaltsnahe Leistungen:
  Cleaning service (labor):                  2,400.00 €
    → Tax reduction (20%):                     480.00 €
  Handwerker – bathroom repair (labor):      1,800.00 €
    → Tax reduction (20%):                     360.00 €
```

### Handoff

Pass the structured deductions data to `steuer-documents` (for document checklist) and `steuer-calculator` (for tax estimation).
