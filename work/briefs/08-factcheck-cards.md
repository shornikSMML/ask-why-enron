# Brief: Fact-Checker, Round 1 (fact cards)

**Role:** You are the team's independent fact-checker. Nothing reaches the site until you've checked it. In this round you check the **fact cards** before any writer uses them. Follow `00-common-rules.md` and the "Rules for the agents" in `sources/README.md`. You enforce them.

**Inputs:** `work/facts/reader-a.json`, `reader-b.json`, `reader-c.json`, `work/facts/people-outcomes.md`, and `work/drafts/footnote.json` (the annotations are checked in the same way as cards).

**What to check, against the source itself (open the file at the cited page or lines; never trust the card's quote):**
1. **Every card that names a real person, and every footnote annotation:** check all of them.
2. **Every card with a date or a dollar amount:** check all of them.
3. **Other cards:** a random sample of at least 25%.
For each card:
- Does the file's fingerprint match `download_log.csv`? (Check each file once.)
- Is the quote verbatim at that locator? For OCR cards, check against the page image (Read the PDF with `pages`).
- Does the claim say no more than the quote and its context support?
- Is the verb right for the kind of source (alleged / found / testified / held / pleaded guilty / convicted)?
- For outcomes: is anyone called guilty whose conviction was reversed or vacated, or who was never charged? Is anything asserted that no library document states?
- Do sources disagree? Note it.

**The reader tips (give a ruling on each, with reasons):**
1. "Warren Buffett read Enron's footnote, didn't understand it, and threw the 10-K away." Search `work/text/` and the `.txt` sources for "Buffett" yourself. If there's no library support, the ruling is "exclude; log as gap." Say what kind of document would be needed.
2. "At its peak, Enron was America's seventh-largest company." Rule on whether and how it may be stated (exact wording, attribution, hedging), based on the cards and your own check of `sec-kopper-complaint` and any other library support.

**Outputs:**
- `work/facts/factcheck-round1.md`: a summary; a table of every card or annotation checked (id | verdict: OK / FIXED / REJECTED / NEEDS-SOURCE | note); the rulings on the reader tips.
- Apply fixes directly in the card files. Add `"checked": "OK" | "FIXED" | "REJECTED"` and `"checker_note"` fields to each checked card. **Don't delete rejected cards**: mark them `REJECTED` so writers skip them.
- **Append every correction** (anything you changed or rejected) as a row in `build-log/corrections.md`, using the table columns already there.
- `work/facts/factcheck-gaps.md`: any gaps you find.
