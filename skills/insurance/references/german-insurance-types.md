# German Insurance Types — Comprehensive Reference

This file is the knowledge base for the insurance audit skill. It covers all 10 insurance types relevant to German residents and expats, with real numbers, provider names, and decision logic.

**Last verified:** 2026-04-17

Primary sources used for the Krankenversicherung (GKV) 2025 figures:
- Bundesministerium für Arbeit und Soziales (BMAS) — Sozialversicherungs-Rechengrößenverordnung 2025: `https://www.bmas.de/DE/Service/Gesetze-und-Gesetzesvorhaben/sozialversicherungs-rechengroessenverordnung-2025.html`
- Bundesministerium für Gesundheit (BMG) — Festlegung durchschnittlicher Zusatzbeitragssatz 2025 (announced 2024-11-07)

---

## 1. Krankenversicherung (Health Insurance)

### Overview
Health insurance is **mandatory** for all residents in Germany. Two systems exist:
- **GKV** (Gesetzliche Krankenversicherung) — statutory/public health insurance
- **PKV** (Private Krankenversicherung) — private health insurance

**Legal basis:** SGB V (Social Code Book V) for GKV; VVG (Insurance Contract Act) for PKV.

### Who Needs It
Everyone. No exceptions. If you live in Germany, you must have health insurance.

### GKV (Public) Details — values verified for 2025

- **Base contribution rate (allgemeiner Beitragssatz):** 14.6% of gross income, split 50/50 employer/employee (SGB V §241). Unchanged for 2025.
- **Durchschnittlicher Zusatzbeitragssatz 2025 (average supplementary contribution, BMG-festgesetzt):** **2.5%** (up from 1.7% in 2024). Also split 50/50 employer/employee since 2019 (GKV-VEG). Announced by BMG on 2024-11-07 per §242a SGB V. Individual Krankenkassen set their own Zusatzbeitrag; in practice the effective average collected in 2025 was higher (~2.9%), but 2.5% is the legal benchmark used for Familien-/Studentenversicherung and dependent contribution calculations.
- **Beitragsbemessungsgrenze Krankenversicherung (BBG GKV) 2025:** **66,150 EUR/year** (5,512.50 EUR/month). Harmonised federally (the previous West/Ost split no longer applies for KV — the KV BBG has always been federally uniform). Source: BMAS Sozialversicherungs-Rechengrößenverordnung 2025.
- **Versicherungspflichtgrenze / Jahresarbeitsentgeltgrenze (JAEG) 2025:** **73,800 EUR/year** (6,150 EUR/month). Employees with regular Arbeitsentgelt above this threshold for one full calendar year may opt out of GKV into PKV.
- **Familienversicherung:** Non-working spouse and children covered for free in GKV (§10 SGB V).
  - 2025 income limit for Familienversicherung: **535 EUR/month** (1/7 of the Bezugsgröße 2025 = 3,745 EUR/month), or **556 EUR/month** if the income is from a Minijob (Mindestlohn-linked Minijob grenze). Verify current Minijob-Grenze at BMAS before final advice.

**GKV-Höchstbeitrag (at BBG, 2025):**

| Component | Rate (employee share) | Monthly at BBG 5,512.50 EUR |
|---|---|---|
| Allgemeiner Beitrag (14.6% / 2) | 7.30% | 402.41 EUR |
| Durchschn. Zusatzbeitrag (2.5% / 2) | 1.25% | 68.91 EUR |
| **KV employee share total** | **8.55%** | **≈ 471.32 EUR/month** |

Add Pflegeversicherung (not GKV proper but bundled on the same Entgeltabrechnung): 3.4% base (plus 0.6% Kinderloszuschlag for childless over 23; less for multi-child parents under new 2023 reform). Employee share typically ~1.8% (Sachsen differs). At BBG that is roughly another 100 EUR/month on top of the KV number.

### PKV (Private) Details
- **Entry requirements:** Income above JAEG (employed) or self-employed (no income threshold)
- **Premium range:** EUR 250-1,200+/month depending on:
  - Age at entry (younger = cheaper)
  - Health status at application
  - Coverage level chosen
  - Deductible (Selbstbeteiligung) selected
- **Employer contribution (Arbeitgeberzuschuss, §257 SGB V):** 50% of the PKV premium, capped at the maximum employer share of GKV — for 2025 this cap is **≈ EUR 471/month** (5,512.50 EUR × 8.55%, using base 14.6% + durchschn. Zusatzbeitrag 2.5%, employer half). Pflegeversicherung employer share is added on top.
- **Age warning:** Premiums increase with age. After age 55, switching back to GKV is extremely difficult (essentially locked in)
- **Alterungsrueckstellungen:** PKV builds age provisions, but these are partially lost when switching insurers

### Cost Structure by Profile (2025 figures, KV employee share only — excludes Pflegeversicherung)
Calculation basis: 8.55% of gross (up to BBG 5,512.50 EUR/month) = 7.3% allg. Beitrag + 1.25% durchschn. Zusatzbeitrag (employee half of 14.6% + 2.5%).

