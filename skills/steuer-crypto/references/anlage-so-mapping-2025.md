# Anlage SO — Crypto Mapping — Tax Year 2025

**Last verified:** 2026-09-01
**Status:** Anlage SO 2025 was published in the 2025 form set. **The Zeile numbers changed vs. 2024:** the Kryptowerte block (§23) now starts at **Zeile 45** (2024: 41), and the §22 Nr.3 Leistungen block carries a dedicated Kennzahl for "Tätigkeiten im Zusammenhang mit Kryptowerten" (Staking/Lending/Mining) at **Zeilen 14–20**. An earlier version of this file carried the 2024 numbers (41–55) over unchanged — that was wrong.
**Sources:** Haufe — Änderungen in den Vordrucken der Überschusseinkünfte 2025 (https://www.haufe.de/steuern/finanzverwaltung/einkommensteuererklaerung-2025-aenderungen-in-den-vordrucken/aenderungen-in-den-vordrucken-der-ueberschusseinkuenfte-2025_164_670430.html, retrieved 2026-09-01); Blockpit Krypto-Steuererklärung Anleitung (https://www.blockpit.io/de-de/steuer-guides/krypto-steuererklaerung-eintragen-anleitung, retrieved 2026-09-01); two further preparer guides agree. **[secondary-source, official PDF not yet checked]** — the BMF Anlage SO 2025 PDF was not fetched.

> **Rule for 2025 filings:** Every Zeile number below is **[secondary-source, official PDF not yet checked]**. Verify each against the live ELSTER 2025 form (or the BMF form PDF) before quoting it to a user or writing it into an export.

---

## §22 Nr.3 EStG — Leistungen "Tätigkeiten im Zusammenhang mit Kryptowerten" (Staking, Lending, Mining, Earn)

All Zeilen: **[secondary-source, official PDF not yet checked]**.

| Field | Zeile 2024 | Zeile 2025 | Source from crypto-ledger yearly_tax_summary[2025] |
|---|---|---|---|
| Kennzahl "Tätigkeiten im Zusammenhang mit Kryptowerten" | — (no dedicated Kennzahl) | 14 | enter the Kennzahl / tick |
| Art der Leistung / Betrag (up to three entries) | 10–11 | 15–17 | "Staking-Einkünfte" / "Lending-Rewards" / "Mining" with EUR amount at receipt |
| Summe der Einnahmen | 10–11 | 18 | sect_22_3_income_eur |
| Werbungskosten | 15 | 19 | 0 (oder tatsächlich nachgewiesen) |
| Einkünfte (Einnahmen minus Werbungskosten) | 16 | 20 | computed |

**Freigrenze §22 Nr.3:** 256 EUR Freigrenze — below 256 EUR tax-free; from 256 EUR **fully** taxable from the first euro (§22 Nr.3 S. 2 EStG; unchanged for 2025).

---

## §23 EStG — Private Veräußerungsgeschäfte — Kryptowerte (Zeilen 45–51)

All Zeilen: **[secondary-source, official PDF not yet checked]**. The 2025 form has a dedicated Kryptowerte block (2024: shared block "Virtuelle Währungen, sonstige Token und andere Wirtschaftsgüter" at 41–55). Gold, Kunst and other andere Wirtschaftsgüter are entered in their own block on the 2025 form — Zeile numbers for that block not captured here.

| Field | Zeile 2024 | Zeile 2025 | Source from crypto-ledger yearly_tax_summary[2025] |
|---|---|---|---|
| Kennzahl "1" — Kryptowerte veräußert | 42 (marker "Kryptowährungen") | 45 | tick / enter "1" |
| Bezeichnung (Coin) / Verweis auf Steuerreport | 43 | 46 | "Bitcoin, Ethereum, ... — siehe beigefügten Steuerreport" |
| Zeitraum (Anschaffung / Veräußerung) | 44–45 | 47 | per-lot acquisition_date, per-disposal disposal_date (or range covered by the Steuerreport) |
| Veräußerungspreis (Summe) | 46 | 48 | sum of proceeds_eur |
| Anschaffungskosten (Summe) | 46 | 49 | sum of cost_basis_eur |
| Werbungskosten | — | 50 | trading fees not already in cost basis |
| Gewinn / Verlust | 53–55 | 51 | sect_23_net_eur |
| Freigrenze 1,000 EUR | automatisch | automatisch | §23 Abs. 3 S. 5 EStG — **unchanged** for 2025 |

> The 2025 block is aggregate (one Summe per field, backed by an attached Steuerreport / disposals CSV) — it no longer has per-transaction sub-blocks and separate Summenzeilen like the 2024 form's 41–47 / 48–52 / 53–55.

---

## 2025 Parameter Changes (Non-Zeile)

- **§23 Freigrenze:** 1,000 EUR/Person/Jahr (no change — in force since 2024).
- **§22 Nr.3 Freigrenze:** 256 EUR (below 256 tax-free; from 256 fully taxable) — no change.
- **BMF Krypto-Schreiben 06.03.2025:** clarified Simple Earn redemption handling and confirmed 1-year holding-period clock is not extended by lending/staking. This affects the classification logic in `crypto/references/transaction-taxonomy.yaml`, not the Anlage SO Zeile numbers.
- **Holding period for crypto:** 1 year remains (no 10-year extension for staked/lent coins — BMF 06.03.2025 confirmed).

---

## Open Items for 2025

| Item | Status |
|---|---|
| Kryptowerte block Zeilen 45–51 and Leistungen block Zeilen 14–20 | [secondary-source, official PDF not yet checked — Haufe + three preparer guides agree; fetch the BMF Anlage SO 2025 PDF and confirm] |
| Zeile numbers of the separate "andere Wirtschaftsgüter" (Gold, Kunst) block on the 2025 form | [not captured] |
| Verlustabzug-Zeile for §23 on the 2025 form (2024: Zeile 62) | [UNVERIFIED for 2025 — may have shifted] |

---

## Sources

- **Haufe — Änderungen in den Vordrucken der Überschusseinkünfte 2025:** https://www.haufe.de/steuern/finanzverwaltung/einkommensteuererklaerung-2025-aenderungen-in-den-vordrucken/aenderungen-in-den-vordrucken-der-ueberschusseinkuenfte-2025_164_670430.html (accessed 2026-09-01)
- **Blockpit — Krypto-Steuererklärung eintragen (Anlage SO 2025 Zeilen):** https://www.blockpit.io/de-de/steuer-guides/krypto-steuererklaerung-eintragen-anleitung (accessed 2026-09-01) — secondary source
- **BMF Formular-Management-System (2025 forms catalog):** https://www.formulare-bfinv.de/ (accessed 2026-04-17; Anlage SO 2025 PDF not yet fetched)
- **Steuerrat24 2025 Formulare Übersicht:** https://www.steuerrat24.de/steuererklaerung/steuererklaerung-2025/steuerformulare-2025.html (accessed 2026-04-17)
- **BMF-Schreiben 06.03.2025 "Einzelfragen zur ertragsteuerrechtlichen Behandlung bestimmter Kryptowerte":** https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf (accessed 2026-04-17)
- **For baseline Zeile-numbers (2024):** see `./anlage-so-mapping-2024.md`
