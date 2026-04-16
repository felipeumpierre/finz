Route this portfolio command based on the argument provided.

**Argument received:** $ARGUMENTS

## Routing Rules

If no argument or "review":
→ Read `skills/portfolio/SKILL.md` and all three reference files:
  - `skills/portfolio/references/german-investment-tax.md`
  - `skills/portfolio/references/allocation-guidelines.md`
  - `skills/portfolio/references/financial-analysis-guide.md`
→ Check if `workspace/portfolio-state.json` exists. If yes, load it and run the full three-module review (Allocation Health, Tax Efficiency, Financial Fundamentals).
→ If no state file exists, ask the user to provide their holdings data or point to a folder to scan.
→ After the review, present the prioritized action list.

If "scan" followed by a folder path (e.g., "scan ~/Documents/depot"):
→ Read `skills/portfolio/SKILL.md` and `skills/scanner/SKILL.md`.
→ Run the scanner on the specified folder, filtering for investment documents (Depotauszug, broker statements, Ertraegnisaufstellung, trade confirmations).
→ After extraction to `workspace/portfolio-state.json`, automatically run the full review workflow.

If "tax-check":
→ Read `skills/portfolio/SKILL.md` and `skills/portfolio/references/german-investment-tax.md`.
→ Load `workspace/portfolio-state.json`. If no state file exists, ask the user to provide holdings data first.
→ Run ONLY Analysis Module 2 (Tax Efficiency): Sparerpauschbetrag, Teilfreistellung, Vorabpauschale, Verlustverrechnung, foreign broker reporting, Freistellungsauftrag.
→ Update `workspace/tax-state.json` with capital income data for Anlage KAP pre-fill.
→ Present tax optimization recommendations with EUR amounts.

If "status":
→ Read `skills/portfolio/SKILL.md`.
→ Load `workspace/portfolio-state.json`. If no state file exists, tell the user no portfolio data has been captured yet and suggest running `/portfolio review` or `/portfolio scan <folder>`.
→ Show a quick summary: total positions, total value, allocation split, broker distribution.
→ Flag any stale data (current_value is null, last_updated is old).
→ Do NOT run deep analysis — status is a quick check only.

If "summary":
→ Read `skills/portfolio/SKILL.md`.
→ Load `workspace/portfolio-state.json`. If it does not exist or has no positions, return a structured summary indicating no data is available — do not prompt the user or ask questions.
→ Return structured data for `/insights`:
  - Total portfolio value across all brokers (sum of all position current_value fields)
  - Allocation split as percentages: stocks / ETFs / bonds / cash (group by position type)
  - Sparerpauschbetrag used (from tax_year_summary.sparerpauschbetrag_used)
  - Total dividends received and realized gains/losses for current year (from tax_year_summary)
  - Foreign broker income requiring Anlage KAP (sum of income from brokers where withholds_german_tax is false)
→ Do NOT run any analysis, generate recommendations, or modify any data.

## State File

Always read from and write to `workspace/portfolio-state.json`. Create it if it doesn't exist on first data capture.

When running tax-check, also update `workspace/tax-state.json` with investment-related tax data:
- `capital_income.dividends_received`
- `capital_income.realized_gains`
- `capital_income.realized_losses`
- `capital_income.vorabpauschale_estimated`
- `capital_income.foreign_broker_income`
- `capital_income.sparerpauschbetrag_used`

## Cross-Domain Integration

- After tax-check, remind the user that this data feeds into `/steuer intake` for Anlage KAP
- If `workspace/profile.json` exists, use risk tolerance and family data for allocation targets
- If `workspace/insurance-state.json` exists, check if emergency fund recommendation conflicts with insurance coverage

## Important Reminders

- Before doing anything, read the relevant SKILL.md and reference files for the sub-command
- After each interaction that captures or updates data, write to the state file immediately
- Be opinionated: every recommendation includes what to do, why, tax impact in EUR, and where to redirect
- English only. German terms with explanations in parentheses on first use
- Never fabricate financial data. If current prices are needed and unavailable, ask the user
