# Phase 2 M07–P1 — Evaluation, Falsification and Acceptance Design for M05 Context States

**2026-11-11 Asia/Manila | Research/validation PROTOCOL ONLY. No runner, no replay, no Pine, no trading, no performance sample.**
**Inputs:** [R1 structural arming](04-reference-arming-and-pivot-order.md), [R2 zone-to-reaction](05-zone-contact-reaction-timing.md), [R3 candle grammar](06-candle-pattern-and-confirmation-grammar.md), [R4 multi-timeframe state](07-mtf-context-conflicts-and-causal-states.md), [reconciliation register](../METHODOLOGY_RECONCILIATION.md), original [Coach PDF](../../sources/coach%20trading%20lessons.pdf) SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730.

## A. A single result must not masquerade as four kinds of verification

| Evidence layer | What can actually be checked | What it cannot certify | Current state |
|---|---|---|---|
| E0 SOURCE FIDELITY | coach wording, figures, source-order, scenario distinction, source vs student claims, page references | profitable entries or a unique numeric FVG/RSI formula | studied PDF and selected pages rechecked; 26 PCSS units exist |
| E1 FORMAL LOGIC | definitions, contradictions, edge-case proofs, constructed expected classifications | that a computer implementation follows them | 140 written case rows across R0–R4; no runner |
| E2 SYNTHETIC EXECUTION | later deterministic bar/event fixtures run on actual code, timing and reset/reload invariants | predictive performance in real venues | NOT AUTHORIZED OR EXECUTED |
| E3 REAL MARKET RESEARCH | later fixed-venue, fixed-pair, historical as-of backtest with fees/funding, baseline/ablation, holdout | broker execution identity, future returns, guaranteed edge | NOT AUTHORIZED OR EXECUTED |
| E4 TRADINGVIEW ACCEPTANCE | later actual Pine compilation, chart reload/realtime behavior, visible labels, alert behavior as permitted by account | external broker orders/returns | NOT AUTHORIZED OR EXECUTED |

**Current case inventory:** [M01 base](01-causal-market-structure.md) 16, [entry/risk](02-topdown-entry-state-and-risk.md) 20, [M02 zones](03-zones-sr-ob-fvg-fibonacci.md) 20, [R1](04-reference-arming-and-pivot-order.md) 16, [R2](05-zone-contact-reaction-timing.md) 18, [R3](06-candle-pattern-and-confirmation-grammar.md) 20, [R4](07-mtf-context-conflicts-and-causal-states.md) 30 = **140 paper-designed rows, 0 executed test cases**. Some rows intentionally overlap; 140 is an inventory count, **not** 140 independent findings.

## B. Source-anchored qualitative acceptance cases: not candles from a live venue

| PDF evidence | Source-observed case | Non-negotiable interpretation target | Data limitation |
|---|---|---|---|
| p6 | HTF 1H/4H trend+zone and LTF 5m/15m confirmation | keep trend/location and entry timeframe separate; no forced one-pair-only universe | no full OHLC timestamped dataset |
| p9–10 | trend+zone+signal, no zone contact -> NO TRADE, confirmation closes | keep WAIT_ZONE and WAIT_CONFIRMATION distinct | numeric zone and candle algorithms absent |
| p18 | SOL 4H UP, 1H weakening, 15m bearish scalp, plus separate aligned LONG | retain source-recognized countertrend/scalp branch, not global HTF flip | no full trade accounting or fill evidence |
| p21/p24 | bullish/bearish continuation templates with EMA/RSI and LTF pullback reaction | distinguish conditions as observed context vs independently selected hard gates | RSI lookback/bounce ambiguity, EMA redundancy |
| p27–28 | 4H strong bullish TON/RSI ~97, Coach says wait for pullback | overbought context can coexist with UP; no automatic SELL or chase | 1H/15m source claims not all separately pictured |
| p30 | bullish Q&A1 structure/EMA/RSI supports continuation unless bearish confirmation | avoid numerical probability and inevitable continuation claims | no probability estimates provided |
| p31 | 30m FARTCOIN OB proposed and 5m reaction; source separates student's already-open trade | do not relabel proposed Coach levels as actual executed entry | no verified execution |
| p32 | BTC 4H down + 15m consolidation; conditional SHORT rejection or LONG breakout | opposite **conditional** branch statuses, no simultaneous orders | screenshots are historical source case, not tick feed |
| p35 | BPI daily still bearish/no CHoCH, 4H possible bounce | timeframe-relative change and equity vs crypto distinction | no BPI candle dataset, no crypto translation of peso levels |

**Important:** A single discretionary source example is insufficient to adjudicate a numeric pivot span, wick ratio, RSI slope, zone mitigation or backtest expectancy. A human/source annotation should be labelled “qualitatively compatible”, “incompatible”, or “insufficient information”, never forced into ground-truth precision on unobservable candle history.

## C. Predeclare comparison candidates before seeing historical returns

| Dimension | Baseline candidate | Challenger | Evidence to adjudicate |
|---|---|---|---|
| Structural reference | R1-A frozen/armed, prebreach suppress | R1-B reset/re-cross; R1-C manual | event freshness, late detection, source-relevant cases |
| Contact-to-reaction | R2-A separate closed reaction bar | R2-B same closed contact/reaction | event sequencing, missed source patterns |
| Candle geometry | EN-BODY engulf + follow-through variants | EN-RANGE, wick/body ratio, strong body | label disagreements by location and timing |
| MTF information timing | MTF-T0 context frozen at LTF open | MTF-T1 context known by decision close | no HTF future leakage, timestamp fidelity, detection delay |
| Conflict architecture | M05-A separate state vector and profile branches | M05-B weighted vote, M05-C unanimity, M05-D manual | expressive fidelity, false auto-veto, readability |
| Market instruments | each qualified venue product separately | pooled or transferred candidate | no unsupported pooled levels; venue invariance is a test question |

