# finz — Personal Finance Toolkit for German Expats

A multi-domain personal finance toolkit built as Claude Code skills. Covers cash flow tracking, investment portfolio review, insurance auditing, tax filing, crypto tax, and cross-domain insights + advisory — all connected through a shared financial profile.

## Quick Start

1. **Set up your profile:** `/finz:profile setup` — builds your financial identity (one-time)
2. **Scan your documents:** `/finz:scan scan ~/path/to/folder` — classify and extract data from PDFs
3. **Get a dashboard:** `/finz:insights` — see your full financial picture
4. **Get recommendations:** `/finz:advisor` — ranked, actionable improvements
5. **Use any domain tool:** `/finz:cash`, `/finz:portfolio`, `/finz:insurance`, `/finz:steuer`, `/finz:crypto`

## Commands

| Command | What it does |
|---------|-------------|
| `/finz` | Master help — lists all domains |
| `/finz:profile` | Manage your financial identity (personal details, family, salary, risk context) |
| `/finz:scan` | Scan folders of documents — classify, approve, extract structured data |
| `/finz:cash` | Accounts, credit cards, expenses, cash-flow tracking |
| `/finz:portfolio` | Investment review — allocation, tax efficiency, fundamentals, sell/buy recommendations |
| `/finz:insurance` | Insurance audit — what you have, what you're missing, recommendations |
| `/finz:steuer` | German tax filing — ELSTER walkthrough, deductions, calculation |
| `/finz:crypto` | Crypto tax engine — ingest Binance/Coinbase/Crypto.com CSVs, FIFO accounting, §23 / §22 Nr.3 EStG |
| `/finz:insights` | Cross-domain dashboard — net worth, cash flow, emergency fund, SPB, tax readiness |
| `/finz:advisor` | Actionable recommendations — ranked by EUR impact. Proactive scan + goal-driven modes |

Invoke any domain bare (e.g. `/finz:cash`) to see its sub-commands.

### Advisor Examples

```
/finz:advisor
/finz:advisor "where can I free up 500/m to invest more?"
/finz:advisor "is my insurance coverage adequate?"
/finz:advisor "should I sell AAPL this year?"
```

## How It All Connects

```
NAS folders --> /finz:scan --> document-registry.json
                                |
                    +-----------+-----------+
                    |           |           |
              insurance-    portfolio-   tax-state.json
              state.json    state.json   (existing)
                    |           |           |
            /finz:insurance /finz:portfolio /finz:steuer
                    |           |           |
                    +-----------+-----------+
                                |
                          profile.json
                       (read by all skills)
                                |
          /finz:insights (dashboard) + /finz:advisor (actions)
```

**Cross-domain data flow:**

- `/finz:scan` feeds classified + extracted data into all domain state files
- `/finz:profile` provides personal details to all skills (no re-entering data)
- `/finz:portfolio tax-check` pre-fills Anlage KAP data for `/finz:steuer intake`
- `/finz:insurance audit` identifies premiums for Vorsorgeaufwand deduction in `/finz:steuer deductions`
- `/finz:advisor` reads all state files and ranks improvement opportunities across every domain

## Data Files

All state files live in `workspace/` (gitignored — contains personal data):

| File | Purpose | Written by |
|------|---------|------------|
| `profile.json` | Shared financial identity | `/finz:profile` |
| `tax-state.json` | Tax filing data | `/finz:steuer` |
| `insurance-state.json` | Insurance policies and audit results | `/finz:scan`, `/finz:insurance` |
| `portfolio-state.json` | Holdings, allocations, tax positions | `/finz:scan`, `/finz:portfolio` |
| `cash-state.json` | Accounts, credit cards, expenses, interest | `/finz:scan`, `/finz:cash` |
| `document-registry.json` | Scanned file classifications and corrections | `/finz:scan` |
| `crypto-ledger.json` | Full crypto transaction ledger (lots, disposals, income) | `/finz:crypto ingest` |
| `crypto-summary.json` | Crypto yearly tax summary and current holdings | `/finz:crypto ingest` |
| `crypto-decisions.json` | User decisions for ambiguous crypto transactions | `/finz:crypto resolve` |

## Design Principles

- **English only** — German financial terms are always explained in parentheses
- **Opinionated but transparent** — recommendations come with reasoning and real numbers
- **Show the math** — every recommendation traces back to your data
- **Your decision** — the tool has a point of view but you always make the call
- **No hidden logic** — reference files document all rules; skill logic is readable
- **Auto-capture where possible** — the system records progression without explicit user action

## Roadmap

- **v1.0** (current) — `finz` namespace, advisor skill, per-domain help
- **v1.1** — temporal layer: `history.json`, goals, staleness indicators, trend-aware advisor
- **v1.2** — event system: calendar + life event workflows
- **v1.3** — narrow cross-border extension: foreign real estate tracking

See `docs/superpowers/specs/2026-04-16-finz-architecture-design.md` for the full design.

## Disclaimer

This toolkit is NOT a Steuerberater (tax advisor) and cannot provide binding tax or financial advice. It helps organize information, identify opportunities, estimate positions, and prepare data. Always consult a qualified professional for complex situations.
