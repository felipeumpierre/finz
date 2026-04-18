# Anlage SO — Crypto Mapping — Tax Year 2024

**Last verified:** 2026-04-18
**Primary source (form catalog):** Bundesfinanzministerium Formular-Management-System — https://www.formulare-bfinv.de/
**Primary source (ELSTER help):** https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2024 (retrieved 2026-04-18)
**Primary source (Zeile 42 confirmation):** ELSTER Anwender Forum thread #383747 — https://forum.elster.de/anwenderforum/forum/elster-webanwendungen/mein-elster/383747-anlage-so-zeilen-10-und-49 (retrieved 2026-04-18). Forum participants explicitly confirm: *"In der Anlage SO gehst du auf Private Veräußerungsgeschäfte - Andere Wirtschaftsgüter Zeile 42 'Kryptowährungen'"*; Zeilen 43–46 hold per-transaction details.
**Form PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_SO_steuern.de_01.pdf (retrieved 2026-04-17)
**Secondary source (cross-check):** Haufe 2024 Anlage-SO commentary §4.3 (Zeilen 30–55), steuern.de Ausfüllhilfe Anlage SO

> **Correction from the retired `anlage-so-mapping.md`:** the previous file claimed §23 uses Zeilen 41/42/43/46 and §22 Nr.3 uses Zeilen 10/12. For the **2024** form, §23 for crypto/Gold/andere Wirtschaftsgüter uses **Zeilen 41–55** (Grundstücke are in 30–40). §22 Nr.3 uses Zeilen 10–16. The old mapping numbers (41/42/43/46) were a guess and did not correspond to the correct sub-lines for crypto.

---

## §22 Nr.3 EStG — Sonstige Einkünfte (Staking-Rewards, Earn, Lending, Leistungen außerhalb §23)

| Field | Zeile | Source from crypto-ledger yearly_tax_summary[2024] |
|---|---|---|
| Art der Leistung | 10–11 | "Staking-Einkünfte" / "Lending-Rewards" / "Earn-Rewards" |
| Einnahmen | 10–11 | sect_22_3_income_eur |
| Werbungskosten | 15 | 0 (oder tatsächlich nachgewiesen) |
| Gewinn/Verlust | 16 | (Differenz 10-11 minus 15) |

**Freigrenze §22 Nr.3:** 255 EUR/Jahr. Unter 256 EUR: steuerfrei; ab 256 EUR: **voll** steuerpflichtig ab dem ersten Euro.

---

## §23 EStG — Private Veräußerungsgeschäfte — "Virtuelle Währungen, sonstige Token und andere Wirtschaftsgüter" (Zeilen 41–55)

**Official 2024 block label** (per ELSTER help help_est_ufa_10_2024, retrieved 2026-04-18): *"Virtuelle Währungen, sonstige Token und andere Wirtschaftsgüter"* — covers crypto, NFTs, Gold, Kunst, other chattel sold within the 1-year holding period.

Grundstücke laufen in **Zeilen 30–40** (separater Block "Grundstücke und grundstücksgleiche Rechte") und sind **nicht** Teil des Crypto-Use-Cases.

**Verlustabzug zu privaten Veräußerungsgeschäften:** Zeile **62** (Verlustvortrag §23).

