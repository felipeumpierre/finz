# ELSTER Form Zeilen — Tax Year 2024

**Last verified:** 2026-04-18
**Primary source (form catalog):** Bundesfinanzministerium Formular-Management-System — https://www.formulare-bfinv.de/
**Primary source (ELSTER help):** https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2024 (retrieved 2026-04-18)
**Secondary sources:** Haufe Finance Office 2024 Ausfüllhilfen, steuern.de Ausfüllhilfen 2024, ELSTER Anwender Forum.

> **Rule:** before quoting a Zeile number to a user, match it against this file. If a purpose isn't listed here, tell the user "I don't have a verified Zeile number for that — check the current form in ELSTER or the BMF Anleitung."

> **Coverage note:** the ELSTER help provides Zeile **ranges** (e.g., "Zeile 7 bis 15: Kapitalerträge mit inländischem Steuerabzug") rather than one-label-per-Zeile. For sub-field specifics within a range, consult ELSTER directly at filing time.

---

## Hauptvordruck (ESt 1 A) — 2024

The 2024 Hauptvordruck contains personal data, Veranlagungsart, Bankverbindung, Einkommensersatzleistungen, and outgoing Anlagen pointers. **§35a (haushaltsnahe Aufwendungen) moved out of the Hauptvordruck for TY 2024** — it is now its own separate Anlage (see "Anlage Haushaltsnahe Aufwendungen" below).

| Purpose | Zeile | Notes |
|---|---|---|
| Allgemeine Angaben (Name, Adresse, IdNr, Religion, Ehegatte) | 7–33 | Personal-data block per ELSTER help |
| Eheschließung / Lebenspartnerschaft / Trennung / Scheidung (Datum) | 18 | |
| Veranlagungsart (Einzel vs. Zusammenveranlagung) | 19 | |
| Bankverbindung — IBAN, Kontoinhaber, BIC | 30–33 | |
| Antrag Arbeitnehmer-Sparzulage (checkbox) | 34 | |
| Einkommensersatzleistungen (steuerfrei, progressionswirksam — Elterngeld, Krankengeld, ALG I, Kurzarbeitergeld) | 35–36 | Progressionsvorbehalt |
| Ergänzende Angaben zur Steuererklärung (checkbox) | 37 | |

> **Key structural change for TY 2024:** Three new separate Anlagen absorbed content previously sitting inside Hauptvordruck:
> - **Anlage Haushaltsnahe Aufwendungen** — §35a (was Hauptvordruck Zeile 38/39 in earlier years)
> - **Anlage Sonderausgaben** — Spenden, Kirchensteuer, Ausbildungskosten, Unterhaltsleistungen
> - **Anlage Außergewöhnliche Belastungen** — medical, disability, Pflege, Bestattung
>
> Old SKILL.md references to "Hauptvordruck Zeile 38/39" are **no longer valid** for 2024.

---

## Anlage Haushaltsnahe Aufwendungen — 2024 (NEW in 2024)

**This Anlage is NEW for TY 2024.** §35a EStG (haushaltsnahe Beschäftigungsverhältnisse, haushaltsnahe Dienstleistungen, Handwerkerleistungen) migrated out of the Hauptvordruck into its own separate form.

| Purpose | Zeile | Cap (§35a) | Notes |
|---|---|---|---|
| Aufwendungstypen (Minijob, Dienstleistungen, Handwerker, Pflege) | 4–9 | see below | ELSTER help lumps these as "Aufwendungen in die jeweiligen Zeilen" |
| Geringfügige Beschäftigungen im Privathaushalt (Minijobs) — §35a Abs. 1 | 4 | 510 €/yr (20 %) | |
| Sozialversicherungspflichtige Beschäftigungsverhältnisse + haushaltsnahe Dienstleistungen + Pflege- und Betreuungsleistungen — §35a Abs. 2 | 5 | 4,000 €/yr (20 %) | |
| Handwerkerleistungen — Rechnungsbetrag | 6 | 1,200 €/yr (20 % labour only) | |
| Handwerkerleistungen — enthaltene Lohn-/Maschinen-/Fahrtkosten inkl. USt | 7 | | **Only labour is §35a-tax-reducing**, not materials |
| Weitere Handwerkerleistungs-Zeilen | 8–9 | | Additional contracts |
| Haushaltsbezogener Höchstbetrag bei Alleinstehenden | 10–11 | | Mitbewohner-Angaben |

