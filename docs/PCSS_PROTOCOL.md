# PCSS operational study protocol

This is a **recovery-oriented summary**, not a replacement for the complete user-provided PCSS (exact identity in SOURCE_MANIFEST.md).

## Intent
Learn Coach Fredy's complete set of lessons rigorously and cumulatively, not memorize isolated patterns, rush through pages, or turn them into implementation immediately. Respect original source order, including all definitions, qualifiers, examples, figures, activities, and notes. Treat each section as a teaching unit with source tracking.

## Procedure for each manageable portion
1. **Source inventory:** locate the original PDF page(s). Enumerate all relevant paragraphs, defined trading terms, diagrams, image-embedded details, examples, conditions, exercises and qualifications. Inspect figures, not just extracted PDF text. Track items one by one.
2. **Original teaching:** preserve Coach's actual statements and sequence. Present original meaning and vocabulary first; explain Taglish/technical terms without rewriting their provenance.
3. **Intuition and visualization:** explain what the chart pattern means; annotate or create accurate supplementary schematic examples when useful, clearly labeled as reconstructed, not originals.
4. **Rigorous formalization:** identify what is known versus missing (e.g. pivot lookback, wick-to-body ratio, what constitutes a touch, confirmation candle close, timeframes, bar states, simultaneous zones). Propose candidate quantitative definitions but never attribute them to Coach unless explicit.
5. **Ponder-style critique:** explore alternatives, counterexamples, high-risk assumptions, edge cases, and links to previous lessons. Challenge both source claims and our own ideas.
6. **Independent supplementation:** where warranted, research official Pine/TradingView docs, academic/market microstructure principles, statistics, and robust engineering methods; cite them separately from PDF.
7. **Examples and applications:** walk through every source example, trade scenario, diagram and exercise; explicitly note any ambiguity or inability to verify a historical result.
8. **Recap and checkpoint:** conclude with useful retention notes, exact last completed source item, what comes next, unresolved questions and implementation implications.
9. **GitHub sync:** record completed/partially completed items in LESSON_COVERAGE.md, methodology or experimental notes, and STATE.md; commit/push verified increment. No progress marked complete without evidence.

## Coverage, pacing and teaching
- Follow the 35-page PDF's sequence. Cover one *conceptually coherent* portion at a time; never rush or skip repeated material without explaining its contextual role.
- Include source definitions, assumptions, illustrations and worked case analyses. No arbitrary page count per chat.
- Explain prerequisites just when needed; distinguish the original lesson from added explanation or correction.
- Use charts/diagrams where genuinely helpful; ensure no geometry or price action is misrepresented.
- Use clear natural language with original trading jargon, LaTeX math for exact equations when useful, and enough depth for comprehension.
- Do not force quizzes or active recall assessments. The user may request them.
- When a lesson is discussed, no automatic jump to the next lesson; maintain a verifiable checkpoint.
- User may ask questions that interrupt the sequence: answer fully, then preserve the source position.

## Domain-specific safeguards
- A probabilistic trading interpretation is not a theorem. Do not turn phrases like 'high probability', 'safe', or 'guaranteed' into empirical findings without data.
- A signal that uses future bars must be defined as retrospectively confirmed and must not be presented as available on earlier bars.
- Distinguish actual OHLC/market data from artistically redrawn examples.
- The source may use discretionary terms such as 'strong candle', 'rejection', 'liquidity', 'OB', or 'FVG'. Record these as operationalization questions, not resolved algorithms.
- Verify calculations, dimensional units, RR arithmetic, and practical leverage/margin assumptions independently while retaining what the source actually states.

## For independent enhancements
Use this order: **Coach source -> PCSS comprehension -> source-specific rule extraction -> gap/assumption audit -> independent research/alternative definitions -> experimental rule design -> validation plan -> implementation after user approval**. Keep original and extended rule modes separately identifiable.

## Definition of lesson complete
A lesson becomes complete only when all original source items (including images) have been studied, the user-facing explanation has been given, relevant gaps and interpretations have been recorded, the resulting repo checkpoint has been pushed and independently read back, and the state ledger has been updated.
