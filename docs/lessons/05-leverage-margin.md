# PCSS Lesson 05 — Leverage and Margin

**Status:** COMPLETE, 2026-11-09 (Asia/Manila): exact-source page audit, complete teaching, independent mathematical verification, source/extension separation, and a design-research handoff.  
**Original Coach authority:** [coach trading lessons.pdf, page 7](../../sources/coach%20trading%20lessons.pdf) — the *only Coach Fredy-origin source*.  
**Original PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`.  
**PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`.  
**Market mandate:** cryptocurrency only for future implementation, explicitly including XAUUSDT, XAUTUSDT and PAXGUSDT; study source Forex comparison nonetheless.  
**Implementation status:** no Pine code, TradingView compilation, strategy backtesting, live trading, or deployment.

## Source inspection and ordered inventory

Rendered the original PDF page 7 at 2.5x zoom and compared visually with native text extraction. The page has text and formatting bullets/circles, but **no original chart image, data table, independent exercise, theorem, proof or formula diagram**. The following is an exhaustive logical inventory of the displayed page, not an invented section organization attributed to Coach.

| Source item | Page 7 content | Coverage |
| --- | --- | --- |
| 05-01 | Heading “05. Leverage and Margin.” | Covered |
| 05-02 | “LEVERAGE” defined metaphorically as “hiram na buying power” | Covered |
| 05-03 | Leverage example assumes capital $100 | Covered |
| 05-04 | 1x gives $100 position; 10x gives $1,000; 20x gives $2,000 | All arithmetic verified |
| 05-05 | Higher leverage: bigger possible profit, faster losses | Covered and qualified for fixed margin vs fixed notional |
| 05-06 | Coach's recommendation: prioritize risk management; low leverage suited to style | Covered; no specific safe leverage is established |
| 05-07 | “LEVERAGE DIFFERENCE sa crypto and forex” | Covered in original order |
| 05-08 | Crypto: more volatile; high leverage risky; small moves can liquidate at 20x–100x | Covered; liquidation is product/collateral-dependent |
| 05-09 | Crypto: claims platform maximum often 100x–125x depending on coin volatility; leverage adjustable by coin | Preserved as Coach's snapshot/generalization, **not a verified current universal exchange rule** |
| 05-10 | Forex: claims smaller moves, broker settings such as 1:100x, 500x, 1000x, more controlled volatility | Covered; market- and broker-specific, not universally proven |
| 05-11 | Forex: position risk should be controlled using lot size | Covered; relevant position-size principle extends to crypto |
| 05-12 | “MARGIN” defined as money used to open a trade | Covered and clarified as collateral/initial margin |
| 05-13 | Margin example: account capital $1,000, open $100 position at 1x using $100 margin | Verified |
| 05-14 | Same $100 position at 10x uses approximately $10 margin | Verified |
| 05-15 | Coach's warning: small posted margin can coexist with large position exposure | Covered and qualified |
| 05-16 | “MARGIN DIFFERENCE sa ng crypo and forex”: crypto usually higher requirement due volatility | Covered as a contingent heuristic |
| 05-17 | Forex typically lower required margin due higher available leverage | Covered as a contingent heuristic |

There is **no specified exchange, contract, mark-price policy, collateral type, liquidation calculation, maintenance-margin formula, broker-specific maximum, spread, fee or funding schedule** on this page.

## 1. Leverage — source and first example

**COACH_EXPLICIT:** Coach calls leverage “parang ‘hiram na buying power’” — an analogy for controlling more notional position value with smaller committed funds.

He uses $100 capital and shows:
- 1x -> $100 notional;
- 10x -> $1,000 notional;
- 20x -> $2,000 notional.

**INDEPENDENT MATHEMATICAL EXPLANATION:** In a simple linear derivative model, with \(N\) position notional, \(M_0\) initial margin, and leverage \(\lambda\), \(N=\lambda M_0\), or \(M_0=N/\lambda\). This concerns *the margin requirement on a specified position*, not a universal profit law. Committed collateral may be different from account equity and could be supplemented depending on margin mode.

**Worked example:** $100 initial margin at 20x supports $2,000 nominal exposure. A 1% adverse move creates $20 nominal mark-to-market loss before costs, equal to 20% of that $100 margin. A 2% adverse move creates a $40 nominal loss. A 5% adverse move creates $100 nominal loss; **real liquidation can occur earlier** due to maintenance margin and other constraints. Not a real liquidation-price estimate.

**Source qualification:** “Higher leverage -> larger potential profit/loss” is true **if it is used to create greater position notional**. It is misleading as a universal statement without holding position size constant. See the next section.

## 2. Fixed-margin vs fixed-notional experiments — independent proof

