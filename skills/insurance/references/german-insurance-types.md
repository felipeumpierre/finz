# German Insurance Types — Comprehensive Reference

This file is the knowledge base for the insurance audit skill. It covers all 10 insurance types relevant to German residents and expats, with real numbers, provider names, and decision logic.

**Last verified:** 2026-06-03 (Krankenversicherung §1 updated to 2026 figures)

> **Verification caveat:** Only §1 Krankenversicherung was re-checked against primary sources for 2026. The other insurance types in this file still carry their 2025 figures and have NOT been re-verified for 2026 — treat them as "no newer source contradicts" rather than freshly confirmed.

Primary sources used for the Krankenversicherung (GKV/PKV) 2026 figures:
- Bundesministerium für Arbeit und Soziales (BMAS) — Sozialversicherungs-Rechengrößenverordnung 2026 (BBG, JAEG, Bezugsgröße)
- Bundesministerium für Gesundheit (BMG) — durchschnittlicher Zusatzbeitragssatz 2026 = **2.9%** (announced ~Nov 2025 per §242a SGB V); Pflegeversicherung rates
- GKV-Spitzenverband — effective collected Zusatzbeitrag average
- PKV-Verband (pkv.de) — PKV 2026 Beitragsanpassung; Basis-/Standardtarif caps

---

## 1. Krankenversicherung (Health Insurance)

### Overview
Health insurance is **mandatory** for all residents in Germany. Two systems exist:
- **GKV** (Gesetzliche Krankenversicherung) — statutory/public health insurance
- **PKV** (Private Krankenversicherung) — private health insurance

**Legal basis:** SGB V (Social Code Book V) for GKV; VVG (Insurance Contract Act) for PKV.

### Who Needs It
Everyone. No exceptions. If you live in Germany, you must have health insurance.

### GKV (Public) Details — values verified for 2026

- **Base contribution rate (allgemeiner Beitragssatz):** 14.6% of gross income, split 50/50 employer/employee (SGB V §241). **Unchanged — frozen at 14.6% since 2015.** (Ermäßigter Beitragssatz, no Krankengeld entitlement: 14.0%.)
- **Durchschnittlicher Zusatzbeitragssatz 2026 (average supplementary contribution, BMG-festgesetzt):** **2.9%** (up from 2.5% in 2025, 1.7% in 2024). Split 50/50 employer/employee since 2019 (GKV-VEG). Announced by BMG ~Nov 2025 per §242a SGB V. This is the **legal benchmark** used for Familien-/Studentenversicherung and dependent contribution calculations. The **effective average actually collected** across funds in early 2026 is higher — **~3.36%** (range ~2.18%–4.39% per fund; GKV-Spitzenverband, read via secondary — verify before quoting). Use 2.9% for calculations; cite 3.36% only as the "effective collected average."
- **Beitragsbemessungsgrenze Krankenversicherung (BBG GKV) 2026:** **69,750 EUR/year** (5,812.50 EUR/month) — up from 66,150. Federally uniform. Source: BMAS Sozialversicherungs-Rechengrößenverordnung 2026.
- **Versicherungspflichtgrenze / Jahresarbeitsentgeltgrenze (JAEG) 2026:** **77,400 EUR/year** (6,450 EUR/month) — up from 73,800. Employees with regular Arbeitsentgelt above this threshold for one full calendar year may opt out of GKV into PKV. **Besondere JAEG** (for those already in PKV before 2003): **69,750 EUR/year** — note this coincides with the BBG, a frequent point of confusion.
- **Familienversicherung:** Non-working spouse and children covered for free in GKV (§10 SGB V).
  - 2026 income limit for Familienversicherung: **565 EUR/month** (1/7 of the Bezugsgröße 2026 = 3,955 EUR/month), or **603 EUR/month** if the income is from a Minijob. (Bezugsgröße is primary/BMAS; the 565/603 limit values are derived/secondary — verify the exact Minijob-Grenze at BMAS before final advice.)

**GKV-Höchstbeitrag (at BBG, 2026):**

| Component | Rate (employee share) | Monthly at BBG 5,812.50 EUR |
|---|---|---|
| Allgemeiner Beitrag (14.6% / 2) | 7.30% | 424.31 EUR |
| Durchschn. Zusatzbeitrag (2.9% / 2) | 1.45% | 84.28 EUR |
| **KV employee share total** | **8.75%** | **≈ 508.59 EUR/month** |

