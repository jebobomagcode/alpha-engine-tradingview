# PCSS Q&A Activity 02 — FARTCOIN Scalp, Pullback Location and Confirmation

**Study status:** COMPLETE source-first PCSS, mathematical comparison and independent research only, 2026-11-09 Asia/Manila. Original PDF page 31 rendered and **visually inspected** against its native selectable text; page 32 inspected only to confirm the subsequent Q&A boundary. **Page 31 has NO embedded trading chart or other figure**: the earlier coverage row describing a “FART chart” was inaccurate and is corrected.
**Only Coach-origin authority:** [original coach trading lessons.pdf, page 31](../../sources/coach%20trading%20lessons.pdf), SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. User's PCSS file SHA-256 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56 is local/private and not published. No Pine code, original screenshot trades, exchange-feed backtest, strategy execution or deployment.

## 1. Exact source-order inventory (complete text-only exchange)

The entire activity is on **one PDF page (p31)**. The exchange is Student→Coach→Student→Coach→Student→Coach. There is **no source chart, no OHLC sequence, no independent confirmation that any order was executed or filled, and no account size/fees/leverage/contract details**. The student's statement “Nag long na ako” is a **student-reported** position. Coach gives an alternative hypothetical entry he would wait for, not a certified performance result.

| ID | Original source item in order | What is established / still unknown |
| --- | --- | --- |
| QA2-01 | Page heading Q&A activity no.2 | One text-only page, no actual chart/figure |
| QA2-02 | Student says already LONG on FARTCOIN | Source reports a position but offers no order receipt |
| QA2-03 | Student asks where to take profit | Existing-position management question |
| QA2-04 | Coach asks basis for LONG based on earlier lessons | Reason-before-target teaching |
| QA2-05 | Student 1H: two red candles rejected support | No OHLC/image to validate support rejection |
| QA2-06 | Student 1H: subsequently one solid green candle | Not enough to certify strict bullish engulfing |
| QA2-07 | Coach asks for entry price | Trade details requested |
| QA2-08 | Student entry 0.2436 | Source-stated price, unit/venue unspecified |
| QA2-09 | Student stop loss 0.2385 | Student's stop, not Coach alternative |
| QA2-10 | Student says scalping only | Different holding-horizon intent from swing trade |
| QA2-11 | Coach says healthier for scalp continuation | Discretionary validation, not measured expectancy |
| QA2-12 | Coach says placement good 'since below supp and liquidity zone' | Ambiguous referent: do not silently assume entry or stop relative to an unseen level |
| QA2-13 | Coach introduces his own preferred entry alternative | Not an instruction to alter an already executed position |
| QA2-14 | Coach would wait at 0.238–0.240 | Proposed lower pullback zone |
| QA2-15 | Coach looks for bullish engulfing confirmation | Exact wick/body rules unspecified |
| QA2-16 | Coach also permits rejection-wick candle | Alternative candle reaction, geometry unspecified |
| QA2-17 | Coach looks for RSI bounce 40–50 | Not equivalent to mandatory crossover above50 |
| QA2-18 | Coach also wants price above EMA50 | Which timeframe and exact candle state unspecified |
| QA2-19 | Coach stop below 0.231 | Strict inequality, stop amount unknown |
| QA2-20 | Coach target 0.258 to 0.279 | Proposed range, not filled profit |
| QA2-21 | Coach advises trailing stop | Activation, offset and execution policy unspecified |
| QA2-22 | Coach calls this a pullback entry | Location and confirmation must be sequenced |
| QA2-23 | Coach emphasizes safer entry behavior | Qualitative language, not a guarantee of safety |
| QA2-24 | Coach says PATIENCE PO | Source emphasis |
| QA2-25 | Coach says let entry point/zone come to you | Avoid chasing; no exact time-out |
| QA2-26 | Coach recommends 30m Order Block as main zone | No chart/OB geometry or boundaries supplied |
| QA2-27 | Coach recommends 5m for entry confirmation | Lower-TF execution context |
| QA2-28 | Coach repeats always look for LTF confirmation | Final source instruction |

