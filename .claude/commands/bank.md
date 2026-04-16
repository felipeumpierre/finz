Route this bank command based on the argument provided.

**Argument received:** $ARGUMENTS

## Routing Rules

If no argument or "status":
→ Read `skills/bank/SKILL.md`.
→ Load `workspace/bank-state.json`. If it doesn't exist, tell the user no banking data has been captured yet and suggest running `/bank scan <folder>` or providing account details.
→ Display all accounts grouped by owner with balances, interest rates, and status badges.
→ Compute total cash across all active accounts.
→ Flag idle cash earning 0% with EUR opportunity cost at the best rate available across the user's own accounts.

If "expenses" (with optional month argument, e.g., "expenses jan 2026" or "expenses"):
→ Read `skills/bank/SKILL.md`.
→ Parse the month from the argument, or default to the most recent month with data.
→ Load `workspace/bank-state.json`. If it doesn't exist, tell the user no data has been captured yet.
→ Combine spending from all Girokonto monthly_summaries and linked credit card statements for the target month.
→ Exclude `kreditkarte` and `ueberweisungen_intern` from expense totals.
→ Show the category breakdown table with month-over-month comparison.
→ Compute and display savings rate.
→ If `sonstiges` exceeds 10% of total expenses, proactively offer to walk through uncategorized items and store corrections.

If "interest" (with optional year argument, e.g., "interest 2025" or "interest"):
→ Read `skills/bank/SKILL.md`.
→ Load `workspace/bank-state.json`. If it doesn't exist, tell the user no data has been captured yet.
→ Default to the current calendar year if no year is specified.
→ Show interest earned per account with tax withheld.
→ Load `workspace/portfolio-state.json` if it exists to compute combined Sparerpauschbetrag (SPB) usage.
→ Calculate opportunity cost for accounts earning 0%.
→ Update `workspace/tax-state.json` with bank interest data for Anlage KAP if interest was earned.

If "scan" followed by a folder path (e.g., "scan ~/Documents/bank"):
→ Read `skills/bank/SKILL.md` and `skills/scanner/SKILL.md`.
→ Read `skills/bank/references/expense-categories.md` for categorization patterns.
→ Run the scanner on the specified folder, filtering for banking documents:
  - Kontoauszug (bank statements)
  - Zinsbescheinigung (interest certificates)
  - Kreditkartenabrechnung (credit card statements)
  - Kontoabschluss (account closing statements)
  - Tagesgeld-Auszug (savings account statements)
→ For each banking document, run the categorize-rollup-present-correct flow:
  1. Read all transactions (date, Verwendungszweck, amount, debit/credit)
  2. Categorize each transaction using the priority order: own-IBAN match → credit card payment → learned patterns → insurance providers → predefined patterns → sonstiges
  3. Roll up into monthly category totals
  4. Present the categorized summary with uncategorized items listed
  5. Prompt the user to correct uncategorized items; store each correction as a learned pattern
→ Write all extracted data to `workspace/bank-state.json`.
→ After extraction, automatically run the `status` workflow.

If "summary":
→ Read `skills/bank/SKILL.md`.
→ Load `workspace/bank-state.json`. If it doesn't exist, return a JSON object with `data_missing: true` and zero values.
→ Compute: total_cash, accounts_by_owner, monthly_cash_flow (most recent month), avg_monthly_cash_flow (last 3 months), interest_ytd, interest_annual_projected, opportunity_cost_annual, spb_used_from_interest.
→ Output the structured JSON only — no formatted report. This output is consumed by `/insights`.

## State File

Always read from and write to `workspace/bank-state.json`. Create it if it doesn't exist on first data capture.

When running `interest`, also update `workspace/tax-state.json` with:
- `capital_income.bank_interest_received`
- `capital_income.bank_ket_withheld`

## Cross-Domain Integration

- After `interest`, remind the user that this data feeds into `/steuer intake` for Anlage KAP if interest was earned at a foreign bank without German withholding.
- If `workspace/profile.json` exists, use it for family context (joint SPB calculation for married couples vs. single allowance).
- If `workspace/insurance-state.json` exists, load provider names to auto-classify insurance premium transactions during scan.
- `/bank summary` data feeds into `/insights` for the full financial cockpit.

## Important Reminders

- Before doing anything, read `skills/bank/SKILL.md` for the sub-command being executed.
- For any transaction categorization, always read `skills/bank/references/expense-categories.md` first.
- After each interaction that captures or updates data, write to `workspace/bank-state.json` immediately.
- English only. German banking terms with explanations in parentheses on first use.
- Be opinionated about idle cash. Every 0% balance with a better option gets called out with the EUR/year opportunity cost.
- Show the math. Savings rates with real EUR numbers. SPB usage in EUR with remaining allowance shown.
- Never fabricate balances or transaction data. If data is missing, say so and ask the user.
- Corrections to categories are stored as learned patterns — always confirm the pattern saved and how many transactions were updated.