| Profile | GKV Monthly (Employee Share, KV only) | PKV Monthly (Estimate) |
|---------|------------------------------|------------------------|
| Single, age 30, EUR 50k salary | ~EUR 356 | EUR 280-450 |
| Single, age 30, EUR 80k salary | **~EUR 471 (at BBG cap)** | EUR 280-450 |
| Single, age 45, EUR 90k salary | **~EUR 471 (at BBG cap)** | EUR 450-800 |
| Family, one income, EUR 80k | ~EUR 471 (at BBG cap; family free in GKV) | EUR 800-1,500+ (each person separate) |

Note: Pflegeversicherung employee share adds roughly +100 EUR/month at BBG (on top of the KV figures above). The previous version of this reference quoted ~EUR 563/month; that value was based on outdated Zusatzbeitrag 1.7% and old BBG — updated here against 2025 BMAS/BMG sources.

### Key Comparison: GKV vs PKV
| Factor | GKV | PKV |
|--------|-----|-----|
| Family coverage | Free Familienversicherung | Each person pays separately |
| Premium basis | Income-based | Risk-based (age, health) |
| Premium trend | Rises with salary | Rises with age and medical inflation |
| Benefits | Standardized, politically determined | Contractually fixed at sign-up |
| Waiting times | Longer for specialists | Usually shorter |
| Flexibility | Easy to switch insurers | Lose Alterungsrueckstellungen when switching |

### Tax Deductibility
- **Basisabsicherung (basic coverage):** Fully deductible as Vorsorgeaufwendungen under Section 10 EStG
  - This includes the basic health and long-term care insurance portion
  - Employee cap: EUR 1,900/year for sonstige Vorsorgeaufwendungen
  - Self-employed cap: EUR 2,800/year
  - In practice, health insurance premiums alone usually exhaust this cap
- **Zusatzversicherungen (supplementary):** Also deductible in theory, but cap is typically already exhausted

### Top Providers
- **GKV:** TK (Techniker Krankenkasse), HKK, IKK Classic, AOK (regional)
- **PKV:** DKV, Debeka, HanseMerkur, Allianz, Signal Iduna
- **Expat-friendly:** TK (English service), Feather (digital-first), Ottonova (digital PKV)

### Expat Considerations
- Most expats start in GKV through employment — this is usually the right choice
- PKV temptation: lower premiums when young and single, but dangerous trap if you plan to have a family in Germany
- If planning to leave Germany eventually, PKV might make sense (no family lock-in concern)
- GKV Familienversicherung is an enormous benefit for families — often worth EUR 400-800/month vs PKV

### Common Pitfalls
- Switching to PKV for short-term savings, then being locked in when family situation changes
- Not understanding that PKV premiums increase significantly with age
- Assuming PKV is "better" — GKV benefits are comprehensive and family coverage is free
- After age 55: virtually impossible to return to GKV even if income drops

---

## 2. Privathaftpflicht (Personal Liability Insurance)

### Overview
Covers damage you accidentally cause to others — property damage, personal injury, financial loss. Under BGB Section 823, you are personally liable with your ENTIRE wealth, unlimited.

**Legal basis:** BGB Section 823 — unlimited personal liability.

### Who Needs It
**Everyone.** This is the single most important insurance after health insurance. The cost-to-risk ratio is unmatched: EUR 3-5/month protects against potentially millions in liability.

### When Critical
- Always. There is no situation where a German resident should not have this.
- Especially important: if you rent (Schluesselverlust — lost keys can cost EUR 5,000-20,000 for lock replacement in apartment buildings), if you have children, if you cycle.

### Cost Structure
| Coverage | Single | Family (with children) |
|----------|--------|----------------------|
| Basic (EUR 5M) | EUR 30-40/year | EUR 45-60/year |
| Standard (EUR 10M) | EUR 35-50/year | EUR 50-70/year |
| Premium (EUR 50M+) | EUR 40-65/year | EUR 55-85/year |

The premium difference between EUR 5M and EUR 50M+ coverage is often only EUR 10-20/year. Always get the higher coverage.

### Coverage Tiers
- **Basic:** Third-party property damage, personal injury, Mietsachschaeden (rental property damage)
- **Standard:** + Schluesselverlust (lost keys), Gefaelligkeitsschaeden (favors gone wrong), worldwide coverage
- **Premium:** + deliktunfaehige Kinder (children under 7), Forderungsausfalldeckung (uninsured at-fault party), Allmaelichkeitsschaeden (gradual damage)

### Key Comparison Criteria
1. **Coverage amount:** Minimum EUR 10M, ideally EUR 50M+
2. **Schluesselverlust:** Must be included (lost apartment/building keys)
3. **Deliktunfaehige Kinder:** Covers damage by children under 7 (they are legally not liable, so without this, nobody pays)
4. **Worldwide validity:** Essential for expats who travel
5. **Mietsachschaeden:** Damage to rental apartment (standard in Germany where most people rent)
6. **Forderungsausfalldeckung:** Protects you if someone uninsured injures you

### Provider Landscape
- **Best value:** HUK-COBURG, Haftpflichtkasse Darmstadt, VHV
- **Expat-friendly (English, digital):** Feather, Getsafe, Lemonade
- **Premium traditional:** Allianz, AXA, Zurich

### Tax Deductibility
Technically deductible as sonstige Vorsorgeaufwendungen (other precautionary expenses). However, the EUR 1,900 cap for employees is almost always exhausted by health insurance contributions alone. **Practical tax benefit: EUR 0 for most employees.**

Self-employed with the EUR 2,800 cap might have marginal room, but at EUR 50-80/year premium, the tax saving would be negligible anyway.

