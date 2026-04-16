Route this command based on the argument provided.

**Argument received:** $ARGUMENTS

## Routing Rules

If no argument or "help":
→ Show the following help and stop:

```
/finz:profile — Financial identity manager
──────────────────────────────────────────

Sub-commands:
  setup               Interactive interview to build your profile from scratch
  update              Modify specific fields (natural language supported)
  show                Display current profile grouped by section
  status              Quick completeness check

Examples:
  /finz:profile setup
  /finz:profile update
  /finz:profile show
```

If "setup":
→ Read `skills/profile/SKILL.md` and begin the setup interview.
→ Check if `workspace/profile.json` already exists. If yes, show the user what's already been captured and ask if they want to update it or start fresh.
→ Check if `workspace/tax-state.json` exists with personal data. If yes, offer to migrate shared fields automatically (names, DOBs, tax IDs, employers, salary, children, address).
→ Walk through each section one question at a time: family status, personal details, tax details, employment, spouse (if applicable), children, address, risk context.
→ Save to `workspace/profile.json` after each answered question.

If "update":
→ Read `skills/profile/SKILL.md`.
→ Load `workspace/profile.json`. If it doesn't exist, tell the user to run `/finz:profile setup` first.
→ Ask the user what they want to change. Accept natural language (e.g., "my salary is now 115,000").
→ Show the current value, confirm the change, and save immediately.
→ If the change affects other skills (salary affects tax estimates, family status affects filing strategy, risk context affects insurance), mention it briefly.

If "show":
→ Read `skills/profile/SKILL.md`.
→ Load `workspace/profile.json`. If it doesn't exist, tell the user to run `/finz:profile setup` first.
→ Display the profile in a clean, human-readable format grouped by section: Personal, Employment, Family, Address, Risk Context.
→ Highlight any missing or incomplete fields.
→ Show the `last_updated` timestamp.

If "status":
→ Load `workspace/profile.json` and give a quick completeness check:
  - How many fields are filled vs. empty
  - Which sections are complete vs. need attention
  - When it was last updated
→ Don't modify any data, just report.

## State File

Always read from and write to `workspace/profile.json`. Create it if it doesn't exist. The structure follows the schema documented in `skills/profile/SKILL.md`.

## Important Reminders

- Before doing anything, read `skills/profile/SKILL.md` for the full skill definition.
- After each interaction that captures new data, write it to the profile file immediately — don't wait until the end.
- The conversation must always be done in English. Never change to German. If the user doesn't understand a concept, iterate to explain.
- Use German financial terms with brief explanations in parentheses when first introduced.
- Be warm and patient — one question at a time during setup.
- This is a financial identity, not a tax form. Keep the tone conversational and explain why each piece of data matters.
