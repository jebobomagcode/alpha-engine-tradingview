# M05–R4 supplemental audit: evidence gates and causal scope

**2026-11-11, Asia/Manila | Independent logic/source consistency review ONLY | no Pine, executable fixtures, market backtest, deployment, order, or profit claim.**

Authoritative Coach origin: [coach trading lessons.pdf](../../sources/coach%20trading%20lessons.pdf), original 35-page PDF SHA-256 481ca1adf146212316846823070db7ba78c788eae89b08db10f0694b61fe5730. This audit follows the previously authored [R4 M05 proposal](../methodology/07-mtf-context-conflicts-and-causal-states.md) and [evaluation protocol](../research/phase2-mtf-validation-and-falsification-protocol.md). Its purpose is to find an internal inconsistency, not to certify a trading edge.

## Source-grounded acceptance boundaries

| Original PDF | What Coach actually illustrates | What the proposed model must not claim |
| --- | --- | --- |
| p6, Lesson 04 | 1H/4H trend and zones; 5m/15m entry context | A universal mandatory three-timeframe agreement rule |
| p10, Lesson 08 | If selected zone is not reached, no trade; entry after closed confirming LTF candle | That a visible candle pattern alone establishes a valid setup |
| p18, Lesson 13 | Bullish SOL 4H, weakened 1H, possible bearish 15m scalp against that HTF; separate HTF-aligned long | That the 15m scalp automatically reverses the 4H structure |
| pp27–28, Lesson 21 | Strongly bullish TON 4H and very high RSI, but Coach waits for pullback and confirmation | That RSI above 70 automatically means SELL or immediately BUY |
| p32, Q&A 03 | 4H bearish, 15m consolidation: conditional short rejection OR conditional breakout long | A single unconditional direction from the shared snapshot |
| p35, final BPI note | Bearish Daily conditions coexist with temporary 4H recovery possibilities | That an unconfirmed 4H bounce is a Daily reversal, or that PSE price levels transfer to crypto |

All entries above describe the PDF's source cases; no live candles or actual order executions were reconstructed.

## Identified defect and exact MTF-04 repair

**Finding AUD-M05-01:** The earlier written MTF-04 case said _4H DOWN, 15m RANGE and no rejection_ and gave WAIT_CONFIRMATION as one expected result without first specifying whether there was a known eligible zone or a confirmed contact. This could violate R4's own status definitions and the Coach p10 waiting sequence.

The correct independent gate is conditional on *what is already known*, even while the 4H DOWN and 15m RANGE observations remain unchanged:

| Evidence status at decision time | Eligible descriptive gate | Meaning |
| --- | --- | --- |
| No known eligible zone for the selected source/profile | ZONE_INSUFFICIENT | Cannot even establish a zone-wait state |
| Eligible zone known, but not contacted by a completed qualifying touch | WAIT_ZONE | Observe for price to reach the zone; do not infer a reaction |
| Contact seems to occur only on the still-forming bar | CONTACT_PENDING | Completion/finality not established; no retrospective intrabar fill |
| Eligible zone and completed contact known, no qualifying completed reaction yet | WAIT_CONFIRMATION | Only now is this exact gate supported |
| Completed reaction exists, but entry/SL/TP/contract specification incomplete | RISK_INCOMPLETE | A signal shape does not equal risk-qualified trade |
| Needed HTF source history itself absent or invalid | DATA_INSUFFICIENT or CONTEXT_INSUFFICIENT, by the specific missing dependency | Missing data is not bearish, ranging, or a proven rejection |

The written MTF-04 row in R4 has been narrowed accordingly. This is a correction to one predeclared *paper* case, not a new trade rule. There is no assumed entry, stop, target, position or performance outcome.

## Causal self-check: availability is not a nominal timestamp

Proposed invariant: every source item that supports a decision at time tau must have its own verified available_at <= tau. For an LTF candle with opening o and closing c:

- Under R4 MTF-T0, its HTF context is frozen to the last confirmed, eligible HTF evidence knowable at o. A newly closed 4H bar cannot govern the preceding LTF candle's opening context.
- Under R4 MTF-T1, an HTF event received after c can inform a fresh decision at a later tau, if it is confirmed and available by tau. It must not be silently backdated as knowledge available at o.
- Same scheduled close time is not proof of same data availability. A 5m event available at 12:00:01 and a 4H event at 12:00:03 cannot be combined in a decision stamped 12:00:02.

**Why these conditions matter:** two implementations can both be causal yet disagree near HTF boundaries because their policies admit different evidence. Their labels should carry the selected policy ID and decision clock. This remains a research design requirement, not a demonstrated nonrepainting Pine implementation.

The external Pine engineering constraint agrees with official TradingView documentation: requesting a developing HTF series can repaint; a historical expression offset plus lookahead-on is a documented last-confirmed-HTF technique, whereas barstate.isconfirmed used *inside* request.security is not a reliable HTF finality solution. See [Other timeframes and data](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/), [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/), and [Bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/). Their runtime behavior has not been implemented or tested here.

## Ponder findings and decision

- **Preserve branch plurality.** A source-recognized 15m countertrend scalp and a possible 4H-aligned long are different scenario predicates, not votes in one majority score. Unanimity and voting remain independent challengers for later comparison, not Coach-exact rules.
- **Protect missingness semantics.** Absence of evidence for a predicate cannot silently be promoted to evidence that its opposite occurred. This avoids accidental BUY/SELL decisions from unavailable timeframe bars.
- **Preserve provenance and decision age.** Later 4H reversal evidence may invalidate a current conditional candidate, but must not rewrite an older historical snapshot as if the information was already known.
- **Source-to-market transfer is an empirical question.** Coach's SOL/BTC/TON examples and BPI equity discussion do not establish profitable parameters or transferable prices for XAUUSDT derivatives, XAUTUSDT or PAXGUSDT tokens. Feed/product and venue keys must remain separate.

## Audit outcome and limits

**AUD-M05-01 resolved in written MTF-04 classification.** PDF-source and logical consistency checked for the specific cases cited, not every manuscript statement. The inventory remains **140 deliberately constructed paper cases (30 MTF), zero executable cases or real-market backtests**; no new empirical result was added. M05/R4 is a completed *research proposal and protocol draft*, not a selected production model. Next practical research gate is harmonized cost/risk/microstructure assumptions and the precise conditions for which source-compatible entry branches can be evaluated without claiming fills or execution.