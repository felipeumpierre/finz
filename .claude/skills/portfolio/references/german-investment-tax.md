# German Investment Tax Reference

Comprehensive reference for German investment taxation (Abgeltungssteuer, InvStG 2018). All figures current as of tax year 2025/2026.

**Last verified:** 2026-04-17

Primary sources used for verification:
- Bundesfinanzministerium (BMF) — annual Basiszins-Schreiben: `https://www.bundesfinanzministerium.de`
- Gesetze im Internet — current EStG / InvStG text: `https://www.gesetze-im-internet.de/estg/__20.html`
- Jahressteuergesetz 2024 (BGBl. 2024 I Nr. 387, in force 2024-12-06): `https://www.recht.bund.de/bgbl/1/2024/387/regelungstext.pdf`

---

## Abgeltungssteuer (Flat Tax on Capital Income)

Capital income in Germany is taxed at a flat rate, separate from progressive income tax.

**Base rate:** 25.00%
**Solidaritaetszuschlag (Soli):** 5.5% of the tax = 1.375%
**Effective rate without church tax:** 25% + 1.375% = **26.375%**

**With Kirchensteuer (church tax):**
- Church tax rate 8% (Bayern, Baden-Wuerttemberg): effective rate = **27.819%**
- Church tax rate 9% (all other states): effective rate = **27.995%**

The church tax reduces the base: the formula accounts for church tax as a deductible expense within the capital income tax calculation. The exact formulas:

- 8% church tax: tax = income x 25% / (1 + 0.08 x 25%) x (1 + 5.5% + 8%) = 27.819%
- 9% church tax: tax = income x 25% / (1 + 0.09 x 25%) x (1 + 5.5% + 9%) = 27.995%

**What is taxed at Abgeltungssteuer:**
- Dividends (Dividenden)
- Interest (Zinsen)
- Capital gains from selling securities (Veraeusserungsgewinne)
- Vorabpauschale on accumulating funds
- Income from derivatives and certificates

**Guentigerpruefung (cheaper check):** If the taxpayer's personal marginal income tax rate is below 25%, they can apply for taxation at the personal rate instead (Anlage KAP, line 4). The Finanzamt checks automatically if you file.

---

## Sparerpauschbetrag (Saver's Allowance)

The tax-free allowance for capital income.

| Status | Allowance |
|--------|-----------|
| Single | **1,000 EUR** |
| Married filing jointly (Zusammenveranlagung) | **2,000 EUR** |

These amounts apply since **2023** (increased from the previous 801 EUR / 1,602 EUR).

**What the Sparerpauschbetrag covers:**
- Dividends
- Interest
- Realized capital gains
- Vorabpauschale
- All capital income types

**Freistellungsauftrag (exemption order):**
- Filed per broker/bank — instructs them not to withhold tax up to the specified amount
- The sum of ALL Freistellungsauftraege across all banks must NOT exceed the total allowance (1,000 / 2,000 EUR)
- Can be split across brokers in any proportion
- Can be changed during the year (takes effect from the date of change, but some brokers recalculate retroactively for the calendar year)
- If no Freistellungsauftrag is filed, the broker withholds tax from the first euro of capital income

**Optimization strategy:**
- Allocate more Freistellungsauftrag to the broker generating more taxable income (dividends, distributions)
- For accumulating ETFs, the Vorabpauschale is small — allocate less there
- Monitor usage during the year and redistribute if one broker's allocation is exhausted while another has headroom

**If the Sparerpauschbetrag is not fully used:**
- Consider realizing small capital gains to "use up" the allowance — those gains are tax-free
- This is especially valuable for long-held positions with embedded gains that will eventually be taxed

---

## Teilfreistellung (Partial Exemption) — InvStG 2018

Applies to **investment funds** (Investmentfonds) under the Investment Tax Reform Act 2018. Does NOT apply to individual stocks, bonds, or direct investments.

| Fund Type | Equity Allocation | Exemption Rate | Effective Tax Rate (no church tax) |
|-----------|-------------------|----------------|------------------------------------|
| Equity fund (Aktienfonds) | >50% stocks | **30%** | 26.375% x 0.70 = **18.4625%** |
| Mixed fund (Mischfonds) | 25-50% stocks | **15%** | 26.375% x 0.85 = **22.4188%** |
| Bond/other fund | <25% stocks | **0%** | **26.375%** (no exemption) |
| Real estate fund (domestic, Immobilienfonds) | n/a | **60%** | 26.375% x 0.40 = **10.55%** |
| Real estate fund (foreign, >50% foreign property) | n/a | **80%** | 26.375% x 0.20 = **5.275%** |

