# finz — Personal Finance Toolkit Architecture

**Date:** 2026-04-16
**Status:** Design approved — ready for implementation planning
**Scope:** Architectural redesign from `steuer` (tax-focused) to `finz` (holistic personal finance toolkit for German expats)

## Context

The existing project started as a German tax filing assistant (`steuer`) and accreted additional domains organically: banking, portfolio, insurance, crypto, document scanning, and cross-domain insights. The command surface is flat (`/bank`, `/portfolio`, `/steuer`, ...), and each domain reports current state but does not recommend actions, track progress over time, or surface time-sensitive obligations.

This design rebrands the project as `finz`, consolidates commands under a namespace, and adds a holistic advisor layer on top of temporal history, goal tracking, calendar events, and a narrow cross-border capability.

## Vision

`finz` helps a German-resident expat family understand their complete financial picture — current state, historical trajectory, cross-domain optimization opportunities, and time-bound obligations — through a single set of Claude Code skills with a unified command namespace.

Design principles:
- **Opinionated but transparent** — every recommendation includes a EUR figure and a traceable reason
- **Local files, plain JSON** — no databases in v1; users can inspect and hand-edit any state
- **Auto-capture where possible** — the system records progression without explicit user action
- **English primary, German terms explained** — target audience is expats

## Command Namespace

All commands move under the `finz:` namespace. Old commands (`/bank`, `/steuer`, etc.) are removed.

| New command | Replaces | Domain |
|-------------|----------|--------|
| `/finz` | — | Master help / overview |
| `/finz:profile` | `/profile` | Financial identity |
| `/finz:scan` | `/scanner` | Document intelligence |
| `/finz:cash` | `/bank` | Accounts + cards + expenses + cash flow |
| `/finz:portfolio` | `/portfolio` | Investments |
| `/finz:insurance` | `/insurance` | Coverage audit |
| `/finz:steuer` | `/steuer` | German tax filing |
| `/finz:crypto` | `/crypto` | Crypto tax engine |
| `/finz:insights` | `/insights` | Cross-domain dashboard |
| `/finz:advisor` | *(new, v1.0)* | Recommendations engine |
| `/finz:calendar` | *(new, v1.2)* | Time-based events |
| `/finz:life-event` | *(new, v1.2)* | Life-event workflows |

Each command shows a help section (listing subcommands) when invoked with no arguments. `/finz` with no arguments shows the full command tree.

File layout:
```
.claude/commands/finz.md                 → master help
.claude/commands/finz/
  profile.md
  scan.md
  cash.md
  portfolio.md
  insurance.md
  steuer.md
  crypto.md
  insights.md
  advisor.md
  calendar.md          (v1.2)
  life-event.md        (v1.2)
```

### Rename rationale

- **`/bank` → `/finz:cash`** — the domain already tracks credit cards, expense categorization, cash flow, and interest income. "Cash" better describes the liquidity/flow focus and pairs naturally with `portfolio` (invested), `insurance` (protected), `steuer` (owed), `crypto` (volatile).
- **`/scanner` → `/finz:scan`** — shorter, fits the namespace pattern. Pure stylistic rename.

## New Skill: `/finz:advisor`

The advisor is the system's recommendations engine. It reads all state files and produces actionable guidance ranked by EUR impact.

Two modes:

**1. Proactive scan** — invoked bare (`/finz:advisor`). Scans all domains for non-obvious improvements and ranks them by EUR impact. Examples of what it catches:
- Idle cash in 0% accounts vs available Tagesgeld rates across the user's own accounts
- Unused Sparerpauschbetrag allowance mid-year (use-it-or-lose-it)
- Concentration risk, tax-inefficient holdings (no Teilfreistellung where it could apply)
- Insurance gaps relative to profile
- Uncategorized expenses hiding patterns (large `sonstiges` bucket)
- Foreign broker income needing Anlage KAP
- Goal pacing gaps *(v1.1+)*
- Calendar items within a 30-day horizon *(v1.2+)*
- Cross-border flags for foreign real estate *(v1.3+)*

**2. Goal-driven** — invoked with a free-form question:
```
/finz:advisor "I want to invest 500/m more — where should it come from?"
```
The skill interprets the question, pulls relevant data across domains, and produces an analysis with a concrete action plan.

### Output principles

- Every recommendation includes a EUR number (benefit, cost, or gap)
- Every recommendation includes a next action (usually another `/finz:*` command)
- Data staleness is surfaced — if a state file is >90 days old, recommendations based on it carry a "based on data from X" caveat
- Maximum 5–7 recommendations per scan (quality over quantity)

### Subcommand for goals (v1.1)

Goal management is exposed through the advisor rather than a separate top-level command:

- `/finz:advisor goals show`
- `/finz:advisor goals add <name> <target_eur> <target_date>`
- `/finz:advisor goals update <id> ...`
- `/finz:advisor goals remove <id>`

## Temporal Layer (v1.1)

### `workspace/history.json`

Append-only monthly snapshots. Auto-captured by any skill that writes material state.

