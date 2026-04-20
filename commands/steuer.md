Route this tax declaration command based on the argument provided.

**Argument received:** $ARGUMENTS

If no argument or "help":
→ Show the following help block and stop:

```
/finz:steuer — German tax filing workflow
─────────────────────────────────────────

Sub-commands:
  start               Begin full guided workflow from Phase 1
  intake              Extract data from Lohnsteuerbescheinigungen
  deductions          Interactive deduction interview
  documents           Generate personalized document checklist
  calculate           Estimate tax liability, compare filing strategies
  filing              Step-by-step ELSTER form guide
  crypto              Route to crypto tax export
  status              Show progress so far
  summary             Generate comprehensive summary

Examples:
  /finz:steuer start
  /finz:steuer intake
  /finz:steuer calculate
  /finz:steuer status
```

## Routing Rules

If "start":
→ Read `skills/steuer-orchestrator/SKILL.md` and begin the full guided workflow from Phase 1.
→ Check if `workspace/tax-state.json` exists. If yes, show the user what's already been captured and ask if they want to continue or start fresh.
→ If starting fresh, create the workspace directory structure and initialize an empty state file.

If "intake":
→ Read `skills/steuer-intake/SKILL.md`.
→ Ask the user to provide their Lohnsteuerbescheinigung(en) — they can paste text, provide a file path, or describe the data.
→ Extract the data, validate it, and save to `workspace/tax-state.json`.
→ After intake, ask if they want to continue to deductions or stop here.

If "deductions":
→ Read `skills/steuer-deductions/SKILL.md` and also `skills/steuer-deductions/references/commonly-missed-deductions.md`.
→ Check `workspace/tax-state.json` for existing income data. If none, warn that intake should be done first (but don't block — the user might want to explore deductions generally).
→ Conduct the interactive deduction interview, one category at a time.
→ Save all captured deductions to `workspace/tax-state.json`.

If "documents":
→ Read `skills/steuer-documents/SKILL.md`.
→ Load `workspace/tax-state.json` to see what income and deductions have been identified.
→ Generate a personalized document checklist based on the user's specific situation.
→ Save the checklist to `workspace/output/document-checklist.md`.

If "calculate":
→ Read `skills/steuer-calculator/SKILL.md`.
→ Load `workspace/tax-state.json`. If income data is missing, tell the user they need to do intake first.
→ Run the full tax estimation: compute zvE, apply Splitting, compare Zusammenveranlagung vs. Einzelveranlagung, run Günstigerprüfung for Kindergeld vs. Kinderfreibetrag.
→ Save results to `workspace/tax-state.json` and produce a summary at `workspace/output/tax-summary.md`.

If "filing" or "fill" or "elster":
→ Read `skills/steuer-filing/SKILL.md`.
→ Load `workspace/tax-state.json`. If income data is missing, tell the user to run intake first.
→ Check if `filing.status === "in_progress"` — if yes, resume from where the user left off.
→ Walk the user through each ELSTER form step-by-step, one section at a time.
→ After each form is confirmed complete, update `filing.forms_completed` in the state file.
→ At the end, show the completion checklist and pre-submission reminders.

If "status":
→ Load `workspace/tax-state.json` and present a clear overview of:
  - What phases have been completed
  - Key numbers captured so far (income, total deductions, estimated refund if calculated)
  - What's still missing or recommended to do next
→ Don't modify any state, just report.

If "summary":
→ Load `workspace/tax-state.json` and generate a comprehensive summary document.
→ Save to `workspace/output/full-summary.md`.
→ This should be a document the user could print and bring to a Steuerberater, or use as a reference while filing in ELSTER.

## State File

Always read from and write to `workspace/tax-state.json`. Create it if it doesn't exist. The structure should follow this schema:

```json
{
  "tax_year": null,
  "last_updated": "ISO timestamp",
  "phases_completed": [],
  "filing_status": null,
  "persons": [],
  "children": [],
  "deductions": {
    "werbungskosten": {},
    "sonderausgaben": {},
    "aussergewoehnliche_belastungen": {},
    "haushaltsnahe": {},
    "handwerker": {}
  },
  "documents": {
    "checklist": [],
    "collected": [],
    "missing": []
  },
  "calculation": null
}
```

If "crypto":
→ Read `skills/steuer-crypto/SKILL.md`.
→ Load `workspace/crypto-summary.json` if it exists.
→ If it doesn't exist, tell the user to run `/finz:crypto ingest` first.
→ Route to the steuer-crypto sub-skill for Anlage SO line mapping, export, or Nacherklärung.

## Important Reminders

- Before doing anything, read the relevant SKILL.md file(s) for the phase you're entering.
- After each interaction that captures new data, write it to the state file immediately — don't wait until the end.
- If the user provides information out of order (e.g., mentions a deduction during intake), capture it and save it to the right place in the state.
- Be flexible: the user should be able to jump around, revisit phases, and add information incrementally.
- The conversation must always be done in english. Never change to German. If the user doesn't understand a concept, iterate over to explain.
