# Integrated research candidate v0.1.4

**D-032/D-033 · 2026-11-13 PHT · Candidate on draft PR #2.** The accepted private release is still v0.1.3. The experimental extension is in [the new Pine source](../../pine/alpha-engine-research.pine). It runs on standard Binance Spot PAXGUSDT 5m candles. The existing Lesson 08 inputs, decisions, and M01 probe are preserved in the candidate body.

## What runs

| Component | Provenance and implementation |
| --- | --- |
| I1 structure | **COACH_EXPLICIT** PDF pp. 9, 15–16 and 25 supplies trend, continuation and possible-shift concepts. **AI_INDEPENDENT_EXPERIMENTAL** strict 2/2 by default, same-side and dual ambiguity reset, recent four alternating pivots, one-use R1-A or R1-B closed crossings. A possible shift requires a new post-event four-swing sequence. |
| I2 locations | **PCSS_INTERPRETATION** p. 10 treats prior support as context. **AI_INDEPENDENT_EXPERIMENTAL** latest protected HL plus configurable tick tolerance, one three-bar gap with later geometric overlap, one prior opposite-body candle range admitted at a continuation crossing and retired on a wrong-side close, and 50/61.8/70.5 retracement levels on an ordered leg. The OB candle-color convention is independent. The p. 14 example alone does not prescribe it. Role reversal, separate ranked supply/demand zones and multi-zone lifecycle are deferred. |
| I3 filters | **COACH_EXPLICIT** pp. 10, 17–18 and 20–24 discuss candle confirmation, EMA and RSI context. **AI_INDEPENDENT_EXPERIMENTAL** EMA20/50/200 ordering, RSI14 context, strict real-body engulfing, and an optional bullish lower wick at least twice the body with close beyond the zone. Momentum is descriptive. |
| I4 workflow | **COACH_EXPLICIT** pp. 6 and 10 establish higher-timeframe context then lower-timeframe reaction at location. **AI_INDEPENDENT_EXPERIMENTAL** aligned prior completed 1H and 4H EMA20/50, prior-open armed 5m support, same-closed-bar geometric contact/reaction, WAIT, REASSESS and INSUFFICIENT. The accepted declared-setup R2 comparators remain separately available. Broader 15m, range and countertrend workflows are deferred. |
| I5 geometry | **PCSS_INTERPRETATION** p. 10 and existing M06 risk spec. **AI_INDEPENDENT_EXPERIMENTAL** candidate close, one tick below the support floor, armed high as target, nominal reward/risk only for valid price order. No sizing, fees, fills or expected returns. |

## Verified scope

- Build `AE-0.1.4-93081cd2faee`, Git blob `5f2ef2aebd2291e87067e8183796c665768eccf2`, SHA-256 `1c93604857281b3c3fd673d6d30ca7a33178e43f76b20a6a40cd29ebbdf17235`.
- **PASS:** 84 local standard checks and 21 separately executed historical structural research checks. The standard suite includes four candidate source checks, the I1 frozen receipt replay, and the preserved baseline. The source tests establish unchanged Lesson 08 body and assert code boundaries. They do not execute Pine.
- **PASS:** TradingView readback of the full unsaved editor matched the candidate after CRLF to LF normalization, and the exact build compiled and displayed on the qualified chart. On the Nov 12 23:35 UTC closed cutoff, the panel showed possible shift, an earlier 19:05 UTC downward CHoCH candidate at 3878.85, down-aligned 1H/4H EMA context and RSI 51.3. Latest bear gap displayed a geometric test; the supply block remained open. Those are native chart observations, not independently verified venue receipt order.
- **OPEN_UNRESOLVED:** native pattern/lifecycle stress cases, same-input toggle and reload parity, and private saved-script durability. The existing private script was not replaced. The integrated file is a release candidate, not the accepted private release.

The higher-timeframe request uses the prior bar for every requested expression. The visible close timestamp is a chart-clock boundary. See [TradingView's timeframe guidance](https://www.tradingview.com/pine-script-docs/faq/other-data-and-timeframes/) and the [I1 contract](../research/phase3-6-structural-reference-contract.md).
