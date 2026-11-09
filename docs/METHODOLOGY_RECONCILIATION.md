# Phase 2 — Cross-Lesson Reconciliation Register (research v0.1)

**Scope:** PDF original text plus existing 26 unit studies; not an implementation or a definitive set of automated rules. 2026-11-09 Asia/Manila. [Master traceability](methodology/00-source-to-rule-traceability.md). Every OPEN entry must remain unresolved until a named experiment/technical decision qualifies it.

| ID | PDF evidence and source wording/topic | Material reconciliation | Rule disposition and priority |
|---|---|---|---|
| R01 | Lesson07 p9 sideways: avoid unless HTF considered; Lesson10 pp12–13 sideways 1H Gold Spot range with conditional BUY/SELL | These can coexist as different trade *branches*, not a global contradiction to erase | OPEN: trend-following baseline vs explicitly documented conditional range model; **HIGH** |
| R02 | Lesson07 p9 valid confluence gives engulfing; Lesson08 p10 allows engulfing OR long-wick rejection+follow-through OR strong body and says “1 strong confirmation enough” | Engulfing is a preferred example, not universally mandatory across all lessons | Research alternatives keep source presets distinct; **HIGH** |
| R03 | Lesson08 p10 states zone never reached → NO TRADE and entry after confirmation candle closes | Must distinguish bias from source-style entry eligibility and decision time from fill time | Adopt as source sequence invariant *for Lesson08-style setup*, no always-on order; **CRITICAL** |
| R04 | Lesson12 pp15–16 BOS above prior HH/below prior LL; Lesson20 p25 CHoCH above prior LH/below prior HL | Both depend on prior actual trend and known structural swing reference, not a simple arbitrary rolling high | M01 conditional structure foundation; **CRITICAL** |
| R05 | Lesson20 p25 CHoCH “possible” reversal; N-02 p35 4H possible bounce, Daily no CHoCH | Local momentum shift cannot mechanically reclassify weekly/daily regime | Separate timeframes, possible vs confirmed; **CRITICAL** |
| R06 | Lesson16 p21 RSI bounces above50 in continuation example; Q&A2 p31 Coach says RSI bounce 40–50 for scalping | Context-specific trigger; strict universal RSI>50 LTF requirement would exclude Q&A2 | M03 multiple hypothesis definitions, none universally source-certified; **HIGH** |
| R07 | Lesson14 p19 repeatedly 0.5–0.618 Golden Zone, later manually add0.705 and watch0.618–0.705 | Distinct source windows, not one single 0.5–0.705 range | M02 keep two selectable research candidates and no unverified averaging; **HIGH** |
| R08 | Lesson18 p23 common EMA20/50/200; Q&A1 p29 EMA20/50/100/200; N-02 p34 settings screenshot main EMA Length9 then p35 instruct20,50,200 | Indicator periods depend on illustration/context; demo settings are not Coach EMA9 trade rule | M03 period data provenance; preset is never a source universal law; **MEDIUM** |
| R09 | Lesson19 p24 “price above EMA50” and “EMA sloping upward” listed separately | For same close-based EMA and a one-bar comparison, signs are algebraically dependent when 0<alpha<1 | M03 don't count independent votes; change horizon/source if testing extra signal; **HIGH** |
| R10 | Lessons04/08 1H/4H→5m/15m; Q&A2 p31 30m OB→5m; N-02 pp34–35 Weekly/Daily/4H PSE example | No single source-mandated timeframe ladder for every market | M00/M05 venue- and style-qualified hierarchy; **HIGH** |
| R11 | Lesson11 p14 OB is last candle before strong move, “big money entered” explanation | Neither displacement threshold, OB candle geometry nor institutional participation is observable from OHLC alone | M02 propose causal versions; don't assert actual institution/order identity; **HIGH** |
| R12 | Lesson13 pp17–18 Coach SOL countertrend SHORT scalp while 4H bullish vs Lesson08 trend-aligned BUY focus | Countertrend scalp is a **source example** with different horizon/risk, not automatic violation of all source material | M05 trend continuation and countertrend scalp separate branches; **HIGH** |
| R13 | Lesson21 pp26–28 two actual TON 4H screenshots; described 1H/15m context unpictured, “fart sir” ambiguity | Cannot assert full-snapshot evidence agreement or exact ticker/time parity | M00 distinguish chart OBSERVED vs Coach assertion vs inferred, **HIGH** |
| R14 | Q&A3 p32 bearish HTF+15m consolidation; conditional 15m short rejection OR 1H breakout long | Same resistance vicinity can generate mutually exclusive conditional outcomes, not simultaneous directions | M05 conflicting-timeframe WAIT and breakout/rejection paths; **HIGH** |
| R15 | Lesson17 p22 RSI overbought>70/oversold<30; Q&A1 p29 4H RSI69.91; N-02 p34 weekly RSI~29.04 | Strict inequalities should not be blurred by “near”; level does not itself trigger a BUY/SELL | M03 exact boundary states, **MEDIUM** |
| R16 | Lesson08 p10 target next level OR 1:2/1:3; Q&A2 p31 alternative stop below .231; Q&A3 p32 approx coach prices; trailing stop unspecified | Price, account-capital risk, execution, and sample RR must remain distinct. No unique ratio from inequality | M06 risk basis required; **HIGH** |
| R17 | Note N-01 p33 Tue–Thu and London/NY clock is forex majors/gold, summer-like PHT | Crypto 24/7 and DST invalidates mandatory universal session gates | M00 informational timing only until evidence; **MEDIUM** |
| R18 | Note N-02 pp34–35 title “BSP charting”, images PSE:BPI | Chart issuer and monetary authority differ; cannot obtain a “BSP stock” dataset | M00 identity qualification must come before analysis; **CRITICAL** |
| R19 | Lesson07 p9 “high probability” BUY/SELL claims and Note N-02 “institutional” selling label | Neither mathematical conditional probability nor participant identity is demonstrated by examples | No numerical probability/“institutional verified” badges before independent data; **HIGH** |
| R20 | Multiple drawings of BOS, FVG, CHoCH, EMA “retests” show idealized or retrospectively selected candles | Plotting a pivot at its origin on history can falsely imply it was knowable then | M00 timestamp known-at and delayed events, **CRITICAL** |

## Reconciliation decision procedure

1. Verify original passage/figure and semantic scope; do not rewrite original content.
2. If statements serve different contexts (trend vs range, continuation vs scalp, forex vs crypto), keep **separate scenario profiles** and do not globally weaken a source gate.
3. If genuinely unspecified, create at least two testable INDEPENDENT candidate rules plus a no-automation/manual baseline.
4. Declare event reference, timestamp, validity, failure examples, data requirements and conditions of reversal.
5. Choose a research baseline *provisionally* only where it is the simplest auditable candidate; do not brand it “Coach exact.”
6. Before a real trading claim, demand later separate market-data reproducibility, realistic fees/slippage/funding and out-of-sample validation. No historical returns or win rates are established here.

## Current research order

**P0** identity/timing and structure/pivots (M00–M01) → **P1** zones and candle signals (M02/M04) → **P2** RSI/EMA and multi-timeframe candidate states (M03/M05) → **P3** risk and optional enhancements (M06/M07). This is an engineering dependency order, not replacement of the PCSS source order. The full original PDF has already been studied in that order.

**Important:** Reconciliation register OPEN does not mean earlier 26 source studies are incomplete. It means the original Coach prose lacks one uniquely reproducible automated interpretation.
