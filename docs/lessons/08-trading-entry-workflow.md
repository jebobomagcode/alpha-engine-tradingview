# PCSS Lesson 08 — Trading: Source-Grounded Decision Workflow

**Status:** COMPLETE at source-study level, 2026-11-09 (Asia/Manila). Original text in page order audited, teaching delivered, independent mathematical examples checked, open formalization issues recorded.  
**Primary Coach source:** [coach trading lessons.pdf, original PDF page 10](../../sources/coach%20trading%20lessons.pdf). This is the **sole** Coach Fredy-origin source.  
**PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`.  
**Original PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`.  
**Project scope:** Crypto, including separate XAUUSDT, XAUTUSDT and PAXGUSDT products. No older project used or modified.  
**Implementation status:** ZERO Pine scripts, chart validation, executable strategy rules, backtests, deployments or orders.

## Source audit — every element in original page order

The exact PDF's page 10 was rendered at high resolution and inspected visually against native extracted text. The original page is **textual only**, with circular red section markers, a red heart summary marker, and no original chart photograph, drawing, table, formal exercise, theorem, worked numerical trade or numerical stop buffer.

| ID | Original Coach source statement or element | Coverage and source limit |
| --- | --- | --- |
| 08-01 | Heading “08. Trading”; “BEFORE ENTERING A TRADE” | Covered |
| 08-02 | Check HIGHER TIMEFRAME such as **1H/4H** first | Covered; coherent with Lesson 04 |
| 08-03 | Find support and resistance | Covered; no exact zone algorithm |
| 08-04 | Mark highs/lows; if uptrend, higher high/higher low; if downtrend, lower low/lower high | Covered; swing algorithm undefined |
| 08-05 | Identify valid trading places; “Wag po entry ng entry”; “SAFE” entry area | Covered; "safe" is Coach's qualitative label, NOT guaranteed financial safety |
| 08-06 | Directional bias: uptrend -> focus buy, downtrend -> focus sell | Covered; not an immediate order |
| 08-07 | WAIT until price reaches designated support/buy or resistance/sell zone | Covered; source does not define contact as wick, body or close |
| 08-08 | If price does not reach zone -> **NO TRADE** | Covered; hard Coach gate |
| 08-09 | Only after reaching the zone, move to LOWER TIMEFRAME | Covered; no explicit restatement of 5m/15m in page 10 (the values are in Lesson 04) |
| 08-10 | At LTF, look for a bearish/bullish engulfing candle, “best” | Covered; geometry thresholds from Lesson 06 unresolved |
| 08-11 | Alternatively, long-wick rejection **+ follow-through candle** | Covered; two-part sequence, no size/direction/delay rule |
| 08-12 | Alternatively, a strong large-body candle | Covered; "malaki ang body", quantitative threshold absent |
| 08-13 | “no need 3 candles; 1 strong confirmation is enough” | Covered; do NOT misread as requiring exactly one physical candle for every confirmation type |
| 08-14 | Entry **after confirmation candle closes** | Covered; event time is not synonymous with execution fill price |
| 08-15 | Stop loss: above resistance for sell, below support for buy | Covered; margin, tick buffer, wick/body and zone invalidation undefined |
| 08-16 | Take profit: next support/resistance **or** 1:2 / 1:3 risk-reward | Covered; source offers alternatives with no specified priority if they conflict |
| 08-17 | Closing five-step recap in order: (1) S/R, (2) HTF trend, (3) wait zone, (4) engulfing/confirmation LTF, (5) entry + SL + TP | Covered exactly in source order |

The prose first walks through the HTF trend and S/R together; the final numbered recap lists support/resistance first, then HTF trend. Both original orderings are preserved rather than artificially harmonized.

## 1. HTF preparation: context before action

**COACH_EXPLICIT:** Start with 1H or 4H, identify support/resistance and structure highs/lows, determine the price bias; focus buy in uptrend, sell in downtrend.

**PCSS interpretation:** Trend answers direction, zone answers where a potentially relevant reaction may occur. Those conditions guide *attention*, not immediate entry. Original Coach's phrase “SAFE mag entry” should mean a preferred *methodological location*. It does **not** mean no losing trades are possible. Actual market price can break support and resistance.

