# Tax Parameters — Multi-Year Reference

**Last verified:** 2026-04-17
**Valid for:** Tax years 2023, 2024, 2025, 2026 (where published)
**Rule:** Every figure here is sourced to a primary document. If a figure is used inside a skill, it MUST be read from this file, not inlined.

Abbreviations: EStG = Einkommensteuergesetz (Income Tax Act). SolZG = Solidaritätszuschlaggesetz (Solidarity Surcharge Act). BKGG = Bundeskindergeldgesetz (Federal Child Benefit Act). BEA = Betreuungs-, Erziehungs- oder Ausbildungsbedarf (care, upbringing or education allowance). zvE = zu versteuerndes Einkommen (taxable income).

---

## Grundfreibetrag (basic tax-free allowance) — §32a Abs. 1 EStG

| Tax year | Single zvE threshold | Joint (Splitting) | Source |
|---|---|---|---|
| 2023 | 10,908 EUR | 21,816 EUR | [BMF EStH 2023 §32a](https://esth.bundesfinanzministerium.de/lsth/2023/A-Einkommensteuergesetz/IV-Tarif/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 |
| 2024 | 11,784 EUR | 23,568 EUR | [BMF EStH 2024 §32a](https://esth.bundesfinanzministerium.de/esth/2024/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 |
| 2025 | 12,096 EUR | 24,192 EUR | [BMF LStH 2025 §32a](https://lsth.bundesfinanzministerium.de/lsth/2025/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 |
| 2026 | 12,348 EUR | 24,696 EUR | [BMF LStH 2026 §32a](https://lsth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 |

---

## Top-rate thresholds (§32a EStG)

The 42% threshold is the lower edge of the "Proportionalzone"; the 45% threshold is the "Reichensteuer" edge. Both apply to single-person zvE (double for Splitting).

| Tax year | 42% starts at | 45% starts at | Source |
|---|---|---|---|
| 2023 | 62,810 EUR | 277,826 EUR | [BMF EStH 2023 §32a](https://esth.bundesfinanzministerium.de/lsth/2023/A-Einkommensteuergesetz/IV-Tarif/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 |
| 2024 | 66,761 EUR | 277,826 EUR | [BMF EStH 2024 §32a](https://esth.bundesfinanzministerium.de/esth/2024/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 |
| 2025 | 68,481 EUR | 277,826 EUR | [BMF LStH 2025 §32a](https://lsth.bundesfinanzministerium.de/lsth/2025/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 |
| 2026 | 69,879 EUR | 277,826 EUR | [BMF LStH 2026 §32a](https://lsth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html) — retrieved 2026-04-17 |

The 45% Reichensteuer threshold of 277,826 EUR has been stable since the 2020 reform. The 42% threshold is indexed via the annual tariff adjustment.

For the full polynomial formula used inside each bracket, see `st32a-coefficients.md`.

---

## Solidaritätszuschlag (solidarity surcharge) Freigrenze — §3 Abs. 3 SolZG 1995

The Soli is 5.5% of assessed income tax, but only charged if the tax itself exceeds the Freigrenze. Above the Freigrenze, a Milderungszone phases the surcharge in.

| Tax year | Single Freigrenze (EUR tax) | Joint Freigrenze (EUR tax) | Source |
|---|---|---|---|
| 2023 | 17,543 EUR | 35,086 EUR | [lohnsteuer-kompakt.de Soli-Freigrenze](https://www.lohnsteuer-kompakt.de/steuerwissen/solidaritaetszuschlag-erhoehung-der-freigrenze-3) — retrieved 2026-04-17 |
| 2024 | 18,130 EUR | 36,260 EUR | [BMF "Das ändert sich 2024"](https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/das-aendert-sich-2024.html) — retrieved 2026-04-17 |
| 2025 | 19,950 EUR | 39,900 EUR | [Haufe SolZG Anhebung 2025](https://www.haufe.de/id/beitrag/solidaritaetszuschlag-zur-einkommensteuer-31-anhebung-der-freigrenzen-HI14712446.html) — retrieved 2026-04-17 |
| 2026 | 20,350 EUR | 40,700 EUR | [gesetze-im-internet.de §3 SolZG 1995](https://www.gesetze-im-internet.de/solzg_1995/__3.html) — retrieved 2026-04-17 |

Notes:
- The in-force text on gesetze-im-internet.de currently shows the 2026 values (20,350 / 40,700). The 2025 values (19,950 / 39,900) were set by the Steuerfortentwicklungsgesetz (Dec 2024).
- The old flat Freigrenze of 972 EUR / 1,944 EUR was replaced in 2021 by the current indexed values.

---

## Kinderfreibetrag + BEA-Freibetrag — §32 Abs. 6 EStG

Per child, per parent. Joint filers get the doubled amount per child. The Finanzamt performs an automatic Günstigerprüfung (comparison) against Kindergeld; the more favourable is applied.

| Tax year | Kinderfreibetrag per parent | BEA-Freibetrag per parent | Combined per child (both parents) | Source |
|---|---|---|---|---|
| 2023 | 3,012 EUR | 1,464 EUR | 8,952 EUR | [sozialpolitik-aktuell tabVII14](https://www.sozialpolitik-aktuell.de/files/sozialpolitik-aktuell/_Politikfelder/Familienpolitik/Datensammlung/PDF-Dateien/tabVII14.pdf) — retrieved 2026-04-17 |
| 2024 | 3,306 EUR | 1,464 EUR | 9,540 EUR | [BMF EStH 2024 §32](https://esth.bundesfinanzministerium.de/esth/2024/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32/inhalt.html) — retrieved 2026-04-17 |
| 2025 | 3,336 EUR | 1,464 EUR | 9,600 EUR | [kindergeld.org Kinderfreibetrag](https://www.kindergeld.org/kinderfreibetrag/) — retrieved 2026-04-17 |
| 2026 | 3,414 EUR | 1,464 EUR | 9,756 EUR | [gesetze-im-internet.de §32 EStG](https://www.gesetze-im-internet.de/estg/__32.html) — retrieved 2026-04-17 |

Notes:
- The BEA-Freibetrag has been 1,464 EUR per parent unchanged since 2021.
- In a retroactive increase passed via the Steuerfortentwicklungsgesetz (Dec 2024), the 2024 Kinderfreibetrag was raised from 3,192 to 3,306 EUR; 2025 from 3,306 to 3,336 EUR. Early-published values may still show the pre-increase amounts.

---

## Kindergeld (BKGG) — monthly per child

| Tax year | Amount per child per month | Source |
|---|---|---|
| 2023 | 250.00 EUR | [Bundesagentur für Arbeit Kindergeld-Info](https://www.arbeitsagentur.de/news/kindergeld-kinderzuschlag-2025) — retrieved 2026-04-17 |
| 2024 | 250.00 EUR | [Bundesagentur für Arbeit](https://www.arbeitsagentur.de/news/kindergeld-kinderzuschlag-2025) — retrieved 2026-04-17 |
| 2025 | 255.00 EUR | [Bundesagentur für Arbeit Presse 2025-50](https://www.arbeitsagentur.de/presse/2025-50-kindergeld-und-kinderzuschlag-steigen-ab-januar-2025) — retrieved 2026-04-17 |
| 2026 | 259.00 EUR | [finanz.de Kindergeld-Tabelle 2025/2026](https://www.finanz.de/news/tabelle-erhoehung-kindergeld-10105/) — retrieved 2026-04-17 |

Since 2023 the amount has been unified across all children (no more increase per Ordnungszahl). Annual Kindergeld per child = 12 × monthly amount.

---

## Arbeitnehmer-Pauschbetrag (employee flat Werbungskosten) — §9a Nr. 1a EStG

Automatically applied to employment income when no higher itemized Werbungskosten are claimed. Capped at the level of the employment income itself (no negative income via the Pauschbetrag).

| Tax year | Amount | Source |
|---|---|---|
| 2023 | 1,230 EUR | [gesetze-im-internet.de §9a EStG](https://www.gesetze-im-internet.de/estg/__9a.html) — retrieved 2026-04-17 |
| 2024 | 1,230 EUR | [gesetze-im-internet.de §9a EStG](https://www.gesetze-im-internet.de/estg/__9a.html) — retrieved 2026-04-17 |
| 2025 | 1,230 EUR | [gesetze-im-internet.de §9a EStG](https://www.gesetze-im-internet.de/estg/__9a.html) — retrieved 2026-04-17 |
| 2026 | 1,230 EUR | [gesetze-im-internet.de §9a EStG](https://www.gesetze-im-internet.de/estg/__9a.html) — retrieved 2026-04-17 |

Has been 1,230 EUR since 2023 (raised from 1,200 in 2022). The gesetze-im-internet.de text shows the in-force 2026 version, which confirms the figure is still unchanged.

---

## Entfernungspauschale (commuter flat) — §9 Abs. 1 Nr. 4 + Abs. 2 EStG

Per workday per full km between residence and first workplace. Annual cap 4,500 EUR unless own vehicle used.

| Tax year | km 1–20 | km 21+ | Annual cap (without own vehicle) | Source |
|---|---|---|---|---|
| 2023 | 0.30 EUR | 0.38 EUR | 4,500 EUR | [finanztip Entfernungspauschale](https://www.finanztip.de/entfernungspauschale/) — retrieved 2026-04-17 |
| 2024 | 0.30 EUR | 0.38 EUR | 4,500 EUR | [finanztip Entfernungspauschale](https://www.finanztip.de/entfernungspauschale/) — retrieved 2026-04-17 |
| 2025 | 0.30 EUR | 0.38 EUR | 4,500 EUR | [BMF LStH 2025 Anhang 14](https://lsth.bundesfinanzministerium.de/lsth/2025/B-Anhaenge/Anhang-14/inhalt.html) — retrieved 2026-04-17 |
| 2026 | 0.38 EUR | 0.38 EUR | 4,500 EUR | [gesetze-im-internet.de §9 EStG](https://www.gesetze-im-internet.de/estg/__9.html) — retrieved 2026-04-17 |

From 2026 onwards the rate is unified at 0.38 EUR/km from the first kilometre. For low earners below the Grundfreibetrag, a Mobilitätsprämie (§§101 ff EStG) can be claimed instead.

---

## Homeoffice-Pauschale — §4 Abs. 5 Satz 1 Nr. 6c EStG

Daily flat for days worked predominantly from home (no separate Arbeitszimmer required).

| Tax year | Per day | Max days | Max annual | Source |
|---|---|---|---|---|
| 2023 | 6.00 EUR | 210 | 1,260 EUR | [BMF EStH 2024 Homeoffice-Pauschale](https://ao.bundesfinanzministerium.de/esth/2024/tabellarische-Uebersicht/Homeoffice-Pauschale.html) — retrieved 2026-04-17 |
| 2024 | 6.00 EUR | 210 | 1,260 EUR | [BMF EStH 2024 Homeoffice-Pauschale](https://ao.bundesfinanzministerium.de/esth/2024/tabellarische-Uebersicht/Homeoffice-Pauschale.html) — retrieved 2026-04-17 |
| 2025 | 6.00 EUR | 210 | 1,260 EUR | [DHW Homeoffice-Pauschale 2025](https://www.dhw-stb.de/2024/07/homeoffice-pauschale-2025-das-solltest-du-bei-der-steuererklaerung-beachten/) — retrieved 2026-04-17 |
| 2026 | 6.00 EUR | 210 | 1,260 EUR | [UNVERIFIED — not yet confirmed against primary source for TY 2026] |

The Homeoffice-Pauschale counts against the Arbeitnehmer-Pauschbetrag (1,230 EUR): only the amount exceeding 1,230 EUR adds to refundable Werbungskosten.

---

## Altersvorsorge-Höchstbetrag — §10 Abs. 3 EStG

Cap for basic retirement-provision special expenses (gesetzliche RV, berufsständische Versorgung, Rürup). 100% of up-to-cap contributions deductible since 2023. The cap equals the Höchstbeitrag zur knappschaftlichen Rentenversicherung (BBG knappschaft × 24.7%).

| Tax year | Single cap | Joint cap | Source |
|---|---|---|---|
| 2023 | 26,528 EUR | 53,056 EUR | [rentenfuchs.info Höchstbetrag 2024](https://www.rentenfuchs.info/rentenbeitraege-steuerlich-absetzen-hochstbetrag-2024/) — retrieved 2026-04-17 |
| 2024 | 27,566 EUR | 55,132 EUR | [rentenfuchs.info Höchstbetrag 2024](https://www.rentenfuchs.info/rentenbeitraege-steuerlich-absetzen-hochstbetrag-2024/) — retrieved 2026-04-17 |
| 2025 | 29,344 EUR | 58,688 EUR | [rentenfuchs.info Höchstbetrag 2025](https://www.rentenfuchs.info/rentenbeitraege-steuerlich-absetzen-hochstbetrag-2025/) — retrieved 2026-04-17 |
| 2026 | [UNVERIFIED — value depends on BBG knappschaft 2026; check DRV KBS publication] | — | [rentenfuchs.info Höchstbetrag 2026](https://www.rentenfuchs.info/rentenbeitrage-steuerlich-absetzen-hoechstbetrag-2026/) — retrieved 2026-04-17 |

For employees, the deductible amount is the sum of employer + employee RV contributions (the employer share must be added back per §10 Abs. 3 Satz 5 EStG).

---

## Sonstige Vorsorgeaufwendungen cap — §10 Abs. 4 EStG

Cap for non-pension insurance (Basis-Krankenversicherung, Pflegeversicherung, plus Haftpflicht/BU/RLV under "other"). Basis-KV and Pflege are fully deductible even beyond the cap (§10 Abs. 4 Satz 4); the cap bites only when "other" insurance pushes the total above it.

| Tax year | Employees (tax-free KV subsidy) | Self-employed / without subsidy | Source |
|---|---|---|---|
| 2023 | 1,900 EUR | 2,800 EUR | [gesetze-im-internet.de §10 EStG](https://www.gesetze-im-internet.de/estg/__10.html) — retrieved 2026-04-17 |
| 2024 | 1,900 EUR | 2,800 EUR | [gesetze-im-internet.de §10 EStG](https://www.gesetze-im-internet.de/estg/__10.html) — retrieved 2026-04-17 |
| 2025 | 1,900 EUR | 2,800 EUR | [gesetze-im-internet.de §10 EStG](https://www.gesetze-im-internet.de/estg/__10.html) — retrieved 2026-04-17 |
| 2026 | 1,900 EUR | 2,800 EUR | [gesetze-im-internet.de §10 EStG](https://www.gesetze-im-internet.de/estg/__10.html) — retrieved 2026-04-17 |

The cap is doubled for jointly assessed couples. The values have been stable since 2010.

---

## §35a caps — haushaltsnahe Dienstleistungen & Handwerker

All three reduce the assessed tax directly (not the zvE), at 20% of qualifying costs up to the cap. Combined maximum per household per year: 5,710 EUR (510 + 4,000 + 1,200).

| Sub-section | Scope | Rate | Annual cap | Source |
|---|---|---|---|---|
| §35a Abs. 1 | Minijob household employment (geringfügige Beschäftigung im Privathaushalt) | 20% | 510 EUR | [gesetze-im-internet.de §35a EStG](https://www.gesetze-im-internet.de/estg/__35a.html) — retrieved 2026-04-17 |
| §35a Abs. 2 | Haushaltsnahe Dienstleistungen + sozialversicherungspflichtige Beschäftigung + Pflege/Betreuung | 20% | 4,000 EUR | [gesetze-im-internet.de §35a EStG](https://www.gesetze-im-internet.de/estg/__35a.html) — retrieved 2026-04-17 |
| §35a Abs. 3 | Handwerkerleistungen (labour cost only, not materials) | 20% | 1,200 EUR | [gesetze-im-internet.de §35a EStG](https://www.gesetze-im-internet.de/estg/__35a.html) — retrieved 2026-04-17 |

These caps have been unchanged since 2009. They apply per Haushalt (one household cannot multiply the cap across Zusammenveranlagung partners).

---

## Kinderbetreuungskosten — §10 Abs. 1 Nr. 5 EStG

Deductible as Sonderausgaben for children up to 14 (or disabled, any age).

| Tax year | Deductible share | Cap per child per year | Source |
|---|---|---|---|
| 2023 | 2/3 of costs | 4,000 EUR | [lohnsteuer-kompakt — Kinderbetreuungskosten 2025](https://www.lohnsteuer-kompakt.de/steuerwissen/kinderbetreuungskosten-hoeherer-sonderausgabenabzug-2025/) — retrieved 2026-04-17 |
| 2024 | 2/3 of costs | 4,000 EUR | [lohnsteuer-kompakt — Kinderbetreuungskosten 2025](https://www.lohnsteuer-kompakt.de/steuerwissen/kinderbetreuungskosten-hoeherer-sonderausgabenabzug-2025/) — retrieved 2026-04-17 |
| 2025 | 80% of costs | 4,800 EUR | [Jahressteuergesetz 2024 — Haufe summary](https://www.haufe.de/id/beitrag/jahreswechsel-20242025-lohnsteuerliche-aenderungen-34-sonderausgaben-fuer-kinderbetreuungskosten-HI16672501.html) — retrieved 2026-04-17 |
| 2026 | 80% of costs | 4,800 EUR | [gesetze-im-internet.de §10 EStG](https://www.gesetze-im-internet.de/estg/__10.html) — retrieved 2026-04-17 |

The 2/3 → 80% and 4,000 → 4,800 EUR upgrade was enacted by the Jahressteuergesetz 2024 (Bundesrat vote 2024-11-22) with effect from 2025-01-01. Only costs for care/supervision qualify; Nachhilfe, Sport, Musikunterricht do not.

---

## Sonderausgaben-Pauschbetrag — §10c EStG

Applied automatically if no other Sonderausgaben are claimed. Almost always superseded by Vorsorgeaufwendungen in practice.

| Tax year | Single | Joint | Source |
|---|---|---|---|
| 2023–2026 | 36 EUR | 72 EUR | [gesetze-im-internet.de §10c EStG](https://www.gesetze-im-internet.de/estg/__10c.html) — retrieved 2026-04-17 |

Unchanged since the EStG was enacted.

---

## Kirchensteuer rate

| Bundesland | Rate (% of ESt) |
|---|---|
| Bayern, Baden-Württemberg | 8% |
| All other 14 Bundesländer | 9% |

Source: KiStG of each Bundesland; see [Wikipedia: Kirchensteuer in Deutschland](https://de.wikipedia.org/wiki/Kirchensteuer_(Deutschland)) — retrieved 2026-04-17 for overview (consult the specific Landesgesetz for binding rate).

Kirchensteuer itself is deductible as Sonderausgabe (§10 Abs. 1 Nr. 4 EStG).

---

## Zumutbare Belastung (for außergewöhnliche Belastungen) — §33 Abs. 3 EStG

Computed progressively per income tier against Gesamtbetrag der Einkünfte. The tier thresholds (15,340 EUR / 51,130 EUR) are fixed by statute and have not changed since 1975.

| Gesamtbetrag der Einkünfte tier | Single / married no child | 1–2 children | 3+ children |
|---|---|---|---|
| up to 15,340 EUR | 5% / 4% | 2% | 1% |
| 15,340–51,130 EUR | 6% / 5% | 3% | 1% |
| over 51,130 EUR | 7% / 6% | 4% | 2% |

Source: [gesetze-im-internet.de §33 EStG](https://www.gesetze-im-internet.de/estg/__33.html) — retrieved 2026-04-17. Note: Per BFH ruling VI R 75/14 (2017), the tiers are applied **progressively** (each tier's rate only to income within that tier), not in one lump.

---

## What to do when a value here is stale

1. Do NOT guess — mark the figure `[UNVERIFIED — needs check against <URL>]` in any output that uses it.
2. WebFetch the primary source (gesetze-im-internet.de, bundesfinanzministerium.de, bzst.de, arbeitsagentur.de, bundesbank.de).
3. Update this file with the retrieved value + the source URL + retrieval date.
4. Only then use the value in a calculation.
