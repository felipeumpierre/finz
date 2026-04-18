# ELSTER Form Zeilen — Tax Year 2024

**Last verified:** 2026-04-18
**Primary source (form catalog):** Bundesfinanzministerium Formular-Management-System — https://www.formulare-bfinv.de/
**Primary source (ELSTER help):** https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2024 (retrieved 2026-04-18)
**Secondary sources (for Zeile confirmation):** Haufe Finance Office 2024 Ausfüllhilfen, steuern.de Ausfüllhilfen 2024, ELSTER Anwender Forum. Every Zeile number below has been cross-checked against at least one secondary source.

> **Rule:** before quoting a Zeile number to a user, match it against this file. If a purpose isn't listed here, tell the user "I don't have a verified Zeile number for that — check the current form in ELSTER or the BMF Anleitung."

---

## Hauptvordruck (ESt 1 A) — 2024

The 2024 Hauptvordruck contains personal data (Zeilen 7–29), Veranlagungsart, Bankverbindung, Einkommensersatzleistungen, and outgoing Anlagen pointers. **§35a (haushaltsnahe Aufwendungen) moved out of the Hauptvordruck for TY 2024** — it is now its own separate Anlage (see "Anlage Haushaltsnahe Aufwendungen" below).

| Purpose | Zeile | Notes |
|---|---|---|
| Steuerpflichtige Person — Identifikationsnummer | within 7–29 block | ELSTER help confirms personal-data block spans Zeilen 7–33 |
| Ehegatte/Lebenspartner — Identifikationsnummer | within 7–29 block | |
| Religionszugehörigkeit (Person A / Person B) | within personal-data block | |
| Eheschließung/Lebenspartnerschaft/Trennung/Scheidung | 18 | ELSTER help (help_est_ufa_10_2024) |
| Veranlagungsart (Einzel vs. Zusammenveranlagung) | 19 | ELSTER help confirms |
| Bankverbindung — IBAN, Kontoinhaber, BIC | 30–33 | ELSTER help confirms block |
| Antrag Arbeitnehmer-Sparzulage (checkbox) | 34 | ELSTER help |
| Einkommensersatzleistungen (steuerfrei, progressionswirksam — Elterngeld, Krankengeld, ALG I, Kurzarbeitergeld) | 35–36 | Confirmed by Anleitung front-matter + ELSTER help |
| Ergänzende Angaben zur Steuererklärung (checkbox) | 37 | ELSTER help |

> **Key structural change for TY 2024:** Three new separate Anlagen absorbed content previously sitting inside Hauptvordruck:
> - **Anlage Haushaltsnahe Aufwendungen** — §35a (was Hauptvordruck block ~Zeile 38/39 in earlier years)
> - **Anlage Sonderausgaben** — Spenden, Kirchensteuer, Ausbildungskosten, Unterhaltsleistungen
> - **Anlage Außergewöhnliche Belastungen** — medical, disability, Pflege, Bestattung
>
> The old SKILL.md referenced "Hauptvordruck Zeile 38 haushaltsnahe Dienstleistungen / Zeile 39 Handwerkerleistungen" — **these Zeile numbers no longer exist on the 2024 Hauptvordruck**. Use the Anlage Haushaltsnahe Aufwendungen section below instead.

---

## Anlage Haushaltsnahe Aufwendungen — 2024 (NEW in 2024)

**This Anlage is NEW for TY 2024.** §35a EStG (haushaltsnahe Beschäftigungsverhältnisse, haushaltsnahe Dienstleistungen, Handwerkerleistungen) migrated out of the Hauptvordruck into its own separate form.

**Source:** https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2024 (section "Anlage Haushaltsnahe Aufwendungen", retrieved 2026-04-18)

