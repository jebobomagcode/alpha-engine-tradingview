# PCSS Lesson 01 — Trading 101: Choosing a Market

**Status:** COMPLETE (source coverage and user-facing study), 2026-11-09 Asia/Manila  
**Coach source:** [coach trading lessons.pdf, page 1](../../sources/coach%20trading%20lessons.pdf)  
**Coach PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`  
**Coach PDF Git blob SHA-1:** `c99de01b9178e16e240f83f5c4594fa5683a1ba2`  
**PCSS file SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`  
**Coverage:** page 1 only. Do not imply Lesson 02 was taught.  
**No Pine implementation, backtest, live order, or chart validation performed.**

## Scope and original source inventory

The original letter-sized page was inspected in a rendered page image and compared with extracted PDF text. It contains prose categories and icons, **no distinct chart/diagram, original quantitative exercise, theorem, or proof**.

| Source element, in order | Original content audited | Coverage |
| --- | --- | --- |
| Header and introductory instruction | “01. TRADING 101”, “FOR BEGINNERS”, choose where to trade | Covered |
| Crypto: platform examples | Binance, Bybit, OKX (reported by Coach, **not endorsements**) | Covered |
| Crypto: 3 pros | 24/7, active movement, low initial capital possible | Covered |
| Crypto: 3 cons | High volatility; fake hype/scam/meme coins; emotional trading/FOMO | Covered |
| Forex: broker examples | IC Markets, XM, occasionally Exness (Coach report only) | Covered |
| Forex: 3 pros | More stable than crypto; “cleaner” for technical analysis; leverage | Covered with qualifications |
| Forex: 3 cons | Leverage cuts both ways; account wipeout risk; 24/5 sessions | Covered |
| PH stocks: broker examples | COL Financial and DragonFi (Coach report only) | Covered |
| PH stocks: 3 pros | Relatively less stressful; long-term investment; dividends | Covered with qualifications |
| PH stocks: 3 cons | Slower movement; restricted hours; high capital for noticeable nominal returns | Covered |
| “TO SUMMARIZE” | Crypto fast-paced/stress, Forex structure/discipline, stocks “safe”/long term | Covered; unsafe universal claim qualified |
| “REAL TALK” | Discipline plus risk control emphasized over merely being in the market | Covered and critically expanded |

The source is qualitative; it specifies **no formal indicator signal, mathematical market-selection rule, product specification, or automated threshold** in this lesson.

## 1. Coach-expressed starting principle

**COACH_EXPLICIT (p. 1):** “Pili muna kayo kung saan kayo mag trade.” In English: choose the market to trade before deciding on tactical analysis.

**INTERPRETATION:** The market's operating hours, traded products, volatility, liquidity, and broker/venue mechanics affect both analysis and risk. This is a sensible starting question, not a claim that the source provides a market-selection algorithm.

**INDEPENDENT_EXTENSION:** Separate:
- *market / asset class* (crypto, FX, equities);
- *instrument* (specific pair, token, company share);
- *trading product* (spot, margin, perpetual futures, CFDs, actual share ownership);
- *venue and data source* (exchange, broker, TradingView symbol feed).

A chart does not, by itself, establish product economics or execution availability.

## 2. Cryptocurrency — source, explanation, qualifications

**COACH_EXPLICIT:** Coach uses Binance, Bybit, and OKX. Advantages: 24/7 access; large price moves; relatively low entry capital. Drawbacks: large/sudden adverse price moves; speculative or fraudulent coins; FOMO and emotional decisions.

**Explanation:** Crypto spot markets generally trade around the clock, allowing weekend analysis. Fractional trading can reduce the amount required to participate; this does not remove trading fees, spread, liquidity limits, custody risk, or price risk.

**Independent caution:** Volatility means price variability, not positive expected return. “More movement” offers more possible trades but also more possible losses. A price move of -10% on a 10,000 PHP unlevered position implies approximately 1,000 PHP adverse price movement before costs (illustrative, not actual market data). FOMO is a behavioral risk: entering after chasing a move contradicts a rules-based decision process.

**Potential design implication (not yet an accepted feature):** record whether price already moved beyond the designated confirmation/entry context; explain why a setup is WAIT or NO TRADE rather than prompting a late entry. Need rules from later Coach lessons and independent verification first.