### Expat Considerations
- Some policies exclude damage in your home country — check for worldwide coverage
- Digital-first providers (Feather, Getsafe) offer English contracts and support
- If you had liability insurance in your home country, it does NOT cover you in Germany

### Decision Factors
- Do you live in Germany? → Get Haftpflicht. Full stop.
- Single or family? → Family policy covers partner and children for ~EUR 15-20/year more
- Rent an apartment? → Ensure Schluesselverlust and Mietsachschaeden are included
- Have children under 7? → Get deliktunfaehige Kinder coverage

### Common Pitfalls
- Not having it at all (some expats assume their home country policy covers them)
- Choosing the cheapest policy without checking for Schluesselverlust coverage
- Not updating from single to family when partner or children arrive

---

## 3. Berufsunfaehigkeitsversicherung — BU (Disability Insurance)

### Overview
Protects your ability to earn income if you can no longer perform YOUR SPECIFIC profession due to illness or accident. This is the most important insurance for anyone whose lifestyle depends on their salary.

**Key statistic:** 1 in 3 German workers will experience a period of occupational disability before retirement. The most common causes are mental health (30%), musculoskeletal (20%), and cancer (15%).

### Who Needs It
- **Critical:** Anyone with a salary above EUR 40,000 who has financial obligations (rent, family, lifestyle)
- **Especially critical:** Single-income families, people with mortgages, high earners
- **Less critical:** People with substantial passive income or wealth that can replace their salary

### When Critical
- Family depends on your income
- You have a mortgage
- Your lifestyle requires your current income level
- You have no alternative income sources

### Statutory Fallback: Erwerbsminderungsrente (EM-Rente)
The statutory disability pension is woefully inadequate:
- **Average EM-Rente:** ~EUR 1,001/month (full reduction), ~EUR 560/month (partial)
- **Requirements:** At least 5 years of contributions, 3 of last 5 years employed
- **Covers only:** Complete inability to work ANY job (not your specific profession)
- **Gap example:** EUR 90,000 salary = ~EUR 4,500 net/month → EM-Rente ~EUR 1,001 → monthly gap of EUR 3,500

### Cost Structure
| Profile | Monthly Premium (EUR 2,000/mo benefit until 67) |
|---------|------------------------------------------------|
| Office worker, age 25 | EUR 35-50/month |
| Office worker, age 30 | EUR 40-60/month |
| Office worker, age 35 | EUR 55-80/month |
| Office worker, age 40 | EUR 75-120/month |
| Manual worker, age 30 | EUR 80-150/month |
| IT professional, age 30 | EUR 45-65/month |

**Rule of thumb:** Coverage should be 60-80% of net income. At minimum EUR 1,500/month benefit, ideally EUR 2,000-3,000/month.

### Coverage Tiers
- **Basic BU:** Covers your profession, standard contract terms
- **BU with Dienstunfaehigkeitsklausel:** For civil servants (Beamte) — aligned with their specific disability rules
- **BU-Zusatzversicherung:** Bundled with life insurance (often worse value — prefer standalone BU)

### Key Comparison Criteria (NON-NEGOTIABLE)
1. **No abstrakte Verweisung:** The insurer cannot reassign you to a different profession. If you're a software engineer who can't code anymore, they can't say "but you could work as a phone operator."
2. **Benefit until age 67:** Must align with retirement age. Policies ending at 60 or 63 leave a dangerous gap.
3. **Nachversicherungsgarantie:** Right to increase coverage without a new health check when life events occur (marriage, child, salary increase, home purchase).
4. **Leistung ab 50% BU:** Benefits start when you're 50% unable to perform your profession (not higher).
5. **No Arztanordnungsklausel:** Insurer can't force you to undergo specific treatments.
6. **Verzicht auf Umorganisation:** For self-employed — insurer can't demand you reorganize your business.

### Provider Landscape
- **Top-rated (Stiftung Warentest / Franke & Bornberg):** Alte Leipziger, HDI, Hannoversche, LV1871, Nurnberger, Europa, DBV
- **Good value:** Europa, Hannoversche (direct insurers, no broker commission = lower premiums)
- **Expat-friendly:** Work with an independent broker (Versicherungsmakler) who handles English communication

### Tax Deductibility
- **Premiums:** Deductible as sonstige Vorsorgeaufwendungen under Section 10 EStG
  - BUT: the cap (EUR 1,900 for employees, EUR 2,800 for self-employed) is almost always already exhausted by health insurance contributions
  - **Practical tax benefit for most employees: EUR 0**
- **Benefits received:** Taxed at the Ertragsanteil, typically 17-18% of the benefit is taxable
  - Example: EUR 2,000/month BU benefit → ~EUR 350/month taxable → at 30% marginal rate = ~EUR 105/month tax

### Expat Considerations
- Apply as early as possible — premiums are locked based on entry age and health
- Use **anonyme Risikovoranfrage** (anonymous pre-inquiry): A broker submits your health profile anonymously to multiple insurers to see who would accept you and at what terms, WITHOUT triggering a rejection that goes on your record
- Pre-existing conditions are a major factor — be 100% honest on the application (Gesundheitsfragen). Lies can void the entire policy retroactively.
- If you plan to leave Germany: check if the policy remains valid abroad (most do, but verify)

