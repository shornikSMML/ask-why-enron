# Brief: Fact-Checker, Round 2 (every page)

**Role:** The independent review of everything a reader will see, before Phase 1 counts as done. Follow `00-common-rules.md` and `sources/README.md` "Rules for the agents". Two Fact-Checker instances run at the same time, each with its own part (below). **Don't edit the drafts or data files yourself.** Report findings; the writer fixes them; then you re-check (Round 3).

**Part A (instance A):** `work/drafts/ch1.html` ... `ch7.html`, including figure captions.
**Part B (instance B):**
- `js/cast-data.js`, `js/timeline-data.js`;
- `js/glossary-data.js` (only entries containing Enron-specific facts, and any definition that is wrong as general knowledge);
- the three Enron diagrams `images/diagram-raptor.svg`, `diagram-chewco-ljm.svg`, `chart-restatement.svg` (and their `-narrow` versions: same facts);
- `work/drafts/footnote.json`: its intro and closing, plus a 25% spot re-check of the annotations fixed in Round 1.

**For every citation or factual sentence:**
1. **Does the cited card support the sentence exactly?** No added detail, no stronger verb, no merged facts that the cards don't join. Where the text relies on a card's notes rather than its quote, check the source itself at the locator.
2. **Does the card's source say it at that locator?** For every claim about a named person, and every date or dollar amount, open the source. For other claims, a 30% sample.
3. **Verbs and outcomes:** alleged / found / testified / concluded / held / pleaded guilty / convicted. No one is called guilty whose conviction was reversed or vacated, or who was only charged. "No charges shown in the library" never becomes "never charged". Taking the Fifth is not presented as guilt.
4. **Quotes:** verbatim, short, correctly attributed.
5. **Disagreements:** handled as the table in `work/facts/factcheck-round1.md` rules.
6. **Reader tips:** Buffett absent; the Fortune ranking only in the ruled wording.
7. **Tone:** neutral and factual; no sensational or judging words (flag them).
8. **Concept explanations** drawn from general knowledge must be correct and must not smuggle in Enron-specific claims.
9. **Citations:** `data-src` is a manifest id; `data-page` points to the right PDF page; no candidate document (`sources/candidates/`) is cited anywhere.

**Output:** `work/facts/factcheck-round2-partA.md` or `-partB.md`. Each is a table: # | file | location (paragraph or entry id) | problem | what the source says (with locator) | required fix | severity (**must-fix** = factually wrong or unsupported; **should-fix** = wording, verb, tone; **note**). End with a one-line verdict per file: PASS / PASS AFTER FIXES / FAIL.
