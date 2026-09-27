# Brief: Reform Writer, "Why This Matters to You" (Phase 2)

Follow `00-common-rules.md` and the AUDIENCE AND TONE section of `CLAUDE.md`. Use only checked cards (OK or FIXED): `work/facts/reader-sox.json` (S-cards; **read every `checker_note`** and the rulings in `work/facts/factcheck-phase2-sox.md`), plus existing cards (the C-070–081 SOX cards; the A, B, C, and G cards for the Enron links). Write in the same fragment format as the chapters, into `work/drafts/why-it-matters.html`, about 1,800–2,400 words.

**Sections (required ids):**
- `#s302`: CEO/CFO certification (§§302, 906)
- `#s404`: internal control reports (§404)
- `#pcaob`: the PCAOB (§§101–109)
- `#independence`: auditor independence (§§201–203, 206)
- `#whistleblowers`: document destruction, whistleblowers, criminal penalties (§§802, 806, 807, 1102, 1107)
- `#today`: "What this means for you"

**For each provision:**
1. **What the law requires**, cited to the statute ("requires").
2. **The Enron problem Congress had in mind.** Link to the relevant chapter with a normal `<a href="chapters/chN.html#…">` and cite the committee report, testimony or Enron cards. Floor statements and prepared testimony are characterizations: use "said".
3. **"What it means for you"**, one short paragraph addressed to a student about to enter business or accounting (an accountant, auditor, analyst, manager or employee). General-knowledge explanations are allowed, but make **no specific claims about how the rules work today**. The library covers the law and its first year only.

**`#today` section:** explain plainly that the library covers 2002–2003, and that later developments (how §404 has been applied, PCAOB standards and inspections, later amendments) aren't covered yet. The owner may add official documents on these later. **Don't state post-2003 facts.** End with the page's **Ask Why** question.

**Rulings to follow exactly:**
- **§201:** "eight named services, plus any the PCAOB bans by rule".
- **§402:** follow the statute's exceptions, not the CRS phrase "of any kind".
- **§807:** give both 10 (Daschle, floor) and 25 (the law), without explaining the change. Don't confuse it with the Bush "5 to 20 years" figure, which is a different penalty.
- **Lay's pay/loans:** only with attribution, and never combine the periods (SEC 2001 stock sales; JCT 2001 withdrawals; the examiner's 1999–2001 figure). The "$70 million" figure is only the Senate report's, citing the WSJ. Prefer to leave it out.
- **The April 2003 SEC orders:** the library holds landing pages only. Use the SEC press release for "the Board was ready", and say nothing about the orders' content.

Tag paragraphs `data-lens` where apt (`auditors`, `board`, `money`). Wrap first uses of terms in `span.term` and list new term ids with plain definitions in `work/drafts/reform-terms.md`. Put at least one `<figure data-image="diagram-sox-map">` placeholder (a diagram will be drawn). Build the citations the way the Story Writer does. You can use or copy `work/drafts/story-src/expand.py`, extended for S-cards, and keep your source file in `work/drafts/reform-src/`. Run `integrate.py --no-log` and the tests. Report briefly.
