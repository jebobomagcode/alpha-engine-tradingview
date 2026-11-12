# M07 bounded market evidence — Binance PAXGUSDT Spot v1

**Retrieved 12 November 2026, Asia/Manila.** Purpose is product qualification and input-integrity verification for the Lesson 08 1H→5m descriptive profile. This receipt freezes a narrow public evidence window. It carries no setup labels, modeled fills, or performance results.

## Product decision

**Select Binance Spot PAXGUSDT** for the first validation. This is the PAXG/USDT token spot market, with price in USDT per PAXG and ordinary base quantity in PAXG. A hypothetical cash spot purchase supports the long-side continuation example without a contract multiplier, funding, mark-price liquidation or collateral model. A bearish result may remain descriptive, with ordinary unborrowed spot short feasibility unavailable. The prototype evaluation should begin with one long setup. Product qualification here refers to the public Binance data and metadata. TradingView identity and account-specific eligibility still require verification.

| Candidate assessed | Disposition and basis |
| --- | --- |
| Binance Spot PAXGUSDT | Selected narrow baseline. Exact symbol returned TRADING and isSpotTradingAllowed=true. Public 1H and 5m coverage is documented below. |
| Binance Spot XAUTUSDT | Comparable simple candidate. The refreshed response also showed TRADING, USDT quote, price tick 0.01, LOT_SIZE step 0.0001 and minimum notional 5 USDT. PAXG was chosen as a fixed initial scope before reading its bars. This is a research tie-break, with relative liquidity, cost and suitability untested. |
| Binance USDⓈ-M PAXGUSDT and XAUTUSDT | Distinct token perpetuals. M06 observed different lot rules from Spot and additional funding, trigger-basis and margin inputs. Defer those dependencies in the initial validation. |
| Binance USDⓈ-M XAUUSDT | Distinct commodity TradFi perpetual. M06 observed underlying-session and pricing-regime inputs as well as derivatives constraints. The previous Spot lookup for XAUUSDT returned invalid symbol. Keep its reference exposure and futures data separate. |

