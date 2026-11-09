# M00/M01 — Causal Market Data, Swings, BOS, CHoCH (research specification v0.1)

**Status: FORMAL RESEARCH CANDIDATES, NOT APPROVED CODE OR MARKET-VALIDATED INDICATOR.** 2026-11-09 Asia/Manila.
**Primary Coach anchors:** [PDF p6 Time Frame](../../sources/coach%20trading%20lessons.pdf), [p9 structure](../lessons/07-market-structure-confluence.md), [p10 entry workflow](../lessons/08-trading-entry-workflow.md), [pp15–16 BOS](../lessons/12-bos-break-of-structure.md), [p25 CHoCH](../lessons/20-choch-change-of-character.md), [p32 Q&A3](../lessons/qa-03-btc-consolidation-retest-and-breakout.md), [pp34–35 BPI](../lessons/note-02-bpi-bsp-stock-charting.md). All Coach rules here refer to the **single original PDF**; later mathematical definitions are explicitly **INDEPENDENT**.

## A. Original Coach statement, then formalization gap

**COACH_EXPLICIT:**
- Uptrend means higher highs + higher lows, downtrend means lower highs + lower lows (PDF pp9,15).
- BOS is **continuation**: in UP, break previous HH; in DOWN, break previous LL (pp14–16).
- CHoCH is **possible reversal**: in DOWN, break prior LH upward; in UP, break prior HL downward (p25).
- Use higher timeframe to locate trend/zone, lower timeframe to confirm (p6); don't enter until chosen zone is reached and a confirmation candle **closes** in the Lesson08 workflow (p10).
- Sideways/breakout context is different from an established trend (p9, Q&A3 p32). In BPI p35 a potential local 4H bounce is not a confirmed Daily CHoCH.

**OPEN_UNRESOLVED, absent from Coach:** how swing pivots are detected and confirmed, ties, min distance, how many swings define trend, wick versus close breaking, pivot buffer, what counts as “previous” high/low, protected/structural vs micro pivots, whether simultaneous timeframe conflicts block new trades, how a CHoCH progresses to full reversal, and exact signal persistence/expiry. Our definitions below are **candidate research specifications** and must not be labeled Coach-certified.

## B. M00: immutable market/time/evidence contract (INDEPENDENT_PROPOSAL)

A bar record must carry at least:

| Field | Meaning / invariant |
|---|---|
| instrument_key | Exchange/provider prefix, exact ticker, market type (spot/perpetual/other), quote currency, contract identity and source; never infer BTCUSD=BTCUSDT or gold tokens=gold derivative |
| timeframe | Source-defined duration/calendar interval, exchange session/alignment, candle boundaries |
| open_at, close_at | Original bar time interval, UTC; open_at < close_at. Session gaps and variable daily durations allowed |
| O,H,L,C,V | Numeric prices in stated quote units; H≥max(O,C), L≤min(O,C), V≥0 when trustworthy. Mark bad/missing data, do not silently replace |
| is_final | Confirmed close data vs developing candle; a developing bar cannot certify the closed-bar version |
| available_at | Earliest actual data availability/confirmation instant. Must be no earlier than close_at for a strictly closed bar; latency may be later |
| provenance | Real feed vs source screenshot vs coach assertion vs constructed illustrative fixture; quality/coverage label |

When historical feed has unknown adjustment, missing candle, duplicate timestamp, unverifiable quote currency or instrument mismatch, return a **DATA_INSUFFICIENT** state for rules depending on it. No bar timestamp is retroactively re-labeled as known earlier because an algorithm later draws a nice chart.

**Decision-time admissibility:** for event time \(\tau\), evidence \(e\) may be used only if \(e.\mathrm{available\_at}\le \tau\). Forming data may be shown as explicitly **PROVISIONAL**, but must not contaminate a claimed confirmed historical event.