Let linear position notional be \(N=qP_0\), with long entry price \(P_0\), base quantity \(q\), and fractional price return \(r=(P_1-P_0)/P_0\). Then:
\[
\mathrm{PnL}=q(P_1-P_0)=Nr.
\]
Relative to initial margin \(M_0=N/\lambda\),
\[
\frac{\mathrm{PnL}}{M_0}=\lambda r.
\]
This identity is a **simplified unrealized return-on-initial-margin** in a linear product, not a liquidation formula.

**Experiment A: fixed margin $100** with variable leverage and proportional -2% price move:
- 1x, notional $100 -> loss $2;
- 10x, notional $1,000 -> loss $20;
- 20x, notional $2,000 -> loss $40.

**Experiment B: fixed position notional $100**:
- 1x needs $100 margin; loss on -2% move $2;
- 10x needs $10 margin; same price move still loses $2.

**Result:** leverage by itself does not change price PnL when position notional and price path are fixed; it changes required initial margin and may influence distance to liquidation and collateral flexibility. Choosing high available leverage is not the same as choosing high exposure. A 1x position can still exceed a user's desired stop-loss risk if position size is excessive or a stop is poorly located.

## 3. Coach's crypto vs Forex leverage comparison

**COACH_EXPLICIT:**
- Crypto: greater volatility; high leverage can liquidate accounts quickly. Coach cites 20x–100x risk and exchange maximums around 100x–125x for some coins, with leverage adjustable per coin.
- Forex: generally smaller price movement in his experience; broker leverage examples 1:100, 1:500, 1:1000; position exposure controlled by **lot size**.

**INTERPRETATION:** Coach's central risk lesson is to size exposure cautiously in relation to how much underlying price can move. The Forex passage is included for full source fidelity even though Forex is not an implementation target under user decision D-013.

**INDEPENDENT QUALIFICATIONS:**
- Maximum leverage is **not uniform**: venue, region, product, risk bracket, position notional and exchange rules can change it. Do not embed the cited 100–125x as a current hard-coded constant.
- Forex can also be very volatile around news or thin-liquidity periods. Asset-class volatility rankings need measurement by instrument and timeframe, not declarations of inherent stability.
- Forex lot size is the contract-specific measure of quantity; in crypto, base-asset units or contracts with specified multipliers play the same position-exposure role.
- Spot markets and fully paid token purchases usually do not have the same liquidation mechanism as leveraged perpetuals. Do not conflate XAUUSDT (when a gold-reference perpetual), XAUTUSDT and PAXGUSDT spot-token markets.

## 4. Margin — Coach's original second example

**COACH_EXPLICIT:** Margin is “pera mo na ginagamit pang open ng trade”. With $1,000 account capital, open a **$100 position**:
- at 1x, about $100 initial margin;
- at 10x, about $10 initial margin.
He warns that small margin enables large exposure.

**VERIFICATION:** \(M_0=N/\lambda\). With \(N=100\), \(M_0=100\) at 1x and \(M_0=10\) at 10x. Coach's arithmetic is correct.

**CRUCIAL DIFFERENCE BETWEEN THE TWO COACH EXAMPLES:** In the leverage example, posted capital/margin is treated as fixed ($100) and position changes ($100/$1,000/$2,000). In the margin example, account capital is $1,000, but **position is held fixed at $100**, so changing leverage changes *required margin* ($100/$10), not market price P&L. They illustrate two distinct experimental controls, not two equivalent representations of increasing risk.

**More precise vocabulary (independent):**
- **Account balance/equity:** total current account funds and, in equity, open PnL effects; may differ in multiasset accounts.
- **Position notional:** underlying market exposure stated in a quote/settlement currency.
- **Initial margin:** collateral required to open/finance the position.
- **Maintenance margin:** collateral required to maintain it as open.
- **Free/available margin:** collateral not committed or otherwise reserved; platform-defined.
- **Margin mode:** isolated versus cross; collateral allocation and liquidation consequences differ.

## 5. Margin differences: crypto vs Forex — what follows and what does not

**COACH_EXPLICIT:** Crypto usually has higher margin requirements because it is volatile; Forex may have smaller margin requirements because high leverage is available.

**INDEPENDENT CRITIQUE:** This can describe particular retail broker/exchange conditions, but is not a universal law. Margin requirement is a **product/venue risk policy**, not simply a mathematical transformation of “crypto volatility.” A specific crypto contract can have different risk tiers from another; the same instrument can have different limits across accounts/jurisdictions. Actual fees, mark price, liquidation method, maintenance margin and collateral rules need verified contract specs.

### Isolated vs cross margin (not in Coach's source)

The Binance Academy overview explains that isolated mode ring-fences allocated collateral to the position, whereas cross margin can apply wider account collateral across positions, increasing possible account-level exposure if losses accumulate. Exact eligibility and loss isolation depend on the product's rules, fees and margin configuration; isolated does not mean a guaranteed safe position. External source:
https://www.binance.com/en/academy/articles/what-are-isolated-margin-and-cross-margin-in-crypto-trading