The comparison uses [M06 public product evidence](phase2-m06-binance-public-metadata.md) and refreshed exact-symbol Spot responses. The PAXG Spot snapshot specifies price tick 0.01 USDT/PAXG, LOT_SIZE min/step 0.0001 PAXG and max 9,000 PAXG, and NOTIONAL minimum 5 USDT. MARKET_LOT_SIZE max is 179.43979497 PAXG in this response. Its other raw fields remain available in the metadata. Resolve applicable order filters separately, including any reference-price or market quantity rules. The observed rules are as of retrieval. Their historical effective time, account fees and fill effects remain unknown. [Binance Spot filters](https://developers.binance.com/en/docs/products/spot/filters)

## Request, coverage and content identity

Venue is Binance global public Spot. Klines are native trade-price OHLC and base/quote volume from **GET /api/v3/klines** for **PAXGUSDT**, using timeZone=0. Exchange metadata is **GET /api/v3/exchangeInfo?symbol=PAXGUSDT**. Request parameters below use UTC milliseconds. The documented API interprets start and end in UTC, including with a timezone parameter. [Binance Spot market-data endpoint documentation](https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market)

| Evidence | Exact request parameters beyond symbol and timezone | Observed rows and UTC window | Local observation time, UTC |
| --- | --- | --- | --- |
| [5m response](evidence/m07-paxgusdt-spot-v1/klines-5m.json) | interval=5m, startTime=1794355200000, endTime=1794441599999, limit=288 | 288 consecutive rows. Open range 2026-11-11 00:00 through 23:55. Last reported close 23:59:59.999. | 2026-11-12 05:24:31.233 |
| [1H response](evidence/m07-paxgusdt-spot-v1/klines-1h.json) | interval=1h, startTime=1794268800000, endTime=1794441599999, limit=48 | 48 consecutive rows. Open range 2026-11-10 00:00 through 2026-11-11 23:00. Last reported close 2026-11-11 23:59:59.999. First 24 hours are prior context. | 2026-11-12 05:24:31.034 |
| [Selected Spot metadata](evidence/m07-paxgusdt-spot-v1/exchange-info.json) | exact symbol | One PAXGUSDT Spot row. Response serverTime 1794461071312, 2026-11-12 05:24:31.312 UTC. | 2026-11-12 05:24:31.383 |

The acquisition batch started at 2026-11-12 05:24:29.810 UTC (13:24:29.810 PHT). PHT adds eight hours. The 5m window is [11 November 08:00, 12 November 08:00) PHT, with hourly context starting 10 November 08:00 PHT. All 336 rows end before the batch began. The alternate XAUTUSDT exact-symbol metadata response was observed 05:24:31.045 UTC. A preceding multi-symbol metadata request returned HTTP 400, Binance code −1101. Individual exact-symbol requests resolved the lookup. No alternative candle product was substituted.

| Preserved connector response text | Bytes | SHA-256 |
| --- | ---: | --- |
| klines-5m.json | 46,291 | 48c2cb774b312a6a7061fae4b9dd8fae8b0274cea0cb476f0a1e54033163e180 |
| klines-1h.json | 8,009 | 30f7eb868fdb3b040728c7e78fa7d6d48c93cd24b37783b10619ca148c6eb95d |
| exchange-info.json | 5,254 | 2be70bbeefb9e813c16e4bf74c965578462054734c532f3a43d84ec5780c4253 |

These are exact UTF-8 bytes of each connector text payload, including its JSON wrapper when present. HTTP wire bytes and response headers are unavailable. No decimal strings were recast before freezing. Kline payloads do not independently restate symbol in each row, so pair the raw bytes with the named request. Row identity is venue, product, symbol, interval, UTC open and revision. The payload hash identifies this frozen response version.

## Finality, gaps and availability

- **Finality for this historical snapshot.** Treat bars as completed for input validation because their whole intervals ended before acquisition. Each recorded close is open plus interval minus 1 ms. Use the exclusive end for the earliest modeled close boundary. An active bar is provisional in a future realtime capture. The historical snapshot carries no proof of when the exchange first published each finalized row.
- **Observed availability** is the local tool-response timestamp for this acquisition. **Modeled historical availability** is the documented evaluation boundary when doing a controlled replay, never earlier than exclusive close. HTF context at an LTF open additionally uses the explicit modeled HTF publication rule in the [M07 protocol](phase2-mtf-validation-and-falsification-protocol.md). Native exchange receipt times and same-wall-clock ordering are unknown. Strict observed-sequence qualification cannot be certified by these bars.
- **Continuity.** Compare expected interval opens against returned identities, count duplicates, gaps, wrong intervals and out-of-range rows. Missing required bars produce an insufficient-evidence reason. Preserve gaps, with no invented OHLC and no silent forward fill to qualify a setup. Keep genuine zero-volume observations if the source supplies them and scope any interpretation accordingly.
- **Revision.** Keep v1 immutable. A repeat request may yield a new raw hash. Record receipt and distinguish serialization-only changes from semantic revisions using row IDs and all fields. Use a new evidence version for semantic changes, preserving earlier as-issued snapshots and comparisons. Metadata effective dates and chart feed versions stay separate from historical bar timestamps.

## Verified input checks and limits

The 5m and 1H responses matched all expected aligned opens and inclusive closes, with no duplicate, missing, or out-of-window rows in the requested intervals. All rows passed positive-price OHLC ordering and nonnegative volume/trade-count checks, including taker amounts within totals. Within the common 24 hours, each native 1H bar matched its 12 constituent 5m bars exactly for all nine compared fields: O/H/L/C, base volume, quote volume, trade count, taker base volume and taker quote volume. This is **216 internal field matches** for one Binance sample. The preceding 24 hourly bars have no corresponding 5m coverage in the receipt.

The matching evidence establishes bounded completeness and internal consistency at retrieval. It supplies no TradingView parity, setup ground truth, intrabar touch order, bid/ask depth, fees or fills. The day is an input acceptance window. A later empirical study would need separate sampling and authorization.
