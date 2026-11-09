# Lesson 09 research — support/resistance and role reversal candidate specification

**Status:** OPEN / RESEARCH-ONLY, no code, Pine compilation, TradingView runtime observation, market backtest, trade execution, or proven improvement.  
**Date:** 2026-11-09 (Asia/Manila).  
**Source hierarchy:** Original [Coach PDF p. 11](../../sources/coach%20trading%20lessons.pdf), PCSS [Lesson 09](../lessons/09-support-resistance.md); official TradingView technical references and all formulas below are **independent enhancements**.  
**Crypto-only implementation mandate:** BTC/ETH-type crypto when selected, plus XAUUSDT gold-reference derivative and distinct XAUTUSDT/PAXGUSDT backed-token markets; actual exchange symbol/product must be verified.

## A. Exact Coach claims — no more and no less

- Support: floor, price may stop falling and buyers may step in, potential upward reaction.
- Resistance: ceiling, price may stop rising and sellers may step in, potential downward reaction.
- Memory aid: support BUY area below, resistance SELL area above.
- **Broken support -> potentially resistance; broken resistance -> potentially support.**
- Buy/sell near these locations **only with confirmation**, e.g., engulfing/rejection.
- Original illustration is an approximately horizontal trading range with red/green horizontal bands and repeated touches, no precise prices or actual crypto market timestamp.
- No definition of minimum touches, pivots, tolerance, timeframe, strength, breakout threshold, retest, expiry, role-flip confidence, or success probability.

## B. Competing zone construction alternatives

### Option A — Manual owner-supplied boundaries

Let user explicitly mark \([a,b]\) on selected exchange-qualified instrument and HTF. Advantage: clear traceability to a human's interpretation; disadvantage: subjectivity, data-entry error, reduced reproducibility, and potential lookahead if drawn after viewing future price.

Temporal requirement: each supplied zone must log **when it was identified**, not simply the bar from which the owner later drew it.

### Option B — Confirmed swing clusters

Identify historical price extrema by a predeclared pivot algorithm; record pivot **event time** and later **confirmation/known-from time**. Cluster a bounded set of confirmed swing prices into support/resistance intervals using a predeclared tolerance. Possible tolerance units: symbol ticks, percentage of price, or volatility-scale (e.g., prior-known ATR). Each choice has transferability tradeoffs.

Pros: reproducible after specification; cons: pivot delay, sensitivity, clustering instability, retroactive updates. A zone derived from a pivot requiring future bars may not validate an earlier candle.

### Option C — Causal rolling extremes / observed touch density

Calculate prior-known rolling highs/lows, perhaps several bands for prior ranges. Pros: simpler and responsive, no future bars. Cons: active bands change frequently, possible false touch events, may diverge from Coach's illustrative repeatedly tested horizontal zones.

### Option D — No automatic zone selection

Only show structural reaction indicators or educational overlays, and keep final zone judgment manual. This is a legitimate simple baseline; can outperform opaque zone algorithms in interpretability without claiming higher trade performance.

No option is selected or accepted as Coach-prescribed.

## C. Geometry of an interval and bar contact

For a price zone \(Z=[a,b]\), \(a\le b\), valid OHLC \(L\le \min(O,C)\le\max(O,C)\le H\):

- **Range intersection:** \(L\le b\) AND \(H\ge a\).
- **Close-in-band:** \(a\le C\le b\).
- **Body overlap:** \(\min(O,C)\le b\) AND \(\max(O,C)\ge a\).
- **Break above candidate:** \(C>b\) (closing threshold), versus \(H>b\) (intrabar/wick threshold).
- **Break below candidate:** \(C<a\), versus \(L<a\).
- **Containment:** high/low fully within zone \((a\le L\land H\le b)\) is a different and more restrictive event.

**Example:** support \([100,102]\), candle low \(99.5\), close \(102.5\). Wick breaks lower boundary but closing price does not. A source label "nabasag" does not determine which interpretation Coach intended.

Boundary equality and tick tolerance must be explicit; comparisons must be stable across currency prices and feed revisions. Missing/nonstandard OHLC must propagate uncertainty, not silent NO TRADE certainty.

## D. Break-and-role-flip state machines, no source threshold

