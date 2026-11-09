# Research candidates — Lesson 02 candlestick classification

**Status:** PROPOSED / OPEN_UNRESOLVED; neither a Coach rule nor a coded implementation.  
**Source cross-reference:** [Lesson 02](../lessons/02-basic-candlestick-patterns.md) and original [PDF pages 2–3](../../sources/coach%20trading%20lessons.pdf).  
**Owner scope:** crypto with explicitly included XAUUSDT, XAUTUSDT, PAXGUSDT.  
**Date:** 2026-11-09.

## Principle

Three independent layers must not be conflated:
1. **Morphology**: measurable OHLC shape alone.
2. **Context**: preceding trend, level/zone interaction, instrument/feed characteristics.
3. **Decision**: confirmed candle, required subsequent confirmation and risk controls — to be specified from later Coach lessons and independent testing.

## Exact mathematical primitives

For OHLC \(O,H,L,C\):
\[
B=|C-O|,\quad U=H-\max(O,C),\quad D=\min(O,C)-L,\quad R=H-L=B+U+D.
\]
Only use normalized candle-shape ratios when \(R>0\). Bar validity requires numeric finite OHLC and \(L\le\min(O,C)\le\max(O,C)\le H\). Treat \(R=0\), missing OHLC, or unconfirmed realtime bars explicitly rather than manufacturing a signal.

Proposed normalized shape metrics: \(b=B/R,\ u=U/R,\ d=D/R\), so \(b+u+d=1\) for valid \(R>0\).

### Possible criteria to investigate — illustrative, NOT FIXED

- **Hammer shape**: \(d\ge d_\text{min}\), \(u\le u_\text{max}\), \(b\le b_\text{max}\); test whether a body/wick ratio (such as \(D\ge2B\)) adds anything or is unstable near \(B=0\).
- **Shooting Star / Inverted Hammer shape**: \(u\ge u_\text{min}\), \(d\le d_\text{max}\), \(b\le b_\text{max}\). Which name applies depends on **preceding** trend/context, not current candle color alone.
- **Doji shape**: \(b\le b_\text{doji}\), subject to tick-size and low-volatility degeneracy; note some dojis may also satisfy hammer/star silhouette tests.
- **Ambiguous cases**: explicitly prioritize/deconflict multiple labels; propose no signal when meaning cannot be resolved or thresholds conflict.
- **Tick-size handling**: thresholds at or below a symbol's minimum tick may be dominated by discretization. Avoid arbitrary universal absolute-USDT wick cutoffs.
- **Context**: use only already confirmed prior bars; never infer a support zone from a later price bounce then pretend it was known earlier.
- **Confirmation**: final candle shape can change before close. On chart's current timeframe, evaluate confirmed-bar semantics; do not misapply `barstate.isconfirmed` within `request.security()`. See official TradingView documentation.
- **MTF values**: current higher-timeframe values may repaint. Official TradingView confirmed-HTF pattern offsets the expression by one HTF bar and uses `barmerge.lookahead_on`, at the cost of latency. This is a *future technical constraint*, not implemented code.

## Competing hypotheses and validation design

- H0: OHLC geometry adds no incremental out-of-sample prediction beyond prior trend, volatility, volume/liquidity and a simple baseline.
- H1: geometry plus independently validated location/confirmation provides incremental utility over that baseline.
- H2: added rule complexity overfits and degrades robustness vs simpler morphology-only or no-pattern approaches.

Before data mining, fix a baseline definition, markets/venues, label timing, entry/exit assumptions, fees/slippage/funding and holdout periods. Evaluate classification agreement between synthetic fixture cases and expected geometry separately from market outcome tests. Then compare BTC/ETH-type crypto (when selected), gold-reference derivatives XAUUSDT, and gold-backed token pairs XAUTUSDT/PAXGUSDT separately when actual feeds support it. Record insufficient sample sizes, differing histories, survivorship/selection, liquidity and multiple-testing effects.

## Open and undecided

- Actual numerical ratios for each candle shape.
- Whether doji and hammer are mutually exclusive or multi-label.
- Support/resistance zone definition; previous-trend pivot algorithm.
- Whether wick-to-range or wick-to-body is more portable.
- Whether any independent volume, volatility, liquidity, ATR or regime filter improves performance.
- Definition and timing of “confirmation” given later Coach source lessons.
- Market/instrument venue identifiers and product-specific TradingView data access.

**No Pine Script has been written, compiled, backtested, deployed or used for an actual trading decision.**

## External research boundaries

- [CME technical analysis education](https://www.cmegroup.com/education/courses/trading-and-analysis/technical-analysis) for OHLC interpretation.
- [TradingView bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/) and [repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) for future Pine design.
- [Marshall/Young/Rose (2006)](https://www.sciencedirect.com/science/article/pii/S0378426605002116), [Lu et al. (2015)](https://www.sciencedirect.com/science/article/pii/S0378426615002678), and [Thai equity study](https://journals.sagepub.com/doi/full/10.1177/2158244017736799): market-specific and method-sensitive studies, **not evidence that the particular Coach pattern definitions work for crypto**.
