---
description: German crypto tax ingestion, analysis, and Steuerberater export. Routes to /crypto subcommands.
---

Route this crypto command based on the argument provided.

Read `.claude/skills/crypto/SKILL.md` and execute the subcommand matching $ARGUMENTS:

- `(none)` or `help` → Help section
- `ingest` → Ingest section
- `resolve` → Resolve section
- `review` → Review section
- `optimize` → Optimize section
- `tax` (with optional --year) → Per-year tax drill-down
- `status` → Status section
- `export --year YYYY` → Export Steuerberater package

Arguments: $ARGUMENTS
