# Lesson 11 — Order Block, BOS and CHoCH: independent design candidates

**Status:** RESEARCH PROPOSALS ONLY; not final Coach method, not implemented, not compiled, not empirically backtested.  
**Date:** 2026-11-09, Asia/Manila.  
**Coach authority:** [Original PDF p.14](../../sources/coach%20trading%20lessons.pdf); [completed source study](../lessons/11-order-block-bos-choch.md).  
**Owner scope:** crypto, including distinct venue-qualified XAUUSDT, XAUTUSDT, PAXGUSDT. Other projects remain unrelated and untouched.

## Verified source facts (not inferred)

- OB = **last candle before a strong pump or drop**, associated by Coach with large-money participation and hoped-for reaction on revisit.
- Figure bullish OB is **green candle 1** near a Swing Low with later blue candles 2–3 rising; bearish OB is **red candle 1** near Swing High with later orange candles 2–3 declining. Both draw a shaded region, note "1→3 GAP", and show a green check.
- Coach's BOS NOTE says mark a BOS based on a **break of previous HH or LL** only after recognizing market structure (notes HH/HL).
- **BOS = trend continuation**. **CHoCH = possible trend reversal**.
- No exact objective strong-move threshold, zone band construction, gap formula, break condition or historical probability.

## 1. Avoid imported OB polarity conventions

Some external market-structure literature calls last bearish candle prior to upward impulse a bullish OB; last bullish before downward impulse a bearish OB. **Do not automatically impose that convention here** because Coach's actual figure labels green bullish candle 1 and red bearish candle 1.

Candidate comparators:
- **Source-illustration polarity**: accept visually shown same-direction candle 1 if preceding valid displacement and swing context match.
- **Source-text neutral**: last candle of any color before strong qualifying move (closest to literal Coach wording).
- **Opposite-color outside baseline**: independently compare a common alternative, clearly label **NOT sourced from Coach**, and exclude from claimed Coach parity.

No option is finalized as executable code.

## 2. OB bounding and displacement alternatives

Use OHLC of candidate candle \(t\): \(O_t,H_t,L_t,C_t\).
- **Full wick interval**: \(Z^{wick}=[L_t,H_t]\).
- **Real body interval**: \(Z^{body}=[\min(O_t,C_t),\max(O_t,C_t)]\).
- **Hybrid half-body/edge**: only if explicitly specified and tested as an enhancement; no such rule from source.

A subsequent move could be defined through:
- largest body/range of next K completed candles relative to prior-known ATR;
- close displacement from candidate's extreme normalized by prior-known volatility;
- predefined number of candles and cumulative directional price movement;
- optional three-candle gap geometry inspired by source's "1→3 GAP" picture, but neither a gap definition nor its necessity is Coach-defined.

**Design constraint:** confirm at time \(t_{\mathrm{known}}\) after the necessary post-candle observations are completed. Do not call it a source-confirmed OB on candle 1 while candles 2/3 are still future.

## 3. Independent three-candle gap research — not a Coach FVG rule

If selecting a generic bullish three-candle high/low non-overlap criterion:
\[
L_3>H_1
\]
and bearish variant:
\[
H_3<L_1.
\]
This is a **possible independent interpretation of gap-like geometry**, not Coach's p.14 definition, and may not exactly match the figure's dashed-body markings. Use standard OHLC with a clear time order and instruments with valid bars. Body gaps and wick gaps are distinct and may disagree. Never claim every OB demands a fair value gap based solely on one figure's "1→3 GAP" label.

An image-explained relation can be useful despite having no empirically demonstrated power; absence of precise source definition means no mandatory numeric rule.

## 4. Structure and break model candidates

At each analysis bar, maintain a set of **confirmed, causally knowable** pivot extrema and trend states from a separately defined swing detector. Candidate event fields:
- instrument/venue/product/timeframe;
- relevant prior swing high/low value and when it became *confirmed*;
- trend state as known before break;
- break direction, wick-vs-close criterion, close timestamp, equality/tick buffer;
- new label **BOS / CHoCH / INSUFFICIENT** and source-policy provenance.