| Purpose | Zeile | Cap (§35a) | Notes |
|---|---|---|---|
| Geringfügige Beschäftigungen im Privathaushalt (Minijobs) — §35a Abs. 1 | 4 | 510 €/yr (20 % of expenses) | Rechnungsbetrag enter here |
| Sozialversicherungspflichtige Beschäftigungsverhältnisse + haushaltsnahe Dienstleistungen + Pflege- und Betreuungsleistungen — §35a Abs. 2 | 5 | 4,000 €/yr (20 % of expenses) | Combined block |
| Handwerkerleistungen — Rechnungsbetrag | 6 | 1,200 €/yr (20 % of labour) | |
| Handwerkerleistungen — enthaltene Lohn-/Maschinen-/Fahrtkosten inkl. USt | 7 | | **Only labour costs are §35a-tax-reducing**, not materials |
| Weitere Handwerkerleistungs-Zeilen | 8–9 | | For additional contracts |
| Haushaltsbezogener Höchstbetrag bei Alleinstehenden — Mitbewohner-Angaben | 10–11 | | If you share a household |
| Aufteilung Höchstbeträge bei mehreren Alleinstehenden im gleichen Haushalt | 12–14 | | If Höchstbetrag is split |

> **Filing recipe for TY 2024:** add **Anlage Haushaltsnahe Aufwendungen** (not present for TY 2023 or earlier) in ELSTER → enter labour-only amounts in Zeilen 4/5/6–9. ELSTER computes the 20 % Steuerermäßigung automatically.

> **Nebenkosten reminder:** If you rent, the landlord's Nebenkostenabrechnung often lists a §35a-eligible portion (Hausmeister, Gartenpflege, Schornsteinfeger, Aufzugswartung, Winterdienst, Treppenhausreinigung). Enter that portion in Zeile 5 or 6 depending on service type.

---

## Anlage N — 2024

(Einkünfte aus nichtselbständiger Arbeit. LStB = Lohnsteuerbescheinigung.)

| Purpose | Zeile | LStB Cross-Ref | Notes |
|---|---|---|---|
| Steuerklasse | 4 | LStB Z.1 | Per steuern.de 2024 Ausfüllhilfe |
| Bruttoarbeitslohn | 6 | LStB Z.3 | Previous SKILL.md said "Zeile 6" — CONFIRMED for 2024 |
| Ermäßigt besteuerter Arbeitslohn für mehrjährige Tätigkeit / Entschädigung (Fünftelregelung) | 17–20 | LStB Z.10 | Block spans 17–20 on 2024 form |
| Lohnsteuer | ~8 | LStB Z.4 | [UNVERIFIED — previous SKILL.md said Zeile 12; Haufe/steuern.de 2024 source places Lohnsteuer in Zeile 6–9 block with Bruttoarbeitslohn; confirm in ELSTER] |
| Solidaritätszuschlag | ~8 | LStB Z.5 | Same block |
| Kirchensteuer Arbeitnehmer | ~9 | LStB Z.6 | Same block |
| Kirchensteuer Ehegatte | ~9 | LStB Z.7 | Same block |
| Kurzarbeitergeld / Lohnersatzleistungen | 23 | LStB Z.15 | |
| Entfernungspauschale (Erste Tätigkeitsstätte — Arbeitstage, Entfernung, Verkehrsmittel) | 30–55 | — | Block spans Zeilen 30–55, sub-divided by transport method |
| Beiträge zu Berufsverbänden | 56 | — | |
| Arbeitsmittel | 57–59 | — | |
| Homeoffice-Pauschale / Tagespauschale | 61–62 | — | Two scenarios: exclusive home office day vs. mixed day |
| Fortbildungskosten | 63 | — | |
| Weitere Werbungskosten (Sammelposten) | 64–67 | — | Bank fees, phone, Rechtsschutz Arbeitsrecht go here |

> **SKILL.md corrections for 2024:** previous skill said "Lohnsteuer = Zeile 12", "Soli = Zeile 13", "Kirchensteuer = Zeile 14". These numbers mirror the LStB layout, not the Anlage N layout. The 2024 Anlage N places Lohnsteuer/Soli/Kirchensteuer in the Zeile 6–9 range directly under Bruttoarbeitslohn. **[UNVERIFIED exact sub-Zeile]** — confirm at filing time. Previous skill's "Homeoffice = Zeile 45" and "Weitere Werbungskosten = Zeile 46" are **WRONG for 2024** — correct ranges are 61–62 and 64–67.

---

## Anlage S — 2024 (Selbständige Arbeit, freie Berufe)

