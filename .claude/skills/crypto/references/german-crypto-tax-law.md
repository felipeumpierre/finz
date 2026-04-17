# German Crypto Tax Law — Reference

**Last verified:** 2026-04-17
**Tax year anchor:** 2025

## Authoritative sources

- **Einkommensteuergesetz (EStG) §22 Nr. 3** — Sonstige Einkünfte, Leistungen.
  <https://www.gesetze-im-internet.de/estg/__22.html> (retrieved 2026-04-17)
- **EStG §23** — Private Veräußerungsgeschäfte.
  <https://www.gesetze-im-internet.de/estg/__23.html> (retrieved 2026-04-17)
- **BMF-Schreiben 10.05.2022** — "Einzelfragen zur ertragsteuerrechtlichen Behandlung von virtuellen Währungen und von sonstigen Token" (IV C 1 - S 2256/19/10003 :001). First comprehensive federal crypto guidance.
- **BMF-Schreiben 06.03.2025** — "Einzelfragen zur ertragsteuerrechtlichen Behandlung bestimmter Kryptowerte" (IV C 1 - S 2256/00042/064/043). Replaces the 2022 letter; retains the substantive positions of 2022 and adds Mitwirkungs- und Aufzeichnungspflichten, rules for Steuerreports (Rz. 29b), Claiming (Rz. 13, 48a), and the use of sekundengenauen vs. tagesaktuellen Kursen (Rz. 43, 58, 91). Terminology switched from "virtuelle Währungen und sonstige Token" to "Kryptowerte".
  HTML announcement: <https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte.html>
  PDF: <https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte-bmf-schreiben.pdf> (retrieved 2026-04-17)
- **Abgabenordnung (AO) §153** — Berichtigung von Erklärungen.
  <https://www.gesetze-im-internet.de/ao_1977/__153.html> (retrieved 2026-04-17)
- **AO §371** — Selbstanzeige bei Steuerhinterziehung.
  <https://www.gesetze-im-internet.de/ao_1977/__371.html> (retrieved 2026-04-17)
- **AO §233a** — Verzinsung von Steuernachforderungen und -erstattungen.
  <https://www.gesetze-im-internet.de/ao_1977/__233a.html> (retrieved 2026-04-17)

## Tax rate — IMPORTANT

**Crypto gains are NOT subject to Abgeltungssteuer (26.375 % including Solidaritätszuschlag).**

Gains under §23 EStG (Private Veräußerungsgeschäfte) and income under §22 Nr. 3 EStG (Sonstige Einkünfte) are both **sonstige Einkünfte** — they flow into the taxpayer's regular zu versteuerndes Einkommen and are taxed at the **persönlicher Grenzsteuersatz** (personal marginal income-tax rate) per §32a EStG, between 14 % and 45 % (plus 5.5 % Solidaritätszuschlag on the tax amount once the Soli-Freigrenze is exceeded, plus any Kirchensteuer of 8 %/9 %).

Why: Abgeltungssteuer applies only to Kapitalerträge under §20 EStG (dividends, interest, fund distributions, stock disposals). Crypto is classified by BMF as "anderes Wirtschaftsgut" under §23 Abs. 1 Nr. 2 EStG, not §20. Therefore the Kapitalertragsteuer / Abgeltungssteuer regime — including the 1,000 EUR / 2,000 EUR Sparerpauschbetrag, the Freistellungsauftrag mechanism, and the 25 % flat rate — **does not apply to crypto**.

Practical consequence: a high earner in the 42 % bracket pays 42 % income tax + 2.31 % Soli + any Kirchensteuer on a taxable crypto gain; a low earner may pay significantly less. Estimating crypto tax by multiplying by 0.26375 is always wrong.

## §23 EStG — Private Veräußerungsgeschäfte

### Holding period

