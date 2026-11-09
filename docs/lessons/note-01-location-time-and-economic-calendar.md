# PCSS Note N-01 — Important Note on Location and Time

**COMPLETE for source study and independent research, 2026-11-09 Asia/Manila.** Sole Coach primary source: [coach trading lessons.pdf, page 33](../../sources/coach%20trading%20lessons.pdf). SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. Private personal PCSS file SHA-256 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56, not committed. **NO Pine implementation, market backtest, trading or deployment.**

## A. Original PDF inventory

Original p33 is ONE text-only Taglish note, visually inspected and native text compared. No original figure, chart, exact numerical strategy, demonstrated statistics, theorem, mathematical formula or exercise. Page32 completes Q&A3; page34 begins BSP charting (separate, NOT YET STUDIED). All 21 source units are preserved in order:

| ID | Coach's item (exact source order) | Evidence qualification |
|---|---|---|
| N01-01 | Title Important Note on Location and time | Single text-only source page |
| N01-02 | For forex major pairs and gold | Explicit forex/gold, NOT crypto market instruction |
| N01-03 | Tuesday to Thursday preferred days | No proven win-rate comparison |
| N01-04 | Strongest movement and volume often there | Qualitative Coach assertion |
| N01-05 | Times stated from the Philippines | PHT frame |
| N01-06 | London session around 3PM–12AM | Approximate summer-time schedule |
| N01-07 | New York session around 8PM–5AM | Approximate summer-time schedule |
| N01-08 | London+NY overlap around 8PM–12AM | Not all-year fixed |
| N01-09 | Overlap more volatile for GBP/USD, EUR/USD, Gold | Forex/gold focus |
| N01-10 | Monday often ranging/slow after weekend open | Not 24/7 crypto rule |
| N01-11 | Friday profit-taking caution | Source qualitative |
| N01-12 | Friday manipulation or sudden reversals after NY | Coach characterization, not proven manipulation |
| N01-13 | High-impact news may be useful | No mandatory news blackout stated |
| N01-14 | CPI | Named macro event |
| N01-15 | NFP | Named macro event |
| N01-16 | FOMC | Named macro event |
| N01-17 | Interest Rates | Named macro event |
| N01-18 | Check economic calendar before sleeping/charting | Pre-trade preparation |
| N01-19 | Check major news for following day | Not a live-calendar integration contract |
| N01-20 | Forex Factory as news/calendar source | Original named resource |
| N01-21 | Investing.com economic calendar | Original named resource |

## B. Coach's weekday advice — source explicitly FOREX majors & gold

**COACH_EXPLICIT:** “For forex (major pairs & gold),” Coach prefers **Tuesday–Thursday**, believing they have stronger movements and volume. **Monday** can be slow/ranging after the weekend reopening. **Friday** warrants care regarding profit-taking, reversals or what Coach calls manipulation, particularly after NY session.

**PCSS meaning:** Traditional forex follows a weekday/weekend trading structure. But strong turnover/volatility is not equivalent to positive net expectancy, and the PDF gives no sample, win rate, volatility statistics, spread/slippage measurement or objective weekday rule. “Friday manipulation” is not independently verified market manipulation from this source.