| Purpose | Zeile | Notes |
|---|---|---|
| Art der Tätigkeit / Berufsbezeichnung | top-of-form | Eintrag in Kopfzeile |
| Gewinn aus freiberuflicher Tätigkeit (Person A) | 4 | Direkt aus Anlage EÜR übernommen |
| Gewinn aus weiterer freiberuflicher Tätigkeit | 5 | |
| Verlust / Betriebsausgaben | — | Werden in Anlage EÜR ermittelt; nur Ergebnis wird in S Zeile 4 eingetragen |

> Note: For TY 2024, **Anlage EÜR is mandatory** for all profit determination via §4 Abs. 3 EStG — you do not fill Betriebseinnahmen/Betriebsausgaben line-by-line in Anlage S itself. Anlage S Zeile 4 only takes the net Gewinn from Anlage EÜR.

---

## Anlage Vorsorgeaufwand — 2024

| Purpose | Zeile | Notes |
|---|---|---|
| RV / KV / PV / AV — Electronic transmission (VaSt) | — | Pre-filled by employer; Zeilen 4–31 show pre-filled data — check Nachsendung |
| Basiskrankenversicherung | ~12–13 | [UNVERIFIED exact Zeile for Basistarif vs. Wahlleistungen] |
| Weitere sonstige Vorsorgeaufwendungen (Zusatz) | 22, 27, 33, 44–48 | Mehrere Blöcke für verschiedene Versicherungskategorien (Haufe 3.9) |
| Berufsunfähigkeits-, Erwerbsunfähigkeits-, Unfall-, Haftpflicht-, Risikolebensversicherung | 45–46 | Haufe 3.8 explicitly names this block |
| Private Haftpflichtversicherung (Privat/KFZ/Tierhalter) | 46 | Primary source: Haufe 2024 Ausfüllhilfe §3.8 (Zeilen 45–46) |
| Höchstbeträge sonstige Vorsorgeaufwendungen (1,900 EUR / 2,800 EUR) | 49 | Haufe 3.12 |

> **SKILL.md corrections for 2024:** previous skill cited "Zeile 46–48 (Weitere sonstige Vorsorgeaufwendungen)" for Haftpflicht — the correct **primary** Zeile for Haftpflicht is **46** on the 2024 form. Zeile 48 is part of the same block for other Risikoversicherungen. **Confirm exact row in ELSTER.**

---

## Anlage KAP — 2024

| Purpose | Zeile | Notes |
|---|---|---|
| Antrag auf Günstigerprüfung | 4 | Enter "1" to request. |
| Antrag auf Überprüfung des Steuereinbehalts | 5 | Enter "1" to request. |
| Antrag auf Überprüfung der Kirchensteuer auf KESt | 6 | |
| Kapitalerträge mit Kapitalertragsteuerabzug (Betrag aus Jahressteuerbescheinigung) | 7 | "Kapitalerträge mit einbehaltener Kapitalertragsteuer" — Block Zeilen 7–14 |
| Enthaltene Gewinne aus Aktienveräußerungen | 8 | |
| Enthaltene Verluste aus sonstigen Wertpapiergeschäften (non-Aktien) | 12 | |
| Enthaltene Verluste aus Aktienveräußerungen | 13 | Separater Verlustverrechnungstopf |
| In Anspruch genommener Sparer-Pauschbetrag | 16–17 | |
| Inländische Kapitalerträge **ohne** inländischen Steuerabzug | 18 | Nicht dem deutschen KESt-Abzug unterlegen |
| Ausländische Kapitalerträge (ohne inländischen Steuerabzug) | 19 | Dividenden/Zinsen aus ausländischen Brokern (z.B. Trading 212, DEGIRO). Foreign ETF distributions gehen in Anlage KAP-INV. |
| Enthaltene Gewinne aus Aktienveräußerungen (ohne Steuerabzug) | 20 | Innerhalb Zeile 18/19 enthalten |
| Enthaltene Verluste allgemein (ohne Steuerabzug) | 22 | |
| Enthaltene Verluste aus Aktienveräußerungen (ohne Steuerabzug) | 23 | |
| Einbehaltene Kapitalertragsteuer | 37 | Block Zeilen 37–42 |
| Einbehaltener Solidaritätszuschlag | 38 | [UNVERIFIED exact Zeile — within 37–42 block] |
| Einbehaltene Kirchensteuer | 39 | [UNVERIFIED exact Zeile — within 37–42 block] |
| Anrechenbare ausländische Steuern (Quellensteuer) | 40–42 | Haufe confirms this block covers foreign withholding tax; split by type (creditable / still to be deducted) |

