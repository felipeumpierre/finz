---
name: steuer-crypto
description: >
  Steuerberater-export sub-skill for crypto tax. Produces Anlage SO line mappings,
  disposal/income CSV exports, and Nacherklärung letter templates from the crypto ledger.
  Invoked by the steuer-orchestrator when crypto income or disposals are present.
  Also triggered when user asks about crypto and taxes together, wants to export for their
  Steuerberater, or needs to file a self-correction for crypto.
---

# Steuer-Crypto Export Skill

This skill takes the computed crypto ledger (`workspace/crypto-ledger.json`) and produces
Steuerberater-ready export packages per tax year.

## Important Disclaimer

You are NOT a Steuerberater. All outputs are best-effort and must be reviewed by a qualified
tax advisor before submission to the Finanzamt.

---

## Sub-commands

### `export --year YYYY`

Produce the full export package for year YYYY in `workspace/output/crypto-YYYY/`:

1. Read `workspace/crypto-ledger.json` and `workspace/crypto-summary.json`
2. Filter all disposals, income events for year YYYY
3. Generate:
   - `anlage-so-YYYY.md` — pre-filled Anlage SO fields (see `references/anlage-so-mapping.md`)
   - `disposals-YYYY.csv` — all §23 disposals: date, coin, amount, proceeds, cost, gain, treatment
   - `income-YYYY.csv` — all §22 Nr.3 events: date, coin, amount, EUR value, category
   - `lots-YYYY.csv` — lot detail per disposal (acquisition date, price, holding days)
   - `cover-note-YYYY.md` — plain-language summary for handoff to Steuerberater
   - `nacherklaerung-YYYY.md` — self-correction letter (only if `needs_correction = true`)

### `anlage-so --year YYYY`

Show the Anlage SO line mapping for YYYY inline (no file output). Useful for quick reference
during ELSTER filing.

Read the year-specific Anlage SO mapping:

- `references/anlage-so-mapping-2024.md` — for TY 2024 filings
- `references/anlage-so-mapping-2025.md` — for TY 2025 filings (flagged [UNVERIFIED] for Zeile numbers pending ELSTER confirmation)

### `nacherklaerung --year YYYY`

Generate the self-correction letter template for YYYY using `references/nacherklaerung-template.md`
and populating it with the actual numbers from `workspace/crypto-summary.json`.

Only generate if `yearly_tax_summary[YYYY].needs_correction = true`. If false, tell the user
no correction is needed for that year.

---

## Integration with steuer-orchestrator

When the steuer-orchestrator detects crypto income or disposals (via `workspace/crypto-summary.json`
or `workspace/crypto-ledger.json`), it should:

1. Include crypto §23 taxable amounts in the zvE calculation
2. Include crypto §22 Nr.3 income in Sonstige Einkünfte
3. Flag years needing correction in the overall tax assessment
4. Recommend running `/crypto export --year YYYY` before filing

## State Files

| File | Read/Write | Purpose |
|---|---|---|
| `workspace/crypto-ledger.json` | Read | Source of truth for all transactions |
| `workspace/crypto-summary.json` | Read | Yearly tax summaries and holdings |
| `workspace/output/crypto-YYYY/` | Write | Export packages per year |

## References

- `references/anlage-so-mapping-2024.md` — Anlage SO Zeile numbers for crypto, TY 2024 (authoritative, sourced to BMF form PDFs + Haufe/steuern.de)
- `references/anlage-so-mapping-2025.md` — Anlage SO Zeile numbers for crypto, TY 2025 (structure presumed preserved from 2024; [UNVERIFIED] pending form-PDF confirmation)
- `references/nacherklaerung-template.md` — Self-correction letter template

**Correction history (2026-04-17):** the prior single `anlage-so-mapping.md` cited Zeilen 41/42/43/46 for §23 and 10/12 for §22 Nr.3. That mapping was wrong — §23 for crypto (andere Wirtschaftsgüter) uses Zeilen **41–55** on the 2024 form, with Summenzeilen at **53/54/55**. The old file has been deleted; use the per-year files above.
