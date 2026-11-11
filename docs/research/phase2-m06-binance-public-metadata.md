# M06 Binance public product and cost evidence

**Retrieved 12 November 2026, Asia/Manila.** Scope is Binance global public Spot and USDⓈ-M REST metadata through the connected Binance public-data service. Field values below are a projection of the returned payloads. They describe the retrieved snapshot, with product applicability and freshness to be checked for any later research decision. The source scope is exchange documentation and observed responses, separate from the Coach PDF.

## 1. Endpoint and snapshot receipts

| Receipt | Read-only endpoint and request scope | Observed result and response clock |
| --- | --- | --- |
| B01 | Binance Spot GET /api/v3/exchangeInfo?symbol=XAUUSDT | HTTP 400, exchange code −1121, invalid symbol. This endpoint did not return a Spot record for the requested symbol. |
| B02 | Binance Spot GET /api/v3/exchangeInfo?symbol=XAUTUSDT | One symbol, TRADING. Raw serverTime 1794433537920, 2026-11-11 21:45:37.920 UTC. |
| B03 | Binance Spot GET /api/v3/exchangeInfo?symbol=PAXGUSDT | One symbol, TRADING. Raw serverTime 1794433537996, 2026-11-11 21:45:37.996 UTC. |
| B04 | Binance USDⓈ-M GET /fapi/v1/exchangeInfo, full response filtered locally by exact symbol | 946 symbol records returned. All three requested exact strings had one TRADING record each. Raw serverTime 1794392311942, 2026-11-11 10:18:31.942 UTC. The USDⓈ-M docs direct readers to a separate time endpoint for current server time. This field does not establish observation freshness or decision-time availability. |
| B05 | Binance USDⓈ-M GET /fapi/v1/fundingInfo, full response filtered locally | 820 rows returned. All three exact strings had one adjustment row. Each has its own updateTime below. |
| B06 | Binance USDⓈ-M GET /fapi/v1/tradingSchedule | Six asset classes returned. The COMMODITY class carried five intervals. Raw updateTime 1794430320254, 2026-11-11 20:52:00.254 UTC. |

Endpoint definitions and response scope appear in [Spot general endpoints](https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/general) and [USDⓈ-M market data](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data). The displayed UTC values are conversions of raw response fields. They do not establish native chart receipt times. Global metadata does not establish regional or user account access.

## 2. Instrument identity and permissible increments

Every returned instrument has quote asset USDT. All three USDⓈ-M records have margin asset USDT. Quantity ranges below are exchange order quantity fields in that product's declared quantity basis. Contract payout units require their own evidence. The literal enum TRADIFI_PERPETUAL is reproduced as returned.

| Venue and product | Symbol / base | Class and reference | Price tick | LOT_SIZE min / step / max | MARKET_LOT_SIZE min / step / max | Notional metadata |
| --- | --- | --- | ---: | --- | --- | --- |
| Binance Spot | XAUTUSDT / XAUT | XAUT token spot pair | 0.01 | 0.0001 / 0.0001 / 9,000 | 0 / 0 / 508.15827583 | NOTIONAL min 5, max 9,000,000 USDT |
| Binance Spot | PAXGUSDT / PAXG | PAXG token spot pair | 0.01 | 0.0001 / 0.0001 / 9,000 | 0 / 0 / 182.93315625 | NOTIONAL min 5, max 9,000,000 USDT |
| Binance USDⓈ-M commodity TradFi perpetual | XAUUSDT / XAU | TRADIFI_PERPETUAL, COMMODITY, TradFi. Gold-reference derivative. | 0.01 | 0.001 / 0.001 / 10,000 | 0.001 / 0.001 / 1,000 | MIN_NOTIONAL 5 USDT |
| Binance USDⓈ-M token perpetual | XAUTUSDT / XAUT | PERPETUAL, COIN, RWA/Crypto. XAUT underlying. | 0.01 | 0.001 / 0.001 / 2,000 | 0.001 / 0.001 / 200 | MIN_NOTIONAL 5 USDT |
| Binance USDⓈ-M token perpetual | PAXGUSDT / PAXG | PERPETUAL, COIN, RWA/Crypto. PAXG underlying. | 0.01 | 0.001 / 0.001 / 2,000 | 0.001 / 0.001 / 200 | MIN_NOTIONAL 5 USDT |

