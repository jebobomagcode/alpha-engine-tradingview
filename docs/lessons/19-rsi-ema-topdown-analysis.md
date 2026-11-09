# PCSS Lesson 19 — RSI + EMA Application Using Top Down Analysis

**Status:** COMPLETE for source-first study and independent methodological research, 2026-11-09 Asia/Manila. Original PDF p24 rendered, visually inspected, and checked against native text; p25 inspected to confirm Lesson 20 boundary. No Pine code, chart acceptance, historical backtest, deployment, trading order or demonstrated financial edge.

**Sole Coach-source:** [Original PDF p24](../../sources/coach%20trading%20lessons.pdf). Original SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. Private PCSS SHA-256 99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56 (not published). Scope: independent crypto TradingView project, including distinct exchange/product-qualified XAUUSDT, XAUTUSDT, PAXGUSDT; previous projects not touched.

## Source inventory — original page order

Lesson 19 occupies one **text-only** page: title, colored heading/step markers, three numbered steps and paired LONG/SHORT examples. There is no original chart illustration, price-series case, mathematical proof, assigned exercise, trade fill, risk specification or performance figure. Original p25 contains separate Lesson 20 CHoCH charts and must not be attributed to p24.

| ID | Coach source item in order | Audit note |
| --- | --- | --- |
| 19-01 | Heading: RSI + EMA Application Using Top Down Analysis | Exact Lesson 19 heading |
| 19-02 | Repeated RSI + EMA Top Down Analysis subheading | No diagram |
| 19-03 | STEP 1 — Higher Timeframe Bias | First source stage |
| 19-04 | Start on 4H, Daily or 1H | No mandatory HTF/LTF pairing specified |
| 19-05 | Observe market structure | Distinct from indicator bias |
| 19-06 | Observe EMA direction | Length/method unspecified |
| 19-07 | Observe RSI momentum | Not a defined entry trigger |
| 19-08 | Bullish example: price above EMA 50 | Explicit period 50 in this example |
| 19-09 | Bullish example: EMA sloping upward | Slope horizon missing |
| 19-10 | Bullish example: RSI above 50 | Source midpoint reading |
| 19-11 | Conclusion: bullish bias | Qualitative inference |
| 19-12 | STEP 2 — Wait for Pullback | Second source stage |
| 19-13 | Do not chase impulsive move | Explicit patience |
| 19-14 | Watch retracement | No quantitative distance |
| 19-15 | Watch EMA retest | No touch definition |
| 19-16 | Watch FVG revisit (babalikan ang gap) | No gap-formation/expiry rule |
| 19-17 | Watch key support/resistance | No zone geometry |
| 19-18 | STEP 3 — Lower Timeframe Confirmation; 15M/5M | Third source stage |
| 19-19 | Look for rejection candles | Geometry undefined on this page |
| 19-20 | Look for BOS / CHOCH | Slash does not settle OR/AND/order |
| 19-21 | Look for RSI holding momentum | Exact state unspecified |
| 19-22 | Look for EMA support/resistance respected | Response definition unspecified |
| 19-23 | Example Long Setup | Repeats Lesson 16 |
| 19-24 | LONG HTF: bullish structure | Source condition |
| 19-25 | LONG HTF: price above EMA | Length not repeated |
| 19-26 | LONG HTF: RSI above 50 | Source condition |
| 19-27 | LONG LTF: price retraces to EMA/FVG | Slash ambiguous |
| 19-28 | LONG LTF: RSI bounces above 50 | Cross/retest ambiguous |
| 19-29 | LONG LTF: bullish rejection candle appears | Candle geometry unspecified |
| 19-30 | Conclusion: continuation longorbuy | Not a recorded fill |
| 19-31 | Example Short Setup | Repeats Lesson 16 |
| 19-32 | SHORT HTF: bearish structure | Source condition |
| 19-33 | SHORT HTF: price below EMA | Length not specified |
| 19-34 | SHORT HTF: RSI below 50 | Source condition |
| 19-35 | SHORT LTF: price retraces to EMA resistance | FVG not named in short example |
| 19-36 | SHORT LTF: RSI rejects below 50 | Rejection semantics undefined |
| 19-37 | SHORT LTF: bearish confirmation candle | Exact pattern undefined |
| 19-38 | Conclusion: continuation short | No stop/target/order |

**All 38 source items present.** The paired LONG and SHORT blocks repeat Lesson 16 p21 essentially verbatim. Preserve their original scope and do not count the repetition as independent empirical confirmation.

## Prerequisites, only as needed

Lesson 07: HH/HL vs LH/LL directional structure. Lesson 08: area of interest before reaction and entry/risk. Lesson 12: BOS continuation relative to a known structure. Lesson 16: the same LONG/SHORT continuation templates. Lesson 17: usual RSI length 14 and momentum midpoint 50. Lesson 18: common EMA20/50/200, dynamic retests, slope and sideways whipsaws. These are earlier-source reminders, not new p24 claims.

## Step 1 — Higher Timeframe Bias (COACH_EXPLICIT)

Coach explicitly names **4H, Daily, 1H** as possible higher timeframes. In order, inspect (a) market structure; (b) EMA direction; (c) RSI momentum. His concrete bullish example is **price above EMA50, EMA sloping upward, RSI above 50**, interpreted as bullish bias.

**Source distinctions:** The three-line example does not demonstrate a HH/HL series even though structure is on the checklist. EMA50 is explicitly chosen for this bullish illustration, but the following LONG/SHORT blocks merely say “EMA” with no number. We must not silently impose EMA50 in every strategy context, or equate indicator bias with formally confirmed swing structure.

