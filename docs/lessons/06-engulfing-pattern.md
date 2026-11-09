# PCSS Lesson 06 — Engulfing Pattern

**Status:** COMPLETE — source-order teaching and original-page visual audit, mathematical examples, interpretation critique, and design research (2026-11-09 Asia/Manila).  
**Authoritative original Coach source:** [coach trading lessons.pdf, page 8](../../sources/coach%20trading%20lessons.pdf). **This is the sole Coach-origin source.**  
**PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`.  
**Original PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`.  
**Scope:** original section 06 on PDF page 8, all text and three illustrated panels; **no implementation, Pine compilation, trade backtest or live market validation**.  
**Project market target:** Crypto, including distinct XAUUSDT, XAUTUSDT, PAXGUSDT instruments, per owner D-013. No older project accessed or adapted.

## Source-first page inventory (in reading order)

The entire original PDF page 8 was rendered at high resolution and inspected visually with extracted text crosscheck. It has a short text lesson followed by **three illustrated panels** and does not contain an original mathematical formula, source OHLC table, explicit numerical threshold, assigned exercise, or source proof.

| ID | Original page-8 item | What is present and what is not | Covered |
| --- | --- | --- | --- |
| 06-01 | Heading “06. ENGULFING PATTERN” | Introduces section | Yes |
| 06-02 | “NEXT LESSON: ENGULFING PATTERN” marker | Colored text bullet | Yes |
| 06-03 | “Bullish Engulfing” heading | Green bullet | Yes |
| 06-04 | “Nangyayari sa support area” | Market location emphasized | Yes |
| 06-05 | Large green candle engulfs prior red candle | No body-vs-full-wick mathematical boundary supplied | Yes |
| 06-06 | “pumasok ang buyers → possible taas” | Coach's intuitive market narrative, **possible**, not a certainty | Yes |
| 06-07 | “Bearish Engulfing” heading | Red bullet | Yes |
| 06-08 | “Nangyayari sa resistance area” | Market location emphasized | Yes |
| 06-09 | Large red candle engulfs prior green candle | No percentage or size cutoff supplied | Yes |
| 06-10 | “pumasok ang sellers → possible baba” | Coach's intuitive narrative, not proven order-flow causality | Yes |
| 06-11 | **Left orange-bordered image** | Two retrospective price sequences: bullish engulfing around a local bottom, bearish engulfing around a local top, with small curly-brace annotations and later price bars | Visually audited |
| 06-12 | **Upper-right orange-bordered image** | “Variations in Bearish Engulfing Pattern”: preceding uptrend, boxed green-to-red engulfing anatomy, subsequent red declining bars, “Confirmation of downtrend” annotation | Visually audited |
| 06-13 | **Lower-right orange/green-bordered image** | “BULLISH ENGULFING”: side-by-side **Strong engulfing** and **Weak engulfing**, each illustrating red bars followed by a green bar; green-bar body is visibly larger in the strong example | Visually audited |

**Critical source boundary:** The strong/weak comparison appears in a supporting third-party image embedded in Coach's PDF; **it is not accompanied by Coach-authored thresholds or an explicit rule in the short text**. In the *weak* image, the green body appears not to cover the entire small preceding red real body under a strict body-containment interpretation. This is an ambiguity to document, not silently eliminate. The page's figures illustrate apparent subsequent movements; they do not establish statistical win rates or imply future continuation is certain.

## 1. Bullish Engulfing — Coach's original idea

**COACH_EXPLICIT:** A BIG green candle engulfs a previous red candle **in a support area**. Coach says buyers enter and that price may rise.

**Explanation:** Two adjacent candle bodies reverse color from bearish (red, close below open) to bullish (green, close above open). A sufficiently large bullish body appears to consume or overwhelm the prior bearish body. The context at established support matters to Coach's interpretation.

**Important limit:** Standard OHLC data cannot establish the market participants' identities or their intentions. Coach's “buyers entered” is an explanatory metaphor for net price recovery and potential demand, not direct evidence that one type of trader arrived. Nor is a bullish candle a guaranteed reversal.

