# finz — Personal Finance Toolkit for German Expats

A multi-domain personal finance toolkit packaged as a [Claude Code plugin](https://code.claude.com/docs/en/plugins.md). Covers cash flow tracking, investment portfolio review, insurance auditing, tax filing, crypto tax, and cross-domain insights + advisory — all connected through a shared financial profile.

## Vision

`finz` helps a German-resident expat family understand their complete financial picture — current state, historical trajectory, cross-domain optimization opportunities, and time-bound obligations — through a single set of Claude Code skills with a unified command namespace.

What the toolkit aims to achieve:

- **One mental model, many domains** — cash, investments, insurance, tax, and crypto all read from the same profile and write to shared state files, so nothing needs to be entered twice.
- **Recommendations, not just reports** — every domain can report current state; the advisor layer ranks actions by EUR impact across all domains.
- **Transparent math** — every recommendation traces back to the user's own data. No fabricated benchmarks.
- **Expat-first** — English conversation, German terms explained on first use, cross-border flags where they matter.
- **Local files only** — all state is plain JSON in `workspace/`. No databases, no cloud, user can inspect or hand-edit anything.

## Design Principles

- **English only** — German financial terms are always explained in parentheses on first use.
- **Opinionated but transparent** — recommendations come with reasoning and real EUR numbers.
- **Show the math** — every recommendation traces back to the user's data.
- **Your decision** — the tool has a point of view but the user always makes the call.
- **No hidden logic** — reference files document all rules; skill logic is readable markdown.
- **Auto-capture where possible** — material writes record progression without explicit user action.
- **Never invent information** — no fabricated names, numbers, or benchmarks. Ask when unsure.

## Install

`finz` is distributed as a Claude Code plugin via a GitHub-backed marketplace.

Inside Claude Code:

```
/plugin marketplace add felipeumpierre/finz
/plugin install finz@finz
```

Then restart Claude Code (or run `/reload-plugins`) and try:

```
/finz:help
```

To update later:

```
/plugin marketplace update finz
/plugin install finz@finz
```

To remove:

```
/plugin uninstall finz@finz
/plugin marketplace remove finz
```

See the official docs: [Claude Code plugins](https://code.claude.com/docs/en/plugins.md) · [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces.md).

## Quick Start

1. **Set up your profile:** `/finz:profile setup` — builds your financial identity (one-time)
2. **Scan your documents:** `/finz:scan scan ~/path/to/folder` — classify and extract data from PDFs
3. **Get a dashboard:** `/finz:insights` — see your full financial picture
4. **Get recommendations:** `/finz:advisor` — ranked, actionable improvements
5. **Use any domain tool:** `/finz:cash`, `/finz:portfolio`, `/finz:insurance`, `/finz:steuer`, `/finz:crypto`

## Architecture

```
NAS folders --> /finz:scan --> document-registry.json
                                |
                    +-----------+-----------+
                    |           |           |
              insurance-    portfolio-   tax-state.json
              state.json    state.json   + cash-state.json
                    |           |           |
            /finz:insurance /finz:portfolio /finz:steuer /finz:cash /finz:crypto
                    |           |           |
                    +-----------+-----------+
                                |
                          profile.json
                       (read by all skills)
                                |
          /finz:insights (dashboard) + /finz:advisor (actions)
```

**Cross-domain data flow:**

- `/finz:scan` feeds classified + extracted data into all domain state files.
- `/finz:profile` provides personal details to all skills (no re-entering data).
- `/finz:portfolio tax-check` pre-fills Anlage KAP data for `/finz:steuer intake`.
- `/finz:insurance audit` identifies premiums for Vorsorgeaufwand deduction in `/finz:steuer deductions`.
- `/finz:cash interest` writes bank interest to `tax-state.json` for Anlage KAP.
- `/finz:advisor` reads all state files and ranks improvement opportunities across every domain (read-only).

## Commands

Top-level domains. Invoke any domain bare (e.g. `/finz:cash`) to see its sub-commands. Run `/finz:help` for the master index.

| Command | What it does |
|---------|-------------|
| `/finz:help` | Master help — lists all domains |
| `/finz:profile` | Manage your financial identity (personal details, family, salary, risk context) |
| `/finz:scan` | Scan folders of documents — classify, approve, extract structured data |
| `/finz:cash` | Accounts, credit cards, expenses, cash-flow tracking |
| `/finz:portfolio` | Investment review — allocation, tax efficiency, fundamentals, sell/buy recommendations |
| `/finz:insurance` | Insurance audit — what you have, what you're missing, recommendations |
| `/finz:steuer` | German tax filing — ELSTER walkthrough, deductions, calculation |
| `/finz:crypto` | Crypto tax engine — ingest Binance/Coinbase/Crypto.com CSVs, FIFO accounting, §23 / §22 Nr.3 EStG |
| `/finz:insights` | Cross-domain dashboard — net worth, cash flow, emergency fund, SPB, tax readiness |
| `/finz:advisor` | Actionable recommendations — ranked by EUR impact. Proactive scan + goal-driven modes |

### Sub-commands

#### `/finz:profile`

| Sub-command | Purpose |
|-------------|---------|
| `setup` | Interactive interview to build your profile from scratch |
| `update` | Modify specific fields (natural language supported, e.g. "my salary is now 115,000") |
| `show` | Display current profile grouped by section |
| `status` | Quick completeness check |

#### `/finz:scan`

| Sub-command | Purpose |
|-------------|---------|
| `scan <folder>` | Read, classify, approve, then extract into state files |
| `status` | Show what has been scanned so far |
| `corrections` | Review and correct past classifications (correction learning) |

#### `/finz:cash`

| Sub-command | Purpose |
|-------------|---------|
| `status` | Account overview with idle-cash alerts |
| `expenses [month]` | Categorized spending with month-over-month comparison |
| `interest [year]` | Interest earned, SPB usage, opportunity cost |
| `scan <folder>` | Scan banking documents, categorize, extract |
| `summary` | Structured JSON output for `/finz:insights` |

#### `/finz:portfolio`

| Sub-command | Purpose |
|-------------|---------|
| `review` | Full analysis: allocation, tax efficiency, fundamentals |
| `scan <folder>` | Scan folder for investment docs, then review |
| `tax-check` | Investment tax optimization (SPB, Teilfreistellung, losses) |
| `status` | Quick holdings summary |
| `summary` | Structured JSON output for `/finz:insights` |

#### `/finz:insurance`

| Sub-command | Purpose |
|-------------|---------|
| `audit` | Full gap analysis across 10 insurance types |
| `scan <folder>` | Scan folder for insurance docs, then audit |
| `status` | Current coverage summary (no analysis) |
| `summary` | Structured JSON output for `/finz:insights` |

#### `/finz:steuer`

| Sub-command | Purpose |
|-------------|---------|
| `start` | Begin full guided workflow from Phase 1 |
| `intake` | Extract data from Lohnsteuerbescheinigungen |
| `deductions` | Interactive deduction interview |
| `documents` | Generate personalized document checklist |
| `calculate` | Estimate tax liability, compare filing strategies (Zusammen- vs. Einzelveranlagung, Günstigerprüfung) |
| `filing` | Step-by-step ELSTER form guide (resumable) |
| `crypto` | Route to crypto tax export (Anlage SO, Nacherklärung) |
| `status` | Show progress so far |
| `summary` | Generate comprehensive summary document |

#### `/finz:crypto`

| Sub-command | Purpose |
|-------------|---------|
| `ingest` | Parse Binance / Coinbase / Crypto.com CSVs, run FIFO |
| `resolve` | Walk through open issues, record decisions |
| `review` | Full ledger review: holdings, disposals, income |
| `optimize` | Tax-free milestones, loss-harvesting opportunities |
| `tax [--year YYYY]` | Per-year §23 / §22 Nr.3 drill-down |
| `status` | Last ingest stats, open issues, holdings summary |
| `export --year YYYY` | Generate Steuerberater export package |

#### `/finz:insights`

Single command with no sub-commands — always runs the full cockpit (net worth, cash flow, emergency fund, SPB, tax readiness, priority actions).

#### `/finz:advisor`

| Mode | Purpose |
|------|---------|
| (no argument) | Proactive scan — ranks non-obvious improvements by EUR impact (5–7 max) |
| `"<question>"` | Goal-driven — answers a specific free-form question with real numbers |

Examples:

```
/finz:advisor
/finz:advisor "where can I free up 500/m to invest more?"
/finz:advisor "is my insurance coverage adequate?"
/finz:advisor "should I sell AAPL this year?"
```

## Data Files

All state files live in `workspace/` (gitignored — contains personal data):

| File | Purpose | Written by |
|------|---------|------------|
| `profile.json` | Shared financial identity | `/finz:profile` |
| `tax-state.json` | Tax filing data | `/finz:steuer`, `/finz:portfolio tax-check`, `/finz:cash interest` |
| `insurance-state.json` | Insurance policies and audit results | `/finz:scan`, `/finz:insurance` |
| `portfolio-state.json` | Holdings, allocations, tax positions | `/finz:scan`, `/finz:portfolio` |
| `cash-state.json` | Accounts, credit cards, expenses, interest | `/finz:scan`, `/finz:cash` |
| `document-registry.json` | Scanned file classifications and corrections | `/finz:scan` |
| `crypto-ledger.json` | Full crypto transaction ledger (lots, disposals, income) | `/finz:crypto ingest` |
| `crypto-summary.json` | Crypto yearly tax summary and current holdings | `/finz:crypto ingest` |
| `crypto-decisions.json` | User decisions for ambiguous crypto transactions | `/finz:crypto resolve` |

## Repo Layout

```
finz/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # single-plugin marketplace definition
├── commands/                # slash commands → /finz:<name>
│   ├── help.md              # /finz:help
│   ├── profile.md           # /finz:profile
│   └── ...
├── skills/                  # domain skills invoked by commands
│   ├── profile/SKILL.md
│   ├── crypto/SKILL.md
│   └── ...
├── agents/                  # background agents
│   └── steuer-agent.md
├── workspace/               # [gitignored] personal state files
├── README.md
└── LICENSE
```

## Developing the Plugin

To work on `finz` itself (or fork it), clone the repo and point Claude Code at your working copy:

```bash
git clone https://github.com/felipeumpierre/finz.git
cd finz
claude --plugin-dir .
```

`--plugin-dir .` loads the plugin live from the current directory — no install, no cache. Edits to `commands/`, `skills/`, or `agents/` are picked up by running:

```
/reload-plugins
```

inside the Claude Code session. This reloads commands, skills, agents, and hooks without a restart.

To publish a new version:

1. Bump `version` in `.claude-plugin/plugin.json`.
2. Commit and push to `main`.
3. Users get it via `/plugin marketplace update finz` + `/plugin install finz@finz`.

## Roadmap

### v1.0 — Foundation + Advisor (current)

- `finz` namespace, packaged as a Claude Code plugin
- `/finz:advisor` proactive + goal-driven modes on current state
- Per-domain help when invoked bare
- PII sanitization and `.gitignore` hardening

### v1.1 — Temporal layer

- `workspace/history.json` — append-only monthly snapshots, auto-captured after any material write
- `workspace/goals.json` + `/finz:advisor goals show | add | update | remove`
- Staleness indicators in `/finz:insights` and `/finz:advisor` (>90 days flagged)
- Trend-aware advisor: pace tracking against goals, projected completion dates

### v1.2 — Event system

- `skills/finz/references/german-finance-calendar.md` — built-in German tax/finance cycles (Vorabpauschale, deadlines, SPB window, etc.)
- `workspace/calendar.json` + new `/finz:calendar` command (`show`, `year`, `add`, `remove`)
- Auto-population hooks: `/finz:scan` on Steuerbescheid → Einspruch window, `/finz:crypto` → tax-free milestones, goals → target dates
- `/finz:life-event <name>` with templates for baby, job change, marriage, divorce, relocation, property purchase, inheritance
- `/finz:advisor` and `/finz:insights` surface within-30-day calendar items

### v1.3 — Narrow cross-border extension

- `profile.foreign_real_estate[]` — track foreign property (Brazil-first)
- `cash-state.json` `account.currency` field + `installment_payments_abroad` category
- Auto-calendar entries for §23 EStG 10-year clock, IPTU reminders, payoff dates
- Advisor cross-border flags (e.g. "Brazilian apartment sold before X would trigger §23 gains in Germany")

Explicit non-goals: no Brazilian tax computation, no DBA computation, no multi-jurisdiction tax residency tracking. Scope stays narrow on purpose.

## License

[MIT](./LICENSE) — free to use, modify, and share.

## Disclaimer

This toolkit is NOT a Steuerberater (tax advisor) and cannot provide binding tax or financial advice. It helps organize information, identify opportunities, estimate positions, and prepare data. Always consult a qualified professional for complex situations.