Using the *effective* collected Zusatzbeitrag (~3.36%) the KV employee share is ≈521.96 EUR/month instead.

**Pflegeversicherung** (not GKV proper but bundled on the same Entgeltabrechnung) — 2026: **3.6% base** (was already raised to 3.6% on **1 Jan 2025**, so the previous "3.4%" was stale even for 2025) **plus 0.6% Kinderlosenzuschlag** for childless over 23 (→ 4.2%). Per-child reduction of **−0.25 pp for the 2nd–5th child** (children under 25), down to 2.6% at 5+ children. Employee base share ~1.8% (Saxony 2.3%); childless employee ~2.4%. Pflege-BBG = KV-BBG = 5,812.50 EUR/month. At BBG this adds roughly **+105 EUR/month** (1 child) to **+140 EUR/month** (childless) on top of the KV number.

**Total GKV employee share at BBG (KV + Pflege), 2026:** ≈**613 EUR/month** (1 child) to ≈**661 EUR/month** (childless).

### PKV (Private) Details
- **Entry requirements:** Income above JAEG (employed: 2026 = 77,400 EUR/year, must *exceed* it for a full year) or self-employed/Freiberufler (no income threshold) or Beamte (via Beihilfe). The opt-out from GKV is a §8 SGB V exemption filed within 3 months — **irrevocable** for the duration of that employment.
- **Premium range:** EUR 250-1,200+/month depending on age at entry, health status at application, coverage level, and deductible (Selbstbeteiligung) selected. 2026 PKV-Verband **average premium ≈ 617 EUR/month**.
- **Employer contribution (Arbeitgeberzuschuss, §257 SGB V):** 50% of the PKV premium, capped at the maximum employer share of GKV — for 2026 this cap is **≈ EUR 508.59/month** for KV (5,812.50 EUR × 8.75%, using base 14.6% + durchschn. Zusatzbeitrag 2.9%, employer half) **plus ≈ EUR 104.63/month** Pflege employer share = **≈ EUR 613/month combined** (Saxony Pflege share differs).
- **Age warning:** Premiums increase with age and medical inflation. 2026 average PKV Beitragsanpassung was **~13%** (affecting ~60% of insured; 2025 was ~18% for two-thirds). Increases are lumpy by design — §203 VVG only permits repricing when actual costs deviate beyond a threshold.
- **Alterungsrückstellungen (aging provisions):** Level-premium reserves built up while young to dampen old-age premiums. A **10% statutory surcharge (gesetzlicher Zuschlag)** is levied ages 22–60 and deployed from 65. Since 2009 a portable **Übertragungswert** (capped at the Basistarif-equivalent) transfers to a new insurer on switching; the richer-tariff reserves above that are **forfeited**, and a new Gesundheitsprüfung applies. A **Beitragsentlastungstarif** can be bought to cap premiums in old age.
- **Returning to GKV (§6 Abs. 3a SGB V):** From **age 55**, return is essentially locked out. Before 55, routes back exist: income dropping below the JAEG (as an employee), entering Familienversicherung via a GKV-insured spouse, or receiving ALG I. Pensioners need to meet the **KVdR 9/10 rule** to enter GKV-Rentner.

**Family & children in PKV (there is NO Familienversicherung):**
- Each family member holds a **separate, individually underwritten contract** with its own premium — PKV has no free family coverage ("In der Privaten Krankenversicherung muss sich jede versicherte Person eigenständig versichern", PKV-Verband).
- **Members are NOT required to be with the same insurer.** A child can legally be insured with a different PKV company than the parent, and one spouse may be PKV while the other is GKV. Many families do use one insurer for convenience, but it is not a legal requirement.
- **Important exception — Kindernachversicherung (newborn guaranteed acceptance):** the no-health-check, no-risk-surcharge guarantee for a newborn is tied to **one parent having been insured with that specific company for at least 3 months before the birth**, with the child's application filed **within 2 months of birth**. Insure the newborn with a *different* insurer and a normal Gesundheitsprüfung applies (relevant if the child has health risks). Source: PKV-Verband.
- **Life-change implication (advise on this, not just cost):** PKV with children is rarely just "cheaper or not." A child in GKV would be *free* under Familienversicherung; in PKV each child costs a separate premium that rises over life. Before recommending or staying in PKV, factor in: planned/likely children, whether a GKV-insured spouse could carry children for free, the irreversibility after age 55, and the newborn-acceptance timing above. These are decision drivers a Steuerberater-style adviser must surface even when the pure monthly math favours PKV today.