### Decision Tree
1. Does your lifestyle depend on your salary? → YES → Get BU
2. Do you have dependents? → YES → BU is CRITICAL
3. Can you afford EUR 50-80/month? → YES → Get standalone BU
4. Pre-existing conditions making BU expensive? → Consider Erwerbsunfaehigkeitsversicherung (cheaper, but covers less) or Grundfaehigkeitsversicherung (basic abilities insurance)
5. Risky profession making BU unaffordable? → Unfallversicherung as partial fallback

### Common Pitfalls
- Waiting too long to apply (premiums increase with age, health conditions accumulate)
- Choosing a policy with abstrakte Verweisung (allows reassignment to other jobs)
- Benefit period ending before retirement age (ensure coverage until 67)
- Not using anonyme Risikovoranfrage and getting a rejection on record
- Bundling BU with life insurance (less flexible, often worse value)
- Under-insuring: EUR 500/month coverage is nearly useless for a EUR 90,000 salary

---

## 4. Rechtsschutzversicherung (Legal Protection Insurance)

### Overview
Covers legal costs — lawyer fees, court fees, expert witnesses — for disputes in covered areas. Modular structure lets you pick which areas to cover.

### Who Needs It
- **Highly recommended for expats:** Employment disputes (Arbeitsrecht) are common, especially during probation or restructuring. German labor courts are employee-friendly, but only if you can afford to go.
- **Renters:** Landlord disputes are common in tight housing markets (Berlin, Munich)
- **Car owners:** Traffic law disputes after accidents

### When Critical
- Expat in a new job (employment law disputes)
- Renting in a competitive market (landlord conflicts)
- Any situation where you might need a lawyer but wouldn't want to pay EUR 3,000-10,000+ out of pocket

### Cost Structure
| Module | Annual Premium |
|--------|---------------|
| Privat (personal) only | EUR 150-250/year |
| Privat + Beruf (employment) | EUR 200-350/year |
| Privat + Beruf + Verkehr (traffic) | EUR 280-450/year |
| Privat + Beruf + Wohnen (housing) | EUR 300-500/year |
| All four modules (full coverage) | EUR 350-680/year |

### Key Comparison Criteria
1. **Waiting period (Wartezeit):** Typically 3 months for most disputes. Employment and housing disputes usually have 3-month waiting periods. Traffic has no waiting period.
2. **Coverage scope:** Check that Arbeitsrecht (employment law) is included — this is the most valuable module for expats
3. **Self-contribution (Selbstbeteiligung):** EUR 150-300 per case. Higher deductible = lower premium
4. **Mediation coverage:** Modern policies include mediation costs as alternative to court
5. **Phone consultation:** Free initial lawyer consultations included in most premium policies

### Modules Explained
- **Privat:** Contract disputes, consumer rights, data protection, neighbor conflicts
- **Beruf (Employment):** Termination protection (Kuendigungsschutz), salary disputes, workplace discrimination, Zeugnis (reference letter) disputes
- **Verkehr (Traffic):** Accidents, traffic violations, disputes with other drivers or insurers
- **Wohnen (Housing):** Landlord disputes (Nebenkostenabrechnung, deposit return, Mietpreisbremse), neighbor noise

### Provider Landscape
- **Top-rated:** ARAG, DAS, Advocard (part of Generali), Roland
- **Good value:** WGV, Deurag
- **Expat-friendly:** ARAG (English support available), Feather

### Tax Deductibility
- **Beruf (employment) portion:** Deductible as Werbungskosten (work-related expenses)
  - The Beruf module typically represents 40-60% of the total premium
  - If your policy costs EUR 400/year and Beruf is ~50%, you can deduct EUR 200 as Werbungskosten
  - At 35% marginal tax rate: saves ~EUR 70/year
- **Other modules (Privat, Wohnen, Verkehr):** NOT deductible (private expense)
- **Practical approach:** Ask your insurer for a written breakdown of the Beruf portion, or estimate 50%

### Expat Considerations
- Employment law disputes are the #1 reason expats need this insurance
- 3-month waiting period means: get it BEFORE you need it (ideally when starting a new job)
- German labor courts (Arbeitsgericht): in the first instance, each party pays their own lawyer regardless of outcome — Rechtsschutz ensures you can actually exercise your rights
- Alternative for housing only: Mieterverein (tenant association) membership EUR 60-100/year covers legal advice and representation for rental disputes

### Decision Tree
1. Are you an expat employee? → Strongly recommended (especially Beruf module)
2. Do you rent? → Add Wohnen module, or join a Mieterverein as cheaper alternative
3. Do you drive? → Add Verkehr module
4. Budget tight? → Beruf module alone (most valuable for expats, ~EUR 100-150/year standalone)

### Common Pitfalls
- Not respecting the 3-month waiting period (trying to claim for a dispute that started before coverage)
- Forgetting to add the Beruf module (the most valuable part for employees)
- Not requesting insurer pre-approval (Deckungszusage) before engaging a lawyer
- Expecting it to cover already-known disputes at sign-up

---

## 5. Hausratversicherung (Household Contents Insurance)

### Overview
Covers your belongings (furniture, electronics, clothing, valuables) against fire, water damage, burglary, storm, and optionally natural disasters (Elementarschaeden).

### Who Needs It
- **Recommended:** Anyone with household contents worth more than a few thousand euros
- **Especially important:** If you own expensive electronics, musical instruments, bicycles, or art
- **Less important:** If you live minimally and could replace everything for under EUR 2,000-3,000

