---
description: German crypto tax ingestion, analysis, and Steuerberater export. Routes to /finz:crypto subcommands.
---

Route this crypto command based on the argument provided.

**Argument received:** $ARGUMENTS

## Routing Rules

If no argument or "help":
→ Show the following help and stop:

```
/finz:crypto — German crypto tax engine
───────────────────────────────────────

Sub-commands:
  ingest              Parse Binance / Coinbase / Crypto.com CSVs, run FIFO
  resolve             Walk through open issues, record decisions
  review              Full ledger review: holdings, disposals, income
  optimize            Tax-free milestones, loss-harvesting opportunities
  tax [--year YYYY]   Per-year §23 / §22 Nr.3 drill-down
  status              Last ingest stats, open issues, holdings summary
  export --year YYYY  Generate Steuerberater export package

Examples:
  /finz:crypto ingest
  /finz:crypto tax --year 2024
  /finz:crypto export --year 2024
```

For any other argument, read `skills/crypto/SKILL.md` and execute the subcommand matching $ARGUMENTS:

- `ingest` → Ingest section
- `resolve` → Resolve section
- `review` → Review section
- `optimize` → Optimize section
- `tax` (with optional --year) → Per-year tax drill-down
- `status` → Status section
- `export --year YYYY` → Export Steuerberater package

Arguments: $ARGUMENTS
