# M02 — Source-to-Zone Specification: S/R, Role Flip, OB, FVG and Fibonacci (research v0.1)

**STATUS: FORMAL RESEARCH ALTERNATIVES; NONE IMPLEMENTED OR BACKTESTED.** 2026-11-09 Asia/Manila. Original Coach PDF is the sole source for Coach claims: [Lessons 09–11 PDF pp11–14](../../sources/coach%20trading%20lessons.pdf), [Lesson14 PDF p19](../lessons/14-fibonacci-retracement.md), [Lesson21 setup pp26–28](../lessons/21-tonusdt-topdown-setup.md), [Q&A2 p31](../lessons/qa-02-fartcoin-scalp-pullback.md), [N-02 BPI pp34–35](../lessons/note-02-bpi-bsp-stock-charting.md). See [market/structure foundation](01-causal-market-structure.md) and [entry gating](02-topdown-entry-state-and-risk.md).

## A. Source-scoped facts and missing grammar

**COACH_EXPLICIT:**
- PDF p11 defines support/resistance as zones where price previously reacted and describes support/resistance role reversal after break.
- PDF pp12–13 Gold Spot USD 1H/5m has horizontal *areas* (not points); source 1H sideways, near middle no good entry, near boundary with confirming reversal may qualify.
- PDF p14 says Order Block is the “last candle bago nag pump/bagsak ng malakas”; describes large-money reaction, but has no unique OHLC or institutional-flow measurement.
- PDF p19 defines Fibonacci anchor direction with observed swing low/high and initial pullback 0.5–0.618, then adds custom0.705 and proposes **alternative** 0.618–0.705 zone, confirmation required.
- PDF pp18/21/24/27/35 mentions FVGs and revisits/targets, but no complete mathematical FVG formation grammar or zone expiry.
- PDF p31 Coach recommends 30m OB main zone and 5m confirmation; no chart provides source-certified OB boundaries.

**OPEN:** how many touches, extrema significance, clustering/tolerance units, minimum displacement, gap definition, wick/body contact, break vs role flip, origin and invalidation time, filled/mitigated statuses, multiple zones, expiry, overlapping zones and which take priority. Source prices in Gold Spot, BPI PHP or TON/FARTCOIN examples must never be transferred to unrelated crypto feed.

## B. Universal proposed zone record and time contract

A proposed zone is a nonempty closed interval \(Z=[z_{\min},z_{\max}]\), \(z_{\min}\le z_{\max}\), in a **qualified quote currency**. Attach:
- exact exchange/symbol/product, timeframe, candle schedule, provider and whether series adjusted/derived;
- kind and detector-hypothesis ID, with origin bar IDs and immutable original price interval;
- defined_at = moment all geometric inputs become known and final, not the visual pivot origin;
- active_from, eligible-side, original reference role and break/retest policy;
- contact events with their **available_at** and hypotheses (wick, body, close), invalidation, expiry and mitigation history;
- original source statement vs independently detected zone; missing-value reason.

**Causal invariant:** a future-created zone cannot be used to justify a past trade at its historical origin bar. A screenshot-supplied horizontal rectangle without reconstructible raw candles may be reported as **SOURCE_ANNOTATION_ONLY**, not as independently machine-verified S/R, OB or FVG.

**Proposed zone status**: PROPOSED / CONFIRMED_KNOWN / ACTIVE / TOUCHED / REACTED / INVALIDATED / EXPIRED / UNKNOWN. These are our candidate labels, not Coach's.

## C. Support and resistance: baseline plus two explicit detectors

**Z-SR0 manual source-faithful:** chart analyst records historically known support/resistance interval and touch evidence; cannot assert objective automatic detection.

**Z-SR1 confirmed-pivot clusters (INDEPENDENT):** take already available, eligible confirmed swing lows (potential support) or highs (potential resistance), within a predeclared lookback and instrument-specific tolerance \(\delta>0\), cluster spatially; define interval from contributing price extrema, with optional tick padding declared separately. Require at least a predeclared number of prior pivots and *known-at* times; future pivots cannot tighten an old zone retroactively. \(\delta\), minimum pivots, decay, role classification and cluster-combination order are **unselected**. Use reproducible time-order processing rather than scanning the full future series once.

**Z-SR2 rolling completed-bar extrema (INDEPENDENT):** preceding N fully known bar highs/lows and local reaction tests give simpler causal bounding levels, but the result may not correspond to Coach's chart-drawn structural swing zones. N, minimum reaction and width still unselected.

**Role flip:** Coach says a broken support can become resistance and vice versa. Different independent event grammars:
- RF1 first final close beyond pre-known zone boundary marks a **candidate** break;
- RF2 require a subsequent retest from the opposite side and a completed rejecting candle before a **confirmed flip**;
- RF3 allow wick break but require later closing acceptance.
The source does not choose RF1/2/3. A break alone should not fabricate an observed successful retest.

