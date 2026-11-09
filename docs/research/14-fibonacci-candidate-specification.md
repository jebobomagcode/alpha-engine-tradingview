# Lesson 14 — Fibonacci Custom Bands and Causal Anchor Research

**Status:** OPEN RESEARCH CANDIDATES ONLY; no Pine, market tests, strategy results or orders. Source: [Coach PDF p. 19](../../sources/coach%20trading%20lessons.pdf); [complete PCSS Lesson 14](../lessons/14-fibonacci-retracement.md). Date 2026-11-09 Asia/Manila. Crypto scope XAUUSDT, XAUTUSDT and PAXGUSDT remain distinct exchange/product feeds.

## Coach source requirements

- Tool suggests support/resistance pullback reaction locations. Five stated levels 0.236,0.382,0.5,0.618,0.786.
- Initial Golden Zone 0.5–0.618, in both up and down trends.
- HTF 4H/Daily choose swing, plot fib and wait zone; LTF 5m/15m obtain engulfing/liquidity-sweep/other confirmation, then consider entry/SL/TP.
- SL beneath/above 0.786 by direction; exact price buffer missing.
- **Last paragraph** says manually add 0.705 ratio and seek entry around 0.618–0.705 after confluence, without clearly overriding earlier region.
- No exact swing detector, objective touch/reaction, TP method, achieved trade, probability or historic data.

## A. Source ambiguity — three testable candidate policies

**Policy A (initial):** shallow economic retracement r in [0.500,0.618].
**Policy B (final settings):** deeper r in [0.618,0.705].
**Policy C (dual visualization):** show both as differently labeled regions, with policy unresolved; do not merge them and claim Coach only has one golden zone.

Working recommendation for future research *presentation* is C. Final executable eligibility should not be locked before studying full PDF and comparing tests.

## B. Numerical geometry — independent, not attributed to Coach

Let valid confirmed extrema L<H, r in [0,1].
- UP economic pullback: P(r)=H-r(H-L).
- DOWN economic retracement: P(r)=L+r(H-L).
- Positive-price log alternative: UP H*(L/H)^r; DOWN L*(H/L)^r. TradingView supports a log-scale Fib option. Arithmetic and log output differ.

At L=100, H=120, independent synthetic example:

| r | bullish correction | bearish correction |
| --- | ---: | ---: |
| .236 | 115.28 | 104.72 |
| .382 | 112.36 | 107.64 |
| .500 | 110.00 | 110.00 |
| .618 | 107.64 | 112.36 |
| .705 | 105.90 | 114.10 |
| .786 | 104.28 | 115.72 |

Stop price only inequality S_long<104.28 or S_short>115.72; exact S/TP/position size UNKNOWN, hence no fixed RR. “Custom 0.705” is not a verified predictive threshold.

## C. Anchor selection alternatives — no winner approved

1. **Manual analyst-defined anchors:** transparent Coach-like discretionary labeling; low automatic reproducibility and hindsight selection risk.
2. **Confirmed structural pivots:** clear rules, but delayed; maintain origin and known-at timestamps.
3. **Causal rolling highs/lows:** automatic and timely but levels may continually move; difficult to freeze.
4. **Impulse/BOS-based anchored range:** may aid alignment with Coach structure but depends on an independently defined displacement/BOS threshold and pivot logic.

Store exact venue-qualified instrument, timeframe, anchor origin and confirmation times, ratio math mode, tool Reverse mode (display-only semantics), candidate status, frozen/evolving status and price interval. Do not assign historical setup eligibility before anchors became knowable.

## D. Important alternative conditions

- Fib and structural support/resistance based on the same swings are correlated; requiring overlap may be redundant rather than an independent confidence increase.
- Long S below .786 and short S above .786 are Coach's constraints, but no fixed offset: independent candidate buffers include price ticks, ATR and spread-aware models; never call one Coach-approved.
- LTF confirmation from an engulfing/lower-timeframe liquidity sweep remains qualitative; require separate event and time formalization.
- RR is indeterminate until entry, stop and TP are fully defined. A “target previous high” or “next S/R” convention would be imported from broader source or independent design; page 19 itself provides no unique TP.
- Chart scale and drawing Reverse setting alter displayed ratio mapping; validate actual price coordinates against the model.
- Frequent updates to the last swing high can retroactively relocate Fib levels and create future-data-looking chart drawings.

Official TradingView refs:
https://www.tradingview.com/support/solutions/43000518158-fibonacci-retracement-drawing-tool/
https://www.tradingview.com/pine-script-docs/concepts/repainting/

## E. Discriminating future tests, NONE run

1. Up 100->120: .5=110, .618=107.64, .705=105.9, .786=104.28.
2. Down 120->100: .5=110, .618=112.36, .705=114.1, .786=115.72.
3. Shallow band contact but deep band not touched: report A eligibility only, not B.
4. Deep band contact without LTF engulfing/rejection: WAIT/no entry.
5. Confirmed swing becomes known only after apparent historical zone touch: prohibit lookahead.
6. Chart Reverse option makes ratio labels different: compare actual price levels, not just text.
7. Arithmetic versus log mode of same swing: disclose differing outputs.
8. Stop at .786 exactly instead of beyond: fails Coach inequality; tick buffer unspecified.
9. No TP defined: RR_UNKNOWN.
10. Unconfirmed HTF candle/anchor: provisional; no false confirmed history.
11. Liquidity sweep requires a selected prior swing, wick/close and reaction time rule; unknown by source.
12. Overlap between Fib and structural S/R derived from same swings: compare against baseline and test for correlated evidence.
13. Different gold-linked token and derivative feeds: invalidate cross-product zones.
14. Repeatedly updating swing high changes band after old signals: detect state inconsistency.
15. Empirical comparison of A vs B vs C needs precommitted markets, realistic fees and holdout results; no performance inference from a single cherry-picked figure.

**Ponder recommendation:** source-faithful dual-band research overlay, frozen/confirmed HTF anchors, and explicit WAIT/NO TRADE + unknown RR. Keep anchor method, source-band precedence and TP logic open until later evidence. No code authorized.

**Next:** Lesson 15, Reliability on Charting, original PDF page 20, only on user continuation.
