# Brief: Image Researcher & Diagrammer, second pass (Enron-specific diagrams)

**Role:** Draw three original diagrams that show specific Enron facts. Every number, name, or date in a diagram must come from a **checked fact card** (`checked` is "OK" or "FIXED") in `work/facts/reader-a.json` or `work/drafts/footnote.json`. Read `work/facts/factcheck-round1.md` for how to present source disagreements. **No web.** Follow `00-common-rules.md` and your first-pass conventions: wide and narrow versions; readable in light and dark; `credits.json` and `credits.js` entries marked `is_original_diagram: true`.

New field for each of these diagrams in `credits.json`: `"fact_cards": ["A-0xx", ...]`, listing every card that supports something shown. Add a short source line inside the SVG itself (e.g. "Sources: Powers Report pp. 97–101; Enron Form 10-Q, Q3 2001"). The Fact-Checker will check these diagrams.

1. `diagram-raptor` (Ch. 3): how the Raptor "hedges" worked. Enron put in its own stock (or rights to it); the Raptor vehicles promised to cover losses on Enron's investments; so the protection depended on Enron's own share price, and when the price fell the vehicles couldn't pay. Include LJM2's role and only the amounts the cards support.
2. `diagram-chewco-ljm` (Ch. 3): the cast of entities (JEDI and Chewco; LJM1; LJM2; the Raptors), who ran or controlled each according to the cards (e.g. Kopper at Chewco; Fastow at LJM), and their relationship to Enron. Keep it simple: at most about 8 boxes.
3. `chart-restatement` (Ch. 5): a simple bar chart of the reduction to reported net income by year, 1997–2000, using the **Form 10-Q** figures (as the Fact-Checker ruled). Add a note that the Nov. 8, 2001 8-K and the Powers Report give different figures. Accessible: include the numbers as labels, not only bar heights.

**Outputs:** the SVGs (+ `-narrow`) in `images/`, updated `images/credits.json` and `credits.js`, and a final report.