## D. Order Blocks: explainable but not institution-certified

**COACH_EXPLICIT p14:** last candle before a strong upward/downward move; “large money entered” is Coach's interpretation, not something OHLC directly measures.

**Z-OB0 source/manual:** label a visually chosen last candle's entire high-low or body range with source provenance; source does not specify which bounds.

**Z-OB1 last-opposite-candle + independently defined displacement (INDEPENDENT):** after a *completed* qualifying bullish displacement, search back for most recent bearish candle within a declared window and define prospective demand interval from specified wick/body. For bearish displacement use last bullish candle. The displacement threshold, candle body criteria, lookback N, fill policy, mitigation and invalidation remain **unselected**.

**Z-OB2 last-candle-regardless-of-color (INDEPENDENT):** identify the immediate candle preceding a confirmed displacement, regardless of its candle color, to match literal “last candle before strong move” more closely. May conflict with common last-opposite-candle interpretations, so compare rather than claim Coach mandates Z-OB1.

**Prevent lookahead:** a strong move known only when a future displacement bar closes can certify an OB no earlier than that displacement close. Drawing a rectangle at the OB candle origin is for audit, not a tradable early signal. **Never label the origin candle as known OB before displacement exists.** No institutional identity is verified.

### D1. Original page-14 image qualification (2026-11-10 audit correction)

**Direct source-image observation:** Original Coach PDF page 14 explicitly has two Order Block illustration panels with candles numbered 1, 2 and 3. Both show a label **“1→3 GAP”** and a shaded OB area. In the bullish panel, candle 1 labelled “OB Candle” is **green** near a Swing Low, and in the bearish panel candle 1 is **red** near a Swing High. The image is also repeated on page 15. The earlier blanket impression that there was *no illustrated three-candle gap* is incomplete; the page-14 image supplies qualitative 1-to-3 gap evidence, though it does not give an unambiguous formal wick/body formula, numerical displacement threshold, whether a gap is required for every OB, or when a zone is no longer valid.

**Consequence:** Z-OB1 last-opposite-candle is an INDEPENDENT market convention and does **not** reproduce both original illustrations as a universal candle-color rule. Z-OB0 source annotation and Z-OB2 any-color predecessor are important source-compatible alternatives. Z-FVG1 below is an *independent precise mathematical interpretation of the illustrated 1→3 concept*, not a fully explicit Coach formula. Keep the FVG and OB evidence separate; one graphic is not independent order-flow validation. See [source study Lesson 11](../lessons/11-order-block-bos-choch.md) and [pre-implementation audit](../audits/2026-11-10-phase2-preimplementation-audit.md).

## E. Fair Value Gaps: source uses term but not geometry

**COACH_EXPLICIT:** FVG is named as a gap/imbalance location revisited on pullback (p18/21/24/27/35). The **p14/p15 source diagrams visibly label a “1→3 GAP” between numbered candle illustrations**, so a three-candle gap concept has source-figure support. However, the PDF still supplies no unique strict wick-versus-body inequalities, minimum size, required displacement, whether such a gap defines every FVG/OB, or a gap fill/expiry rule. Exact Z-FVG1 inequalities remain INDEPENDENT formalization.

**Z-FVG0 manual/screenshot annotation:** preserve Coach's claimed zone and PDF page, but mark formulation UNVERIFIED.

**Z-FVG1 three-closed-candle geometric gap (INDEPENDENT common candidate):**
- For three consecutive fully available bars \(i-2,i-1,i\), **bullish gap** if \(L_i>H_{i-2}\); initial interval \([H_{i-2},L_i]\).
- **Bearish gap** if \(H_i<L_{i-2}\); interval \([H_i,L_{i-2}]\).
- It only becomes known after bar \(i\) closes/arrives. Require actual three consecutive feed bars; missing bars and session jumps must be flagged rather than silently accepted.
- A separate unselected minimum gap width in ticks or normalized volatility may remove micro gaps; don't invent a source threshold.
- Mitigation alternatives: any wick contact, body contact, midpoint fill, full closure beyond far boundary; source doesn't specify which.

**Z-FVG2 gap+displacement evidence:** add middle candle strength, ATR/tick threshold, or structural break requirement to Z-FVG1, each explicitly independent; may overfit and excludes some bare three-candle gaps. Empirical comparisons must be after-cost and event-causal.

**Critical:** “FVG” on a price chart is not proof of actual order-book liquidity imbalance or executable price discovery. A PSE stock overnight gap is not necessarily the same mechanism as a continuous crypto three-bar FVG.