**HTF aggregation:** On a 5m analysis bar, use only the latest **confirmed, available** 1H/4H context as of decision time. A 4H bar ending 12:00 is not fully knowable at 11:55. Internal UTC timestamps and user display Asia/Manila; trading-session labels are **descriptive hypotheses**, not source-approved crypto gates.

**External technology evidence (not Coach):** TradingView [other timeframes and data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) describes future leakage when using HTF \`lookahead_on\` without a historical expression offset. [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) specifically warns against back-plotting a pivot at the earlier origin as if it were known there. These are future engineering constraints, not a claim that any Pine code was run.

## C. Candidate swing methods: three materially different models

**M01-P0: manual prior-known swing annotations (baseline).** An analyst marks the actual swing time, level and the date/time the reference was knowable. Preserve annotations with source/provenance and separate “source chart suggests” from true computed rules. Faithful to discretion, but not fully automatable; still a necessary comparison.

**M01-P1: confirmed local fractal pivots (simple reproducible candidate).** For bar \(i\), choose independent integers \(\ell\ge1\) left and \(r\ge1\) right. A **high pivot** candidate at \(i\) has \(H_i\) strictly greater than all highs of \(i-\ell,\ldots,i-1\) and \(i+1,\ldots,i+r\), and a **low pivot** analogously strictly smaller. It only becomes confirmed when all \(r\) right-hand bars are **final and available**; its \(\mathrm{known\_at}\) is at least the maximum of those right-bar availability times. The pivot may be **drawn** at origin \(i\) for explanation but must never be represented as a past actionable event before \(\mathrm{known\_at}\). Strict comparisons reject ties; an alternate tie-handling policy would be a different hypothesis. \(\ell=r=2\) is **one independently chosen fixture example, not a Coach parameter or adopted production choice.**

**M01-P2: directional-change/volatility pivots.** Confirm a high after price reverses at least a predeclared amount (e.g. a volatility-scaled threshold) and a low after the opposite reversal. Confirmation is causal and adaptive to volatility, but the pivot location and reference significance differ from the fractal method. No ATR length/multiplier is selected; changing the threshold changes the hypothesis.

**M01-P3: rolling-window high/low breakout.** Use the previous \(N\) completed bars' extremes as fast causal levels, but **do not call a break a Coach-exact HH/HL BOS** unless an independent preceding structural trend is also established. It is a separate breakout baseline; \(N\) is not Coach-supplied.

**Research preference:** P0 as transparent manual comparison and P1 as the simplest explicit deterministic *research* candidate, with P2 and P3 as challenges. No selected Pine detector yet.

## D. Candidate trend grammar (INDEPENDENT, needed before BOS)

Maintain a time-ordered, confirmed alternating pivot sequence for a **single exchange-qualified instrument+timeframe**. Resolve two consecutive highs without an intervening low (and converse) using a documented event compression policy; never silently use a future replacement.

Let \(L_1,H_1,L_2,H_2\) be consecutive alternating **confirmed** low/high/low/high pivots, with levels \(L_2>L_1+\varepsilon\) and \(H_2>H_1+\varepsilon\). Define a proposed **UP context** after all four pivot confirmations. Similarly, if \(H_1,L_1,H_2,L_2\) are consecutive high/low/high/low pivots, \(H_2<H_1-\varepsilon\) and \(L_2<L_1-\varepsilon\), define **DOWN context** after all four confirmations.

Here \(\varepsilon\ge0\) is a fixed comparison margin in quote-price units derived from a **separately declared** integer number of instrument tick sizes. \(\varepsilon=0\) means strict break; one tick is a **different independent hypothesis**, not Coach's rule.

**Neither UP nor DOWN established → STRUCTURE_UNKNOWN (or RANGE_CANDIDATE with separate evidence).** A couple of same-direction candlesticks cannot substitute for eligible structural pivots. Warmup and missing bars may prevent a classification. Do not silently use the latest price to choose future pivots.

Proposed reference in UP: last previously **confirmed eligible HH** for bullish continuation, and last **confirmed eligible HL** for potential bearish CHoCH. In DOWN: prior **confirmed eligible LL** for bearish continuation and prior **confirmed eligible LH** for possible bullish CHoCH. The pivot-reference ownership, invalidation and replacement after a break remain subject to tests.

## E. Proposed event grammar for **closed-bar** research branch

For closed bar \(t\), requiring a known trend state and eligible confirmed swing reference available **before the decision bar**:

- **Bullish BOS candidate:** prior regime UP; last eligible HH = \(h^\*\); prior close \(C_{t-1}\le h^\*+\varepsilon\), current **final close** \(C_t>h^\*+\varepsilon\); reference not previously consumed.
- **Bearish BOS candidate:** prior regime DOWN; last eligible LL = \(l^\*\); \(C_{t-1}\ge l^\*-\varepsilon\), final \(C_t<l^\*-\varepsilon\); ref unconsumed.
- **Bullish CHoCH candidate:** prior regime DOWN; last eligible LH = \(h^\*_{\mathrm{LH}}\); \(C_{t-1}\le h^\*_{\mathrm{LH}}+\varepsilon\), final \(C_t>h^\*_{\mathrm{LH}}+\varepsilon\).
- **Bearish CHoCH candidate:** prior regime UP; last eligible HL = \(l^\*_{\mathrm{HL}}\); \(C_{t-1}\ge l^\*_{\mathrm{HL}}-\varepsilon\), final \(C_t<l^\*_{\mathrm{HL}}-\varepsilon\).

These formulas deliberately choose **close-confirmed first crossing**, because source Lesson08 says entry after a confirmation candle closes (although that lesson does NOT formally define BOS as close break). **This is our conservative research candidate, not an exact Coach BOS/CHoCH definition.** A source-preserving alternative is a **completed-bar wick breach** \(H_t>h^\*+\varepsilon\) or \(L_t<l^\*-\varepsilon\), recorded as **WICK_TEST**; an intrabar breach before bar close is PROVISIONAL. Compare the two interpretations empirically later rather than mixing them in one label.

Upon first event, **consume its reference** to avoid emitting a new BOS/CHoCH every bar that remains beyond one old pivot. New qualifying structure can arm a new reference only when separately established. Missing or ambiguous references → **INSUFFICIENT_STRUCTURE**, not positive event.

**Important:** A CHoCH indicates a **potential structural shift**, NOT instant confirmed new UP/DOWN regime. Proposed separate follow-up reversal-confirmation policy (e.g. subsequent eligible opposite-direction BOS and pivot structure) remains OPEN; do not relabel the CHoCH as reversal completed.

## F. Invariants and risk of hindsight

1. A swing with right confirmation lag \(r\) is **NOT actionable at its origin bar**; origin label and confirmation time must both be preserved.
2. BOS continuation needs prior trend and eligible same-direction reference. CHoCH needs prior opposing regime and its opposite-side protected reference.
3. A current bar does not retroactively make the previous bar “trend confirmed” if it only learned about the pivot now.
4. Exact-level equality is not a strict break unless a separately selected equality/tick policy says otherwise.
5. A wick above pivot with close below is not a **close-confirmed BOS**, though may be a candidate sweep/rejection event.
6. Repeated crossings of an already consumed reference are not fresh BOS events.
7. Structure at 4H remains distinct from 15m and 5m; a lower-timeframe CHoCH is not automatically a higher-timeframe trend reversal.
8. Separate venue/product candles never share exact pivot levels by ticker resemblance alone.
9. Externally supplied “higher probability” or “institutional buyers” wording cannot justify precise numeric confidence scores or participant identities.
10. Structure alone is NOT a valid Lesson08 trade; zone contact, confirmation after zone contact and risk review are separately necessary.

## G. Designed finite fixtures and expected outcomes (MANUAL, NOT EXECUTED)

All prices are invented test units and **not current crypto observations**. At each event bar, unless stated otherwise, assume a single valid feed/timeframe, all specified structural pivots were already confirmed and available **before** the bar, \(\varepsilon=0\), and bar values shown are **final**.

| Fixture | Prior structure/reference | Current test | Expected for proposed **closing-break** candidate |
|---|---|---|---|
| F01 | UP, earlier \(L_1=90,H_1=100,L_2=94,H_2=106\) | previous \(C=104\), new \(C=107\) | Bullish BOS candidate above HH106 |
| F02 | UP, same, last confirmed HL94 | previous \(C=96\), new \(C=93\) | Bearish CHoCH candidate below HL94; NOT full DOWN |
| F03 | DOWN, \(H_1=110,L_1=100,H_2=106,L_2=95\) | previous \(C=97\), new \(C=94\) | Bearish BOS candidate below LL95 |
| F04 | DOWN same, last LH106 | previous \(C=104\), new \(C=107\) | Bullish CHoCH candidate above LH106; NOT full UP |
| F05 | UP with previous HH106 | current \(H=107,C=105\) | WICK_TEST only, no closed bullish BOS |
| F06 | UP with previous HH106 | final \(C=106\) | No strict break (equality) |
| F07 | UP previous HH106 consumed on first BOS | later close crosses106 again | No second event from same reference |
| F08 | Candidate pivot origin bar \(i\), research choice \(r=2\) | at bar \(i+1\) future second right bar unclosed | Pivot unavailable; cannot be BOS/CHoCH reference |
| F09 | Candidate pivot at \(i\), \(r=2\) | after bar \(i+2\) confirmed | Pivot becomes eligible **no earlier than** \(i+2\) bar availability |
| F10 | Two highs tied exactly | strict fractal pivot policy | Neither unique high pivot in overlapping window, possibly insufficient structure |
| F11 | Last confirmed state neither UP nor DOWN | price close breaks rolling 20-bar high | Generic window-break candidate, **NOT** source-labeled BOS |
| F12 | 4H UP, 15m DOWN (each independently established) | 15m closed bearish BOS | 15m event possible; no automatic 4H bearish reversal |
| F13 | 4H bar ends at 12:00 PHT | 5m decision 11:55 PHT | 12:00 4H final information inaccessible at 11:55 |
| F14 | Price correct but duplicate timestamps or missing bars | attempt pivot event | DATA_INSUFFICIENT until qualified feed normalization |
| F15 | Correct bullish BOS but no chosen support-zone contact | Lesson08-style trade request | WAIT_ZONE/NO_TRADE, not BUY |
| F16 | 5m rejection visible intrabar but not closed | request confirmation | PROVISIONAL only; no closed entry confirmation |

These are **expected results under explicit assumptions**, NOT tests executed by a Pine script, a Python engine, or an exchange dataset. They check that the proposed language is discriminating; edge cases and executable test fixtures remain separate work.

## H. Open specifications before this can be an approved detector

- Pivot \(\ell,r\) choice, tie and event compression policy, swing degree/hierarchy, initial/trailing warmup.
- Whether gap-driven crossings and traded-away pivot levels qualify; close vs wick variants; \(\varepsilon\) and exchange tick rounding.
- Need for displacement/volume condition and how it changes the number of events; source does not prescribe one.
- Previous HH/LL versus “protected” HL/LH across multiple nested scales; how many BOS events reset reference.
- What confirms a CHoCH as a trend change vs still-range; no risk-free reversal label.
- Session-specific missing bars and HTF data availability in real TradingView runtime.
- Interaction with M02 location, M04 candle reaction, M05 multi-timeframe state and M06 risk. This document **does not** make a trade signal.

**Research milestone 01 COMPLETE as a written, source-anchored candidate spec. M00/M01 algorithm selection and actual implementation remain OPEN.** Next module research should move to M02 support/resistance/OB/FVG and M04 confirmation-candle grammar while keeping M01 alternative choices visible.
