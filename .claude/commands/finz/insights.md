Read `skills/insights/SKILL.md`, then execute the full financial cockpit workflow.

**Arguments received:** $ARGUMENTS

## What to do

`/finz:insights` is a single command with no sub-commands. Ignore any arguments — always run the full cockpit.

## Execution Steps

1. Read `skills/insights/SKILL.md` for the complete workflow and output format.

2. Load all state files in parallel:
   - `workspace/profile.json`
   - `workspace/cash-state.json`
   - `workspace/portfolio-state.json`
   - `workspace/insurance-state.json`
   - `workspace/tax-state.json`

3. Compute all cross-domain figures as specified in SKILL.md:
   - Net worth (cash + investments + pension)
   - Monthly cash flow (avg last 3 months from cash-state)
   - Emergency fund coverage (liquid cash / avg monthly expenses)
   - Interest earned YTD + idle cash opportunity cost
   - Total Sparerpauschbetrag usage (bank interest + portfolio SPB)
   - Tax readiness checklist (data completeness across all state files)

4. Render the cockpit in the exact format defined in SKILL.md.

5. List priority cross-domain actions (max 5, most important first).

6. End with a next-steps prompt. Refer the user to any of the following for deeper analysis:
   - `/finz:cash` — accounts, expenses, interest
   - `/finz:portfolio` — investment review and tax efficiency
   - `/finz:insurance` — coverage audit
   - `/finz:steuer` — tax filing workflow
   - `/finz:advisor` — ranked cross-domain recommendations

## Missing Data Handling

- If a state file does not exist: show the section with a `[NO DATA]` notice and which command to run.
- If a state file exists but fields are null or missing: show what is available, mark the rest as unavailable.
- Never skip a section because data is missing — always show the header.

## Important Reminders

- Read `skills/insights/SKILL.md` before doing anything else.
- `/finz:insights` produces a single, complete response — no back-and-forth.
- Do not run deep domain analysis — the cockpit is a summary view. Refer the user to the domain commands or `/finz:advisor` for depth.
- Never fabricate numbers. Show real data or explicit "no data" notices.
- English only. German terms with brief explanations in parentheses on first use.
