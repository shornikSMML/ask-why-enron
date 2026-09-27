# Brief: Reform Writer, second revision pass

Update `work/drafts/why-it-matters.html` (edit `work/drafts/reform-src/`) using the new checked cards T-001… in `work/facts/reader-sox-revision.json`. **Read every `checker_note` and the rulings in `work/facts/factcheck-revision2-sox.md`.** The gap map is in `work/facts/revision2-gap-map.md`.

1. **`#today`:** replace the "library covers only 2002–2003" paragraph with a short, sourced account of what came next:
   - the SEC's 2003 §404 rule and its later compliance dates (use the **corrected** dates in T-008);
   - the 2007 SEC guidance (top-down, risk-based);
   - AS 2201 as today's version of AS No. 5, with its objective;
   - GAO on smaller companies and on audit-firm concentration;
   - *Free Enterprise Fund* (2010): the Syllabus and opinion labelled as the checker required;
   - the Dodd-Frank §404(c) exemption text;
   - the SEC whistleblower awards (10–30% in total, voluntary information).

   Keep it plain and neutral, about 500–800 words. **Keep one honest sentence** saying what the library still doesn't cover (e.g. the first PCAOB inspections, later amendments beyond these documents).
2. **"What it means for you" paragraphs:** add one or two specific, sourced points where the cards support them (e.g. "material weakness" meaning management may not call its controls effective; partner rotation of 5 years on / 5 years off). Keep advice general where no card supports specifics.
3. **Rulings:**
   - §201 stays "eight named kinds … plus any the PCAOB bans by rule". You may add that the SEC's 2003 release counts these as nine categories.
   - SSAE No. 10: only in the SEC's words, "on a transition basis". Don't call it "interim". Say nothing about the orders' contents.
   - The 2006 exemption figures are proposals.
4. Add new glossary term ids for new concepts (e.g. `material-weakness`, `emerging-growth-company`, `accelerated-filer`) to `work/drafts/reform-terms.md`, with plain definitions.
5. Rebuild, run `integrate.py --no-log` and the tests, and write the old and new text to `work/facts/fixes-revision2-reform.md`. Report briefly.
