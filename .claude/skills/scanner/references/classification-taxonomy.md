# Document Classification Taxonomy

This taxonomy defines all document categories and sub-types the scanner recognizes. For each sub-type: identifying signals, common providers, and what data to extract.

---

## Tax (Steuer)

Documents related to income tax filing, tax assessments, and tax authority correspondence.

### Lohnsteuerbescheinigung (Wage Tax Certificate)

**Signals:** Header contains "Lohnsteuerbescheinigung" or "Ausdruck der elektronischen Lohnsteuerbescheinigung". Numbered Zeilen (lines) with income and tax amounts. Employer name and Steuernummer in header.

**Common providers:** Any German employer. The employer name appears in the header.

**Extract:** Gross wages (Bruttoarbeitslohn), Lohnsteuer, Solidaritaetszuschlag, Kirchensteuer, social security contributions (RV, AV, KV, PV), tax class, period, employer name. See extraction-templates.md for full field list.

### Steuerbescheid (Tax Assessment Notice)

**Signals:** Header "Bescheid fuer [year] ueber Einkommensteuer" or similar. Issued by Finanzamt. Contains festgesetzte Einkommensteuer, zu versteuerndes Einkommen, Erstattung or Nachzahlung amount.

**Common providers:** Finanzamt (local tax office). The specific Finanzamt name and address appear in the header.

**Extract:** Tax year, assessed income tax, Solidaritaetszuschlag, Kirchensteuer, refund or additional payment amount, zvE (zu versteuerndes Einkommen), Finanzamt name and Steuernummer.

### Vorauszahlungsbescheid (Prepayment Assessment)

**Signals:** Header contains "Vorauszahlungsbescheid" or "Bescheid ueber Vorauszahlungen". Lists quarterly prepayment dates (10.03, 10.06, 10.09, 10.12) with amounts.

**Common providers:** Finanzamt.

**Extract:** Quarterly prepayment amounts, applicable period, Finanzamt name, Steuernummer.

### Steuererklaerung (Tax Return Copy)

**Signals:** ELSTER submission confirmation, "Einkommensteuererklaerung", form headers (Mantelbogen, Anlage N, Anlage V, etc.). May be a PDF printout of the filed return.

**Common providers:** User's own filing (ELSTER printout) or Steuerberater submission.

**Extract:** Tax year, which Anlagen were filed, key figures if visible. Primarily for reference — the Steuerbescheid is the authoritative document.

---

## Insurance (Versicherung)

Insurance policies, confirmations, premium notices, and annual statements.

### Haftpflicht (Personal Liability Insurance — Privathaftpflichtversicherung)

**Signals:** "Privathaftpflicht", "Haftpflichtversicherung", coverage descriptions mentioning Personen-/Sach-/Vermoegensschaeden. Policy document or Versicherungsschein.

**Common providers:** Allianz, HUK-COBURG, DEVK, CosmosDirekt, Adam Riese, Haftpflichtkasse.

**Extract:** Provider, policy number, annual premium, coverage amount, who is covered (single/family/partner), start date, special inclusions (Schluesselversicherung, Gefaelligkeitsschaeden, Auslandsschutz).

### BU (Disability Insurance — Berufsunfaehigkeitsversicherung)

**Signals:** "Berufsunfaehigkeit", "BU-Versicherung", "BU-Rente", monthly benefit amount, waiting periods (Karenzzeit).

**Common providers:** Allianz, Alte Leipziger, HDI, Swiss Life, Nuernberger, Hannoversche.

**Extract:** Provider, policy number, monthly BU-Rente, annual premium, coverage until age, Karenzzeit, abstract vs. concrete Verweisung, start date, Nachversicherungsgarantie.

### Rechtsschutz (Legal Protection Insurance)

**Signals:** "Rechtsschutzversicherung", coverage areas (Privat, Beruf, Verkehr, Wohnen), Selbstbeteiligung amount.

**Common providers:** ARAG, ROLAND, Allianz, DAS, DEVK, WGV.

