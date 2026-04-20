# Financial Analysis Guide

How to analyze individual holdings — stocks and ETFs — for the portfolio review. Includes metrics, interpretation, sentiment methodology, data sources, and the interaction between fundamentals and tax efficiency.

---

## Key Financial Metrics for Individual Stocks

### Valuation Metrics

**Price-to-Earnings Ratio (P/E)**
- Trailing P/E: current price / last 12 months EPS
- Forward P/E: current price / estimated next 12 months EPS
- Interpretation:
  - Compare to the stock's own 5-year average (is it cheap or expensive vs its own history?)
  - Compare to sector median (is it cheap or expensive vs peers?)
  - High P/E alone is not bad — growth stocks command premium. But P/E expansion without earnings growth is a warning sign.
- Red flags: P/E > 2x sector median without clear growth justification, negative earnings (no P/E)

**Price-to-Sales Ratio (P/S)**
- Current price / revenue per share
- Most useful for high-growth companies that are not yet profitable
- Compare to historical P/S and sector peers
- Red flags: P/S > 10x for a mature company, P/S expanding while revenue growth decelerates

**PEG Ratio (Price/Earnings to Growth)**
- P/E divided by expected earnings growth rate
- PEG < 1.0: potentially undervalued relative to growth
- PEG 1.0-2.0: fairly valued
- PEG > 2.0: potentially overvalued relative to growth
- Limitation: depends on growth estimates, which can be wrong

**Free Cash Flow Yield**
- Free cash flow per share / current price
- Measures how much cash the business generates relative to its price
- FCF yield > 5%: generally attractive
- FCF yield < 2%: expensive unless high growth
- More reliable than earnings-based metrics (harder to manipulate)

**Enterprise Value / EBITDA (EV/EBITDA)**
- Useful for comparing companies with different capital structures
- Removes the effect of debt, taxes, and accounting choices
- Lower is cheaper. Compare within sector.

### Growth Metrics

**Revenue Growth (CAGR)**
- 3-year and 5-year compound annual growth rate
- Interpretation:
  - >20% CAGR: high growth
  - 10-20% CAGR: solid growth
  - 5-10% CAGR: moderate growth
  - <5% CAGR: mature/slow growth
  - Negative: declining (warning sign)
- Acceleration vs deceleration matters more than the absolute number

**Earnings Growth**
- EPS CAGR over 3 and 5 years
- Compare to revenue growth — earnings growing faster than revenue = margin expansion (positive)
- Earnings growing slower than revenue = margin compression (negative)

**Dividend Growth**
- Annual dividend growth rate
- Consecutive years of dividend increases
- Payout ratio (dividends / earnings): sustainable if <60% for most sectors, <80% for utilities/REITs
- Dividend yield vs historical average for the stock

### Profitability Metrics

**Gross Margin**
- (Revenue - COGS) / Revenue
- Trend matters: expanding = pricing power or efficiency gains, contracting = competitive pressure
- Compare to sector: software >70%, industrials 25-35%, retail 20-40%

**Operating Margin**
- Operating income / Revenue
- Captures the efficiency of core operations
- Trend over 4-8 quarters is more important than a single data point

**Net Margin**
- Net income / Revenue
- Includes financing costs and taxes
- Can be distorted by one-time items — always check for adjustments

**Return on Equity (ROE)**
- Net income / shareholders' equity
- Measures how efficiently the company uses investor capital
- >15% generally good, >20% excellent
- Warning: high ROE with high debt can be misleading (financial leverage)

---

## Quarterly Earnings Analysis (Last 4 Quarters)

For each of the last 4 quarters, evaluate:

### Earnings Beat/Miss
- Did EPS beat or miss consensus estimates?
- By how much? (>5% beat is strong, >5% miss is concerning)
- Pattern: 4 consecutive beats = strong execution. 2+ misses = deterioration
- Revenue beat/miss is equally important — earnings beats from cost-cutting without revenue growth are not sustainable

### Guidance
- Did management raise, maintain, or lower forward guidance?
- Raised guidance = confidence, positive
- Maintained guidance when market expected a raise = slightly negative
- Lowered guidance = warning sign, especially if done multiple quarters in a row

### Margin Trends
- Are gross, operating, and net margins trending up or down over the 4 quarters?
- Seasonal effects: some businesses have natural margin variation by quarter (retail Q4, etc.)
- Consistent margin contraction over 3+ quarters = red flag

### Red Flags to Watch For
- Revenue declining year-over-year
- Earnings misses despite lowered expectations
- Significant one-time charges or write-downs
- Executive departures (especially CFO)
- Accounting methodology changes
- Unusual inventory buildup
- Rising accounts receivable faster than revenue (potential collection issues)
- Regulatory investigations or fines
- Dividend cut or suspension
- Share issuance (dilution) without clear growth investment

---

## ETF Evaluation Criteria