> **Nebenkosten reminder:** If you rent, the landlord's Nebenkostenabrechnung often lists a §35a-eligible portion (Hausmeister, Gartenpflege, Schornsteinfeger, Aufzugswartung, Winterdienst, Treppenhausreinigung). Enter that portion in Zeile 5 or 6 depending on service type.

---

## Anlage N — 2024

(Einkünfte aus nichtselbständiger Arbeit. LStB = Lohnsteuerbescheinigung.)

| Purpose | Zeile | LStB Cross-Ref | Notes |
|---|---|---|---|
| Arbeitslohn block (Bruttoarbeitslohn, Versorgungsbezüge, Steuern einbehalten, SV-Beiträge) | 4–20 | LStB Z.3–Z.7 etc. | ELSTER help names "Zeile 4 bis 20: Arbeitslohn" as a block |
| Bruttoarbeitslohn | 6 | LStB Z.3 | Single confirmed sub-line within the 4–20 block |
| Arbeitslohn und Versorgungsbezüge für mehrere Jahre sowie Entschädigungen (Fünftelregelung) | 16–20 | LStB Z.10 | Sub-block within 4–20 |
| Arbeitslohn ohne Steuerabzug | 21 | — | e.g., foreign employer without inländischen Steuerabzug |
| Steuerfreie Aufwandsentschädigungen / Einnahmen | 22 | — | |
| Lohn- / Entgeltersatzleistungen (Kurzarbeitergeld, Krankengeld, ALG) | 23 | LStB Z.15 | Progressionsvorbehalt |
| Steuerfreier Arbeitslohn bei Auslandstätigkeit | 24–27 | — | Per DBA / Auslandstätigkeitserlass |
| Ansässigkeit in Belgien | 28 | — | Sonderfall |
| Grenzgänger | 29 | — | |
| **Werbungskosten block** | 30–86 | | Main employee-expense block |
| Entfernungspauschale (Wege zwischen Wohnung und erster Tätigkeitsstätte) | 30–53 | — | Subdivided by transport method; 30 Ct/km first 20 km, 38 Ct/km from 21st km |
| Ersatzleistungen des Arbeitgebers / der Agentur für Arbeit (z.B. Jobticket, Fahrtkostenzuschuss) | 54–55 | LStB Z.18 | Reduces Entfernungspauschale |
| Beiträge zu Berufsverbänden / Gewerkschaftsbeiträge | 56 | — | |
| Arbeitsmittel | 57–59 | — | Computer, Fachliteratur, Werkzeug |
| Aufwendungen für ein häusliches Arbeitszimmer | 60 | — | **Full room deduction** (§4 Abs. 5 Nr. 6b EStG) — mutually exclusive with Homeoffice-Pauschale |
| Homeoffice-Pauschale / Tagespauschale | 61–62 | — | 6 €/day × max 210 days = 1,260 €/yr (§4 Abs. 5 Nr. 6c EStG) |
| Fortbildungskosten | 63 | — | |
| Weitere Werbungskosten (Sammelposten) | 64–67 | — | Bank fees (Kontoführung 16 €), phone/internet share, Rechtsschutz Arbeitsrecht |
| Reisekosten bei beruflich veranlasster Auswärtstätigkeit | 68–80 | — | Full block |
| — Fahrt- und Übernachtungskosten, Reisenebenkosten | 68–74 | — | Sub-block |
| — Mehraufwendungen für Verpflegung (Verpflegungspauschale) | 75–80 | — | 14 €/28 €/Abwesenheit |
| Werbungskosten in Sonderfällen | 81–86 | — | Doppelte Haushaltsführung separate Anlage |

> **Sub-Zeile gaps still [UNVERIFIED]:** within Zeile 4–20 block, the exact sub-Zeile for einbehaltene Lohnsteuer (LStB Z.4), Solidaritätszuschlag (LStB Z.5), Kirchensteuer AN (LStB Z.6), Kirchensteuer Ehegatte (LStB Z.7) was not exposed by the ELSTER help granular listing — confirm in ELSTER when filing.