| Field | Zeile | Source from crypto-ledger yearly_tax_summary[2024] |
|---|---|---|
| **Art des Wirtschaftsguts** — checkbox/selector "Kryptowährungen" | **42** | **CONFIRMED** via ELSTER Anwender Forum; primary marker for crypto disposals |
| Bezeichnung / Coin (z.B. "Bitcoin", "Ethereum", "Solana") | 43 | per-disposal record, coin field |
| Anschaffungszeitpunkt | 44 | per-lot, acquisition_date |
| Veräußerungszeitpunkt | 45 | per-disposal, disposal_date |
| Veräußerungspreis / Anschaffungskosten / Gewinn | 46 | per-disposal, proceeds_eur / cost_basis_eur / gain_eur |
| Art des Wirtschaftsguts (weiterer Block — z.B. Gold, andere Krypto-Coins) | 48 | |
| Anschaffungs-/Veräußerungszeitpunkt (weiterer Block) | 49 | |
| Veräußerungspreis (weiterer Block) | 50 | |
| Anschaffungskosten (weiterer Block) | 51 | |
| Gewinn/Verlust (weiterer Block) | 52 | |
| **Summe der Gewinne** | 53 | sect_23_gain_eur (all positive lines summed) |
| **Summe der Verluste** | 54 | sect_23_loss_eur (absolute value of all negative lines) |
| **Verbleibender Gewinn / Verlust (Saldo)** | 55 | sect_23_net_eur |
| Freigrenze 1,000 EUR | automatisch | Ab 2024: 1,000 EUR/Person/Jahr (vorher 600 EUR); ELSTER wendet an |

> **Structure note:** Haufe §4.3 confirms Zeilen 30–55 as the full Private-Veräußerungsgeschäfte block. The retrieved mapping splits that block:
> - 30–40: Grundstücke & grundstücksgleiche Rechte
> - 41–47: erster Block "andere Wirtschaftsgüter" (bis zu einem Veräußerungsgeschäft pro Block; bei mehreren Geschäften die weiteren Einzelheiten über zusätzliche Anlagen SO oder eine Gesamtaufstellung)
> - 48–52: zweiter Block "andere Wirtschaftsgüter"
> - 53–55: Summenzeilen und Saldo
>
> **[UNVERIFIED per-sub-line]:** the exact one-Zeile-per-field mapping within 41–47 (Art / Anschaffung / Veräußerung / Preis / Kosten / Gewinn) was not extractable from the PDF binary via WebFetch. When filing, verify in ELSTER that each sub-field has the expected label.

---

## Workflow Rules

1. **Freigrenze application.** The §23 net result (Zeile 55) is tax-free only if the **total** §23 gains across **all** andere Wirtschaftsgüter (crypto + Gold + any other) for the year are **below** 1,000 EUR. If >= 1,000 EUR, the **full** amount is taxable from the first euro.
2. **Losses carry forward.** §23 losses can only offset §23 gains (same category — private Veräußerungsgeschäfte). If the year ends in a §23 net loss, request Verlustfeststellung so the Finanzamt carries it forward. [UNVERIFIED exact checkbox Zeile on Anlage SO 2024; may be on the Mantelbogen.]
3. **§22 Nr.3 vs. §23 separation.** Staking rewards that qualify as *Leistung* go to §22 Nr.3 at receipt (EUR value at receipt date). When the acquired coins are later sold, the later sale is a §23 disposal with the §22 Nr.3 receipt-date EUR value as the acquisition cost basis. Do not double-count.
4. **1-year holding period.** Per BMF 06.03.2025, the 10-year extension for staked/lent coins is **NOT** applied — the standard 1-year holding still applies. Once held >1 year, disposals are tax-free regardless of staking.

---

## Sources

- **Anlage SO 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_SO_steuern.de_01.pdf (retrieved 2026-04-17)
- **Haufe 2024 Anlage SO §4.3 (Zeilen 30–55):** https://www.haufe.de/id/beitrag/anlage-so-sonstige-einkuenfte-2024-43-private-veraeusserungsgeschaefte-spekulationsgeschaeft-zeilen3055-HI16702150.html (retrieved 2026-04-17)
- **steuern.de Anlage SO 2024 Ausfüllhilfe:** https://www.steuern.de/steuererklaerung-anlage-so (retrieved 2026-04-17)
- **BMF-Schreiben 06.03.2025 "Einzelfragen zur ertragsteuerrechtlichen Behandlung bestimmter Kryptowerte":** https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf (retrieved 2026-04-17)
- **§22 Nr.3 EStG Freigrenze 255 EUR:** https://www.gesetze-im-internet.de/estg/__22.html
- **§23 EStG Freigrenze 1,000 EUR (since 2024):** https://www.gesetze-im-internet.de/estg/__23.html