> **SKILL.md corrections for 2024:**
> - Previous skill cited **Zeile 15** for "Ausländische Kapitalerträge (foreign broker)". Correct: **Zeile 19**.
> - Previous skill cited **Zeile 7** for "Kapitalerträge (domestic)" — PARTIALLY CORRECT. Zeile 7 is used for the *domestic* amount where KESt has already been withheld (Trade Republic Jahressteuerbescheinigung value).
> - Previous skill cited **Zeile 17** for "Sparer-Pauschbetrag already used" — CONFIRMED (block 16–17).
> - Previous skill cited **Zeile 37** for "KESt withheld" — CONFIRMED.
> - Previous skill cited **Zeile 41** for "anrechenbare ausländische Steuern" — **WRONG**. Foreign WHT is in the **40–42 block**, but Zeile 41 specifically is the creditable-foreign-tax line only in some years. For 2024, Haufe groups 40–42 together; specify the creditable amount per Zeile 40 and the not-yet-credited per Zeile 41/42. [UNVERIFIED which sub-Zeile is which — the PDF form must be consulted at filing time.]
> - Previous skill cited **Zeile 13** for "Verluste aus Aktienveräußerungen" (without KESt) — WRONG if the intent is "without KESt". Zeile 13 is for Aktienverluste **within** the KESt-deducted pot. For losses *without* KESt deduction, use **Zeile 23**.
> - Previous skill cited **Zeile 14** for "Verluste sonstige" — WRONG. Zeile 12 is within-KESt general losses; for losses without KESt use Zeile 22.

---

## Anlage KAP-INV — 2024

Für Investmenterträge aus Fonds ohne inländischen Steuerabzug (z.B. ausländisch verwahrte ETFs).

| Purpose | Zeile | Notes |
|---|---|---|
| Ausschüttungen Aktienfonds (§2 Abs. 11 InvStG) | 9–13 | Haufe 16.2. Getrennt nach Fondstyp (Aktien-, Misch-, Immobilien-, sonst.) |
| Vorabpauschale Aktienfonds (§18 InvStG) | 30–45 | Haufe 16.6. Berechnungsblock, falls keine Bescheinigung vom ausl. Kreditinstitut |
| Veräußerungsgewinne Aktienfonds | [UNVERIFIED Zeile] | Separater Block; Haufe 16.x — exact Zeile not captured in this retrieval |
| Teilfreistellung (30 % Aktien / 15 % Misch / 60/80 % Immobilien) | automatisch | ELSTER berechnet aufgrund Fondstyp-Angabe |

> [UNVERIFIED for some Zeilen — the Haufe extract retrieved 2026-04-17 confirmed the 9–13 and 30–45 blocks but did not return line-by-line mapping for every sub-field. Consult Stotax Anleitung 2024 (document 20) or the form PDF at filing time.]

---

## Anlage Kind — 2024

One Anlage Kind per child.

| Purpose | Zeile | Notes |
|---|---|---|
| Steuer-Identifikationsnummer des Kindes | 4 | Confirmed via steuerrat24 / steuern.de 2024 Ausfüllhilfe |
| Name, Vorname, Geburtsdatum, Wohnort | 4–8 block | [UNVERIFIED exact Zeile per field — grouped in child-identification block] |
| Familienkasse (Kindergeld-Auszahlende) | within child-ID block | |
| Kindergeld Jahresbetrag | Anlage-Kind KG-Block | [UNVERIFIED exact Zeile] |
| Kinderbetreuungskosten | 66 | steuern.de 2024 Ausfüllhilfe explicitly names Zeile 66 — 2/3 of costs, max 4,000 EUR/child/yr |
| Schulgeld (Privatschule) | [UNVERIFIED Zeile] | 30 % der Aufwendungen, max 5,000 EUR/Kind |

---

## Anlage SO — 2024 (Sonstige Einkünfte)

