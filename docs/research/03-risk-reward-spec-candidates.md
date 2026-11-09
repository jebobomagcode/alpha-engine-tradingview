# Lesson 03 research — risk-reward, expectancy, compounding and sizing

**Source**: [Lesson 03 PCSS](../lessons/03-trading-risk-reward.md), [PDF pp. 4–5](../../sources/coach%20trading%20lessons.pdf).  
**Status:** RESEARCH ONLY — proposed, not coded or statistically validated (2026-11-09).  
**Scope:** crypto including XAUUSDT, XAUTUSDT, PAXGUSDT (product/venue distinction required).

## Core quantitative invariants

For proposed net trade model with win probability \(p\), mean realized win \(G\), mean realized positive loss magnitude \(L\), fixed total round-trip cost \(k\) in account units:
\[
E_\mathrm{net}=pG-(1-p)L-k.
\]
Zero-cost break-even:
\[
p_\mathrm{BE}=\frac{L}{G+L}=\frac{1}{1+\rho}, \quad \rho=G/L.
\]
With constant cost \(k\):
\[
p_\mathrm{BE,net}=\frac{L+k}{G+L}=\frac{1+c}{1+\rho},\quad c=k/L.
\]
These model parameters are **unverified**. For Coach's \(G=200,L=100\), \(p_\mathrm{BE}=1/3\). When \(k=10\) account units, \(p_\mathrm{BE,net}=110/300\approx36.6667\%\). No source lesson asserts those exact formulas or fee inputs.

Per fixed-size \(n\)-trade block, wins \(w\):
\[
P\&L=wG-(n-w)L,\quad C_\mathrm{end}=C_0+P\&L.
\]
At \(w=9,n=20,G=200,L=100,C_0=5000\), net=700, ending 5700.

### Compounding models — NOT equivalent

- **Fixed R per 20-trade cycle:** constant initial cycle capital percent risk \(f=0.02\) and same 9W/11L composition imply \(C_{j+1}=C_j[1+7f]=1.14C_j\). Cycle sequence: 5000,5700,6498,7407.72,8444.8008,9627.072912.
- **Risk recalculated each individual trade:** conditional full +2R / −1R gives \(C_{20}=5000(1.04)^9(0.98)^{11}\approx5698.45195049\). With this simplistic constant percentage and only win/loss outcomes, multiplication commutes, but a real strategy can introduce path-dependence through stop modifications, margin limits, drawdown limits, fills and variable transaction costs.
- Neither model means that subsequent 45% winning composition is known or guaranteed. Separate cash equity, margin, free collateral and unrealized P/L in future specs.

## Planned risk-calculator interface (candidate, not actual code)

Inputs: account equity currency/amount; target risk fraction or nominal risk cap; market/instrument and venue; long/short side; intended entry/stop/target prices; valid tick size and quantity precision; payout/contract multiplier; fee model; optional funding, spread and slippage assumptions.

Outputs: planned absolute risk and account percent; gross price-target ratio; estimated cost-adjusted payoff ratio; tentative risk-constrained quantity; key uncertainty flags and reasoned WAIT/INSUFFICIENT if missing/invalid. Never fabricate unavailable data.

For straightforward linear USDT instruments with payout multiplier \(m\), nominal loss-to-stop is \(q m |P_e-P_s|\) and prospective target P&L is \(qm|P_t-P_e|\), before costs. Derivative product specifics vary; this is not universally safe across inverse or quanto products. Check contract minimums, liquidation level, margin and stop gap/slippage separately. Leverage changes funding/margin/exposure, **not a magic waiver of price-distance loss**.

## Design cautions and tests to plan

**Source fidelity:** reproduce Coach's six tables/exercises exactly, including 1:1 comparison and 2% risk between-cycle reset; source labels not silently corrected.

**Unit fixtures (future):** positive/negative/zero risk stop distances, long/short side, nonfinite/zero price, no room for costs, negative balance, multiplier mismatch, tick/precision rounding, cost units, insufficient margin, ambiguous RR convention.

**Statistical review (future):** do not infer a true 45% win probability from a hand-built 20-trade example. Compare actual realized returns and costs, sample sizes, multiple-testing effects, regime shifts, baseline strategy, and out-of-sample uncertainty. Distinguish arithmetic identity from empirical predictive success.

**Simulation caveats:** TradingView's broker emulator fills only under assumptions derived from available chart bars; if stop and target occur within one bar, order sequence is ambiguous without trustworthy lower-TF observations. Commission, slippage, margin, request.security timing, funding availability and live fills require further investigation. Official source:
https://www.tradingview.com/support/solutions/43000786181-broker-emulator/
https://www.tradingview.com/support/solutions/43000628599-strategy-properties/

**Crypto and gold tokens:** do not assume XAUUSDT perpetual, XAUTUSDT token markets or PAXGUSDT token markets have identical contract units, margins, fees, volume profiles, funding and settlement.

## Decision checkpoint

**Candidate direction:** risk math should ultimately be a distinct, testable analytical layer beneath chart visuals and any strategy backtester, with assumptions exposed. It should not convert a positive planned RR into a confirmed trade signal or promise of profit.

**OPEN_UNRESOLVED:** exact risk fraction and sizing conventions, instrument contracts, fee/funding sources, stop/target methods, live-vs-historical calculation semantics. These depend on later Coach lessons and explicitly scoped independent research; no implementation decision locked.
