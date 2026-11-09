# Lesson 05 — Leverage, Margin and Solvency Research Candidates

**Status:** PROPOSED ONLY; not code, actual liquidation calculation, backtest, brokerage connection, trade signal, or investment advice.  
**Original Coach:** [PDF p. 7](../../sources/coach%20trading%20lessons.pdf); [complete PCSS Lesson 05](../lessons/05-leverage-margin.md).  
**Independent research date:** 2026-11-09.  
**Crypto scope:** general cryptocurrency plus specific gold-related symbols XAUUSDT, XAUTUSDT, PAXGUSDT; **no cross-product assumptions or silent Forex implementation**.

## 1. Definitions and core equation candidates

For a linear quote-settled position with entry \(P_e\), quantity \(q\) in base asset units, leverage \(\lambda>0\), initial margin \(M_0\), notional \(N=qP_e\):
\[
N=\lambda M_0,\qquad M_0=\frac{N}{\lambda}.
\]
When contract multiplier \(m\ne1\), use product-specific payout definition instead of assuming \(qP_e\) represents exact notional. For a linear long with move \(r=(P-P_e)/P_e\):
\[
\Delta\mathrm{PnL}=Nr,\qquad\mathrm{ROM}_{\mathrm{initial}}\approx\lambda r.
\]
Do not apply linear formulas unchanged to inverse/quanto or token products. Collateral and margin requirements can include fees/reserves and tiers.

**Invariant:** holding notional fixed, changing leverage alone does **not** change gross price PnL. Holding margin fixed, changing leverage changes permissible notional, *if* fully used. Numerically verified test cases:
- $100 margin, 1x/10x/20x -> $100/$1,000/$2,000 exposure; -2% -> -$2/-$20/-$40.
- $100 position, 1x/10x -> $100/$10 initial margin, while -2% -> -$2 for both.

## 2. Strong blockers against unsafe “calculator” features

- Insufficient maintenance margin rate or notional risk bracket.
- Unknown source of liquidation price: mark vs last; mark/index specification unavailable.
- Incorrect/is-it-spot check: a token spot market does not liquidate solely because its unlevered asset price falls.
- Cross margin: unknown collateral shared with other positions and positions that alter the liquidation level.
- Isolated margin: unknown added/removed margin and actual protected collateral scope.
- Missing contract multiplier, quantity step, tick size, unrealized fee/funding obligations and other reservations.
- Account base/quote/settlement currency conversion unknown.
- Unrealistic assumption that configured leverage is actual effective leverage.
- Stop price beyond likely liquidation region; stop order execution not guaranteed, even if entered.
- No dependable user account link; Pine chart alone does not reveal the user's available collateral or open positions.

**Decision proposal:** if exchange-correct risk inputs are missing, show "LIQUIDATION PRICE: UNAVAILABLE" rather than inventing a percentage formula. The system may still report exact price-distance risk under stated assumptions.

## 3. Isolated vs cross margin

The venue's margin allocation determines collateral available to losses:
- *Isolated*: a position-specific allocation and applicable rules; may limit direct exposure of other unallocated funds, but fees, liquidation losses, and user reallocation can affect outcomes.
- *Cross*: pool of account collateral across positions; losing one position may consume margin supporting others; aggregate risk matters.
Source, Binance Academy: https://www.binance.com/en/academy/articles/what-are-isolated-margin-and-cross-margin-in-crypto-trading

Do not simply display “isolated safe” or “cross risky”; they manage collateral differently, and tradeoffs depend on user strategy and account structure.

## 4. Mark price, maintenance and risk tiers

Official Binance Futures liquidation FAQ (updated 2026-01-04): mark price drives liquidation and unrealized PnL; last price is the most recent transaction print. Liquidation is triggered as collateral falls below maintenance margin requirements. Position size affects margin/risk tiers. The available material does not establish the exact current tier or permissible leverage for any specific gold contract:
https://www.binance.com/en/support/faq/detail/360033525271

**Research challenge:** verify exact contract rule and version at development time, including symbol, venue, quote currency, settlement, market regime, funding schedule, size tiers, liquidation fees, insurance conditions, and possible regional unavailability.

## 5. TradingView specific non-equivalence

TradingView strategies simulate a broker and leverage using margin settings (e.g. `margin_long=20` means 20% account margin, theoretical 5x leverage). Its broker emulator's forced liquidation behavior is a separate software model from any particular exchange's real liquidation engine; it may close 4 times the amount needed to cover a margin call in simulation.
https://www.tradingview.com/support/solutions/43000717375-how-to-simulate-trading-with-leverage-in-pine-script/
https://www.tradingview.com/pine-script-docs/concepts/strategies/
https://www.tradingview.com/support/solutions/43000786181-broker-emulator/

**Research-only requirement:** if a future strategy is authorized, publish a clear broker-model ≠ live-exchange-model warning. Do not present backtest margin call timestamp as confirmed Binance liquidation timestamp.

## 6. Test plan once coding is authorized

- Arithmetic invariants for fixed position vs fixed margin.
- Linear long and short price movement; positive/negative/zero invalid prices and exact price currency units.
- Leverage = 0/negative/nonfinite, notional <=0, margin > equity, leverage cap exceeded.
- Contract size and tick/step rounding; precision loss on tokens.
- Funding/fees balance drift; conflicting BTC/crypto/gold product feeds.
- Maker vs taker fee, spread, entry and exit slippage.
- Isolated to cross, additional margin, maintenance margin rate changes, multiple simultaneous positions.
- Mark/last divergence and missing mark price at certain timestamps.
- Stop would be triggered later than liquidation, stop market order fills beyond intended stop.
- Unknown account equity; indicator should not assume access to private data.
- Compare any implemented arithmetic against the venue reference calculator and TradingView chart runtime. No source-specific claims of acceptance until tested.

## 7. Ponder decision

At this early stage, **prioritize a truthful risk hierarchy**: market exposure -> intended loss-to-stop -> margin/solvency -> product-specific liquidation uncertainty. Reject simplistic formulations like “20x means liquidation exactly 5% away”. Neither Coach's low-leverage advice nor ours establishes a universally safe numeric multiplier.

No specific risk % or leverage default selected. No source-unauthorized implementation produced.

**Next:** Lesson 06 — Engulfing Pattern, original PDF page 8. Do not auto-advance.