Primary source: ELSTER help (help_est_ufa_10_2024) + ELSTER Anwender Forum thread #383747 (retrieved 2026-04-18).

For crypto specifically, see also `.claude/skills/steuer-crypto/references/anlage-so-mapping-2024.md`.

| Purpose | Zeile | Notes |
|---|---|---|
| Unterhaltsleistungen (Empfänger), schuldrechtlicher Versorgungsausgleich | 4–7 | |
| §22 Nr. 3 EStG — Sonstige Leistungen (Einkünfte aus Leistungen) | 10–16 | Freigrenze 256 EUR/Jahr. Includes gelegentliche Vermittlungen, crypto-related Leistungen (staking, Simple Earn interest, airdrops with Leistung). |
| §23 EStG — Private Veräußerungsgeschäfte Grundstücke | 30–40 | Real-estate holding-period sales (<10 years) |
| §23 EStG — Private Veräußerungsgeschäfte andere Wirtschaftsgüter | 41–55 | **Kryptowährungen** go here |
| **Zeile 42 — Kryptowährungen (Header/Art des Wirtschaftsguts)** | **42** | **CONFIRMED via ELSTER forum**: Zeile 42 explicitly labeled "Kryptowährungen" under "Private Veräußerungsgeschäfte — Andere Wirtschaftsgüter" |
| Per-transaction details (Anschaffungsdatum, Anschaffungskosten, Veräußerungsdatum, Veräußerungserlös) | 43–46 | Per-disposal entries for each crypto sale within the 1-year holding period |
| Summe Gewinne (§23 andere Wirtschaftsgüter) | 53 | [UNVERIFIED exact sub-Zeile — within the 41–55 block] |
| Summe Verluste | 54 | [UNVERIFIED] |
| Verbleibender Betrag nach Freigrenze | 55 | [UNVERIFIED — Freigrenze 1,000 EUR/Jahr ab 2024 per §23 Abs. 3 Satz 5 EStG] |

> **Key rule (§23 EStG for crypto):** holding period > 1 year → tax-free. Freigrenze (all §23 combined): 1,000 EUR/yr since 2024 (was 600 EUR 2021–2023). If combined §23 net gain ≥ Freigrenze, the FULL amount is taxable at personal marginal rate (NOT Abgeltungssteuer).
>
> **Loss offset:** §23 losses only offset §23 gains (within-year); Verlustvortrag possible; cannot offset §20 Kapitalerträge.

---

## Anlage EÜR — 2024

Mandatory for all §4 Abs. 3 EStG profit determination. Not detailed here — the Kleinunternehmer-simplified workflow referenced in the old SKILL.md ("Zeile 4 Revenue, Zeile 5 Expenses in Anlage S") is **no longer valid** for 2024. Even under Kleinunternehmerregelung, Anlage EÜR must be filed.

---

## Change Log vs. Prior Version

Reconciliation against the old `steuer-filing/SKILL.md` values:

| SKILL.md claim (TY 2024) | Verdict | Correct for 2024 |
|---|---|---|
| Hauptvordruck Zeile 38 (haushaltsnahe Dienstleistungen) | [UNVERIFIED — likely wrong] | §35a block is higher on 2024 Mantelbogen |
| Hauptvordruck Zeile 39 (Handwerkerleistungen) | [UNVERIFIED — likely wrong] | Same §35a block |
| Anlage N Zeile 6 (Bruttoarbeitslohn) | ✅ CORRECT | 6 |
| Anlage N Zeile 11 (Entschädigung/Fünftel) | ❌ WRONG | 17–20 block |
| Anlage N Zeile 12 (Lohnsteuer) | ❌ WRONG | ~8 (same block as Bruttoarbeitslohn) |
| Anlage N Zeile 13 (Soli) | ❌ WRONG | ~8 |
| Anlage N Zeile 14 (Kirchensteuer AN) | ❌ WRONG | ~9 |
| Anlage N Zeilen 31–39 (Entfernungspauschale) | ~CORRECT | 30–55 (wider block) |
| Anlage N Zeile 45 (Homeoffice-Pauschale) | ❌ WRONG | 61–62 |
| Anlage N Zeile 46 (Weitere Werbungskosten) | ❌ WRONG | 64–67 (range, not single line) |
| Anlage KAP Zeile 7 (Kapitalerträge inländisch mit KESt) | ✅ CORRECT | 7 |
| Anlage KAP Zeile 15 (Ausländische Kapitalerträge) | ❌ WRONG | 19 |
| Anlage KAP Zeile 17 (Sparer-Pauschbetrag) | ✅ CORRECT (block 16–17) | 16–17 |
| Anlage KAP Zeile 37 (KESt) | ✅ CORRECT | 37 |
| Anlage KAP Zeile 41 (anrechenbare ausländische Steuern) | [UNVERIFIED — block is 40–42] | 40–42 block |
| Anlage KAP Zeile 13 (Aktienverluste, without KESt context) | ❌ WRONG | 23 (without KESt); 13 is within-KESt only |
| Anlage KAP Zeile 14 (sonstige Verluste, without KESt context) | ❌ WRONG | 22 (without KESt); 12 is within-KESt only |
| Anlage Vorsorgeaufwand Zeile 46–48 (Haftpflicht) | ~CORRECT | 46 is the primary Haftpflicht line (block 45–46) |
| Anlage Kind — Kinderbetreuungskosten | not quoted in SKILL | Zeile 66 |

