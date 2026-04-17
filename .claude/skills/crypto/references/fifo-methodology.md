# FIFO Methodology — Reference

**Last verified:** 2026-04-17
**Tax year anchor:** 2025

## Authoritative basis

- **BMF-Schreiben 10.05.2022** — permits the FIFO-Methode as a vereinfachende Verwendungsreihenfolge for crypto where individual assignment of disposed-of units to specific Anschaffungsvorgänge is not feasible, and establishes the **walletbezogene Betrachtung** (per-wallet / per-exchange view) rather than a global FIFO across all holdings.
- **BMF-Schreiben 06.03.2025** — retains the walletbezogene FIFO-Betrachtung and adds Mitwirkungs- und Aufzeichnungspflichten requiring that the Verwendungsreihenfolge be reconstructable per wallet (<https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte.html>, retrieved 2026-04-17).

The taxpayer may alternatively use individual identification (Einzelbewertung) where lots are genuinely separable, but may not freely switch between methods within a tax year for the same asset/wallet pair.

## Per-wallet FIFO — the core rule

Maintain **one FIFO queue per (coin, wallet)**, where `wallet` is the operational unit at which the taxpayer holds the asset:

- Each centralised exchange account (Binance, Coinbase, Crypto.com, Kraken) is a separate wallet.
- Each self-custody wallet (MetaMask account, Ledger device) is a separate wallet.
- Sub-accounts within one exchange that are operationally distinct (Binance Spot vs. Funding vs. Earn, if the user treats them separately and the exchange reports them separately) may be modelled as separate wallets. Default: collapse sub-accounts within the same exchange into one wallet unless the user explicitly separates them.

Disposals consume lots from the queue of the **wallet where the disposal took place**, in order of `acquired_at` ascending (oldest first).

## Cross-exchange transfers

A transfer from wallet A to wallet B is **not a disposal**. It is a movement of existing lots with their `acquired_at` preserved:

1. Remove the transferred quantity from wallet A's FIFO queue (oldest-first).
2. Re-insert those lots into wallet B's FIFO queue with the **original `acquired_at` timestamps unchanged**.
3. If a transfer fee is paid in-kind (e.g., 0.0005 BTC network fee deducted from A's balance), the fee itself is a partial-disposal-equivalent; see Fee treatment below.

The 1-year holding clock runs from the original Anschaffung, not the transfer. Transferring BTC from Binance to a cold wallet the day before a sale does not reset the clock.

## Partial disposals

A disposal of `q` units where `q` is smaller than the oldest lot's remaining quantity:

1. Consume `q` from the oldest lot; keep that lot in the queue with `remaining_quantity -= q`.
2. Realize §23 gain/loss on exactly `q` units:
   `proceeds_per_unit * q − cost_basis_per_unit * q − prorated_fees`.
3. Holding-period test uses the oldest lot's `acquired_at`.

A disposal of `q` units spanning multiple lots:

1. Consume successive lots until `q` is exhausted.
2. Each consumed slice is a distinct §23 line item with its own holding-period determination — some slices may be tax-free (> 1 year) and others taxable (< 1 year) within the same disposal.

## Fee treatment

Per BMF and German accounting practice (§255 HGB as Anschaffungsnebenkosten):

- **Buy-side fees** (trading fee when acquiring crypto): **added to cost basis**. A 10,100 EUR purchase with 100 EUR fee yields a cost basis of 10,100 EUR (not 10,000).
- **Sell-side fees** (trading fee when disposing of crypto): **deducted from proceeds**. A 12,000 EUR sale with 50 EUR fee yields 11,950 EUR proceeds.
- **In-kind network/withdrawal fees** (e.g., 0.0005 BTC paid as miner fee on a transfer): treated as a deemed disposal of the fee quantity at FMV in EUR on the fee date. This is the conservative position — some literature treats intra-wallet-management fees as non-realizing. Default to conservative; document the choice.

The crypto engine pro-rates fees to each consumed lot on partial disposals (fee × consumed_quantity / total_disposal_quantity).

## Lot origin for staking, lending, airdrop rewards

When a §22 Nr. 3 event produces crypto (staking reward, Simple Earn interest, airdrop mit Leistung, lending interest paid in crypto):

1. Recognize the FMV in EUR at the time of wirtschaftliche Verfügungsmacht as §22 Nr. 3 income.
2. Insert a new lot into the wallet's FIFO queue with:
   - `quantity` = received quantity
   - `acquired_at` = receipt timestamp
   - `cost_basis_per_unit` = FMV-EUR-per-unit at receipt (not zero)
3. A later disposal within 1 year of this `acquired_at` is a §23 event on (proceeds − FMV-at-receipt), separate from the §22 Nr. 3 event.

**Pure airdrops without Leistung** (no action required from recipient) are not §22 Nr. 3 and are commonly treated as zero-basis §23 lots with `acquired_at` = receipt date; BMF position is nuanced and depends on the airdrop mechanics. Flag in output.

## External-in deposits (unknown origin)

A deposit appears in a CEX wallet but the source is not in the ingested data:

1. **Preferred:** user-provided `external_basis_override` in `crypto-decisions.json` — the user supplies `acquired_at` and `cost_basis_per_unit` they reconstructed from their prior records.
2. **Fallback:** conservative — set `acquired_at` to the deposit timestamp and `cost_basis_per_unit` to FMV at deposit. This assumes the crypto was freshly acquired at the deposit date, which maximises the chance of a §23 disposal if sold soon after. Flag in the issues list so the user is prompted to supply the override.

Reason: without the original Anschaffungsvorgang, the only defensible position is that no pre-deposit §23 holding period can be claimed.

## External-out withdrawals (unknown destination)

A withdrawal leaves a CEX wallet but the destination is not in the ingested data:

- Treated as a **conservative disposal at FMV on the withdrawal date**, creating a §23 event for the consumed lots.
- Flagged as an issue so the user can either confirm disposal (sent to a third party, gift, payment) or re-classify as a transfer (provide the destination wallet so the lots flow there with preserved `acquired_at`).

Reason: without evidence of continued ownership, the conservative assumption is disposal. The flag lets the user correct before finalising the ledger.

## Decimal precision

All arithmetic uses `decimal.Decimal` (Python stdlib), not `float`. BTC has 8 decimal places; some tokens have 18. Float rounding errors cascade through FIFO lot consumption and can produce visibly wrong EUR totals. The engine stores quantities and prices as Decimal and formats only at output time.

## Cross-references

- Price resolution for FMV at receipt and at disposal: `skills/crypto/references/price-sources.md`
- Tax-law framework and §23 / §22 Nr. 3 interplay: `skills/crypto/references/german-crypto-tax-law.md`
- Classification of CSV rows into `disposal`, `income`, `transfer`: `skills/crypto/references/transaction-taxonomy.yaml`
