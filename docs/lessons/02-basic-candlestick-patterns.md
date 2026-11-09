# Lesson 02 — Basic Candlestick Patterns (PCSS source-complete study)

**Status:** COMPLETE — full page-2/3 inventory, visual audit, user-facing PCSS teaching, independent cautions and design questions.  
**Source:** [Coach Fredy's one and only original PDF, pp. 2–3](../../sources/coach%20trading%20lessons.pdf)  
**Original PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`  
**Full personal PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`  
**Study date:** 2026-11-09 (Asia/Manila)  
**Scope:** 02. Basic candle stick pattern only, including adjacent illustrations. No Lesson 03 teaching, code, TradingView compilation, or backtesting.

## Source-first audit — exact original sequence

Both pages were visually rendered from the exact original PDF at 180 dpi, and the page text was compared with the embedded charts/images. The following ledger is the checked source inventory, **not a list of independently validated trading signals**.

| # | PDF page and original item | Figures and/or text, with noteworthy details | Covered |
| --- | --- | --- | --- |
| 02-01 | p. 2 heading “02. Basic candle stick pattern”; “BASIC CANDLESTICK PATTERN” | Introduces candle pattern lesson | Yes |
| 02-02 | p. 2 upper-left orange-bordered image | “Doji Candlesticks”: open/close/high/low annotations; green/red near-flat bodies; long upper/lower wick variants | Yes |
| 02-03 | p. 2 upper-right orange-bordered image | Hammer silhouette with long lower wick; Shootingstar silhouette with long upper wick | Yes |
| 02-04 | p. 2 text | Lists three main patterns in order: Hammer, Shooting Star, Doji | Yes |
| 02-05 | p. 2 “HAMMER (bullish signal)” | Long lower wick; small body at top; price lower then pushed up/rejection; best at support, downtrend possible reversal | Yes |
| 02-06 | p. 2 bottom-left chart with volume | Two marked “Hammer at Support” areas, horizontal support line, multiple rebounds, red/green candles and volume bars. Historical provenance/scale/contract unspecified; cannot infer statistical probabilities from image | Yes |
| 02-07 | p. 3 “SHOOTING STAR (bearish signal)” | Long upper wick, small lower body; higher price rejection; best resistance, uptrend possible reversal | Yes |
| 02-08 | p. 3 upper-left chart | Dashed horizontal resistance line, annotated shooting star near retest, subsequent decline shown. Retrospective illustration, not prospective proof | Yes |
| 02-09 | p. 3 “DOJI (indecision)” | Little/no body, upper+lower wicks, “buyers = sellers” metaphor, indecision; support/resistance or after strong move, possible range/reversal | Yes |
| 02-10 | p. 3 “DIFFERENCE (MADALING TANDAAN)” | Hammer support bullish possibility; shooting star resistance bearish possibility; Doji no control, wait confirmation, possible range | Yes |
| 02-11 | p. 3 lower-left supplemental chart | “Shooting Star vs. Inverted Hammer” with visually similar upper-wick geometry in different preceding-price contexts. Inverted Hammer appears in figure, **not among three formal written pattern headings** | Yes |
| 02-12 | p. 3 lower-right supplemental diagram | “Bullish Hammer” vs “Inverted Hammer”: labeled high/low/open/close; illustrates wick direction and small candle body. No separate formal rule for inverted hammer given in source text | Yes |

The source has **no formal proof, quantitative OHLC cutoff, independent exercise prompt, stepwise statistical test, or exact crypto example** for these pages. Independent worked OHLC examples and formulas below are supplemental, never mislabeled as Coach-supplied.

## 1. Read a candle mathematically — supplementary prerequisite

**COACH_EXPLICIT:** diagrams show high, low, open and close and use wicks/bodies to distinguish shapes.

**INDEPENDENT EXPLANATION:** For a candle on a fixed interval, let open \(O\), high \(H\), low \(L\), close \(C\). Valid ordinary OHLC requires \(L\leq\min(O,C)\leq\max(O,C)\leq H\).

- Real-body size: \(B=|C-O|\).
- Upper wick: \(U=H-\max(O,C)\).
- Lower wick: \(D=\min(O,C)-L\).
- High-to-low range: \(R=H-L=B+U+D\).
- Bullish body if \(C>O\); bearish if \(C<O\); exact flat body if \(C=O\).

**Critical limit:** OHLC does **not** tell us the chronological order of the intra-bar high and low, exact transaction volumes at each price, or whether buyers/sellers were “in control” at every instant. It only reports endpoint and extrema. The PDF's price-action narrative is a plausible interpretation, not direct order-flow evidence.

### Worked example A (ours, not in source)

Suppose a hypothetical candle: \(O=100,H=104,L=92,C=102\). Then \(B=2,\ U=2,\ D=8,\ R=12\). A small top body and long lower wick make it hammer-shaped. To call it a **contextually significant Hammer**, we would also need the preceding trend and independent support location. The example's price numbers are illustrative, not real-time market data.

## 2. Hammer

**COACH_EXPLICIT, p. 2:** Long lower wick; small body near top. Price falls but is pushed back upward; rejection of lower levels. Best near support and in a downtrend for possible bullish reversal.

**Meaning:** the candle closes much closer to its upper end than the observed low. That is consistent with a recovery during the interval, but doesn't prove persistent buyer dominance or tell the high/low temporal sequence. The color is not an essential part of Coach's written geometric definition.

**Visual teaching:** study original p. 2 bottom-left chart: repeated lows meet the marked support band. A hammer shape at these areas is highlighted; a later upward movement is *shown in the example*, but it is not an independently verified event study.

**Independent caution:** hammer geometry in the middle of a range or a thin illiquid token market is less informative as a reversal narrative. A wick may result from brief executions, feed spikes, liquidation cascades or thin liquidity.

**Not yet specified by Coach on these pages:** how long is “long”, how small is “small”, which support line is valid, what qualifies as a downtrend, whether candles must close, or what separate confirmation must occur.

## 3. Shooting Star

**COACH_EXPLICIT, p. 3:** Long upper wick and small lower body. Price moves higher but returns lower, showing upper-price rejection. Best near resistance or after an uptrend for a possible bearish reversal.

**Visual teaching:** the p. 3 upper-left chart features a dashed resistance, a marked wick near it, and a later decline. Later decline is included in the illustration, **not an evidence-based estimate of future bearish probability**.

### Worked example B (ours)

\(O=100,H=110,L=98,C=99\) gives \(B=1,\ U=10,\ D=1,\ R=12\). The silhouette is consistent with a shooting star; whether it is relevant depends on preceding uptrend and resistance context.

**Independent caution:** an upper wick need not represent verified institutional sell orders, and subsequent price can break resistance. A pattern label is not a short-entry instruction.

## 4. Doji

**COACH_EXPLICIT, p. 3:** Tiny/nearly zero real body with upper and lower wicks. Associated with indecision; watch near support/resistance and after strong moves; wait for confirmation. The mnemonic states it may lead to ranging.

**Independent clarification:** \(O\approx C\) only means the interval's net movement is small relative to its path range. “Buyers = sellers” is Coach's explanatory metaphor. Executed trade matching always has both sides, and candle geometry alone cannot measure aggressor pressure or literal balance of intentions.

### Worked example C (ours)

\(O=100.00,H=103.00,L=97.00,C=100.05\) produces \(B=0.05,\ R=6\), hence \(B/R\approx0.00833\), less than 1% of the candle range. It is doji-shaped by many plausible definitions, though Coach supplies **no numerical doji threshold**.

A Doji may precede a range, a reversal, or continuation. It is not an automatic BUY or SELL.

## 5. Source mnemonic and overlooked supplemental diagrams

**COACH_EXPLICIT, p. 3 — “DIFFERENCE (MADALING TANDAAN)”**:
- Hammer — rejection at support; price may rise.
- Shooting Star — rejection at resistance; price may fall.
- Doji — no clear control; await confirmation; range possible.

**SUPPLEMENTAL FIGURE CONTENT:** The bottom-left p. 3 figure explicitly contrasts Shooting Star vs. Inverted Hammer, while bottom-right compares Bullish Hammer and Inverted Hammer OHLC anatomy. This is why *a silhouette is not a trade direction*: a long-upper-wick body after a rally near resistance may be described as shooting star, but a similar candle after a decline may be described as inverted hammer. This contextual distinction is standard technical-analysis interpretation and drawn from the visible figure, not a separately stated Coach rule with numerical conditions. Do **not** mark Inverted Hammer as a fourth original textual lesson.

## 6. Ponder: precision, falsification and limits

1. **Candle morphology vs. price location vs. confirmation are distinct.** A valid shape does not establish support, a trend reversal, nor permission to enter a trade.
2. **A high/low wick is not direct evidence about participant identity.** OHLC cannot identify “institutions” or the exact temporal sequence within a bar.
3. **A seemingly predictive historical annotated chart is vulnerable to selection bias.** A selected winner does not establish the unconditional pattern success rate.
4. **Single patterns do not have guaranteed predictive edge.** External research is mixed and sensitive to exit rule, trend definition, market and costs: Marshall/Young/Rose (2006) reported no value for DJIA stock candlestick rules; Lu et al. (2015) found selected multi-candle patterns profitable with one holding strategy but not another; tests on Thai equities found limited directional forecasting utility. These **equity-market results cannot be transferred as validation to crypto or gold tokens**.

Independent citations, not Coach material:
- CME Group, OHLC definition and subjectivity of pattern interpretation: https://www.cmegroup.com/education/courses/trading-and-analysis/technical-analysis
- Marshall, Young & Rose (2006), DJIA candlestick results: https://www.sciencedirect.com/science/article/pii/S0378426605002116
- Lu et al. (2015), holding-strategy dependence: https://www.sciencedirect.com/science/article/pii/S0378426615002678
- Thailand study (2017), limited predictive evidence: https://journals.sagepub.com/doi/full/10.1177/2158244017736799
- TradingView official Pine v6 bar-state confirmation: https://www.tradingview.com/pine-script-docs/concepts/bar-states/
- TradingView repainting/MTF caveats: https://www.tradingview.com/pine-script-docs/concepts/repainting/

## 7. Implications for eventual crypto TradingView implementation

**CANDIDATES ONLY — no code authorized.** See the separately tracked [research spec candidates](../research/02-candlestick-rule-candidates.md).

Proposed logically separate states:
1. VALID_OHLC / INVALID_OHLC; distinguish incomplete bar from confirmed bar.
2. GEOMETRY_HAMMER / GEOMETRY_SHOOTING_STAR / GEOMETRY_DOJI / OTHER / AMBIGUOUS.
3. TREND_CONTEXT and ZONE_CONTEXT detected independently with source-backed definitions from later lessons.
4. PATTERN_AT_RELEVANT_LOCATION (candidate, not automatically a signal).
5. WAIT_CONFIRMATION vs CONFIRMED vs INVALIDATED — confirmation logic is NOT defined by Lesson 02 and remains pending later lessons.

**Market D-013:** Applies to crypto, including XAUUSDT, XAUTUSDT and PAXGUSDT, but each ticker's venue/product has independent feed/tick/liquidity semantics. Don't assume one wick's significance transfers across spot, perpetual or tokenized-gold products.

## Coverage verdict and continuity

- All original prose headings, three introduced patterns, closing mnemonic, and **six identifiable orange-bordered image panels** across the two pages were inspected visually and described. The panels comprise p. 2 Doji chart, hammer/shooting silhouettes and hammer-at-support price/volume chart; and p. 3 shooting-at-resistance chart, shooting-vs-inverted comparison and hammer-vs-inverted comparison.
- The p. 3 inverted-hammer figure was accounted for without fabricating a fourth formal textual pattern.
- Three independent example candles checked against \(R=B+U+D\). No tests of trading profitability or live charts performed.
- **Lesson 02 is COMPLETE at the source study level.** All proposed quantitative pattern thresholds remain OPEN_UNRESOLVED. Completion is for faithful study, not a claim of deterministic implementation.
- **Next when owner says “Next” or “Proceed”: Lesson 03 — Trading Risk Reward, PDF pp. 4–5.** Do not auto-advance.