---

## Anlage S — 2024 (Selbständige Arbeit, freie Berufe)

| Purpose | Zeile | Notes |
|---|---|---|
| Art der Tätigkeit / Berufsbezeichnung | top-of-form | Eintrag in Kopfzeile |
| Gewinn aus freiberuflicher Tätigkeit (Person A) | 4 | Direkt aus Anlage EÜR übernommen |
| Gewinn aus weiterer freiberuflicher Tätigkeit | 5 | |

> **Note:** For TY 2024, **Anlage EÜR is mandatory** for all profit determination via §4 Abs. 3 EStG. Anlage S Zeile 4 only takes the net Gewinn from Anlage EÜR — you do not fill Betriebseinnahmen/Betriebsausgaben line-by-line in Anlage S itself.

---

## Anlage Vorsorgeaufwand — 2024

| Purpose | Zeile | Notes |
|---|---|---|
| Beiträge zur Altersvorsorge (gesetzliche Rente, Rürup, berufsständische) | 4–10 | — |
| Beiträge zu sonstigen Vorsorgeaufwendungen | 11–48 | Full block |
| Kranken-/Pflegeversicherung Basisabsicherung (voll abziehbar) | 11–42 | GKV + PKV Basistarif-Anteil |
| Beiträge ohne Anspruch auf Krankengeld (Reduzierung) | 12, 15, 29, 32 | Sub-Zeilen |
| Beiträge zu Versicherungen gegen Arbeitslosigkeit | 44 | |
| Beiträge zu eigenständigen Erwerbs- und Berufsunfähigkeitsversicherungen | 45 | BU-Versicherung |
| **Beiträge für private Unfallversicherungen + private Haftpflichtversicherungen** | **46** | **CONFIRMED via ELSTER help** — Unfall + Privathaftpflicht (alt: KFZ-Haftpflicht, Tierhalter-Haftpflicht) share this Zeile |
| Beiträge zu Risikoversicherungen / Rentenversicherungen mit Kapitalwahlrecht / Kapitallebensversicherungen / Rentenversicherungen ohne Kapitalwahlrecht | 46–48 | Multi-Zeile block for Risikoversicherungen |
| Ergänzende Angaben zu den Vorsorgeaufwendungen | 49–55 | e.g., Nachweise, Arbeitgeberzuschuss |

> **Practical note:** For employees in GKV, the sonstige-Vorsorgeaufwendungen cap (1,900 €/yr) is almost always exhausted by KV + PV Basisabsicherung alone. Other entries in Zeilen 44–48 usually have no practical tax benefit.

---

## Anlage KAP — 2024

| Purpose | Zeile | Notes |
|---|---|---|
| Antrag auf Günstigerprüfung für sämtliche Kapitalerträge | 4 | Enter "1" if personal rate < 25 % |
| Antrag auf Überprüfung des Steuereinbehalts | 5 | |
| Erklärung zur Kirchensteuerpflicht / Sperrvermerk | 6 | Kirchensteuer auf KESt bei Sperrvermerk |
| **Kapitalerträge, die dem inländischen Steuerabzug unterlegen haben** (block) | **7–15** | From German brokers' Jahressteuerbescheinigung |
| Sparer-Pauschbetrag (in Anspruch genommen) | 16–17 | Report how much of 1,000/2,000 € allowance already used at source |
| **Kapitalerträge, die NICHT dem inländischen Steuerabzug unterlegen haben** (block) | **18–26a** | **Foreign broker income goes here** |
| — inländische Kapitalerträge ohne Steuerabzug / ausländische Erträge | 18 + 19 | Z.18 = domestic no-withhold (rare), Z.19 = foreign (Trading 212, DEGIRO, IBKR) |
| Erstattungszinsen vom Finanzamt | 26 | |
| Prozess- und/oder Verzugszinsen | 26a | |
| **Kapitalerträge, die der tariflichen Einkommensteuer unterliegen** (block — NOT Abgeltungssteuer) | **27–34** | Certain beteiligungs- or unternehmerische income |
| — Summe Hinzurechnungsbeträge (§ 10 AStG) | 27 | |
| — Laufende Kapitalerträge + Veräußerung sonstiger Kapitalforderungen / stille Gesellschaft / partiarische Darlehen | 28–29 | |
| — Kapitalerträge aus Lebensversicherungen nach 31.12.2004 | 30 | |
| — Kapitalerträge aus unternehmerischer Beteiligung an Kapitalgesellschaft (auf Antrag) | 31–32d | |
| — Gesellschaft bezeichnen | 32b | |
| — Widerrufserklärung | 32c–32d | |
| Kapitalerträge mit ermäßigter Besteuerung nach § 34 Abs. 1 EStG (Fünftelregelung) | 35 | Seltene Sonderfälle |
| Teileinkünfteverfahren + ermäßigt besteuerte Lebensversicherungen (100 % eintragen) | 36 | ELSTER rechnet Teilbesteuerung automatisch |
| **Anrechenbare Steuern** (block header) | **37–42** | KESt, Soli, KiSt, foreign WHT |
| Anrechnungsbeträge zu Erträgen in Zeilen 28–34 + Einnahmen aus anderen Einkunftsarten | 43–45 | |
| Beschränkung der Anrechenbarkeit KESt nach § 36a EStG / § 31 Abs. 3 InvStG | 46 | |
| Kürzungsbetrag nach § 11 AStG | 47–48 | |
| Steuerstundungsmodelle | 55 | § 15b EStG |

