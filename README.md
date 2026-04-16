# Steuer — Personal Finance Toolkit for German Expats

A multi-domain personal finance toolkit built as Claude Code skills. Covers tax filing, insurance auditing, investment portfolio review, and document intelligence — all connected through a shared financial profile.

## Quick Start

1. **Set up your profile:** `/profile setup` — builds your financial identity (one-time)
2. **Scan your documents:** `/scanner scan ~/path/to/folder` — classify and extract data from PDFs
3. **Use any domain tool:** `/steuer`, `/insurance`, `/portfolio`

## Commands

| Command | What it does |
|---------|-------------|
| `/profile` | Manage your financial identity (personal details, family, salary, risk context) |
| `/scanner` | Scan folders of documents — classify, approve, extract structured data |
| `/insurance` | Insurance audit — what you have, what you're missing, recommendations |
| `/portfolio` | Portfolio review — allocation, tax efficiency, fundamentals, sell/buy recommendations |
| `/steuer` | German tax filing — ELSTER walkthrough, deductions, calculation |
| `/crypto` | Crypto tax engine — ingest Binance/Coinbase CSVs, FIFO accounting, §23/§22 Nr.3 EStG |

### Profile

| Sub-command | Description |
|-------------|-------------|
| `/profile setup` | Interactive interview to build your profile |
| `/profile update` | Modify specific fields (e.g., "my salary changed to 115k") |
| `/profile show` | Display current profile summary |
| `/profile status` | Completeness check |

### Scanner

| Sub-command | Description |
|-------------|-------------|
| `/scanner scan <folder>` | Read all files, classify, get your approval, then extract data |
| `/scanner status` | Show what's been scanned |
| `/scanner corrections` | Review and correct past classifications |

### Insurance

| Sub-command | Description |
|-------------|-------------|
| `/insurance audit` | Full gap analysis: what you have vs. what you need |
| `/insurance scan <folder>` | Scan folder for insurance docs, then audit |
| `/insurance status` | Current coverage summary |

### Portfolio

| Sub-command | Description |
|-------------|-------------|
| `/portfolio review` | Full analysis: allocation, tax efficiency, fundamentals |
| `/portfolio scan <folder>` | Scan folder for investment docs, then review |
| `/portfolio tax-check` | Investment tax optimization (Sparerpauschbetrag, Verlustverrechnung, etc.) |
| `/portfolio status` | Quick holdings summary |

### Crypto Tax

| Sub-command | Description |
|-------------|-------------|
| `/crypto ingest` | Parse Binance + Coinbase CSVs, run FIFO, write ledger + summary |
| `/crypto status` | Last ingest stats, open issues, holdings summary |
| `/crypto review` | Full ledger review: holdings, disposals, income events |
| `/crypto resolve` | Walk through open issues and record decisions |
| `/crypto optimize` | Tax-free milestones, loss-harvesting opportunities |
| `/crypto tax --year YYYY` | Per-year §23/§22 Nr.3 drill-down with Anlage SO mapping |
| `/crypto export --year YYYY` | Generate Steuerberater export package |

### Steuer (Tax Filing)

| Sub-command | Description |
|-------------|-------------|
| `/steuer` or `/steuer start` | Begin full guided tax filing workflow |
| `/steuer intake` | Extract data from Lohnsteuerbescheinigungen |
| `/steuer deductions` | Interactive deduction interview |
| `/steuer documents` | Generate document checklist |
| `/steuer calculate` | Estimate tax liability, compare filing strategies |
| `/steuer filing` | Step-by-step ELSTER form guide |
| `/steuer status` | Show progress |
| `/steuer summary` | Generate comprehensive summary |

## How It All Connects

```
NAS folders --> /scanner --> document-registry.json
                                |
                    +-----------+-----------+
                    |           |           |
              insurance-    portfolio-   tax-state.json
              state.json    state.json   (existing)
                    |           |           |
                /insurance  /portfolio  /steuer
                    |           |           |
                    +-----------+-----------+
                                |
                          profile.json
                       (read by all skills)
```