Suggested research states:
- `UNFORMED`: insufficient confirmed levels;
- `ACTIVE_SUPPORT` / `ACTIVE_RESISTANCE`: recognized zone with timestamp;
- `CONTACT` / `REJECTION_CANDIDATE`: subsequent price interacts; confirmation still required;
- `BREAK_PROVISIONAL`: unconfirmed wick penetration / incomplete bar;
- `BREAK_CONFIRMED`: a predeclared completed-bar criterion satisfied;
- `FLIP_CANDIDATE`: a broken zone is watched for the opposite role, but not yet confirmed as such;
- `FLIP_RETESTED`: subsequent price revisits;
- `FLIP_REACTION_CONFIRMED`: post-break reaction meets agreed source-compatible confirmation;
- `INVALIDATED` / `EXPIRED`: failed or stale zones.

These names and transitions are **our inventions**, not Coach quotes. Variants must compare (1) break alone, (2) break+retest, (3) break+retest+directional confirmation. More cautious variants reduce false signals but add delay and may miss moves.

## E. Source cross-lesson consistency question

Lesson 07 cautions against sideways trading without meaningful HTF context; Lesson 08 demands trend/bias+zone and confirmation. Lesson 09 illustration depicts price bouncing within a range and the mnemonic "buy at support, sell at resistance". This **is an educational zone illustration**, not necessarily a complete range-trading authorization. Leave sideways-mode implementation and countertrend trading **OPEN** until the full source is studied and decisions are explicitly differentiated.

## F. Causal correctness and drawing considerations

A zone must store:
- source exchange/market-product and timeframe (e.g. exact XAUUSDT derivative venue rather than assuming same as a gold token);
- `created_from_bar` and `known_at_bar/time`;
- boundaries \([a,b]\), origin method and parameters;
- active/broken/flipped/pending/invalid state, last update timestamp;
- chronological contact, confirmation and event attribution;
- data quality and missing-history status.

TradingView official docs:
- [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) warns against creating pivots after several later bars and then plotting them into the past as if they were known immediately.
- [Lines and boxes](https://www.tradingview.com/pine-script-docs/concepts/lines-and-boxes/) provides script drawing primitives for zone bands and states; lines/boxes have finite counts and garbage collection.
- [Strategies](https://www.tradingview.com/pine-script-docs/concepts/strategies/) warns about lookahead bias and misleading trading simulations.

Do not claim code is non-repainting before actual Pine compilation, live/reload comparisons, and timestamp tests.

## G. Future planned discriminating tests — not yet executed

1. Known earlier two-bounce support, third confirmed contact -> time-causal support report.
2. Support known only from pivots confirmed later -> do not backdate earlier setup eligibility.
3. Price enters band by wick, closes outside -> differ between range touch and close touch.
4. Price closes below former support -> break candidate; check no immediate promise of successful resistance role.
5. Quick wick below support then rebound -> fake breakout alternative; no automatic permanent role reversal.
6. Price closes above resistance, retests and rejects downward vs bounces upward -> different flip validation states.
7. One-bar spike/low-liquidity crypto wick -> compare zone algorithm robustness with a prior-known volatility measure.
8. Equal highs/lows, merged bands, overlapping support and resistance -> ambiguous/no forced decision.
9. User changes instrument from Binance XAUUSDT to a PAXG/XAUT market -> existing zones must not persist as if price scales/feeds matched.
10. A figure visually shows an eventual bounce, but level was selected only *after* viewing that bounce -> reject hindsight-valid signal claims.
11. Sideways LTF, bullish HTF vs sideways both -> preserve context rather than guessing source authorization.
12. Stop lies inside support zone, contradicting Lesson 08 SL-below-zone rule.
13. Repeated contacts without any LTF confirmation -> remain WAIT / NO TRADE despite zone quality.

**Candidate evaluation:** predeclare market/timeframes/costs/zone algorithm and benchmark against manual prior-day high/low or simple rolling extremes. Compare event timing, signal frequency, out-of-sample after-cost performance, false breakouts, latency, complexity and interpretability. H0 is no incremental edge of complex zone algorithm vs simple causal bands.

## H. Ponder conclusion and hard boundaries

**Working direction:** Make S/R *stateful, causal price intervals*, not automatically triggered eternal horizontal lines. A break can change status while a role flip remains a separate hypothesis requiring evidence. Prefer transparent WAIT/INSUFFICIENT states to unverifiable predicted bounces.

**Unresolved:** zone source and width, importance/strength weighting, touch count, HTF swing selection, breakout definition, retest requirement, invalidation/expiry, conflict resolution, data access and actual performance. Do not select numerical constants from this page.

**Next PCSS:** Lesson 10 — Marking a Support and Resistance on a Time Frame, original PDF pages 12–13. Coach provides explicit example zones and proposed trading scenarios there; study in original order at user request.