Schema:
```json
{
  "snapshots": [
    {
      "month": "2026-02",
      "sealed": true,
      "last_updated": "2026-02-28T14:32:00Z",
      "net_worth": {
        "total": 145000,
        "cash": 15470,
        "investments": 125530,
        "pension": 0,
        "foreign_real_estate": 0
      },
      "cash_flow": {
        "income": 4500,
        "expenses": 3550,
        "savings": 950,
        "savings_rate_pct": 21.1
      },
      "portfolio_allocation": {"equities": 78, "bonds": 5, "cash": 15, "other": 2},
      "spb_used": 200,
      "contributors": ["portfolio_scan", "cash_scan"],
      "missing": []
    },
    {
      "month": "2026-03",
      "sealed": false,
      "last_updated": "2026-03-14T09:10:00Z",
      "contributors": ["cash_scan"],
      "missing": ["portfolio"]
    }
  ]
}
```

### Auto-capture mechanism

- **Material update** = new balance, new position, new premium, new disposal/income event. **NOT** material: category corrections, classification overrides, notes, schema migrations.
- After any skill writes material state, it also appends or updates the current month's entry in `history.json`.
- When the calendar rolls to a new month, the previous month's entry is automatically sealed on the next invocation (`sealed: true`).
- `contributors[]` tracks which skills wrote to this month. `missing[]` lists domains with no material write this month.
- Override: `/finz:snapshot force-seal <month>` for edge cases (e.g., finalizing an annual picture).

### `workspace/goals.json`

Goal definitions. Progress is computed on the fly from `history.json`.

Schema:
```json
{
  "goals": [
    {
      "id": "house-2028",
      "name": "House down payment",
      "target_eur": 100000,
      "target_date": "2028-12-31",
      "tracked_via": "net_worth.investments + net_worth.cash",
      "monthly_contribution_target": 1500,
      "created_at": "2026-04-16"
    }
  ]
}
```

Advisor computes from this + history:
- Current value against target (gap or surplus)
- Required monthly rate to hit target vs. actual monthly rate (from history trend)
- Projected completion date at current pace
- Surplus or shortfall as EUR/month

### Staleness surfacing

Already partially in place — each state file has `last_updated`. v1.1 adds:
- `/finz:insights` header shows last-updated date per state file; flags anything >90 days as stale
- `/finz:advisor` carries stale-data caveats into recommendations that depend on that state
- No new file required

## Event System (v1.2)

### Calendar knowledge layers

**Built-in** — `skills/finz/references/german-finance-calendar.md`. Encyclopedic reference for German tax/finance cycles. The advisor reads this when computing time-sensitive recommendations. Examples of entries:
- January: Vorabpauschale debit for accumulating ETFs
- March–April: Lohnsteuerbescheinigungen arrive; VaSt data becomes available in ELSTER
- July 31: Self-filing tax deadline (for prior year)
- April 30 (following year): Extended deadline with Steuerberater
- December 15: Verlustbescheinigung deadline
- Year-end: SPB use-it-or-lose-it, tax-loss harvesting window

**User-specific** — `workspace/calendar.json`. Auto-populated by other skills when relevant events occur. Schema:

```json
{
  "events": [
    {
      "id": "auto-einspruch-2024",
      "title": "Einspruch window ends for Steuerbescheid 2024",
      "date": "2026-05-15",
      "source": "finz:scan",
      "linked_to": {"type": "steuerbescheid", "year": 2024},
      "action": "Review the Bescheid and file Einspruch if disputed"
    },
    {
      "id": "manual-festgeld-matures",
      "title": "Bank B Festgeld matures",
      "date": "2026-09-15",
      "source": "manual"
    }
  ]
}
```

Auto-population hooks:
- `/finz:scan` processes a Steuerbescheid → 1-month Einspruch window entry
- `/finz:crypto` detects a lot becoming tax-free on a specific date → milestone entry
- Goal `target_date` from `goals.json` surfaces here
- `/finz:cash` captures a Festgeld with a known maturity → maturity entry

### `/finz:calendar` command

Subcommands:
- `/finz:calendar` — show next 90 days
- `/finz:calendar year` — full calendar year view
- `/finz:calendar add "title" YYYY-MM-DD` — manual add
- `/finz:calendar remove <id>` — remove manual entries

`/finz:advisor` and `/finz:insights` silently read both calendar layers and surface anything within a 30-day horizon at the top of their reports.

### Life events

Predefined templates live in `skills/finz/references/life-events/`:
- `baby.md` — insurance audit (BU, life, dental, child), Kindergeld, Kita budget, Kinderfreibetrag, tax class change
- `job-change.md` — tax class reassessment, BU re-check, bAV review, income update
- `marriage.md` — tax class optimization, Zusammenveranlagung, insurance merge
- `divorce.md` — tax class, insurance, custody/Kindergeld
- `relocation-de.md` — Finanzamt change, insurance address update
- `relocation-abroad.md` — deregistration, cross-border tax, exit planning
- `property-purchase.md` — mortgage modeling, insurance (Wohngebäude, Bauherrenhaftpflicht)
- `inheritance.md` — Erbschaftsteuer, asset integration, insurance update