### When Critical
- Valuable household contents (electronics, furniture, jewelry)
- Living in a flood or storm-prone area (add Elementarschaeden)
- Expensive bicycle (often covered under Hausrat, sometimes needs separate add-on)

### Cost Structure
| Apartment Size | Annual Premium (Standard) | Annual Premium (Premium) |
|----------------|--------------------------|--------------------------|
| 30-50 sqm | EUR 50-100/year | EUR 80-160/year |
| 50-80 sqm | EUR 80-150/year | EUR 120-220/year |
| 80-120 sqm | EUR 120-200/year | EUR 170-300/year |
| 120+ sqm | EUR 160-250/year | EUR 230-400/year |

**Calculation basis:** Typically EUR 650 per square meter of living space, or individual valuation.

### Key Comparison Criteria
1. **Unterversicherungsverzicht:** Insurer waives the right to reduce payouts if your actual contents exceed the insured amount. Essential clause.
2. **Elementarschaeden:** Covers natural disasters (flooding, earthquakes, landslides). Increasingly important due to climate change. Adds EUR 20-80/year.
3. **Fahrraddiebstahl:** Bicycle theft coverage — often limited to 1-2% of insured sum, or available as add-on
4. **Ueberspannungsschaeden:** Power surge damage (lightning strike frying your electronics)
5. **Glasbruch:** Glass breakage — often a separate add-on, worth it if you have expensive glass elements
6. **Wertsachen limit:** Standard policies cap valuables (jewelry, art, cash) at 20-30% of insured sum

### Provider Landscape
- **Top-rated:** HUK-COBURG, Ammerlaender, VHV, Lemonade
- **Expat-friendly:** Feather, Getsafe, Lemonade (all English, digital)
- **Budget:** Friday, Cosmos Direkt

### Tax Deductibility
- **Generally NOT deductible** — considered a private expense
- **Exception:** If you have a home office (Arbeitszimmer) that qualifies as your primary workspace, you can deduct the proportional share
  - Example: 15 sqm office in 80 sqm apartment = 18.75% of the premium is deductible as Werbungskosten
  - At EUR 150/year premium: EUR 28 deductible → saves ~EUR 10/year tax
- **Practical impact:** Negligible for most people

### Expat Considerations
- If you're renting furnished: you still need Hausrat for YOUR belongings (landlord's furniture is not your responsibility and not covered)
- Some expat packages from employers include temporary Hausrat — check before buying your own
- Digital providers offer month-to-month contracts (no long-term commitment)

### Decision Tree
1. Are your household contents worth more than EUR 5,000? → Consider Hausrat
2. Worth more than EUR 15,000? → Definitely get it
3. Do you have expensive electronics/bicycle/instruments? → Get it
4. Living in flood-prone area? → Add Elementarschaeden
5. Living minimally in a furnished rental? → Probably skip it or get basic coverage

### Common Pitfalls
- Not having Unterversicherungsverzicht — if you're underinsured, payouts are proportionally reduced
- Forgetting to add Elementarschaeden (flooding is the most expensive household claim type)
- Not updating coverage when you accumulate more valuable items
- Assuming the landlord's insurance covers your belongings (it doesn't)

---

## 6. Risikolebensversicherung (Term Life Insurance)

### Overview
Pays a lump sum to your beneficiaries if you die during the policy term. Pure risk coverage — no savings component, no cash value. This is what you want (NOT Kapitallebensversicherung).

### Who Needs It
- **Critical:** Families with children where one parent is the primary earner
- **Critical:** Anyone with a mortgage (covers remaining debt)
- **Not needed:** Single with no dependents, dual-income couple with no debt, retirees

### When Critical
- You have children
- Your partner depends on your income
- You have a mortgage
- You have dependents living abroad (parents, siblings)

### Cost Structure
| Profile | Monthly Premium (EUR 200,000 coverage, 20-year term) |
|---------|------------------------------------------------------|
| Non-smoker, age 25 | EUR 6-10/month |
| Non-smoker, age 30 | EUR 8-14/month |
| Non-smoker, age 35 | EUR 10-20/month |
| Non-smoker, age 40 | EUR 15-30/month |
| Non-smoker, age 45 | EUR 25-50/month |
| Smoker, age 35 | EUR 25-45/month |

**Coverage amount rule of thumb:** 3-5x gross annual salary, or outstanding mortgage amount, whichever is higher.

### Key Comparison Criteria
1. **Coverage amount:** Match to actual need (salary replacement + debt coverage)
2. **Term length:** Until youngest child is financially independent (~age 25) or mortgage is paid off
3. **Nachversicherungsgarantie:** Right to increase coverage without new health check at life events
4. **Vorgezogene Todesfallleistung:** Advance payout if diagnosed with terminal illness
5. **Ueberkreuz-Versicherung (cross-life):** Partners insure each other instead of themselves — avoids Erbschaftsteuer (inheritance tax) on the payout

### Provider Landscape
- **Best value (direct insurers):** CosmosDirekt, Europa, Hannoversche, HUK-COBURG
- **Traditional:** Allianz, AXA, Zurich
- **Comparison:** Check24, Verivox for quick comparison