All 28 entries reflect source textual order, including the colloquial wording “below supp and liquidity zone”, “rsi bounce 40-50”, and Coach's repeated patience emphasis. The PDF contains no original theorem, mathematical derivation or attached exercise other than the Q&A itself.

## 2. Student's existing trade and reasoning (source first)

**STUDENT_SOURCE:** Student says already LONG on **FARTCOIN**, asks possible TP. Coach asks for the reason based on earlier lessons. Student describes on **1H** two red candles rejecting support, then a solid green candle. Coach requests the actual entry and the student reports:
- Entry **0.2436**;
- SL **0.2385**;
- Intended style **scalp**.

**Evidence limitation:** No photo of the student's 1H chart, account execution receipt, price quote currency, date/time, exchange or contract variant is in the source page. FARTCOIN is a named asset but **FARTUSDT spot/perpetual is not verified**. The red candles can have rejection wicks while closing red, but exact OHLC and candle geometry are unknown; “solid green” alone does not prove a fully specified bullish engulfing candle.

## 3. Coach's response in original order

**COACH_EXPLICIT:** Coach says the student's proposed position looks “mas healthy ... for scalp continuation” and comments that placement is correct “since below supp and liquidity zone.” This phrasing does not make the exact intended referent (the stop, a zone, or a drawn placement) fully identifiable without the missing chart. Preserve it as uncertain, not a confirmed stop-relative-to-zone fact.

**Coach's own different preferred scenario:**
1. Wait for price around **0.238–0.240**.
2. Look for **bullish engulfing** or **rejection wick candle** and **RSI bounce around 40–50**.
3. Check price **above EMA50**. The exact comparison timeframe is not explicitly attached to this EMA condition.
4. **Stop-loss below 0.231** (strict inequality; exact stop unspecified).
5. **TP from 0.258 to 0.279**, with a **trailing stop**; no unique trail parameters given.
6. Coach explains that this would be a **pullback entry**, emphasizes safer placement and **PATIENCE**: let the entry point/zone come to you.
7. Use **30M Order Block as the main zone**, then **5M for entry confirmation**, always looking for a lower-timeframe reaction.

**Source syntax:** Coach does not establish exact AND/OR grammar or bar timing between bullish engulfing, rejection wick, RSI bounce and price above EMA50; do not silently impose a rigid all-four Boolean filter. He does not declare that numeric 0.238–0.240 is a fully verified 30m OB boundary; no chart or independent OB candles are included.

## 4. Cross-lesson PCSS prerequisite recall

- Lesson08: location/zone first, reaction/confirmation before proposed entry and risk evaluation.
- Lesson09–11: support, liquidity and OB are **location concepts** whose true boundaries require price data.
- Lesson16: one continuation LONG example RSI “bounces above 50” whereas **this Coach Q&A says “RSI bounce 40–50”** during a scalp pullback. Do not universalize the earlier strict above-50 reading to exclude all future bullish bounces inside the 40–50 range. Source does not fully define whether bounce occurs into, from, or through this region.
- Lesson17: usual RSI14 midpoint50; overbought/oversold not automatic entries. This Q&A does not explicitly repeat RSI period.
- Lesson19: higher-TF bias → pullback location → LTF confirmation, now concretely 1H student context, **30m Coach's OB main zone**, **5m Coach's confirmation**.
- Lesson21: wait rather than chase; trade-specific stop is not necessarily global trend invalidation.
- Q&A1: bullish context is conditional, not a filled order or probability statistic.

## 5. Independent math: student's exact stop distance

The original source reports Entry E=0.2436 and stop S=0.2385:
R = E−S = **0.0051** per asset unit in the price's *unspecified quote currency*;
R/E = 0.0051/0.2436 = **2.093596%**, a stop-distance percentage, **not account-capital risk or expected loss** without size/leverage/costs.

If and ONLY IF applying Coach's *alternative* targets hypothetically to the student's exact entry/stop:
- T=0.258: reward 0.0144, gross RR=0.0144/0.0051≈**2.823529:1**.
- T=0.279: reward 0.0354, gross RR=0.0354/0.0051≈**6.941176:1**.

This cross-configuration is our arithmetic comparison, **not** evidence Coach explicitly assigned those targets to this student's already-open position.

