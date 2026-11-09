# PCSS Lesson 09 — Support & Resistance

**Status:** COMPLETE — original PDF page 11 inspected visually and as native text; full source-order teaching delivered, original chart inventoried, independent explanation and design research recorded (2026-11-09, Asia/Manila).  
**Primary Coach source:** [coach trading lessons.pdf, page 11](../../sources/coach%20trading%20lessons.pdf), the **sole Coach-origin source**.  
**Original PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`.  
**Original PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`.  
**Scope:** crypto-oriented eventual TradingView research (including XAUUSDT, XAUTUSDT, PAXGUSDT as distinct venue-qualified products); original lesson fully studied irrespective of asset examples.  
**Implementation state:** zero Pine scripts, tests on market data, strategy backtests, alerts, live orders or deployments.

## Page 11 source-order coverage audit

The full original page was rendered from the 35-page source at 2.2x zoom and visually inspected; the PDF native text was extracted and checked. A **single large upper-page chart image** contains horizontal green support and red resistance bands and repeated touches/rejections; the remaining source text includes headings and colored bullets. There are **no original numerical price labels on the diagram, original formula, proof, assigned exercise or historical trade performance claim**. The study does not treat the figure as a documented crypto dataset.

| ID | Source element in displayed order | Verified and explained |
| --- | --- | --- |
| 09-F1 | Top-page chart image: green horizontal SUPPORT strip along repeated swing troughs, red RESISTANCE strip near repeated swing highs, 4 green upward and 4 red downward arrows, candles oscillating within/near the bands, a right-edge upward candle reaching/potentially piercing the resistance region | Audited; no numeric price labels, timeframe, venue, asset identity, or measured outcome; no assumption that all touches held |
| 09-01 | Heading “09. SUPPORT & RESISTANCE” and red marker “SUPPORT & RESISTANCE” | Covered |
| 09-02 | Green “SUPPORT” bullet; “floor price” | Covered |
| 09-03 | Decline often stops around support | Covered; not guaranteed |
| 09-04 | Buyers enter around support (Coach's narrative) | Covered; not proof of order flow identity |
| 09-05 | Price usually rises after such support interest (Coach's description) | Covered as qualitative generalization only |
| 09-06 | Red “RESISTANCE” bullet; “ceiling price” | Covered |
| 09-07 | Rise often stops around resistance | Covered; not guaranteed |
| 09-08 | Sellers enter around resistance (Coach's narrative) | Covered; not proof of order flow identity |
| 09-09 | Price usually falls after such resistance interest (Coach's description) | Covered, no numerical probability attached |
| 09-10 | “SIMPLE WAY TO REMEMBER”: support = BUY area (below), resistance = SELL area (above) | Covered as location shorthand, NOT automatic order |
| 09-11 | Broken support can become resistance | Covered; break threshold and retest not specified |
| 09-12 | Broken resistance can become support | Covered; break threshold and retest not specified |
| 09-13 | “Always remember”: buy at support and sell at resistance only WITH confirmation (engulfing/rejection/etc.) | Covered; connected to Lessons 06–08 |

**Provenance:** The drawing illustrates a horizontal trading range with repeated touches; it does not establish exact support/resistance calculation rules, instrument-specific viability, a numeric success rate, or deterministic breakdown/breakout detection. The closing bars reaching the upper zone are noteworthy, but their later outcome is unknowable from the image.

## 1. Coach's SUPPORT definition and meaning

**COACH_EXPLICIT:** Support is like a price floor; price declines often stop there, buyers enter, and the result is usually an upward movement.

**PCSS interpretation:** “Floor” refers to a *region previously associated with downward-price reactions*, not an absolute lower bound. In the original chart, four green arrows indicate returns toward a lower horizontal band, followed in several places by rising bars. The green band gives visual evidence that Coach imagines *a zone with finite height*, not simply a mathematical point.

**INDEPENDENT QUALIFICATION:** OHLC candlesticks show market prices, not which traders are buying, their intent, or a guarantee of continued demand. If market conditions change, support may fail. The words “usually” and “buyers enter” are explanatory/qualitative, not measured statistics. We should not infer a precise conditional success probability.

## 2. Coach's RESISTANCE definition and meaning

**COACH_EXPLICIT:** Resistance is a price ceiling; upward moves frequently stop there, sellers enter, and price tends to fall.

**PCSS interpretation:** In the original illustration, a horizontal **red band** is tested near multiple peaks marked by four red down arrows. Declines then appear in several illustrated sequences, but the right edge also shows an upward candle reaching or moving beyond the band. **A resistance band is not impermeable**.

**INDEPENDENT QUALIFICATION:** “Seller enters” is a conceptual description, not direct exchange order-flow evidence. Candle shadows can pierce band edges before closing back inside. Similar-looking historical tests do not guarantee rejection next time.

## 3. Original memory aid

**COACH_EXPLICIT, source wording:** “Support = BUY area (sa baba)” and “Resistance = SELL area (sa taas)”.

**Interpretation consistent with Lessons 07–08:** An *area to evaluate BUY or SELL setups*, not an instant BUY/SELL order. The current price and relevant trade direction matter. HTF trend/bias, prior-known zone, lower-timeframe confirmation, and risk controls are needed. Coach's latest wording explicitly says to trade at those areas **only with confirmation**.

**Important cross-lesson ambiguity:** Lesson 07 states sideways regimes should generally be avoided except for suitable higher-timeframe context, and Lesson 08 requires a directional HTF bias. Yet the illustration in Lesson 09 shows an extended horizontal range. The source does not resolve if range-bound BUY/SELL examples override the directional-bias requirements. Thus *the illustration explains what zones look like; it does not unambiguously approve countertrend or sideways execution*. Preserve this uncertainty for later study.

## 4. Level-role reversal: support -> resistance / resistance -> support

**COACH_EXPLICIT, page 11:** “Pag nabasag ang support-nagiging resistance” and “Pag nabasag ang resistance-nagiging support.”

**Interpretation:** If price breaks below a previously supportive region, market participants may subsequently treat it as an upper barrier when price rallies. Conversely, if price breaks above old resistance, the region may act as a lower support area on a future retracement.

**CRITICAL INDEPENDENT QUALIFICATION:** A level flip is a *candidate change of market role*, not a guaranteed law. The page does NOT formally define:
- whether "nabasag" means wick penetration, a candle close outside, a sequence of closes, or a threshold measured in ticks/ATR;
- whether a retest is required;
- how much movement outside the band constitutes a breakout;
- whether immediately piercing the opposite side invalidates the flip;
- whether the flip is active before a first retest or only after observed rejection;
- what happens if support and resistance overlap or both are broken rapidly.

A short-lived wick penetration and a multi-candle breakout might be classified differently by different algorithms. This is a principal unresolved decision, not a license to hardcode one definition as Coach-origin.

## 5. Complete illustrative price-zone example — independent, not source data

Let a hypothetical USDT-quoted crypto market have previously identified **support** zone \(Z_S=[100,102]\) and **resistance** zone \(Z_R=[110,112]\). These values are made up for teaching and do not describe an actual XAU, BTC or PAXG price chart.

**At support:** Suppose a bar's interval is \(L=101,H=105,C=104\). It intersects the band but closes above; this is a potential *contact and reaction*. It is not yet a Coach-aligned BUY without independent HTF trend context and an acceptable closed LTF confirmation event.

**Wick-only breakdown:** Suppose a subsequent bar reaches \(L=99.5\), but closes at \(C=102.5\). It pierced below the zone while closing above. A wick-break rule would classify penetration; a close-below rule would not. Coach provides no choice here.

**Close-below breakdown:** Suppose a later bar instead closes at \(C=98\), below the \(100\) lower boundary. That would qualify under a hypothetical close-beyond-zone rule, but a *confirmed resistance flip* still might require further events under an independent design.

**Possible retest:** If price later rallies toward \([100,102]\) from below and then rejects, the old support region *may* function as resistance. Requiring this retest is a proposed independent validation option; Coach's page does **not** explicitly require it.

**Resistance flip:** Similarly, a sustained or closed breakout above \([110,112]\), potentially followed by a pullback and support reaction, could suggest a resistance-to-support transition. No quantitative policy is established by the source.

### Mathematical zone-contact alternatives, not from Coach

Let zone \(Z=[a,b]\), where \(a\le b\), and a completed ordinary candle have \((O,H,L,C)\).

- **Any high-low overlap:** \(L\le b\land H\ge a\).
- **Close inside:** \(a\le C\le b\).
- **Real-body overlap:** \(\min(O,C)\le b\land\max(O,C)\ge a\).
- **Break below by closing price:** \(C<a\); **break above:** \(C>b\) (only candidate interpretation).
- **Wick break below:** \(L<a\); **wick break above:** \(H>b\) (different candidate).

A price bar can contact via wick without body overlap or a close in-zone. The rules yield different outcomes; thresholds and edge equality need to be tested rather than selected by intuition.

## 6. Confluence and confirmation — Coach's final reminder

**COACH_EXPLICIT:** Trade from support/resistance **“basta may confirmation (engulfing/rejection and etc.)”**.

**Cumulative methodology:** 
1. HTF trend and zone context from Lessons 04, 07 and 08.
2. A zone must be established and then contacted before seeking confirmation (Lesson 08); otherwise NO TRADE.
3. LTF confirmation may be engulfing (preferred), rejection + follow-through, or large body (Lesson 08). Lesson 09 repeats engulfing/rejection examples but **does not delete** the alternative strong candle.
4. Evaluate after confirmation candle closes, entry, SL outside appropriate zone, TP structural or 1:2/1:3 planned RR, realistic costs and position risk.
5. Changed/broken zones may need reassessment or role reversal; no automatic flip trade without a confirmation event.

**No numeric trading edge has been proven.** A horizontal range example does not override the source's previous caution about sideways regimes.

## 7. Independent Ponder: candidate engineering decisions

Read separate [zone research candidates](../research/09-zone-role-reversal-candidates.md). No algorithm is locked:
- **Manual/owner-supplied levels:** high source transparency, difficult automation and subjective reproducibility.
- **Confirmed swing cluster bands:** causal pivot levels, clustering/width rules, significant confirmation delay, correlated trend/zone inputs.
- **Rolling/volatility-scaled extrema:** causal and more automatic, risk of unstable zone width, false touches and noisy assets.
- **Break/flip state machine:** classify zone as active, challenged, broken/provisional, candidate flip, retested/validated or invalidated, with explicit known-at times.
- **Evaluation:** predeclare zone creation and contact mechanics, compare to simple previous-high/previous-low reference, test historical/live alignment, false breakouts, number of touch observations, signal latency, fees and out-of-sample outcomes.

**TradingView source, external not Coach:** 
- [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/), particularly historical pivot labels plotted before confirmation.
- [Lines and boxes](https://www.tradingview.com/pine-script-docs/concepts/lines-and-boxes/): tools for plotting actual zones, with drawing limits and ID management.
- [Strategies](https://www.tradingview.com/pine-script-docs/concepts/strategies/): lookahead-bias and execution simulation caveats.

Zone drawings must distinguish *where the historical pivot occurred* and *when the zone became knowable*. A visually backdated zone is not proof that a trader could have acted on it at that point.

## Coverage conclusion

- Full original **page 11** examined visually and native PDF text read; all support, resistance, mnemonic, two role-reversal statements and confirmation closing reminder addressed.
- The single image (both shaded horizontal bands, repeated arrow-marked tests, green/red candlesticks) described and critiqued.
- No source price examples, chart timeframe, formal quantitative threshold or separate exercise to reproduce.
- All equations and invented prices labeled **independent**; no unsupported statistical probabilities or forecast claims.
- **Lesson 09 COMPLETE as a source-based PCSS study only.** **Next:** Lesson 10 — Marking a Support and Resistance on a Time Frame (PDF pp. 12–13), with Coach's **actual numerical** support/resistance zones and buy/sell examples. Do not skip those actual figures/numbers, and do not start without owner instruction.
