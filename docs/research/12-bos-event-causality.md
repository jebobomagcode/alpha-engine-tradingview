# Lesson 12 — BOS Event Semantics and Causal Formalization Research

**Status:** OPEN RESEARCH — not implemented, compiled, backtested or validated. 2026-11-09 Asia/Manila.
**Coach source:** [PDF pp15–16](../../sources/coach%20trading%20lessons.pdf), [PCSS Lesson 12](../lessons/12-bos-break-of-structure.md). Sole Coach-origin authority is the PDF.
**Market scope:** crypto, with distinct XAUUSDT derivative vs XAUTUSDT/PAXGUSDT product feeds and symbol/venue attribution.

## Coach-explicit contract

- Establish **trend first**: UP HH/HL, DOWN LH/LL.
- **BOS means continuation**.
- UP + break previous HH -> upwards continuation.
- DOWN + break previous LL -> downwards continuation.
- Page 15 images: paired bullish/bearish BOS; **repeated Lesson 11 OB diagram** (not a new required BOS filter); ascending HH/HL/BoS zigzag; mixed downtrend BOS and CHOCH with demand zone and bullish recovery.
- Page 16 image: repeated falling LL/BOS tags in bearish candlestick structure.
- No exact pivot confirmation, break rule, strength threshold, historical outcome, timeframe priority or CHoCH protected swing definition.

## Distinct candidate break semantics — independent, not Coach rules

Given prior-known structural state S, confirmed high H* or low L*, valid current OHLC:
- **Closing break:** UP ∧ C > H* -> bullish BOS candidate; DOWN ∧ C < L* -> bearish candidate.
- **Wick break:** UP ∧ H > H*; DOWN ∧ L < L*. Intrabar provisional status possible.
- **Buffered break:** require > one or more ticks, a percent of price or prior-known volatility distance. No buffer is specified by the source.
- **Repeated-close confirmation:** multiple completed closes beyond level; potentially fewer false breaks but delayed entries; not mandatory from Coach.

No variant has been selected; retain independent/source provenance per rule.

## Required chronological contract

Before labeling a break, preserve:
- exact venue-qualified symbol/product, timeframe, OHLC source, timestamps and data validity;
- structural high/low origin candle and later *confirmation/known-at* candle;
- known prior trend snapshot, not a trend recomputed using future price;
- break comparison price (wick versus close), candidate and final confirmation timestamp, buffer/equality;
- which structural level was broken and whether it has already been consumed by a prior event;
- if ambiguous, return UNKNOWN or WAIT rather than bullish and bearish BOS simultaneously.

**Pitfall:** visually backplotting a pivot label at its extreme is not proof that a user could have acted there. Future-confirmed pivots and HTF values cannot validate earlier LTF signals. TradingView official references:
https://www.tradingview.com/pine-script-docs/concepts/repainting/
https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/
https://www.tradingview.com/pine-script-docs/concepts/bar-states/

## BOS vs CHoCH research boundary

Proposed *not source-final* classification:
- prior UP and high-side break = bullish continuation BOS;
- prior DOWN and low-side break = bearish continuation BOS;
- prior UP and relevant protected-low break = possible bearish CHoCH;
- prior DOWN and relevant protected-high break = possible bullish CHoCH;
- prior MIXED/SIDEWAYS/unknown and an arbitrary price break = context unknown, not forced BOS.

The CHOCH figure on page 15 shows bearish BOS *and later* possible change. It does not prescribe how many new swing events are needed before confirming the new uptrend.

## Hypothetical discriminator tests — NOT executed

| ID | Pre-existing state and event | Expected candidate interpretation |
| --- | --- | --- |
| A | UP, known H*=110, C=112 | close-based bullish BOS |
| B | UP, H*=110, H=112 but C=109 | wick-only break; not close break |
| C | DOWN, known L*=90, C=87 | close-based bearish BOS |
| D | UP, known protected low=95, C=94 | possible bearish CHoCH, not automatic bearish BOS |
| E | DOWN, known protected high=108, C=109 | possible bullish CHoCH, not automatic bullish BOS |
| F | SIDEWAYS with a crossing | state/threshold ambiguous; no forced Coach continuation |
| G | Pivot discovered after break bar | reject retrospective use |
| H | Both prior high and low crossed by outside bar | preserve ambiguity/priority needed |
| I | Many consecutive closes above same broken high | do not call each a distinct fresh BOS without new level |
| J | CHOCH graphic followed by bullish recovery | do not retrospectively claim initial reversal known from later bars |
| K | OB graphic repeats preceding lesson | do not infer every BOS requires OB or gap |
| L | 4H UP but 1H DOWN | separate timeframe assessments, do not invent priority |
| M | Change from XAUUSDT perpetual to XAUTUSDT or PAXGUSDT spot market | do not reuse structural prices across feeds |

## Future validation and falsification

Test chronology invariants, synthetic fixtures, real Pine historical/realtime and reload consistency after future authorization. Compare wick, close and buffered variants against simple prior-high/low baselines, including false break rates, signal counts, latency, and out-of-sample performance with realistic fees. Do not claim edge from drawings or without trade entry/SL/TP definitions. Simulated broker fills are a separate research question.

**Proposed direction:** source-faithful trend-first logic, separate event recognition and structural meaning, distinct confirmed/provisional/insufficient states; no numerical thresholds finalized and no code produced.

**Next user-directed PCSS:** Lesson 13, Manage Your Risk, PDF pages 17–18.