### Liquidation mark price vs last traded price (not in Coach's source)

Binance's futures rules (FAQ updated 2026-01-04) distinguish the **Mark Price**, used for liquidation and unrealized PnL, from the **Last Price** representing recent transactions. A chart or protective order using a different price basis can produce apparently surprising divergence. Collateral below maintenance margin drives liquidation; exact formulas are instrument-specific.
https://www.binance.com/en/support/faq/detail/360033525271

No fixed percentage liquidation distance such as \(1/\lambda\) can be asserted as an accurate real exchange liquidation price without maintenance margin, contract multiplier, funding, fees, collateral, side, and margin mode.

## 6. Relation to Lessons 03 and 04

- **Lesson 03 RR:** a planned $100 stop-risk budget is **not the same** as posting $100 initial margin. First calculate planned loss from entry/stop and quantity (and validate exposure/contract rules), then assess margin sufficiency and liquidation risk. The stop may slip or fail to execute, so this planned amount is not a guaranteed maximum.
- **Lesson 04 MTF:** a structurally attractive HTF zone and LTF trigger do not override inadequate collateral or high liquidation susceptibility. Market-structure signals and solvency checks are distinct analytical layers.
- **Source hierarchy:** Coach source supplies leverage/margin intuitions, but neither lesson prescribes exact venue-specific liquidation math.

## 7. Future TradingView integration — independent proposals only

**Indicator-first, strategy-ready proposal:** keep market analysis separate from a **risk-and-margin diagnostic** that only produces numbers when instrument metadata and account inputs support them. Candidate outputs:
1. Market/venue and product type, linear/inverse/other payout, symbol point value/contract size/quantity precision and currency units.
2. User-defined capital, position quantity, entry/stop/target, leverage and margin mode, clearly distinguished from true brokerage account state.
3. Price-distance planned gross PnL and RR; estimated transaction costs/funding only when supported by real input data.
4. Initial margin estimate and hypothetical return-on-margin, explicitly labeled as **not** liquidation price or maximum loss.
5. Maintenance and liquidation: either externally verified venue-specific calculation with documented assumptions or `UNAVAILABLE / DO NOT INFER`. Pine typically does not know a user's live account collateral or exchange-specific real-time margin tiers automatically.
6. `WAIT / INSUFFICIENT_MARGIN_DATA` or a clear warning if stop/target, product specification, leverage or collateral facts are missing.

**TradingView simulator research:** Strategies (not indicators) support simulated leverage via margin percentages for long and short positions, including `margin_long` and `margin_short`; a margin ratio of 20% corresponds to 5:1 theoretical leverage. TradingView's broker emulator simulates margin calls under its own model, including liquidating an amount different from a particular cryptocurrency exchange's live liquidation engine. Therefore, a TradingView Strategy Tester “margin call” is **not proof** that Binance would liquidate at the same point.
Sources:
- https://www.tradingview.com/support/solutions/43000717375-how-to-simulate-trading-with-leverage-in-pine-script/
- https://www.tradingview.com/pine-script-docs/concepts/strategies/
- https://www.tradingview.com/support/solutions/43000786181-broker-emulator/

## 8. Ponder notes — competing improvement hypotheses

- **H0:** A simple no-margin analytics panel with source-grounded trade context is less misleading than an exchange-inaccurate liquidation estimate.
- **H1:** Margin/exposure validation and honest data-quality warnings add useful risk information without distorting Coach's entry method.
- **H2:** Extra margin metrics create false confidence and operational errors if account mode, fees, tiers, collateral and exchange price basis are stale or unavailable.
- **Test boundary:** Comparing static formula outputs against verified contract-specific exchange reference calculators, boundary/error cases and actual TradingView broker-emulator behavior is required before any displayed numeric liquidation estimate can be accepted.

**OPEN_UNRESOLVED:** exact venue-qualified XAUUSDT/XAUTUSDT/PAXGUSDT products, live risk-tier access, cross/isolated choices, account currency/collateral, precise multiplier and PnL models, funding/fees, mark vs last-price source, strategy emulator parity, and actual end-user leverage. **No default safe leverage is prescribed.**

## Study conclusion and checkpoint

The page-7 inventory contains 17 audited source items. All Coach numeric examples were recalculated; no original image or exercise was omitted. All math extensions, venue mechanics and TradingView technical references are distinguished from original Coach statements.

**Lesson 05 COMPLETE for PCSS source study, NOT implemented or validated as software.**

**Next source item when the owner advances:** Lesson 06 — Engulfing Pattern (PDF page 8), inspecting all original candlestick figures. Stop at this checkpoint per PCSS.
