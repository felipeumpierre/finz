---
name: steuer-intake
description: >
  Extract and structure income data from German tax documents, primarily Lohnsteuerbescheinigungen
  (wage tax certificates). Use this skill when the user uploads a Lohnsteuerbescheinigung PDF or image,
  or provides income data that needs to be structured for tax filing. Also use when the user mentions
  Lohnsteuerbescheinigung, Gehalt (salary), Bruttoarbeitslohn, Lohnsteuer, or any German payroll document.
  Handles both single and multiple documents (e.g., both spouses, multiple employers in one year).
---

# Steuer Intake — Income Document Extraction

This skill extracts structured data from German income tax documents, primarily the **Lohnsteuerbescheinigung** (annual wage tax certificate issued by employers).

## Profile Integration

Before starting the extraction process, check if `workspace/profile.json` exists. If it does, pre-populate personal details from the profile instead of asking the user again:

- **Person names, DOBs, tax IDs** → Use `profile.persons[]` to match extracted documents to the correct person
- **Tax class** → Cross-validate the Steuerklasse on the Lohnsteuerbescheinigung against `profile.persons[].tax_class`
- **Employer** → Cross-validate employer name against `profile.persons[].employer`
- **Address** → Use `profile.address` for the Steuererklärung header

If profile data conflicts with the document (e.g., different tax class), flag it to the user: "Your profile says Steuerklasse III, but this Lohnsteuerbescheinigung shows Steuerklasse IV. Which is correct for this tax year?" Update the profile if the user confirms a change.

If `workspace/portfolio-state.json` exists with investment data, mention it during income type collection: "I see you have investment data from your portfolio review — I can use that to pre-fill your Anlage KAP (capital gains declaration). Want me to pull that in?"

If no `profile.json` exists, continue with the normal extraction process below — no profile is required.

## What is a Lohnsteuerbescheinigung?

It's the document every employer in Germany must issue to each employee by the end of February for the previous tax year. It summarizes all payroll-relevant data: gross income, taxes withheld, social security contributions, and more. The data is also transmitted electronically to the Finanzamt.

## Extraction Process

### Step 1: Receive the Document

The user provides the Lohnsteuerbescheinigung as a PDF, image, or typed data. If it's a PDF or image, read it carefully and extract all numbered fields (Zeilen).

### Step 2: Extract Key Fields

The Lohnsteuerbescheinigung has numbered lines (Zeilen). Extract these critical fields:

**Employer & Personal Info (Header)**
- Employer name and Steuernummer
- Employee name
- Zeitraum (period — should be full year for annual filing)
- Steuerklasse (tax class: I, II, III, IV, V, VI)
- Kirchensteuermerkmale (church tax indicators: ev, rk, or none)
- Number of Kinderfreibeträge

**Income (Zeilen 1-10)**
- **Zeile 3**: Bruttoarbeitslohn (gross wages) — this is the most important number
- **Zeile 4**: Ermäßigt besteuerter Arbeitslohn (reduced-rate wages, e.g., severance)
- **Zeile 5**: Steuerfreier Arbeitslohn nach DBA (tax-free wages under double taxation agreements)
- **Zeile 6**: Steuerfreie Arbeitgeberleistungen für Zukunftssicherung
- **Zeile 8**: Kurzarbeitergeld or other wage replacement benefits (Progressionsvorbehalt!)

**Taxes Withheld (Zeilen 4-7 in tax section)**
- **Zeile 4 (Steuer)**: Einbehaltene Lohnsteuer
- **Zeile 5 (Steuer)**: Einbehaltener Solidaritätszuschlag
- **Zeile 6 (Steuer)**: Einbehaltene Kirchensteuer des Arbeitnehmers
- **Zeile 7 (Steuer)**: Einbehaltene Kirchensteuer des Ehegatten

**Social Security Contributions (Zeilen 22-28)**
- **Zeile 22a/22b**: Arbeitnehmeranteil Rentenversicherung (employee pension contribution)
- **Zeile 23a/23b**: Arbeitgeberanteil Rentenversicherung (employer pension contribution)
- **Zeile 25**: Arbeitnehmeranteil Arbeitslosenversicherung
- **Zeile 26**: Beiträge zur Krankenversicherung
- **Zeile 27**: Beiträge zur Pflegeversicherung
- **Zeile 28**: Arbeitgeberzuschuss zur Kranken-/Pflegeversicherung

**Other Important Fields**
- **Zeile 17**: Steuerfreie Verpflegungszuschüsse
- **Zeile 18**: Pauschalbesteuerte Arbeitgeberleistungen für Fahrten Wohnung-Arbeitsstätte
- **Zeile 20**: Arbeitgeberanteil zur betrieblichen Altersversorgung (bAV)
- **Zeile 35**: Aufwendungen für doppelte Haushaltsführung