**Prerequisite links:** Lesson 04 assigns HTF context versus LTF entry. Lesson 07 introduces HH/HL vs LH/LL and trend/zone/engulfing confluence. Neither Lesson 08 nor earlier source fixes the required pivot strength, time of confirmation, HTF disagreement precedence, or exact zone boundary.

## 2. Zone first; absence of contact = NO TRADE

**COACH_EXPLICIT:** After marking trend/zone, WAIT for price to reach the preidentified zone; **“if hindi po umabot NO TRADE.”** Once price arrives, *then* go down to lower TF to seek confirmation.

**INDEPENDENT ENGINEERING PROPOSAL:** This is a sequence/temporal-gating condition, not merely a score. A potential LTF engulfing at a random unrelated price must not be classified as source-aligned. Distinguish `WAIT_ZONE`, `ZONE_CONTACT`, `WAIT_CONFIRMATION`, `SETUP_CANDIDATE`, `NO_TRADE`, and `INSUFFICIENT_DATA`.

**Gap:** Zone contact might be defined by high-low interval intersecting a zone, candle close inside, body overlap, or a price tolerance. Each can produce different signal counts. None is provided here. The zone must be known *before* contact; drawing it from a future pivot and backtesting earlier entries is invalid.

## 3. Coach's three **alternative** confirmation patterns

**COACH_EXPLICIT, original order:**
1. Bullish or bearish engulfing ("best").
2. Long-wick rejection PLUS a follow-through candle.
3. One strong candle, large real body.

He adds: no need for three confirmation candles, one strong confirmation is sufficient.

**IMPORTANT SOURCE INTERPRETATION:** He is discussing **one qualifying confirmation event**, not stipulating that each permitted *pattern* uses exactly one chart candle. Engulfing normally uses two adjacent candles (Lesson 06). Rejection + follow-through requires observation of a later candle. A large single candle can qualify as one-bar morphology. Do not silently require all three types, and do not collapse wick+follow-through into a single-candle rule without evidence.

The PDF does not specify: wick-to-body ratios, how far engulfing extends, which candle counts as follow-through, whether it must close beyond the rejection high/low, large-body ATR/range threshold, how many bars may elapse, or objective confirmation strength.

**Confluence nuance:** Lesson 07 says trend+zone+engulfing yields “high probability” setups, while Lesson 08 presents engulfing as **preferred**, with other confirmation alternatives. For the **full methodology**, Lesson 08 expands the accepted confirmation possibilities; do not silently make engulfing mandatory if another qualifying confirmed reaction is permitted. The financial probability remains unmeasured.

## 4. Entry after the confirmation candle close

**COACH_EXPLICIT:** "After confirmation candle closes."

**INDEPENDENT TEMPORAL AUDIT:** A forming candle may appear strong, then reverse. The decision cannot be retroactively treated as available before the confirmation close. In strategies, a signal generated on bar close is NOT automatically filled at that exact close. Official TradingView documentation describes broker emulator default next-available-tick fills after order creation:
https://www.tradingview.com/pine-script-docs/concepts/bar-states/
https://www.tradingview.com/pine-script-docs/concepts/strategies/

Distinguish:
- zone contact timestamp;
- final confirmation bar-close timestamp;
- order decision/creation timestamp;
- hypothetical or actual execution fill timestamp and fill price.
Only verified, causally available HTF data may count for a retrospectively shown LTF signal. Do not invoke `barstate.isconfirmed` inside `request.security()` as an HTF confirmation solution; see TradingView docs.

## 5. Stop loss and target: original vs independent risk math

**COACH_EXPLICIT:** Sell stop above resistance; buy stop below support. Profit objective at **next support/resistance OR 1:2 / 1:3 RR**. No fixed buffer, position sizing method, fill model, or precedence among structurally versus RR-determined targets is specified.

**Original concepts connected:** Lesson 03 risk:reward arithmetic and Lesson 05 leverage/margin mechanics. A potential zone-based entry is not mechanically or financially safe.

### Independent hypothetical BTCUSDT example — no live chart

Suppose:
- Previously identified HTF uptrend and support zone 99,800–100,000 USDT, established before price approaches;
- LTF price contacts the support and later closes a directionally appropriate qualifying confirmation (not numerically defined by Coach);
- illustrative entry \(E=100{,}100\) USDT after close, stop \(S=99{,}750\) USDT, i.e. below the example support band.

