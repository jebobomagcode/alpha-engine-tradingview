# PCSS Lesson 11 — Order Block; BOS versus CHoCH

**Status:** COMPLETE at source-study level: original PDF page 14 text and both halves of original graphic inspected; source item inventory, layered explanation, independent counterexamples and design research documented (2026-11-09, Asia/Manila). **Not** implemented, backtested or empirically validated.  
**Only Coach-origin source:** [coach trading lessons.pdf, original PDF p. 14](../../sources/coach%20trading%20lessons.pdf).  
**Source PDF SHA-256:** 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. **PCSS SHA-256:** 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56.  
**Owner scope:** crypto including separate XAUUSDT, XAUTUSDT and PAXGUSDT products; previous unrelated projects remain untouched.  
**Next:** Lesson 12 — BOS (Break of Structure), PDF pp. 15–16, only on owner's next instruction.

## Ordered original source inventory

The entire source page was inspected as a rendered PDF and native extracted text. It has **one composite illustration with two labeled panels** near its top, followed by Order Block text, a BOS note and a simple BOS-versus-CHoCH comparison. There are **no original numeric threshold, OHLC dataset, empirical probability table, executed trades, formula, proof or assigned exercises** on this page.

| ID | Original element in page order | Source audit |
| --- | --- | --- |
| 11-F1 | Top composite figure: left panel titled **Bullish Order Block Candle**, right panel titled **Bearish Order Block Candle** | Both panels inspected visually |
| 11-F1a | Bullish panel shows prior falling orange bars, **green candle 1** marked "OB Candle" near a **Swing Low**, then blue rising candles 2 and 3; lower green zone rectangle; annotation **"1→3 GAP"**, green check | Crucial: image does **not** explicitly require last bearish candle for bullish OB; shaded zone boundaries not given mathematically |
| 11-F1b | Bearish panel shows prior rising blue bars, **red candle 1** marked "OB Candle" near a **Swing High**, then orange falling candles 2 and 3; upper pink/red rectangle; annotation **"1→3 GAP"**, green check | Crucial: image does **not** explicitly require last bullish candle for bearish OB |
| 11-01 | Heading "11. ORDER BLOCK" | Covered |
| 11-02 | Red bullet heading "ORDER BLOCK" | Covered |
| 11-03 | OB is the last candle before a strong pump or drop | Covered; no objective displacement magnitude/time window supplied |
| 11-04 | Coach says large money entered there | Preserved as Coach's interpretation, not direct OHLC proof of actor identity or orders |
| 11-05 | Coach expects considerable possibility of another reaction when price returns | Preserved as qualitative statement, no measured probability or guaranteed reaction |
| 11-06 | NOTE: properly marking **BOS** depends on breaking a previous **HH or LL** | Covered; exact wick/close/threshold undefined |
| 11-07 | Don't casually place BOS; first identify **HH and HL** | Covered verbatim conceptually; context with bearish LH/LL from earlier lessons matters |
| 11-08 | Once structure is clear, BOS location becomes apparent | Covered; conceptual, not an automatic detector algorithm |
| 11-09 | "BOS vs CHoCH (Simple Difference)" | Covered |
| 11-10 | **BOS = continuation (trend continues)** | Covered, no operational details supplied |
| 11-11 | **CHoCH = possible reversal (direction changing)** | Covered with emphasis on "possible", not certain |

**No additional BOS or CHoCH illustration exists on this page beyond the OB figure.** The next section of the PDF expands BOS on pages 15–16; it is not silently incorporated into this completed page-14 lesson.

## 1. Definition: Order Block

**COACH EXPLICIT:** "last candle bago nag pump/bagsak ng malakas"; associated with "malalaking pera"; price returning to that earlier area may react again.

**Meaning/intuition:** Identify a candidate candle directly preceding a strong directional displacement; its price region becomes a location of interest on later revisits. It is a past price-region hypothesis, **not** a guaranteed pending order or automatic trade signal. Candlestick prices alone cannot identify institutional activity or order ownership.

**Original figure nuance:** Bullish OB is a green candle 1 before candles 2–3 move upward, marked near Swing Low. Bearish OB is a red candle 1 before candles 2–3 move downward, marked near Swing High. Both include shaded rectangles and "1→3 GAP" annotation. These facts are visually present in the PDF, but Coach gives **no explicit gap/FVG formula, no minimum candle body, no exact zone-wick-vs-body rule, no mandatory BOS-before-OB rule and no zone expiry/retest policy**. Do not overwrite the actual image by importing a convention of "last opposite-colored candle before a move", which is visibly not what these panels label.

### Hypothetical independent example — NOT Coach data

Suppose a BTCUSDT candidate candle has \(O=100\), \(H=103\), \(L=99\), \(C=102\) and later candles show a strong rise. A body-derived zone candidate would be \([100,102]\); a full-range zone candidate \([99,103]\). Both are reasonable *alternative independent definitions* but **Coach does not choose either**, and the strong rise must first be defined and observed.

If a hypothetical later price revisits 101, it contacts both example zones. That contact alone gives no statistically justified BUY. A future script must record *when the displacement became sufficient to recognize the OB* and check whether a subsequent revisit happened **after** recognition.

## 2. BOS note — structure must precede the break label

**COACH EXPLICIT:** BOS marking should depend on break of previous HH or LL. Identify structure (he writes HH/HL) first; once the structure is clear, BOS becomes apparent.