### Total Expense Ratio (TER)
- The annual management fee charged by the fund
- For broad market index ETFs: <0.20% is good, <0.10% is excellent, >0.30% is expensive
- For niche/thematic ETFs: higher TER is expected (0.30-0.65%)
- TER is deducted from fund performance, not charged separately

**Benchmarks:**
| ETF Category | Good TER | Acceptable TER | Expensive TER |
|-------------|----------|-----------------|---------------|
| S&P 500 | <0.10% | 0.10-0.15% | >0.15% |
| MSCI World | <0.20% | 0.20-0.30% | >0.30% |
| MSCI EM | <0.20% | 0.20-0.40% | >0.40% |
| Bond aggregate | <0.15% | 0.15-0.25% | >0.25% |
| Thematic/sector | <0.40% | 0.40-0.65% | >0.65% |

### Tracking Difference (TD)
- The actual performance gap between the ETF and its benchmark index
- MORE IMPORTANT than TER — a fund with 0.20% TER but -0.05% TD outperforms one with 0.07% TER and 0.15% TD
- Negative TD (outperforming the index): possible through securities lending revenue or tax optimization
- Check 3-year and 5-year average tracking difference for reliability
- Source: trackingdifferences.com, justETF

### Fund Size (AUM — Assets Under Management)
- Larger funds generally have better liquidity and lower trading spreads
- < 50M EUR: small, potential closure risk, wider spreads — WARNING
- 50-100M EUR: acceptable but monitor
- 100M-1B EUR: solid
- > 1B EUR: large, very liquid, low closure risk

### Replication Method
- **Physical full replication:** Holds all index constituents. Most transparent, preferred.
- **Physical sampling (optimized):** Holds a representative sample. Normal for large indices (MSCI World has 1,500+ stocks). Acceptable.
- **Synthetic (swap-based):** Uses a swap contract with a counterparty bank. Adds counterparty risk. May have tax advantages. Less transparent. Flag and explain the trade-off.

### Distribution Policy
- **Distributing (ausschuettend):** Pays dividends to investor. Simpler for tax, uses Sparerpauschbetrag automatically.
- **Accumulating (thesaurierend):** Reinvests dividends in the fund. More tax-efficient for growth (Vorabpauschale is usually less than actual distributions). Preferred for buy-and-hold if Sparerpauschbetrag is already used via other income.

### Domicile
- Ireland (IE): preferred for German investors — best DBA treaty with the US, efficient dividend taxation at fund level
- Luxembourg (LU): also good, similar DBA benefits
- Germany (DE): acceptable but may be less tax-efficient at fund level
- US: avoid (UCITS non-compliance, estate tax risk, withholding tax issues)

### Teilfreistellung Eligibility
- Confirm the fund qualifies for the expected Teilfreistellung rate
- Equity ETFs (>50% stocks): 30% exemption
- Check the fund's actual equity allocation — some "mixed" ETFs may surprise
- Source: fund factsheet, broker securities detail, justETF/extraETF

---

## Sentiment Rating Methodology

Assign one sentiment rating per holding based on the combined analysis.

### Strong Buy
**Criteria (meet at least 3):**
- Strong fundamental growth (revenue + earnings growing >10%)
- Undervalued vs historical and sector (P/E, P/S below average)
- Positive earnings momentum (beats in recent quarters, guidance raised)
- Tax-efficient structure (ETF with Teilfreistellung, or Irish-domiciled)
- Underweight in portfolio (adds diversification)
- Strong free cash flow generation

### Buy
**Criteria (meet at least 2):**
- Solid fundamental growth (positive revenue and earnings trends)
- Reasonably valued (not significantly above historical averages)
- No major red flags in recent quarters
- Fits portfolio allocation targets
- Acceptable tax efficiency

### Hold
**Criteria:**
- Fundamentals are adequate (stable, not deteriorating)
- Fairly valued (near historical and sector averages)
- No compelling reason to add or reduce
- Position size is appropriate
- Default rating when no strong signal exists in either direction

### Consider Selling
**Criteria (meet at least 1):**
- Fundamentals weakening (1-2 quarterly misses, margins declining)
- Significantly overvalued vs historical (P/E >1.5x 5-year average without growth acceleration)
- Concentration risk (position >10% of portfolio for individual stocks)
- Better tax-efficient alternative exists (e.g., move from individual stock to ETF for Teilfreistellung)
- Tax-loss harvesting opportunity exists but the investor may want to keep the position

### Sell
**Criteria (meet at least 1):**
- Fundamentals deteriorating significantly (multiple misses, guidance cuts, margin collapse)
- Severe concentration risk (position >20% for individual stocks)
- Large unrealized loss with clear tax-loss harvesting benefit AND the position can be replaced with a better alternative
- Company-specific risk event (accounting scandal, regulatory action, industry disruption)
- The position no longer fits the investment thesis under which it was purchased