> **Corrections from old SKILL.md:**
> - Zeile 15 → use **Zeile 19** for ausländische Kapitalerträge ohne KESt
> - Zeile 41 → Anrechenbare Steuern sit in the **37–42 range as a block header**, with sub-Zeilen 43–45 for the Anrechnungsbeträge themselves. [UNVERIFIED exact sub-Zeile within 37–42 for foreign WHT alone — confirm in ELSTER]
> - Zeilen 22/23 are the right "without KESt" Verluste lines (Z.13 and Z.12 are within-KESt) — this is inferred from the 18–26a block structure; exact sub-Zeile split confirmed by Haufe commentary [UNVERIFIED against primary].

---

## Anlage KAP-INV — 2024

Für Investmenterträge aus Fonds ohne inländischen Steuerabzug (z.B. ausländisch verwahrte ETFs bei Trading 212, DEGIRO, IBKR).

| Purpose | Zeile | Notes |
|---|---|---|
| **Laufende Erträge aus Investmentanteilen** (block) | **4–13** | ELSTER help block header |
| — Ausschüttungen (Aktienfonds, Mischfonds, Immobilienfonds, sonstige Fonds) | **4–8** | **Corrected** — previously shown as 9–13 in old ref |
| — Vorabpauschalen (per Fondstyp) | **9–13** | **Corrected** |
| **Gewinne und Verluste aus Veräußerung von Investmentanteilen** (block) | **14–28** | ELSTER help block header |
| — Veräußerungsgewinne / -verluste (per Fondstyp) | 14, 17, 20, 23, 26 | Five sub-Zeilen, one per fund type |
| — Gewinne aus Veräußerung bestandsgeschützter Alt-Anteile | 15, 18, 21, 24, 27 | Altbestandsschutz vor 2009 (100 k € Freibetrag) |
| Zwischengewinne nach InvStG 2004 | 29 | Für Bestände vor InvStG-2018-Reform |
| **Ermittlung der Vorabpauschalen** (Berechnungsblock) | **30–45** | Eintragung, wenn keine Bescheinigung vom ausl. Kreditinstitut |
| **Ermittlung der Gewinne/Verluste aus Veräußerung** (Berechnungsblock) | **46–56** | |
| Während der Besitzzeit angesetzte Vorabpauschalen | 53 | Abzug bei Veräußerung zur Vermeidung Doppelbesteuerung |
| Gewinne aus Veräußerung bestandsgeschützter Alt-Anteile | 55 | |

> **Teilfreistellung** (30 % Aktien / 15 % Misch / 60 %/80 % Immobilien) applies automatically based on fund type declared. InvStG 2018 §20.

> **Previous ref error fixed:** old reference claimed Ausschüttungen at 9–13; the ELSTER help is explicit — Ausschüttungen are 4–8, Vorabpauschalen are 9–13. Anyone using the old mapping would have double-counted or miscategorised.