**Safety-net / regulated PKV tariffs (2026):**
- **Basistarif** — benefits comparable to GKV, open to all, no risk surcharge; premium capped at the **GKV Höchstbeitrag ≈ 1,017.18 EUR/month** (17.5% × BBG incl. Zusatzbeitrag).
- **Standardtarif** — for long-standing pre-2009 insured; capped at **≈ 848.62 EUR/month** (14.6% × BBG).
- **Notlagentarif** — automatic fallback on premium non-payment; covers only acute/emergency care until arrears are cleared.
- **Pflegepflichtversicherung in PKV** — mandatory for PKV insured, risk-priced, capped at the GKV Pflege Höchstbeitrag. PKV-Verband averages ~56.50 EUR/month with Beihilfe, ~122.64 EUR/month without (secondary figures).

### Cost Structure by Profile (2026 figures, KV employee share only — excludes Pflegeversicherung)
Calculation basis: 8.75% of gross (up to BBG 5,812.50 EUR/month) = 7.3% allg. Beitrag + 1.45% durchschn. Zusatzbeitrag (employee half of 14.6% + 2.9%).

| Profile | GKV Monthly (Employee Share, KV only) | PKV Monthly (Estimate) |
|---------|------------------------------|------------------------|
| Single, age 30, EUR 50k salary | ~EUR 365 | EUR 280-450 |
| Single, age 30, EUR 80k salary | **~EUR 509 (at BBG cap)** | EUR 280-450 |
| Single, age 45, EUR 90k salary | **~EUR 509 (at BBG cap)** | EUR 450-800 |
| Family, one income, EUR 80k | ~EUR 509 (at BBG cap; family free in GKV) | EUR 800-1,500+ (each person separate) |

Note: Pflegeversicherung employee share adds roughly +105 EUR/month (1 child) to +140 EUR/month (childless) at BBG, on top of the KV figures above — so the total GKV employee share at the cap is ≈613–661 EUR/month. Using the *effective* collected Zusatzbeitrag (~3.36%) instead of the legal 2.9% benchmark raises the KV cap figures by ~13 EUR/month.

### GKV vs PKV — Services, Differences, Pros & Cons

Single consolidated comparison. PKV columns describe what a tariff *can* offer — actual benefits depend on the chosen tariff (a cheap PKV tariff can be worse than GKV).

| Dimension | GKV | PKV |
|---|---|---|
| **Delivery principle** | Sachleistungsprinzip — card, Kasse pays provider directly; no upfront cost, minimal paperwork | Kostenerstattungsprinzip — you pay the bill, then claim reimbursement; more paperwork/upfront cash |
| **Benefit basis** | Catalogue set by the G-BA; politically variable, can be expanded *or trimmed* | Contractually fixed at sign-up; insurer cannot unilaterally cut agreed benefits |
| **Family coverage** | Free Familienversicherung (spouse + children) | None — every member is a separate, individually-priced contract |
| **Premium basis** | Income-based; falls if income falls | Risk-based (age + health at entry) |
| **Premium trend** | Rises with salary; rising effective cost via Zusatzbeitrag | Rises with age + medical inflation (2026 avg ~13% for ~60% of insured) |
| **Doctor/specialist access** | Standard; specialists can have longer waits | Often faster appointments; broader provider/method choice |
| **Hospital (stationär)** | Ward room, treating-duty physician | Wahlleistungen possible: Chefarztbehandlung, single/double room |
| **Dental (Zahnersatz)** | Festzuschuss 60% / 70% / 75% (Bonusheft); €0 for implants | Higher reimbursement; implants/premium ceramics often covered |
| **Prescriptions** | 10% co-pay (min €5 / max €10) | Reimbursed per tariff (often fuller, incl. some non-GKV drugs) |
| **Alt. medicine / Heilpraktiker, vision aids** | Limited or excluded | Coverable if the tariff includes it |
| **Psychotherapy** | Covered, often long waits for a slot | Tariff-dependent; access can be faster |
| **Sick pay** | Krankengeld from day 43 (70% gross / max 90% net) | Optional Krankentagegeld tariff (freely chosen amount/start day) |
| **Switching / flexibility** | Easy to switch Kassen, no reserves lost | Reserves partly lost on insurer switch; new Gesundheitsprüfung |
| **Return / lock-in** | Open | Near-impossible return to GKV after age 55 |
| **Best fit** | Families, variable/falling income, those wanting simplicity | Young healthy high-earning singles; Beamte (via Beihilfe) |

