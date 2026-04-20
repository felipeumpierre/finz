# EUR Price Resolution — Reference

**Last verified:** 2026-04-17
**Tax year anchor:** 2025

## Authoritative basis

BMF-Schreiben 10.05.2022 and BMF-Schreiben 06.03.2025 accept the **tagesaktuelle Kurs** (daily spot price in EUR) of the relevant Handelsplattform as the valuation basis for recognition and disposal. The 06.03.2025 letter (Rz. 43, 58, 91) explicitly distinguishes **sekundengenaue Kurse** (second-precise) from **Tageskurse** (daily) and permits daily valuation with adequate documentation.

Source: <https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte.html> (retrieved 2026-04-17).

Practical rule: **00:00 UTC daily snapshot** from a recognised aggregator (CoinGecko, CoinMarketCap) is acceptable for private investors and is the default used by most Steuerreport-tools.

## Resolution order

For each `(coin, timestamp)` the engine needs an EUR price, it walks this priority chain:

1. **Embedded EUR in the source CSV.**
   If the CSV row is already a direct EUR leg (Coinbase `EUR-Spot` trade, Crypto.com row with `Native Currency = EUR`, Binance `BUSD/EUR` pair), trust the exchange-reported EUR value as the contemporaneous Marktpreis. This is the most defensible source because it is the actual transaction price.

2. **Manual override** — `workspace/crypto-decisions.json → manual_prices[]`.
   User-supplied `{coin, date, eur_price, source_note}` takes precedence over network lookups. Use for delisted assets, user-verified archive prices, or edge cases.

3. **Local cache** — `workspace/cache/prices/{coin}/{YYYY-MM-DD}.json`.
   Once a network price has been fetched it is written to cache. Subsequent runs read from cache — deterministic, offline-safe, and avoids rate-limit issues.

4. **CoinGecko historical API.**
   - Endpoint: `GET https://api.coingecko.com/api/v3/coins/{id}/history`
   - Required params: `id` (e.g. `bitcoin`), `date` in `DD-MM-YYYY` format.
   - Optional: `localization=false` (drops the localized-name payload).
   - Response EUR price: `market_data.current_price.eur`.
   - Snapshot time: **00:00:00 UTC** of the requested date. CoinGecko publishes the snapshot at 00:35 UTC the following day; same-day prices are therefore not available until ~00:35 UTC the next calendar day.
   - Docs: <https://docs.coingecko.com/v3.0.1/reference/coins-id-history> (retrieved 2026-04-17).
   - Example: `GET /coins/bitcoin/history?date=30-12-2023&localization=false` → returns BTC EUR price as at 2023-12-30 00:00 UTC.

## Daily granularity is acceptable

- BMF 06.03.2025 accepts daily valuation as long as the method is applied consistently within the tax year and adequately documented.
- Second-precise pricing is required only in narrow cases where it makes a material difference and the taxpayer's tooling naturally produces it (e.g., algorithmic trading with minute-level P&L).
- Default for this engine: 00:00 UTC daily snapshot via CoinGecko, which matches what the large Steuerreport providers (Accointing, CoinTracking, Blockpit) use.

## EUR cross-rate derivation for non-EUR pairs

For a trade like BTC/USDT at 14:35 UTC where neither leg is EUR:

1. Look up USDT/EUR at 14:35 UTC (or the daily snapshot for that date).
2. Compute implicit EUR amount: `btc_quantity * btc_usdt_price * usdt_eur_price`.
3. Alternative: look up BTC/EUR at the same timestamp directly and compute `btc_quantity * btc_eur_price`.

The two paths can disagree by a few tenths of a percent due to independent aggregator sources. The engine prefers the direct lookup (BTC → EUR) when both assets are on CoinGecko. For stablecoin pairs (USDT/USDC → EUR) the direct lookup is always used because the stablecoin's EUR price is close to the reciprocal of the EUR/USD FX rate.

For Binance Spot trades where the non-EUR base pair is the only reported leg, the ingestor stores the reported `quote_price` and multiplies by the quote asset's EUR price at the trade timestamp (daily or closest 5-minute bar if available).

## Delisted / defunct asset fallback

When CoinGecko has no data for a coin (delisted, rug-pulled, project defunct):

1. Check the manual overrides first.
2. If none, try the last known CoinGecko price before delisting and extrapolate zero (assume defunct asset is worthless at today's date, but retain the last valid price for historical Anschaffungskosten).
3. If even the historical data is missing, flag the asset in the ledger's `issues[]` list. The user must either supply a manual price or accept that the Anschaffungskosten for that lot cannot be reconstructed — a common outcome for small 2017–2018 altcoin holdings. In that case, the conservative position is zero cost basis, producing a larger taxable gain.
4. For assets that migrated tokens (e.g., ERC-20 → native chain migration), use the pre-migration price and preserve the original `acquired_at` across the migration (the migration is treated as non-realizing).

## Documentation

Every price used in the ledger is stored in the cache file with a `source` field recording which step in the resolution order produced it (`csv_embedded`, `manual_override`, `cache`, `coingecko_api`). This preserves the audit trail the Finanzamt may ask for under the BMF 06.03.2025 Mitwirkungspflichten.

## Cross-references

- FIFO consumption of lots priced here: `skills/crypto/references/fifo-methodology.md`
- Tax-law framework for when FMV recognition is required: `skills/crypto/references/german-crypto-tax-law.md`