### Tax Deductibility
- **Premiums:** Technically deductible as sonstige Vorsorgeaufwendungen
  - BUT: cap (EUR 1,900 employees / EUR 2,800 self-employed) is almost always already exhausted by health insurance
  - **Practical tax benefit: EUR 0 for most people**
- **Payout:** Generally tax-free for the beneficiary
  - **Exception:** If the policyholder and the insured person are different AND the beneficiary is a third party, Erbschaftsteuer may apply
  - **Ueberkreuz tip:** Partners insure each other → payout is from a contract the survivor owns → no inheritance tax issue

### Expat Considerations
- If you have dependents in your home country who rely on remittances, term life is critical
- Ueberkreuz-Versicherung is especially valuable for expat couples (avoids German inheritance tax complications)
- Check if the policy pays out worldwide (most do, but verify)
- If you plan to leave Germany: policy typically remains valid, but check terms

### Decision Tree
1. Do you have children? → Get term life insurance
2. Does your partner depend on your income? → Get term life insurance
3. Do you have a mortgage? → Get term life insurance (coverage = outstanding mortgage)
4. Single, no dependents, no debt? → You don't need this
5. Dual income, no kids, no mortgage? → Probably don't need this yet. Revisit when life changes.

### Common Pitfalls
- Getting Kapitallebensversicherung instead of Risikolebensversicherung (the savings component is terrible value)
- Under-insuring: EUR 50,000 coverage when you earn EUR 90,000/year barely covers one year
- Not doing Ueberkreuz-Versicherung and creating a tax liability for the beneficiary
- Forgetting to update beneficiaries after life changes (divorce, new child)

---

## 7. Zahnzusatzversicherung (Supplementary Dental Insurance)

### Overview
Supplements GKV dental coverage. GKV covers basic dental care but pays only 60-75% of Regelversorgung (standard treatment) for crowns, bridges. It covers ZERO for implants, premium ceramics, or orthodontics (for adults).

### Who Needs It
- **Recommended:** Anyone in GKV over age 30 (dental work becomes more likely)
- **Optional:** Under age 30 with good dental health
- **Not needed:** PKV members (private insurance usually includes comprehensive dental)