Gross price risk per unit:
\[
R=E-S=350\ \mathrm{USDT}.
\]
A hypothetical 1:2 target for this long is \(T_2=E+2R=100{,}800\) USDT; a 1:3 target is \(T_3=E+3R=101{,}150\) USDT. These are **independent mathematical teaching calculations**, not actual Coach source trades or market advice.

**Conflict case:** Suppose next confirmed resistance is \(100{,}450\) USDT; the zone target offers reward of \(350\) USDT and gross reward/risk = 1, not 2. The 1:2 target lies beyond that prior resistance. Coach offers "next level" **or** fixed RR but does not prescribe choosing farther RR regardless of obstruction, filtering based on minimum RR, or profit-taking in parts. This is **OPEN_UNRESOLVED**; never resolve by fabricated source attribution.

**Execution caveats:** Slippage, fees, spread, funding (where relevant), tick/step sizing, contract multiplier and stop order gaps can change realized loss and RR. Stop orders are not guaranteed maximum-loss caps in all market conditions. For XAUUSDT derivatives vs XAUTUSDT/PAXGUSDT token markets, product metadata must be distinct.

## 6. Original closing summary (preserved)

Coach's final numbered list is:
1. Support and resistance.
2. HTF trend.
3. Wait for zone.
4. Engulfing or confirmation on LTF.
5. Entry + SL + TP.

The complete workflow is a **gated decision process**, not a collection of independent BUY/SELL triggers.

## 7. Independent Ponder critique and falsification

- **SAFE is not risk-free:** prefer "PREFERRED ZONE" or "Coach-qualified area" to a financial safety assertion in the eventual UI.
- **Contact uncertainty:** Must choose objective wick/body/close/proximity rule, preserve known-at time and support/resistance validity; no hidden retroactive zone drawing.
- **Confirmation ambiguity:** "one strong confirmation" is one *confirmation event*, which may involve multiple bars. The three offered options are alternatives, not a requirement to observe all three.
- **Target conflict:** An S/R target can yield only 1R while 2R lies behind another obstacle. Source does not define priority; test competing policies, rather than assuming max reward is safer.
- **Entry latency:** Bar-close signal versus actual fill after the close; assuming a same-close ideal fill is an avoidable backtest distortion.
- **Signal selection bias:** This checklist may *reduce frequency* without improving conditional performance; use ablation comparisons in multiple crypto/gold markets.
- **Scope:** Preserve the original Coach baseline, clearly label independent additions and measure actual after-cost outcomes before assigning any probability.

## 8. Proposed future state transition, not implemented

`INSTRUMENT_OK → HTF_STRUCTURE_AND_ZONE_AVAILABLE → BIAS → WAIT_ZONE → ZONE_CONTACT → LTF_WAIT_CONFIRMATION → CONFIRMATION_CLOSED → ENTRY_RISK_REVIEW → RESEARCH_CANDIDATE`

Possible blockers: `NO_VALID_ZONE`, `HTF_CONFLICT`, `PRICE_NOT_AT_ZONE`, `ZONE_INVALIDATED`, `WAIT_CONFIRMATION`, `FORMING_CANDLE`, `ENTRY_PRICE_UNKNOWN`, `SL_OUTSIDE_RULE_UNVERIFIED`, `TP_POLICY_AMBIGUOUS`, `RISK_UNACCEPTABLE` (if policy later established), `INSUFFICIENT_DATA`.

These are *design proposals*, not Coach's literal labels or approved software code.

## Verification and checkpoint

- Source page 10 manually inspected as rendered original and native text; **17 audited item rows**, all complete.
- All three confirmation variants, explicit NO TRADE gate, after-close entry condition, both SL side placements, and either/or TP choice retained.
- Hypothetical arithmetic \(R=350\), \(T_{2R}=100800\), \(T_{3R}=101150\), next resistance yields 1R independently recomputed.
- No original diagrams, calculations or exercises were present or omitted.
- The five-step recap and its slight order variation relative to introductory prose both preserved.
- **Lesson 08 COMPLETE for PCSS teaching and research specification, not software implementation.**
- **Next:** Lesson 09 — Support & Resistance, original PDF page 11, only when the owner advances.
