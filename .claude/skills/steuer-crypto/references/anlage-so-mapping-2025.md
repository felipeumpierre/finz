# Anlage SO — Crypto Mapping — Tax Year 2025

**Last verified:** 2026-04-17
**Status:** Anlage SO 2025 was published in the 2025 form set (Steuerrat24 / BMF Formular-Management-System confirm). The Mantelbogen was restructured for 2025 but **Anlage SO structure is expected to be preserved** from 2024 — the §23 Private Veräußerungsgeschäfte block and the §22 Nr.3 Sonstige Leistungen block did not have any announced restructure for TY 2025.
**Primary source:** Bundesfinanzministerium Formular-Management-System — https://www.formulare-bfinv.de/ (accessed 2026-04-17)

> **Rule for 2025 filings:** Treat every Zeile number below as presumed-carried-over from 2024 but flagged [UNVERIFIED for 2025] until it has been checked in the live ELSTER 2025 form. If the form shifts a single Zeile (e.g., because a new block was added), all downstream numbers shift too. Verify at filing time.

---

## §22 Nr.3 EStG — Sonstige Einkünfte (Staking-Rewards, Earn, Lending, Leistungen außerhalb §23)

| Field | Zeile 2024 | Zeile 2025 | Source from crypto-ledger yearly_tax_summary[2025] |
|---|---|---|---|
| Art der Leistung | 10–11 | 10–11 [UNVERIFIED for 2025] | "Staking-Einkünfte" / "Lending-Rewards" |
| Einnahmen | 10–11 | 10–11 [UNVERIFIED for 2025] | sect_22_3_income_eur |
| Werbungskosten | 15 | 15 [UNVERIFIED for 2025] | 0 |
| Gewinn/Verlust | 16 | 16 [UNVERIFIED for 2025] | computed |

**Freigrenze §22 Nr.3:** 255 EUR/Jahr — **unchanged** for 2025 (§22 Nr.3 EStG).

---

## §23 EStG — Private Veräußerungsgeschäfte — andere Wirtschaftsgüter (Kryptowährungen, Gold, Kunst)

| Field | Zeile 2024 | Zeile 2025 | Source from crypto-ledger yearly_tax_summary[2025] |
|---|---|---|---|
| Art des Wirtschaftsguts / Bezeichnung | 41–47 | 41–47 [UNVERIFIED for 2025] | per-disposal, coin |
| Anschaffungszeitpunkt | 41–47 | 41–47 [UNVERIFIED for 2025] | per-lot |
| Veräußerungszeitpunkt | 41–47 | 41–47 [UNVERIFIED for 2025] | per-disposal |
| Veräußerungspreis | 41–47 | 41–47 [UNVERIFIED for 2025] | per-disposal |
| Anschaffungskosten | 41–47 | 41–47 [UNVERIFIED for 2025] | per-lot |
| Gewinn/Verlust pro Vorgang | 41–47 | 41–47 [UNVERIFIED for 2025] | per-disposal |
| Zweiter Block (andere Wirtschaftsgüter) | 48–52 | 48–52 [UNVERIFIED for 2025] | |
| Summe der Gewinne | 53 | 53 [UNVERIFIED for 2025] | sect_23_gain_eur |
| Summe der Verluste | 54 | 54 [UNVERIFIED for 2025] | sect_23_loss_eur |
| Verbleibender Gewinn/Verlust (Saldo) | 55 | 55 [UNVERIFIED for 2025] | sect_23_net_eur |
| Freigrenze 1,000 EUR | automatisch | automatisch | §23 Abs. 3 S. 5 EStG — **unchanged** for 2025 |

---

## 2025 Parameter Changes (Non-Zeile)

- **§23 Freigrenze:** 1,000 EUR/Person/Jahr (no change — in force since 2024).
- **§22 Nr.3 Freigrenze:** 255 EUR/Jahr (no change).
- **BMF Krypto-Schreiben 06.03.2025:** clarified Simple Earn redemption handling and confirmed 1-year holding-period clock is not extended by lending/staking. This affects the classification logic in `crypto/references/transaction-taxonomy.yaml`, not the Anlage SO Zeile numbers.
- **Holding period for crypto:** 1 year remains (no 10-year extension for staked/lent coins — BMF 06.03.2025 confirmed).

---

## Open Items for 2025

| Item | Status |
|---|---|
| Confirmation that Anlage SO Zeilen 41–55 structure is preserved | [UNVERIFIED for 2025 — check form PDF at filing time] |
| Per-sub-line label mapping (Art / Anschaffung / Veräußerung / Preis / Kosten / Gewinn) within 41–47 and 48–52 | [UNVERIFIED — same caveat as 2024] |

---

## Sources

- **BMF Formular-Management-System (2025 forms catalog):** https://www.formulare-bfinv.de/ (accessed 2026-04-17)
- **Steuerrat24 2025 Formulare Übersicht:** https://www.steuerrat24.de/steuererklaerung/steuererklaerung-2025/steuerformulare-2025.html (accessed 2026-04-17)
- **BMF-Schreiben 06.03.2025 "Einzelfragen zur ertragsteuerrechtlichen Behandlung bestimmter Kryptowerte":** https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf (accessed 2026-04-17)
- **For baseline Zeile-numbers (2024):** see `./anlage-so-mapping-2024.md`
