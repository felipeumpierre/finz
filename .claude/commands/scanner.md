Route this command based on the argument provided.

**Argument received:** $ARGUMENTS

## Routing Rules

If no argument or "help":
→ Show available scanner sub-commands: `scan <folder>`, `status`, `corrections`.
→ Briefly explain what each does.

If "scan" followed by a folder path (e.g., "scan /path/to/documents" or "scan ~/Documents/steuer"):
→ Read `skills/scanner/SKILL.md`, `skills/scanner/references/classification-taxonomy.md`, and `skills/scanner/references/extraction-templates.md`.
→ Execute the full scanner flow: discover files, classify, present table for approval, extract approved files, write to state files.
→ The classify → approve → extract flow is NON-NEGOTIABLE. Never extract without user approval.
→ Check `workspace/document-registry.json` for past corrections before classifying (correction learning).
→ After extraction, update `workspace/document-registry.json` and the appropriate domain state files (`workspace/insurance-state.json`, `workspace/portfolio-state.json`, `workspace/tax-state.json`).

If "status":
→ Read `skills/scanner/SKILL.md`.
→ Load `workspace/document-registry.json`. If it doesn't exist, tell the user no scans have been performed yet.
→ Show: total files scanned, classification breakdown by category, last scan date, any files flagged as Unknown.
→ Don't modify any state, just report.

If "corrections":
→ Read `skills/scanner/SKILL.md` and `skills/scanner/references/classification-taxonomy.md`.
→ Load `workspace/document-registry.json`. If it doesn't exist, tell the user no scans have been performed yet.
→ Show all past corrections and current classifications.
→ Let the user review and update any classification.
→ Store new corrections in the registry for future learning.

## State Files

- **Document registry:** `workspace/document-registry.json` — tracks all scans, file classifications, and corrections.
- **Insurance state:** `workspace/insurance-state.json` — insurance policies extracted from scanned documents.
- **Portfolio state:** `workspace/portfolio-state.json` — investment data extracted from scanned documents.
- **Tax state:** `workspace/tax-state.json` — tax, income, and official document data. Follows the schema used by steuer-intake.

Create any state file if it doesn't exist. Never overwrite existing data — always merge.

## Important Reminders

- Before doing anything, read the relevant skill and reference files for the sub-command.
- The classification table and user approval are the GATE. Nothing gets extracted without explicit user confirmation.
- Confidence levels must be honest. Do not inflate "low" to "medium" or "medium" to "high".
- When the user corrects a classification, store the correction immediately for future learning.
- The conversation must always be done in English. Never change to German. Use German terms with explanations in parentheses when first introduced.
- After each extraction, write to the state files immediately — don't wait until the end.
