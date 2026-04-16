# Gap Analysis Framework

This document defines the methodology for evaluating a user's insurance coverage against their needs. Every audit follows this framework to produce consistent, profile-driven recommendations.

---

## Evaluation Dimensions

Every insurance type is evaluated on three dimensions:

### 1. Relevance
Does this insurance make sense for the user's situation?

- **Relevant:** The user's profile includes triggers that make this insurance applicable
- **Not relevant:** No profile triggers match (e.g., KFZ for someone without a car)

### 2. Priority
How urgently does the user need this insurance?

| Priority | Definition | Action Required |
|----------|-----------|-----------------|
| **Critical** | Legally mandatory OR financial ruin without it | Get immediately |
| **Recommended** | Significant financial risk, strong cost-benefit ratio | Get within 1-3 months |
| **Optional** | Nice to have, moderate risk, or cost-benefit is marginal | Consider when budget allows |
| **Not needed** | Not applicable to this user's situation | Skip entirely |

### 3. Tax Impact
What is the practical tax benefit of this insurance premium?

- Calculate whether the premium is deductible
- Determine under which category (Vorsorgeaufwendungen, Werbungskosten, etc.)
- Assess whether the relevant cap is already exhausted
- Compute the actual EUR saved per year in taxes

---

## Profile-Driven Priority Logic

The following rules map profile fields to insurance priorities. Multiple triggers can overlap — use the HIGHEST priority triggered.

### Krankenversicherung (Health)
- **Always Critical.** Legally mandatory for all German residents.
- Profile check: Verify user has health insurance. If not, this is priority #0.
- GKV vs PKV analysis: Compare based on salary, family status, age, long-term plans.

### Privathaftpflicht (Liability)
- **Always Critical.** Near-universal recommendation.
- Profile check: Verify user has it. If not, this is the cheapest critical gap to close.
- Family check: If `family_status == "married"` or `children.length > 0`, recommend family policy.

### BU (Disability)
**Priority triggers:**
| Profile Condition | Priority |
|-------------------|----------|
| `gross_annual_salary > 40000` AND (`children.length > 0` OR `family_status == "married"`) | **Critical** |
| `gross_annual_salary > 40000` AND single | **Recommended** |
| `gross_annual_salary > 60000` (any status) | **Critical** |
| `employment_type == "self-employed"` | **Critical** (no employer safety net) |
| `gross_annual_salary < 30000` AND no dependents | **Optional** |

**Coverage calculation:**
1. Determine net monthly income: `gross_annual_salary * 0.6 / 12` (approximate for tax class 1)
2. Estimate EM-Rente: ~EUR 1,001/month (average, assuming full contribution history)
3. Gap = net monthly income - EM-Rente
4. Recommended BU benefit = 60-80% of net income (minimum EUR 1,500/month)
5. Estimate premium based on age and profession from cost benchmarks

### Rechtsschutz (Legal Protection)
**Priority triggers:**
| Profile Condition | Priority |
|-------------------|----------|
| `residency_status == "expat"` AND `employment_type == "employed"` | **Recommended** |
| `residency_status == "expat"` (any employment) | **Recommended** |
| Permanent resident, stable employment | **Optional** |
| Self-employed (own legal structure) | **Optional** (business legal insurance is separate) |

**Module recommendation:**
- Expat employee → Beruf + Privat (at minimum)
- Renter → Add Wohnen module (or suggest Mieterverein as cheaper alternative)
- Car owner → Add Verkehr module

### Hausrat (Household Contents)
**Priority triggers:**
| Profile Condition | Priority |
|-------------------|----------|
| `risk_context.owns_property == true` | **Recommended** |
| Renter with household contents > EUR 10,000 (estimated) | **Recommended** |
| Renter with minimal possessions | **Optional** |

**Estimation heuristic:** If the user hasn't specified their household value, estimate based on:
- Salary > EUR 70,000 → likely has substantial household contents → Recommended
- Salary EUR 40,000-70,000 → likely moderate contents → Optional to Recommended
- Note: always ask the user rather than assuming

