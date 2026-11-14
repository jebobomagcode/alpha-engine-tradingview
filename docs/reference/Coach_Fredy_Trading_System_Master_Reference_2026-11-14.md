# Coach Fredy Trading System — Comprehensive Source, PCSS, Research and Improvement Master Reference

**Version:** 2026-11-14 research consolidation  
**Source repository:** [jebobomagcode/alpha-engine-tradingview](https://github.com/jebobomagcode/alpha-engine-tradingview)  
**Primary Coach source:** [`sources/coach trading lessons.pdf`](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/sources/coach%20trading%20lessons.pdf) (35 pages)  
**Intended use:** source-faithful study, conceptual methodology design, rule qualification, research and critique.  
**Explicit exclusion:** no platform implementation, source code, chart-interface instructions, integration design, deployment, product-development procedure, or operational automation.

> **Evidence warning.** This is a consolidation of the repository's detailed source-study, PCSS, methodology and research documents, not a newly Coach-approved instruction manual or a trading performance study. Original Coach teachings, PCSS explanations, independent hypotheses and unresolved questions are kept distinct. A backtest-like illustration is not proof of profitability. Sources were retrieved from the repository's main branch and relevant November 14 research-design branch; where newer material remains experimental, that status is preserved.

## Contents

1. Mission, source hierarchy, terms and evidence discipline
2. Complete source-unit inventory and page map
3. The Coach method in one integrated decision sequence
4. PCSS: how each source lesson is studied and interpreted
5. Lessons 01–21: complete ordered conceptual reference
6. Coach Q&A Activities 01–03
7. Final Notes N-01 and N-02
8. Scenario families: continuation, range, scalp, countertrend and reversal
9. Independent research architecture: M00–M07
10. Structural pivots, swing references, BOS/CHoCH and causal corrections (R1)
11. Zones, OB, FVG, Fibonacci, role flip, contact and invalidation (R2)
12. Candle geometry, alternative confirmations and range triggers (R3)
13. Multi-timeframe disagreement, setup lifecycle, WAIT and insufficiency (R4)
14. Indicators, confluence dependence, and objective interpretations
15. Full risk, reward, margin, sizing, exits, costs and expectancy
16. Important source-case computations and conditional plans
17. Consolidated Coach-to-research gap ledger
18. Experimental methodological defaults, challengers and limitations
19. Research evidence, falsification and validation standards
20. Terminology dictionary, final principles and source bibliography

---

# 1. Mission, source hierarchy and evidential discipline

The project's intellectual task is to understand Coach Fredy's *entire* stated trading framework before supplementing the definitions missing from his discretionary lessons. The user explicitly permits independent improvements and does not require the improved framework to reproduce every undocumented judgment. That permission does not transform independent rules into Coach's words. The most useful system is therefore a **source-grounded baseline with openly differentiated, falsifiable extensions**, not a mixture presented as one unalterable doctrine.

### Source hierarchy

1. **COACH_EXPLICIT** — the 35-page original `coach trading lessons.pdf`, including original text, figures, quoted price levels, source examples and recorded Coach responses. This is the **only** repository-designated Coach-origin document.
2. **PCSS_INTERPRETATION** — the comprehensive lesson studies explaining the original source in order, deriving prerequisite mathematics, accounting for illustrations, and carefully distinguishing observed figures from commentary.
3. **STUDENT_ASSERTION** — a student answer or hypothetical trade in a Coach Q&A; not automatically a Coach-endorsed order, observed fill or validated market fact.
4. **INDEPENDENT_EXTENSION / EXPERIMENTAL** — precise mathematical definitions or additional risk safeguards introduced by the project's research. They are candidates, not certified source rules or profitable methods.
5. **VERIFIED_WITHIN_SCOPE** — a specifically named proof, calculation, synthetic case, or controlled observation; this label must name *what* was verified, rather than falsely implying actual trade performance.
6. **OPEN_UNRESOLVED / UNKNOWN** — a rule, parameter, reference, dataset, sequence or decision for which the source and available evidence do not establish a unique answer.

The public repository publishes a *summary* of the personal PCSS protocol, but **not the original private PCSS document**. This master can faithfully compile the public operational summary and completed lesson studies; it cannot claim to reproduce the private PCSS file word for word.

The repository source-manifest records the 35-page original's SHA-256 as `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`, Git blob SHA-1 `c99de01b9178e16e240f83f5c4594fa5683a1ba2`, and size 2,267,976 bytes. A 2026-11-09 audit maps **26 original source units to all 35 PDF pages**: 21 numbered lessons, 3 Q&A activities, 2 concluding notes. This is *documented study coverage*, not evidence that every trading mechanic has been uniquely formalized or that every market claim is true.

### Core safeguards

- Preserve each example's exact **market, venue/product, timeframe, data basis, date where known and provenance**. Forex gold spot prices, gold-linked derivatives, gold tokens, BTC from distinct exchanges, TON, SOL and Philippine equities cannot be treated as the same price series.
- A retrospective figure shows what somebody annotated **after seeing a chart**; it does not establish the exact point when a reference was knowable to a real-time trader.
- A higher probability, safer trade, institutional accumulation, liquidity grab, or strong zone is often **qualitative Coach language**. None of these establishes numerical win rate, actor identity, causality or guaranteed execution.
- A trading scenario can be directionally interesting but not *eligible* for a source-style entry. `WAIT`, `INSUFFICIENT`, `REASSESS`, and `NO TRADE` are legitimate, informative outcomes.
- Historical diagrams, paper cases, algebraic proofs, controlled behavior tests and after-cost market performance are **different kinds of evidence**.

# 2. Original source-unit inventory

| Unit | Original PDF pages | Main subject | Full source-first PCSS record |
|---|---:|---|---|
| 01 | 1 | Trading 101: choosing a market | [01](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/01-trading-101.md) |
| 02 | 2–3 | Hammer, shooting star, doji | [02](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/02-basic-candlestick-patterns.md) |
| 03 | 4–5 | Risk:reward, win rates, compounding | [03](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/03-trading-risk-reward.md) |
| 04 | 6 | Higher and lower timeframes | [04](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/04-time-frame.md) |
| 05 | 7 | Leverage, margin, exposure | [05](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/05-leverage-margin.md) |
| 06 | 8 | Bullish and bearish engulfing | [06](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/06-engulfing-pattern.md) |
| 07 | 9 | Structure and confluence | [07](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/07-market-structure-confluence.md) |
| 08 | 10 | Complete conditional entry sequence | [08](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/08-trading-entry-workflow.md) |
| 09 | 11 | Support/resistance and role reversal | [09](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/09-support-resistance.md) |
| 10 | 12–13 | Gold-spot range, conditional long/short | [10](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/10-marking-support-resistance.md) |
| 11 | 14 | Order blocks; BOS versus CHoCH | [11](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/11-order-block-bos-choch.md) |
| 12 | 15–16 | BOS and continuation | [12](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/12-bos-break-of-structure.md) |
| 13 | 17–18 | SOL countertrend short and conditional long | [13](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/13-manage-your-risk-sol.md) |
| 14 | 19 | Fibonacci retracement and zones | [14](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/14-fibonacci-retracement.md) |
| 15 | 20 | Reliability and confluence components | [15](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/15-reliability-on-charting.md) |
| 16 | 21 | Long and short continuation examples | [16](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/16-long-short-setup.md) |
| 17 | 22 | RSI and momentum | [17](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/17-rsi-relative-strength-index.md) |
| 18 | 23 | EMA and regime context | [18](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/18-ema-exponential-moving-average.md) |
| 19 | 24 | RSI + EMA top-down method | [19](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/19-rsi-ema-topdown-analysis.md) |
| 20 | 25 | CHoCH and possible structural shift | [20](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/20-choch-change-of-character.md) |
| 21 | 26–28 | TON multi-timeframe conditional analysis | [21](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/21-tonusdt-topdown-setup.md) |
| Q&A 01 | 29–30 | BTC bullish HTF, retest and disconfirmation | [QA1](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/qa-01-btc-htf-bias-and-confirmation.md) |
| Q&A 02 | 31 | FARTCOIN long, scalp plan and RSI 40–50 | [QA2](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/qa-02-fartcoin-scalp-pullback.md) |
| Q&A 03 | 32 | BTC bearish HTF, 15m consolidation, both conditional directions | [QA3](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/qa-03-btc-consolidation-retest-and-breakout.md) |
| N-01 | 33 | Timing, forex sessions and macro news | [N1](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/note-01-location-time-and-economic-calendar.md) |
| N-02 | 34–35 | PSE:BPI multi-timeframe stock analysis | [N2](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/lessons/note-02-bpi-bsp-stock-charting.md) |

The individual linked study documents contain the page-by-page figure and paragraph inventories; they remain the authoritative **full-detail primary-source companions** to this consolidated reference. This master integrates their methodological content and research rather than claiming to be a verbatim retranscription of the Coach PDF.

# 3. The integrated Coach decision framework

A useful **source-faithful conceptual reconstruction** is:

1. **Identify the market and exact instrument.** Know whether the chart describes crypto, forex or equities, what product is being traded, and what quoted prices mean.
2. **Read the higher-timeframe context:** rising HH/HL, falling LH/LL, or unresolved/ranging structure. Identify important support/resistance and potential pullback locations. RSI and EMA may inform context but are not independent replacements for price structure.
3. **Select a scenario, not just a direction.** Source examples include trend continuation, explicitly conditional sideways-range reversal, countertrend scalp, and post-breakout alternatives. These differ in holding horizon, invalidation and evidence requirements.
4. **Wait for a meaningful price location.** A structurally attractive chart in the middle of a range is not automatically an entry. In Lesson 08, failure to reach the preselected zone means **NO TRADE**.
5. **Observe an appropriate lower-timeframe reaction** near that location. Lesson 08 explicitly offers *alternatives*: engulfing; a rejection candle **plus follow-through**; or a strong-body confirmation. Do not require all three at once. Other source scenarios use different confirmations.
6. **Respect time.** The Lesson 08-style entry comes *after the confirmation candle closes*; the sideways gold-range example separately discusses a *break of confirmation*. Historical drawings must not convert a not-yet-known pivot or zone into an earlier signal.
7. **Assess stop, target and risk** with actual entry and price distances, plus the chosen product's quantity and cost assumptions. A possible direction or attractive target is not a complete trade plan.
8. **Stand aside, reassess or invalidate** if the scenario lacks location, sufficient completed evidence, coherent risk or current context. A lower-timeframe possible CHoCH does not itself reverse the higher-timeframe trend.

**This sequence is a synthesis**, not an assertion that every Coach example shares one universal Boolean checklist. For example, the SOL pullback short intentionally trades against a still-bullish 4H context; the BTC consolidation Q&A distinguishes a conditional bearish rejection from a later possible bullish breakout. Good analysis can legitimately report both paths as *conditional*, rather than force a single BUY/SELL prediction.

# 4. PCSS study method and interpretation standard

The repository's [`PCSS_PROTOCOL.md`](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/PCSS_PROTOCOL.md) summarizes the authorized approach:

1. Inventory each original PDF page in source order, including paragraphs, definitions, examples, diagrams, screenshots, annotations, notes and qualifications.
2. Preserve what Coach actually says or shows *before* introducing reinterpretation.
3. Explain intuition, prerequisite vocabulary and price-action logic with clear examples and faithful figures.
4. Formalize ambiguous concepts only after stating what is **missing**; label every threshold or rule not in the source as independent.
5. Challenge assumptions and consider alternatives, counterexamples, misleading hindsight, indicator dependence and financial consequences.
6. Cross-reference other lessons without erasing genuine variation among examples.
7. Check every arithmetic example and all claims against image provenance, market identity and temporal constraints.
8. Maintain source traceability and evidence status; a complete lesson study is not a profitable trading strategy.

The study standard encourages understandable language while retaining discipline-specific terms. It does **not** require forced active-recall quizzes, and it does **not** authorize treating a hypothetical example as an actual market trade. A mathematically true correction should be displayed as a correction rather than silently rewriting Coach's original text.

---
# 5. Original Lessons 01–21 — complete conceptual reference

## Lesson 01 (PDF p1): Trading 101 — markets, discipline and risk

**COACH_EXPLICIT.** Choose where you trade before learning setups. Coach compares: (a) **cryptocurrency**, whose quoted advantages include around-the-clock access, active price movement and comparatively low possible starting capital, but also high volatility, hype/scams and FOMO; (b) **forex**, described as potentially less erratic with active currency sessions and leverage, but with material leverage and account-loss risks and a 24/5 schedule; and (c) **Philippine shares**, associated with ownership, dividends and longer holding horizons, but limited market hours, often slower movement and greater nominal capital for a given peso return. Named intermediaries or exchanges are descriptive examples, not recommendations or verified current terms.

**PCSS and improvement.** Asset class, ticker, actual instrument, exchange, settlement currency, and product (spot, perpetual, shares, OTC/CFD, etc.) are separate facts. "Crypto moves more" or "forex is cleaner" is neither a universal theorem nor proof of easier profit. Price volatility increases possible gain *and loss*, and leverage magnifies the effect of exposure rather than creating free value. Behavioral discipline, patience, identifying actual edge and keeping losses bounded matter more than stories about a market being inherently safe. A trading idea must be checked on the product and conditions for which it is used.

**Open:** comparative risk statistics by regime, venue-specific access and liquidity, future instrument qualifications, fee/contract differences, and whether perceived technical clarity survives out-of-sample tests.

## Lesson 02 (pp2–3): Basic candlestick patterns

**COACH_EXPLICIT.** **Hammer:** small body toward the top, long lower wick, visual rejection of lower prices. Near support and after weakness, it can indicate a *possible* bullish reversal. **Shooting star:** small body toward the bottom, long upper wick, often examined near resistance/uptrend as possible bearish rejection. **Doji:** nearly equal open and close, often with wicks, suggests indecision; by itself it does not select a direction. Coach's mnemonic connects hammer with bullish possibility at support, shooting star with bearish possibility at resistance, and doji with waiting for confirmation. Figures also compare shooting stars and **inverted hammers**; the latter appears visually but is *not* a fourth main written pattern definition.

**PCSS mathematical anatomy (independent):** for a valid candle, open \(O\), high \(H\), low \(L\), close \(C\), the body is \(B=|C-O|\), upper wick \(U=H-\max(O,C)\), lower wick \(W=\min(O,C)-L\), total range \(R=H-L=B+U+W\). If \(C>O\) it has a bullish body; if \(C<O\) bearish; equality yields zero body. A long wick describes the **shape of observed prices**, not actual identities of buyers, sellers or hidden institutions.

**Independent improvement.** Keep separate (1) the candle's geometry, (2) previous trend or location, (3) post-pattern follow-through, and (4) conditional trade eligibility. Candidate thresholds such as minimum \(W/R\), maximum \(B/R\) or a doji ratio need explicit parameters, equality policy and market-specific validation. A zero-range but valid candle is not the same as malformed OHLC. Neither a hammer nor a doji guarantees reversal.

## Lesson 03 (pp4–5): Risk:reward, win rate, long-term simulation

**COACH_EXPLICIT numerical example.** Capital starts at **₱5,000**. Each modeled loss costs **₱100**, and each modeled win returns **₱200**, corresponding to **1 risk : 2 reward** before costs. Ten trades:

| Scenario | Wins | Losses | Gross winning amount | Gross losing amount | Net | End capital |
|---|---:|---:|---:|---:|---:|---:|
| 50% winners | 5 | 5 | ₱1,000 | ₱500 | **+₱500** | ₱5,500 |
| 40% winners | 4 | 6 | ₱800 | ₱600 | **+₱200** | ₱5,200 |
| 30% winners | 3 | 7 | ₱600 | ₱700 | **−₱100** | ₱4,900 (derived) |
| 45% of 20 trades | 9 | 11 | ₱1,800 | ₱1,100 | **+₱700** | ₱5,700 |
| Next 20-trade cycle: loss ₱114, gain ₱228 | 9 | 11 | ₱2,052 | ₱1,254 | **+₱798** | ₱6,498 |
| Same 45% win rate but 1:1, ₱100 per win/loss | 9 | 11 | ₱900 | ₱1,100 | **−₱200** | ₱4,800 (derived) |

Coach describes a rough **35–40%** win-rate zone for a 1:2 scheme. The **independent exact zero-cost gross break-even probability** for full 2R wins and full 1R losses is \(1/(2+1)=1/3\), or 33⅓%. In *exactly ten* binary trades, four wins are the first positive integer outcome. Actual costs raise break-even. The 1:1 comparison holds win rate constant across different reward targets; that is a **hypothetical counterfactual**, not evidence that the same strategy would have the same win probability at different targets.

**PCSS distinction.** Coach's next-cycle example resets the cash risk **between twenty-trade blocks**, not after every trade. Repeating the hypothetical +14% cycle would generate ₱5,700; ₱6,498; ₱7,407.72; ₱8,444.80; ₱9,627.07 from initial ₱5,000. These are *arithmetic trajectories under assumed repeated outcomes*, not forecasts, broker statements or observed annualized returns.

**Research improvement.** Separate **planned price-distance R:R**, **cash risk given quantity**, **net outcomes after fees/slippage/funding**, and **expectancy under a *measured* outcome distribution**. A positive planned 2R does not imply a positive expected return, a guaranteed stop fill or sustainable compounded growth. Study losing streaks, sample uncertainty and risk-of-ruin only under specified assumptions.

## Lesson 04 (p6): Higher timeframe and lower timeframe

**COACH_EXPLICIT.** Coach gives 1H/4H examples for **higher-timeframe (HTF)** trend, support/resistance and bias, and 5m/15m examples for **lower-timeframe (LTF)** reaction, confirmation, entry, stop and target. One example uses 1H or 4H analysis followed by a 5-minute entry examination. The source does not mandate one universal HTF/LTF pairing and does not prescribe a mathematical voting rule between timeframes. "No need overconfirm" on the HTF is a teaching preference, not permission to act on an unconfirmed LTF trigger.

**PCSS.** A 4H bar spans four 1H bars, sixteen 15m bars or forty-eight 5m bars, assuming aligned continuous intervals; a 1H bar spans four 15m or twelve 5m bars. Every timeframe should carry its **own** structural and indicator observations. A lower-timeframe bearish reaction inside a bullish 4H market can reflect a pullback; it does not rewrite 4H history.

**Research improvement.** Only evidence **final and genuinely available by the decision time** may support the decision. Compare a conservative context frozen when the local candle opens with a model admitting newly confirmed context at decision close; document delays and conflicting readings. Do not import a later-formed HTF high/low into an earlier decision. Missing bars or unfinished HTF observations are reasons for qualified uncertainty, not neutral evidence.

## Lesson 05 (p7): Leverage, margin and liquidation

**COACH_EXPLICIT.** With **$100 posted capital**, exposure at 1× is illustrated as **$100 notional**, 10× as **$1,000**, and 20× as **$2,000**. With a **fixed $100 position**, an initial-margin illustration is about $100 at 1× and $10 at 10×. Coach warns of volatility, rapid liquidation and leverage magnifying risk; his examples of maximum leverage and forex broker ratios are contextual, not permanent venue rules. Crypto risk can be greater on volatile instruments; forex also carries leverage and gap risk. Appropriate lot/quantity sizing matters.

**Independent correction.** If position **size remains fixed**, changing selected leverage normally changes collateral requirements and liquidation headroom, **not** gross price P&L for the same price move and linear position. If posted collateral stays fixed and leverage is used to expand notional, price P&L magnitude increases correspondingly. Distinguish free margin, initial/maintenance margin, cross versus isolated collateral, mark-price liquidation, price of the traded contract and potential loss beyond a planned stop.

A stop-risk budget of $100 is **not** the same concept as $100 initial margin. No universal liquidation-price approximation is reliable without exact contract, maintenance tier, collateral mode, fees and account conditions. An order may be liquidated or slipped before a hypothetical ideal stop is filled.

## Lesson 06 (p8): Engulfing pattern

**COACH_EXPLICIT.** At **support**, a large green candle engulfing the previous red candle may suggest a bullish reaction; at **resistance**, a large red candle engulfing a prior green candle may suggest a bearish reaction. The figures show stronger and weaker shapes, and subsequent movement, but no required mathematical body/wick inequality, percentage threshold, mandatory follow-through duration or verified win rate.

**Independent alternative definitions.** A **real-body engulf** compares each candle's open/close body. A **full-range engulf** requires the entire second high–low range to contain the first range. They are *not equivalent*. For example: previous red candle \((O,H,L,C)=(105,110,98,101)\), second green \((100,107,99,106)\); the green body contains the previous red body, but the green candle's wicks do **not** contain the prior high 110 or low 98. Optional strength criteria such as body/range or body-size ratio are separate hypotheses, not original Coach requirements.

Preserve a distinction between **pattern observed**, **pattern at an eligible zone**, and **full setup ready**. A single bullish engulfing candle away from required support cannot satisfy the specific Lesson 08 zone gate. One candle simultaneously qualifying as body-engulfing and large-body is not two independent measurements of buying pressure.

## Lesson 07 (p9): Market structure and confluence

**COACH_EXPLICIT.** Coach organizes a valid setup around **Trend + Zone + Signal**. Uptrend features **higher highs (HH) and higher lows (HL)**; downtrend features **lower highs (LH) and lower lows (LL)**. Sideways markets have weak directional progression; he cautions against indiscriminate trades unless broader context is considered. A textbook bullish setup is uptrend + support + bullish engulfing; bearish is downtrend + resistance + bearish engulfing. Coach calls these "high probability," but supplies no numerical probability or out-of-sample evidence.

**PCSS improvement.** A single local higher high or lower low is insufficient to declare a complete trend without defining comparable structural swings. An ongoing price move can contain corrections that produce a lower-TF lower high inside a HTF uptrend. Trend, S/R and candlestick observations are **related transformations of price**, and adding their labels cannot be assumed to multiply success probabilities. Explicitly identify if any observation is missing, provisional, contradictory or retrospective.

**Source visual caution.** The example chart contains **Gold Spot/U.S. Dollar** with a forex feed, not a gold-token or crypto perpetual. Its prices and zones cannot be transposed to another instrument.

## Lesson 08 (p10): The primary trend-location-confirmation entry workflow

**COACH_EXPLICIT ordered procedure:**

1. Start on the HTF (e.g., 1H or 4H). Identify direction from highs/lows and important support/resistance.
2. Under an uptrend, principally watch support for a **BUY** scenario; under a downtrend, watch resistance for a **SELL** scenario. A directional bias alone does not justify entry.
3. **WAIT until price reaches the chosen zone.** Coach explicitly says that if price fails to reach it, **NO TRADE**.
4. Inspect the LTF for **one relevant confirmation alternative**: (a) bullish/bearish engulfing, often preferred; **OR** (b) long-wick rejection **plus** a follow-through candle; **OR** (c) one strong, large-body directional confirmation. "One strong confirmation is enough" must not be misread as three physical candles or three simultaneous indicator votes; the rejection+follow-through alternative inherently has more than one element.
5. **Enter only after the confirmation candle closes** under this Lesson 08 scenario. The source supplies no universal order type, slippage policy or exact entry fill price.
6. Long stop **below support**; short stop **above resistance**. Take profit at the **next S/R level OR** a fixed **1:2 or 1:3** risk/reward proposal. These are alternatives; Coach does not establish a universal precedence when the next obstacle conflicts with an exact 2R objective.

**Research refinements.** Keep HTF context, pre-known zone, eligible contact, reaction onset, reaction completion, and potential entry eligibility as **separate events**. The zone must exist *before* the claimed contact. Whether one fully completed candle may count as both touch and confirmation, or whether a different later candle is required, is a research choice. Waiting for close does not prove that an entry at that close was available or executed. A touch is not a fill. Completed reaction without a coherent stop or target is *risk incomplete*, not a verified order.

## Lesson 09 (p11): Support, resistance and role reversal

**COACH_EXPLICIT.** Support is the floor-like area where downward price movement has previously attracted an upward response; resistance is the ceiling-like area where rising price has previously met selling/rejection. Coach's shorthand is "buy at support, sell at resistance," always **with confirmation**. Broken support may become resistance and broken resistance may become support.

**PCSS.** Zones are usually **intervals**, not infinitely precise points. Their existence and validity depend on historical evidence, timeframe and rules for selecting significant prior reactions. "Buyers/sellers are here" is a market interpretation, not identification of particular participants from OHLC.

**Independent improvement.** Compare explicitly drawn manual intervals, clusters of previously *confirmed* swing prices and rolling completed-bar extrema. A first close beyond a zone can be a **candidate break**; a separately confirmed retest/rejection can be required for **role-flip qualification**, if that alternative is selected. Do not label a broken level as successfully retested before a retest happens. Define wick/body/close contact, equality, number of touches, clustering distance, active lifetime and invalidation rather than silently selecting them.

## Lesson 10 (pp12–13): Sideways Gold Spot — conditional range trading

**COACH_EXPLICIT original case.** A historical **1H Gold Spot/USD forex chart** is interpreted as sideways, with **support approximately 4,670–4,680** and **resistance approximately 4,730–4,750**. The accompanying 5m chart is near **4,710**, roughly the range middle, so Coach does not consider immediate entry attractive.

- **Conditional short:** wait for **4,730–4,750** and bearish engulfing or shooting-star rejection; Coach says entry at the **break of confirmation**, stop **4,755**, target near support **4,670–4,680**.
- **Conditional long:** wait for **4,670–4,680** and bullish engulfing or hammer; again entry at **break of confirmation**, stop **4,665**, target near resistance **4,730–4,750**.
- **No qualifying reversal candle:** the candidate is invalid/no trade; avoid chasing midrange price and assumed fakeout-proof levels.

**Critical reconciliation.** This is not a contradiction to Lesson 07's advice to avoid directionless markets: the range example is a **separate conditional style**. Nor is the "break of confirmation" clause identical to Lesson 08's entry **after confirmation close**. Research comparisons can distinguish a later wick break of the confirmation high/low from a later completed-close break, but Coach does not uniquely choose one. No real fill, source snapshot time or realized P&L was established. Those historical dollar prices are not levels for a gold-related crypto market.

## Lesson 11 (p14): Order block and BOS/CHoCH distinction

**COACH_EXPLICIT.** An **order block (OB)** is described as the **last candle before a strong pump or drop**, with the suggestion that larger market participants caused the move and that price may react if it revisits the area. The source does not define a numerical displacement, candle-color requirement, zone bounds, retest expiry or observable proof of institutional orders. **BOS** indicates trend **continuation**, whereas **CHoCH** indicates a **possible** character change/reversal. Coach emphasizes finding actual structure before casually annotating a BOS.

**Important source-figure correction.** The original page-14 bullish OB panel labels a **green** candle 1 near a swing low before rising candles 2–3; the bearish panel labels a **red** candle 1 near a swing high before a decline. Both show a shaded zone and **"1→3 GAP"**. It is therefore inaccurate to claim that Coach universally requires a **last opposite-colored candle** for every OB. The 1-to-3 graphic lends source support to a three-candle gap *idea* but still does **not** define a mandatory precise FVG inequality or require all order blocks to contain such a gap.

**Independent alternatives.** Source/manual OB annotation; any-color last predecessor before qualified displacement; last-opposite-color predecessor as a common but *non-source-certified* convention. These produce different outputs and must be compared rather than silently blended. A retrospective candle only becomes a *known confirmed OB candidate* after the qualifying subsequent move is observed. Neither an OB nor a plotted FVG proves actual order-book liquidity or institutional identity.

## Lesson 12 (pp15–16): BOS (Break of Structure)

**COACH_EXPLICIT.** First determine the established direction: uptrend = HH and HL, downtrend = LH and LL. A **bullish BOS** is continuation when price breaks a previous significant **higher high** in an uptrend; a **bearish BOS** is continuation when it breaks a previous significant **lower low** in a downtrend. The diagrams show repeated structural continuation; one also contains a contrasting CHoCH visual, not proof that every BOS mandates an OB/FVG.

**Research improvement.** "Previous HH/LL" is a *structural reference*, not merely whichever maximum/minimum appears in an arbitrary rolling window. Define eligible swings, their observation and later confirmation times, structural regime, reference identity, wick versus close crossing, ties/buffers, and whether each level can trigger only once. If structure is unknown, a price crossing a rolling high is a **generic breakout candidate**, not automatically Coach-type BOS. A later-confirmed swing must not backdate a break label to an earlier cutoff.

## Lesson 13 (pp17–18): Manage your risk — SOL example

**COACH_EXPLICIT core situation.** Coach describes SOL with 4H **bullish** HH/HL, no bearish 4H BOS, and a **pullback**. The 1H is described as bullish but weakening, with possible CHoCH and supply/rejection evidence. The 15m shows weakening momentum and lower highs. This permits discussing a **countertrend SHORT scalp**, while separately proposing a **HTF-aligned LONG only after further confirmation**.

**Coach's short plan (proposed/historical commentary, not a verified fill):**

| Component | Source-stated level or condition |
|---|---|
| Short area | 86.4–86.7, near supply/OB/FVG |
| 1H bearish FVG | 86.4–86.8 |
| 15m bearish OB | 86.5–86.7 |
| Stop | 87.2 |
| TP1 | 85.8 |
| TP2 | 85.3 |
| TP3 | 84.8, if the full pullback develops |
| Higher context | 4H remains bullish; 4H demand near 85.2–85.5; 1H demand ~85.6–85.8 |
| Style | Countertrend pullback short, scalp/intraday horizon |

**Gross 1R geometry with fixed source stop/targets varies by where the short actually enters:** at entry 86.4, stop distance 0.8 and rewards 0.6, 1.1, 1.6 => **0.75R**, **1.375R**, **2R**. At entry 86.7, stop distance 0.5 and rewards 0.9, 1.4, 1.9 => **1.8R**, **2.8R**, **3.8R**. These are endpoint comparisons, not realized trade returns. Any lower target below stated HTF demand requires additional contextual scrutiny; source does not establish a specific fill.

**Coach's separate long scenario.** Wait at demand **85.2–85.6**, then look for **15m bullish CHoCH and strong bullish displacement/large green candle**. Long only after confirmation, stop **strictly below 84.9**, objectives around **86.5** and **87+**. The stop is an **inequality**, not a defined exact price; exact R:R is therefore not determined.

**Critical lesson.** A 15m bearish structural or momentum shift can coexist with a bullish 4H structure. A countertrend scalp may be source-described without endorsing an automatic short or declaring the macro trend bearish. The two scenarios need different time horizons, invalidations, and status; neither is a verified financial result.

## Lesson 14 (p19): Fibonacci retracement

**COACH_EXPLICIT.** Use Fibonacci on a meaningful swing. For a rising trend, connect **swing low → swing high** and watch a retracement. For a falling trend, **swing high → swing low** and watch a rebound. Levels listed include **0.236, 0.382, 0.5, 0.618, 0.786**. The lesson first emphasizes a **0.50–0.618 "Golden Zone"**, then separately tells the student to add **0.705** and look at **0.618–0.705**, still waiting for confirmation. Suggested stops are beyond the **0.786** retracement boundary in the respective direction, but exact anchors/buffers/prices are not supplied.

**Independent coordinate derivation.** With swing low \(L\), high \(H\), \(D=H-L>0\): upward-trend retracement price at ratio \(r\) is \(P_\uparrow(r)=H-rD\); downward-trend rebound is \(P_\downarrow(r)=L+rD\). Thus the uptrend 0.5–0.618 band is \([H-0.618D,H-0.5D]\), and 0.618–0.705 is \([H-0.705D,H-0.618D]\); the downtrend bands mirror upward from the swing low.

**Source preservation:** the two Coach entry windows **share** the 0.618 boundary but should **not** be casually rewritten as one uniform prescribed 0.50–0.705 region. The source does not establish priority between them. Research must define swing selection, when both anchors were confirmed and frozen, interval equality, retracement overlap, competing zones and stop feasibility. A perfect historical low/high identified only later is not an earlier tradable anchor.

## Lesson 15 (p20): Reliability and confluence

**COACH_EXPLICIT components:** (1) market structure plus support/resistance, (2) EMA trend, (3) RSI momentum, (4) FVG/OB/liquidity, (5) confirmation candles. RSI above **50** commonly reflects bullish momentum, below **50** bearish momentum, but Coach explicitly says RSI alone is insufficient and price structure and S/R remain important. He describes the combination as more "reliable" in ordinary-language terms, without empirical statistics.

**Independent caution.** Structure, moving averages, RSI and candles are often derived from the *same price observations*. They are neither independent witnesses nor calibrated probability votes. A market's RSI above 50 does not guarantee the next candle rises, an FVG does not identify real hidden orders, and more checkboxes may overfit or delay entries. Compare a simple structure+location+reaction baseline with additions, using actual incremental evidence and realistic costs. Retain alternative/conditional observations if source examples support them.

## Lesson 16 (p21): Long and short continuation examples

**COACH_EXPLICIT LONG example:** HTF bullish structure; price above an EMA; RSI above 50. On LTF, price retraces toward **EMA/FVG**; RSI **bounces above 50**; bullish **rejection candle** appears. Result: conceptual continuation-long opportunity after appropriate context.

**COACH_EXPLICIT SHORT example:** HTF bearish structure; price below EMA; RSI below 50. LTF retraces to **EMA resistance**; RSI **rejects below 50**; bearish **confirmation candle** appears. These are deliberately not word-for-word mirror images: the SHORT example does **not** explicitly name FVG in its LTF line, and the LONG mentions a *bullish rejection* while the SHORT permits a generic *bearish confirmation*.

**Important open questions.** The slash "EMA/FVG" is not formal AND/OR syntax. "RSI bounce" may mean a retest, cross, resumption or bounded reversal and is not quantified. No mandatory EMA period is given on this page. Coach's two examples should not become a universal rigid six-predicate filter without source justification and evaluation. The 40–50 scalp RSI behavior in Q&A2 is a *separate context*, not an error to erase.

## Lesson 17 (p22): RSI — Relative Strength Index

**COACH_EXPLICIT.** RSI estimates momentum/relative strength of recent price changes, often using **period 14**. Common interpretive reference levels: **70** overbought, **30** oversold, **50** momentum midline. Above 50 suggests more bullish recent momentum; below 50 more bearish. Above 70 does **not** automatically mean sell; below 30 does **not** automatically mean buy. Strong trends can remain high/low for extended periods. Use RSI to corroborate market structure, location and price action—not as an isolated trading command. RSI divergence is not developed as a rule in this source lesson.

**Mathematical supplement.** In the common Wilder form, \(RS=\overline G/\overline L\), \(RSI=100-100/(1+RS)\), with smoothed positive gains \(\overline G\) and losses \(\overline L\) and explicitly defined initialization. Edge cases (no loss, no gain, insufficient warmup) require numeric policies. This formula is **an independent mathematical explanation**, not a verbatim Coach derivation or proof of order-flow buying/selling pressure.

**Open.** Equality exactly at 30/50/70, unconfirmed latest bar, RSI lookback/seed, the meaning of "bounce" (especially 40–50), source-price choice, multi-timeframe conflicts, divergence and whether a threshold adds evidence after structural context.

## Lesson 18 (p23): Exponential moving average (EMA)

**COACH_EXPLICIT.** EMAs are used for trend context, dynamic support/resistance, momentum continuation and market bias. Common periods: **EMA20** short-term, **EMA50** intermediate, **EMA200** macro/overall trend. Price above an EMA is characterized as bullish relative to that average, below as bearish; price may pull back to an EMA as dynamic support or rebound toward it as resistance. Upward slope suggests bullish momentum, downward bearish, flat suggests range/weak momentum. Frequent crosses in sideways conditions can create misleading signals.

**Independent mathematics.** For a close-based EMA of period \(n>1\), \(\alpha=2/(n+1)\) and \(E_t=\alpha C_t+(1-\alpha)E_{t-1}\). Therefore \(E_t-E_{t-1}=\alpha(C_t-E_{t-1})\) and \(C_t-E_t=(1-\alpha)(C_t-E_{t-1})\). For the **same close**, same EMA series and a **one-bar** slope, the signs are identical: \(C_t>E_t\) if and only if \(E_t>E_{t-1}\). Treating "price above EMA" and "EMA rising from the immediately previous bar" as **two independent positive votes** is algebraic double counting. This result does not automatically extend to a k-bar slope, different price sources or different timeframes.

**Further improvement.** Do not infer numeric momentum from the EMA's *displayed pixel angle*: zoom and scale alter the visual angle without changing data. Compare explicitly measured one-/multi-bar slope, percent or volatility-adjusted change as different hypotheses. Multiple EMA lengths are correlated. A demonstration showing an initial EMA setting of 9 is **not** a universal Coach EMA9 rule; the stock note later instructs 20/50/200.

## Lesson 19 (p24): RSI + EMA top-down analysis

**COACH_EXPLICIT workflow:**

1. **HTF bias:** start from a suitable **4H, Daily or 1H** source. Read structure, EMA direction and RSI momentum. A bullish illustrative combination is price above **EMA50**, EMA sloping upward and RSI above 50.
2. **Wait for a pullback:** avoid chasing the impulsive leg. Watch an EMA retest, FVG revisit or important support/resistance area.
3. **LTF confirmation:** on **15m/5m**, inspect rejection candles, possible BOS/CHoCH, RSI retaining momentum and EMA support/resistance responses. The source does not settle whether BOS/CHoCH are alternatives, prerequisites or sequential events for every style.

The lesson repeats the long/short continuation case descriptions from Lesson 16. The specific EMA50 in *one HTF illustration* should not be silently applied to every indicator or every market. RSI and EMA readings remain contextual; they cannot substitute for separate observation of HH/HL or LH/LL.

**Independent contribution.** Store *which* timeframe, exact completed candle, price basis and indicator parameters supplied every claim. Do not let a later HTF close retroactively validate an earlier 5m rejection. A confluence tally must account for EMA redundancy, all price-derived indicators, conflicting regimes, and missing observations.

## Lesson 20 (p25): CHoCH — Change of Character

**COACH_EXPLICIT.** A **bullish CHoCH** may occur when an established downtrend **breaks a previous lower high (LH)**; a **bearish CHoCH** may occur when an established uptrend **breaks a previous higher low (HL)**. The source calls this a **possible reversal** or shift, not confirmation that a complete new HH/HL or LH/LL trend already exists. The original sketches show continuation BOS sequences separated by a contrary structural break and possible transition.

**Independent specification.** Preserve source trend, eligible previous swing level and the **first causal crossing**. A new CHoCH is a *warning/possible-shift event*; only independent later opposite-direction swing evidence can establish a full opposite regime under a selected model. A CHoCH on 5m/15m does not by itself flip 1H/4H. No source-mandated wick/close threshold, buffer, follow-through count or win rate is available.

## Lesson 21 (pp26–28): Multi-timeframe TON setup

**Original figure observations versus written description.** The actual two screenshots are **TON/TetherUS 4H**, with source price around **2.731–2.736** and RSI14 approximately **97.45–97.46**, along with 20/50/100/200 EMA indicators or Fibonacci view. The source separately **asserts** 1H and 15m analysis, but does not provide corresponding verified 1H and 15m screenshots. A phrase resembling "fart sir" is ambiguous. The analysis therefore cannot claim that every timeframe, zone or asset reference was independently image-verified.

**COACH_EXPLICIT 4H/1H reading.** Strong bullish 4H HH/HL and no major bearish break, price above 20/50/100/200; RSI very high, indicating strong recent buying momentum but also **risk of chasing and a potential pullback**. Written 1H narrative describes continuation/consolidation, bullish BOS beyond **2.48** and **2.60**, progression toward **2.73+**, no confirmed bearish CHoCH, RSI around **79**, and EMA20 support around **2.40–2.45** (EMA50 around **2.14**). These 1H values are **Coach text**, not screenshot-confirmed OHLC evidence.

**Coach-stated levels / possible areas:**

| Type | Original TON source levels / interpretation |
|---|---|
| FVG | 2.58–2.62; 2.48–2.52; 2.38–2.44 |
| Bullish OB | 2.45–2.50 |
| Nearby support | ~2.65; 2.58–2.62; 2.45–2.50 OB/Fib; stronger 2.38–2.40 |
| Resistance/objectives | 2.75, 2.80, and major psychological 3.00 |
| Conditional pullback-entry zone | 2.58–2.62, **after** bullish engulfing or strong rejection confirmation |
| Proposed stop | **strictly below 2.52** (no exact stop price) |
| Profit and management | 2.75 toward 3.00; trailing-stop language without exact algorithm |

The strength of a 4H uptrend does **not** justify chasing a high-RSI price at market. Use *conditional location and confirmation*, and distinguish written source levels from independently computed FVG/OB/Fibonacci features. Because stop and actual entry are not uniquely fixed, no exact realized risk multiple or outcome follows.

---
# 6. Coach's complete Q&A activities

## Q&A 01 (pp29–30): BTC bullish HTF with conditional continuation

**Source evidence.** Two mobile chart screenshots show **BTCUSD 4H** and **15m**. Observed screenshot prices are roughly **82,446** on 4H and **82,427** on 15m, with EMA20/50/100/200 and RSI14; 4H RSI is approximately **69.91**, 15m approximately **63.10**. The student identifies upward market structure, EMA support and potential continuation and says they are waiting for a **retest and good confirmation candle** before entry. Coach approves the broad interpretation and says continuation is more likely in this example **unless strong bearish confirmation develops**.

**PCSS source discrimination.** The student's written "ema2" appears to be an abbreviated/incorrect description of a visible EMA20, not evidence of an EMA2 strategy. A student-claimed BOS lacks a marked, time-qualified structural anchor in the screenshots and should not be promoted to independently verified BOS. RSI **69.91 is below the strict >70 overbought threshold**; "near 70" and ">70" are different claims. The teaching reinforces conditionality, waiting for useful location and allowing disconfirmation rather than certainty.

**Research gaps.** Screenshot venue/product basis, actual bar identity and order history, the retest zone, the strength of bearish disconfirmation, swing qualification, oscillator warmup and exact entry/stop/target remain unspecified. A fixed bullish label should not persist after legitimately observed disconfirming evidence.

## Q&A 02 (p31): FARTCOIN scalp and separate Coach alternative

**Student's already-existing reported position.** The student says they are LONG FARTCOIN, justified by a 1H support reaction (two red rejection candles and then a solid green candle), entry **0.2436**, stop **0.2385**, scalp horizon, and a question about take profit. The original exchange includes **no chart** and no actual exchange receipt. An engulfing classification cannot be proven from these words alone.

**Coach's separate, preferred conditional pullback setup.** He would wait for **0.238–0.240**, a bullish engulfing **or** rejection-wick response, a contextual **RSI bounce around 40–50**, and price above **EMA50**. He proposes stop **strictly below 0.231**, targets **0.258–0.279**, trailing management, **30m OB** as main location and **5m confirmation**. He emphasizes **patience: let price reach the chosen entry region** rather than chasing it. His remarks that the student's placement is "below support and liquidity" have an ambiguous referent in the absence of a chart.

**PCSS non-equivalence.** The student's real-or-reported existing position and Coach's proposed *new* pullback are not the same trade. The exact 30m OB candle, a 5m reaction timestamp, the meaning of RSI "bounce" and which timeframe must be above EMA50 are unknown. A Lesson 16 example says RSI **bounces above 50**; this Q&A refers to **40–50**. Both must survive as source-specific possibilities until a contextual hypothesis is tested. A strict >50 requirement would wrongly suppress an otherwise source-described 40–50 scalp setup.

**Exact independent math.** Student stop distance \(0.2436-0.2385=0.0051\) price units, about **2.0936% of entry**. This is **not account-equity risk**. Coach's alternative **does not have a unique R:R** because he specifies an entry interval and an *open inequality* for the stop. Under a separately declared illustrative stop 0.2300 (not chosen by Coach), possible gross R multiples range from **1.8R** to **5.125R** over specified entry/target endpoints. No actual trading return or relative probability follows from these calculations.

## Q&A 03 (p32): BTC bearish context, consolidating LTF, conditional short *or* later long

**Images and student's proposal.** The source uses **Bitstamp BTCUSD** 4H/1H/15m screenshots: a recent bearish decline with 15m consolidation, prices around **79,242–79,276** at the captured views. The student proposes **SHORT entry 79,419**, stop **79,918**, TP **78,423** and calls it **1:2**. Independent signed arithmetic gives risk **499**, reward **996**, gross **996/499 ≈ 1.99599R**, supporting his *rounded* claim. The claimed "evening star" and trendline are not independently marked so their strict validity is unverified.

**Coach response.** He accepts the **higher-timeframe bearish bias**, but notices **15m consolidation**, cautions not to chase and favors waiting for BOS/CHoCH, a useful retest or rejection. One **conditional short** is near **79,850** with a **15m rejection wick OR bearish engulfing OR failed breakout above ~79.8k**; his example stop is around **80,250**, target near **79,000 or lower**, with possible trailing. A distinct **conditional long breakout** may become relevant after **BOS on 15m**, **BOS on 1H**, **or a 1H candle close above roughly 79,850–80,000**. Preserve **all three** Coach alternatives; do not silently collapse them to only one 1H close threshold.

**Research synthesis.** A short rejection and a later breakout long are not necessarily contradictory because they are *different conditional paths* with different evidence and times. A 15m bullish change does not automatically make 4H bullish. A bearish HTF is not enough to short in the middle of unresolved LTF consolidation. Coach's numeric levels are approximate and not independent actual orders. Any priority, mutual exclusion, expiry, invalidation or transition between the branches is an **independent** research decision.

# 7. Final original notes

## N-01 (p33): Location/time, sessions and economic news

**COACH_EXPLICIT, expressly for forex majors and gold.** Coach favors **Tuesday–Thursday**, with Monday sometimes slower/ranging after reopening and Friday posing profit-taking or sudden move concerns. His PHT session examples are **London approximately 3 PM–12 AM**, **New York approximately 8 PM–5 AM**, and overlap **8 PM–12 AM**. He asks traders to check major scheduled events: **CPI**, **NFP**, **FOMC**, **interest-rate announcements**, and the following day's macro calendar. Examples of information resources include Forex Factory and Investing.com calendars.

**Independent qualification.** The stated session hours resemble periods when both regions are on daylight-saving time; when both are on standard time, London is more like **4 PM–1 AM PHT**, New York **9 PM–6 AM**, overlap **9 PM–1 AM**. There are several transition weeks when one market has changed clocks and the other has not. These are approximate normal sessions; holidays/venue rules can vary. **Crypto trades continuously** on most major venues, so Coach's Tue–Thu or weekday forex heuristics must not become mandatory crypto prohibitions without separate evidence. Macro-news awareness can be useful but does not prove a fixed pre/post-announcement blackout, direction or volatility edge.

**Research gap.** Effects depend on instrument, session, announcement surprise, release latency, market regime, timezone/DST and execution costs. Event schedules should be treated as versioned observations, not timeless hard-coded truths or automatically bearish/bullish news predictions.

## N-02 (pp34–35): “BSP charting” — actual plotted PSE:BPI stock

**Identity correction.** Source heading refers to "BSP charting," but charted equity is **PSE:BPI — Bank of the Philippine Islands**. The **Bangko Sentral ng Pilipinas (BSP)** is the monetary authority that sets policy rates; it is **not** the stock plotted. The lesson links Philippines equity analysis with company earnings and quarterly reports, BSP interest rates, inflation and economic growth. This is not evidence for a universal crypto fundamental filter.

**Original visual observations.** Five source screenshots include an EMA settings panel (showing an initial length of 9) and Weekly, Daily, 4H stock charts. Coach subsequently instructs EMA **20, 50 and 200**; the initial 9 is a displayed interface setting, **not** a general Coach EMA9 trading doctrine. Sample price near **₱87.75**, Weekly RSI14 about **29.04**, Daily about **31.97**, 4H about **34.63**. The distinct timeframe readings cannot be flattened into a single oscillator label.

**Coach Weekly view.** Bearish structural breakdown references around **₱110–112** and **₱98–100**, price below EMA20/50/200, RSI near/below 30; support around **₱85–86**, **₱80–82** conditional next, and major **₱75**. Resistance **₱92–94**, **₱98–100**, major **₱110**. Candidate FVG/OB bands **₱98–103** and **₱108–112**; additional FVG **₱92–97**, possibly first rebound destination. Speculation about "institutional" selling is **not verified order-flow actor identification**.

**Coach Daily view.** No confirmed bullish CHoCH/reversal yet; a break around **₱92** is a possible higher-confidence character-change prerequisite in his reading. EMA/RSI still favor a bearish interpretation despite the possibility of a short-term bounce.

**Coach 4H view.** Consolidation, weakening bearish momentum and possible accumulation/rebound; a break around **₱89.5–90** could allow a *temporary 4H bullish move*. This does **not** automatically qualify a Daily reversal through ~₱92 or overturn Weekly bearish structure.

**Independent improvements.** Source zone overlaps—resistance **₱92–94** with FVG **₱92–97**, resistance **₱98–100** with FVG/OB **₱98–103**, and **₱110** within **₱108–112**—are not independent confluence probability multipliers. A charted zone does not independently prove the FVG/OB's creation candles. The word accumulation, without participant-level data, remains conjecture. Neither BPI peso levels nor stock-session conventions are reusable instrument prices for crypto.

---

# 8. Scenario families that must stay distinct

| Scenario | Source lineage | Directional premise | Required location / trigger in principle | Important non-equivalence |
|---|---|---|---|---|
| **Trend continuation** | L04, L07–L09, L16, L19; L08 core | HTF up or down; location aligned with structural direction | Established S/R or other qualifying pullback area, LTF completed reaction and coherent risk | Bias alone never means immediate order; L08 no-zone = NO TRADE |
| **Sideways range reversal** | L10 | Explicit 1H range, usually near its boundary | Reversal candle then proposed "break of confirmation" trigger | Not a universal exception that every directionless market is tradable |
| **Countertrend scalp** | L13 SOL | HTF trend retained, weaker/interim LTF move against it | Separate short-horizon reaction at supply/resistance, style-specific risk | LTF short does not convert 4H bullish to bearish |
| **HTF-aligned post-pullback long** | L13 SOL | Bullish 4H; wait for demand | Demand + 15m bullish CHoCH + strong green displacement | Different entry region and objective from countertrend short |
| **Pullback scalp** | QA2 FARTCOIN | Existing student long separate from Coach alternative | 30m OB/pullback, 5m reaction, RSI context 40–50, EMA50 | Not the same as generic RSI>50 condition; no source chart |
| **Reversal watch** | L20, N02 | Local break against prior trend | Previous LH/HL broken under a defined reference, then independent HTF confirmation | Possible CHoCH ≠ fully changed HTF regime |
| **Conditional rejection short** | QA3 BTC | HTF bearish, 15m range | Rejection/failed breakout around specified resistance | Can fail and later transition to breakout watch |
| **Conditional breakout long** | QA3 BTC | New bullish evidence despite prior bearish context | Source alternatives: 15m BOS, 1H BOS, or 1H close above named area | Not simply a bullish RSI candle and not automatic HTF trend reversal |
| **High-momentum wait-for-retrace** | L21 TON, QA1 BTC | Existing bullish structure but poor immediate location | Pullback to genuine prior area, completed bullish evidence | Extremely high RSI is not automatic short or long; WAIT is legitimate |
| **Higher-timeframe bearish / local bounce** | N02 BPI | Weekly/Daily bearish, 4H recovery possible | Maintain timeframe-specific context and conditional levels | 4H bounce ≠ Daily/Weekly reversal |

**Cross-scenario policy (independent):** the system may recognize multiple *conditional scenario descriptions*, but should not silently issue opposed unconditional orders at the same time. When incompatible scenarios would be actionable under different premises, explicitly report **CONDITIONAL_CONFLICT**, identify conditions for each, and withhold a common action decision. If a style is unselected, describe the market while reporting **UNSELECTED_STYLE** for hypothetical trade eligibility.

---
# 9. Independent research architecture: the M00–M07 methodology map

The Coach lessons are a **discretionary framework**: identify the market context, structural direction and meaningful location, wait for a reaction, and define risk before taking a position. The repository's research effort decomposes this into independently auditable questions. These modules are *conceptual research categories*, not requirements stated by Coach, not claims that a unique procedure has been selected, and not a software blueprint.

| Research domain | Question to settle | Coach anchor | Key unresolved elements |
|---|---|---|---|
| **M00 — market and evidence identity** | What exact price series, product and observation is being interpreted, and when was it available? | All sourced chart examples; L01/L04 | instrument and venue equivalence, continuous clock, data revisions, missingness |
| **M01 — structural price action** | Which swings establish UP/DOWN/RANGE, and what constitutes a genuinely new BOS or possible CHoCH? | L07, L11, L12, L20; N02 | pivot choice, degree, ties, regime evidence, previous protected references, arming |
| **M02 — price zones** | What constitutes S/R, a flipped level, a credible OB/FVG, and a Fibonacci retracement area? | L09–L11, L14, L21 | intervals and clustering, displacement/gap criteria, mitigation, lifetime, overlap |
| **M03 — momentum and smoothed trend** | What distinct information do RSI, EMA and other context add? | L15–L19; QAs | settings, slope horizon, RSI bounce, dependence, conflicting signals |
| **M04 — candle reaction** | Which observable completed-candle shapes count as rejection, engulfing, follow-through or strong confirmation? | L02, L06, L08; L10 | wick/body geometry, size ratios, strictness, follow-through and age |
| **M05 — conditional setups and timeframe context** | Which scenario is under consideration? What prior facts authorize waiting, disqualification, or a new *candidate*? | L04, L07–L08, L10, L13, L16, L19; QAs | HTF/LTF causal timing, scenario profiles, conflicts, lifetimes |
| **M06 — loss, payoff and trade feasibility** | Is a proposed entry/stop/target geometrically coherent, sizeable, and realistic after costs and uncertainty? | L03, L05, L08, L10, L13, L21; QAs | account-risk budget, fill, partials, funding, liquidation, exit path |
| **M07 — evidence and falsification** | Does a chosen precise interpretation match documented Coach examples, remain causal, and show useful incremental information? | Entire 35-page corpus | independent annotations, matched data, negative cases, out-of-sample economics |

**Dependency logic.** A price-level crossing cannot be called a *structural BOS* until M00 identifies valid observations and M01 identifies the prior regime and eligible swing. A zone reaction is not a source-style entry until M02's prior location, M04's confirmation and M05's timing agree. M06's risk analysis can then be meaningful without claiming an actual trade. M07 evaluates each claim independently. Where an upstream premise is absent, a later attractive candle is not permission to invent that premise.

**Source-fidelity versus improved method.** A simple human-marked zone plus a closed bullish confirmation may be closer to an original source example than a sophisticated quantitative zone model. Conversely a carefully specified algorithm might be more reproducible and less hindsight-prone while disagreeing with some discretionary Coach annotations. These are different objectives; neither is sufficient evidence of higher after-cost performance.

## M00 in detail — what counts as a usable observation?

A research claim about price action must identify at least: exact product, venue, traded instrument, quote and settlement units, price basis (e.g., transaction-price versus alternative risk reference), timeframe, bar open and close boundaries, OHLC values, finality, first knowable time and provenance. Quote precision, minimum tick, interval continuity and any known exchange closure also matter. These safeguards are **independent additions** motivated by the Coach PDF's mixing of instruments and markets.

**Valid ordinary OHLC geometry**, with positive finite prices, satisfies

\[
L_t\le\min(O_t,C_t)\le\max(O_t,C_t)\le H_t.
\]

A candle with \(O_t=H_t=L_t=C_t\) can be a *valid flat candle*. That is not the same as a corrupt bar with \(H_t<\max(O_t,C_t)\), a missing bar, a duplicate interval with conflicting values or an unfinished candle. Replacing missing intervals with invented flat candles corrupts swing, EMA, RSI, three-candle FVG and reaction interpretation.

**Observation clocks must be separate.** A source bar has its own trading interval; a provider may only confirm or deliver it later. A human can only make a claim at the point when its required evidence is available. Corrections and later revisions may change a *new* assessment but cannot retroactively establish what an earlier decision-maker actually knew. Record both the original as-issued assessment and a later revised one, if needed.

**Markets are not interchangeable.** Coach uses gold spot, several crypto pairs, and PSE:BPI equity in the same pedagogy. Their levels, candles, funding mechanisms, sessions and execution assumptions differ. The later project-specific research narrowed future instruments to **positively qualified Binance USDⓈ-M USD-stablecoin-quoted and -settled perpetual contracts**, potentially including gold-reference XAUUSDT once its exact product is verified. This is an **owner research-scope decision dated November 14, 2026**, not an original Coach rule, and does not erase the pedagogical forex/equity cases. A contract's eligibility must be positively demonstrated; ticker resemblance alone is not a contract-specification proof.

# 10. Structural pivots, swing references, BOS and CHoCH: R1 research and corrections

## 10.1 Coach foundation and the central ambiguity

**COACH_EXPLICIT:** a bullish structural sequence has **higher highs and higher lows**; bearish structure has **lower highs and lower lows**. The relevant previous structural high or low is a prerequisite for interpreting a **BOS**, which is a continuation break. A break over the previous LH of an established downtrend or below the prior HL of an established uptrend may be a **CHoCH**, a **possible** reversal warning. Neither a free-standing crossing of a rolling high nor a single wick through a line is Coach's uniquely specified BOS rule. The source does not specify pivot windows, a unique swing scale, an exact break buffer, strict close/wick priority or how to treat equal values.

**Independent baseline — strict local extrema.** A proposed high pivot at index \(i\) with selected left and right spans \(\ell,r\ge1\) qualifies when its high is strictly greater than the \(\ell\) left highs and \(r\) right highs; low pivots mirror this using strict less-than. This choice has an inevitable discovery delay: a pivot visually located at index \(i\) only becomes knowable *after its required right-hand bars are final and available*. No numeric spans came from Coach. Equality-tolerant alternatives or volatility-based directional-change swings are plausible competitors; no single method is source-certified.

**Structural sequence proposed for comparison:** preserve ordered alternating high and low pivots; compare last two qualified highs and lows. An UP hypothesis requires the latest high greater than its predecessor **and** the latest low greater than its predecessor; DOWN requires both strictly lower. A complete sequence that fails both is **MIXED**, while too few observations or a disrupted ordering is **UNKNOWN/INSUFFICIENT**, not automatically RANGE. A range requires its own evidence of contained oscillation and boundaries, not simply absence of trend proof.

## 10.2 A confirmed pivot, a qualified structure and an armed break are not simultaneous

For each reference distinguish:

1. **Pivot origin** — bar whose extreme visually defines the candidate level.
2. **Pivot confirmation time** — right-hand evidence becomes final and available.
3. **Regime known time** — enough ordered swings establish the relevant UP/DOWN context.
4. **Reference armed time** — pivot and appropriate structural context both qualify for a *new* crossing.
5. **Break observed time** — earliest admissible fresh crossing, if any.
6. **Assessment/publication time** — when that classification is actually issued, which may be later than the nominal interval boundary.

A conservative hypothesis demands

\[
t_{\rm arm}\ \ge\ \max(t_{\rm pivot\ known},\ t_{\rm regime\ known}).
\]

This is a causality requirement, not a new Coach sentence. A past candle may be *annotated* as a structural origin later, but a trader could not have acted on its later-confirmed classification at the origin.

### Critical correction from the independent audit

An earlier constructed audit supposed a high pivot at **106** could be validly confirmed by a strict right-hand-fractal test even though one required right bar **closed at 107**. That case is impossible: the right bar's high must be at least its close, and thus is at least 107, greater than 106. A strict pivot high of 106 is therefore **rejected**, not confirmed late. The corrected research separates two entirely different phenomena:

- **Invalid candidate:** a required right high disqualifies the purported pivot.
- **Valid pivot but late structural eligibility:** pivot at 106 was validly confirmed at 10:00, price closes 107 at 10:05, but required UP-context only becomes knowable at 10:10. The earlier 107 move is **pre-arming price history**, not a new 10:10 BOS. It must not be backdated or silently revived.

This correction matters because it prevents a mathematically impossible example from being used to justify a real rule. It is **proven under the stated strict-fractal hypothesis**, not an observation of Coach's market.

## 10.3 R1 reference-breaking competitors

**R1-A — frozen-reference, latest-prior-close research baseline.** Given an identified structural reference and regime, arm only after both are known. At arming, inspect the most recent eligible completed close. If it is already beyond the selected threshold, that reference is blocked in this strict baseline. If not, require a fresh subsequent completed close crossing the frozen reference from the non-broken side. Count a qualifying event **once**; consume that reference, and require a new eligible reference for another event. A missing preceding close means eligibility is unknown, rather than a convenient fresh event.

**R1-B — distinct reset and re-cross.** A pre-breached reference can become eligible *again* if a later fully closed price first returns to its original safe side and another **separate subsequent** closed bar crosses out. This increases coverage but risks recycling an obsolete structural anchor. The initial pre-breach remains historical, never renamed a newly discovered BOS.

**R1-C — human-selected structural reference.** An analyst supplies a specific swing, prior role, regime and **genuine** known-at time. This honors source discretion better in some cases, but is susceptible to hindsight if the label was authored from a later complete chart; mark it retrospective when that is true.

**History-window veto comparator.** A stricter challenger blocks a proposed reference if *any* beyond-threshold close occurred in a declared pre-arming history window, even if the latest at-arming close returned inside. This is distinct from R1-A's latest-close test, and can reject a later legitimate fresh crossing. Require complete history to apply the veto; an incomplete history is not evidence of “no prior breach.”

A useful divergence case is high **106**, confirmed at 10:00, with closes **107**, then **105** both known by arming at 10:10, followed by a later close **108**. Latest-close R1-A can admit the fresh 105→108 crossing under its chosen arming semantics, whereas the full-history veto can reject it because 107 existed before arming. Neither preference has demonstrated higher trading expectancy. Preserve the competing event counts and reasons instead of silently choosing whichever looks best retrospectively.

### Proposed closed-break rule

For a pre-known high reference \(h\) and chosen independent buffer \(\varepsilon\ge0\), an UP break may require a prior eligible completed close not above \(h+\varepsilon\) and a **new final close strictly above \(h+\varepsilon\)** after arming. A DOWN break mirrors this below \(\ell-\varepsilon\). A wick-only excursion, close equality and gap-through are different classifications. No source-stated universal buffer exists.

**BOS versus CHoCH.** With established UP and eligible previous HH, a qualifying upward break is **continuation BOS**; an eligible downward break of a protected HL is a **possible bearish CHoCH**. With established DOWN, a new break below a prior LL is **continuation BOS**, while above a protected LH is **possible bullish CHoCH**. This classification requires an objectively chosen protected/reference swing degree. A CHoCH cannot, merely by existing, establish two new ordered opposite-direction swing pairs and an independently confirmed regime. Keep `POSSIBLE_SHIFT` until genuinely sufficient additional structure exists.

## 10.4 Pivots that resist an easy narrative

- **Tied extremes:** under strict-fractal rules, equal highs or lows disqualify the corresponding side; a one-tick tolerance variant would be a different hypothesis.
- **Outside candle:** the same bar can be a local maximum and minimum. OHLC does not tell which extreme formed first. It cannot safely become two time-ordered swing legs without finer genuinely ordered evidence.
- **Consecutive same-side pivots:** restart/quarantine an ambiguous run as a simple baseline, or compare a more-extreme provisional replacement. Neither should rewrite an already consumed reference's old event.
- **Missing or discontinuous windows:** an absent candle cannot be replaced with the next available row when a pivot requires *adjacent time periods*.
- **No prior trend:** a rolling 20-bar breakout with no completed HH/HL or LH/LL reference is an *unclassified level crossing*, not automatically Coach BOS.
- **Break against trend:** a bearish break during bullish macro structure may be an LTF CHoCH; it is not a higher-timeframe bearish regime until that timeframe independently qualifies.
- **Revised evidence:** a late price-bar correction can justify a new revised assessment, not erasure of the earlier recorded as-of decision.

## 10.5 Market-structure research candidates beyond fixed fractals

| Candidate | Definition and advantage | Failure mode and requirement |
|---|---|---|
| **Manual swing reference** | Source-oriented analyst records role, level, scale and time | Subjective selection, hindsight and reviewer disagreement |
| **Strict symmetric fractals** | Local extrema with explicit left/right windows and delayed confirmation | Equal ties, parameter sensitivity, frequent small pivots, delayed availability |
| **Directional-change / deviation swing** | Alternation after a chosen price or volatility reversal magnitude | Requires selected deviation, evolving extreme and freeze policy |
| **Same-side extreme retention** | Compress sequential highs or lows to the most pronounced candidate | Can alter apparent degree/sequence; must not retroactively alter events |
| **Rolling past-window extrema** | Simple causal high/low boundary comparator | Not necessarily a structural swing or source-like BOS |
| **Human-adjudicated predeclared references** | Allow a conservative manual gold standard and abstention | Requires actual prospective evidence and independent reviewers |

The current research preference is conservative causal **reference consumption plus explicit uncertainty**, compared against simpler or more permissive alternatives. Parameter values and market-value claims remain unselected.

---
# 11. Zones, OB, FVG, Fibonacci and contact chronology: M02/R2

## 11.1 The common idea — location, not prediction

**COACH_EXPLICIT:** support is a location where downward price movement previously met buying/reaction; resistance is where upward movement previously met selling/reaction. A broken support can later serve as resistance, and a broken resistance as support. Some pullbacks revisit **order blocks (OB)**, **fair value gaps (FVG)**, **EMA levels**, or **Fibonacci retracements**. These are possible areas of interest, not orders that must be placed automatically. In Lesson 08, *absence of a visit to a selected zone means NO TRADE for that workflow*. In Lesson 10 the range middle is unattractive and the edges offer conditional, not unconditional, entries.

**Independent zone definition:** an interval \(Z=[a,b]\), \(a\le b\), with identified instrument, quote unit, price basis, zone type, provenance, source candles/swing, first known-at time, eligibility side, lifecycle, invalidation criterion, and whether its boundaries are manual annotations or reproducible calculations. This is more reliable than pretending a rectangle is a mathematically unique object.

## 11.2 Support and resistance: alternative ways to recognize a *previously knowable* zone

- **Manual/source S/R:** a human marks a region supported by earlier highs/lows or repeated reactions. This is closest to Coach's examples but contains subjective choices. Mark whether the region was selected before or after the illustrated bounce.
- **Confirmed-pivot cluster S/R:** group *already known* swing lows into candidate support and highs into candidate resistance within a declared price tolerance \(\delta\), lookback and minimum count. Bound the zone using contributing extremes with optional documented padding. Do not combine adjacent clusters by a transitive chain that allows the final cluster's full diameter to exceed the chosen tolerance unnoticed.
- **Prior completed-window extrema:** define levels from the highest high and lowest low of the preceding \(N\) eligible observations. This is simple and reproducible but is not guaranteed to match Coach's structurally meaningful levels.
- **Reaction-density approach:** use prior tested rejections/touches as additional evidence, while accounting for the fact that the same underlying candle may be reused in structural and zone calculations. The minimum touch count and tolerance are not in the source.

**Potential role-flip sequences:** (RF1) classify a candidate break at first qualified closed price outside the known region; (RF2) wait for an **opposite-side retest and rejection** before confirming a flip; or (RF3) admit a wick crossing but require subsequent closing acceptance. The source states the *possibility* of role reversal, not that a break itself proves the later successful retest. A flip has a prior role and a new role; that historical identity must be preserved.

## 11.3 Order blocks: source figure versus market convention

**Coach's definition (p14):** an OB is the last candle before a strong price pump/drop, interpreted as a possible place where a substantial participant entered and to which price may react on return. The term *large money* is an intuitive narrative; ordinary OHLC alone cannot authenticate an institution or its filled orders.

**Critical PCSS visual observation:** the original bullish illustration identifies a **green** candle 1 near a swing low, followed by rising candles 2 and 3; the bearish illustration identifies a **red** candle 1 near a swing high, followed by descending candles 2 and 3. Both include a **“1→3 GAP”** and shaded zones. It would contradict the actual figures to assert that Coach **always** labels the last **opposite-colored** candle an OB. His prose also lacks a minimum displacement magnitude, exact OB body-versus-wick boundary and universal FVG prerequisite.

| Candidate | Independent operational hypothesis | Relation to source |
|---|---|---|
| **OB0** | Human/source-identified final candle before an evident completed move, zone by declared body/range | Descriptive source comparator, not objective order-flow proof |
| **OB1** | Last **opposite-colored** candle before selected completed displacement, within a finite backward search | Common external convention; does not reproduce both original figure colors universally |
| **OB2** | Immediate **preceding candle regardless of color** before confirmed displacement | Closer to literal prose and figure-color flexibility; still needs objective displacement threshold |
| **OB3** | OB plus structural break, minimum body/ATR movement, or gap requirement | More selective independent hypothesis, not stated as universally mandatory by Coach |

No candidate OB becomes *known* at its origin simply because future bars later demonstrate displacement. The first admissible OB-known time follows completion of all evidence required by that chosen hypothesis. Distinguish untouched, first-touched, partially revisited, invalidated, fully filled under one definition, expired, and **unknown**. Coach supplies no fixed rule for mitigation, retest count, decay, replacement or expiry. Do not infer actual institutional order concentration from a shape label.

## 11.4 Fair value gaps (FVG): an explicit *candidate* three-candle grammar

Coach repeatedly mentions FVGs as imbalance/revisit zones in L13, L15, L16, L19, L21 and N02. The original figure's 1→3 GAP supplies qualitative support for a three-candle visual motif, **but not a uniquely specified inequality**. A defensible independent research baseline uses consecutive, valid **completed** candles \(i-2,i-1,i\):

\[
\begin{aligned}
\text{bullish FVG candidate:}&\quad L_i>H_{i-2},
&&Z=[H_{i-2},L_i],\\
\text{bearish FVG candidate:}&\quad H_i<L_{i-2},
&&Z=[H_i,L_{i-2}].
\end{aligned}
\]

The candidate exists only after candle \(i\) is final and available. Equality produces **no positive-width gap** in this strict hypothesis. A missing middle interval must be reported; a calendar/weekend jump in another market should not be silently equated with continuous-market price imbalance. A second experimental variant adds middle-candle displacement/body, minimum ticks, volatility-normalized width or accompanying structural evidence. It might exclude noise, or overfit and miss genuine source-like examples. No market-data edge is established.

**Mitigation candidates** are different: first wick touch, body overlap, midpoint visit, full far-edge traversal, or directional closing acceptance. A gap visually revisited is not proof that it was filled by a hypothetical order. FVG and OB that arise from the same three candles are *not two independent probability observations*.

## 11.5 Fibonacci: both of Coach's separate zones must survive

For a known bullish impulse swing \(L<H\), define \(D=H-L\). An **independently derived** price for downward retracement fraction \(r\) is

\[
P_{\rm up}(r)=H-rD.
\]

For a known bearish impulse from \(H\) to \(L\), the upward retracement price is

\[
P_{\rm down}(r)=L+rD.
\]

Coach initially emphasizes the **0.500–0.618** region and later adds **0.705**, looking for confirmations in **0.618–0.705**. These are two *different source-defined windows* sharing boundary 0.618, not one newly mandated continuous 0.500–0.705 area. The source levels 0.236, 0.382, 0.500, 0.618, 0.786 remain relevant; stop beyond 0.786 in the specified direction is source guidance, but buffer/quote precision/anchor method are not supplied.

For one **hypothetical** bullish impulse \(L=100,H=120\):

- **0.500–0.618 band:** \([107.64,110.00]\).
- **0.618–0.705 band:** \([105.90,107.64]\).
- A bearish impulse \(H=120,L=100\) gives corresponding upward bands \([110.00,112.36]\) and \([112.36,114.10]\).

**Late-anchor risk:** if the high is only established as a confirmed swing after price already touched the displayed retracement, the retrospectively drawn Fib is not evidence that the level was known beforehand. Compare frozen eligible swing anchors, evolving impulse anchors and manual as-of anchors, each explicitly attributed. Source teaching does not prescribe a universal refresh/anchor-lock policy.

## 11.6 Zone overlap, confluence and nonindependence

Suppose a resistance interval overlaps an OB and a Fibonacci retracement formed from substantially the same highs/lows. This may make the region visually interesting, but the three observations can be derived from **the same price evidence**. Their count cannot be multiplied into a numerical hit probability, and “three confluences” is not automatically three independent measurements. Report each origin and dependence. Separate the *geometric intersection* of zones from their **union**, which can increase width and decrease precision.

The BPI case illustrates this directly: resistance 92–94 overlaps FVG 92–97; resistance 98–100 overlaps FVG/OB 98–103; resistance 110 lies within 108–112. The correct claim is **co-location of source annotations**, not a proven concentration of verified institutional sell orders.

## 11.7 R2 contact → reaction → eligibility: preserve five stages

For an eligible zone \(Z=[a,b]\) and a completed candle with price interval \([L_t,H_t]\), one independent **geometric overlap** predicate is

\[
(H_t\ge a)\land(L_t\le b).
\]

An alternative body-only predicate replaces the candle interval with \([\min(O_t,C_t),\max(O_t,C_t)]\). A wick-only touch and a body-contact rule can legitimately disagree. If a market gaps over the zone, high/low bounds can straddle an interval without proving an actual *trade* occurred at each intervening price. A hypothetical fill at that zone cannot be inferred from OHLC intersection.

The stages must be kept distinct:

1. **Context established:** relevant market structure or declared range known.
2. **Zone established:** correct level and source evidence known *before* candidate contact.
3. **Zone contact:** completed overlap or more specific observed event, with its own time.
4. **Reaction confirmed:** qualifying completed candle or multi-candle sequence becomes knowable.
5. **Trade scenario eligible for risk review:** source-sequence and research prerequisites are met; risk is separately assessed. This is not an actual fill.

**R2-A — later-bar research comparator.** Require a different lower-timeframe candle *after* the completed touch bar to provide reaction. A strict subvariant requires touch evidence to have been available by reaction-bar **open**, whereas a more permissive comparison admits a later-bar reaction when both are known by decision time. A distinct bar's existence does not itself establish that the touch was observed *before the reaction began*. This approach is conservative about same-bar ambiguity but can miss one-candle reactions described in Lesson 08.

**R2-B — same completed candle comparator.** If the zone was established beforehand, a single **fully closed and available** candle may establish geometric overlap and a qualifying bullish/bearish candle pattern at the same close. This fits the source's statement that one strong confirmation can suffice; it **does not** claim when inside that candle price contacted the zone, nor does it infer an intrabar entry. This variant may be more source-compatible for some examples but requires cautious pattern and invalidation handling.

**R2-C — truly ordered finer-grained evidence.** If authentic time-ordered observations show a particular contact followed by a later reaction, those events can be analyzed in sequence. Ordinary OHLC is insufficient to reconstruct their exact path. Lack of observed order should be marked **UNKNOWN**, not silently converted into a plausible ordered story.

## 11.8 Invalidation, episode reuse and timing conflicts

**Independent invalidation alternatives:** support may be invalidated after a complete close below its far lower boundary, after any wick excursion below, or only after multi-candle acceptance/structural shift. Resistance mirrors these conditions above its far upper boundary. These disagree most when a candle temporarily pierces a zone and closes back inside. Coach does not prescribe a global invalidation algorithm.

**Same candle touches and invalidates.** Under the completed-close-beyond-far-edge hypothesis, a candle that overlaps demand but closes below its floor records **TOUCHED_AND_INVALIDATED**, not a bullish qualified touch from which a long is automatically promoted. Do not let an attractive wick override declared structural invalidation without a separate source-compatible rule.

**Contact episodes.** Once a known zone is contacted, a bounded episode might be defined to seek reaction. Additional bars oscillating inside that same zone are not automatically independent new setups; explicit episode reset rules are needed for genuine departure and re-entry. Missing time periods, later revisions or a materially new zone are new evidence states, not permission to rewrite old episodes. Expired or invalidated setups cannot be resurrected solely by later receiving a fee estimate or another unrelated indicator.

**Important distinct range branch.** Lesson 10 says entry at a **“break of confirmation”**, whereas Lesson 08 says enter *after the confirmation candle has closed*. An experimental **RB1** trigger could be a subsequent, valid, armed excursion beyond the confirmation candle extreme; **RB2** might require a subsequent completed **close** beyond it. Both require the reference candle to be final and known **before** the new crossing. A candle cannot cross its *own final high* after that high is defined; the reference must come from a previous completed candle. These are alternative research interpretations; the original source does not pick one universally.

---

# 12. Candle geometry, alternative confirmations and R3 corrections

## 12.1 Source pattern grammar, without adding compulsory filters

From original Lessons 02, 06 and 08:

- **Hammer at support:** small body near top, long lower wick; possible bullish rejection. Not guaranteed to reverse.
- **Shooting star at resistance:** small body near bottom, long upper wick; possible bearish rejection.
- **Doji:** small or absent real body with wicks; indecision, *not* a stand-alone direction.
- **Bullish engulfing:** a large green candle engulfs a preceding red candle, especially near support; **bearish** mirrors this near resistance. Coach does not uniquely say body-only versus full range.
- **Lesson 08 alternative confirmations:** (a) engulfing, **or** (b) long-wick rejection **plus follow-through**, **or** (c) strong large-body candle. Coach does **not** demand all three at once. “One strong confirmation enough” does not erase the follow-through explicitly needed for that one particular confirmation type.
- **Lesson 10 range:** may require a later *break* of a confirmation signal, not merely the same immediate close condition.

Separate **shape**, **location**, **trend context**, **timing**, and **risk readiness**. A bullish engulf away from any eligible support/demand region can be a real geometric pattern while still **not** meeting Lesson 08's source-style location prerequisite.

## 12.2 Exact OHLC primitives

For a valid completed candle, let

\[
\begin{aligned}
B_t&=|C_t-O_t| &&\text{real body size},\\
U_t&=H_t-\max(O_t,C_t) &&\text{upper wick},\\
W_t&=\min(O_t,C_t)-L_t &&\text{lower wick},\\
R_t&=H_t-L_t=B_t+U_t+W_t &&\text{total range}.
\end{aligned}
\]

Bullish color requires \(C_t>O_t\); bearish color \(C_t<O_t\); equality is neither. For a **valid zero-range** candle, \(R_t=0\) and all normalized body/wick fractions are undefined: do not divide by zero or automatically call it a tradable doji. For a **zero-body, nonzero-range** candle, wick/body ratios are undefined although wick/range may be meaningful. Invalid or missing OHLC/finality requires an **INSUFFICIENT** classification separate from valid flat price movement.

## 12.3 Engulfing has competing precise interpretations

**EN-BODY (independent, equality-permissive):** a bullish candidate has a preceding red body \(C_{t-1}<O_{t-1}\), current green body \(C_t>O_t\), with

\[
O_t\le C_{t-1},\qquad C_t\ge O_{t-1}.
\]

Bearish mirrors the colors and relative inequalities. The **strict closing edge** variant replaces last \(\ge\) with \(>\); a stricter opening edge may also be compared. Dojis are excluded from the two opposite-color definition. Coach's big-body wording may motivate a separate proportional body-strength test, but does not give its numerical threshold.

**EN-RANGE:** with the same color/direction context, a full high–low engulf additionally/alternatively demands \(L_t\le L_{t-1}\) and \(H_t\ge H_{t-1}\). These two tests are not equivalent. For example, prior red \((O,H,L,C)=(105,110,98,101)\) and current green \((100,107,99,106)\) satisfies **EN-BODY**, but not **EN-RANGE** because its high and low remain inside the prior extremes. The source figures do not resolve the universal convention.

**EN-BIG:** one may separately test \(B_t/R_t\ge\beta\) or \(B_t\ge\lambda B_{t-1}\), with experimentally declared \(\beta,\lambda\). No such values are Coach-specified. Engulfing and strong-body measurements may describe **one identical candle**, not two independent pieces of evidence.

## 12.4 Hammer, shooting star, rejection and doji proposals

For a positive-range candle, an experimental **hammer** predicate can require \(B_t/R_t\le b\), \(W_t/R_t\ge w\) and body near the upper portion. A **shooting star** mirrors those tests with **upper wick** \(U_t/R_t\ge w\) and body near the bottom. A **doji** comparator can use \(B_t/R_t\le d\) with both relevant wicks positive. The constants \(b,w,d\) and body-location tolerance have no unique Coach values; contextual support/resistance must be independently evaluated.

**Directional rejection is essential.** A bullish rejection near support needs evidence in the **lower wick**; a bearish rejection at resistance needs evidence in the **upper wick**. Testing \(\max(U,W)/R\) in both directions is wrong: it can accept a *large upper wick at support* as bullish lower-price rejection. The source-driven correction is seen in a hypothetical green candle \((O,H,L,C)=(101,110,100,102)\), for which \(R=10\), **lower wick fraction 0.1** and **upper wick fraction 0.8**. A threshold of 0.5 on the *maximum* would pass, but the direction-correct lower-wick criterion fails. The 0.5 is an illustrative audit threshold, **not Coach's rule**.

**Follow-through alternatives** after a prior rejection are (FT1) later finished candle closes beyond the rejection **body edge**; (FT2) later finished candle closes or crosses beyond the rejection candle's **entire high/low** under a selected break basis; (FT3) later directional displacement or volume strength beyond a predeclared level. A later candle may qualify FT1 without qualifying FT2. The source says follow-through but does not specify which, how many bars may elapse or what expires a rejection pattern.

**STRONG-BODY candidate:** an eligible fully closed directional candle with body fraction \(B/R\ge s\), independent of the prior candle's color. Source uses “malaki ang body,” not a fixed measured \(s\). One strong body at a wrong location can still fail the *setup* even if it passes the candle-shape test.

## 12.5 Pattern timing and ambiguity cases

| Condition | Appropriate research result |
|---|---|
| Engulfing appearance changes while candle is developing | **PROVISIONAL**, not confirmed pattern |
| Finished hammer-like lower wick at previously known support | Possible rejection shape and location, not automatic long |
| Bearish shooting star at resistance but context/downstream risk absent | Valid shape; scenario may still WAIT/INSUFFICIENT |
| Doji after an impulse | Indecision; next step requires independently defined confirmation |
| Rejection candle final, later follow-through still forming | WAIT_CONFIRMATION for that branch |
| Candle simultaneously strong-body and engulf | One underlying price observation; avoid double-counting |
| Completed candle overlaps zone and invalidates it under selected policy | Preserve contact fact; withhold ready status |
| Pattern on a zone only established **after** the pattern | Not eligible historical location-confluence event |
| A gap creates ambiguous intrabar price path | Geometric facts only; observed order/fill UNKNOWN |
| Exact equal OHLC / malformed candle | ZERO_RANGE versus DATA_INSUFFICIENT must stay distinct |

**Main research choice.** Keep source's multiple confirmation alternatives, compare simple clear shapes to more selective candidates on identical evidence, then ask whether extra thresholds improve *held-out* after-cost outcomes or merely delay entries and reduce coverage. No mathematical elegance alone establishes a financial edge.

---

# 13. Multi-timeframe context, conflicts and decision-state research: R4

## 13.1 The source is genuinely multi-scenario

Coach uses HTF for bias and locations, LTF for reactions, and demonstrates examples that *disagree across scales*. Examples: SOL 4H bullish but 15m bearish scalp; BTC 4H down but 15m consolidating; BPI Daily bearish but 4H tentative bounce; TON 4H extremely bullish but a fresh immediate long is discouraged. A system that simply scores how many timeframes are bullish and returns the majority would erase the meaningful conditions described in those examples. Similarly, requiring unanimity across all timeframes would exclude documented countertrend and pullback scenarios.

The proposed research representation is a **set of scoped observations**, each carrying its own instrument, timeframe, definition, source evidence and time of availability. Distinguish:

- Higher-timeframe **confirmed structural regime** from lower-timeframe **momentum**.
- Lower-timeframe **structural change warning** from an actual higher-timeframe reversal.
- **Contextual bias** from the **current scenario type**.
- **Qualified prior zone** from current price location relative to it.
- **Developing contact**, **completed contact**, **completed reaction** and full **risk readiness**.
- Human source annotation from an independently calculated feature.

## 13.2 Timeframe combinations in original source versus experimental profile

| Context | Source evidence | Research interpretation |
|---|---|---|
| **1H/4H → 5m/15m** | L04, L08 | General HTF-to-LTF preparation and confirmation; not a universally compulsory exact ladder |
| **4H/Daily/1H → 5m/15m** | L14, L19 | Swing/Fib/indicator analysis with chosen higher contextual scale |
| **30m OB → 5m** | QA2 Coach FARTCOIN alternative | Source-specific pullback scalp |
| **4H bullish + 1H weak + 15m bearish** | L13 SOL | Countertrend short can coexist with separate HTF-aligned long watch |
| **4H bearish + 15m range** | QA3 BTC | Conditional rejection short versus later breakout long, each with own conditions |
| **Weekly/Daily/4H** | N02 BPI stock | Timeframe-relative recovery; not a fixed hierarchy for crypto |
| **4H, 1H, 15m, 5m together** | Later owner research direction | Experimental four-layer decomposition: macro context, intermediate structure, prior setup area, reaction; **not** Coach's universally prescribed four-factor checklist |

The November 14 experimental decomposition treats **4H** as the broader structural regime, **1H** as intermediate confirmation/context, **15m** as the prior zone/setup location, and **5m** as the local closed reaction. This may be an organizationally useful hypothesis, but strict four-way agreement and a fixed relevance hierarchy do not follow from Coach's PDF. The full method must still retain legitimate range, scalp and breakout branches.

## 13.3 Research timing alternatives: what did we know at the decision?

Suppose a 5m candle spans **11:55–12:00** and a 4H bar also nominally ends at **12:00**.

- **MTF-T0 — opening-context freeze:** assess the 5m candle using only the higher-timeframe records fully known at its **11:55 open**. The just-ending 4H bar cannot retroactively govern 11:55–12:00. This is a deliberately conservative causal model.
- **MTF-T1 — decision-time context:** at a decision after 12:00, allow a newly final higher-timeframe record if genuinely available by that decision, but explicitly record that it was learned **after** the 5m candle opened. It did not exist as a 11:55 premise.
- **MTF-T2 — retrospective human annotation:** preserve the assessor's reported context and the annotation's actual creation time. A source screenshot taken later cannot establish earlier intrabar knowledge or genuine publication order.

At a simultaneous nominal bar close, **equal timestamps do not prove equal receipt order**. Missing authenticated receipt metadata justifies a modeled conservative clock or an unknown ordering statement. A later higher-timeframe update should prompt **new assessment or REASSESS**, not historical rewriting.

## 13.4 Conditional setup gating, not one universal BUY/SELL vote

**Trend continuation.** Require established relevant HTF trend and location, a previously knowable eligible zone, a completed contact/reaction under declared pattern/timing choices and coherent risk. An LTF pullback against the HTF is not intrinsically a disqualifier. If HTF structure materially changes, reassess.

**Conditional sideways range.** Require a credible range and pre-known boundary; await a reversal reaction and, for Coach's range case, a separately defined later **break of confirmation**. Being directionless alone is not a buy/sell rule.

**Countertrend scalp.** Label the trade style explicitly **AGAINST_HTF**, retain the HTF trend and set a different holding-horizon/risk premise. The L13 short does not imply Coach permits all countertrend shorts anywhere.

**Pullback scalp.** Retain QA2-specific 30m location/5m confirmation and RSI 40–50 *contextual* variant. Do not force the generic 4H/1H hierarchy or universal RSI>50 filter on it.

**Reversal watch.** A lower-timeframe CHoCH is a **candidate local structural change**. Require independently confirmed higher-timeframe regime evidence before declaring a macro reversal.

**Conditional breakout.** QA3 supplies three distinct possible positive confirmations for breakout-long: **15m BOS**, **1H BOS**, **or a 1H close above its cited area**. Do not remove one alternative when creating a new generalized rule. A possible breakout can coexist with a still-bearish 4H context and must be described honestly.

## 13.5 Diagnostic state vocabulary — independent extension, source-compatible purpose

| Proposed state | Interpretation | Critical distinction |
|---|---|---|
| **DATA_INSUFFICIENT** | Required OHLC, market identity, interval, precision or finality is missing/invalid | Missing data is not a flat or neutral market |
| **CONTEXT_INSUFFICIENT** | Needed HTF structural regime cannot yet be established | No proven trend is not the same as proven range |
| **ZONE_INSUFFICIENT** | No qualified prior zone exists for the selected scenario | Different from a known zone that simply was not reached |
| **UNSELECTED_STYLE** | Distinct scenario branches are recognized but no decision style is specified | Observation may still be useful |
| **WAIT_ZONE** | A known eligible location has not been contacted | Captures L08's NO TRADE if no zone visit |
| **CONTACT_PENDING** | Intrabar zone touch appears but is not yet confirmed with admissible data | Developing event is provisional |
| **WAIT_CONFIRMATION** | Qualified contact exists but required completed reaction does not | No premature entry trigger |
| **WAIT_BREAK** | A range reversal candle is established, but its separate breakout criterion is not met | Specific to L10-style trigger variant |
| **REASSESS** | Relevant context or prior premise has changed | Must not keep stale readiness attached |
| **INVALIDATED** | A stated zone/scenario invalidation condition occurred | Cannot silently reuse the old qualified episode |
| **EXPIRED / SUPERSEDED** | Candidate exceeded declared lifetime or its reference was replaced | Historical status may survive but not current eligibility |
| **CONDITIONAL_CONFLICT** | Opposed conditional scenarios meet distinct prerequisites at same evaluation point | Do not fabricate one globally certain action |
| **RISK_INCOMPLETE** | Location/reaction may be meaningful but essential entry/stop/target/units/cost fields lack qualification | Pattern correctness ≠ feasible position |
| **CANDIDATE_FOR_REVIEW** | Selected scenario and risk assumptions qualify a descriptive conditional plan | **Not** an order, executed fill, win probability or financial recommendation |

A conservative method should show **known failures**, **unknown information**, and **unselected hypotheses** as separate conditions, not just output WAIT for all of them. As newer data arrives, explain what changed. A historical setup record remains tied to the evidence and assumptions valid at its original assessment time.

## 13.6 Stable setup and episode lifecycle

A setup's identity should be established by its **market, scenario, direction, contextual source/reference and zone version** before any later contact or reaction. Contact episodes and confirming candles are *events attached to* that identity, not ingredients retroactively inserted into the identity itself. This makes it possible to distinguish:

- Zone found → awaiting price contact.
- Zone first contacted → awaiting qualified reaction.
- Reaction established → risk inputs missing or research candidate available.
- No reaction within chosen lifetime → expired.
- Zone breached or context materially reversed → invalidated/reassess.
- Price exits and re-enters later → potential **new episode** only under an explicit reset rule.
- Evidence arrives late or is corrected → a versioned *new* assessment; original as-issued record is retained.

A current candidate should not become newly actionable merely because an unrelated missing fee, price tick or historical file later arrives *after* its expiry. The proper result is a revised retrospective risk assessment or no current qualification. Preserve temporal and structural ownership of every condition.

## 13.7 Examples that falsify oversimplified rules

1. **4H UP, 15m DOWN with no support contact:** the macro trend remains UP, but the continuation entry is WAIT_ZONE. A simple majority/EMA signal might incorrectly mark immediate BUY.
2. **4H UP, 1H weakening, 15m bearish confirmation at supply:** a conditional countertrend-scalp reading can exist without renaming 4H DOWN. An all-timeframe unanimity rule would miss Coach's SOL example.
3. **4H DOWN, 15m RANGE:** default action is not automatic SHORT; the exact reason depends on whether a qualified resistance zone exists, was contacted, and has a completed bearish reaction.
4. **4H DOWN, 15m bullish CHoCH:** possible LTF change, not confirmed 4H trend reversal.
5. **4H UP, RSI near 97, price above EMAs but away from support:** explicit WAIT for a better retracement location is compatible with Coach's TON example.
6. **Weekly/Daily bearish BPI, 4H possible bounce:** lower-scale improvement does not retroactively create Daily bullish BOS or CHoCH.
7. **Two contrary conditional scenarios ready under different styles:** report conflict and the differing premises rather than inventing a decisive score.
8. **HTF closes just as LTF reaction closes:** do not inject newly available HTF evidence as though it was known before the local candle began.

---

# 14. RSI, EMA, indicator confluence and redundancy

## 14.1 RSI source reading and separate contextual roles

**Coach source:** RSI measures relative directional momentum/strength from recent gains and losses; common illustrative length **14**, interpreted at **70** (overbought), **30** (oversold) and **50** (momentum midpoint). Values above 50 indicate bullish momentum *in the source's heuristic*; below 50 indicate bearish momentum. Values above 70 can persist through powerful advances; below 30 can persist during strong declines. Neither automatically calls for reversal. Coach specifically says do not buy solely because RSI reaches 30 or sell solely because it reaches 70.

**Independent standard formula.** If a chosen method produces average positive change \(\overline G\) and average magnitude of negative change \(\overline D\), with a specified smoothing/initialization convention, \(RS=\overline G/\overline D\) and

\[
RSI=100-\frac{100}{1+RS}.
\]

Zero-gain/zero-loss and warmup cases require explicit conventions; do not assume two data vendors with different seeds and histories compute identical edge values. A simple threshold is descriptive, not a causal forecast.

**Source-specific momentum cases** cannot be replaced with one invariant threshold:

- **L16/L19 continuation-long example:** RSI above 50 in HTF bullish context; lower-timeframe RSI “bounces above 50”.
- **QA2 FARTCOIN pullback scalp:** Coach describes RSI bounce **40–50**, plus price relative to EMA50 and zone reaction.
- **L21 TON:** 4H RSI ~97 and still strongly bullish, yet Coach prefers to **wait**, not buy at the top or mechanically short as “overbought”.
- **QA1 BTC:** RSI ~69.91 on 4H is **below**, not above, strict 70. “Near overbought” is a description, not equal to the overbought predicate.
- **N02 BPI:** weekly RSI ~29.04 is actually below 30, while Daily and 4H RSI ~31.97 and ~34.63 are above 30; their market structure can still be bearish.

**Independent bounce hypotheses:** crossing upward through 50, dipping into 40–50 and turning upward without crossing, recovering from <40 into the band, sustaining >50 for a selected number of completed bars, or comparing normalized RSI slope. Each has a different entry time and false-trigger profile; Coach does not define one as universal.

## 14.2 EMA settings, meaning and exact mathematical redundancy

Coach's **EMA20** is short-term context, **EMA50** medium, **EMA200** broader trend. Price above an EMA and rising EMA are interpreted as bullish, while below/falling is bearish. A flat EMA or repeated price crossings indicates possible sideways whipsaw. An EMA can function as possible dynamic support/resistance but does not guarantee a bounce, and its exact current plotted value is not necessarily an order fill price. L21's TON figure has 20/50/100/200; Q&A1 also has 20/50/100/200; final BPI source shows an initial settings value 9 then asks the learner to use 20/50/200. **Neither EMA9 nor exactly one EMA period is mandated for all Coach setups.**

**Independent recurrence** for a close-based standard EMA of length \(n>1\):

\[
E_t=\alpha C_t+(1-\alpha)E_{t-1},\qquad \alpha=\frac{2}{n+1},\quad 0<\alpha<1.
\]

Two useful identities follow algebraically:

\[
E_t-E_{t-1}=\alpha(C_t-E_{t-1}),\qquad C_t-E_t=(1-\alpha)(C_t-E_{t-1}).
\]

Therefore, for that **same bar, same close input and same EMA recurrence**:

\[
C_t>E_t\quad\Longleftrightarrow\quad E_t>E_{t-1}
\]

and the corresponding downward/zero cases match. **Price above the current close-based EMA and EMA sloping upward over exactly one bar are algebraically redundant.** They cannot be honestly treated as two independent confirmations. The fact is a mathematical proof under its stated definition; it says nothing about a multi-bar slope, high/low price versus close, different EMA sources, or predictive financial merit.

**Notional “angle” is not an invariant.** A visual slope angle changes when chart price scale or viewing proportions change. Research candidates instead define \(\Delta_k E=(E_t-E_{t-k})/k\) for declared \(k\), or normalize by price/volatility. Each needs warmup, timeframe, threshold and robustness analysis. An exact numeric threshold is **not** found in Coach's lessons.

## 14.3 Rejections/retests of EMA: distinct candidates

A possible EMA retest may be defined by (a) wick price interval crossing the EMA; (b) real-body contact; (c) close crossing then returning; (d) distance within a chosen fixed tick/percentage/volatility tolerance; or (e) a multi-bar countertrend retracement followed by completed directional reaction. These events differ substantially. A short, high-volatility wick is not necessarily a useful “respected EMA”. Coach's source does not give a unique tolerance or dwell time.

## 14.4 Avoid a false probability model from correlated confluence

**Source:** Coach emphasizes *trend + area + confirmation*, then uses EMA, RSI, FVG and OB as contextual evidence. These are useful classes of explanation but they often share the same underlying price changes:

- EMA20/50/200 all transform the same series at different horizons.
- RSI is also derived from recent close changes; RSI >50 and price momentum can overlap substantially.
- BOS, higher highs and pivot-derived support can share the same structural extrema.
- An FVG and OB can derive from the same displacement candles.
- Engulfing and strong-body labels can describe the same single bar.
- Price-above-EMA and one-bar-up-slope are *exactly equivalent* under the standard recurrence assumptions.

Consequently **do not add one point for every label and call the total a calibrated win probability**. Analyze whether an added filter contributes new information after accounting for already included measures, and at what cost in signal delay, missed valid cases and sample size.

**Independent ablation comparisons:** a structure+zone+closed-candle baseline; remove RSI; remove EMA; remove OB/FVG; replace strict patterns with broader source-style alternatives; use one EMA versus multiple. Predeclare training/validation boundaries, equal instrument cases and realistic friction. A fancy stack is not superior merely because it seems more detailed.

---
# 15. Complete risk, reward, margin, position sizing, exit and expectancy research: M06

## 15.1 Source principle: direction is not sufficient without a quantified plan

Coach's lessons teach that an entry should have an identifiable stop and profit objective, and that R:R can make the difference between a profitable **hypothetical payoff distribution** and a losing one. Lesson 08 uses a stop beyond structural support/resistance and a target at the next opposite structural level **or** a fixed multiple such as 1:2 or 1:3. Lesson 05 introduces margin and leverage but warns against unmanaged exposure. Lesson 13's SOL case distinguishes a short scalp against a still-bullish larger structure from a conditional long aligned with that structure. A range or candle pattern is not independently a financially complete plan.

**Independently introduced M06 distinction:** there are at least four different questions: (1) is the stop/target on the correct side of a proposed entry? (2) what loss in **price units** does that imply? (3) what quantity, product and currency conversion turn that movement into **cash risk**? (4) does an actual order, if any, fill at the modeled prices and protect the desired quantity? The source gives teaching examples primarily for the first two; the detailed contracts below are research additions.

## 15.2 Signed trade geometry avoids hidden wrong-side errors

Let \(E\) denote hypothetical entry, \(S\) hypothetical stop, \(T\) hypothetical target, and \(s=+1\) for long or \(s=-1\) for short. Define

\[
d_p=s(E-S)>0,\qquad g_p=s(T-E)>0,\qquad \mathrm{RR}_{\rm gross}=\frac{g_p}{d_p}.
\]

A candidate failing either strict positive-distance condition has **invalid direction/geometry**; absolute values must not be used to disguise a long stop **above** entry or a short target **above** entry. If either distance is zero, the proposed ratio is undefined or invalid. For a hypothetical fixed multiple \(\rho>0\), a target is

\[
T=E+s\rho d_p.
\]

For a support region \([a,b]\), one *independent strict outside-zone interpretation* requires a long stop \(S<a\), and for a resistance region a short stop \(S>b\). Coach says “below”/“above”; he does not mandate an extra number of ticks or an ATR buffer. Price-based structural invalidation (such as a candle close through a zone) and the trigger conditions of a **protective stop** are different: a zone can be retested while a position's stop is struck, or vice versa, depending on chosen policies.

A **next-level target** and an **exact 2R/3R target** need not coincide. If the nearer structural obstacle lies well before the fixed-R target, they form *competing plans*. Never silently assume the farther target is reachable or drop the structural level to make arithmetic prettier. Source L08 presents alternatives without a global selection priority.

## 15.3 Exposure and leverage: fixed collateral versus fixed notional

Coach's 100-unit capital example illustrates that with a fully allocated USD 100 margin, changing assumed leverage from \(1\times\) to \(10\times\) to \(20\times\) can correspond to USD 100, 1,000 or 2,000 notional. But a separate fixed **USD 100 notional** illustration uses roughly USD 100 initial margin at \(1\times\) or USD 10 at \(10\times\). These are two different experiments.

Under a simplified linear position, price P&L for a fixed position quantity is unchanged solely by selecting a different leverage setting. Higher leverage enables greater notional for a fixed collateral allocation and can therefore amplify *account* gains and losses **when exposure is increased**. Initial margin is collateral, **not** the amount a stop order guarantees to lose. Liquidation can occur before an intended stop due to margin requirements, mark price, funding, collateral mode or volatility. Neither a named low leverage nor a stop level can eliminate tail loss.

Margin terminology to keep distinct: initial margin, maintenance margin, available/free margin, account equity, isolated versus cross margin, product-specific risk tiers and liquidation-price assumptions. Coach's educational platform maximums are historical illustrations, **not** universal current contract facts.

## 15.4 Unit-consistent position sizing: a proposed linear model

For a linear product, quantity \(q\) in declared order units and multiplier \(m\) in underlying units per order unit, one price-unit change has gross quote-currency value \(qm\). Planned loss at stop reference in quote currency is

\[
L_{\rm gross}=qm d_p.
\]

If an appropriate same-time conversion factor \(x\) converts quote currency to the account currency, the modeled account loss is \(xqm d_p\). When an account-loss budget is \(B\) and costs are ignored solely to form a preliminary bound,

\[
q_{\rm preliminary}\le \frac{B}{xmd_p}.
\]

This is **not** final executable size. Actual allowed quantity depends on exchange-defined increments, minimum notional, tick price rounding, contract multiplier, account equity, fee/funding assumptions, margin, other exposure and liquidity. Rounding quantity upward can violate the risk budget. The source does not specify a universal account-risk percentage. One illustrative source risk of 2% per 20-trade cycle must not be converted into an approved risk fraction for all trades.

Inverse-contracts, spot units, tokenized gold and cash-settled derivatives have differing P&L/unit conventions. A formula for one product cannot be reused merely because the ticker shares an asset name. Public market/product specifications are not evidence of an individual's balance, margin, leverage configuration or actual open positions.

## 15.5 Entry activation, fills and path uncertainty

A signal candle **closing** is an observable prerequisite in Coach's Lesson 08, not a guarantee that the order would fill at that same historical close. A plan may use a subsequent market order, limit order, stop entry or another procedure, all requiring separately declared activation, execution and price-basis assumptions.

**Spread:** difference between tradable bid/ask and a reference mid or last price. **Slippage:** realized execution difference from the modeled expected fill. **Fees:** product/account/order-tier dependent, and not necessarily symmetric. **Funding:** periodic credits or debits on eligible perpetual positions depending on actual signed realized funding rates and notional held. **Borrowing interest:** separate where applicable. Counting an already adverse fill price **and** separately subtracting the same price slippage a second time is double counting.

A **stop-market** order can trigger but fill at a worse price during a gap. A **stop-limit** order can trigger without any fill if market price moves past its limit. A partial fill leaves remaining exposure, and a take-profit notional cannot automatically exceed what was actually entered. An ordinary OHLC candle with both \(H>T\) and \(L<S\) does not reveal which barrier price came first. For example, long at 100 with stop 95 and target 105, a later bar \((O,H,L,C)=(100,106,94,101)\) admits both **target-first** and **stop-first** intrabar paths. One fixed “take profit wins” assumption creates a result not demonstrated by that candle.

**Trailing stops** require at least an activation event, selected trigger price, offset or adjustment rule, update frequency, protection attachment and actual filled position size. Coach mentions trailing in several cases, but none supplies a complete universal trailing algorithm. A list of TP1, TP2, TP3 targets is not proof that all targets were executed or that every allocation is equal. Partial target fractions plus a residual position must sum to no more than the filled quantity.

## 15.6 Numerical expectancy: what Coach's examples actually prove

Let \(p\) be win probability in an *assumed two-outcome model*, \(G>0\) gross gain on a win, \(D>0\) gross loss on a loss, and \(C_W,C_L\ge0\) their respective costs. Define net win \(W=G-C_W\), positive net loss magnitude \(L=D+C_L\). For \(W,L>0\), conditional expectancy and break-even satisfy

\[
\mathbb E[\Pi]=pW-(1-p)L,\qquad p_{\rm break-even}=\frac{L}{W+L}.
\]

At **gross 1:2**, where \(G=200,D=100\) with **zero costs**, break-even is **1/3 = 33.333…%**. Coach's rounded practical language “~35–40%” is compatible with the idea that a slightly greater win rate may be needed for profit, but it is not the exact zero-cost mathematical threshold. In precisely **10** binary trades, 3 wins produce a net loss and 4 produce a net gain for Coach's fixed-size assumptions. At 45% win over 20 such trades (9 wins, 11 losses), net is \(9(200)-11(100)=700\), and capital rises from **₱5,000 to ₱5,700** in the *example*.

**Costs change the threshold.** If a win of 200 incurs 10 cost and a 100 gross loss incurs 10 cost, net win=190 and net loss magnitude=110, so break-even becomes \(110/(190+110)=110/300\approx36.667\%\). If the modeled net win is nonpositive, the two-outcome setup has no positive expectancy for any nonzero loss probability. The model must handle partial/no-fill, scratch, variable exit and funding outcomes separately rather than pretending all are exactly one full target or one full stop.

**The win rate is not supplied by Coach's illustrative trade counts.** It must be estimated from a valid representative process with a well-defined eligible setup population and outcome rule. Larger targets may change the probability of winning. Thus the source's identical 45% win rate applied to 1:1 and 1:2 examples is a **controlled mathematical comparison**, not an empirical statement that both styles actually win 45% of the time. A high nominal ratio with very low fills or high fees may still be unattractive.

## 15.7 Compounding is scenario arithmetic, not a track record

Coach's source re-risks **2% of the new capital at the next 20-trade cycle**, rather than necessarily recalculating after *every trade*. Under his assumed outcomes, capital goes:

| Completed hypothetical cycle | Capital |
|---:|---:|
| 0 | ₱5,000 |
| 1 | ₱5,700 |
| 2 | ₱6,498 |
| 3 | ₱7,407.72 |
| 4 | ₱8,444.80 (rounded) |
| 5 | ₱9,627.07 (rounded) |

These numbers follow repeatedly multiplying by **1.14** under the fixed assumed cycle results and ignoring cost/liquidation. They are *not* evidence that the method will achieve this trajectory or that 2% per trade is safe. Percentage risk, drawdown and position size under sequential losses must be considered jointly. A 2% risk setting is not the same as 2% price-stop distance or 2% initial margin.

## 15.8 M06 alternative analytical tiers

| Tier | Independent research scope | What it can and cannot establish |
|---|---|---|
| **A — nominal geometry** | Check source-style entry, stop beyond zone, target at level or fixed R, correct signs, range endpoints | Can show a coherent *price-based* hypothetical plan; cannot show fill, account cash risk or profitable expectancy |
| **B — cost- and contract-aware envelope** | Add independently qualified tick/quantity/multiplier/settlement, permitted size, fees, funding, spread and adverse-fill scenarios | Can reject infeasible or negative-net plans under named assumptions; cannot guarantee a maximum loss outside scenario family |
| **C — execution-path scenarios** | Enumerate gap, partial fill, stop-limit nonfill, mixed TP/SL sequencing and trailing alternatives | Can expose uncertainties; actual outcomes require genuine ordered executions/price evidence |

An incomplete condition should be labeled at the relevant layer. For example, a valid bullish pattern with unknown stop and margin is **RISK_INCOMPLETE**, not “invalid candle” and not “certain buy.” An expired pattern cannot be revived by later account data. The proposed **CANDIDATE_FOR_REVIEW** label is informational, not an instruction to execute an order.

---

# 16. Consolidated numerical source cases and what can be concluded

This section collects key source price proposals in a single place. These are **historical pedagogical snapshots, not current market prices, executable signals or claimed filled positions**. Many are approximate zones; preserve inequalities and unknowns.

| Source case | Original contextual status | Illustrative entry / stop / target | Mathematically valid inference and important limitation |
|---|---|---|---|
| **L03 ₱5,000 risk-reward** | Hypothetical independent 1:2 win/loss simulation | Risk ₱100, win ₱200 | 50% in 10 → +₱500; 40% → +₱200; 30% → −₱100; 45% over 20 → +₱700; not realized performance |
| **L05 fixed-margin leverage** | Educational notional/margin illustrations | USD100 collateral at 1x/10x/20x; fixed USD100 position at 1x/10x | Fixed collateral with higher allowed notional ≠ fixed notional with lower margin; leverage alone is not stop loss |
| **L10 gold range long** | 1H sideways range; only at support with 5m reversal | Support **4,670–4,680**, stop **4,665**, opposite resistance **4,730–4,750** | Conditional location and confirmation-break remain; actual fill price missing |
| **L10 gold range short** | Opposite range boundary | Resistance **4,730–4,750**, stop **4,755**, TP support **4,670–4,680** | Confirmation-break unknown; do not reuse forex levels for a different product |
| **L13 SOL countertrend short** | 4H bullish but 1H weak / 15m bearish scalp | Entry **86.4–86.7**, stop **87.2**, TP1 **85.8**, TP2 **85.3**, TP3 **84.8** | Gross per-target RR varies with entry; source does not report realized price/fill or allocation |
| **L13 SOL conditional HTF long** | Wait for 4H demand and bullish 15m CHoCH/displacement | Zone **85.2–85.6**, stop **strictly below 84.9**, TP **86.5**, **87+** | Exact stop and completed entry absent; can't derive unique cash risk/ratio |
| **L21 TON conditional long** | 4H very bullish / RSI ~97 / wait for retracement | Entry area **2.58–2.62**, stop **strictly below 2.52**, TP **2.75–3.00** | No unique R:R without exact stop; deeper zones could remain valid after upper setup stops |
| **QA2 student FARTCOIN long** | Student reports existing scalp position | Entry **0.2436**, stop **0.2385** | Distance **0.0051**, approximately **2.0936%** of entry; NOT account-risk percentage |
| **QA2 Coach proposed alternative** | New pullback scalp, 30m OB / 5m reaction | Entry **0.238–0.240**, stop **strictly below 0.231**, targets **0.258–0.279** | No exact stop, fill or independently verified zone; RSI 40–50 bounce is contextual |
| **QA3 student BTC short** | Student's suggested plan; Coach separately offers alternatives | **79,419 / 79,918 / 78,423** | Risk **499**, reward **996**, gross **1.99599R**, rounds to 1:2 |
| **QA3 Coach conditional short** | 4H bearish, wait resistance rejection in 15m range | Entry ~**79,850**, stop ~**80,250**, TP ~**79,000 or below** | Approximate gross geometry only, unexecuted; later breakout may instead qualify a different scenario |
| **QA3 Coach conditional long** | Only after meaningful breakout evidence | **15m BOS** or **1H BOS** or **1H close above ~79,850–80k** | No source exact stop/target; a distinct *conditional* scenario |
| **N02 PSE:BPI bounce** | Weekly/Daily bearish; 4H local bounce possible | Weekly support **₱85–86**, Daily shift around **₱92**, 4H bounce break **₱89.5–90** | No global trend reversal, actual order, or cross-instrument transferable level |

## 16.1 SOL short payoff sensitivity (L13)

Assuming source stop **87.2** and each target considered separately with a fully filled **hypothetical** entry:

| Entry | Stop distance | TP1 85.8 | TP2 85.3 | TP3 84.8 |
|---:|---:|---:|---:|---:|
| 86.4 | 0.8 | **0.75R** | **1.375R** | **2.00R** |
| 86.7 | 0.5 | **1.80R** | **2.80R** | **3.80R** |

The entry endpoint changes the ratio; the “same” source trade idea does not have one fixed per-target RR. These are **gross geometric** ratios and omit size, fees, slippage, funding and probability. The model does not assert all three target legs are fully filled or that any particular fraction was allocated to each.

## 16.2 Illustrative but non-Coach stop for TON (L21)

Coach provides only **stop below 2.52**. To demonstrate why exact RR is not identified, independently *assume* \(S=2.51\). Then:

| Assumed entry | Assumed target | Risk/unit | Reward/unit | Gross RR |
|---:|---:|---:|---:|---:|
| 2.58 | 2.75 | 0.07 | 0.17 | 2.43R |
| 2.62 | 2.75 | 0.11 | 0.13 | 1.18R |
| 2.58 | 3.00 | 0.07 | 0.42 | 6.00R |
| 2.62 | 3.00 | 0.11 | 0.38 | 3.45R |

**2.51 is NOT Coach's selected stop.** Replacing it changes the ratios. A stop below the *upper* pullback region may invalidate that particular setup without proving the macro trend or a lower OB failed.

## 16.3 Example gross ratios for the original L10 gold range endpoints

If one makes the **strong extra assumption** that an entry fills exactly at a selected quoted zone endpoint (not guaranteed because Coach additionally requires a confirmation break), the following endpoint comparisons illustrate variability:

- Long at support 4,670, stop 4,665, target resistance 4,730 → risk 5, reward 60, **12R**.
- Long at support 4,680, stop 4,665, target 4,730 → risk 15, reward 50, **3.333R**.
- Short at resistance 4,730, stop 4,755, target support 4,680 → risk 25, reward 50, **2R**.
- Short at resistance 4,750, stop 4,755, target 4,670 → risk 5, reward 80, **16R**.

A later break-of-confirmation entry can occur at **another price**, so these are **boundary geometry**, not a promise of extraordinary achieved reward.

## 16.4 Source Q&A FARTCOIN comparisons must never be mixed as if one trade

Student reported \(E=0.2436,S=0.2385\); the Coach alternative is \(E\in[0.238,0.240]\) with \(S<0.231\) and targets \(T\in[0.258,0.279]\). Because Coach's stop is an **open inequality**, its exact RR cannot be obtained from his statement.

A hypothetical **separately chosen** \(S=0.230\) for Coach's alternative illustrates four possible endpoint cases: (E,T)=(0.238,0.258) gives **2.50R**; (0.240,0.258) **1.80R**; (0.238,0.279) **5.125R**; and (0.240,0.279) **3.90R**. A lower entry does not automatically make the plan less risky in *percentage-stop distance*: this different stop can be wider. Neither plan's actual fills or relative outcomes are known.

---

# 17. Coach-to-research gap ledger — explicit uncertainties and corrections

This ledger is intentionally more important than an apparently polished “one true strategy” checklist. The original PDF is complete **as a lesson collection**, but many concepts are not numerically determined. Research findings below are either precise consequences under stated assumptions, or still competing hypotheses.

| ID | Coach concept / source anchor | Missing or conflicting definition | Independent candidate or required qualification | Status |
|---|---|---|---|---|
| G01 | Chart examples span forex, crypto, stock | Product/venue/price-basis equivalence | Positive instrument identity and unit matching | Essential research safeguard |
| G02 | Candles and multiple periods | Bar close, finality, valid OHLC, missing intervals | Time-indexed final-only admissible observations | Specified conceptually; feeds differ |
| G03 | Original drawings | When a marked reference was actually known | Origin, confirmation, first availability, decision-time separation | Causal safeguard |
| G04 | HH/HL and LH/LL (L07) | Swing algorithm, degree, ordered validity | Manual vs fractal vs deviation swings | OPEN selection |
| G05 | Sideways/range (L07/L10) | How many swings/which bounds establish range | Explicit range profile, not merely UNKNOWN | OPEN |
| G06 | Previous HH/LL for BOS (L11/L12) | Eligible protected references and close/wick break | Frozen armed structural references; R1-A/B comparators | OPEN choice |
| G07 | CHoCH possible reversal (L20) | When change becomes a confirmed new regime | Separate possible change and independently verified new swings | Research principle stable, exact detector OPEN |
| G08 | Fractal pivot examples | Equal highs/lows, dual-extreme candles, same-side consecutive pivots | Strict ties, quarantine, extreme-retain and order limits | Experimental |
| G09 | Historical chart markings | Backdating, reference re-use, late arming | Exact-once consumption, at-arming checks, no lookahead | Provisional method |
| G10 | Support/resistance (L09) | Zone width, lookback, number of tests, decay | Manual, pivot-cluster, rolling candidates | OPEN |
| G11 | S/R role reversal | First break vs retest and completed acceptance | RF1/RF2/RF3 competing models | OPEN |
| G12 | Order block (L11) | Same-color versus opposite-color predecessor; displacement threshold | OB0 manual, OB1 opposite, OB2 any-color | OPEN; source figures explicitly preserved |
| G13 | “Large money entered” (L11) | No participant/order evidence | Describe price geometry only; actor UNKNOWN | Inference limitation |
| G14 | FVG (multiple lessons) | Three-bar rule, minimum size, gaps and mitigation | Strict three-candle baseline; added displacement comparator | Experimental, not Coach-exact |
| G15 | Fibonacci (L14) | Anchor freezing, redraw, 0.5–0.618 versus 0.618–0.705 | Keep bands separate and timestamp eligible anchors | Source distinction established; implementation OPEN |
| G16 | “Reached support” (L08) | Wick, body, close, actual traded price | Geometric overlap versus observed contact | OPEN comparator |
| G17 | Candle shape (L02/L06) | Ratios, candle size, equality and strong threshold | Explicit OHLC geometry and separate context | OPEN thresholds |
| G18 | Engulfing (L06) | Body-only versus high–low range | EN-BODY/EN-RANGE | OPEN selection |
| G19 | Rejection candle (L08) | Wrong-wick false positives | Direction-specific lower/upper wick rather than maximum wick | Logical correction validated |
| G20 | Rejection + follow-through | Which subsequent bar/level/delay | FT1 body edge, FT2 full extreme, others | OPEN |
| G21 | One strong candle enough (L08) | Same candle touch/reaction ordering | R2-A later versus R2-B same-close | OPEN comparison |
| G22 | Range “break of confirmation” (L10) | Wick excursion versus subsequent completed close | RB1/RB2 | OPEN |
| G23 | Zone invalidation | Wick, close or acceptance beyond far edge | I1/I2/I3, same-bar priority | OPEN |
| G24 | Repeated touches | Contact episode reset, re-arm, expiry | Stable setup ID and explicit episode lifetime | OPEN parameters |
| G25 | RSI 50 bounce (L16) versus 40–50 (QA2) | Exact crossing/bounce grammar, scenario context | Separate continuation and scalp hypotheses | Context distinction established, thresholds OPEN |
| G26 | RSI70/30 | Overbought/oversold forecast meaning | Momentum-only unless extra evidence | Source caution established |
| G27 | EMA periods 9/20/50/100/200 in figures | Which periods/timeframes universally mandatory | Source/context-specific periods; no universal 9 | Source distinction established |
| G28 | Price above EMA + one-bar EMA slope | Apparent distinct confluence actually dependent | Algebraic equivalence under same close EMA | **Mathematically validated** |
| G29 | Flat/“angled” EMA | Non-invariant visual angle, slope horizon | k-bar, normalized, ATR-scaled alternatives | OPEN |
| G30 | All-timeframe bias | Different directions in same case | Scoped trend/momentum/timeframe statements | Source reconciliation established |
| G31 | HTF/LTF availability | Same-time boundary receipt and revised data | T0 freeze versus T1 decision-time, no backdating | OPEN native ordering; causal principle stable |
| G32 | Continuation versus range/scalp | No universal trade priority or style | Distinct scenario families; CONDITIONAL_CONFLICT | Experimental reporting principle |
| G33 | Stop “below”/“above” | Open inequality, exact tick buffer | Signed geometry and declared stop basis | Math stable, buffer OPEN |
| G34 | Next-zone TP versus 2R/3R | Incompatible nearby obstacle and fixed target | Explicit alternatives and target feasibility | OPEN policy |
| G35 | Leverage/margin (L05) | Fixed notional vs fixed collateral conflation | Separate position size, exposure, margin and equity | Mathematical correction |
| G36 | Fixed risk fraction | Source example vs general account-risk setting | Independent budget, sizing, precision, costs | No universally approved fraction |
| G37 | Stop and target execution | Slippage, gap, nonfill, partial exit, barrier order | Named plausible paths, abstain where OHLC path unknown | Open empirical evidence |
| G38 | Trailing TP plans | Trigger, adjustment, size and residual allocation | Explicit alternative policies, not assumed completed exits | OPEN |
| G39 | Perpetual cost and liquidation | Fee/funding schedule, mark, margin tiers | Product-specific assumptions and bounds | Requires qualifying evidence |
| G40 | “High probability”/“reliable” | No numerical win probability, calibration or return sample | Held-out source alignment and after-cost evaluation | **No empirical edge established** |
| G41 | Institutional accumulation/liquidity | OHLC not participant identity, not full order book | Qualitative labels with uncertainty, no verified actor | Inference limitation |
| G42 | Case study screenshots (L21/QAs) | Unshown 1H/15m evidence, venue/timestamp, hypothetical fills | Separate visible, textual assertion and independent inference | Incomplete evidence |
| G43 | Forex sessions and news (N01) | DST, crypto 24/7, news effect heterogeneity | Market-specific optional observation, not universal gate | Independent qualification |
| G44 | “BSP charting” (N02) | Heading entity mismatch | Plotted PSE:BPI distinct from BSP central bank | **Source identity corrected** |
| G45 | Manual annotations as truth | Independent human evidence and retrospective bias | Prospective blinded label protocol with abstention | Human pilot not completed |
| G46 | Rich rule combinations | Correlated features, selection bias, overfit | Simple comparator, ablation, walk-forward and holdout | Financial outcome OPEN |

## 17.1 Highest-consequence unresolved choices

The first category of open items concerns **logical correctness**, not parameter optimization: knowing the reference *before* using it, refusing impossible simultaneous intrabar histories, keeping the correct venue and product, valid signed long/short price geometry, and withholding classifications when essential evidence is missing. These should be non-negotiable scientific safeguards independent of any win-rate result.

The second category concerns **source alignment**: pivots and protected structure, R1 pre-breach/reset policy, OB color and displacement, FVG formation/mitigation, exact contact and same-bar versus later-bar confirmation, EMA/RSI contextual meaning, range confirmation-break triggers and scenario lifetimes. Two defensible interpretations can generate different historical candidates; one should not be selected because it produces attractive after-the-fact charts.

The third category concerns **financial utility**: after-cost expectancy, sensitivity to tick spread/funding, risk of gap liquidation, live filling, nonstationary volatility, sample-size uncertainty, multiple testing and degradation under out-of-sample market conditions. Strong performance claims remain unsupported by the educational PDF and logical case inventory.

---
# 18. Newer experimental methodological defaults and competing hypotheses

The repository's November 14 research-design checkpoint offers a concrete *candidate version* of an independently improved, **source-informed continuation analysis**. The owner approved the **broad direction**, not Coach provenance, a uniquely correct parameter choice, or profitable performance. The numerical details below are reported solely as **experimental methodology candidates**. They should not be read as instructions to implement anything on a particular platform.

## 18.1 Proposed four-scale continuation interpretation

A specific candidate organizes evidence into broad **4H structural context**, **1H intermediate structural assessment**, **15m known support/resistance location**, and a **5m completed directional reaction**. The broad context determines whether *continuation-long* or *continuation-short* should be evaluated. Opposing 1H structure may remain observable rather than becoming a hidden veto. A valid 15m pullback may oppose 4H structure, and a 5m reaction alone cannot convert 4H DOWN into UP.

This is a useful **testable profile**, but the original Coach corpus also explicitly contains 30m→5m scalp, 1H/5m ranges, daily/4H cases, countertrend scalp, and other conditional branches. Therefore the four-scale candidate is **not** the complete definition of Coach's system and should not eliminate those source cases.

## 18.2 Specific experimental assumptions under comparison

| Subject | November 14 candidate hypothesis | Alternative/falsification comparison |
|---|---|---|
| Swing extrema | Strict **2-left/2-right** local price pivots on consecutive, final observations | Compare **1/1**, **3/3** and directional-change candidates; estimate latency and missed structure |
| Pivot equality | Equal values disqualify the strictly compared side | Tick-tolerant and inclusive-equality alternatives |
| Pivot ordering | A dual high/low extreme cannot be chronologically ordered; reset/quarantine the attempted sequence | Compare same-side more-extreme retention; do not invent missing intrabar ordering |
| Regime | Four consecutive alternating eligible pivots; last high/low each higher for UP or each lower for DOWN | Manual labels, fewer/more pivots, mixed-versus-incomplete classification |
| Structural break | R1-A with previously armed frozen reference and new strict final-close crossing; one-time reference consumption | R1-B distinct reset/re-cross and complete-history comparator |
| S/R region | Band **one instrument tick** above/below a selected 15m confirmed pivot low/high | Percentage, volatility/ATR-normalized and human-marked S/R regions |
| Bullish confirmation | Immediately preceding final bearish candle plus current final bullish **real-body engulf**, current open \(\le\) prior close, current close **strictly greater** than prior open | Equality-inclusive EN-BODY, whole-range EN-RANGE, rejection+follow-through and strong-body alternatives |
| Bearish confirmation | Symmetric two-body bearish engulf at qualified prior resistance | Rejection/strong-body and contextual short variants |
| Zone contact and confirmation | Compare R2-B **same final candle** overlap+reaction with R2-A **later finished candle** | Strict evidence-known-before-reaction-onset version; compare delayed/missed cases |
| OB/FVG/Fibonacci/EMA/RSI | Initially **contextual observations**, not a mandatory confidence count | Study incremental benefit and delay before using any as a veto or bonus |
| Opposite directional candidates | Preserve separate scenario-level reasons; do not apply ungrounded majority vote | Compare simpler one-branch baseline and unanimity only as negative/sensitivity controls |

These thresholds are not evidence that **2/2 pivots** or **one tick around a structural price** is optimal across assets. One tick has dramatically different percentage and volatility meaning for different prices. A four-pivot sequence is a reproducible candidate definition, not identical to a human Coach swing scale. A strict current close beyond previous candle open changes edge-case classifications relative to equality-permissive engulfing, and therefore must be treated as a *particular selected experiment*, not as the only source reading.

## 18.3 Improvements that should survive model changes

The most durable research improvements are **procedural/epistemic rather than arbitrary numerical thresholds**:

1. **Preserve source attribution.** Coach teaches broad price-action logic; the research adds exact definitions where absent.
2. **Preserve original examples even when they challenge a simplified checklist.** A source long with RSI40–50 context should not be silently called invalid because another lesson used >50.
3. **Causal admissibility:** do not call future-selected levels known in the past. Delayed pivots, zones, EMA/RSI and candles become relevant only once their evidence exists.
4. **Acknowledge ambiguity:** two valid OHLC-compatible paths, a missing earlier bar, or unavailable source chart makes some decisions unknowable from the provided evidence.
5. **Reject logically impossible cases** rather than tune parameters to accommodate them.
6. **Keep context, setup readiness, nominal risk and actual execution separate.** A good-looking engulf is not a filled order, and a planned stop is not a guaranteed loss cap.
7. **Do not double-count derived evidence** or convert arbitrary confluence totals into invented probabilities.
8. **Require meaningful negative cases.** WAIT, invalidation and data insufficiency should have just as rigorous definitions as apparent long/short setups.
9. **Use simple, transparent baselines.** Complexity should earn its place by incremental, robust evidence rather than novelty.
10. **Retain distinct market products and source conditions.** Price differences and contract restrictions cannot be patched by assuming equivalence.

## 18.4 Important comparisons still unanswered

- Do manually marked Coach-like structural levels have better explanatory compatibility than symmetric fractal pivots, or do the latter reduce hindsight enough to justify missing some manual cases?
- Does allowing same-closed-bar touch+reaction (R2-B) improve source coverage without generating too many spurious contacts compared with later-bar R2-A?
- Are body-engulf, range-engulf, wick rejection + follow-through and strong directional candle equally useful within the same trend-zone context, or only in specific regimes?
- Does a “last opposite candle” OB add value beyond any-color predecessor and a simpler support/resistance location, despite its divergence from the source figures?
- Does a three-candle FVG add independent signal information after controlling for local volatility, recent impulse candles and nearby support/resistance?
- Does RSI momentum/EMA context provide an incremental after-cost advantage once price structure, location and reaction are already included?
- Are 4H/1H/15m/5m roles more robust than a source-specific 1H/5m or 30m/5m setup in volatile versus sideways periods?
- How does the relative value of a more restrictive filter change when accounting for **missed opportunities**, **signal delay**, **spread**, **funding**, and **sample size**, not just win fraction among trades left after filtering?

None of these comparisons is resolved solely by the educational PDF, a manually constructed scenario or acceptance tests of logical behavior.

---

# 19. Research evidence, falsification and validation standards: M07

## 19.1 A claim must name its actual evidence class

| Evidence class | What it can establish | What it cannot establish |
|---|---|---|
| **Original source inspection** | Coach's actual concepts, illustrations, prices, constraints and ambiguous wording | A mathematically unique rule or expected net profitability |
| **PCSS interpretation** | Clear teaching, exact source-vs-extension mapping, corrections and examples | Coach endorsement of independently invented rules |
| **Algebraic proof** | A mathematical identity under stated assumptions, such as one-bar EMA redundancy | Forward-predictive power or real account benefit |
| **Constructed paper case** | Logical consistency of a candidate event contract for particular specified inputs | That the candidate matches actual historical market behavior or that it is financially beneficial |
| **Controlled deterministic test** | A specified algorithm follows expected outputs for covered fixtures | Agreement with undisclosed discretionary Coach intent or all real-market states |
| **Frozen real-market observation** | Exact observed candles/contract fields for a qualified price feed at stated cutoffs | Authentic availability before a retrospective capture, order fills, or universal performance |
| **Independent human comparison** | Reproducibility/semantic agreement between properly isolated reviewers, if genuinely collected | True probability of profitable trades without outcomes and execution data |
| **After-cost historical study** | Conditional sample outcomes for a defined population, strategy and simulator assumptions | Guaranteed out-of-sample/live outcomes or precise fills without transaction evidence |
| **Live prospective fills** | Observed execution under the specific account, market and period | Invariant results across changing regimes, products or market depth |

**Do not upgrade evidence without the corresponding observation.** For example, 20 paper scenarios proving that a state machine refuses stale inputs are valuable logical tests; they are not twenty profitable trades. A reproducible price-bar checksum proves byte identity, not a unique interpretation of market structure.

## 19.2 Documented research audits and corrections

A November 12 independent repository/methodology review inspected the 26-study source ledger, methodological proposals and written cases. It raised multiple precise defects, including an impossible proposed strict-fractal example and ambiguous candle-time sequencing. Later reconciliation separated the corrected counterexamples, with original historical claims retained as audit history.

- **Invalid pivot example (AUD-C01):** a supposed strict pivot high 106 could not survive a required right bar closing 107. Correct distinction: pivot rejection versus valid pivot with late known structural regime.
- **Impossible self-high event (TIME-14):** a candle cannot exceed *its own final high*. The corrected version uses a separately timestamped price observation in a later bar before the reference becomes armed. Without ordered evidence, a later high alone does not establish an eligible crossing after arming.
- **Incorrect flat-versus-malformed candle (TIME-18):** a zero-range valid candle must have all four OHLC values equal; a “large directional green body with zero range” is impossible. Flat price data and invalid OHLC are separated.
- **Wrong-wick rejection (R3):** taking the *maximum* of upper and lower wick fractions incorrectly declares bullish rejection from a large **upper** wick near support. Directionally correct numerator is required.
- **Pre-arm history versus latest-close policy:** a reference previously breached and later returned before activation must be analyzed distinctly under R1-A and history-veto models; neither can silently retro-label the old price breach.
- **Same-closed-bar versus later-bar reaction:** both are plausible research choices with different coverage and latency. A stricter requirement that contact evidence was known *before reaction onset* is a third, more restrictive condition and should not be conflated with merely using a later candle.
- **Q&A3 source alternatives restored:** Coach's conditional bullish breakout criteria include 15m BOS, 1H BOS, **or** 1H close above the cited range; omitting two alternatives was a source-fidelity error.
- **Stable scenario identity:** contact/reaction evidence should attach to an existing setup, not retroactively define its historical origin/identity.

The above correctness fixes do not settle whether the resulting strategy is financially useful. They remove self-contradictions and unsupported attributions in the research specification.

## 19.3 Prospective structural-reference study: an important evidence limitation

The repository planned a 12-slot prospective human structural-reference annotation exercise with explicit time cutoffs, blinded/captured historical prefixes, structural reference roles, abstention rights and agreement criteria. The later recorded owner directive **cancelled that human pilot as a mandatory prerequisite before collection**. The ledger recorded **0 of 12 human captures/annotations** at that checkpoint. Therefore the research cannot honestly claim completed human inter-rater agreement or a validated discretionary “ground truth” from this exercise.

Separate structural-reference research and controlled cases tested internal consistency of proposed swing/reference models. Those checks support named logical outcomes within their evidence bounds, but they do **not** establish independent agreement with Coach's original discretionary judgments or any net strategy expectancy.

## 19.4 A credible future evaluation procedure, conceptually

1. **Freeze the research question in advance.** State exactly which uncertainty is being tested: source compatibility, logical correctness, reaction delay, missingness, or after-cost trade outcomes.
2. **Define the eligible population.** Instrument, exchange, contract, price basis, timeframe combination, date span, sessions and regime classification must be explicit.
3. **Separate benchmark classes.** Human source-like manual reference where available, simple causal comparator (e.g., prior swing, prior range extrema), and one or two more complex challengers.
4. **Predeclare parameters and event definitions.** Freeze pivot widths, equality rules, R1/R2 choices, contact method, candle definitions, stop/target policies, missing data treatment and observed-as-of time.
5. **Keep false positives, false negatives and abstentions.** A model that refuses every setup may be temporally “safe” but has zero useful coverage; a model that classifies every candle may be high-coverage and low-specificity.
6. **Use finite edge-case counterexamples first.** Equal highs, dual swings, unconfirmed HTF, missing candle, stale zone, same-bar invalidation, RSI/EMA warmup, incorrect price units, and opposing conditional branches.
7. **Evaluate matched real observations only after logical admissibility.** Exclude forming candles, fix session boundaries and verify source identity rather than mixing different market products.
8. **Choose held-out periods and walk-forward assessment.** Do not fit thresholds to the exact period later claimed as proof. Distinguish selection/tuning periods and evaluation periods.
9. **Account for executable economics.** Transaction costs, bid–ask, realized/product-specific funding, slippage, variable fills, minimum quantity/tick, liquidation/collateral and ambiguous stop/target path.
10. **Compare against simple baselines and ablations.** Determine whether RSI, EMA, extra zones or other features add information *beyond* structure, location and confirmation.
11. **Measure uncertainty.** Report numbers of eligible setups, qualifying cases, abstentions, total risk exposure, distribution of gains/losses, drawdowns and sensitivity to plausible execution and parameter assumptions. Avoid uncalibrated “high probability” tags.
12. **Preserve negative results.** A failed hypothesis, inconsistent human annotation or unobservable timing boundary is a research outcome, not something to erase to make a chart look decisive.

## 19.5 Practical falsification questions for every major module

| Domain | Example that should expose a weakness |
|---|---|
| Structural reference | Later evidence establishes a visually attractive pivot, but an alleged earlier BOS depended on it before confirmation |
| Regime classification | One lower high appears amid unresolved swings: falsely label established downtrend |
| Pivot arithmetic | Strict high survives a required right bar with a higher close: impossible |
| Zone construction | Future reactions tighten today's historical support so that an old candidate retrospectively improves |
| OB/FVG | A qualified “institutional” order block is asserted from candle geometry with no participant-level record |
| Fibonacci | Perfect retracement anchor is selected only after seeing the complete rebound |
| Candle reaction | Upper wick near support is mistaken for bullish lower-wick rejection |
| Candle validity | Flat candle is treated as malformed, or malformed OHLC treated as a tradable doji |
| Timing | Zone and candle become final together, but a model asserts an actual fill halfway through that candle |
| Timeframe context | A later 4H close is used to justify a 5m decision taken before that close existed |
| Conflict | Countertrend scalp automatically flips the higher-timeframe trend |
| RSI/EMA | EMA price-side and one-bar slope counted as independent votes |
| Risk | Long stop is above entry but absolute-value ratio looks attractive |
| Execution | A bar trades beyond both stop and target; result presumes target first without path evidence |
| Market identity | Historical Gold Spot support price is reused as an identical XAUUSDT or gold-token contract level |
| Performance | A chosen indicator stack outperforms only during the period used to tune its thresholds |

A methodology that cannot report **unknown** when evidence is genuinely missing is not more complete; it is less trustworthy. Conversely, abstention should itself be measured so conservatism does not conceal a strategy that rarely has a usable qualified event.

## 19.6 What has **not** been established

The repository's audited records do **not** furnish a statistically calibrated Coach win probability, a verified profitable after-cost track record, proof that every OB/FVG corresponds to real institutional liquidity, exact authenticated source-case fills, or a fully resolved single definition of every discretionary price-action term. The PCSS completeness audit covers **source study**, not closure of these methodological unknowns. The newer candidate numerical defaults are experiments until tested against predeclared observations and, separately, market outcomes.

---
# 20. Glossary, integrated principles and source bibliography

## 20.1 Trading terminology and precise research distinctions

| Term | Meaning in this reference | Important limit |
|---|---|---|
| **HTF / LTF** | Higher/lower timeframe providing context versus detailed reaction | No single Coach-mandated universal pair |
| **OHLC(V)** | Open, high, low, close (and optionally volume) for a defined interval and instrument | One bar does not expose exact within-bar event order |
| **HH / HL** | Higher structural swing high / higher structural swing low | A previous and current *eligible* comparable swing must be defined |
| **LH / LL** | Lower structural swing high / lower structural swing low | A single lower high alone is not necessarily a complete downtrend |
| **UP/DOWN/RANGE/UNKNOWN** | Proposed structural classification states | Not all cases lacking trend are ranges; unknown is an epistemic state |
| **BOS** | Coach's continuation break of prior eligible structural high/low in prevailing trend | Requires regime, reference and break semantics; not generic rolling breakout |
| **CHoCH / CHOCH** | Change of Character: possible shift after key contrary structural break | Not a guaranteed trend reversal or order |
| **Protected swing** | Research-selected structurally significant prior high/low whose break challenges current trend | How it is identified is not uniquely Coach-defined |
| **Pivot origin** | Historical interval where an extreme occurred | Different from the later time it becomes confirmed |
| **Reference arming** | First point a preknown structure/level may legitimately qualify a subsequent event | Independent causality concept; cannot backdate |
| **Consumed reference** | Already used level not allowed to emit the same new event repeatedly | Independent exact-once research policy |
| **Zone / S/R band** | Support/resistance as bounded region, not necessarily one exact price | Geometry/width/touch count need definitions |
| **Role reversal / role flip** | Previously broken support acting as possible resistance or vice versa | A break does not prove a successful later retest |
| **Supply / demand** | Qualitative selling / buying response region | A zone is not measured institutional inventory |
| **OB (Order Block)** | Coach: last candle before strong pump/drop; later reaction area | Last-opposite-candle method is an independent convention, not universal source law |
| **FVG (Fair Value Gap)** | Price imbalance/gap region considered for possible revisit | Three-candle inequalities are independent formalization, not unique source formula |
| **Displacement** | Strong directional price movement | Source lacks universal absolute/ATR/body threshold |
| **Fibonacci retracement** | Fractional return from a qualifying swing impulse | Source has two separate bands, 0.5–0.618 and 0.618–0.705 |
| **Hammer** | Small upper-area body, pronounced lower wick | Context and confirmation matter; no source ratio |
| **Shooting star** | Small lower-area body, pronounced upper wick | Context and confirmation matter; no source ratio |
| **Doji** | Small/near-zero body expressing possible indecision | Not a standalone BUY/SELL |
| **Engulfing** | Opposite-direction large candle covering prior candle by some chosen criterion | Body versus full range must be specified independently |
| **Rejection wick** | Price excursion away from a location followed by relative retracement within candle | Direction-relevant wick is essential; does not identify an actor |
| **Follow-through** | Later price/candle behavior supporting initial rejection | Timing and threshold unspecified by Coach |
| **Confirmation break** | Later trigger beyond an earlier completed confirmation reference in range case | Wick versus close alternative; distinct from L08 immediate-after-close workflow |
| **Confluence** | Several context factors aligning with one scenario | Correlated factors cannot be interpreted as independent win-probability multipliers |
| **RSI** | Relative Strength Index; momentum oscillator; Coach uses 14/30/50/70 as common reference | Contextual 40–50 scalp rebound differs from above-50 continuation |
| **EMA** | Exponential moving average describing smoothed price and possible dynamic S/R | Price-above-current-EMA and one-bar-upward-EMA are dependent for same close input |
| **RSI bounce** | Context-dependent recovery/hold from a region | No universal mathematical crossing/retest grammar supplied |
| **Trend continuation** | Scenario aligned to an established larger structural direction after pullback/reaction | HTF bias alone is not entry readiness |
| **Range reversal** | Scenario near established sideways boundary with directional reaction | L10 adds its own ambiguous confirmation-break step |
| **Countertrend scalp** | Shorter-horizon opportunity contrary to established larger trend | Not a declaration that HTF trend reversed |
| **Reversal watch** | Tracking possible structure change without claiming full reversal | Needs own-timeframe follow-up evidence |
| **Stop-loss (SL)** | Proposed protective exit level/order trigger | Intended price differs from guaranteed filled execution |
| **Take-profit (TP)** | Proposed reward objective, possibly multiple levels | No certainty target is reached/fills; portions must be specified |
| **R / RR / R:R** | Risk unit and reward relative to risk, ordinarily price-distance ratio when appropriately defined | Not account cash risk unless position units and costs added |
| **Margin** | Collateral associated with a leveraged exposure | Not equal to planned stop risk |
| **Leverage** | Relationship allowing larger exposure relative to collateral | Does not independently change P&L at a fixed linear quantity |
| **Notional** | Economic exposure from quantity × contract/price basis | Different from collateral and equity |
| **Funding** | Periodic settlement transfer for applicable perpetual positions | Requires actual product/rate/held-notional data |
| **Slippage / spread** | Realized execution difference / bid–ask crossing cost | Must not count the same adverse price effect twice |
| **Partial fill** | Less than requested quantity actually executed | Remaining order/position is unresolved exposure |
| **R1-A / R1-B / R1-C** | Frozen-reference crossing / reset-recross / manual anchor research variants | Not Coach-coded requirements or validated optimal policies |
| **R2-A / R2-B / R2-C** | Later-bar reaction / same-completed-bar reaction / genuine ordered finer-grained observation | Distinct clocks and no intrabar fill inference |
| **MTF-T0 / T1 / T2** | Open-time HTF context freeze / decision-time evidence / retrospective manual source context | Must report when each premise became known |
| **WAIT / INSUFFICIENT** | Await a missing source-style precondition / cannot establish necessary evidence | Neither implies market direction is false or true |
| **CANDIDATE_FOR_REVIEW** | Research description satisfying declared hypothetical gates | Never an executed trade or validated recommendation |
| **PCSS** | Personal Comprehensive Study Standard: source-order, rigorous explanation and verification discipline | Original private PCSS text is not in this public repository |

## 20.2 An integrated source-faithful reading of a hypothetical trade

The following is a **teaching sequence**, not a universal mechanical Coach checklist and not a live trade recommendation.

**First: identify the market and context.** Choose the correct instrument/venue/product and inspect meaningful higher-timeframe structure. Is the source-consistent reading uptrend, downtrend, range, local possible change, or not yet established? Do not let EMA or RSI alone relabel HH/HL and LH/LL structure. Record conflicts, not just the most attractive direction.

**Second: identify a justified location.** Mark a previous support or resistance region; optionally study separate OB, FVG, Fibonacci or EMA context if these were actually recognizable beforehand. Understand whether the contemplated style is trend continuation, range, countertrend scalp, pullback scalp or reversal watch. No contact with the intended zone means **NO TRADE** in L08's source workflow.

**Third: wait for a qualifying response.** Interpret lower-timeframe completed candles with their specific context. Coach permits bullish/bearish engulfing, rejection with its required follow-through, or a strong-body reaction in different source cases. The range case uses a later confirmation-break wording. A doji or an overbought RSI alone is not an entry. Note precisely what was observed and which definition was applied rather than treating ambiguous candles as certainties.

**Fourth: distinguish the new observation from a new trade.** A valid reaction may still need a later trigger, an independent risk proposal, or re-evaluation after changing higher-timeframe context. A CHoCH is a possible structural change, not a guaranteed full market reversal. In uncertain cases, WAIT/INSUFFICIENT is an analytical result.

**Fifth: test the loss and target separately.** For a hypothetical long, the proposed stop is below the relevant support/entry and the target above; for a hypothetical short, vice versa. Compare nearest structural obstacle with the alternative 2R/3R objective, then assess contract units, cash budget, costs and whether execution uncertainty can render the geometry unrealistic. A perfectly calculated nominal RR does not establish positive expected value without a valid conditional probability and fill model.

**Sixth: update with evidence without rewriting the past.** If context invalidates, a zone fails, a setup expires, or new data arrives, reassess current eligibility. Preserve the as-of logic of earlier assessments. Do not silently convert an earlier unknown condition into an old confirmed signal merely because later prices made the chart look obvious.

## 20.3 Study and recall summary: core ideas worth retaining

1. **Structure precedes labels.** HH/HL, LH/LL and meaningful prior references are more important than naming every passing wick a BOS.
2. **BOS continues; CHoCH suggests possible change.** A possible change is not the same as a confirmed new HTF trend.
3. **Trend, zone and reaction are distinct.** Their conjunction is source-like confluence, but the order matters.
4. **Location matters.** In L08, zone not reached means NO TRADE. A high momentum reading far from a reasonable location can justify patience.
5. **Confirmation is contextual and plural.** Engulfing is not the only pattern; rejection+follow-through and strong-body alternatives must remain.
6. **The same word can have scenario-specific conditions.** RSI >50 in continuation and a 40–50 bounce in a scalp are not universally contradictory.
7. **A range trade is a separate branch.** The L10 break-of-confirmation language should not overwrite the L08 after-close description.
8. **Countertrend does not mean new overall trend.** The SOL short and SOL long plans are separate and have different risks.
9. **OB, FVG, supply/demand and Fibonacci are potential locations, not verified institutional fills or independent probabilities.**
10. **Price above EMA and a one-bar rising EMA can be the same mathematical evidence.** Extra indicators are not automatically extra information.
11. **Wait for data that actually existed.** A level identified using future candles is not usable as if it were already known.
12. **Risk arithmetic requires context.** Price stop distance, cash risk, margin and executable exits are separate.
13. **An excellent hypothetical R:R can still lose after costs or low target-hit probability.** Coach's mathematical examples are not market win-rate estimates.
14. **Uncertainty must survive.** An incomplete historical Q&A is incomplete, not a license to fill in unshown candles.
15. **Independent improvement is permitted but must be falsifiable.** Exact research thresholds are not automatically Coach rules or established winning edges.

## 20.4 Bibliography — original source and PCSS records

Every relative repository path listed below is a direct source or evidence trail for this compilation. The GitHub links lead to the source documents and retain their original wording, technical detail and prior research decisions. In a few cases, newer experimental proposals live on a research branch rather than on `main` and are identified explicitly.

**Original Coach source and source-coverage control**

- [Original 35-page Coach PDF](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/sources/coach%20trading%20lessons.pdf)
- [Source manifest and provenance hierarchy](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/SOURCE_MANIFEST.md)
- [Full 26-unit coverage ledger](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/LESSON_COVERAGE.md)
- [Complete PDF-source study audit](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/SOURCE_STUDY_COMPLETION_AUDIT.md)
- [PCSS operational study protocol](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/PCSS_PROTOCOL.md)
- [Cross-lesson reconciliation](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/METHODOLOGY_RECONCILIATION.md)
- [Research and validation standards](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/RESEARCH_AND_VALIDATION.md)
- [Source-to-rule traceability](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/00-source-to-rule-traceability.md)
- [Decision register and provenance of owner research scope](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/DECISIONS.md)

**Full 21 PCSS studies and five supplemental studies**

The complete direct-link list, including original page numbers, appears in **Section 2** above. All 26 studies are individually included there. The present bibliography avoids repeating those full links but incorporates their companion research documents below.

## 20.5 Bibliography — lesson-specific research, in original source order

These are **independent research documents**, not additional Coach-authored lessons:

| Source unit / topic | Companion research document |
|---|---|
| L02 Candlestick candidates | [02 candlestick classification](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/02-candlestick-rule-candidates.md) |
| L03 R:R/compounding | [03 reward, expectancy and sizing](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/03-risk-reward-spec-candidates.md) |
| L04 Multi-timeframe knowledge | [04 causal timeframe research](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/04-multi-timeframe-causality.md) |
| L05 Leverage/margin | [05 solvency research](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/05-margin-leverage-solvency-candidates.md) |
| L06 Engulfing | [06 competing geometry](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/06-engulfing-formalization.md) |
| L07 Structure/confluence | [07 structural candidate rules](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/07-market-structure-confluence-candidates.md) |
| L08 Entry sequence | [08 location, reaction and risk](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/08-entry-state-machine-candidates.md) |
| L09 Support/resistance | [09 role reversal](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/09-zone-role-reversal-candidates.md) |
| L10 Range/confirmation | [10 range and confirmation-break alternatives](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/10-range-entries-and-confirmation-break.md) |
| L11 OB/BOS/CHoCH | [11 structural-zone research](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/11-order-block-bos-choch-candidates.md) |
| L12 BOS | [12 causal BOS events](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/12-bos-event-causality.md) |
| L13 Countertrend SOL | [13 countertrend and MTF risk](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/13-countertrend-risk-mtf.md) |
| L14 Fibonacci | [14 anchor and band hypotheses](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/14-fibonacci-candidate-specification.md) |
| L15 Confluence reliability | [15 feature dependence and ablation](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/15-indicator-reliability-confluence-ablation.md) |
| L16 Long/short continuation | [16 directional state alternatives](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/16-long-short-continuation-state-candidates.md) |
| L17 RSI | [17 momentum and RSI hypothesis](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/17-rsi-state-momentum-candidates.md) |
| L18 EMA | [18 mathematical redundancy and range filters](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/18-ema-slope-redundancy-range-candidates.md) |
| L19 Top-down RSI/EMA | [19 causal confluence research](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/19-topdown-timecausal-confluence-research.md) |
| L20 CHoCH | [20 confirmed-pivot change semantics](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/20-choch-confirmed-pivots-and-break-semantics.md) |
| L21 TON | [21 source-provenance and risk](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/21-tonusdt-topdown-case-provenance-and-risk.md) |
| Q&A1 BTC | [BTC MTF continuation and disconfirmation](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/qa-01-btc-mtf-continuation-retest-and-bearish-evidence.md) |
| Q&A2 FARTCOIN | [Pullback, RSI band and cash-risk differences](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/qa-02-fartcoin-scalp-entry-risk-and-rsi-band.md) |
| Q&A3 BTC | [Conditional short/rejection vs breakout long](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/qa-03-btc-conditional-retest-breakout-risk.md) |
| Note N01 sessions | [Crypto session, DST and news applicability](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/note-01-crypto-sessions-dst-and-event-risk.md) |
| Note N02 BPI | [BPI structure and cross-market interpretive limits](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/note-02-bpi-mtf-reversal-and-crypto-transfer.md) |

## 20.6 Bibliography — cross-lesson methodology and critical audits

**Nine foundational research specifications**

1. [M00/M01 causal market data, pivots and structural breaks](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/01-causal-market-structure.md)
2. [M02–M06 top-down entry, alternative confirmation and risk](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/02-topdown-entry-state-and-risk.md)
3. [M02 support/resistance, OB, FVG, Fib](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/03-zones-sr-ob-fvg-fibonacci.md)
4. [M01 R1 structural references and arming corrections](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/04-reference-arming-and-pivot-order.md)
5. [M02/M04/M05 R2 contact, reaction and time](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/05-zone-contact-reaction-timing.md)
6. [M04 R3 candle and confirmation grammar](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/06-candle-pattern-and-confirmation-grammar.md)
7. [M05 R4 contextual states and timeframe conflicts](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/07-mtf-context-conflicts-and-causal-states.md)
8. [Cross-domain causality and stable setup lifecycle](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/08-cross-module-causal-reconciliation.md)
9. [M06 risk, margin, execution and outcome uncertainty](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/methodology/09-m06-risk-and-execution-uncertainty.md)

**Counterexamples, falsification and frozen research evidence**

- [Phase 2 causal reconciliation paper cases](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase2-causal-reconciliation-paper-cases.md)
- [Phase 2 frozen-prefix evidence and its limitations](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase2-frozen-prefix-evidence-v1.md)
- [Phase 2 causal timing assessment](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase2-frozen-prefix-timing-assessment.md)
- [M06 bounded public market metadata](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase2-m06-binance-public-metadata.md)
- [M06 paper cases and exact endpoint arithmetic](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase2-m06-paper-cases.md)
- [M07 frozen market-evidence scope](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase2-m07-frozen-market-evidence.md)
- [M07 validation and falsification protocol](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase2-mtf-validation-and-falsification-protocol.md)
- [Strict structural reference comparisons](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase3-6-structural-reference-contract.md)
- [Structural reference adjudication/counterexamples](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase3-6-structural-reference-adjudication.md)
- [Uncollected human annotation pilot and evidence limitations](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/research/phase3-6-prospective-annotation-collection.md)
- [Independent November 12 methodology review](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/audits/2026-11-12-independent-repository-and-methodology-review.md)
- [Early pre-reconciliation audit](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/audits/2026-11-10-phase2-preimplementation-audit.md)
- [November 11 causal timing reconciliation](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/audits/2026-11-11-causal-timing-reconciliation.md)
- [November 11 evidence-gate consistency audit](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/audits/2026-11-11-m05-evidence-gate-consistency-audit.md)

**Newer experimental research baseline (not Coach source)**

- [November 14 experimental continuation-method specification at its reviewed research commit](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/e282ae19a46dfa405992b006f0706819e01ddcf8/docs/product/v1-1-candidate-specification.md), especially its section on experimental assumptions. Only the **methodological** substance is included in this master; platform implementation and product details are intentionally excluded.
- [Research decision history](https://github.com/jebobomagcode/alpha-engine-tradingview/blob/main/docs/DECISIONS.md), including the principle that Coach source is the foundation but independently improved hypotheses are allowed, with explicit origin labels and no guaranteed-profit claims.

## 20.7 Source coverage and exclusions declaration

**Included:** complete ordered coverage of all **21 numbered Coach lessons**, **3 Q&A activities** and **2 final notes**; operational PCSS study standard; source examples and exact price/RSI/EMA numbers where recoverable from the repository; all cross-lesson methodology domains M00–M07; R1–R4 rule competitors and mathematical corrections; experimental new structural/zone/candle defaults; risk and cost research; source-to-gap register; validation principles; direct links to the relevant research corpus.

**Explicitly excluded at user request:** platform-specific instructions, scripts, development frameworks, interfaces, code, product engineering, release procedure, deployments and alerts. The reference is solely about the **trading methodology, interpretation, risk and independent research**.

**Residual completeness limitation:** the original *private* comprehensive PCSS file is not in the public repository, so this consolidation uses its documented operational protocol and all 26 completed source studies rather than claiming a verbatim reproduction. The original PDF's images were audited at the repository's earlier PCSS checkpoints; this current consolidation relies on those records and retrieved documentation rather than asserting a new independent page-by-page image reinspection. Repository files in active research branches can evolve. This is a **dated single-document synthesis**, not a proof that every draft, historical comment or future revision has been exhausted.

**Final epistemic conclusion:** Coach's central principle is **context → structurally meaningful location → patient confirmation → controlled risk**. The repository's strongest independent contributions so far are **source reconciliation, exact temporal causality, mathematical correctness, traceable uncertainty, scenario separation, and realistic risk/validation discipline**. Deterministic details that remain experimentally selected must not be called original Coach rules; neither source study completeness nor logical validity establishes a profitable trading edge.

---

*End of research consolidation — November 14, 2026 (Asia/Manila).*