**What Teilfreistellung applies to:**
- Distributions (Ausschuettungen) from the fund
- Capital gains when selling fund shares (Veraeusserungsgewinne)
- Vorabpauschale

**What it does NOT apply to:**
- Individual stocks — no Teilfreistellung, full 26.375% on gains and dividends
- Individual bonds
- Direct real estate ownership
- Certificates and derivatives

**How to verify a fund's Teilfreistellung eligibility:**
- Check the fund prospectus or factsheet for the "Teilfreistellungssatz"
- The broker usually displays it in the securities details
- justETF and extraETF databases include this information
- UCITS equity ETFs tracking stock indices (MSCI World, S&P 500, etc.) virtually always qualify for the 30% rate

**Tax advantage of Teilfreistellung:**
- For every 1,000 EUR of gains on an equity ETF: tax = 184.63 EUR (vs 263.75 EUR on a stock)
- Saving per 1,000 EUR of gains: **79.13 EUR** (30% less tax)
- This compounds significantly over time for buy-and-hold investors

---

## Vorabpauschale (Advance Lump Sum Tax)

An annual tax prepayment on accumulating (thesaurierend) funds, ensuring the government collects some tax even when no distributions are made.

**Calculation:**

1. **Basisertrag** (base return) = Fund value on January 1 x Basiszins x 0.70
2. **Vorabpauschale** = min(Basisertrag, actual fund gain during the year)
3. If the fund had a loss during the year: Vorabpauschale = 0
4. Subtract any actual distributions made during the year
5. Apply Teilfreistellung to the Vorabpauschale
6. Tax the result at Abgeltungssteuer rate

**Basiszins (base interest rate):**

| Year | Basiszins | Source (BMF-Schreiben announcing the Bundesbank-calculated rate) |
|------|-----------|--------|
| 2023 | **2.55%** | BMF-Schreiben 04.01.2023 (Basiszins zum 02.01.2023) — confirmed via BMF archive and multiple corroborating sources (retrieved 2026-04-17). See `https://datenbank.nwb.de/Dokument/1007891/` |
| 2024 | **2.29%** | BMF-Schreiben 05.01.2024 (Basiszins zum 02.01.2024) — confirmed via 2025 BMF letter referencing prior-year value (retrieved 2026-04-17) |
| 2025 | **2.53%** | BMF-Schreiben 10.01.2025 (Basiszins zum 02.01.2025). `https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2025-01-10-basiszins-vorabpauschale-zum-2-1-2025.html` (retrieved 2026-04-17) |
| 2026 | **3.20%** | BMF-Schreiben 13.01.2026 (Basiszins zum 02.01.2026). `https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Investmentsteuer/2026-01-13-basiszins-berechnung-vorabpauschale.html` (retrieved 2026-04-17) |

Note: The Bundesbank calculates the Basiszins each January 2 from the term structure of federal securities with 15-year residual maturity and annual coupon (per §18 Abs. 4 InvStG). The BMF publishes it via Schreiben to the Länder finance ministries.

**Timing:**
- Vorabpauschale is deemed received on the first business day of the NEW year (e.g., January 2, 2026 for tax year 2025)
- The broker debits the tax from the cash account in January
- If insufficient cash, the broker may sell fund shares to cover

**Example calculation (equity ETF, 30% Teilfreistellung) — TY 2025:**
```
Fund value Jan 1, 2025:          50,000 EUR
Basiszins 2025:                   2.53%  (BMF-Schreiben 10.01.2025)
Basisertrag = 50,000 x 2.53% x 0.70 = 885.50 EUR
Actual fund gain 2025:           4,000 EUR
Vorabpauschale = min(885.50, 4,000) = 885.50 EUR
After Teilfreistellung (30%):    885.50 x 0.70 = 619.85 EUR
Tax (26.375%):                   619.85 x 26.375% = 163.48 EUR
```

**Foreign brokers:**
- Trading 212, DEGIRO, Interactive Brokers (IBKR), and other non-German brokers do NOT calculate or withhold Vorabpauschale
- The investor must calculate it themselves and declare it on **Anlage KAP-INV**
- Failure to declare is tax evasion (Steuerhinterziehung)

---

## Verlustverrechnung (Loss Offsetting)

**General rules:**
- Capital losses can offset capital gains within the same tax year
- Losses carry forward to future years (Verlustvortrag) if not fully used
- Losses do NOT expire

**Two separate loss pots (Verlusttoepfe):**

1. **Aktienverlusttopf** (stock loss pot): Losses from selling individual stocks can ONLY offset gains from selling individual stocks. They cannot offset ETF gains, dividends, or interest.

