Route this command based on the argument provided.

**Argument received:** $ARGUMENTS

## Routing Rules

If no argument or "audit":
→ Read `skills/insurance/SKILL.md` and the three reference files in `skills/insurance/references/`.
→ Begin the full gap analysis workflow.
→ Read `workspace/profile.json` for the user's financial profile (salary, family, risk context).
→ Read `workspace/insurance-state.json` for existing policies. If it doesn't exist, offer to interview the user or suggest running `/scanner`.
→ Run the gap analysis across all 10 insurance types, produce the coverage matrix, detailed recommendations, and priority action list.
→ Save results to `workspace/insurance-state.json`.

If "scan" (with a folder path argument):
→ Read `skills/insurance/SKILL.md`.
→ Tell the user you'll scan their insurance documents first, then run the audit.
→ Run `/scanner` on the specified folder, filtering for insurance-related documents.
→ Extract policy information into `workspace/insurance-state.json`.
→ Then automatically proceed to the full audit workflow above.

If "status":
→ Read `skills/insurance/SKILL.md`.
→ Load `workspace/insurance-state.json`. If it doesn't exist, tell the user to run `/insurance audit` first.
→ Show a quick summary: number of active policies, coverage by type, total annual spend, date of last audit, any unresolved gaps.
→ Don't modify any data, just report.

If "summary":
→ Read `skills/insurance/SKILL.md`.
→ Load `workspace/insurance-state.json`. If it does not exist or has no policies, return a structured summary indicating no data is available — do not prompt the user or ask questions.
→ Return structured data for `/insights`:
  - Number of active policies (count of policies where status is not "cancelled" or "expired")
  - Total annual premiums (sum of annual_premium across all active policies)
  - Gap status from last audit (if audit_results exists: number of gaps, severity of the worst gap; otherwise "no audit run")
  - Tax-deductible premiums total (sum of annual_premium for policy types that qualify as Vorsorgeaufwendungen: krankenversicherung, pflegeversicherung, berufsunfaehigkeitsversicherung, risikolebensversicherung, unfallversicherung, haftpflichtversicherung)
→ Do NOT run any analysis, generate recommendations, or modify any data.

## State File

Always read from and write to `workspace/insurance-state.json`. Create it if it doesn't exist. The structure follows the schema documented in `skills/insurance/SKILL.md`.

## Important Reminders

- Before doing anything, read `skills/insurance/SKILL.md` and the reference files for the operation you're performing.
- After each interaction that captures new data, write it to the state file immediately — don't wait until the end.
- The conversation must always be done in English. Never change to German.
- Use German insurance terms with brief explanations in parentheses when first introduced.
- Be OPINIONATED. Every recommendation must include a clear stance backed by numbers and reasoning.
- Show the math. Real EUR amounts, real monthly costs, real tax impacts.
- Respect the user's intelligence — explain the WHY, not just the WHAT.
- Always the user's decision. Present recommendations clearly, but never pressure.