**Extract:** Provider, policy number, annual premium, coverage areas, Selbstbeteiligung, who is covered, start date, waiting periods.

### Hausrat (Household Contents Insurance)

**Signals:** "Hausratversicherung", coverage per square meter, Versicherungssumme, mentions of Einbruchdiebstahl, Feuer, Leitungswasser.

**Common providers:** Allianz, HUK-COBURG, DEVK, CosmosDirekt, VHV.

**Extract:** Provider, policy number, annual premium, Versicherungssumme, apartment size (qm), covered risks, Fahrraddiebstahl included, Elementarschaeden included, start date.

### KFZ (Motor Vehicle Insurance — Kfz-Versicherung)

**Signals:** "Kfz-Versicherung", "Kraftfahrtversicherung", vehicle identification (Kennzeichen, FIN), Haftpflicht/Teilkasko/Vollkasko, Schadenfreiheitsklasse (SF-Klasse).

**Common providers:** HUK-COBURG, Allianz, DEVK, CosmosDirekt, AXA, VHV.

**Extract:** Provider, policy number, annual premium, vehicle (make/model/Kennzeichen), coverage type (Haftpflicht/TK/VK), SF-Klasse, Selbstbeteiligung TK/VK, start date.

### Krankenversicherung (Health Insurance)

**Signals:** "Krankenversicherung", GKV or PKV indicators, Beitragsbescheinigung, Zusatzbeitrag, Basisbeitrag.

**Common providers:** GKV: TK, AOK, Barmer, DAK, IKK. PKV: DKV, Allianz Private, Signal Iduna, Debeka, AXA.

**Extract:** Provider, GKV vs PKV, annual or monthly premium, Zusatzbeitrag rate (GKV), Basisbeitrag (PKV — tax-deductible portion), who is covered, Arbeitgeberzuschuss if shown.

### Zahnzusatz (Dental Supplementary Insurance)

**Signals:** "Zahnzusatzversicherung", "Zahnversicherung", coverage percentages for Zahnersatz/Zahnbehandlung/Kieferorthopaedie.

**Common providers:** DFV, Ergo Direkt, Allianz, Muenchener Verein, Die Bayerische, ottonova.

**Extract:** Provider, policy number, monthly premium, coverage levels (percentages), waiting periods, annual maximum benefit, start date.

### Unfall (Accident Insurance — Unfallversicherung)

**Signals:** "Unfallversicherung", Invaliditaetssumme, Grundsumme, Progression percentage.

**Common providers:** Allianz, DEVK, HUK-COBURG, InterRisk, Die Bayerische.

**Extract:** Provider, policy number, annual premium, Grundsumme, Progression, who is covered, Todesfallleistung, Krankenhaustagegeld, start date.

### Reise (Travel Insurance — Reiseversicherung)

**Signals:** "Reiseversicherung", "Auslandsreisekrankenversicherung", "Reiseruecktritt", worldwide or Europe coverage.

**Common providers:** ADAC, Allianz Travel, HanseMerkur, ERV, DKV.

**Extract:** Provider, policy number, annual premium, coverage type (Kranken/Ruecktritt/Gepaeck), coverage region, who is covered, maximum trip duration, start date.

### Risikoleben (Term Life Insurance — Risikolebensversicherung)

**Signals:** "Risikolebensversicherung", "Todesfallschutz", Versicherungssumme, Todesfallleistung, beneficiary.

**Common providers:** CosmosDirekt, Hannoversche, HUK-COBURG, Europa, Allianz.

**Extract:** Provider, policy number, annual premium, Versicherungssumme, coverage end date, beneficiary (Bezugsberechtigter), kreuzweise if couple, start date.

---

## Investment (Kapitalanlage)

Documents from brokers, banks, and fund companies about investments.

### Jahresabrechnung (Annual Broker/Bank Statement)

**Signals:** "Jahresabrechnung", "Jahresdepotauszug", "Jahressteuerbescheinigung" from a broker or bank. Lists positions, transactions, tax figures for the year.

**Common providers:** Trade Republic, Scalable Capital, ING, DKB, comdirect, Consorsbank, flatex.