2. **Allgemeiner Verlusttopf** (general loss pot): Losses from selling ETFs, funds, bonds, and other instruments can offset ANY capital income (gains, dividends, interest).

This asymmetry makes individual stock losses less flexible than ETF losses.

**Loss limitation on certain instruments — REPEALED (status as of 2026-04-17):**

The two 20,000 EUR annual caps previously in §20 Abs. 6 Satz 5 and Satz 6 EStG have been **abolished** by the Jahressteuergesetz 2024 (JStG 2024, BGBl. 2024 I Nr. 387, in force 2024-12-06). Both §20 Abs. 6 Satz 5 EStG (Termingeschäfte cap) and Satz 6 (Forderungsausfälle / worthless-security cap) were struck.

- **Losses from derivatives (Termingeschäfte / §20 Abs. 2 Nr. 3 EStG):** no longer limited to 20,000 EUR/year. The separate loss-pot (gesonderter Verlustverrechnungskreis) was abolished. Such losses now offset all capital income under the general §20 Abs. 6 rules.
- **Losses from total loss of worthless securities / bad-debt write-off (Forderungsausfälle / Ausfallverluste):** no longer capped at 20,000 EUR/year.
- **Retroactive effect:** The abolition applies **to all open cases** (including years back to 2020, where the Einkommensteuerbescheid is not yet bestandskräftig). The BFH had already ruled the Termingeschäfte cap verfassungswidrig in its AdV-decision from June 2024 (Az. VIII B 113/23); the legislator followed up by repealing it.
- **Broker implementation:** Banks are required to implement the new offset logic in the Kapitalertragsteuerabzug by **1 January 2026**. For 2024 and 2025, any residual caps applied by the broker must be corrected in the Einkommensteuererklärung (Anlage KAP) and the Finanzamt processes the refund.

Sources (retrieved 2026-04-17):
- JStG 2024, BGBl. 2024 I Nr. 387: `https://www.recht.bund.de/bgbl/1/2024/387/regelungstext.pdf`
- Current §20 EStG text (without the 20,000 EUR caps): `https://www.gesetze-im-internet.de/estg/__20.html`
- Bayerisches Landesamt für Steuern, "Verlustverrechnungsbeschränkungen bei den Einkünften aus Kapitalvermögen"
- Flick Gocke Schaumburg, "Update zum JStG 2024" (2024)

**What is still in force under §20 Abs. 6 EStG:**
- Capital losses still cannot offset income from other Einkunftsarten (e.g., Arbeitslohn).
- The Aktienverlusttopf restriction (losses from individual stocks only offset gains from individual stocks, §20 Abs. 6 Satz 4 EStG) remains in force.

**Tax-loss harvesting (Verlustverrechnung) — actively recommended when:**
- Unrealized losses exist that can offset realized gains
- The Sparerpauschbetrag is already exhausted (otherwise gains are tax-free anyway)
- The position is one the investor wants to keep (sell and rebuy strategy)

**Germany has NO wash sale rule:**
- Unlike the US (30-day rule) or UK (bed and breakfast rule), Germany allows selling a security and immediately rebuying it
- The loss is fully recognized for tax purposes
- The new purchase resets the cost basis to the current (lower) price
- This is entirely legal and explicitly used in German tax planning

**Example:**
```
Position: 100 shares of ETF X, avg purchase price 80 EUR, current price 65 EUR
Unrealized loss: 100 x (65 - 80) = -1,500 EUR

Action: Sell all 100 shares at 65 EUR, immediately rebuy 100 shares at 65 EUR
Realized loss: -1,500 EUR
Tax savings: 1,500 x 26.375% = 395.63 EUR (or 1,500 x 18.4625% = 276.94 EUR with 30% TF)

New cost basis: 65 EUR per share (will pay more tax when eventually selling at a gain)
Net benefit: Time value of money — the tax savings now are worth more than the future tax cost
```

---

## Anlage KAP / KAP-INV — Foreign Broker Reporting

If any capital income was earned through a foreign broker that did NOT withhold German tax, the taxpayer MUST file Anlage KAP and/or Anlage KAP-INV.

**Brokers that do NOT withhold German Abgeltungssteuer:**
- Trading 212 (UK/Bulgaria)
- DEGIRO (Netherlands)
- Interactive Brokers (IBKR) (Ireland/UK/US)
- Swissquote, Saxo Bank, eToro, and other non-DE-domiciled brokers

**Brokers that DO withhold German Abgeltungssteuer:**
- Trade Republic
- Scalable Capital (Baader Bank)
- ING DiBa
- Comdirect / Commerzbank
- DKB
- Consorsbank
- Deutsche Bank / Maxblue
- All German Sparkassen and Volksbanken

