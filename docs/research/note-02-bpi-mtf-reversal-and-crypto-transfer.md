# N-02 Independent Research — BPI Weekly/Daily/4H and Crypto-Ready Reversal Semantics

**Status OPEN RESEARCH, NOT executable Pine code, TradingView chart tests, historical market backtest or verified profitability.** Source: [final Coach PDF pp34–35](../../sources/coach%20trading%20lessons.pdf), [PCSS N-02](../lessons/note-02-bpi-bsp-stock-charting.md). Separate Coach statements and our models.

## Source identity matters

Heading “BSP charting” versus screenshot issuer **BANK OF THE PHILIPPINE ISLANDS PSE:BPI**. BSP is Philippines central bank (source fundamentals: interest rates). Correct ticker before data retrieval. Chart is historical Philippine peso equity, not a cryptocurrency or an issued BSP share. Source screenshot p34 includes EMA settings Length9; Coach actual written instruction p35 says EMA20/50/200. Weekly/Daily/4H chart indicators RSI14. Source labels no complete swing/zone coordinates.

## Core source trend logic and timeframes

Weekly down BOS cited 110–112 and98–100, price under EMA20/50/200, RSI29–30; supports85–86,80–82,75; resistances92–94,98–100,110; FVG/OB98–103,108–112; FVG92–97 possible bounce objective.

Daily still bearish/no CHoCH unless Coach's PHP92 area is broken; 4H consolidation/weakening bearish momentum with temporary bullish possibility on break89.5–90, not an automatic Daily or Weekly reversal. Image RSI ~29.04 Weekly /31.97 Daily /34.63 4H, prices~PHP87.75. No authentic executed trades, stop, target fill, institutional flow or deterministic pivot rules.

## Independent hierarchy vs source

A useful future event representation must separately keep:
- prior trend per timeframe and how its pivots were selected/confirmed;
- observed local momentum phase and whether forming/closed;
- protected swing reference/known-at time, BOS or CHoCH qualification;
- zones (source claim vs independently computed coordinates, formation, touch, invalidation);
- alternate 4H recovery candidate and still-unconfirmed Daily CHoCH;
- separate trade-eligibility and full risk information, WAIT/INSUFFICIENT otherwise.

**Do not count price above EMA and one-bar EMA upward as independent votes when mathematically equivalent for same close-based EMA.** Cross-timeframe contrary states are not automatically errors. RSI oversold may persist in an ongoing downtrend.

## Three independent model alternatives (NOT selected for code)

**M0 source-aligned dashboard:** manually annotated multi-TF trends, textual source zones, possible local bounce, unknown pivot conditions. Highest source fidelity, not automated.

**M1 minimal closed-bar structure detector:** prior known swings and possible LTF break with HTF contradictory/bullish evidence status kept separate. Defines a concise testable baseline but exact swing criterion remains independent.

**M2 state-plus-zones research:** add RSI/EMA, FVG and OB formation, contact/expiry and price-action confirmation, with explicit time-of-evidence and scoring redundancy tests. Complex and easily overfit.

**M3 multi-regime/backtest qualification:** distinguish trend, consolidation, countertrend bounce and confirmed reversal; only select extra rules if after-cost holdout improvement survives different years and venues.

Preference is **M0 then M1**, compare others only after objective rule specifications are agreed, with no coding initiated by this study.

## Data-feed and market structure transfer caution

Official [PSE trading hours](https://www.pse.com.ph/investing-at-pse/) have limited weekday sessions, recess and holidays. PSE 4H aggregation can be very different from 24/7 crypto 4H, depending on candle timestamping and exchange sessions; never assume parity.

Company earnings, BSP rate decisions, stock splits/dividends and adjusted price series can cause different gaps from crypto funding/liquidation/liquidity and gold-backed token contracts. Gold XAUUSDT derivative versus XAUTUSDT and PAXGUSDT token markets require separate symbol and quote identities.

TradingView [request.security and lookahead](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) documents danger of using future HTF close historically, and [repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) documents pivot backdating/real-time bar changes.

## Disconfirming cases to design, not run

1. “BSP” title but PSE:BPI ticker: protect market identity.
2. EMA main input9 screenshot but final EMA20/50/200 instruction.
3. EMA smoothing Length9 versus main EMA Length9 are different settings.
4. Weekly RSI29.04 is strictly under30 though source says nearly oversold.
5. Price87.75 snapshot versus support range85–86.
6. 4H rises above89.5 but not90 on close; threshold definition ambiguous.
7. 4H closes above90 while Daily still below92; local recovery not full reversal.
8. Daily wicks above92 then closes below; wick-vs-close policies disagree.
9. Daily closes above92 without a confirmed preceding LH at92; source-level alone insufficient for mechanical CHoCH.
10. Weekly FVG92–97 overlaps resistance92–94 and cannot independently double-count.
11. FVG/OB98–103 overlaps resistance98–100, not new independent price evidence.
12. FVG/OB108–112 contains major resistance110; no institution identity proved.
13. Price rebounds from oversold Weekly RSI then returns to new low.
14. Earlier bearish BOS pivot only confirmed after displayed break; no hindsight event.
15. 4H PSE chart bar spans lunch/session gap unlike four continuous crypto hours.
16. Ex-dividend/split adjustment changes BPI historical price/EMA/FVG; provenance required.
17. No complete source stop and entry price; RR UNKNOWN.
18. Crypto coin has 24/7 candles but Philippine stock has holidays; weekly close semantics differ.
19. XAUUSDT derivative 4H ≠ XAUTUSDT/PAXGUSDT token liquidity.
20. Higher-TF series fetched with unoffset lookahead leaks future historical values.
21. More confluence rules reduce sample without improving holdout net expectancy.
22. 4H lateral price interpreted as “accumulation” without order-flow proof; preserve tentative label.

All cases planned; NONE EXECUTED. No Pine tests, no live chart behavior and no financial edge claimed.

**Next project milestone:** full-source method reconciliation, then source-scoped rule specifications with explicit causal timing and tests; only after explicit user coding authorization proceed to Pine.
