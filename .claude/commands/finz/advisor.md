Route this advisor command based on the argument provided.

**Argument received:** $ARGUMENTS

## Routing Rules

If no argument:
→ Read `skills/advisor/SKILL.md` and execute Mode 1 (Proactive scan).
→ Load all available state files in parallel (profile, cash-state, portfolio-state, insurance-state, tax-state, crypto-summary).
→ Apply the 8 heuristics defined in the skill, compute EUR impact for each, and output the top 5–7 sorted descending.
→ Include a data-freshness note at the bottom.

If the argument is "help":
→ Show the following help and stop:

```
/finz:advisor — Cross-domain financial recommendations
──────────────────────────────────────────────────────

Modes:
  (no argument)           Proactive scan — finds non-obvious
                          improvements, ranks by EUR impact
  "<question>"            Goal-driven — answers a specific
                          free-form question with real numbers

Examples:
  /finz:advisor
  /finz:advisor "where can I free up 500/m to invest more?"
  /finz:advisor "is my insurance coverage adequate?"
  /finz:advisor "should I sell AAPL this year?"
```

For any other argument (including quoted strings, natural-language questions, or raw words):
→ Read `skills/advisor/SKILL.md` and execute Mode 2 (Goal-driven).
→ Treat the full $ARGUMENTS as the user's question.
→ Interpret the question, identify relevant state files, produce a focused analysis per the skill's output principles.

## State Files Read (not modified)

The advisor is read-only — it never writes to any state file. It consumes:
- `workspace/profile.json`
- `workspace/cash-state.json`
- `workspace/portfolio-state.json`
- `workspace/insurance-state.json`
- `workspace/tax-state.json`
- `workspace/crypto-summary.json`

If a file is missing, the advisor skips heuristics that depend on it and notes so in the output.

## Important Reminders

- Before doing anything, read `skills/advisor/SKILL.md` for the full heuristic definitions and output format.
- Every recommendation MUST include a EUR number and a next-action `/finz:*` command.
- Maximum 5–7 recommendations in proactive mode. Quality over quantity.
- Never fabricate numbers. If data is missing for a heuristic, skip it and note at the bottom.
- English only. German terms with parenthetical explanations on first use.
- The advisor is strictly read-only. Do not modify any state file.
