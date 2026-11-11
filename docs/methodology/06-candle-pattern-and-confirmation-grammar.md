# Phase 2 M04-R3 — Source-Scoped Candle Patterns and Confirmation Alternatives

**Status:** source-to-mathematics RESEARCH, no numerical thresholds selected, no Pine, no completed synthetic detector tests or crypto-market backtests. **Date:** 2026-11-11 Asia/Manila.
**Original Coach only:** [PDF](../../sources/coach%20trading%20lessons.pdf) pp2–3 (hammer, shooting star, doji), p8 (engulfing), p9 (trend/zone/signal), p10 (engulf, rejection + follow-through, strong body and entry after close), p13 (range reversal and “break of confirmation”), p21 (HTF/LTF continuation), p31 (bullish rejection vs engulf scalp), p32 (bearish rejection or engulf). Supplementary exact-timing research: [R1](04-reference-arming-and-pivot-order.md), [R2](05-zone-contact-reaction-timing.md).

## A. Coach's actual teachings and what he did NOT quantify

- **p2 hammer:** lower wick long, small body near top, bullish rejection, best examined near support/downtrend, **possible** reversal.
- **p3 shooting star:** long upper wick, small body near bottom, preferably resistance/uptrend, possible reversal; **doji:** nearly no body with upper and lower wicks, expresses indecision and requires confirmation.
- **p8 bullish engulfing:** a BIG green candle engulfs previous red candle, near support; bearish reverses colors near resistance. Coach does **not** uniquely specify engulfing as real-body inclusion versus complete high-low range inclusion, minimal body, exact equality, or a future candle requirement.
- **p10:** one can seek engulfing, a rejection long wick **plus follow-through candle**, OR a strong large-body candle; one strong confirmation can suffice. Entry only after the relevant confirmation candle **closes** in the Lesson08 workflow. The three categories are **alternatives**, not three mandatory simultaneous votes.
- **p13:** sideways range entry mentions confirmation pattern and a later/ambiguous “break of confirmation,” unlike explicit p10 after-close entry. Keep distinct.
- **p31/p32:** lower-timeframe candles interpreted together with location, RSI/EMA context and HTF conditions; none are independent proof of a universal numeric edge.

**OPEN:** thresholds for “big”/“small”, lower/upper wick proportions, previous-candle color and doji boundaries, gap crossing, engulf strictness, number/magnitude of follow-through bars, pattern age and source-defined scores. Everything mathematical below is an **independent candidate**, not a Coach formula.

## B. Defensible OHLC geometry and input validity

For an eligible **completed** candle \(t\) with \(L_t\le\min(O_t,C_t)\le\max(O_t,C_t)\le H_t\), define:

\[
R_t=H_t-L_t,\quad B_t=|C_t-O_t|,\quad
U_t=H_t-\max(O_t,C_t),\quad
W_t=\min(O_t,C_t)-L_t.
\]

\(R_t=B_t+U_t+W_t\). The candle is green when \(C_t>O_t\), red when \(C_t<O_t\), and doji-color neutral when equal. Only final+available candles are considered in a **confirmed** classification; never infer last tick order from OHLC.

**No divide-by-zero:** for \(R_t=0\), ratios \(B_t/R_t,U_t/R_t,W_t/R_t\) are undefined. Return ZERO_RANGE for ratio-dependent geometry on valid flat OHLC. A flat bar supplies valid price data and does not by itself supply the source’s two-wick doji geometry. Report malformed or missing required inputs separately. For \(B_t=0\), a wick/body quotient is undefined even when the range is positive; use a separate wick/range comparator or an explicitly declared tick-adjusted denominator. Invalid OHLC, negative/nonfinite price or absent finality must not produce a confirmed pattern.

**Units:** integer tick-price representation or a consistent quoted price grid is essential before comparing boundary equality; rounding/tolerance rules are external to Coach's PDF and remain OPEN.

## C. Engulfing research candidates

**EN-BODY:** prior bar red \(C_{t-1}<O_{t-1}\), current green \(C_t>O_t\), and \(O_t\le C_{t-1}\), \(C_t\ge O_{t-1}\) for a *bullish body engulf*. Reverse colors and inequalities symmetrically for bearish engulf. Equality permissiveness is one candidate; strict inequality is an alternative.