---

## Anlage Kind — 2024

One Anlage Kind per child.

| Purpose | Zeile | Notes |
|---|---|---|
| Angaben zu Kindern (Name, Geburtsdatum, IdNr, Wohnort) | 4–9 | General child-identification block |
| Familienkasse (Kindergeld-Auszahlende) | 7 | Specific Zeile within the 4–9 block |
| Kindschaftsverhältnis | 10–15 + 38–43 | Two separate blocks |
| Minderjährige Kinder / Volljährige Kinder | 16–25 | |
| Übernommene Kranken- und Pflegeversicherungsbeiträge | 26–37 | If paid for the child |
| Übertragung Kinderfreibetrag / Freibetrag für Betreuung/Erziehung/Ausbildungsbedarf | 38–43 | Bei getrennt lebenden Eltern |
| Übertragung Behinderten-Pauschbetrag des Kindes auf Eltern | 58–60, 62 | Verweis auf Anlage Außergewöhnliche Belastungen für Erläuterung |
| Übertragung behinderungsbedingte Fahrtkostenpauschale | 63–65 | |
| **Kinderbetreuungskosten** | **66–72** | 80 % der Kosten, max 4,800 € / Kind / Jahr (JStG 2024 raised from 2/3 × 4,000) |

> **Sub-Zeile for the child's IdNr** is within Zeile 4–9 but the exact sub-line is [UNVERIFIED] — previously assumed to be Zeile 4; could be Zeile 5 or 6. Confirm at filing time.

---

## Anlage SO — 2024 (Sonstige Einkünfte)

Primary source: ELSTER help (help_est_ufa_10_2024) + ELSTER Anwender Forum thread #383747 (retrieved 2026-04-18).

For crypto specifically, see also `.claude/skills/steuer-crypto/references/anlage-so-mapping-2024.md`.

| Purpose | Zeile | Notes |
|---|---|---|
| Wiederkehrende Bezüge (z.B. Zeitrenten, nachträgliche Einkünfte) | 4 | |
| Ausgleichsleistungen zur Vermeidung des Versorgungsausgleichs | 5 | |
| Unterhaltsleistungen (Empfänger) | 6 | Realsplitting-Empfänger |
| Werbungskosten (Sonstige Einkünfte) | 7 + 9 | Split across two Zeilen |
| §22 Nr. 3 EStG — Einkünfte aus Leistungen (block) | between 8 and 17 | **[UNVERIFIED exact Zeilen]** — ELSTER help doesn't list them individually but they sit between Werbungskosten Z.7/9 and Verlustabzug Z.18. Includes gelegentliche Vermittlungen, crypto-related Leistungen (staking, Simple Earn interest, airdrops with Leistung). Freigrenze 256 €/yr. |
| Verlustabzug bei Leistungen | 18 | Verlustvortrag aus Vorjahren (§22 Nr.3) |
| Abgeordnetenbezüge | 19–28 | |
| Steuerstundungsmodelle | 29 | §15b EStG |
| **Private Veräußerungsgeschäfte** (§23 EStG — block) | **30–62** | Complete §23 block |
| — **Grundstücke und grundstücksgleiche Rechte** | 30–40 | Real-estate holding-period sales (<10 years) |
| — **Virtuelle Währungen, sonstige Token und andere Wirtschaftsgüter** | 41–55 | **OFFICIAL 2024 block label** — crypto, NFTs, Gold, Kunst, other chattel (1-year holding) |
| — Verlustabzug zu privaten Veräußerungsgeschäften | 62 | Verlustvortrag §23 |

