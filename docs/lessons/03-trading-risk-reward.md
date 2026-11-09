# Lesson 03 — Trading Risk Reward (PCSS source-complete study)

**Status:** COMPLETE — source-order teaching, precise audit of all original calculations, supplementary mathematical proofs, research notes, and open specification questions.  
**Source:** [Coach Fredy's original PDF, pp. 4–5](../../sources/coach%20trading%20lessons.pdf)  
**Coach PDF SHA-256:** `481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730`  
**Full PCSS SHA-256:** `99d4370e53e00e54c3d0f0c796e29a5fc9e5b7b437a01137e4b08086e37dec56`  
**Date:** 2026-11-09 (Asia/Manila).  
**Scope:** original section 03, pp. 4–5. Page images inspected at 144 dpi and text extraction crosschecked. These two pages contain textual simulations and colored bullet/icons, **no candlestick charts, screenshots, stand-alone visual diagrams, assigned exercises, or originally stated proof**. All independent formulas below are labeled separately. **No Pine code, financial backtesting, live orders, or deployments.**

## Original source inventory in exact order

| ID | Original source element | Exact assumptions/numerical content (source-level summary) | Status |
| --- | --- | --- | --- |
| 03-01 | p. 4 title and 1:2 RR simulation / Setup | Capital PHP 5,000; risk per trade 100; reward per win 200; risk:reward 1:2 | Studied and verified |
| 03-02 | p. 4 Scenario 1 — 10 trades, 50% win rate | 5 wins at 200 each = 1,000; 5 losses at 100 each = 500; net +500; new capital 5,500 | Verified |
| 03-03 | p. 4 Scenario 2 — 10 trades, 40% win rate | 4 wins earn 800, 6 losses cost 600; net +200; capital 5,200 | Verified |
| 03-04 | p. 4 Scenario 3 — 10 trades, 30% win rate | 3 wins earn 600, 7 losses cost 700; net −100; Coach calls it a loss; ending 4,900 derived by us (not written) | Verified |
| 03-05 | p. 4 “Lesson” win-rate note | At 1:2, “at least ~35–40% winrate” | Coach approximation qualified: exact gross theoretical break-even 1/3; 4 of 10 minimum profitable in a ten-trade integer sample |
| 03-06 | p. 4 “LONG TERM (20 TRADES – REALISTIC)” | 45%: 9 wins of 200 = 1,800, 11 losses of 100 = 1,100; net +700, capital 5,700 | Arithmetic verified; “realistic” is an unvalidated descriptive assertion |
| 03-07 | p. 4 “CONTINUATION (COMPOUND)” | Next capital 5,700; 2% risk approximately 114; 9 wins at 228 = 2,052; 11 losses at 114 = 1,254; net 798, capital 6,498 (about 6,500) | Verified; risk reset between cycles, not after each trade |
| 03-08 | p. 4 “AFTER FEW CYCLES” | Starting 5,000, following cycles approx. 6,500 → 7,500 → 9,000+ | Directionally compatible with repeated +14% cycle assumption, not exact cycle-by-cycle accounting or evidence of actual repeatability |
| 03-09 | p. 4 final clause continued p. 5 | “Kahit hindi mataas winrate mo” / “Lumalaki pa rin account mo” | Source continuity preserved |
| 03-10 | p. 5 comparison 1:1, same 45% win rate | 9 wins at 100 = 900; 11 losses at 100 = 1,100; net −200 | Verified, **but holding the same win rate across distinct targets is a counterfactual assumption, not an observed fact** |
| 03-11 | p. 5 “FINAL LESSON” on 1:2 | You need not always win; profit is possible even with more losing trades | Valid under fixed payout/cost assumptions |
| 03-12 | p. 5 “Sa maling RR” and conclusion | A skilled trader can lose under unfavorable payoff sizing; magnitudes of wins/losses matter more than count alone | Clarify: payoff distribution and win probability jointly determine expectancy, plus costs |

## 1. Risk:reward and units

**COACH_EXPLICIT:** 5,000 PHP starting account, 100 PHP per full loss, 200 PHP per full win, hence risk:reward = 1:2.

**INDEPENDENT EXPLANATION:** Let initial account equity \(C_0=5000\), planned risk \(L=100\), planned reward \(G=200\). Risk fraction \(f=L/C_0=0.02=2\%\). The **R-multiple** unit is 100 PHP, so stopped trades are −1R and full targeted winners +2R, ignoring costs.

Do not interpret 1:2 as a guarantee. It is *planned* payoff ratio, not realized win/loss. Trades can exit at different prices and incur fees.

## 2. Scenarios — exact arithmetic audit

For \(n\) trades with \(w\) wins and \(n-w\) losses, with fixed gain and loss:
\[
\mathrm{Net}=wG-(n-w)L,\qquad C_{\mathrm{end}}=C_0+\mathrm{Net}.
\]

| Coach scenario | Wins and losses | Gross positive | Gross negative | Net | Ending capital |
| --- | --- | --- | --- | --- | --- |
| 10, 50% | 5W, 5L | PHP 1,000 | PHP 500 | +PHP 500 | PHP 5,500 |
| 10, 40% | 4W, 6L | PHP 800 | PHP 600 | +PHP 200 | PHP 5,200 |
| 10, 30% | 3W, 7L | PHP 600 | PHP 700 | −PHP 100 | PHP 4,900 (derived) |
| 20, 45% | 9W, 11L | PHP 1,800 | PHP 1,100 | +PHP 700 | PHP 5,700 |
| 20, 45%, **next cycle** | 9W, 11L, L=114, G=228 | PHP 2,052 | PHP 1,254 | +PHP 798 | PHP 6,498 |
| 20, 45%, **1:1 comparison** | 9W, 11L, L=G=100 | PHP 900 | PHP 1,100 | −PHP 200 | PHP 4,800 (derived) |

**Verdict:** no arithmetic mistakes found in Coach's stated scenario totals, but scenario-to-reality assumptions are strong. Original page 5 does not explicitly say ending 4,800; we derive it.

## 3. Exact gross break-even win rate and sample-size caveat

**INDEPENDENT DERIVATION (not in original PDF):** Define winning probability \(p\), average realized win \(G>0\) and average realized absolute loss \(L>0\). Gross expected payoff:
\[
E=pG-(1-p)L=p(G+L)-L.
\]
At break-even \(E=0\), so
\[
p_{\mathrm{BE}}=\frac{L}{G+L}=\frac{1}{1+\rho},
\]
where \(\rho=G/L\) is **reward/risk** (not risk:reward). For 1:2 planned risk:reward, \(\rho=2\), so \(p_{\mathrm{BE}}=1/3\approx33.33\%\). Strictly positive expected gross result requires \(p>1/3\).

**Coach approximate “at least ~35–40%” reconciled:** At 35% there is positive expected gross P&L under the model, while a **ten-trade sample** has integer wins: 3 of 10 loses and 4 of 10 profits. A 35% *empirical* win rate cannot occur in exactly ten binary trades. This is a useful discretization insight, not a Coach-origin statement.

The actual unknown winning probability may not equal a small sample's observed win rate. The source provides no probability model, confidence interval, drawdown or market distribution.

## 4. Twenty-trade example

**COACH_EXPLICIT:** at 45%, \(9\times200-11\times100=+700\) PHP, capital 5,700; \(+14\%\) relative to initial 5,000. More losses than wins but positive net.

**INDEPENDENT CAUTION:** Results assume constant **monetary** risk per trade for a whole block. They ignore transaction costs, funding (where applicable), variable stops, partial fills, missed targets, gaps, stop slippage, and correlated outcome streaks. “Realistic” is Coach's label, **not empirical support** that 45% or 2R is achievable across our crypto/gold markets.

## 5. Compound continuation across twenty-trade cycles

**COACH EXPLICIT:** After first 20-trade cycle, risk 2% of current 5,700 PHP = 114 PHP; 2R target = 228 PHP. Exactly 9W/11L produces \(9(228)-11(114)=798\), new 6,498 PHP. Original later sequence 6,500 → 7,500 → 9,000+ is illustrative and approximate.

**INDEPENDENT FORMALIZATION:** Each cycle nets 7R from 9 wins and 11 losses. If 1R is fixed as 2% of capital **at the start of that cycle**, then cycle return is \(7(0.02)=14\%\). Under the *unrealistically constant winning composition assumption*,
\[
C_n=C_0(1+0.14)^n.
\]

| Completed cycles | Exact hypothetical capital (PHP) |
| --- | --- |
| 0 | 5,000 |
| 1 | 5,700 |
| 2 | 6,498 |
| 3 | 7,407.72 |
| 4 | 8,444.8008 |
| 5 | 9,627.072912 |

**Major distinction:** If 2% of **current equity** is risked on *each* trade, the same nine winners and eleven losers yield
\[
C_{20}=5000(1.04)^9(0.98)^{11}\approx5698.45195,
\]
not 5,700. Both models are arithmetically coherent and differ because returns compound after each trade rather than reset at cycle boundaries. Neither reproduces guaranteed future growth. This choice must be explicit in future software.

## 6. Same 45% win rate at 1:1

**COACH EXPLICIT:** \(9(100)-11(100)=-200\) PHP. His comparison highlights that reward/loss magnitude matters.

**Critical PONDER qualification:** **changing the profit target can change the chance of hitting the target.** Holding win rate at 45% while switching from 1:2 to 1:1 is an instructive controlled arithmetic thought experiment, **not an empirical estimate** that 1:2 outperforms 1:1 on the same market data. Compare full realized after-cost outcome distributions, not just hypothetical payout pairs.

For 1:1, the zero-cost break-even rate is 50%. More generally the effect depends jointly on \(p\), mean win, mean loss and execution costs.

## 7. Source final lesson (p. 5)

**COACH EXPLICIT:** At 1:2, you don't have to win every trade, and even more losing trades than winners can still yield money. At a poor ratio, even skill may not prevent loss. The magnitude of wins and losses matters.

**INDEPENDENT REFINEMENT:** The complete mathematical requirement is **positive net expected payoff after actual transaction costs**, followed by risk-of-ruin, drawdown, model uncertainty and statistically defensible performance evaluation. A favorable intended risk-reward ratio alone does not establish a profitable system. This is an extension, not Coach's original claim.

## 8. Costs, sizing and realistic crypto/gold instruments — extension only

**Fee-adjusted expectancy:** let \(c\ge0\) be constant *round-trip execution cost per attempted trade* in units of the original risk \(L\), including fees/spread/slippage in an illustrative simplified model:
\[
E/L=p\rho-(1-p)-c=p(\rho+1)-1-c.
\]
For \(\rho=2\), \(c=0.1\) (10 PHP cost per trade with 100 PHP at risk), break-even is \(p=(1+0.1)/3\approx36.67\%\), not 33.33%. In practice cost depends on market, fill and quantity, not always constant.

**Position sizing:** for a simplified USDT-quoted linear product with entry \(P_e\), stop \(P_s\), target \(P_t\), and position size \(q\) in underlying/base units, nominal risk before fees is \(\mathcal R=q|P_e-P_s|\), nominal reward \(q|P_t-P_e|\), hence reward/risk distance ratio = \(|P_t-P_e|/|P_e-P_s|\). For a contract-based product with per-contract multiplier \(m\), nominal risk becomes \(q\,m\,|P_e-P_s|\). Confirm exact exchange contract semantics and account/settlement currency; do not assume all crypto/gold markets share a one-unit payout multiplier.

**Illustrative independent example:** A linear USDT pair at entry 100 USDT, stop 95 USDT, intended 2R target 110 USDT, 100 USDT maximum planned price loss (before fees) implies \(q=100/(100-95)=20\) units and 2,000 USDT nominal exposure. It is **not** a recommendation or an actual Coach example; execution could exceed planned loss.

**Gold-related scope D-013:** XAUUSDT may represent a reference-gold-price perpetual with contract/funding/margin mechanics; XAUTUSDT and PAXGUSDT represent distinct token markets, potentially spot or derivative listings depending on venue. Never treat gold-linked symbols as fungible or assume uniform fees/funding/spreads, mark prices, contract multipliers, or stop fill behavior. All must be checked at venue level if implementation eventually begins.

**TradingView simulator limitations (independent official sources):** strategies use a broker emulator based on available chart data; its commissions, slippage, limit fill assumptions, margin, and intrabar movement assumptions must be configured consciously. Official docs: 
- https://www.tradingview.com/support/solutions/43000786181-broker-emulator/
- https://www.tradingview.com/support/solutions/43000628599-strategy-properties/
- https://www.tradingview.com/pine-script-docs/concepts/strategies/

**Binance current provider context (reference, not universal):** Binance's futures fee FAQ (updated 2026-10-22) distinguishes trade commissions and funding; product-specific contract rules matter:
https://www.binance.com/en-PH/support/faq/detail/98488a516eb84e3eb34605683dffd554
This is not an authorization to connect an account or trade.

## Ponder: testable future improvements, not predetermined features

- **Baseline:** Coach's idealized fixed-R, fixed payoff simulations; preserve as source fidelity reference.
- **Enhancement hypothesis A:** before a setup is interpreted as favorable, calculate **price-distance R:R** and projected **after-fee R:R** with instrument-appropriate parameters, while clearly exposing assumptions.
- **Hypothesis B:** adjust allowed position size to predefined account-risk budget using stop distance and contract multiplier; do not rely on leverage or notional alone.
- **Hypothesis C:** display WAIT/INSUFFICIENT if entry, stop, target, tick/contract spec or actual costs are not available, rather than inventing a precise expected profit.
- **Hypothesis D:** optional risk reports (streak loss sensitivity, drawdown, sample-size confidence, expectancy under realized win/loss distribution); do not claim statistical edge without sufficient evidence.
- **Disconfirmation:** if uncertainty in fees, fills, exchange contract details or unstable win-rate estimation undermines accuracy, prefer explicit bounds or no calculation.

### Formal open specification questions

1. Is risk measured per trade from initial balance, per cycle, or dynamically from real-time equity?
2. Which profit/stop prices and market structure justify them? Coach's later lessons may clarify.
3. What position-sizing rule and contract multiplier are valid for each specified crypto venue/product?
4. How should maker/taker fees, funding and unrealized P/L be modeled; what input data does Pine expose?
5. If both stop and take profit lie inside one chart candle, what fill-order assumptions are valid?
6. What drawdown/streak/ruin and after-cost expectancy diagnostics justify a signal?
7. How do we estimate actual win rates honestly without lookahead, survivorship and optimization bias?

## Verified page-scoped study conclusion

- Every original p. 4–5 calculation, setup, two-part continuation sentence, illustrative growth forecast, comparison and closing lesson was covered.
- Independent arithmetic recalculation confirms source totals. The exact mathematical threshold is **33.33%** zero-cost, while Coach's “~35–40%” is a practical approximation; 4/10 winning trades is the smallest positive 10-trade example.
- Fixed risk per cycle versus dynamic fractional risk has been explicitly disambiguated.
- No source charts, tables or graphics were omitted; pages are text-only with formatting icons.
- No performance or causal trading advantage was tested; all proposed software concepts remain unimplemented and pending approval.
- **Lesson 03 complete at PCSS study level.** Next source section: **Lesson 04 — Time Frame**, PDF p. 6, only on user's next direction.