## 3. Forex — source, explanation, qualifications

**COACH_EXPLICIT:** Coach uses IC Markets, XM, sometimes Exness. He characterizes Forex as more stable than crypto, cleaner for technical analysis, and offering leverage. Cons: leverage magnifies losses, poor risk management can wipe out an account, markets operate roughly 24/5 with trading sessions.

**Explanation:** A Forex pair, such as EUR/USD, expresses one currency's value in another. Retail FX trades may be OTC contracts with dealer/platform-specific pricing and execution, not necessarily exchange-listed ownership of currencies.

**IMPORTANT — INTERPRETATION vs VALIDATED FACT:** “More stable” and “cleaner” are discretionary comparisons, not mathematically universal results. A major FX pair may have lower percentage volatility than some tokens over one period, but regimes, instruments, liquidity and event shocks change this. No evidence in page 1 demonstrates that FX price patterns are intrinsically more predictable.

**Leverage intuition (independent worked example):** An illustrative 10,000 PHP capital base exposed to a 10,000 PHP unlevered notional has approximately a 200 PHP loss at a 2% adverse price move. If the same capital backs a 100,000 PHP notional position (10× exposure), the same move yields approximately a 2,000 PHP loss before fees, financing, slippage, margin call and liquidation effects. This is a preview of Lesson 05, not original Lesson 01 arithmetic.

**Source improvement:** Regard leverage as ability to amplify exposure, not free money or inherently beneficial. The U.S. CFTC warns that OTC FX leverage can amplify losses, and retail dealers' execution arrangements create additional risks: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html

**Future design candidate:** time/session-aware market context, but precise session offsets, DST and broker calendars require design and validation rather than hardcoded assumptions at this stage.

## 4. Philippine stocks — source, explanation, qualifications

**COACH_EXPLICIT:** Coach uses COL Financial and DragonFi. Pros: relatively less stress, long-term investing, and potential dividends. Cons: comparatively slower movement, restricted exchange hours, and a need for more capital to earn noticeable nominal profits.

**Explanation:** A share represents ownership in a company; capital gains and dividends are possible, not guaranteed. Lower trading hours may lower monitoring demands, but news and gaps can occur between sessions. The Philippine Stock Exchange's published trading hours and market phases confirm a scheduled-market structure: https://www.pse.com.ph/investing-at-pse/

**Critical correction:** The source's summary associates PH stocks with being “safe + long term.” A long holding period does not make a single equity safe. Shares can lose substantial value; dividends may be discontinued. The U.S. SEC investor education page explicitly describes stock-loss and bankruptcy risk: https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks

**Independent numerical illustration:** At a 5% price change, a 2,000 PHP unlevered position changes by about 100 PHP while a 100,000 PHP position changes by about 5,000 PHP, before costs. Larger capital changes nominal P/L, not the asset's percentage return. Board-lot rules, commissions, and other market costs also matter.

**Potential design implication:** explicit exchange sessions, daily gaps, corporate-action-adjusted market data, liquidity and spread constraints. Nothing is implemented.

## 5. Coach's recap — preserved in original order

**COACH_EXPLICIT:** Crypto suits traders comfortable with fast pace and stress; Forex suits people who like technical structure and discipline; Philippine stocks suit longer-term, less rushed approaches. These are Coach's qualitative suitability suggestions, not established rankings of risk or performance.

**INDEPENDENT_EXTENSION:** A rational market choice should consider: instrument/product, execution venue, trading session, nominal and percentage volatility, liquidity, spread/commission/funding, leverage, price gaps, availability of representative data, and the human's time and risk tolerance.

## 6. “Real Talk” — discipline and risk control

**COACH_EXPLICIT:** “Hindi ka yayaman dahil sa market ha, kikita ka dahil sa disiplina + risk control.”

**Meaning:** Participating in a fast market is not by itself a source of earnings. Consistent decisions and risk limits are central.

**INDEPENDENT_CORRECTION:** Discipline and risk control are important but **not sufficient** for profitable trading. One can faithfully execute a negative-expectancy system. Any claim of advantage requires after-cost statistical and out-of-sample evidence; even a favorable backtest does not guarantee future performance. FINRA's guidance emphasizes costs, margin risk and hazards of frequent trading: https://syndication.finra.org/content/frequent-intraday-trading-understanding-basics