**Extract:** Broker name, tax year, total portfolio value, realized gains/losses, dividends received, Vorabpauschale, Freistellungsauftrag usage, Kapitalertragsteuer paid. See extraction-templates.md for full field list.

### Depotauszug (Portfolio Statement)

**Signals:** "Depotauszug", "Depotbestand", "Vermoegensuebersicht". Lists current holdings with quantities and values at a point in time.

**Common providers:** Same as Jahresabrechnung.

**Extract:** Broker name, statement date, list of positions (ISIN, name, quantity, current value, purchase value if shown), total portfolio value.

### Ertraegnisaufstellung (Income/Earnings Statement)

**Signals:** "Ertraegnisaufstellung", "Steuerbescheinigung", lists dividends, interest, and capital gains with tax treatment.

**Common providers:** Same as Jahresabrechnung.

**Extract:** Broker name, period, total dividends, total interest, realized gains, taxes withheld (KESt, Soli, KiSt), Freistellungsauftrag amount used.

### Kaufabrechnung (Trade Confirmation — Purchase)

**Signals:** "Kaufabrechnung", "Wertpapierabrechnung", "Kauf", single transaction with ISIN, quantity, price, fees.

**Common providers:** Same as Jahresabrechnung.

**Extract:** Broker name, trade date, settlement date, ISIN, security name, quantity, price per unit, total amount, fees/commissions, exchange.

### Dividendenmitteilung (Dividend Notification)

**Signals:** "Dividendenabrechnung", "Ausschuettung", "Thesaurierung", single dividend payment with tax details.

**Common providers:** Same as Jahresabrechnung.

**Extract:** Broker name, payment date, ISIN, security name, gross dividend, Kapitalertragsteuer, Soli, net payment, Quellensteuer if foreign.

---

## Income (Einkommen)

Documents proving income received outside of investment accounts.

### Gehaltsabrechnung (Payslip)

**Signals:** "Gehaltsabrechnung", "Entgeltabrechnung", "Lohnabrechnung", monthly statement with Brutto/Netto, Steuer, Sozialversicherung breakdown.

**Common providers:** Any employer. Often generated by DATEV, SAP, Sage, or Personio.

**Extract:** Employer, month/year, Bruttolohn, Nettolohn, Lohnsteuer, Soli, KiSt, SV contributions, Sonderzahlungen, Ueberstunden.

### Honorarvertrag (Freelance/Consulting Contract)

**Signals:** "Honorarvertrag", "Werkvertrag", "Dienstvertrag", freelance rate, project description, no payroll deductions.

**Common providers:** Any client company.

**Extract:** Client name, contract period, Honorar amount, payment terms, project description, tax treatment (Umsatzsteuer?).

### Nebenkostenabrechnung (Utility/Service Charge Statement)

**Signals:** "Nebenkostenabrechnung", "Betriebskostenabrechnung", landlord letterhead, breakdown of Heizkosten, Wasser, Muellabfuhr, Hausmeister, etc. Nachzahlung or Guthaben.

**Common providers:** Landlord or property management (Hausverwaltung).

**Extract:** Property address, period, total Nebenkosten, breakdown by category, Nachzahlung or Guthaben amount, haushaltsnahe Dienstleistungen portion (tax-relevant!), Handwerkerleistungen portion.

---

## Official (Behoerden)

Government correspondence and official benefit notices.

### Finanzamt Correspondence

**Signals:** Finanzamt letterhead, Aktenzeichen or Steuernummer in header, official tone. May be requests for documents (Beleganforderung), reminders, or general correspondence.

**Common providers:** Local Finanzamt.

**Extract:** Finanzamt name, date, Steuernummer/Aktenzeichen, subject/purpose, any deadlines, any amounts mentioned.

### Kindergeld-Bescheid (Child Benefit Notice)

**Signals:** "Kindergeld", issued by Familienkasse, monthly benefit amount per child, Kindergeldnummer.

**Common providers:** Familienkasse (part of Bundesagentur fuer Arbeit).

