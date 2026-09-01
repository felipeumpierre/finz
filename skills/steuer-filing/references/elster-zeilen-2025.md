# ELSTER Form Zeilen — Tax Year 2025

**Last verified:** 2026-09-01 (Anlagen-structure note, Basiszins, Kinderbetreuung, KAP/KAP-INV notes); Zeile numbers otherwise as of 2026-04-17
**Status:** 2025 Formulare were published by the BMF starting late 2025. The separate *Anlage Sonderausgaben*, *Anlage Außergewöhnliche Belastungen* and *Anlage Haushaltsnahe Aufwendungen* are **not new for 2025** — they have existed since **tax year 2019**, when their content was moved out of the Hauptvordruck ESt 1 A (source: [Haufe — Anlage Haushaltsnahe Aufwendungen 2019 Leitfaden](https://www.haufe.de/steuern/haufe-steuer-office-excellence/anlage-haushaltsnahe-aufwendungen-2019-leitfaden_idesk_PI25844_HI13278820_2019.html), retrieved 2026-09-01). Earlier versions of this file wrongly described them as new for 2025. §35a has been on the Anlage Haushaltsnahe Aufwendungen for TY 2019 onward; only the Zeile numbers within that Anlage need verification for 2025.

**Primary source:** Bundesfinanzministerium Formular-Management-System — https://www.formulare-bfinv.de/ (accessed 2026-04-17)
**Structure note:** Haufe (Änderungen in den Vordrucken 2025, see Sources) describes only incremental changes for 2025 — Anlage SO Kryptowerte block re-numbered (see `steuer-crypto/references/anlage-so-mapping-2025.md`) and Anlage KAP shortened by three lines (see Anlage KAP below).

> **Critical rule for 2025 filings:** Every Zeile number that was valid for 2024 must be re-checked against the 2025 form PDF in ELSTER before being quoted to a user. This document flags **[UNVERIFIED for 2025]** wherever Zeile numbers could not be confirmed at retrieval time.

---

## Hauptvordruck / Mantelbogen (ESt 1 A) — 2025

The 2025 Mantelbogen contains: personal data, Veranlagungsart, Bankverbindung, and pointers to Anlagen. §35a amounts are on the *Anlage Haushaltsnahe Aufwendungen* (since TY 2019, unchanged).

| Purpose | Zeile | Notes |
|---|---|---|
| Steuerpflichtige Person — Identifikationsnummer | Zeile in Personenblock (~7) | [UNVERIFIED for 2025 — structure mirrored 2024 but page layout shortened; verify in ELSTER] |
| Ehegatte/Lebenspartner — Identifikationsnummer | Zeile in Personenblock | [UNVERIFIED for 2025] |
| Religionszugehörigkeit | Zeile in Personenblock | [UNVERIFIED for 2025] |
| Veranlagungsart (Zusammenveranlagung) | Veranlagungsart-Block | [UNVERIFIED for 2025] |
| Bankverbindung — IBAN | Bankverbindungsblock | [UNVERIFIED for 2025] |
| §35a Handwerkerleistungen / haushaltsnahe Dienstleistungen / Beschäftigungsverhältnisse | **on Anlage Haushaltsnahe Aufwendungen** (since TY 2019) | Not on Mantelbogen |

---

## Anlage Haushaltsnahe Aufwendungen — 2025 (separate Anlage since TY 2019)

Dedicated form for §35a EStG (Beschäftigungsverhältnisse, haushaltsnahe Dienstleistungen, Handwerkerleistungen, Pflege/Betreuung).

| Purpose | Zeile | Notes |
|---|---|---|
| Geringfügige Beschäftigungsverhältnisse (§35a Abs. 1) | [UNVERIFIED for 2025] | 20 %, max 510 EUR |
| Sozialversicherungspflichtige Beschäftigungsverhältnisse + haushaltsnahe Dienstleistungen (§35a Abs. 2) | [UNVERIFIED for 2025] | 20 %, max 4,000 EUR combined |
| Handwerkerleistungen (§35a Abs. 3) | [UNVERIFIED for 2025] | 20 %, max 1,200 EUR |
| Pflege- und Betreuungsleistungen | [UNVERIFIED for 2025] | |

> [UNVERIFIED for 2025 — Zeile numbers will be confirmed once the form PDF is machine-readable or once the Haufe 2025 commentary is indexed. The **caps remain unchanged** per §35a EStG: 510 / 4,000 / 1,200 EUR (20 % credit).]

---

## Anlage Sonderausgaben — 2025 (separate Anlage since TY 2019)

Dedicated form for items that were on the Mantelbogen until TY 2018: Kirchensteuer (gezahlt), Spenden/Mitgliedsbeiträge, Berufsausbildungskosten, gezahlte Unterhaltsleistungen.

> [UNVERIFIED for 2025 — Zeile-level mapping pending form-PDF text extraction.]

---

## Anlage Außergewöhnliche Belastungen — 2025 (separate Anlage since TY 2019)

Dedicated form for außergewöhnliche Belastungen (Krankheitskosten, Pflegeheimkosten, Behinderten-Pauschbetrag, etc.) that were sub-sections of the Mantelbogen until TY 2018.

> [UNVERIFIED for 2025 — Zeile-level mapping pending form-PDF text extraction. The Behinderten-Pauschbetrag amounts from §33b EStG carry over unchanged from 2024.]

---

## Anlage N — 2025

**Assumption:** Zeile structure preserved from 2024 (no public announcement of Anlage N restructure for 2025). Structure should match `elster-zeilen-2024.md` Anlage N table.

| Purpose | Zeile 2024 | Zeile 2025 | Notes |
|---|---|---|---|
| Bruttoarbeitslohn | 6 | 6 [UNVERIFIED for 2025] | |
| Entschädigung / Fünftelregelung | 17–20 | 17–20 [UNVERIFIED for 2025] | |
| Lohnsteuer / Soli / Kirchensteuer block | ~6–9 | ~6–9 [UNVERIFIED for 2025] | |
| Entfernungspauschale | 30–55 | 30–55 [UNVERIFIED for 2025] | |
| Beiträge zu Berufsverbänden | 56 | 56 [UNVERIFIED for 2025] | |
| Arbeitsmittel | 57–59 | 57–59 [UNVERIFIED for 2025] | |
| Homeoffice-Pauschale | 61–62 | 61–62 [UNVERIFIED for 2025] | |
| Fortbildungskosten | 63 | 63 [UNVERIFIED for 2025] | |
| Weitere Werbungskosten | 64–67 | 64–67 [UNVERIFIED for 2025] | |

> **2025 parameter change (not Zeile-level):** Arbeitnehmer-Pauschbetrag remains 1,230 EUR (§9a EStG, unchanged since 2023).

---

## Anlage S — 2025

Structure preserved from 2024: Zeile 4 = Gewinn aus freiberuflicher Tätigkeit (from Anlage EÜR), Zeile 5 = Gewinn aus weiterer Tätigkeit. Anlage EÜR continues to be mandatory.

| Purpose | Zeile | Notes |
|---|---|---|
| Gewinn aus freiberuflicher Tätigkeit (Person A) | 4 [UNVERIFIED for 2025] | |
| Gewinn aus weiterer Tätigkeit | 5 [UNVERIFIED for 2025] | |

---

## Anlage Vorsorgeaufwand — 2025

Structure preserved from 2024. Electronic transmission (VaSt) still pre-fills RV/KV/PV/AV.

| Purpose | Zeile 2024 | Zeile 2025 | Notes |
|---|---|---|---|
| Basiskrankenversicherung (pre-filled) | ~12–13 | ~12–13 [UNVERIFIED for 2025] | |
| Private Haftpflichtversicherung | 46 | 46 [UNVERIFIED for 2025] | Parameter: part of 1,900/2,800 EUR sonstige-Vorsorge cap |
| Berufsunfähigkeits-, Unfall-, Risikolebens- | 45–46 | 45–46 [UNVERIFIED for 2025] | |
| Höchstbetragsblock | 49 | 49 [UNVERIFIED for 2025] | |

---

## Anlage KAP — 2025

**Structure change for 2025:** the lines for Termingeschäft-Verluste / Forderungsausfälle (former 20,000 EUR caps) were removed from Anlage KAP 2025 — the form is **three lines shorter**, so Zeile numbers after that block may shift relative to 2024 (Haufe, Änderungen in den Vordrucken 2025; retrieved 2026-09-01). Every 2024 number below remains [UNVERIFIED for 2025] until checked in ELSTER. **Parameter change for 2025:** Basiszins für Vorabpauschale-Berechnung 2025 = **2.53 %** (BMF-Schreiben 10.01.2025, IV C 1 - S 1980/00230/009/002; do not use the 2024 value of 2.29 %). Basiszins 2026 = **3.20 %** (BMF-Schreiben 13.01.2026).

| Purpose | Zeile 2024 | Zeile 2025 | Notes |
|---|---|---|---|
| Antrag auf Günstigerprüfung | 4 | 4 [UNVERIFIED for 2025] | |
| Antrag auf Überprüfung des Steuereinbehalts | 5 | 5 [UNVERIFIED for 2025] | |
| Kapitalerträge mit KESt-Abzug (inländisch) | 7 | 7 [UNVERIFIED for 2025] | |
| Enthaltene Gewinne Aktien (mit KESt) | 8 | 8 [UNVERIFIED for 2025] | |
| Enthaltene Verluste sonstige (mit KESt) | 12 | 12 [UNVERIFIED for 2025] | |
| Enthaltene Verluste Aktien (mit KESt) | 13 | 13 [UNVERIFIED for 2025] | |
| Sparer-Pauschbetrag | 16–17 | 16–17 [UNVERIFIED for 2025] | 1,000 / 2,000 EUR |
| Inländische Kapitalerträge ohne KESt | 18 | 18 [UNVERIFIED for 2025] | |
| Ausländische Kapitalerträge | 19 | 19 [UNVERIFIED for 2025] | |
| Gewinne Aktien (ohne KESt) | 20 | 20 [UNVERIFIED for 2025] | |
| Verluste sonstige (ohne KESt) | 22 | 22 [UNVERIFIED for 2025] | |
| Verluste Aktien (ohne KESt) | 23 | 23 [UNVERIFIED for 2025] | |
| Einbehaltene Kapitalertragsteuer | 37 | 37 [UNVERIFIED for 2025] | |
| Einbehaltener Soli / Kirchensteuer | 38–39 | 38–39 [UNVERIFIED for 2025] | |
| Anrechenbare ausländische Steuern | 40–42 block | 40–42 block [UNVERIFIED for 2025] | |

> **Legal-parameter note for 2025:** the 20,000 EUR loss caps for Termingeschäfte and Forderungsausfälle (former §20 Abs. 6 S. 5–6 EStG) were **repealed by the Jahressteuergesetz 2024 (02.12.2024) for all open cases**; BFH 28.03.2025 VIII R 11/24 confirmed. This was NOT a BVerfG decision. The Aktienverlust ring-fence (§20 Abs. 6 S. 4 EStG) remains in force — BVerfG 2 BvL 3/21 is pending (decision expected late 2026 / early 2027). The repeal is why the corresponding Anlage-KAP lines disappeared in 2025 (see structure note above).

---

## Anlage KAP-INV — 2025

Structure presumed preserved; **Vorabpauschale 2025 amount recalculated with Basiszins 2.53 %**.

| Purpose | Zeile 2024 | Zeile 2025 | Notes |
|---|---|---|---|
| Ausschüttungen (per Fondstyp) | 4–8 | 4–8 [UNVERIFIED for 2025] | per `elster-zeilen-2024.md` (ELSTER help); an earlier version of this file wrongly listed 9–13 |
| Vorabpauschalen (per Fondstyp) | 9–13 | 9–13 [UNVERIFIED for 2025] | |
| Vorabpauschalen-Berechnungsblock | 30–45 | 30–45 [UNVERIFIED for 2025] | |

---

## Anlage Kind — 2025

Structure preserved.

| Purpose | Zeile 2024 | Zeile 2025 | Notes |
|---|---|---|---|
| IdNr des Kindes | 4 | 4 [UNVERIFIED for 2025] | |
| Kinderbetreuungskosten | 66–72 | 66–72 [UNVERIFIED for 2025] | Deduction since VZ 2025: **80 % of costs, max 4,800 EUR/Kind/yr** (§10 Abs. 1 Nr. 5 EStG, JStG 2024; before 2025: 2/3, max 4,000) |

> **2025 parameter changes:** Kindergeld 250 → **255 EUR/month** (FamLeistG); Kinderfreibetrag combined 6,384 → **6,672 EUR/child/yr** (per Steuerfortentwicklungsgesetz 2024). Verify with steuer-calculator reference.

---

## Open Items for 2025

| Item | Status |
|---|---|
| Mantelbogen (ESt 1 A) 2025 Zeile-by-Zeile mapping | [UNVERIFIED — form restructured; requires text-extractable PDF or indexed commentary] |
| Anlage Haushaltsnahe Aufwendungen 2025 Zeilen | [UNVERIFIED — form exists since TY 2019; 2025 Zeile numbers not yet extracted] |
| Anlage Sonderausgaben 2025 Zeilen | [UNVERIFIED — form exists since TY 2019; 2025 Zeile numbers not yet extracted] |
| Anlage Außergewöhnliche Belastungen 2025 Zeilen | [UNVERIFIED — form exists since TY 2019; 2025 Zeile numbers not yet extracted] |
| Confirmation that Anlage N / KAP / SO / Vorsorgeaufwand / Kind / S Zeile numbers were NOT re-numbered for 2025 | [UNVERIFIED — Haufe 2025 commentary pending] |

**Resolution path:** when the user files for TY 2025, verify each quoted Zeile against the ELSTER live form. Update this file with confirmed numbers.

---

## Sources

- **BMF Formular-Management-System catalog:** https://www.formulare-bfinv.de/ (accessed 2026-04-17)
- **Steuerrat24 2025 forms overview:** https://www.steuerrat24.de/steuererklaerung/steuererklaerung-2025/steuerformulare-2025.html (accessed 2026-04-17)
- **Haufe — Änderungen in den Vordrucken der Überschusseinkünfte 2025** (Anlage KAP three lines shorter; Anlage SO Kryptowerte Zeile 45 ff.): https://www.haufe.de/steuern/finanzverwaltung/einkommensteuererklaerung-2025-aenderungen-in-den-vordrucken/aenderungen-in-den-vordrucken-der-ueberschusseinkuenfte-2025_164_670430.html (accessed 2026-09-01)
- **Haufe — Anlage Haushaltsnahe Aufwendungen 2019 Leitfaden** (separate Anlagen exist since TY 2019): https://www.haufe.de/steuern/haufe-steuer-office-excellence/anlage-haushaltsnahe-aufwendungen-2019-leitfaden_idesk_PI25844_HI13278820_2019.html (accessed 2026-09-01)
- **BMF-Schreiben 13.01.2026 Basiszins 2026:** https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2026-01-13-basiszins-berechnung-vorabpauschale.pdf (accessed 2026-09-01)
- **BMF Anlage EÜR 2025 PDF:** https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-08-29-anlage-EUER-2025.pdf (accessed 2026-04-17)
- **Haufe Änderungen in den Vordrucken 2024** (baseline for comparing 2025): https://www.haufe.de/steuern/finanzverwaltung/einkommensteuererklaerung-2024-aenderungen-in-den-vordrucken/aenderungen-in-den-vordrucken-der-ueberschusseinkuenfte-2024_164_639322.html (accessed 2026-04-17)

For Zeile-numbers not re-verified for 2025, fall back to `elster-zeilen-2024.md` and treat every value as [UNVERIFIED for 2025] until confirmed in ELSTER.