### Risikoleben (Term Life)
**Priority triggers:**
| Profile Condition | Priority |
|-------------------|----------|
| `children.length > 0` AND primary earner | **Critical** |
| `family_status == "married"` AND significant salary difference between spouses | **Recommended** |
| Mortgage holder | **Recommended** |
| `risk_context.dependents_abroad == true` | **Recommended** |
| Single, no dependents, no mortgage | **Not needed** |

**Coverage calculation:**
1. Annual salary x 3-5 = base coverage amount
2. Add outstanding mortgage amount if applicable
3. Term = years until youngest child reaches age 25, or mortgage payoff date

### Zahnzusatz (Dental)
**Priority triggers:**
| Profile Condition | Priority |
|-------------------|----------|
| In GKV AND age > 35 | **Recommended** |
| In GKV AND age 25-35 | **Optional** (but locking in low premiums is smart) |
| In GKV AND age < 25 | **Optional** |
| In PKV with dental coverage | **Not needed** |

### Unfall (Accident)
**Priority triggers:**
| Profile Condition | Priority |
|-------------------|----------|
| `risk_context.hobbies_risky == true` | **Recommended** |
| BU unavailable or unaffordable | **Recommended** (as partial fallback) |
| Has BU AND no risky hobbies | **Optional** |
| Desk worker, no risky hobbies, has BU | **Not needed** |

### Reise (Travel Health)
**Priority triggers:**
| Profile Condition | Priority |
|-------------------|----------|
| `residency_status == "expat"` | **Critical** (visiting home country) |
| `nationality != "German"` AND has family abroad | **Critical** |
| Travels internationally at all | **Recommended** |
| Never travels outside Germany | **Not needed** |

### KFZ (Car)
**Priority triggers:**
| Profile Condition | Priority |
|-------------------|----------|
| `risk_context.has_car == true` | **Critical** (Haftpflicht is legally mandatory) |
| `risk_context.has_car == false` | **Not needed** |

---

## Cost-Benefit Calculation Methodology

For each recommendation, calculate the cost-benefit ratio:

### 1. Annual Cost
- Look up the expected premium from cost benchmarks based on user's age, profile, and coverage level
- Factor in any potential premium increase trajectory (especially PKV, BU)

### 2. Risk Exposure (What you stand to lose without it)
- **Haftpflicht:** Unlimited liability → potential loss = entire wealth
- **BU:** Monthly income gap x remaining working years = total exposure
- **Risikoleben:** Dependents' financial needs over remaining dependency period
- **Rechtsschutz:** Average legal dispute cost (EUR 3,000-15,000)
- **Hausrat:** Replacement value of household contents
- **Reise:** Medical repatriation cost (EUR 50,000-100,000)
- **Unfall:** Permanent disability impact on earning capacity and quality of life

### 3. Cost-Benefit Ratio
```
Value Ratio = Risk Exposure / Annual Premium
```

Example calculations:
- **Haftpflicht:** EUR 50,000,000 exposure / EUR 65 premium = 769,230x → extraordinary value
- **Reise:** EUR 80,000 repatriation risk / EUR 12 premium = 6,667x → extraordinary value
- **BU:** EUR 1,260,000 lifetime income gap / EUR 660 annual premium = 1,909x → excellent value
- **Rechtsschutz:** EUR 10,000 avg legal cost / EUR 400 premium = 25x → good value
- **Zahnzusatz:** EUR 3,000 implant cost / EUR 300 premium = 10x → moderate value (but probability matters)

### 4. Probability-Adjusted Value
Not all risks are equally likely. Adjust recommendations with probability context:
- BU: 1 in 3 workers affected → high probability
- Major liability claim: rare but catastrophic → get it anyway
- Dental implant: varies by age, but 40%+ of adults need significant dental work by 50
- Legal dispute: expats face higher rates of employment and housing disputes

---

## Tax Impact Calculation

### Step 1: Determine Deductibility Category

| Insurance | Category | EStG Section |
|-----------|----------|--------------|
| Health (basic) | Vorsorgeaufwendungen — Basisabsicherung | Section 10(1) Nr. 3 |
| Health (supplementary) | Sonstige Vorsorgeaufwendungen | Section 10(1) Nr. 3a |
| BU, Unfall, Haftpflicht, Risikoleben | Sonstige Vorsorgeaufwendungen | Section 10(1) Nr. 3a |
| Rechtsschutz (Beruf portion) | Werbungskosten | Section 9 |
| Hausrat (home office portion) | Werbungskosten | Section 9 |
| KFZ-Haftpflicht | Sonstige Vorsorgeaufwendungen | Section 10(1) Nr. 3a |
| KFZ Teilkasko/Vollkasko | Not deductible | — |