> **Crypto sub-Zeilen within 41–55** (ELSTER Anwender Forum #383747 confirmed):
> - Zeile 42 = "Kryptowährungen" (Art-des-Wirtschaftsguts marker)
> - Zeilen 43–46 = per-transaction (Bezeichnung, Anschaffungszeitpunkt, Veräußerungszeitpunkt, Erlöse/Kosten/Gewinn)
> - Zeilen 53–55 = Summenzeilen (Gewinne / Verluste / verbleibender Betrag nach Freigrenze) — [UNVERIFIED per-sub-line]
>
> **Key rule (§23 EStG for crypto):** holding period > 1 year → tax-free. Freigrenze (all §23 combined): **1,000 €/yr** since 2024 (was 600 € 2021–2023). If combined §23 net gain ≥ Freigrenze, the FULL amount is taxable at **personal marginal rate** (NOT Abgeltungssteuer).
>
> **Loss offset:** §23 losses only offset §23 gains (within-year); Verlustvortrag possible via Zeile 62; cannot offset §20 Kapitalerträge.

---

## Anlage Sonderausgaben — 2024 (NEW separate form in 2024)

| Purpose | Zeile | Notes |
|---|---|---|
| Kirchensteuer (gezahlt, abzgl. Erstattung) | 4 | |
| Zuwendungen (Spenden und Mitgliedsbeiträge) für steuerbegünstigte Zwecke | 5–12 | |
| — Allgemein steuerbegünstigte Zwecke (bis 20 % Einkünfte) | 5–6 | |
| — Politische Parteien (50 % Ermäßigung, max. 825 € / 1,650 €) | 7 | |
| — Unabhängige Wählervereinigungen | 8 | |
| — Spenden ins Stiftungsvermögen (bis 1–2 Mio. €) | 9 | Sonderregel |
| Berufsausbildungskosten (Erstausbildung, max 6,000 €/yr) | 13–14 | Nicht für Zweitausbildung (dort Werbungskosten) |
| Gezahlte Versorgungsleistungen (Renten, dauernde Lasten) | 15–28 | Bei Vermögensübertragung |
| Unterhaltsleistungen geschiedener Ehegatte (Realsplitting) | 29–32 | Max. 13,805 € + Kranken-/Pflegeversicherungsbeiträge |
| Schuldrechtlicher Versorgungsausgleich | 37–39 | |
| Ausgleichsleistungen zur Vermeidung des Versorgungsausgleichs | 40–41 | |

---

## Anlage Außergewöhnliche Belastungen — 2024 (NEW separate form in 2024)

| Purpose | Zeile | Notes |
|---|---|---|
| Behinderten-Pauschbetrag | 4–9 | Nach Grad der Behinderung (384–7,400 € per § 33b EStG) |
| Hinterbliebenen-Pauschbetrag | 10 | 370 €/yr |
| Pflege-Pauschbetrag | 11–18 | 600/1,100/1,800 € je Pflegegrad (Pflegegrad 2–5) |
| Behinderungsbedingte Fahrtkostenpauschale | 19–20 | 900 € oder 4,500 € je Grad der Behinderung + Merkzeichen |

> **Not covered in this ref but still applicable** (consult live form at filing): Krankheitskosten (mit Rezept/Verordnung), Bestattungskosten, Kurkosten, Pflegekosten, Behinderungsbedingte Umbaukosten. These are entered as "andere außergewöhnliche Belastungen" in a later block on the same Anlage.

> **Zumutbare Belastung** (tier progressively applied per §33 Abs. 3 EStG) reduces the deductible portion — ELSTER computes automatically.

---

## Anlage EÜR — 2024

Mandatory for all §4 Abs. 3 EStG profit determination. Not detailed here — the Kleinunternehmer-simplified workflow referenced in old SKILL.md is **no longer valid** for 2024. Anlage EÜR must be filed.

---

## Change Log vs. Prior Version

Reconciliation against the old `steuer-filing/SKILL.md` values (pre-audit):

| SKILL.md claim (TY 2024) | Verdict | Correct for 2024 |
|---|---|---|
| Hauptvordruck Zeile 38 (haushaltsnahe Dienstleistungen) | ❌ MOVED | Anlage Haushaltsnahe Aufwendungen Zeile 5 |
| Hauptvordruck Zeile 39 (Handwerkerleistungen) | ❌ MOVED | Anlage Haushaltsnahe Aufwendungen Zeile 6 |
| Anlage N Zeile 6 (Bruttoarbeitslohn) | ✅ CORRECT | 6 |
| Anlage N Zeile 11 (Entschädigung/Fünftel) | ❌ WRONG | 16–20 block |
| Anlage N Zeile 12–14 (Lohnsteuer/Soli/KiSt) | ❌ WRONG | Within Zeile 4–20 block (exact sub-Zeilen unverified) |
| Anlage N Zeile 45 (Homeoffice-Pauschale) | ❌ WRONG | 61–62 |
| Anlage N Zeile 46 (Weitere Werbungskosten) | ❌ WRONG | 64–67 range |
| Anlage KAP Zeile 15 (Ausländische Kapitalerträge) | ❌ WRONG | 19 (within 18–26a block) |
| Anlage KAP Zeile 17 (Sparer-Pauschbetrag) | ✅ CORRECT | 16–17 |
| Anlage KAP Zeile 37 (KESt) | ✅ CORRECT | 37 (block header 37–42) |
| Anlage KAP Zeile 41 (ausländische Steuern) | ⚠️ within 37–42 block | Anrechnungsbeträge sub-Zeilen 43–45 |
| Anlage KAP Zeile 13 (Aktienverluste) | Context-dependent | 13 = mit KESt, 23 = ohne KESt |
| Anlage KAP-INV Ausschüttungen at 9–13 | ❌ WRONG | Ausschüttungen = 4–8, Vorabpauschalen = 9–13 |
| Anlage Vorsorgeaufwand Haftpflicht at 46–48 | ✅ CORRECT | Zeile 46 primary (Unfall + Haftpflicht combined), 46–48 for Risikoversicherungen block |
| Anlage Kind Kinderbetreuungskosten at 66 | ~CORRECT | 66–72 block |
| Anlage SO "§23 andere Wirtschaftsgüter" at 41–55 | ✅ CONFIRMED | Official 2024 label: "Virtuelle Währungen, sonstige Token und andere Wirtschaftsgüter" |

---

## Sources

- **ELSTER help (primary, authoritative for Zeile-label extraction):** https://www.elster.de/eportal/helpGlobal?themaGlobal=help_est_ufa_10_2024 (retrieved 2026-04-18)
- **ELSTER Anwender Forum #383747 (Anlage SO Zeile 42 confirmation):** https://forum.elster.de/anwenderforum/forum/elster-webanwendungen/mein-elster/383747-anlage-so-zeilen-10-und-49 (retrieved 2026-04-18)
- **Form catalog:** Bundesfinanzministerium Formular-Management-System, https://www.formulare-bfinv.de/ (retrieved 2026-04-17)
- **Hauptvordruck ESt 1 A 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Hauptvordruck_ESt_1_A_steuern.de_01.pdf
- **Anlage N 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_N_steuern.de_01.pdf
- **Anlage KAP 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_KAP_steuern.de_01.pdf
- **Anlage SO 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_SO_steuern.de_01.pdf
- **Anlage Vorsorgeaufwand 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_Vorsorgeaufwand_steuern.de_01.pdf
- **Anlage Kind 2024 PDF mirror:** https://www.steuern.de/fileadmin/user_upload/Steuerformulare_2024/Anlage_Kind_steuern.de_01.pdf
- **Haufe 2024 Anlage-KAP commentary:** https://www.haufe.de/id/beitrag/14-anlage-kap-2024-fuer-einkuenfte-aus-kapitalvermoegen-147-kapitalertraege-die-nicht-dem-inlaendischen-steuerabzug-unterlegen-haben-HI16276374.html
- **Haufe 2024 Anlage-SO commentary (Zeilen 30–55):** https://www.haufe.de/id/beitrag/anlage-so-sonstige-einkuenfte-2024-43-private-veraeusserungsgeschaefte-spekulationsgeschaeft-zeilen3055-HI16702150.html
- **Haufe 2024 Anlage-Vorsorgeaufwand §3.8 (Haftpflicht Zeile 46):** https://www.haufe.de/id/beitrag/anlage-vorsorgeaufwand-vorsorgeaufwendungen-2024-38-berufs-erwerbsunfaehigkeits-unfall-haftpflicht-risikoversicherungen-zeilen4546-HI16702023.html
- **steuerrat24 Anlage Kind 2024 Ausfüllhilfe:** https://www.steuerrat24.de/steuererklaerung/steuererklaerung-2024/ausfuellhilfen-2024/3345-einkommensteuererklaerung-2024-anlage-kind.html