**Missing:** HTF choice precedence, EMA slope lookback and strength, how multiple HTFs disagree, RSI data source, selected price for the EMA comparison, whether the last HTF bar must close, and reliability.

### Exact independent mathematics: potential duplicate confirmation

For same-timeframe close C_t, EMA E_t, n>1 and alpha=2/(n+1),
E_t = alpha*C_t + (1-alpha)*E_(t-1).
Then E_t-E_(t-1)=alpha*(C_t-E_(t-1)) and C_t-E_t=(1-alpha)*(C_t-E_(t-1)).
Because alpha and 1-alpha are positive:

**C_t > E_t if and only if E_t > E_(t-1)**, and similarly for negative and zero differences.

If EMA sloping up means one-bar rise of the same close-based EMA50, then price above EMA50 and EMA50 one-bar up are *algebraically redundant*. Do not count them as separate independent confluence votes. This is our proved conditional observation, not a Coach statement. It may not apply to longer-horizon slopes, visual chart angle, different inputs, offsets or timeframes.

## Step 2 — Wait for Pullback (COACH_EXPLICIT)

Coach says not to chase impulsive movements. Wait for retracement, EMA retest, FVG revisit (price returns to the gap), and key support/resistance. These named objects are preserved in the original order.

**Source ambiguity:** The PDF never specifies whether all four are required or whether they are alternatives. Neither an EMA wick/close touch nor FVG geometry, expiry, S/R strength or time allowance is formally defined. An area may never be revisited, or a pullback may evolve into a true reversal. Treat location as possible context rather than a guaranteed bounce or entry.

## Step 3 — Lower Timeframe Confirmation (COACH_EXPLICIT)

Coach explicitly switches to **15M/5M** and looks for rejection candles, BOS/CHOCH, RSI holding momentum and EMA support/resistance respected. This comes after the HTF-bias and wait-for-pullback steps.

**Unresolved semantics:** BOS means potential continuation, CHoCH possible shift; source slash does not tell us OR/AND, necessary sequence or timeframe-specific swing points. RSI “holding momentum” could mean above/below 50, rising/falling, or a midpoint retest. A completed candle and an intrabar wick can give different results. “EMA respected” requires dynamic touch and rejection timing. Source does not provide numerical event thresholds or a universal four-Boolean confirmation gate.

## Repeated continuation examples (COACH_EXPLICIT)

**LONG:** HTF bullish structure, price above EMA, RSI above 50; LTF price retraces to EMA/FVG, RSI bounces above 50, bullish rejection candle appears. Coach concludes **continuation longorbuy**.

**SHORT:** HTF bearish structure, price below EMA, RSI below 50; LTF price retraces to EMA resistance, RSI rejects below 50, bearish confirmation candle. Coach concludes **continuation short**.

These two blocks repeat Lesson 16 p21 and do not add an entry price, protective stop, profit target, position quantity, holding time or numerical historical performance. The LONG explicitly says EMA/FVG while SHORT names EMA resistance; bullish rejection vs bearish confirmation are also not exactly mirrored. Page 19's EMA50 bias example must not be silently applied as a universal length to the repeated generic-EMA templates.

Lesson 13 describes a separate countertrend SHORT in an HTF bullish market, and Lesson 10 includes range cases. Lesson 19 provides continuation illustrations, not a universal prohibition on other source-described contexts.

## Independent PCSS example — hypothetical, not Coach data

On a hypothetical 4H BTCUSDT instrument: confirmed HH/HL, close 100000 USDT, EMA50 98500 and RSI58. A later 15m bar returns to known support, shows a tentative bullish rejection, but RSI remains 47 and structural CHoCH not confirmed. HTF context can be bullish while LTF confirmation is incomplete. Return WAIT/INSUFFICIENT under a close/confirmation-based research variant. No stop or TP defined, thus no honest unique gross risk/reward ratio.

## Independent time-causal and software considerations

Official TradingView sources, **not Coach-origin**:
- https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/ — HTF requests need care with lookahead. The documented last-confirmed-HTF idiom offsets the requested expression by one bar and uses barmerge.lookahead_on.
- https://www.tradingview.com/pine-script-docs/concepts/repainting/ — forming realtime high/low/close and derived EMA/RSI may change before candle close.
- https://www.tradingview.com/pine-script-docs/concepts/bar-states/ — barstate.isconfirmed is not a usable shortcut *inside* request.security to confirm the HTF requested series.

For future research, store symbol/exchange/product, timeframe, bar-known timestamps, structural swing confirmation times, EMA/RSI source/length, zone formation and touch, LTF event confirmation and risk completeness. Never backdate an HTF state or use future-finalized candles as if already known. No Pine parity or nonrepainting test has yet been conducted.

## Ponder synthesis and unresolved choices

- **Double count:** EMA50 one-bar slope and same close-vs-EMA50 side carry the same sign information under exact conditions.
- **Repeated examples:** Lesson16 and Lesson19 are the same source-defined paired continuation templates, not two empirical validations.
- **No invented grammar:** Step2 location list and Step3 evidence list do not have a defined AND/OR rule, order among all sub-items, timeout or confidence weights.
- **Source hierarchy:** Real HTF structure is separate from EMA/RSI bias; disagreements must not disappear.
- **Risk unknown:** No complete order, stop, target, fills, cost, or proven probability.

See [Lesson 19 independent research](../research/19-topdown-timecausal-confluence-research.md) for explicit alternatives and future disconfirming fixtures. **All 38 original page units studied. Lesson 19 COMPLETE for PCSS learning only, not a built system or financial validation.**

**Next on owner instruction:** Lesson 20 — CHoCH (Change of Character), PDF p25 with multiple source illustrations.