**EN-RANGE:** same opposite-color requirement and a completed current candle with \(L_t\le L_{t-1}\) AND \(H_t\ge H_{t-1}\), plus correct directional close. This requires the **entire wick-to-wick range** engulf, often materially stricter/different from EN-BODY; it is **not** implied by source prose.

**EN-BIG:** independently require \(B_t/R_t\ge \beta\) for a chosen \(\beta\in(0,1]\), or current body \(B_t\) at least \(\lambda B_{t-1}\) for chosen \(\lambda>0\). Neither \(\beta\) nor \(\lambda\) comes from Coach; evaluate against EN-BODY and EN-RANGE, not as silently mandatory extra “Coach confirmation.”

**Counterexample:** preceding red \(O=105,C=101,H=110,L=98\); current green \(O=100,C=106,H=107,L=99\). EN-BODY is TRUE (100≤101 and106≥105), EN-RANGE FALSE (107<110 and99>98). The two definitions cannot be swapped without changing historical signals.

## D. Hammer, Shooting Star, Doji and rejection: research only

**HM-A (independent geometry):** small body \(B_t/R_t\le b\), longer lower wick \(W_t/R_t\ge w\), body in upper region \(\min(O_t,C_t)\ge L_t+pR_t\), with independent symbolic \(0\le b,w,p\le1\). Include support or relevant location as a **separate** condition from shape. Color is NOT mandated by Coach's hammer text.

**SS-A:** mirror for upper wick \(U_t/R_t\ge w\) and body in bottom region \(\max(O_t,C_t)\le L_t+(1-p)R_t\). Again source location is distinct from geometry.

**DOJI-A:** \(B_t/R_t\le d\) with positive upper and lower wicks; Coach uses it as indecision, **NOT a standalone BUY/SELL**. At exact \(B_t=0\), doji can be a candidate when range>0; zero-range requires separate policy. Threshold \(d\) OPEN.

**RJ-A (independent):** test the lower wick for a bullish lower-price rejection and the upper wick for a bearish higher-price rejection. For positive range, the respective candidate fractions are \(W_t/R_t\) and \(U_t/R_t\). A wick/body comparator uses the same direction-specific numerator and requires positive body or an explicit alternative denominator. The maximum of the two wick fractions is a direction-neutral shape measurement. Location and any close-direction predicate remain separate. A wick does not identify institutional volume.

**12 November correction (E6):** For a final green candle \((O,H,L,C)=(101,110,100,102)\) at a support interval ending at 100.5, \(R=10\), \(W=1\), and \(U=8\). A hypothetical 0.5 threshold applied to the maximum passes on the upper wick, while the lower-wick fraction is 0.1. The mirrored resistance example \((109,110,100,108)\) has \(U=1\) and \(W=8\). Both expose the same defect. The threshold is illustrative and the earlier proposal remains in [Git history](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/bad2c01fe961f0f05de6e05555b914baf4062c5d/docs/methodology/06-candle-pattern-and-confirmation-grammar.md).

**Follow-through variants for a prior rejection at \(t\):**
- **FT-1:** next available closed candle \(t+1\) closes above (bullish) or below (bearish) the rejection candle's real-body edge.
- **FT-2:** subsequent closed candle crosses the rejection candle's **entire high/low**.
- **FT-3:** strength threshold for later close/volume, independently specified.
These are different delays and rejection rules; none is source-quantified. Do not label a lone rejection wick as satisfying the **rejection+follow-through** branch before qualifying later data exists.

**STRONG-BODY A:** completed candle with \(B_t/R_t\ge s\) and suitable bullish/bearish color, no required engulf of previous bar. Threshold \(s\) undefined by Coach and must be evaluated per market; it is an alternative confirmation type, not necessarily a stronger trade.

## E. Causal integration with M01 and R2

For **Lesson08**:
1. Prior verified HTF directional regime (or CONTEXT_INSUFFICIENT).
2. Prior known, valid zone and eligible contact under R2-A or R2-B.
3. One selected qualifying branch of EN*, RJ*+FT*, or STRONG-BODY*, with source-compatible location and confirmation after applicable candles close.
4. Risk-proposal integrity check. **CANDIDATE_FOR_REVIEW** is only a diagnosis, not an order/fill.