- **Standard: 1 year.** §23 Abs. 1 Nr. 2 Satz 1 EStG: "Veräußerungsgeschäfte bei anderen Wirtschaftsgütern, bei denen der Zeitraum zwischen Anschaffung und Veräußerung nicht mehr als ein Jahr beträgt." Disposal > 1 year after Anschaffung → not a Veräußerungsgeschäft under §23; tax-free in the private sphere.
- **No 10-year extension for lending/staking.** §23 Abs. 1 Nr. 2 Satz 4 EStG extends the holding period to 10 years for Wirtschaftsgüter "aus deren Nutzung als Einkunftsquelle zumindest in einem Kalenderjahr Einkünfte erzielt werden". The pre-2022 literature debated whether this 10-year clause could apply to crypto that was lent out or staked. **BMF 10.05.2022 definitively rejected that interpretation**: the clause does not apply to virtuelle Währungen used for lending or staking, so the 1-year holding period continues to apply. **BMF 06.03.2025 retains this position unchanged.** The 10-year extension is *not* part of current administrative law for crypto.
- **Clock continuity through Simple Earn / passive staking / lending:** the original Anschaffungszeitpunkt is preserved across Subscribe/Redeem operations that are not themselves realizations (BMF 06.03.2025, Simple Earn and claiming sections).

### Freigrenze

| Tax year | Freigrenze (§23 Abs. 3 Satz 5 EStG) |
|---|---|
| 2021–2023 | 600 EUR |
| 2024 and later | 1,000 EUR |

Current statute (§23 Abs. 3 Satz 5 EStG, as in force): "Gewinne bleiben steuerfrei, wenn der aus den privaten Veräußerungsgeschäften erzielte Gesamtgewinn im Kalenderjahr weniger als 1 000 Euro betragen hat."

**Freigrenze, not Freibetrag.** If the annual §23 Gesamtgewinn (summed across *all* §23 private disposals — crypto, gold, used-object flips, etc.) is `< 1,000 EUR`, the entire amount is tax-free. If it reaches or exceeds 1,000 EUR, the **full amount** becomes taxable from the first euro. There is no tapered allowance.

### Verlustverrechnung

§23 Abs. 3 Satz 7 EStG: "Verluste dürfen nur bis zur Höhe des Gewinns, den der Steuerpflichtige im gleichen Kalenderjahr aus privaten Veräußerungsgeschäften erzielt hat, ausgeglichen werden."

- §23-Verluste offset only §23-Gewinne of the same calendar year. They **cannot** be offset against Kapitalerträge (§20), against Arbeitslohn (§19), or against §22 Nr. 3 income.
- Satz 8 allows carryback (1 year) and carryforward (unlimited) under §10d EStG rules, but only within the §23-Verlustverrechnungskreis.
- A crypto loss cannot soak up stock dividends and vice versa. Separate loss pots.

## §22 Nr. 3 EStG — Sonstige Einkünfte (Leistungen)

Applies to **Staking-Rewards, Lending-Zinsen, Binance Simple Earn / Launchpool rewards, airdrops mit Leistung** (where the user performed some action to receive), and similar "Leistungen" that are not already covered by §23.

- **Recognition:** FMV in EUR at the time the asset is economically received (wirtschaftliche Verfügungsmacht). For passive staking where rewards are deemed claimed year-end under BMF 06.03.2025, the FMV at the deemed-receipt date applies.
- **Freigrenze: 256 EUR/year** across *all* §22 Nr. 3 income combined. If total < 256 EUR → tax-free. If ≥ 256 EUR → full amount taxable.
- **Cost basis:** the FMV at receipt becomes the Anschaffungskosten for the later §23 holding-period clock; a subsequent disposal within 1 year is a separate §23 event measured against that basis.
- **Verlustverrechnung:** §22 Nr. 3 Satz 3 EStG: losses only offset §22 Nr. 3 income of the same period; §10d carryback/carryforward available within that pot only. Cannot offset against §23 gains, Kapitalerträge, or Arbeitslohn.

## NFTs