**Key Anlage KAP lines for foreign broker income:**

| Line | Content |
|------|---------|
| **Line 7** | Check "yes" — capital income not yet taxed in Germany |
| **Line 19** | Total capital income from sources without German withholding (Kapitalertraege, die nicht dem inlaendischen Steuerabzug unterlegen haben) |
| **Line 22** | Losses realized at foreign brokers (Verluste aus Kapitalvermoegen) |
| **Line 23** | Stock sale losses specifically (Verluste aus der Veraeusserung von Aktien — for the Aktienverlusttopf) |
| **Line 41** | Foreign withholding tax paid, eligible for credit (anrechenbare auslaendische Steuern) — e.g., US dividend WHT |

**Anlage KAP-INV (for investment funds at foreign brokers):**
- Report Vorabpauschale that was NOT withheld by a German broker
- Report fund distributions received
- Report gains/losses from selling fund shares
- Include Teilfreistellung information

---

## Tax Calendar for Investment Income

| When | What | Action |
|------|------|--------|
| **January** | Vorabpauschale deducted | Check broker cash accounts. For foreign brokers: begin calculating Vorabpauschale for prior year |
| **March** | Annual tax certificates | German brokers issue Jahressteuerbescheinigung — review for accuracy |
| **March-May** | Filing season | File Anlage KAP / KAP-INV for foreign broker income |
| **Ongoing** | Freistellungsauftrag monitoring | Check if allowance is being used optimally, redistribute if needed |
| **November** | Year-end planning | Review unrealized gains/losses for tax-loss harvesting opportunities |
| **December 15** | Verlustbescheinigung deadline | Request loss certificate from brokers if you want to consolidate loss pots across brokers (Verlustbescheinigung beantragen). MUST be requested by Dec 15, otherwise losses stay with that broker |
| **December** | Tax-loss harvesting | Execute any planned loss realization before year-end. Also consider realizing small gains if Sparerpauschbetrag has headroom |
| **December 31** | Year-end | Last day for transactions to count for the current tax year (settlement date matters for some brokers) |

---

## Irish and Luxembourg ETF Domicile Preference

German investors generally prefer ETFs domiciled in **Ireland** or **Luxembourg** over US-domiciled ETFs:

**Why Ireland:**
- Ireland-US DBA (Double Taxation Agreement) reduces US dividend WHT from 30% to 15%
- This 15% is often fully credited against German tax (Anlage KAP line 41)
- UCITS-compliant, freely tradable in the EU
- Most large ETF providers (iShares, Vanguard) offer Irish-domiciled versions

**Why NOT US-domiciled ETFs (e.g., VTI, VOO, SPY):**
- 30% US WHT on dividends (only partially creditable in Germany, potentially 15% lost)
- Not UCITS-compliant — complex reporting requirements under InvStG
- May trigger "intransparente Fonds" punitive taxation if reporting requirements not met
- Estate tax risk: US-situs assets above $60,000 may be subject to US estate tax for non-US persons

**Luxembourg:**
- Also a popular domicile, similar DBA benefits
- Some ETF providers (DWS/Xtrackers, Amundi) prefer Luxembourg

---

## Special Topics

### Altbestandsschutz (Grandfathering for Pre-2009 Securities)

Securities purchased before January 1, 2009 are exempt from capital gains tax (Abgeltungssteuer) on gains. Since InvStG 2018 reform:
- Fund shares held since before 2009 received a fictitious sale/repurchase on January 1, 2018
- Gains accumulated until Dec 31, 2017 remain tax-free
- A personal allowance of **100,000 EUR** per person applies to these grandfathered gains
- Gains from January 1, 2018 onward are taxable under normal rules

### Crypto and Digital Assets

Since 2024 tax year:
- Crypto held > 1 year: tax-free (private sale exemption, Spekulationsfrist)
- Crypto held < 1 year: taxed at personal income tax rate (NOT Abgeltungssteuer)
- Reported on Anlage SO (Sonstige Einkuenfte), NOT Anlage KAP
- Freigrenze (not Freibetrag): 1,000 EUR/year — if exceeded, the ENTIRE gain is taxed

### Quellensteuer (Foreign Withholding Tax)

- Many countries withhold tax on dividends paid to foreign investors
- Common rates: US 15% (with W-8BEN), France 30% (often reduced), Switzerland 35%
- Creditable against German Abgeltungssteuer up to the DBA rate (usually 15%)
- Excess foreign WHT must be reclaimed from the source country
- Irish-domiciled ETFs handle this at the fund level (most efficient for German investors)