## Ponder notes — source claims tested for unwarranted universality

| Source or proposed assertion | Critical finding | Design consequence |
| --- | --- | --- |
| Crypto movement creates opportunity | Movement also increases loss potential; direction and costs matter | Measure risk objectively, do not reward raw volatility automatically |
| Forex is “cleaner” | Subjective; needs instrument/regime-specific evidence | No hardcoded Forex superiority |
| Leverage is a pro | Exposure increases both gain and loss, and liquidation risk | No leverage recommendation from chart pattern alone |
| PH stocks are “safe” | Incorrect as universal description; individual stocks can fail | No inherent safety ranking |
| Discipline + risk control makes money | Necessary operating traits, insufficient without positive edge | Require independently evaluable method and transparent WAIT states |

**Independent research (accessed 2026-11-09, not Coach sources):**
- Coinbase Help — spot crypto 24/7 vs stock hours: https://help.coinbase.com/en/other-topics/stocks-vs-crypto
- CFTC — eight points for retail OTC Forex: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- Philippine Stock Exchange — investing and trading hours: https://www.pse.com.ph/investing-at-pse/
- SEC Investor.gov — stock ownership and risks: https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks
- FINRA — frequent intraday trading risks: https://syndication.finra.org/content/frequent-intraday-trading-understanding-basics

References support their particular scope (e.g., U.S. FX regulatory claims are not treated as Philippine legal advice). Vendor marketing or Coach's subjective terms do not constitute independent statistical validation.

## Conceptual model for future TradingView work

**PROPOSED, NOT IMPLEMENTED:**

`market -> symbol/instrument -> trading product -> venue/data source -> hours/liquidity/cost regime -> market-context analysis -> condition/wait/no-trade output`

The user's indicator-first, strategy-ready direction remains in force. We should not pick a preferred symbol, platform, market, chart interval, session heuristic or risk threshold solely from Lesson 01. Later lessons provide setup methodology, to be studied in their own original order.

### Open questions, deliberately not prematurely decided
- Which specific instruments and products will first be supported (crypto spot, perpetual, FX/CFD, PSE equities)?
- How will venue feed and trading product be represented in script configuration and validation?
- Which objective measures of volatility, spread and liquidity are usable on TradingView for each asset class?
- How will session closures, daylight saving time, weekends and gaps be handled?
- How should behavioral risk be represented without inventing Coach trade rules?
- What are the actual data and Pine runtime constraints for these instruments?

These are tracked as **OPEN_UNRESOLVED**; they do not prevent completion of the *study of page 1*, and no feature is approved merely by appearing in this note.

## Owner's later project-scope decision (D-013, 2026-11-09)

**USER DIRECTIVE, NOT COACH EXPLICIT:** After Lesson 01 was taught, the owner selected the **crypto trading ecosystem** as the only future TradingView implementation focus, explicitly including **XAUUSDT, XAUTUSDT and PAXGUSDT**. The earlier question of whether Forex/PSE equities would be implementation markets is therefore resolved: they are **not** separate runtime targets. Study of their original Coach PDF material remains required under PCSS. XAUUSDT can be a USDT-settled gold-price derivative, whereas XAUT and PAXG are separate gold-backed crypto tokens. These require distinct venue-qualified symbol verification. Detailed scope and sources: [MARKET_SCOPE.md](../MARKET_SCOPE.md). This dated addendum **does not rewrite Coach's page 1 content** or change Lesson 01's completed study status.

## Complete coverage verdict and checkpoint

- Rendered PDF page 1 inspected; text extraction crosschecked.
- Every original source element inventoried and addressed in the user-facing PCSS teaching.
- No original diagrams or exercises to reproduce on page 1.
- External corrections and design suggestions identified as **not Coach-origin**.
- No empirical signal/performance test done. No Pine code developed.
- **Lesson 01: COMPLETE for source-backed PCSS teaching and initial research.**
- **Next item:** Lesson 02 — Basic Candlestick Pattern, pages 2–3, starting with the chart illustrations and hammer/shooting star/doji. **Do not start automatically**; user will say Next or Proceed.