Not explicitly addressed by BMF 10.05.2022 or BMF 06.03.2025. The BMF 06.03.2025 announcement states: "Nicht-fungible Token (NFT) und sogenanntes Liquidity Mining sind noch nicht Gegenstand des BMF-Schreibens." [BMF 06.03.2025 announcement, <https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte.html>]

Prevailing tax-literature position (not yet codified by BMF): NFTs that function as investment assets are treated analogously to other crypto under §23 EStG — 1-year holding period, 1,000 EUR Freigrenze, same Verlustverrechnungskreis. NFT-related revenue (e.g., royalties, sales by the creator) can be §22 Nr. 3 or — if professionally structured — §15 Gewerbebetrieb.

Practical stance: treat NFTs like other crypto under §23 until BMF publishes specific guidance. Flag as `[UNVERIFIED — no BMF position]` in any output that materially depends on NFT classification.

## Mining

BMF 10.05.2022 (retained by 06.03.2025) distinguishes:

- **Private Vermögensverwaltung / Liebhaberei:** occasional, small-scale mining with no profit-making intent. Rewards at FMV fall under §22 Nr. 3 (with 256 EUR Freigrenze).
- **Gewerblich (§15 EStG):** mining at scale, with professional hardware, intention to profit (Gewinnerzielungsabsicht), and participation in wirtschaftlicher Verkehr. Full Gewinnermittlung, Gewerbesteuer applies, and mining rewards become Betriebsvermögen (Anschaffungskosten = FMV at mining date; later disposal = Betriebseinnahme).

Indicators of Gewerblichkeit per BMF: dedicated mining rigs, electricity contracts optimised for mining, employment of staff, promotional activity, pool participation with commercial characteristics. The transition is fact-dependent; there is no bright-line EUR threshold in the BMF letter.

## DeFi

BMF 06.03.2025 supplements 2022 guidance on claiming and on Steuerreports but **does not yet codify** Liquidity Mining, wrapping, bridging, or LP-token mechanics. Current administrative guidance is fragmentary:

- **Liquidity pools (LP tokens):** unresolved whether depositing into an LP is a disposal of the underlying (triggering §23 if within 1 year) or a non-realizing deposit. Conservative default: treat as §23 disposal of the underlying with §23 re-acquisition when LP is redeemed.
- **Wrapping (e.g., ETH → wETH):** often treated as non-realizing by the literature when the wrapping is 1:1 and reversible, but unconfirmed by BMF. `[UNVERIFIED]`
- **Bridging between chains:** same uncertainty as wrapping.
- **DEX swaps (e.g., ETH → USDC on Uniswap):** clearly a §23 disposal of the sold token and acquisition of the received token, analogous to a CEX swap.

Flag DeFi transactions in output and ask the user whether they want the conservative (every mutation = disposal) or non-conservative (wrapping/bridging non-realizing) interpretation. Document the chosen position in the Nacherklärung letter if used.

## Record-keeping (Mitwirkungs- und Aufzeichnungspflichten)

BMF 06.03.2025 substantially expanded the Mitwirkungs- und Aufzeichnungspflichten section. The taxpayer must be able to reconstruct every transaction: quantity, date, Anschaffungs- and Veräußerungspreis, wallet, exchange, transaction hash where available. Steuerreports from third-party tools (Accointing, CoinTracking, Blockpit, etc.) are acceptable under §158 AO if the underlying methodology is transparent and the configuration is disclosed; the Finanzamt may request supporting screenshots and the raw exchange exports.

This is why the crypto skill stores all source CSVs and emits a reproducible `crypto-ledger.json` alongside the human summary — the pair is the contemporaneous record.

## Self-correction paths