### Step 2: Check Cap Situation

**Sonstige Vorsorgeaufwendungen cap:**
- Employees: EUR 1,900/year
- Self-employed: EUR 2,800/year

**Is the cap exhausted?**
For employees, the health insurance Basisabsicherung portion alone typically exceeds the cap:
- Employee earning EUR 69,300+ pays ~EUR 563/month employee share for GKV
- Annual: ~EUR 6,756 — far above the EUR 1,900 cap
- Therefore: ALL other sonstige Vorsorgeaufwendungen (BU, Haftpflicht, Unfall, Risikoleben) have **zero practical tax benefit** for employees in GKV

For self-employed:
- Health insurance premiums are usually EUR 600-900+/month
- Annual: EUR 7,200+ — far above the EUR 2,800 cap
- Same result: cap exhausted

**Exception — Werbungskosten-deductible portions:**
- Rechtsschutz Beruf module: ~40-60% of premium → typically EUR 100-250/year deductible
- At 35% marginal tax rate: saves EUR 35-88/year
- Hausrat home office share: typically negligible (EUR 10-30/year deductible)

### Step 3: Calculate Actual Tax Savings

```
Tax Saving = Deductible Amount x Marginal Tax Rate
```

For most insurance premiums under sonstige Vorsorgeaufwendungen:
```
Tax Saving = EUR 0 (cap exhausted)
```

For Rechtsschutz Beruf portion:
```
Tax Saving = (Premium x Beruf Share) x Marginal Tax Rate
Example: EUR 400/year x 50% x 35% = EUR 70/year
```

### Step 4: Present Honestly
Always tell the user the truth about tax deductibility:
- "Technically deductible, but the cap is almost certainly already used up by your health insurance. Practical tax benefit: zero."
- Don't let tax deductibility (or lack thereof) drive the recommendation — the insurance value should stand on its own merits.

---

## Adequacy Assessment

When the user already has a policy, assess whether the coverage is adequate:

### Coverage Amount Check
| Type | Minimum Adequate | Standard | Premium |
|------|-----------------|----------|---------|
| Haftpflicht | EUR 5M | EUR 10M | EUR 50M+ |
| BU | 40% net income | 60% net income | 80% net income |
| Risikoleben | 2x gross salary | 3x gross salary | 5x gross salary |
| Hausrat | Match contents value | EUR 650/sqm | Individual valuation |
| Unfall | EUR 100,000 | EUR 200,000 + 225% progression | EUR 300,000 + 350% |

### Policy Terms Check
For each existing policy, verify:
1. Are key protective clauses present? (e.g., BU without abstrakte Verweisung)
2. Is the coverage amount sufficient for the user's current situation?
3. Has the user's situation changed since the policy was purchased? (new child, salary increase, property purchase)
4. Is the premium competitive? (compare to current market)

### Gap Classification
| Finding | Classification |
|---------|---------------|
| Insurance type missing entirely | **Gap — Missing** |
| Coverage amount below minimum adequate | **Gap — Underinsured** |
| Key terms missing or unfavorable | **Gap — Inadequate Terms** |
| Coverage exists but user's situation has changed | **Gap — Outdated** |
| Coverage exists and is adequate | **No Gap** |
| Coverage exists and exceeds needs | **No Gap — Consider reducing if budget-constrained** |

---

## Output Structure

The audit should produce:

1. **Coverage Matrix:** One row per insurance type showing status, priority, and action needed
2. **Detailed Gap Analysis:** For each gap, a full recommendation following the format in SKILL.md
3. **Priority Action List:** Numbered list sorted by priority (Critical first, then Recommended)
4. **Cost Summary:** Total recommended additional monthly/annual insurance spend
5. **Tax Summary:** Any actual tax savings from recommended insurance (typically just Rechtsschutz Beruf)