### Step 3: Validate the Data

Run these sanity checks:

1. **Period check**: Is the Zeitraum a full year (01.01–31.12)? If not, flag it — there may be a second Lohnsteuerbescheinigung from another employer
2. **Tax class plausibility**: If married and filing jointly, typical combinations are III/V or IV/IV
3. **Lohnsteuer plausibility**: Lohnsteuer should be roughly 15–42% of Bruttoarbeitslohn minus Freibeträge, depending on tax class
4. **Soli check**: Solidaritätszuschlag is 5.5% of Lohnsteuer (but may be zero due to Freigrenze since 2021)
5. **Church tax check**: If Kirchensteuer > 0, the person is a church member (8% or 9% of Lohnsteuer depending on Bundesland)

### Step 4: Present the Extracted Data

Present the data in a clear, structured format. Group by person if there are multiple Lohnsteuerbescheinigungen. Example:

```
═══ Lohnsteuerbescheinigung: Max Mustermann ═══
Employer:           Muster GmbH
Period:             01.01.2025 – 31.12.2025
Tax Class:          III
Kinderfreibeträge:  1.0

INCOME
  Bruttoarbeitslohn (Z.3):          65,000.00 €
  Kurzarbeitergeld (Z.8):                0.00 €

TAXES WITHHELD
  Lohnsteuer:                        8,452.00 €
  Solidaritätszuschlag:                    0.00 €
  Kirchensteuer (AN):                   676.16 €

SOCIAL SECURITY (Employee Share)
  Rentenversicherung:                6,045.00 €
  Arbeitslosenversicherung:            845.00 €
  Krankenversicherung:               5,330.00 €
  Pflegeversicherung:                1,170.00 €

EMPLOYER CONTRIBUTIONS
  RV Arbeitgeberanteil:              6,045.00 €
  AG-Zuschuss KV/PV:                3,250.00 €
```

### Step 5: Confirm with User

After presenting, ask the user to verify the data is correct. Common issues:

- OCR misreading numbers (e.g., 1 vs. 7 in German fonts)
- Missing a second Lohnsteuerbescheinigung (job change mid-year)
- Zeile 18 showing employer-paid commuting subsidies (affects Entfernungspauschale calculation later)

## Handling Freelance Income

If the user has freelance income (freiberufliche Tätigkeit or Gewerbebetrieb), they won't have a Lohnsteuerbescheinigung for it. Instead, capture:

- **Total revenue** (Einnahmen / Betriebseinnahmen)
- **Total expenses** (Betriebsausgaben) — or ask if they use Einnahmenüberschussrechnung (EÜR)
- **Profit** (Gewinn = Einnahmen - Ausgaben)
- **Was Umsatzsteuer charged?** (Kleinunternehmerregelung or regular USt?)
- **Were Vorauszahlungen (tax prepayments) made?** If so, how much
- **Was the income from a single client or multiple?** (relevant for Scheinselbständigkeit)

Note: Freelance income requires Anlage S (freie Berufe) or Anlage G (Gewerbe). For EÜR, a separate Anlage EÜR is needed.

## Handling Other Income Types

For each, capture the key numbers and flag the relevant Anlage:

- **Rental income** → Anlage V: Mieteinnahmen, Werbungskosten (Abschreibung, Zinsen, Reparaturen)
- **Capital gains** → Anlage KAP: Usually handled by bank (Abgeltungsteuer), but check if Günstigerprüfung applies
- **Foreign income** → Anlage AUS: Country, amount, taxes paid abroad, applicable DBA
- **Pension income** → Anlage R: Rentenbezüge, Besteuerungsanteil

## Output Format

After extraction, save the structured data so subsequent skills can use it:

```json
{
  "tax_year": 2025,
  "persons": [
    {
      "name": "Max Mustermann",
      "role": "steuerpflichtiger",
      "employers": [
        {
          "employer_name": "Muster GmbH",
          "period": "01.01.2025-31.12.2025",
          "tax_class": "III",
          "kinderfreibetraege": 1.0,
          "church_member": true,
          "church_tax_rate_pct": 9,
          "brutto": 65000.00,
          "lohnsteuer": 8452.00,
          "soli": 0.00,
          "kirchensteuer": 676.16,
          "rv_an": 6045.00,
          "av_an": 845.00,
          "kv_an": 5330.00,
          "pv_an": 1170.00,
          "rv_ag": 6045.00,
          "ag_zuschuss_kv_pv": 3250.00,
          "pauschal_fahrtkosten_ag": 0.00,
          "bav": 0.00
        }
      ],
      "freelance_income": null,
      "other_income": []
    }
  ]
}
```

This JSON is the handoff to the next skills in the pipeline.