**Link with previous PCSS:** Lesson 02 covered hammer, shooting star and doji as single-bar geometry; an engulfing pattern uses **two adjacent bars**. Lesson 04 made HTF zones/context and LTF confirmation separate tasks. We cannot declare the engulfing pair automatically satisfies every later Coach entry-confirmation requirement.

## 2. Bearish Engulfing — Coach's original idea

**COACH_EXPLICIT:** A BIG red candle engulfs a previous green candle **in a resistance area**. Coach interprets it as sellers entering and a possible downward move.

**Explanation:** Two adjacent bodies change from bullish to bearish with a large bearish second candle. At previously established resistance it may be read as a failed upward advance. But the two bars alone do not prove a future decline or tell us that the candle represented institutional selling. Context and next events matter.

The upper-right original image shows uptrend, bearish engulfing and later “confirmation of downtrend.” The **later falling bars must not be retroactively used to classify the earlier pattern as confirmed at its own close**.

## 3. Real body versus full candle range — unresolved Coach ambiguity

**Coach wording:** the second candle “nilamon” the previous candle. He does not explicitly say whether the *real bodies* or the entire *high-low wicks* must be engulfed, and the three figures are not guaranteed to represent one mathematical convention.

**INDEPENDENT FORMALIZATION OPTION A (body-only, common):** For consecutive candles \((O_1,H_1,L_1,C_1)\) and \((O_2,H_2,L_2,C_2)\):

Strict bullish containment candidate:
\[
C_1<O_1,\quad C_2>O_2,\quad O_2\le C_1,\quad C_2\ge O_1
\]
with at least one of the final two boundary comparisons strict if a genuinely larger body is demanded.

Strict bearish containment candidate:
\[
C_1>O_1,\quad C_2<O_2,\quad O_2\ge C_1,\quad C_2\le O_1
\]
with analogous strict-boundary policy.

**OPTION B (full-range):** additionally require the second bar to reach or exceed the previous high and low, \(H_2\ge H_1\), \(L_2\le L_1\). This is a materially stricter *shadow-engulfing* criterion, and is **not** something page 8 clearly mandates.

**OPTION C (relaxed/partial engulfing):** classify partial body overlaps separately as weaker candidates, with transparent numerical definitions. A partially overlapping green candle may be called “weak” in an illustration but does not meet Option A strictly.

None of the options is approved as the final Coach rule. Presenting Option C as “Coach's precise weak-engulfing algorithm” would be fabrication.

## 4. Independent numerical worked examples

These examples are original teaching aids, **not source OHLC observations or backtested trades**.

**Example A: strict bullish body engulfing.** First candle: \(O_1=102,\ C_1=100\) (red, body [100,102]). Second: \(O_2=99.5,\ C_2=103\) (green, body [99.5,103]). The entire red real body lies inside the green body. If \(H_1=105,L_1=99,H_2=104,L_2=99\), then the previous upper wick is not engulfed (\(H_2< H_1\)); **body engulfed ≠ full range engulfed**.

**Example B: strict bearish body engulfing.** First candle: \(O_1=100,C_1=102\) (green, body [100,102]); second: \(O_2=102.5,C_2=99\) (red, body [99,102.5]). It engulfs the first body.

**Example C: misleading large green without full engulfing.** First candle: \(O_1=102,C_1=100\); second: \(O_2=100.5,C_2=103\). The green body is larger than the first red body (2.5 vs 2.0), but the green body starts **above** the previous red close (100.5>100): Option A fails. A naive detector based only on the second body's size would falsely mark full engulfment.

**Example D: boundary equality in 24/7 crypto.** First red \(O_1=102,C_1=100\); second green \(O_2=100,C_2=103\). Body inclusion holds with equality at the lower boundary. A rule requiring the second opening price to be strictly *below* the preceding close would reject this otherwise plausible engulfing setup. Candle opens in highly continuous crypto markets can equal or be very close to the prior close; equality/tick policy must be explicit.

In all four examples, high/low must satisfy valid OHLC inequalities. They are geometric examples only; location and confirmation are additional conditions.

## 5. The original figures: strong vs weak, uptrend/downtrend