| Law | When it applies | Effect | Citation |
|---|---|---|---|
| **§153 AO** | Taxpayer discovers after filing that a prior Erklärung was "unrichtig oder unvollständig" — *without* prior intent to hinterziehen | Must correct "unverzüglich" (without delay) before the Festsetzungsfrist expires. No criminal consequences when the original omission was not grossly negligent or intentional. | <https://www.gesetze-im-internet.de/ao_1977/__153.html> |
| **§371 AO** | Intentional Steuerhinterziehung (§370 AO) the taxpayer now wants to disclose | Immunity from criminal prosecution **only if the Selbstanzeige is complete** (Vollständigkeitsgebot): all unverjährten Steuerstraftaten derselben Steuerart, at minimum the last 10 Kalenderjahre, must be disclosed in full. Partial disclosures are void. | <https://www.gesetze-im-internet.de/ao_1977/__371.html> |

### §371 AO Sperrwirkung (immunity is lost if any of these hold before filing)

- A Prüfungsanordnung under §196 AO has been bekanntgegeben (limited to the announced scope).
- The Einleitung eines Straf- oder Bußgeldverfahrens has been bekanntgegeben.
- An Amtsträger has erschienen for audit or investigation.
- The Tat was bereits entdeckt (in whole or part) and the taxpayer knew or must have reasonably foreseen discovery.
- The hinterzogene Steuer per Tat exceeds **25,000 EUR** (then recourse is the §398a AO "Zuschlagslösung" — immunity against payment of graduated surcharge).
- A besonders schwerer Fall per §370 Abs. 3 AO exists (no immunity available at all via Selbstanzeige for these).

Practical rule for undeclared crypto: if the omission was grossly negligent or intentional, §371 AO (Selbstanzeige) is the correct path and completeness is non-negotiable. If the omission was a good-faith mistake (e.g., user did not understand that staking rewards were §22 Nr. 3 income), §153 AO applies and the risk is far lower. The two paths are mutually exclusive; the classification matters and should be discussed with a Steuerberater/Anwalt before filing.

## Nachzahlungszinsen — §233a AO

- **Karenzzeit:** interest begins 15 months after the end of the tax year in which the tax arose (§233a Abs. 2 Satz 1 AO). For 2023 tax assessments, interest begins 1 April 2025; for 2024, 1 April 2026.
- **Interest rate:** **0.15 % per month = 1.8 % per year** for interest periods from 1 January 2019 onward.
- **Legislative basis:** The Zweites Gesetz zur Änderung der Abgabenordnung und des EGAO (July 2022, BGBl. 2022 I Nr. 28 p. 1142) retroactively reduced the rate from 0.5 %/month to 0.15 %/month for periods from 2019, implementing the BVerfG ruling of 8 July 2021 (1 BvR 2237/14, 1 BvR 2422/17) that declared the prior 0.5 %/month rate unconstitutional from 2014 onward.
- BMF announcement: <https://www.bundesfinanzministerium.de/Content/DE/Pressemitteilungen/Finanzpolitik/2022/03/2022-03-30-zinssatz-fuer-nachzahlungen-und-erstattungen.html>

The legislator is required to review the rate every three years (§238 Abs. 1a AO). A 2025/2026 review may adjust the rate; verify current rate against the AO text if used for live calculations.

## Statute of limitations (Festsetzungsverjährung)

- **Regular:** 4 years (§169 Abs. 2 Nr. 2 AO), computed from the end of the Kalenderjahr in which the Steuererklärung was filed (§170 Abs. 2 AO).
- **Leichtfertige Steuerverkürzung:** 5 years.
- **Steuerhinterziehung:** 10 years (§169 Abs. 2 Satz 2 AO).

This means undeclared crypto from e.g. 2015 remains within reach of the Finanzamt if the omission was intentional, and §371 AO Selbstanzeige must cover the full 10-year window to achieve immunity.

## Cross-references

- FIFO methodology and per-wallet rule: `skills/crypto/references/fifo-methodology.md`
- Price source resolution: `skills/crypto/references/price-sources.md`
- Transaction classification rules: `skills/crypto/references/transaction-taxonomy.yaml`
- Anlage SO line mapping for filing: `skills/steuer-crypto/references/anlage-so-mapping.md`
- Nacherklärung template: `skills/steuer-crypto/references/nacherklaerung-template.md`