## F. Fibonacci: two source entry bands and causal anchors

**COACH_EXPLICIT p19:** For UP move, select swing low \(L\), swing high \(H\), then await downward retracement; DOWN inverse. Default listed levels0.236/0.382/0.5/0.618/0.786. First source band **0.5–0.618** and later manual custom **0.618–0.705**. Confirmation required; stop described beyond0.786 on respective side, but no quote-independent tick buffer or execution rule.

Let \(D=H-L>0\). **INDEPENDENT coordinate derivation**:
- UP retracement at ratio \(r\): \(P_{\mathrm{UP}}(r)=H-rD\).
- DOWN retracement: \(P_{\mathrm{DOWN}}(r)=L+rD\).
- For UP 0.5–0.618 zone: \([H-0.618D,H-0.5D]\); for UP 0.618–0.705: \([H-0.705D,H-0.618D]\).
- For DOWN 0.5–0.618: \([L+0.5D,L+0.618D]\); for DOWN 0.618–0.705: \([L+0.618D,L+0.705D]\).

The two bands **share boundary0.618 but are not one uniform source-defined0.5–0.705 entry zone**. Exact swing selection, frozen anchor known-at and redraw policy are missing. If the swing high is only confirmed after some retracement, a earlier historical touch cannot be counted as known Fibonacci zone in real time. Avoid future-dependent “perfect” swing anchors.

## G. Overlaps are observations, not independent votes

Historical BPI source p35 has Weekly resistance92–94 overlapping FVG92–97; resistance98–100 overlapping FVG/OB98–103; resistance110 inside FVG/OB108–112. This illustrates *co-located source labels* but does not prove independent probability multipliers. A cluster algorithm must count shared candle/pivot origins and avoid double-counting redundant transformations as separate statistical evidence.

Proposed zone display may show overlapping intervals separately (with origin and provenance) or compose a union/intersection only with explicit attribution; no Coach rule says all overlaps are stronger.

## H. Constructed falsification examples — expected conditions, NOT executed

| ID | Invented case | Expected qualification |
|---|---|---|
| Z01 | Support drawn today on previous week's candle using future pivots | Historical pre-draw entry forbidden |
| Z02 | Wick enters support, body never does | Z-SR contact wick vs body variants disagree |
| Z03 | Price in middle of known sideways range | Lesson10 says unattractive entry; WAIT |
| Z04 | Price contacts resistance but no closed rejection | WAIT_CONFIRMATION |
| Z05 | One bar closes below support, retest never happens | RF1 break possible, RF2 flip unconfirmed |
| Z06 | An OB candle exists but no subsequent displacement confirmed yet | No confirmed OB under Z-OB1/Z-OB2 |
| Z07 | Strong bullish displacement after bearish candle | Z-OB1 demand candidate only at displacement close |
| Z08 | Strong bullish displacement after bullish candle | Z-OB1 vs Z-OB2 differ |
| Z09 | Three closed bars with first H100, third L102 | Z-FVG1 bullish gap interval[100,102] |
| Z10 | First H100, third L100 | No positive-width bullish gap under strict > |
| Z11 | Three bars contain missing 15m timestamp | reject/flag gap formation as unreliable |
| Z12 | Gap later half-filled by wick only | mitigation definitions differ |
| Z13 | UP swing low100, high120, r0.5–0.618 | zone[107.64,110.00] |
| Z14 | Same UP swing, r0.618–0.705 | zone[105.90,107.64] |
| Z15 | DOWN swing high120, low100, r0.5–0.618 | zone[110.00,112.36] |
| Z16 | Same DOWN swing r0.618–0.705 | zone[112.36,114.10] |
| Z17 | Swing H not confirmed when price touched Fib level | not historical eligible |
| Z18 | BPI FVG and resistance overlap | not double-counted as independent signals |
| Z19 | FOREX.com Gold Spot level4670 copied to XAUUSDT | invalid cross-product price transfer |
| Z20 | Source says institution selling at BPI zone but only OHLC available | institution identity UNKNOWN |

Illustrative Fib arithmetic follows the stated formulas; no market backtest, historical replay or Pine tests were executed.

## I. Open decisions before automated zones

Exact instrument tick size and rounding; S/R pivot-cluster lookback; role flip geometry, OB candle/window/displacement; FVG gap width/mitigation/invalidation; source-versus-computed labels; Fib anchor freezing, late confirmation and band preference; same-bar touch/reaction ordering; confluence overlap; resource limits of future TradingView chart overlay.

**Working research preference:** manual/source-annotation baseline plus causal pivot-derived S/R, simple three-candle gap and transparent OB variants as **comparison candidates only**. Select after synthetic fixture and venue-specific tests; do not claim these are Coach's exact numeric detectors.