## 6. Independent math: Coach's alternative has NO fixed RR

Coach proposed E in [0.238,0.240], **S<0.231** and T in [0.258,0.279]. He did **not** specify an exact S or a fill. Hence a unique RR **cannot** be calculated from original text. To make a transparent illustrative comparison, independently select **S=0.2300**, which satisfies Coach's strict inequality. Before commissions, slippage, funding or spreads:

| Hypothetical E | T | E−S | T−E | Gross RR |
| ---: | ---: | ---: | ---: | ---: |
| 0.238 | 0.258 | 0.008 | 0.020 | 2.500:1 |
| 0.240 | 0.258 | 0.010 | 0.018 | 1.800:1 |
| 0.238 | 0.279 | 0.008 | 0.041 | 5.125:1 |
| 0.240 | 0.279 | 0.010 | 0.039 | 3.900:1 |

**Material finding:** Coach's entry is **0.0036–0.0056 lower** than the student's (approx 1.48–2.30% of student E), but Coach's independently assumed wider stop means a **larger per-unit risk** than the student's tight 0.0051 stop. Thus student's numeric RR *could be higher* under these different stop assumptions, even though entry is higher. A lower entry price is not sufficient to prove safer/better expectancy; the placement's survival, risk sizing, fill probability, trend conditions and after-cost outcome remain unknown.

The same hypothetical stop S=0.230 gives Coach's price-risk percentage about 3.36% at 0.238 and 4.17% at 0.240, versus student 2.09% stop-distance percentage. These are **not account-risk percentages**. For a fixed account risk budget in a simple linear position, quantity is inversely proportional to stop distance, subject to product contract/fees and tick rules.

## 7. Critical source gaps for the future TradingView system

1. No FARTCOIN ticker/exchange/spot-vs-perpetual and no timeframe screenshots or OHLC; cannot validate drawn support/liquidity/30m OB or red/green candle structure.
2. No order execution record for the already-open position; it is student-reported, not independently verified.
3. Coach's ambiguous “below supp and liquidity zone” is not attributable to a specific exact price anchor from text alone.
4. What RSI “bounce 40–50” means: touch 40, hold above 40, rebound while in band, cross 50, or merely approach? Undefined; unlike Lesson16's strict wording.
5. Which timeframe holds **price above EMA50**? Not specified explicitly in this sentence; don't assert source exact 5m rule.
6. Exact 30m OB formation, mitigation, invalidation, contact definition or relationship to numerical 0.238–0.240 missing.
7. Bullish engulf/rejection geometry, completed versus developing 5m bar and setup expiry absent.
8. Precise stop below 0.231 not supplied; trailing stop activation/distance, take-profit partials and fill cost unknown.
9. Student is already LONG whereas Coach gives an alternative WAIT-for-pullback entry. Do not collapse them into one simultaneously executable order or claim Coach instructed the student to exit/re-enter.
10. Coach's word “safe” is discretionary and comparative, not empirical certification of safety or profit.

## 8. Independent Ponder research direction (NOT code)

A source-traceable research model should distinguish an **EXISTING_POSITION_ASSESSMENT** (student's stated 0.2436/0.2385; unknown size/fill), versus a **NEW_PULLBACK_CANDIDATE** for Coach's alternative. Show 1H source context, 30m OB location and 5m confirmation as independent observations, tracking exact symbol/timeframe/bar-known times. RSI bounce from 40–50 should have alternative explicitly named definitions, not a fabricated universal threshold. Return WAIT/INSUFFICIENT if zone or confirmation is not observable. Treat price-to-stop risk and account risk separately.

See [QA2 independent research](../research/qa-02-fartcoin-scalp-entry-risk-and-rsi-band.md). Official TradingView [repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/) and [multi-timeframe data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/) are *external software references*, not Coach rules. No Pine behavior has been tested.

**Study verdict:** All 28 source items from original page 31 audited, no illustration/calculation/proof exists on that page; source ambiguities and independent computations distinguished. **Q&A no.2 COMPLETE for study only; Q&A no.3 PDF page32 NEXT.** Entire PDF still unfinished (p32–35 outstanding).