**Extract:** Kindergeldnummer, monthly amount per child, number of children, effective date, Familienkasse office.

### Elterngeld-Bescheid (Parental Allowance Notice)

**Signals:** "Elterngeld", "Elterngeld Plus", "Basiselterngeld", monthly benefit amount, Bezugszeitraum (benefit period in Lebensmonate).

**Common providers:** Elterngeldstelle (varies by Bundesland).

**Extract:** Monthly Elterngeld amount, Bezugszeitraum (which Lebensmonate), Basiselterngeld vs. ElterngeldPlus, Partnerschaftsbonus if applicable, Bemessungsgrundlage.

---

## Banking (Bankdokumente)

Documents from banks about accounts, transactions, interest, and credit cards. Distinct from Investment documents — Banking documents relate to current accounts, savings accounts, and credit cards, not brokerage/depot activity.

### Kontoauszug (Bank Statement)

**Signals:** "Kontoauszug", "Kontonummer", IBAN, itemized transaction list with Soll/Haben columns, running balance column, sequential statement number (Auszug Nr. or Blatt Nr.).

**Common providers:** Deutsche Bank, ING, N26, DKB, Commerzbank, Sparkasse, comdirect.

**Extract:** Account IBAN, statement period, opening balance, closing balance, all transactions (date, Verwendungszweck/description, amount, debit/credit indicator) — then run the categorize-rollup-present-correct flow (see extraction-templates.md).

### Zinsbescheinigung (Interest Certificate)

**Signals:** "Zinsbescheinigung", "Jahressteuerbescheinigung" from a bank in a savings/current account context (not broker/depot), interest amounts labeled "Zinsertraege", KESt and Soli withheld, Freistellungsauftrag reference.

**Common providers:** Same as Kontoauszug.

**Distinguishing from broker Jahressteuerbescheinigung:** If the document shows only Zinsertraege (interest income) with no Depot/Wertpapier/ISIN data, classify as Banking > Zinsbescheinigung. If it shows Kapitalertraege from Wertpapiere or lists securities/positions, classify as Investment > Jahresabrechnung. Provider name alone is not sufficient — Deutsche Bank and ING can issue both types.

**Extract:** Year, total interest earned (Zinsertraege), interest rate if shown, tax withheld (Kapitalertragsteuer, Solidaritaetszuschlag), Freistellungsauftrag amount used.

### Kontoabschluss (Account Closing Statement / Rechnungsabschluss)

**Signals:** "Kontoabschluss", "Rechnungsabschluss", quarterly or annual cadence, shows account fees (Kontofuehrungsgebuehren) and any credited interest, formal settlement structure.

**Common providers:** Same as Kontoauszug.

**Extract:** Period, fees charged (Kontofuehrungsgebuehren), interest credited, closing balance.

### Tagesgeld-Auszug (Savings Account Statement)

**Signals:** "Tagesgeldkonto", "Sparkontoauszug", "Extra-Konto" (ING branding), interest rate prominently shown, balance history over the period.

**Common providers:** ING (Extra-Konto), DKB, Consorsbank, comdirect.

**Extract:** Account balance, applicable interest rate (%), interest earned in the statement period.

### Kreditkartenabrechnung (Credit Card Statement)

**Signals:** "Kreditkartenabrechnung", "Kreditkarten-Umsaetze", masked card number (last 4 digits), itemized transactions with merchant names and amounts, total charged (Gesamtbetrag), debit date to linked Girokonto.

**Common providers:** Deutsche Bank (Visa/Mastercard), ING (Visa), N26 (Mastercard), DKB (Visa).

**Extract:** Last 4 digits of card number, statement period, total charged, debit date, linked Girokonto IBAN if shown, all transactions — then run the categorize-rollup-present-correct flow (see extraction-templates.md).

---

## Unknown

Documents that could not be classified with any confidence.

**Signals:** No recognizable document type markers, unfamiliar provider, ambiguous content.

**Action:** Flag for user review. Present whatever signals were found and ask the user to classify manually. If the user provides a classification, store it as a correction for future learning.