> **Advisory framing (not just the monthly number):** the right system depends on life trajectory — children planned, single vs family income, Beamten-status, age, health, and whether GKV-via-spouse is available — far more than on this year's premium. Surface these even when today's math favours one side.

### GKV Rules & Benefits in Detail (2026)

**Who must / who can be in GKV:**
- **Versicherungspflicht (compulsory):** employees earning ≤ JAEG (77,400 EUR/yr), ALG-I recipients, students, KVdR pensioners, KSK artists.
- **Versicherungsfrei (may opt to PKV):** employees above the JAEG for a full year, self-employed/Freiberufler, Beamte.
- **Freiwillig versichert (voluntary GKV):** those who could leave but stay — membership continues automatically as voluntary GKV (§9) unless a §8 PKV opt-out is filed within 3 months.
- **KVdR (pensioner GKV):** entry requires the **9/10 rule** — GKV-insured for 90% of the second half of working life (+3 years credited per child).

**Familienversicherung (§10 SGB V):** spouse and children covered **free of charge** if resident in Germany and income ≤ 565 EUR/month (Minijob 603 EUR). Children to age 18 / 23 (if not working) / 25 (if in education) / no limit if disabled. This is worth EUR 400-800+/month vs PKV where each person pays separately.

**Benefit scope (Sachleistungsprinzip — benefits in kind, no upfront payment):**
- Doctor visits & hospital treatment: free at point of use.
- **Zuzahlungen (co-payments):** hospital 10 EUR/day (max 28 days/year); prescriptions 10% (min 5 / max 10 EUR per item). *(A ~+50% co-payment hike to 7.50/15 EUR is proposed for 2027 — not 2026 law.)*
- **Belastungsgrenze:** annual co-payment cap of **2% of gross income** (**1%** for chronically ill per G-BA Chroniker-Richtlinie) — beyond this the Kasse reimburses.
- **Dental:** Festzuschuss of **60%** of the Regelversorgung standard, rising to **70%** (5-year Bonusheft) / **75%** (10-year Bonusheft). Zero for implants/premium ceramics — hence Zahnzusatzversicherung (see §7).
- **Krankengeld (sick pay):** from day 43 of an illness, **70% of gross / capped at 90% of net**, 2026 cap **135.63 EUR/day**, max **78 weeks within 3 years** per illness.
- Preventive care (Vorsorge/Früherkennung): free.

**Freie Kassenwahl & switching:** 12-month Bindungsfrist, then 2 months' notice. **Sonderkündigungsrecht** — any Zusatzbeitrag increase by your Kasse triggers a special right to switch immediately, overriding the Bindungsfrist (exception: a 36-month Krankengeld-Wahltarif).

**2026 developments & forward context:**
- Average Zusatzbeitrag up to 2.9% (effective collected ~3.36%) — the dominant cost driver, since the 14.6% base is frozen.
- **ePA "für alle"** (electronic patient record): opt-out model, provider use mandatory since Oct 2025, new functions rolling out 2026.
- **GKV-Beitragssatzstabilisierungsgesetz** in draft (Bundestag first reading ~12 Jun 2026): provider-cost caps, possible family-insurance surcharge, dental cuts.
- Projected GKV funding gap **~€15.3 bn in 2027 → ~€40 bn by 2030**; demographic Pflege gap.
- **⚠️ 2027, not 2026:** a large JAEG/BBG jump (JAEG projected **~84,483 EUR/yr**) and the co-payment hike are cabinet/draft stage for 2027 — do not present as enacted 2026 law.

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