---

## Fundamentals and Tax Efficiency Interaction

The sentiment rating should incorporate BOTH fundamental quality and tax positioning. This is where the portfolio skill adds unique value over generic stock analysis.

### Scenarios Where Tax Efficiency Overrides Hold

**Individual stock with mediocre fundamentals (Hold on fundamentals alone):**
- If the same exposure is available via a Teilfreistellung-eligible ETF, upgrade to "Consider Selling"
- Show the math: "Moving from Stock X to ETF Y saves 7.9% on every EUR of future gains"
- This is especially compelling for positions with small embedded gains (low tax cost to switch)

**Position with unrealized loss (Hold on fundamentals alone):**
- If the loss is meaningful (>500 EUR tax savings) and the investor wants to keep the exposure: "Sell and rebuy"
- Germany has no wash sale rule — this is pure tax alpha
- Upgrade to "Sell" with the specific instruction to rebuy immediately

### Scenarios Where Fundamentals Override Tax Efficiency

**Strong stock with no Teilfreistellung:**
- If the stock is a Strong Buy on fundamentals, do NOT downgrade just because of tax structure
- The 7.9% tax drag per gain is real but a strong grower compounds past it
- Note the tax disadvantage but respect the fundamental thesis

**Tax-efficient ETF with poor tracking or high TER:**
- Teilfreistellung does not help if the ETF underperforms its index by a wide margin
- An ETF with 30% Teilfreistellung but 0.5% annual tracking difference may be worse than a stock with good returns

### The Decision Matrix

```
                    Tax-Efficient           Tax-Inefficient
                    (ETF w/ TF)             (Individual stock)
                ┌───────────────────┬───────────────────────┐
Strong          │ Strong Buy        │ Buy                   │
Fundamentals    │ (best of both)    │ (fundamentals win)    │
                ├───────────────────┼───────────────────────┤
Average         │ Buy / Hold        │ Consider Selling      │
Fundamentals    │ (tax-efficient)   │ (switch to ETF?)      │
                ├───────────────────┼───────────────────────┤
Weak            │ Consider Selling  │ Sell                  │
Fundamentals    │ (TF not enough)   │ (no reason to hold)   │
                └───────────────────┴───────────────────────┘
```

---

## Data Sources and Their Limitations

### Free Sources
- **Yahoo Finance:** Price data, basic financials, earnings dates. Reliable for prices, sometimes delayed on fundamentals.
- **Google Finance:** Price data, basic news. Limited financial data.
- **justETF / extraETF:** ETF profiles, TER, tracking difference, Teilfreistellung status. Best source for ETF analysis for European/German investors.
- **trackingdifferences.com:** Tracking difference data for European ETFs.
- **Fund factsheets (from provider):** Official TER, allocation, benchmark, replication method. Available on iShares, Vanguard, Xtrackers, Amundi websites.
- **SEC EDGAR / Company investor relations:** Official filings, earnings reports, 10-K, 10-Q.
- **Deutsche Bundesbank:** Basiszins for Vorabpauschale calculation.
- **BMF (Bundesfinanzministerium):** Official tax parameters, guidance letters.

### Paid / Premium Sources
- **Morningstar:** Fund ratings, analyst reports, detailed ETF analysis. Some free, most behind paywall.
- **Bloomberg Terminal:** Comprehensive financial data. Not available to retail investors.
- **FactSet, Refinitiv:** Institutional data providers.

### Limitations to Always Disclose
- **Earnings estimates are consensus, not truth.** A stock "beating" estimates may still have declining fundamentals if estimates were lowered beforehand.
- **P/E ratios can be misleading** for cyclical companies, companies with one-time charges, or companies at earnings inflection points.
- **Past performance does not predict future returns.** This applies to both stocks and ETFs.
- **Tracking difference varies year to year.** A single year's TD is not reliable — use 3-5 year averages.
- **Fund size can change.** A large fund today could face outflows. A small fund could grow.
- **Tax laws change.** German investment tax law was reformed in 2018 and could change again. Basiszins changes annually.
- **Currency effects are real.** A USD-denominated ETF held by a EUR-based investor has currency exposure. This is not hedged unless the ETF specifically offers a EUR-hedged share class.
- **AI-generated analysis has knowledge cutoffs.** Always verify current prices, recent earnings, and latest tax parameters with live sources. State your knowledge cutoff date explicitly.

### When Data is Unavailable
- State clearly: "Current price data is not available. The analysis below uses the last known price of X EUR from [date]. Please verify the current price."
- Never fabricate financial numbers. If a metric cannot be verified, say: "P/E ratio not available from my sources. Check Yahoo Finance or Morningstar for the current value."
- For forward estimates: "Consensus EPS estimate for next year is approximately X based on [source/date]. Verify with your broker or a financial data provider."