### When Critical
- You're in GKV and expect significant dental work in the future
- You want implants instead of bridges (implants cost EUR 1,500-3,500 per tooth, GKV pays EUR 0)
- You're over 35 and haven't had major dental work yet (statistically, it's coming)

### Cost Structure
| Age at Entry | Monthly Premium (Good Coverage) |
|-------------|--------------------------------|
| Under 25 | EUR 8-15/month |
| 25-30 | EUR 12-22/month |
| 30-40 | EUR 18-35/month |
| 40-50 | EUR 28-50/month |
| 50+ | EUR 40-65/month |

**Important:** Most policies have benefit caps in the first 1-4 years (Zahnstaffel):
- Year 1: EUR 500-1,000 max
- Year 2: EUR 1,000-2,000 max
- Year 3: EUR 2,000-3,000 max
- Year 4: EUR 3,000-4,000 max
- Year 5+: Full coverage (often 80-100% of actual costs)

### Key Comparison Criteria
1. **Implant coverage:** The main reason to get dental insurance. Look for 70-90% coverage
2. **Zahnstaffel (benefit caps in early years):** Lower caps in early years = cheaper premium but less useful if you need work soon
3. **No waiting period (Wartezeit):** Some policies have 8-month waiting period. Premium policies waive this.
4. **Stiftung Warentest rating:** Use their annual dental insurance test as a benchmark
5. **Inlay/Onlay coverage:** Ceramic inlays cost EUR 400-800 each
6. **Professional dental cleaning (PZR):** Some policies cover 1-2 cleanings per year (EUR 80-120 value)

### Provider Landscape
- **Top-rated (Stiftung Warentest):** DFV (Deutsche Familienversicherung), Hallesche, Alte Oldenburger, Wuerttembergische, Bayerische
- **Good value:** ERGO Direkt, Muenchener Verein
- **Expat-friendly:** Feather (English, digital), Ottonova

### Tax Deductibility
- Deductible as sonstige Vorsorgeaufwendungen under Section 10 EStG
- **Practical impact: EUR 0** — the EUR 1,900 employee cap is exhausted by health insurance
- Self-employed might have marginal benefit under the EUR 2,800 cap

### Expat Considerations
- If you come from a country with poor dental care access, getting dental insurance early is smart
- Bonusheft (bonus booklet): GKV increases its payment percentage if you've had regular check-ups. Visit the dentist annually and get it stamped — this works alongside dental insurance
- Some policies exclude pre-existing conditions or ongoing treatments — apply BEFORE you start treatment

### Decision Tree
1. Are you in GKV? → Consider dental insurance (PKV usually covers dental well)
2. Over 30? → More valuable as dental work likelihood increases
3. Need implants? → Dental insurance is almost certainly worth it (single implant = EUR 2,000-3,500)
4. Under 25 with healthy teeth? → Optional, but locking in a low premium now has long-term value
5. Already have significant dental issues? → Harder to get coverage, and existing conditions are excluded

### Common Pitfalls
- Applying after dental problems are already diagnosed (pre-existing conditions excluded)
- Not understanding the Zahnstaffel caps in early years
- Choosing based on premium alone without checking implant coverage percentage
- Forgetting to maintain the Bonusheft for GKV base coverage increase

---

## 8. Unfallversicherung (Accident Insurance)

### Overview
Pays a lump sum or monthly pension if you suffer a permanent disability from an accident. Covers you 24/7 worldwide — unlike statutory accident insurance (gesetzliche Unfallversicherung) which only covers work-related and commute accidents.

### Who Needs It
- **Recommended:** People with risky hobbies (cycling, skiing, climbing, motorsport)
- **Fallback option:** When BU is too expensive or unavailable due to health pre-conditions
- **Supplement:** Doesn't replace BU (BU covers illness too, Unfall only covers accidents)
- **Less important:** If you already have comprehensive BU coverage

### When Critical
- You have risky hobbies or lifestyle
- BU is unavailable or unaffordable for you
- You want additional coverage on top of BU for accident-specific scenarios

### Cost Structure
| Coverage | Monthly Premium |
|----------|----------------|
| Basic (EUR 100,000 Invaliditaetssumme) | EUR 7-12/month |
| Standard (EUR 200,000 + 225% Progression) | EUR 12-18/month |
| Premium (EUR 300,000 + 350% Progression) | EUR 17-25/month |

**Progression explained:** At 100% disability, you receive the full sum multiplied by the progression factor. At 225% progression with EUR 200,000 base: 100% disability = EUR 450,000 payout. Lower disability percentages receive proportionally less with progression amplifying higher percentages.

### Key Comparison Criteria
1. **Invaliditaetssumme:** Base payout amount. Minimum EUR 150,000 recommended.
2. **Progression level:** 225% minimum, 350-500% is better. This is what makes payouts meaningful for severe injuries.
3. **Gliedertaxe:** The table defining what percentage of disability each injury represents. Compare across providers — they vary significantly.
4. **Mitwirkung (pre-existing conditions):** Some insurers reduce payouts if pre-existing conditions contributed. Look for "Mitwirkung ab 50%" (only reduces if pre-existing conditions contributed more than 50%).
5. **Unfallrente:** Optional monthly pension instead of/in addition to lump sum — useful as BU fallback.

### Provider Landscape
- **Top-rated:** Interrisk, NV, VHV, Die Bayerische, Janitos
- **Good value:** CosmosDirekt, Helvetia
- **Expat-friendly:** Feather, Getsafe

### Tax Deductibility
- Deductible as sonstige Vorsorgeaufwendungen
- **Practical impact: EUR 0** — cap exhausted by health insurance for most employees
- If the policy includes an Unfallrente, benefits may be partially taxable

### Expat Considerations
- Worldwide 24/7 coverage is standard — verify it includes your home country and travel destinations
- If you practice sports that are uncommon in Germany, verify they're not excluded
- Useful for expats who engage in outdoor activities (hiking, skiing) in the Alps

### Decision Tree
1. Do you have BU coverage? → Unfallversicherung is supplementary, not critical
2. Is BU too expensive or unavailable? → Unfallversicherung as partial fallback
3. Do you have risky hobbies? → Recommended regardless of BU status
4. Desk worker with no risky hobbies and good BU? → Probably not needed

### Common Pitfalls
- Treating Unfallversicherung as a BU replacement (it only covers accidents, not illness — and illness causes 70% of disability)
- Choosing low progression (100-150%) making the payout insufficient for severe injuries
- Not checking the Gliedertaxe — losing a thumb might be rated at 20% by one insurer and 30% by another
- Confusing it with statutory accident insurance (which only covers work/commute)

---

## 9. Auslandsreisekrankenversicherung (International Travel Health Insurance)

### Overview
Covers medical costs and especially medical repatriation (Ruecktransport) during travel outside Germany. GKV provides NO or very limited coverage outside the EU, and even within the EU, coverage is incomplete.

### Who Needs It
**All expats.** If you ever travel outside Germany — to visit family, on vacation, for business — you need this. It is possibly the best value-for-money insurance in existence.

### When Critical
- You visit your home country (GKV doesn't cover non-EU countries, and even EU coverage has gaps)
- You travel for vacation
- Medical repatriation can cost EUR 50,000-100,000+ (air ambulance from Thailand: ~EUR 80,000)

### Cost Structure
| Type | Annual Premium |
|------|---------------|
| Single (trips up to 42 days) | EUR 9-15/year |
| Single (trips up to 56 days) | EUR 12-20/year |
| Family (trips up to 42 days) | EUR 20-30/year |
| Long-term / expat (trips 56+ days) | EUR 30-100/year |

Yes, that's per YEAR. For EUR 10-15/year, you get coverage that could save you EUR 100,000+.

### Key Comparison Criteria
1. **Medical repatriation (Ruecktransport):** Must be "medically sensible" (medizinisch sinnvoll), NOT just "medically necessary" (medizinisch notwendig). The "sensible" wording means you get flown home even if local treatment is possible but home treatment is better.
2. **Trip duration:** Standard is 42-56 days per trip. Expats visiting home may need longer coverage.
3. **Pre-existing conditions (Vorerkrankungen):** Some policies cover acute flare-ups of known conditions, others don't.
4. **No age limit or transparent age surcharges:** Some policies become very expensive after 65-70.
5. **Pandemic coverage:** Post-COVID, check if pandemics are covered or excluded.

### Provider Landscape
- **Top-rated:** HanseMerkur, Allianz Travel, ERGO Reise (ERV), DKV
- **Best value:** HanseMerkur (consistently top-rated, EUR 9-12/year single)
- **Expat-friendly:** HanseMerkur, Allianz Travel (English claims process)

### Tax Deductibility
- Deductible as sonstige Vorsorgeaufwendungen
- **Practical impact: EUR 0** — cap exhausted. And at EUR 10-20/year premium, the tax saving would be cents anyway.

### Expat Considerations
- This is the #1 most underrated insurance for expats
- GKV Europaische Krankenversicherungskarte (EHIC) only works within EU/EEA and is limited to local public healthcare standards
- If you fly home to Brazil, India, US, or any non-EU country — GKV covers NOTHING
- Medical repatriation alone justifies the cost 100x over
- Some policies offer annual contracts with automatic renewal — set it and forget it

### Decision Tree
1. Do you ever leave Germany? → Get travel health insurance. Done.
2. Do you visit a non-EU home country? → ESSENTIAL. Not negotiable.
3. Already have PKV? → Check if international coverage is included. If not, add Reiseversicherung.
4. Never leave Germany? → You don't need it (but really, never?)

### Common Pitfalls
- Assuming GKV covers you abroad (it barely covers EU, and nothing outside)
- Not checking the Ruecktransport wording ("medizinisch sinnvoll" vs "medizinisch notwendig")
- Buying per-trip insurance when an annual policy is cheaper
- Exceeding the maximum trip duration without realizing coverage has lapsed

---

## 10. KFZ-Versicherung (Car Insurance)

### Overview
Only relevant if you own or regularly drive a car in Germany. Three tiers:
- **KFZ-Haftpflicht:** Mandatory. Covers damage you cause to others.
- **Teilkasko (partial comprehensive):** Covers theft, natural damage, animal collisions, glass, fire.
- **Vollkasko (full comprehensive):** Teilkasko + covers damage to your own car regardless of fault.

### Who Needs It
- **Only car owners/regular drivers.** If you don't have a car, skip this entirely.

### When Critical
- You own a car → KFZ-Haftpflicht is legally mandatory
- New or expensive car → Vollkasko recommended for first 3-5 years
- Older car (worth under EUR 5,000) → Haftpflicht only or Haftpflicht + Teilkasko

### Cost Structure
Highly variable based on many factors:
- **Schadenfreiheitsklasse (SF-Klasse):** No-claims bonus class. Starts at SF 0 (highest premium) for new drivers. Each claim-free year reduces the class. SF 10+ can mean 30-40% of base premium.
- **Typklasse:** Vehicle type classification (sports car vs family sedan)
- **Regionalklasse:** Where you live (Munich is more expensive than rural Saxony)
- **Annual mileage**
- **Garage vs street parking**

| Coverage | Annual Premium Range |
|----------|---------------------|
| Haftpflicht only (experienced driver, mid-range car) | EUR 200-500/year |
| Haftpflicht + Teilkasko | EUR 350-800/year |
| Haftpflicht + Vollkasko (new car, SF 0) | EUR 800-2,500+/year |
| Haftpflicht + Vollkasko (experienced, mid-range) | EUR 500-1,200/year |

### Key Comparison Criteria
1. **SF-Klasse transfer:** If switching from another insurer or country, can your no-claims history be transferred?
2. **Werkstattbindung:** Agreeing to use the insurer's partner workshops saves 10-20% on premium
3. **Selbstbeteiligung (deductible):** Teilkasko typically EUR 150, Vollkasko EUR 300-500
4. **Mallorca-Police:** Covers rental car liability abroad above the local minimum
5. **GAP coverage (for leased/financed cars):** Covers the difference between car value and outstanding loan

### Provider Landscape
- **Consistently competitive:** HUK-COBURG, HUK24, CosmosDirekt, Friday, WGV
- **Traditional:** Allianz, AXA, ADAC
- **Switch period:** Most KFZ policies renew on January 1, with a cancellation deadline of November 30 (Stichtag). Annual comparison shopping in October-November is standard practice.

### Tax Deductibility
- **KFZ-Haftpflicht:** Deductible as sonstige Vorsorgeaufwendungen (but cap usually exhausted)
- **Teilkasko/Vollkasko:** NOT deductible (property insurance)
- **If car is used for work:** Business use portion may be deductible as Werbungskosten
  - Requires a Fahrtenbuch (driving log) or applying the Entfernungspauschale (commute allowance) method

### Expat Considerations
- New to Germany = SF 0 = VERY expensive first year. Some insurers accept foreign no-claims history (ask specifically)
- International driving license valid for 6 months, then you need a German one
- If bringing a car from abroad: re-registration and insurance can be complex
- Consider car-sharing (ShareNow, SIXT Share) if you don't need a car daily — avoids insurance entirely

### Decision Tree
1. Do you own a car? → You MUST have KFZ-Haftpflicht
2. Car newer than 5 years or worth more than EUR 15,000? → Add Vollkasko
3. Car 5-10 years old? → Teilkasko is usually sufficient
4. Car older than 10 years or worth under EUR 5,000? → Haftpflicht only
5. Don't own a car? → You don't need KFZ insurance. Move on.

### Common Pitfalls
- Not switching annually during the November Stichtag — loyalty is not rewarded, comparison shopping saves EUR 100-500/year
- Forgetting to transfer SF-Klasse from a previous insurer or country
- Getting Vollkasko on a car that's not worth it
- Not adjusting annual mileage when working from home (lower mileage = lower premium)
