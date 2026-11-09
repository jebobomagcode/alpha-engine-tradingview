# Lesson 10 research candidates — Conditional Range Entries and Confirmation Break

**Status:** OPEN / RESEARCH ONLY, 2026-11-09. No Pine code, live chart test, backtest or empirical result.  
**Source:** [Coach PDF pp. 12–13](../../sources/coach%20trading%20lessons.pdf), [source-complete Lesson 10](../lessons/10-marking-support-resistance.md).  
**Owner focus:** crypto, with distinct XAUUSDT (depending on venue a gold-reference derivative), XAUTUSDT and PAXGUSDT markets. Do NOT project FOREX.com Gold Spot / U.S. Dollar levels onto those products.

## Original concrete constraints

- 1H support 4,670–4,680; resistance 4,730–4,750; price sideways.
- 5m price around 4,710 in middle -> not ideal entry.
- SELL near resistance only after bearish reversal (engulfing or shooting star); entry on break of confirmation; SL 4,755, TP 4,670–4,680.
- BUY near support only after bullish reversal (engulfing or hammer); entry on break of confirmation; SL 4,665, TP 4,730–4,750.
- No qualifying reversal -> invalid setup, NO TRADE.
- Source does not specify candle break threshold, exact entries or realized performance.

## Four precise unresolved design decisions

### A. Is sideways range trading an exception?

Lesson 07 says avoid sideways unless higher-timeframe context; Lesson 10 illustrates optional range entries in 1H sideways market. Compare:
1. Exception mode: range trade permitted with Coach's zone + confirmation at boundary.
2. Strict trend mode: require 4H directional context even when 1H sideways (not present in Lesson 10 source).
3. Illustration-only: mark potential range scenarios but refrain from executable signals until other criteria.

No policy selected. Test source fidelity against whole PDF before adoption.

### B. What is the break of confirmation?

Lesson 08: enter after confirmation candle closes. Lesson 10: enter on break of confirmation. Hypothetical policies:
- high of bullish confirmation / low of bearish confirmation breached AFTER close (most literal but unverified interpretation);
- body boundary breached after close;
- subsequent candle closes beyond prior extreme;
- immediate entry at confirmation close (Lesson 08 option; fails stronger break condition unless separately justified).

A two-stage sequence is plausible but **NOT Coach-defined math**. Specify valid ordering, trigger expiry, order type, tick buffer and what happens if trigger price is skipped by a gap. TradingView official strategy order fill semantics: https://www.tradingview.com/pine-script-docs/concepts/strategies/.

### C. Which reversal evidence counts?

Page 13 explicitly names bullish engulfing/hammer for buy and bearish engulfing/shooting star for sell. Lesson 08 adds strong-body candles and rejection+follow-through as options. Possible scope-specific policy or inclusive policy must be declared; don't silently erase Lesson 08 alternatives nor impose them without evidence.

### D. What price defines risk and target?

Coach specifies zone ranges plus stop prices, but not entry or exact target inside opposite zone. For linear price-distance model:
- Long planned RR=(T-E)/(E-S), if S<E<T.
- Short planned RR=(E-T)/(S-E), if T<E<S.
- Example SELL hypothetical E=4740,S=4755,T=4680 => risk 15, reward 60, RR 4.
- Example BUY hypothetical E=4675,S=4665,T=4730 => risk 10, reward 55, RR 5.5.

**Neither entry nor fixed RR appears as an achieved result in Coach.** An actual confirmation break can change RR, including making a proposed stop invalid or target too close. Stop offsets of 5 source price units must not become universal crypto defaults.

## Candidate causal state and source provenance

Instrument qualified and confirmed HTF zone -> LTF price located in/away from relevant zone -> reversal candle candidate -> candle complete -> optional subsequent break -> entry estimate/fill -> risk check. Explicit negative/unknown states: MID_RANGE, NO_ZONE_CONTACT, NO_REVERSAL, WAIT_CANDLE_CLOSE, WAIT_CONFIRMATION_BREAK, UNKNOWN_TRIGGER, UNKNOWN_RR, BAD_FEED, HTF_CONFLICT.

Source chart: two actual screenshots, both Gold Spot / U.S. Dollar FOREX.com, 1H and 5m. The example does not include verified year, trade fills, contract size or actual maker/taker/funding costs. Must not infer crypto gold pricing from it.

## Future comparative checks (not executed)

1. 1H sideways, 5m midrange 4,710 -> no entry candidate.
2. Zone touched but reversal pattern absent -> invalid under this example.
3. Confirmation candle appears forming then reverses by close -> cannot report confirmed reversal.
4. Confirmation closes yet price never breaks chosen trigger -> remain WAIT, not an executed trade.
5. 1H/4H disagreement -> report policy unresolved.
6. Support recognized using pivot confirmed AFTER 5m touch -> no retrospective eligibility.
7. Source screenshot mistakenly treated as XAUUSDT or PAXGUSDT -> instrument mismatch.
8. Different potential entries from same zone -> materially different RR; no precise RR before entry.
9. Fill gaps/slippage and same-bar stop/TP -> backtest emulator assumptions, not certain sequence.
10. Strong-body alternate confirmation vs named hammer-only range interpretation -> policy-specific classification, no guessed equivalence.
11. No source market actual win/loss dataset -> no statistical confidence or profitability claim.
12. Compare zone+reversal against simpler baselines with holdouts, realistic fees and venue-qualified crypto candles when coding/testing authorized.

**Ponder decision:** Do not turn the screenshot into a hardcoded trade plan. Preserve explicit observations, unknown trigger rules and WAIT/NO TRADE semantics. Compare source-compatible variants once full study complete. Next Lesson 11 p. 14 on user request.
