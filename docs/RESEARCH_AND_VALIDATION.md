# Research, formalization and validation policy

## Goal
The project is not merely a Coach-method clone. It aims to produce a substantially improved TradingView analytical system **if improvements withstand scrutiny**. More indicators and more complex logic are not automatically better.

## Rule record schema (in use for Phase 2 conceptual research)
Record for each candidate rule:
- Stable rule ID, title, target lesson, PDF page/figure/quoted minimal source anchor.
- Provenance: COACH_EXPLICIT, INTERPRETATION, INDEPENDENT_EXTENSION, EXPERIMENTAL, VALIDATED, OPEN_UNRESOLVED.
- Formal definition (variables, bar indexing, price source, timestamps, confirmation-close semantics, thresholds).
- Inputs, instruments, sessions, HTF/LTF mapping, data/precision limits.
- When the signal becomes knowable, historical vs real-time behavior, repaint/lookahead audit.
- Expected outputs and user-visible blocking/wait reasons.
- Competing valid interpretations and which measurements could distinguish them.
- Unit tests, synthetic fixtures, chart observations, failure cases and links to evidence.
- Current confidence and evidence status; not a generic 'high probability' label.
- Relationship to baseline Coach mode vs optional enhanced mode.

## Hypothesis-driven enhancement procedure
1. Identify a real deficiency or missing specification in the source or current system.
2. Form competing candidates (including a simple baseline and 'do not add this feature').
3. Define what observation would change the decision before using historical results.
4. Independently verify technical claims with current official documentation and credible references.
5. Implement only after authorized; test isolated behavior and source fidelity.
6. Compare outcomes with appropriate controls; document negative or inconclusive results, not just wins.
7. Retain original baseline, reject low-value complexity and avoid feature inflation.

## Testing tiers (separate claims)
- **Source fidelity:** PDF page/image checked; statement accurately interpreted; departures declared.
- **Algorithmic/deterministic correctness:** pure fixture tests, bar-by-bar consistency, boundary and invalid input cases.
- **TradingView runtime:** actual Pine compilation, chart overlays, multi-timeframe alignment, alert/message semantics, object/plot limits. Code review alone is not enough.
- **Temporal validity:** no hidden lookahead, no unreported future-pivot leakage, appropriate confirmed-bar and security-request handling, realistic historical vs live differences.
- **Strategy simulator validity (if built):** instrument/tick properties, position sizing, transaction costs, slippage, spread approximations, execution model, intrabar assumptions, partial fills and stop/target ordering.
- **Financial evidence:** baseline comparisons, multiple symbols/timeframes/regimes, predeclared out-of-sample or walk-forward sets, sensitivity, instability, multiple-testing/overfit checks, drawdown and trade counts. Historical simulation does not guarantee live results.
- **User acceptance:** readability, relevant visible zones/labels, meaningful WAIT/NO TRADE diagnostics, no misleading certainty, explainable decision path.

## Still-unresolved methodological decisions
No final definitions yet for swing/pivot confirmation, HH/HL/LH/LL, BOS/CHoCH timing, S/R zone clustering, OB/FVG boundaries, Fibonacci anchor selection, confirmation/strong candles, liquidity sweep, confluence weights, intra-bar signals, risk/position sizing, or cross-timeframe disagreements. These are **research questions**, not completed findings. Phase 2 now has initial [traceability](methodology/00-source-to-rule-traceability.md), [market-structure](methodology/01-causal-market-structure.md), [entry/risk](methodology/02-topdown-entry-state-and-risk.md), [zone](methodology/03-zones-sr-ob-fvg-fibonacci.md) and [reconciliation](METHODOLOGY_RECONCILIATION.md) documents. They contain proposed mathematics and manual expected cases, not runnable detectors or market validation.

## Engineering notes
Pine Script is a target environment; official language/version constraints should be checked at implementation time. Avoid coupling chart visuals to strategy order simulation. Shared formal specs are more important than speculative premature code sharing. No trades or live execution authorized.