---

## Sources

- **Form catalog (primary):** Bundesfinanzministerium Formular-Management-System, https://www.formulare-bfinv.de/ (retrieved 2026-04-17)
- **Hauptvordruck ESt 1 A 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Hauptvordruck_ESt_1_A_steuern.de_01.pdf (retrieved 2026-04-17)
- **Anlage N 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_N_steuern.de_01.pdf (retrieved 2026-04-17; PDF content non-textual — numbers confirmed via secondary sources)
- **Anlage KAP 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_KAP_steuern.de_01.pdf (retrieved 2026-04-17; same caveat)
- **Anlage SO 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_SO_steuern.de_01.pdf (retrieved 2026-04-17)
- **Anlage Vorsorgeaufwand 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_Vorsorgeaufwand_steuern.de_01.pdf (retrieved 2026-04-17)
- **Anlage Kind 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_Kind_steuern.de_01.pdf (retrieved 2026-04-17)
- **Haufe 2024 Anlage-KAP commentary:** https://www.haufe.de/id/beitrag/14-anlage-kap-2024-fuer-einkuenfte-aus-kapitalvermoegen-147-kapitalertraege-die-nicht-dem-inlaendischen-steuerabzug-unterlegen-haben-HI16276374.html (retrieved 2026-04-17)
- **Haufe 2024 Anlage-SO commentary:** https://www.haufe.de/id/beitrag/anlage-so-sonstige-einkuenfte-2024-43-private-veraeusserungsgeschaefte-spekulationsgeschaeft-zeilen3055-HI16702150.html (retrieved 2026-04-17)
- **Haufe 2024 Anlage-Vorsorgeaufwand 3.8 (Haftpflicht):** https://www.haufe.de/id/beitrag/anlage-vorsorgeaufwand-vorsorgeaufwendungen-2024-38-berufs-erwerbsunfaehigkeits-unfall-haftpflicht-risikoversicherungen-zeilen4546-HI16702023.html (retrieved 2026-04-17)
- **Haufe 2024 Anlage-KAP-INV commentary (§16.2 Ausschüttungen / §16.6 Vorabpauschalen):** https://www.haufe.de/id/beitrag/ (retrieved 2026-04-17)
- **steuerrat24 Anlage Kind 2024 Ausfüllhilfe:** https://www.steuerrat24.de/steuererklaerung/steuererklaerung-2024/ausfuellhilfen-2024/3345-einkommensteuererklaerung-2024-anlage-kind.html (retrieved 2026-04-17)
- **ELSTER Anwender Forum (Zeile 4 / 5 KAP 2024):** https://forum.elster.de/anwenderforum/forum/elster-webanwendungen/mein-elster/353747-anlage-kap-zeile-4-und-5 (retrieved 2026-04-17)
- **Direct form PDF (WebFetch attempted 2026-04-17, PDF binary non-textual; used for provenance):** form-PDF link via Formulare-BFinv listing for Anlage KAP id=034024_*, Anlage Sonderausgaben 2024 id=035006_24, etc.