**INDEPENDENT CRYPTO QUALIFICATION:** Many crypto products can trade seven days a week, subject to venue-specific maintenance and contract restrictions. A gold-linked crypto derivative XAUUSDT, tokenized-gold XAUTUSDT, PAXGUSDT and FX gold XAUUSD must not be assumed to share exchange hours, underlying liquidity or empirical weekday effects. Forex Tue–Thu is not an accepted restriction for crypto. Example venue distinction: [OANDA FX vs crypto operating hours](https://www.oanda.com/us-en/trading/hours-of-operation/).

## C. London/New York — original Coach PH times, then separate DST correction

**COACH_EXPLICIT:** In Philippine Time, **London around 3PM–12AM**, **New York around 8PM–5AM**, their **overlap around 8PM–12AM**. Coach sees this as especially volatile for **GBP/USD, EUR/USD and Gold**.

**INDEPENDENT MATH/CALENDAR CONTEXT:** Those are approximately aligned summer/DST conventional local financial-city session hours, not year-round PHT facts. Conventional 08:00–17:00 local windows convert as:

| Season with both cities aligned | London PHT | New York PHT | Overlap PHT |
|---|---|---|---|
| Both on summer/DST | 15:00–00:00 | 20:00–05:00 | 20:00–00:00 |
| Both on winter/standard time | 16:00–01:00 | 21:00–06:00 | 21:00–01:00 |

The Philippines remains UTC+08. UK and US DST transitions occur on DIFFERENT dates in spring/autumn, producing mixed-week cases that must use actual zone-date conversion. For **2026-11-09**, using IANA timezone data: 08:00 London → 16:00 PHT; 08:00 New York → 21:00 PHT; approximate London/NY overlap **21:00–01:00 PHT**. Reference [BabyPips forex hours](https://www.babypips.com/tools/forex-market-hours) and [OANDA forex sessions](https://www.oanda.com/us-en/skills-and-insights/education/trading-asset-classes/forex/when-is-the-best-time-for-forex-trading/).

This validates a **seasonal caveat**, not Coach source wording for every winter. The source does NOT prove a session-dependent profitable crypto trading strategy; volatile overlap may also increase whipsaws, slippage and position risk.

## D. High-impact news checklist, preserved in source order

**COACH_EXPLICIT:** High-impact news can be significant; lists **CPI**, **NFP**, **FOMC** and **Interest Rates**. Advises checking an **economic calendar before sleeping/charting** to know what major news is scheduled tomorrow. Names **Forex Factory** and **Investing.com economic calendar**.

**INDEPENDENT PREREQUISITE MEANINGS:**
- CPI: Consumer Price Index measuring inflation. [BLS CPI calendar](https://www.bls.gov/schedule/news_release/cpi.htm).
- NFP: Nonfarm Payrolls, commonly reported in the US Employment Situation. [BLS jobs calendar](https://www.bls.gov/schedule/news_release/empsit.htm).
- FOMC: Federal Open Market Committee, responsible for US monetary policy decisions. [Federal Reserve meetings](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm).
- Interest-rate announcements: decisions/communications by central banks affecting rates and associated assets.

**Do NOT invent:** Coach does not specify a mandatory no-trade before/after-news window, exact event timestamp, automatic calendar access, a guaranteed trade direction, a quantified win-rate uplift, or a rule to trade news immediately. His original “best din if may high impact news” is an observation about conditions plus a preparation habit, not a universal event blackout.

**INDEPENDENT risk:** High-impact events can produce sharp moves and frequent reversal; the first research design should make known scheduled events visible rather than automatically label trades as valid or invalid without a tested rule.

## E. Independently researched crypto transfer — separate from Coach

- [Brauneis et al., 2025](https://link.springer.com/article/10.1007/s11156-024-01304-1), 1,940 crypto pairs and 38 exchanges, find nonuniform intraday volatility/volume/liquidity; their sample's activity peak is around 16–17 UTC, not universally best for each market.
- [Coinbase Institutional, 2024](https://www.coinbase.com/institutional/research-insights/research/market-intelligence/trading-activity-from-a-us-lens) observes prominent US-hour BTC activity, not validated profitable entry rules.
- [Aldhahi, 2026](https://www.mdpi.com/1911-8074/19/9/707) reports BTC volatility concentration shifting toward US hours in Kraken BTC/USD hourly history 2016–2025, which may not transfer to a Binance derivative or gold token.
- [2026 FOMC crypto study](https://www.sciencedirect.com/science/article/pii/S1544612326006021) reports elevated BTC/ETH volatility and turnover around scheduled statements, not proof of directional forecasting alpha.

**Inference:** 24/7 crypto market activity is not uniform, but source forex weekday and session rules must be tested separately with instrument-specific OHLC/volume, costs and historical timing before any signal filter.

## F. Causal implementation research (NOT code)

[TradingView sessions](https://www.tradingview.com/pine-script-docs/concepts/sessions/) and [time zones](https://www.tradingview.com/pine-script-docs/concepts/time/) support IANA timezone names. Future context features should use **Europe/London** and **America/New_York** for DST-aware local windows; **Asia/Manila** for display; UTC timestamps for durable computation. The chart timezone may differ from the exchange timezone. Declare whether 15m bars are classified by opening/closing instant when straddling boundaries.

Potential informational fields (hypotheses only): venue-qualified symbol/product, weekday, London/NY/overlap/other, economic event source/date/time known-at, unknown event schedule, measured ATR/volume distribution. Do not claim a real-time CPI calendar is integrated with Pine: calendar availability and public known-at revisions require separate verification.

## PCSS recap and completion status

Coach recommends Tue–Thu and London/NY overlap for **forex majors and gold**, and checking calendars for CPI/NFP/FOMC/rates. Original PH time windows are approximate, seasonal. Independent crypto research supports measuring time-of-day effects, **not imposing those forex preferences directly** or asserting high volatility equals profitable trades. All **21** page-33 source items audited; page 33 has no figures/proofs/exercises. **Note N-01 COMPLETED at study level**. All 21 numbered lessons and Q&A1–3 previously completed. **Note N-02 BSP charting, pages34–35 NOT STUDIED**. Whole PDF not complete.