Each template lists: affected domains, specific checks to run, profile updates needed, calendar entries to create.

`/finz:life-event <name>` reads the template, runs advisor passes focused on affected domains, and produces a checklist with action items linked to real commands (`/finz:insurance audit`, `/finz:profile update children`, etc.).

Users can add custom templates by dropping a markdown file in the directory.

## Cross-Border Extension (v1.3)

Narrow addition for tracking foreign real estate and associated money flows. **Not** a full jurisdictional framework.

### Profile extension

```json
"foreign_real_estate": [
  {
    "nickname": "Porto Alegre apartment",
    "country": "BR",
    "purchase_date": "YYYY-MM-DD",
    "purchase_price_local": 850000,
    "purchase_currency": "BRL",
    "purchase_price_eur": 145000,
    "financing": {
      "monthly_installment_local": 4200,
      "currency": "BRL",
      "installments_total": 120,
      "installments_paid": 8,
      "payoff_date": "YYYY-MM-DD"
    },
    "usage": "vacant|rented|primary-residence-future",
    "notes": ""
  }
]
```

### Cash schema extension

- `account.currency` — new field on each account (default `"EUR"`)
- New expense category: `installment_payments_abroad`

### Calendar auto-entries

When `foreign_real_estate` is registered or updated, the advisor creates calendar entries:
- `payoff_date` → "Property financing paid off"
- `purchase_date + 10 years` → "§23 EStG 10-year clock expires — sale would be tax-free in Germany beyond this date"
- Annual marker → "Brazilian IPTU typically due — confirm payment"

### Advisor enhancements

- Net worth calculation includes `foreign_real_estate` (with "EUR value as of purchase — FX may have changed" caveat)
- Cross-border flags surface when conditions match:
  - "Brazilian apartment sold before [date] would trigger §23 capital gains in Germany."
  - "If you rent it, rental income goes on Anlage V (Mieteinnahmen aus Ausland) with DBA Brazil–Germany."
  - "You've transferred ~X EUR in installments in YYYY — confirm reporting in any foreign jurisdictions if applicable."

### Explicit non-goals

- No Brazilian tax computation (IR ganho de capital, rental tax, IPTU)
- No DBA computation
- No full real estate domain (appraisal tracking, multiple properties with varied usage, etc.)
- No multi-jurisdiction tax residency tracking

## Phasing

### v1.0 — Foundation + Advisor

- `finz` namespace — all commands moved to `.claude/commands/finz/`
- `/bank` → `/finz:cash`, `/scanner` → `/finz:scan`
- Master help (`/finz`) + per-domain help when called bare
- New skill `/finz:advisor` with proactive + goal-driven modes (operating on current state only — no history, goals, or calendar yet)
- README updated to reflect namespace + new brand
- Already-done: PII sanitization, `.gitignore`

### v1.1 — Temporal

- `workspace/history.json` + auto-capture protocol in every material-writing skill
- `workspace/goals.json` + `/finz:advisor goals ...` subcommands
- Staleness indicators in `/finz:insights` and `/finz:advisor`
- Advisor uses history (trend analysis) and goals (pace tracking)

### v1.2 — Event system

- Reference file `skills/finz/references/german-finance-calendar.md`
- `workspace/calendar.json` + `/finz:calendar` command
- Auto-population hooks in `/finz:scan`, `/finz:crypto`, `/finz:cash`
- Life event templates in `skills/finz/references/life-events/`
- `/finz:life-event <name>` command
- Advisor/insights surface within-30-day calendar items

### v1.3 — Cross-border extension (narrow)

- `profile.foreign_real_estate[]` schema
- `cash-state.json` `currency` field + `installment_payments_abroad` category
- Auto-calendar-entries for property tax events
- Advisor cross-border flags

## Out of Scope

Explicitly deferred to later versions:
- Full pension modeling (gesetzliche Rente, Riester, Rürup, bAV, foreign pensions)
- Debt/loan tracking (mortgages, student loans, revolving credit)
- General real estate domain (beyond the single foreign-property tracking in v1.3)
- Multi-jurisdiction tax residency framework
- Scenario planning ("what if I lose my job?")
- Benchmarking against German averages
- Change-log audit trail (only `last_updated` staleness)
- SQLite migration (may be revisited if `crypto-ledger.json` becomes unusable as JSON)
- Currency/FX rate engine (FX conversions stay best-effort with caveats)

## Implementation Notes for Planner

- The namespace rename (v1.0) is largely mechanical — moving files, updating routing paths in command markdown, renaming two domains, updating skill references
- The advisor skill (v1.0) is built on top of existing domain data; its logic is mostly heuristic aggregation with EUR-ranked output. No new state infrastructure required for v1.0.
- Each subsequent version extends the advisor — v1.1 adds trend intelligence, v1.2 adds calendar awareness, v1.3 adds cross-border flagging.
- Auto-capture in v1.1 requires modifying each material-writing skill. This is the highest-touch change of the series.
- Calendar auto-population in v1.2 similarly requires hooks in `scan`, `crypto`, `cash`.
- No breaking migrations needed in state files across the series — all schema changes are additive. Existing state files remain readable at every version.