**Original left figure:** two complete snippets show an engulfing pair near a swing low and high. It shows visually plausible reversal *examples*, not an unbiased outcome sample; later bars are not evidence the original candle was a sure signal.

**Original top-right figure:** explicitly shows a bearish engulfing boxed in the context of an uptrend, with later downward bars indicating “Confirmation of downtrend.” Be precise about the *time when confirmation is knowable*: this annotation is retrospective.

**Original lower-right figure:** “Strong engulfing” has a tall green body extending visibly beyond the small preceding red body; “Weak engulfing” has a noticeably shorter green body whose lower edge appears higher relative to the immediately preceding small red body's close. This does not establish a source numerical strength threshold. The images distinguish *illustrative strength*, not a proven probability of success.

An independent classifier may eventually use body-size ratio, normalized penetration beyond the previous body's boundary, relative volume or volatility, but must test whether those quantities add value. Volume filters or “institutional buyer” detection are NOT Coach-explicit in this lesson.

## 6. Ponder audit — consequences and counterexamples

- **Shape vs context vs decision:** \( \text{ENGULFING\_SHAPE}\ne\text{SUPPORT\_OR\_RESISTANCE}\ne\text{TRADE\_CONFIRMED}\). Do not merge their definitions.
- **Color/price-source semantics:** use explicit open/close comparisons. Dojis, equal opens/closes, gaps, wicks, synthetic candle types (Heikin Ashi, Renko) and missing data need conscious rules.
- **Realtime uncertainty:** at any time before the second candle closes, its close and often high/low can change; a green candle can finish red. A shape visible mid-bar may disappear. See TradingView [bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/) and [repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/).
- **MTF causality:** a 5m engulfing shape evaluated with 1H/4H levels cannot use a HTF level that only became known after that 5m bar or a support zone drawn retroactively from future pivots. Confirm zone chronology.
- **Subtle sampling risk:** a larger engulfing body can simply accompany greater volatility or liquidity, not an independent forecasting advantage. Use matched controls and out-of-sample testing.
- **Instrument scope:** BTC-like crypto, gold derivative XAUUSDT and gold-token pairs XAUTUSDT/PAXGUSDT can have different tick precision, candle gaps, venues and quote-derived behavior. No single numeric USDT threshold can be assumed universally valid.

## 7. Future indicator/strategy design candidates — not implemented

Possible layered research logic:
1. `SOURCE_VALID`: actual exchange-qualified OHLC from the intended instrument/product; exclude data with missing bars or synthetic-price ambiguity when not modeled.
2. `TWO_BAR_GEOMETRY`: bullish/bearish strict and separately experimental weak/partial shape, with transparent boundary/equality policy.
3. `PATTERN_CONFIRMED`: second candle must close before *confirmed* geometry status; mid-candle label may be provisional but not final.
4. `HTF_ZONE_CONTEXT`: support for bullish, resistance for bearish; strictly causal detection rules deferred until later lessons.
5. `LTF_CONFIRMATION_AND_RISK`: separate additional confirmation (if later source requires it) and planned RR. No current automatic trade/alert permission.
6. `EXPLAINABLE_STATUS`: detected geometry / waiting for context / waiting for close / invalidated / data insufficient. Avoid chart clutter.

**Competing alternatives:** (A) strict body engulfing + context; (B) engulfing full wicks; (C) optional weaker partial overlap; (D) **no engulfing filter** as a negative-control baseline. Predefine definitions and evaluate false signals, robustness, delayed confirmation, actual costs and out-of-sample stability. A more complex model is not automatically better.

**Implementation remains on hold.** No Pine source, live chart tests, performance result, or claim of a trading edge has been created by this lesson.

## Lesson coverage verdict

All original page-8 Coach text and all three embedded figure panels were inspected and described, including the less-obvious strong/weak image and “Confirmation of downtrend” annotation. No source formulas or exercises were present. Independent OHLC examples, equations, and technical caveats have been explicitly distinguished.

**Lesson 06 COMPLETE for PCSS source study only.**

**Next on owner instruction:** Lesson 07 — Market Structure and Confluence (PDF page 9). Preserve source sequence and keep implementation decisions reversible.