For **Lesson10 range**: reversal candle alone is not automatically “break of confirmation”; use separate RB1/RB2 later-trigger hypotheses from [R2](05-zone-contact-reaction-timing.md) and still require proper location.

**Alternative confirmation labels are not independent probability votes:** one candle may simultaneously be bullish body-engulfing and strong-body; do not score it as two independent observations of price movement. Separate source narrative, geometric pattern and trade readiness.

**Time contract:** pattern \`known_at\` is the maximum availability timestamp of its required bars. If following candle or HTF regime is unconfirmed, status is PROVISIONAL or INSUFFICIENT. A historical chart may anchor a marker at candle origin after confirmation. Eligibility begins no earlier than availability of all required evidence, and a decision or display first shown later retains its actual publication time.

## F. Planned discriminating cases — manual expectations, not executed code

| ID | Invented example / condition | Candidate model expectation |
|---|---|---|
| CAN-01 | Red previous body [101,105] and green current [100,106], but prior wick span[98,110], current wick span[99,107] | EN-BODY true, EN-RANGE false |
| CAN-02 | Current green body lies inside prior red body; current high/low exceeds prior extremes | EN-RANGE true, EN-BODY false |
| CAN-03 | Both candles are green | Bullish engulf red→green source color condition false |
| CAN-04 | Current bar is forming, appears body engulf but not closed | PROVISIONAL only |
| CAN-05 | Current body exactly touches prior body edges | equality-permissive true, strict comparator may false |
| CAN-06 | Fully flat O=H=L=C | ratio-dependent classification unavailable, not automatic doji signal |
| CAN-07 | O=C, positive R, both wicks positive | Doji candidate if independently chosen \`d\` permits; not trade signal |
| CAN-08 | Small body at top with large lower wick, prior confirmed support | Hammer geometry may qualify; still requires scenario confirmation |
| CAN-09 | Small body at bottom with large upper wick, confirmed resistance | Shooting-star geometry may qualify; not guaranteed SELL |
| CAN-10 | Long lower wick but body=0 | wick/body quotient undefined; wick/range alternative still defined |
| CAN-11 | Long lower wick on candle t, follow-through t+1 still forming | Rejection+follow-through branch unconfirmed |
| CAN-12 | Rejection t; t+1 closed above body edge but not above t high | FT-1 true and FT-2 false |
| CAN-13 | Strong completed green body with no preceding red engulf | STRONG-BODY branch possible independent of EN |
| CAN-14 | Bullish body-engulf occurs away from any eligible support/demand | Not eligible Lesson08 setup despite pattern |
| CAN-15 | Same closed candle touches preknown zone and engulfs | R2-A waits for later reaction, R2-B may qualify at close only |
| CAN-16 | Same candle touch+invalidation close beyond support floor | Conservative I1 invalidation dominates, no valid new candidate |
| CAN-17 | One 5m rejection after 4H source context not yet confirmed | CONTEXT_INSUFFICIENT, not hindsight trade |
| CAN-18 | Candle both EN-BODY and STRONG-BODY | One independent price observation, not two confluence votes |
| CAN-19 | Coach range reversal candle completed, but later break not observed | RB1/RB2 remain WAIT_BREAK, not fill |
| CAN-20 | OHLC invalid e.g. H<max(O,C) | DATA_INSUFFICIENT, no pattern computation |

**Fixtures are thought examples, NOT execution results**. Any later test runner must define exact thresholds, tick behavior, source-detectable patterns and an appropriate independent human-labelled reference sample before claims of equivalence, accuracy, or edge.

## G. Comparison, recommendation and stopping rule

**Source-faithful manual labels** are the interpretation benchmark; **EN-BODY/EN-RANGE**, **HM-A/SS-A/DOJI-A**, **FT-1/FT-2**, **STRONG-BODY-A** are clearly INDEPENDENT candidate algorithms. An experimental baseline could begin with EN-BODY and rejection+later closed follow-through because their geometry is transparent, **but this is not a verified Coach formula or chosen Pine rule**. Do not force all candle types through an engulfing-only detector.

**NEXT:** M05 cross-timeframe state/coherence and an evaluation protocol for measuring disagreement between source-human interpretation and model candidates before any market-edge study. Full M04 threshold selection and behavior remain OPEN.