**Prerequisite from Lesson 07:** Uptrend is HH/HL; downtrend is LH/LL. The page-14 "identify HH/HL" note must be understood in the source's own progression; it is **not** proof that bearish LL/LH structure can be ignored when detecting continuation.

**INDEPENDENT FORMAL IDEA:** With an already-confirmed bullish relevant swing high \(H_*\), a candidate upward break could compare later wick \(H_t>H_*\) or closing price \(C_t>H_*\). They are **not equivalent** and neither is defined by Coach here. Symmetric low-side break might compare \(L_t<L_*\) or \(C_t<L_*\) against a previously known relevant low. Equality, retests and minimum tick-buffer remain open.

**Time-of-knowledge problem:** A pivot requiring later bars is not a known swing at its geometric origin. A BOS signal using a future-confirmed pivot retroactively on earlier candles would be invalid. TradingView's [Repainting documentation](https://www.tradingview.com/pine-script-docs/concepts/repainting/) specifically notes the risk of plotting pivots at old bars after they become identifiable.

## 3. BOS versus CHoCH — source distinction

| Original term | Coach's definition | What it does NOT prove |
| --- | --- | --- |
| **BOS** | Continuation; trend carries on | Not a unique break threshold, and not evidence the next trade is profitable |
| **CHoCH** | Possible reversal; market behavior/direction changing | Does not guarantee reversal, prove a new trend, or identify its confirmation timing |

**INDEPENDENT ILLUSTRATIVE CONTRAST:** Suppose an uptrend has earlier confirmed structural high 110 and low 97. A later completed bar at 112 exceeds the prior high; under a closing-break variant this could be a **continuation candidate (BOS)**. A later drop to 96 below the earlier low could be a **change candidate (CHoCH)**. These are *not* source-trade values or approved operational rules. A single contrary penetration might be noise or a liquidity sweep, not sustained reversal.

**Source boundary:** Page 14 does not identify precisely which protected low/high triggers CHoCH, does not require a subsequent opposite-side BOS to confirm it, and does not define whether the break must use wick or close. Do not pretend the fuller Lesson 12 already supplied answers.

## 4. Retrospective selection and identification bias

If candle at \(t_0\) is labeled an Order Block because subsequent candles at \(t_1,t_2,t_3\) rose strongly, the determination is not knowable at \(t_0\).

At minimum \(t_{\mathrm{known}}\ge t_{\mathrm{evidence\ completed}}\), so the decision eligibility time is later than or equal to recognition and generally later than origin. A shape drawn back at \(t_0\) must not be used to claim that a live user was notified at \(t_0\).

This is the **same causal principle** governing HH/HL pivots, BOS, CHoCH and HTF price zones. Current TradingView documentation on [higher-timeframe lookahead](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) warns that unoffset lookahead_on can leak future values into historical bars.

**Selection risk:** Demonstration figures show ideal examples with attractive moves. They do not measure how often apparently similar OB candles fail, how often zones are revisited, or whether the revisits generate favorable after-cost outcomes.

## 5. Ponder — candidate specifications, no predetermined implementation

See [Lesson 11 research file](../research/11-order-block-bos-choch-candidates.md) for discriminating variants.

Potential distinct outputs to study when the user authorizes coding:

1. **Structure:** predeclared and confirmed swing levels with their event and known-at timestamps.
2. **Displacement:** candidate strong move measured by body/range/ATR/tick/percent; *threshold undecided*.
3. **OB candidate:** last source-compatible candle before the qualified move, with provenance and defined body/wick price interval; image's same-direction candles must not be excluded on grounds of a different internet convention.
4. **BOS/CHoCH candidates:** classification only with a previously known structural bias, identified broken level and break rule; different break directions imply continuation versus possible character change.
5. **Revisit/response:** an OB region touched later, before expiry or invalidation, is a *reaction opportunity to evaluate*, not a sure signal; Lesson 08 confirmation and risk gates remain separate.
6. **Explainable unknowns:** insufficient history, trend unknown, break not closed, incomplete displacement, ambiguous OB polarity, no zone revisit, previously invalidated zone, inconclusive response.

Each item is proposed independent research, not a Coach-authored algorithm. No field, threshold or required sequence has been selected as final.

**TradingView technical note:** Pine has box and line drawing objects suitable for marking zones, but their resource limits and historical/backdated presentation need careful handling. Official [Lines and boxes](https://www.tradingview.com/pine-script-docs/concepts/lines-and-boxes/) and [Limitations](https://www.tradingview.com/pine-script-docs/writing/limitations/) pages document these constraints.

## Source and coverage verdict

- The full single-page lesson was inspected visually and via native extraction.
- Both original illustrated panels, including green bullish OB candle 1, red bearish OB candle 1, shaded zones, swing high/low, 1→3 GAP labels and green checks, were individually inventoried.
- Coach's original three OB claims, entire BOS NOTE and the two simple BOS/CHoCH definitions were preserved in source order.
- No source numerical values or exercises exist on this page; all OHLC and structural-break numbers above are expressly independent examples.
- **Lesson 11 complete at PCSS study/research level. No Pine script, market acceptance or trade simulation.**
- **Next on user's instruction:** Lesson 12, BOS (Break of Structure), PDF pages 15–16, and all figures on those pages.
