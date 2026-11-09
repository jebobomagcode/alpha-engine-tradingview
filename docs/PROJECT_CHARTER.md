# Project charter

**Project:** Alpha Engine TradingView
**Canonical repository:** https://github.com/jebobomagcode/alpha-engine-tradingview
**Established:** 2026-11-09 (Philippines time)
**Status:** Planning/documentation; implementation not started.

## Objective
Develop a faithful, comprehensible and ultimately rigorously evaluated TradingView trading research system grounded in Coach Fredy's sole supplied lesson PDF and substantially improved with independent intelligence, mathematics, research, quantitative validation, and engineering.

This is **not** an implementation, fork, continuation, or migration of any earlier project. It begins from a clean intellectual and engineering slate.

## Four layers of knowledge
1. **Original Coach methodology:** explicit statements/diagrams/examples within the 35-page PDF. These are primary source claims, not externally validated trading facts.
2. **Clarified methodology:** our formalizations of underspecified concepts; assumptions and alternatives explicit.
3. **Independent enhancements:** clearly attributed outside techniques and original research to address gaps, robustness, analytical capabilities, or usability.
4. **Empirically validated findings:** claims bounded by actual reproducible evidence, clearly separated into software correctness, signal validity, and financial performance.

Allow critical review of the original Coach rules and the proposed enhancements. Preserve a usable Coach-baseline variant to test whether changes improve or degrade outcomes.

## Success criteria
- All source material covered in original sequence with verified section/page/figure coverage and retained open questions.
- An evidence ledger for every formalized rule: original passage, interpretation, assumptions, and tests.
- Robust, explainable chart states (including uncertainty, nonconfirmation, WAIT and NO TRADE).
- TradingView scripts, when authorized, that compile and demonstrate actual tested chart behavior rather than relying only on theoretical reasoning.
- Appropriate nonrepainting, MTF alignment, confirmed-bar semantics, risk-modeling and performance checks.
- For a strategy, backtests that document commissions, spreads/slippage assumptions, overfitting risks, out-of-sample evaluation and realistic simulator limitations.
- A versioned GitHub record sufficient to reconstruct decisions and resume work after a lost chat.

## Explicit non-goals / boundaries
- No reliance on earlier Coach Fredy projects, repositories, prior engine code, private previous project decisions, Sites, Cloudflare infrastructure, or deployments.
- No expectation that Coach Fredy will supply new lessons; the provided PDF is the complete Coach corpus.
- No fabrication of additional Coach teachings, technical indicators, or proprietary rules as if source-backed.
- No premature trading automation, live orders, guaranteed outcomes, or untested profitability claims.
- No mandatory active-recall quizzes; the user requests these when wanted.
- No editing Pine Script or executing study lessons before the user's later explicit go-ahead.

## Guiding principles
- Source fidelity, then comprehension, then formalization, then challenges/research, then testable improvement.
- Precise provenance and explicit uncertainty.
- Mathematical clarity; practical TradingView limits and user experience matter.
- Keep essential default displays understandable, avoid chart clutter, provide meaningful diagnostic reasons.
- An indicator-first / strategy-ready architecture is the present working decision.
- Independent testability and frequent verified GitHub commits matter more than long uncheckpointed sessions.