For the two Spot rows, PRICE_FILTER min/max were 0.01/1,000,000. NOTIONAL carried applyMinToMarket=true, applyMaxToMarket=false and avgPriceMins=5. Market validation may use a symbol reference price when available, with a documented average-price fallback. PERCENT_PRICE_BY_SIDE was 1.1/0.8 for bid multipliers and 1.2/0.9 for ask multipliers, with avgPriceMins=5. MARKET_LOT_SIZE min and step above are raw zero fields. Do not divide by zero or infer that every other quantity/notional check is inapplicable. Verify how the selected order type, quantity basis and applicable filters compose. [Spot filter definitions](https://developers.binance.com/en/docs/products/spot/filters)

For the three USDⓈ-M rows, PRICE_FILTER min/max were 0.01/200,000. XAUUSDT showed triggerProtect=0.02, marketTakeBound=0.02 and PERCENT_PRICE multipliers 1.02/0.98. Both token perpetuals showed 0.05, 0.05 and 1.05/0.95 respectively. These fields have exchange-defined roles. They cannot serve as general execution or stop-loss bounds. PAXGUSDT USDⓈ-M returned pricePrecision=4 with tickSize=0.01, a direct example of why display precision cannot replace the price filter. Keep quote constraints, position constraints and trigger conditions in their product and order scope. [USDⓈ-M market data](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data) · [Conditional trigger and protection documentation](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/trade)

XAUUSDT’s gold-reference index exposure is different from the two token references. Spot token inventory is a different product from a token perpetual even with the same displayed ticker. Public Spot instrument flags do not grant account-specific borrowing, margin or short access. A mark, index, contract trade or spot quote must retain its own price basis and timestamp. [XAUUSDT commodity index notice](https://www.binance.com/en/support/announcement/detail/f69c05ebdba7422e9c614685abe84dc5) · [XAUT futures listing](https://www.binance.com/en/support/announcement/detail/a82f1ff4c33244698c149d8b6fed2b01) · [PAXG futures listing](https://www.binance.com/lo-LA/support/announcement/detail/407190c3e5894c679fb4dc1cd7de5982)

## 3. Funding, session and fees

| Binance USDⓈ-M symbol | B05 reported interval | B05 adjusted rate floor / cap | Raw row updateTime |
| --- | ---: | --- | ---: |
| XAUUSDT | 4 h | −0.005 / +0.005 | 1769796333728 |
| XAUTUSDT | 4 h | −0.02 / +0.02 | 1774532681641 |
| PAXGUSDT | 4 h | −0.02 / +0.02 | 1743071583902 |

Rates in this table are dimensionless. They equal ±0.5% and ±2% caps/floors respectively. They are adjustment settings. Realized settlement rates, actual position at each settlement, and paid funding amounts were unavailable. Keep rate direction, notional at settlement and interval history as independent time-varying inputs. Spot inventory has no perpetual funding term. [Funding information endpoint](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data) · [Binance funding methodology](https://www.binance.com/en/support/faq/detail/360033525031)

The B06 COMMODITY underlying schedule shows a regular interval from 2026-11-08 23:00 UTC to 2026-11-13 22:00 UTC, then NO_TRADING for the underlying from 2026-11-13 22:00 UTC to 2026-11-15 23:00 UTC. This is the underlying-session clock. Binance’s commodity notice describes third-party constituent pricing during its regular interval and order-book EWMA off-hours, while stating that the schedule change leaves contract trading operations in place. A futures quote can therefore belong to an off-hours pricing regime. Store venue session, underlying session and index mode separately. Do not use the COMMODITY schedule as a trading-hours filter for either token product. [Trading schedule endpoint](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/market-data) · [Commodity pricing regime notice](https://www.binance.com/en/support/announcement/detail/f69c05ebdba7422e9c614685abe84dc5) · [TradFi product FAQ](https://www.binance.com/es/support/faq/detail/1b88e951ee42414396b0c3a86ba4be4f)

Public fee pages separate Spot and futures schedules. Binance’s 5 November TradFi promotion lists, for example, regular-tier maker 0% and taker 0.04% during the promotion, subject to terms. This is published product evidence, with no private tier, eligibility, applied discount, fee asset or effective fee observed. Preserve fee schedule version, effective window, product, liquidity role and conversion basis per leg. Do not apply the TradFi promotion to token perpetuals or Spot. [Spot fee schedule](https://www.binance.com/en/fee/trading) · [USDⓈ-M fee schedule](https://www.binance.com/en/fee/futureFee) · [5 November TradFi promotion](https://www.binance.com/en/support/announcement/detail/4f406308840549ffb8fdaac9873c25a8)

## 4. Scope of feasibility claims

Public filters support price/quantity grid and nominal constraint analysis. Effective tier, position-dependent limits, exact contract quantity-to-payout mapping as a separately verified contract record, live spread/depth, realized fees, borrow costs, margin mode, collateral, liquidation price and observed fill evidence remain unverified for this mission. The USDⓈ-M leverage bracket endpoint is an authenticated account endpoint, outside this public snapshot. Binance documents tier-dependent maintenance margin and cross/isolated distinctions. Treat displayed margin fields and product launch leverage limits as insufficient to compute an account’s margin or liquidation risk. [USDⓈ-M bracket documentation](https://developers.binance.com/en/docs/catalog/core-trading-derivatives-trading-usd-s-m-futures/api/rest-api/account) · [USDⓈ-M liquidation calculation and assumptions](https://www.binance.com/en/support/faq/detail/b3c689c1f50a44cabb3a84e663b81d93)

Use the tuple (venue, product namespace, exact symbol, price basis, evidence version). Carry independent source and retrieval times. Refresh product rules as-of any later validation. Public metadata can produce a documented unknown or infeasibility result without market candles. No market candles or private endpoints were requested for this snapshot.
