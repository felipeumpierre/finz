# EUR Price Resolution — Reference

Resolution order per (coin, timestamp):

1. Embedded in CSV (EUR leg of trades)
2. Manual override — crypto-decisions.json.manual_prices[]
3. Cache — workspace/cache/prices/{coin}/{date}.json
4. CoinGecko historical API — /coins/{id}/history?date=DD-MM-YYYY

Daily prices (00:00 UTC snapshot). BMF accepts daily granularity.