**Cross-domain data flow:**

- `/scanner` feeds classified + extracted data into all domain state files
- `/profile` provides personal details to all skills (no re-entering data)
- `/portfolio tax-check` pre-fills Anlage KAP data for `/steuer intake`
- `/insurance audit` identifies premiums for Vorsorgeaufwand deduction in `/steuer deductions`

## Data Files

All state files live in `workspace/`:

| File | Purpose | Written by |
|------|---------|------------|
| `profile.json` | Shared financial identity | `/profile` |
| `tax-state.json` | Tax filing data | `/steuer` |
| `insurance-state.json` | Insurance policies and audit results | `/scanner`, `/insurance` |
| `portfolio-state.json` | Holdings, allocations, tax positions | `/scanner`, `/portfolio` |
| `document-registry.json` | Scanned file classifications and corrections | `/scanner` |
| `crypto-ledger.json` | Full crypto transaction ledger (lots, disposals, income) | `/crypto ingest` |
| `crypto-summary.json` | Crypto yearly tax summary and current holdings | `/crypto ingest` |
| `crypto-decisions.json` | User decisions for ambiguous crypto transactions | `/crypto resolve` |
| `resources/crypto/binance/*.csv` | Raw Binance Transaction History exports | user-provided |
| `resources/crypto/coinbase/*.csv` | Raw Coinbase Transaction History exports | user-provided |

## Design Principles

- **English only** — German financial terms are always explained in parentheses
- **Opinionated but transparent** — recommendations come with reasoning and real numbers
- **Show the math** — every recommendation traces back to your data
- **Your decision** — the tool has a point of view but you always make the call
- **No hidden logic** — reference files document all rules; skill logic is readable

## Project Structure

```
.claude/
  skills/
    profile/SKILL.md                    # Financial identity manager
    scanner/SKILL.md                    # Document intelligence
    scanner/references/                 # Classification taxonomy, extraction templates
    insurance/SKILL.md                  # Insurance audit
    insurance/references/               # German insurance types, gap framework, costs
    portfolio/SKILL.md                  # Portfolio review
    portfolio/references/               # Investment tax, allocation, fundamentals
    steuer-orchestrator/SKILL.md        # Tax filing orchestrator
    steuer-intake/SKILL.md              # Income document extraction
    steuer-deductions/SKILL.md          # Deduction interview
    steuer-calculator/SKILL.md          # Tax estimation
    steuer-documents/SKILL.md           # Document checklist
    steuer-filing/SKILL.md              # ELSTER form guide
    crypto/SKILL.md                     # Crypto tax engine
    crypto/scripts/                     # Python pipeline (parsers, classifier, fifo, etc.)
    crypto/tests/                       # Pytest test suite (53 tests)
    crypto/references/                  # German tax law, FIFO methodology, price sources
    steuer-crypto/SKILL.md              # Steuerberater export sub-skill
    steuer-crypto/references/           # Anlage SO mapping, Nacherklärung template
  commands/
    profile.md                          # /profile routing
    scanner.md                          # /scanner routing
    insurance.md                        # /insurance routing
    portfolio.md                        # /portfolio routing
    steuer.md                           # /steuer routing
workspace/
  profile.json                          # Your financial profile
  tax-state.json                        # Tax filing state
  insurance-state.json                  # Insurance data
  portfolio-state.json                  # Investment data
  document-registry.json                # Scanner registry
  output/                               # Generated reports
  resources/                            # Source documents
```

## Future Domains

The architecture supports adding more domains — each follows the same pattern (own skill, own state file, reads from profile.json):

- `/broker` — Broker fee comparison, tax reporting quality
- `/pension` — Riester/Ruerup/bAV planning, retirement projections
- `/snapshot` — Net worth tracking, savings rate, year-over-year trajectory

## Disclaimer

This toolkit is NOT a Steuerberater (tax advisor) and cannot provide binding tax or financial advice. It helps organize information, identify opportunities, estimate positions, and prepare data. Always consult a qualified professional for complex situations.
