---
description: finz — personal finance toolkit for German expats. Master help.
---

Show the full finz command tree and a one-line purpose per domain.

**Argument received:** $ARGUMENTS

If $ARGUMENTS is non-empty and is a domain name (profile, scan, cash, portfolio, insurance, steuer, crypto, insights, advisor), tell the user to invoke `/finz:<name>` directly (e.g., `/finz:cash`). Do not attempt to route.

Otherwise, display the master help below verbatim:

```
FINZ — Personal Finance Toolkit for German Expats
═══════════════════════════════════════════════════

/finz:profile       setup · update · show · status
/finz:scan          scan <folder> · status · corrections
/finz:cash          status · expenses [month] · interest [year] · scan <folder> · summary
/finz:steuer        start · intake · deductions · documents · calculate · filing · crypto · status · summary
/finz:portfolio     review · scan <folder> · tax-check · status · summary
/finz:insurance     audit · scan <folder> · status · summary
/finz:crypto        ingest · resolve · review · optimize · tax [--year] · status · export --year
/finz:insights      (no subcommands — runs full cockpit)
/finz:advisor       (proactive scan) · "<free-form question>" (goal-driven)

Use /finz:<domain> with no argument to see its subcommands.
```

Then, if the user hasn't used the toolkit before, suggest: `Run /finz:profile setup to get started, then /finz:scan <folder> to import your documents.`