**Default research priorities are engineering preferences, not discovered profitability rankings.** Particularly, a stricter baseline may sacrifice many legitimate cases; record that cost rather than declare conservatism universally best.

## D. Invariants to be converted into executable assertions only when separately authorized

1. **As-of snapshot:** every supporting HTF/LTF bar, swing, zone and reaction has available_at <= decision_at.
2. **No backdating:** prior-event labels must never be newly created with event time earlier than their own source known_at.
3. **No mutable past:** processing a new 4H bar may revise current interpretation, not the prior recorded snapshot from a 5m bar.
4. **Stable symbol:** event must share an exchange-qualified product/feed identity; XAUUSDT perpetual != XAUTUSDT spot != PAXGUSDT.
5. **Wait means wait:** in Lesson08 template absent eligible contact => no entry candidate; absent closed LTF reaction => WAIT.
6. **Contrary LTF:** opposite LTF structure does not instantly flip 4H regime.
7. **CHoCH scope:** LTF possible change never equals HTF confirmed reversal without independent HTF evidence.
8. **Missing != false:** unavailable required RSI/HTF is INSUFFICIENT, not bearish; optional absent RSI does not automatically veto.
9. **Conflict preservation:** simultaneous opposing conditional candidates retain both individual reasons; no implied simultaneous actual positions.
10. **Indicator context distinct:** duplicated transformations such as same close above EMA and positive one-bar EMA slope are not two independent score votes.
11. **Invalidation priority:** candidate invalidation stops its current entry readiness; previous historical state is preserved.
12. **Zero actual PnL until execution simulation:** no source chart or hypothetical RR produces a verified return.
13. **Timeframe scheduling:** a newly ending 4H bar cannot govern an earlier 5m candle under MTF-T0; MTF-T1 only after its verified availability.
14. **Intra-bar order unknown:** a candle OHLC range does not prove order placement/fill price or which touched level first.
15. **A known unresolved ambiguity remains labelled:** do not silently invent exact candle ratio, range breakout method, session schedule or OB color criterion.

## E. Manual adjudication worksheet (future procedure; none executed here)

For each source example or eventual frozen, verified OHLC case, the record should include:
- case_id, case family, original PDF page or dataset origin; source quote/figure or bar IDs;
- exact instrument_key/venue/type, timeframe schedule and timezone, snapshot decision_at;
- observed full bars and availability times, unconfirmed bars explicitly excluded;
- Coach literal assessment **versus** analyst annotated state; any field not evidenced = UNKNOWN;
- chosen candidate hypothesis IDs (R1/R2/R3/R4), parameters and input checksum *before outcomes are observed*;
- expected gate status, competing valid interpretations and negative-case reason;
- later actual observed indicator outputs (only after authorized implementation) and whether they match;
- disconfirmations, correction date, version and linked commit.

For a blind human review, show only information available at the case's historical decision boundary, and withhold forward outcomes. Use **ambiguous/insufficient** as valid labels rather than forcing a win/loss or BUY/SELL answer.

## F. Later empirical-study design (proposal only)

Once implementation permission exists: choose each instrument+venue contract explicitly; preserve real historical feed boundaries; exclude forming candles; segment by market regimes and dates; fix candidate parameters before evaluating held-out periods; account for actual fees, slippage, funding and position-size/margin constraints; measure event timing, false positives relative to adjudicated labels, missed source-style cases, coverage/abstention rates, model disagreements, and **after-cost** strategy outcomes only with an expressly defined execution model. Compare a simpler baseline and ablations (including remove RSI, remove EMA, remove FVG/OB, remove additional confluence) to determine whether complex conditions add incremental evidence.

No numerical win rate, lift, p-value, confidence interval, trade count, reward-to-risk distribution, profitability, drawdown, Sharpe ratio or actual backtest assertion is available at this stage. Repeatedly tuning rules on the same sample compromises holdout independence; preserve hypothesis versions.

## G. Future TradingView technical acceptance plan (NOT performed)

- Verify true higher timeframe vs chart timeframe; reject or explicitly handle unsupported inverse mappings.
- Verify HTF data non-leakage. TradingView's [other-timeframes docs](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) illustrate using a historical expression offset with lookahead-on for stable, last-confirmed HTF requests. Do NOT assume simply using lookahead-off makes realtime HTF values fully confirmed.
- Verify historical/real-time reload parity, event-time vs drawing-time, HTF context at LTF boundary and pivot confirmation latency.
- Verify visible panel reasons and no misleading order/fill/guarantee claim, chart switching across BTC/ETH and gold-related variants, resource limits, and Basic-plan account capabilities when actually tested.
- Preserve account-plan restrictions as a later measured fact, not infer that alerts currently work or do not work in this NEW project.

## H. Stop/advance decision

**This document is an accepted research *protocol draft*, not an approved production rule set.** Phase 2 can continue to M03 RSI/EMA semantics and M06 risk/market microstructure; before implementation approval, each chosen candidate needs precise parameter domains, source interpretation, timing semantics, disconfirming synthetic cases, and a feasible actual verification method. The subsequent implementation/test phase remains separately authorized by the owner, not implied by this study.

**Source hierarchy preserved:** original PDF -> PCSS interpretation -> independent formal candidates -> future valid evidence. No code, no automated tests, no backtest or deployment.
