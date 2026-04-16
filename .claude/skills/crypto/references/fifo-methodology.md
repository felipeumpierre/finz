# FIFO Methodology — Reference

- One FIFO queue per (coin, wallet), where wallet = exchange.
- Cross-exchange transfers preserve original acquired_at timestamp.
- All arithmetic uses decimal.Decimal.

## External-in deposits with unknown origin

1. User-provided external_basis_override (preferred)
2. Fallback: conservative — acquired_at = deposit timestamp, cost basis = FMV.

## External-out withdrawals with unknown destination

Treated conservatively as disposal at FMV. Flagged in issues[].
