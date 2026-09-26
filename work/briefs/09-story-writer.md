# Brief: Story Writer

**Role:** Write the seven chapters of "The Story." Follow `00-common-rules.md` (markup conventions included) and the AUDIENCE AND TONE section of `CLAUDE.md`.

**Audience and voice:** undergraduates from any major, no accounting background. Tell it as a story (scenes, people, stakes), but stay **neutral and factual**. No sensationalism, no adjectives that pass judgment ("greedy," "shocking"), and no moralizing. Each chapter should take about 6–10 minutes to read: roughly 900–1,400 words. Short paragraphs.

**Facts:** use **only** fact cards in `work/facts/*.json` whose `checked` is "OK" or "FIXED", or unchecked cards from a sample the checker passed. **Never use cards marked REJECTED.** Give each card's id in `data-card` on the citation. **Every sentence with a specific fact about a person, date, or amount carries a citation.** Use the card's verb. If you need a fact that has no card, don't look it up: add it to `work/drafts/story-requests.md` (the claim, and the kind of source that might have it) and write around it.

**Concept explanations** (mark-to-market accounting, special purpose entities, hedging, restatement, auditor independence) may use general knowledge. Keep them simple, and use one worked illustration clearly labeled as an illustration.

**Glossary terms:** wrap the first use of each accounting or legal term in `<span class="term" data-term="ID">`. List every term id you use, with a one-line plain definition, in `work/drafts/story-terms.md` (the Reference Writer builds the glossary from it).

**Lenses (for Phase 2):** tag paragraphs with `data-lens` (money, auditors, board, knew) where they apply.

**Images:** put one or more `<figure data-image="ID"></figure>` placeholders in each chapter. Pick from `images/credits.json` (use its ids) or name a needed diagram in `work/drafts/story-requests.md`.

**Chapters:**
1. Origins
2. The Business Model and Mark-to-Market Accounting
3. The Special Purpose Entities
4. Warning Signs and the Whistleblower
5. The Collapse
6. Arthur Andersen
7. Aftermath and Reform

Chapter 7 covers the trials and how each case ended, employees' pensions, and SOX and the PCAOB **in brief**. (Phase 2 will add "Why This Matters to You.")

**End each chapter** with `<aside class="ask-why">`: one genuinely open question, the kind an instructor could use to start a class discussion, tied to the chapter. It's a question, not a verdict.

**Reader tip rulings** are in `work/facts/factcheck-round1.md`. Follow them exactly.

**Output:** `work/drafts/ch1.html` ... `ch7.html`. Each is an HTML fragment: `<h1>`, then an optional `<p class="dek">` (a one-sentence summary), then the body. Also `work/drafts/story-requests.md` and `work/drafts/story-terms.md`.
