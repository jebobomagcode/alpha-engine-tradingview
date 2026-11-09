# N-01 Independent Crypto Research — Sessions, DST, Weekdays and Scheduled News

**OPEN HYPOTHESES; no Pine, no live data or news feed, no backtest, no trades or deployment.** Coach sole source [PDF p33](../../sources/coach%20trading%20lessons.pdf); [full source PCSS](../lessons/note-01-location-time-and-economic-calendar.md). Completely independent TradingView research project.

## Source-only contract

Coach text addresses forex major pairs and gold; Tue–Thu preferred activity, Monday sometimes slow after weekend, Friday caution; London 15–00 PHT, NY20–05 PHT, overlap20–00 PHT; GBPUSD/EURUSD/gold; CPI/NFP/FOMC/rate events; check Forex Factory/Investing.com calendars. It does NOT establish mandatory crypto weekday/session restrictions, a universal news blackout, automated calendar access, or statistical profitability.

## DST correction and time policy

Summer aligned London15–00, NY20–05, overlap20–00 PHT; winter aligned London16–01, NY21–06, overlap21–01. UK/US clock transitions differ, creating mixed weeks. On Nov9 2026, London08:00→16:00 PHT, NY08:00→21:00 PHT. Use IANA **Europe/London**, **America/New_York**, **Asia/Manila** and UTC source timestamps, not static hardcoded PHT windows. TradingView documentation [sessions](https://www.tradingview.com/pine-script-docs/concepts/sessions/) and [time](https://www.tradingview.com/pine-script-docs/concepts/time/).

## External empirical context (NOT source)

[38-exchange, 1940-pair study](https://link.springer.com/article/10.1007/s11156-024-01304-1) observes intraday crypto patterns; [Coinbase institutional 2024](https://www.coinbase.com/institutional/research-insights/research/market-intelligence/trading-activity-from-a-us-lens) describes US-hour activity; [Kraken BTC/USD 2016–25 study](https://www.mdpi.com/1911-8074/19/9/707) tracks volatility concentration toward US hours; [2026 FOMC event study](https://www.sciencedirect.com/science/article/pii/S1544612326006021) finds BTC/ETH macro-event-window movement. These differ by era, venue, measured variable and contract; none establish net signal edge for BTCUSDT, XAUUSDT, XAUTUSDT or PAXGUSDT. Source is forex, whereas crypto products can trade 24/7 subject to product/venue exceptions.

## Alternative research designs — NONE SELECTED AS CODE

- **M0 informational context:** DST-correct session labels, weekday and cited news schedule when available; UNKNOWN when no calendar; no eligibility filter. Best source transparency.
- **M1 measurement-only:** classify independently defined completed-bar setups by hour/weekday/session, volatility, volume, trend/range and after-cost performance, then compare neutral no-filter baseline.
- **M2 conditional economic-event risk controls:** test predeclared event proximity windows around CPI/NFP/FOMC only after original known-at calendars and feed access are verified; not a Coach-required prohibition.
- **M3 venue- and instrument-specific hour filters:** only if out-of-sample net benefit survives realistic costs and different regime holdouts; highest overfitting risk.

**Recommendation:** M0 first, then M1 research. Do not infer profit from volume, price volatility, day of week or macro-news label.

## Data and timing requirements

Venue-qualified instrument, spot/perpetual/asset backing, exchange hours/maintenance, UTC bar open/close, IANA-local time and daylight-saving date, session boundary policy, current news release source/time/known-at revisions, and explicit missing-news status. Historical backtests must not use revised event calendars as if past bar knew them. ATR or traded-volume are not the same as bid/ask liquidity or executable slippage.

## Falsification matrix (PLANNED ONLY; no tests run)

1. Aligned July London and NY open15/20 PHT.
2. Aligned November London and NY open16/21 PHT.
3. October mixed UK/US DST transition hours.
4. March mixed UK/US DST hours.
5. 15m bar spanning overlap boundary under open versus close semantics.
6. Session ending after PHT midnight and wrong weekday labeling.
7. Forex weekend close versus active Saturday crypto candles.
8. Crypto venue maintenance despite nominal 24/7.
9. XAUUSDT derivatives vs XAUTUSDT/PAXGUSDT token weekend differences.
10. Tuesday–Thursday filter misses actual eligible weekend setups.
11. Monday crypto volatility contrary to Coach forex pattern.
12. Increased overlap volatility but after-cost profit worsening.
13. Higher trade count in US hours but not higher expectancy.
14. CPI scheduled timestamp revised after earlier trading decision; no calendar lookahead.
15. Missing macro calendar must be UNKNOWN, not no news.
16. FOMC statement and later press conference cause separate event windows.
17. Correlated day/hour and trend regimes confound naive comparisons.
18. Sample from earlier pre-ETF years does not transfer to present BTC time-of-day.
19. Signal is triggered intrabar on developing HTF data; anti-repainting needed.
20. No incremental held-out after-cost improvement for a session filter → retain M0.

## Handoff

Next original source N-02 BSP/Philippine stocks charting pages34–35, NOT YET STUDIED; then entire 35-page PDF source-coverage audit. No code, backtest, deployment or old-repository modifications.