Possible classifiers (independent, not necessarily fully Coach-equivalent):
- UP trend and break prior relevant high upward -> bullish BOS continuation candidate;
- DOWN trend and break prior relevant low downward -> bearish BOS continuation candidate;
- UP trend and break protected relevant low downward -> bearish CHoCH possibility;
- DOWN trend and break protected relevant high upward -> bullish CHoCH possibility;
- MIXED or insufficient pivots -> UNKNOWN, not forced direction.

**No strict bar lookback, protected swing definition, CHoCH confirmation requirement or wick/close policy is in page 14.** Full subsequent source (Lesson 12 and later CHoCH section if present) must be read before finalizing any classifier.

## 5. Time-of-knowledge / no repaint test ideas

Example: candle 1 happens on bar \(t\), candles 2/3 show qualifying impulse. Label can visually anchor at bar \(t\), but it must record known-at bar \(\ge t+2\) if two later candles are required. Similarly, a pivot requiring two right-side bars is knowable only after those two bars close. Signal eligibility requires all prerequisites to be known before the signal.

Official technical references:
- https://www.tradingview.com/pine-script-docs/concepts/repainting/
- https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/
- https://www.tradingview.com/pine-script-docs/concepts/lines-and-boxes/
- https://www.tradingview.com/pine-script-docs/writing/limitations/

Do not claim no-repaint behavior before genuine Pine realtime/reload observations after implementation.

## 6. Discriminating future fixtures (NOT executed)

1. Green candle 1 near swing low and strong upward candles 2/3: must not be rejected solely by imported "bearish last candle" convention.
2. Red candle 1 near swing high and strong downward candles 2/3: same mirror check.
3. Large move with no recognized swing level: OB possible under text-only method, image-confluence uncertain.
4. Small drift, no large displacement: no qualified OB under thresholded variants; threshold unspecified.
5. Candle body zone differs materially from wick zone; revisited price touches only one; preserve variant.
6. Three-candle illustrated gap absent: whether OB invalid depends on chosen optional gap hypothesis, not Coach.
7. Prior bullish HH not confirmed until several bars later: earlier apparent BOS cannot be backdated.
8. Uptrend breaks a known high at wick but closes back below: divergent wick/close BOS classifications.
9. Uptrend breaks relevant low, then recovers: possible CHoCH under break variant, no guarantee of sustained reversal.
10. Mixed/sideways structural state: do not manufacture BOS or CHoCH without context.
11. OB identification precedes alleged strong candles: must be provisional, not historically confirmed at origin.
12. Price never revisits candidate OB: no confirmed zone reaction or automatic BUY/SELL.
13. Zone returns after expiry/mitigation: state depends on predeclared policy, not infinite validity.
14. Multiple successive candidates inside impulse: ambiguous "last" selection requires deterministic tie policy.
15. XAUUSDT derivative chart data differs from XAUTUSDT/PAXGUSDT spot: do not copy OB zones across feeds.

## 7. Ponder recommendation / strongest alternative

**Default research direction:** preserve two layers—**source-faithful recognition** (last candle before strong move; structure-first BOS; CHoCH only possible reversal) and **explicit experimental formalization** (what qualifies as strong; wick/body bounds; break and time rules). Only after complete Coach source study should thresholds be selected against time-causal test evidence.

**Strongest simpler alternative:** do not automatically draw OB at all initially; show well-validated structural swings and let an analyst manually mark source-style OB regions. This avoids false precision but is less automatic and reproducible. Compare complexity and errors before choosing.

**Unresolved:** authoritatively defined displacement, order attribution, polarity, gap necessity, zone expiry, retest and reaction criteria, pivot method, BOS/CHoCH break triggers and relative precedence. Preserve UNKNOWN/WAIT rather than inventing signals.

**No code authorized or made. Next:** Lesson 12 — BOS (Break of Structure), original PDF pp.15–16.
