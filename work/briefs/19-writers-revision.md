# Brief: Writers, revision pass

**Inputs:**
- New checked cards `G-001`... in `work/facts/reader-revision.json`. Read every `checker_note`.
- `work/facts/revision-gap-map.md`: the exact places the site says a fact is "not shown" or "not in the library".
- The Fact-Checker's revision section at the end of `work/facts/factcheck-round3-partB.md`.

**The 11 documents are approved library documents** (the owner approved them in writing). Ten are filed under the folder `candidates`; cite them normally by manifest id.

**Rules:** as before (`00-common-rules.md`). Use only cards checked OK or FIXED. Use the card's verb: DOJ "announced"; an indictment "alleged"; an agreement "agreed"; the court "held".

Replace each "not shown / not in the library" statement that the new cards answer. Keep every statement that is **still** open (Kopper's sentence; the sentence actually imposed on Skilling after the 2013 agreement; what happened to Andersen after the remand; Duncan's plea date and what happened to it). Say plainly what we still don't know.

**Specific points:**
- **Fastow forfeiture:** $29M (2004 release) vs. $20M (2006 release) is a **real disagreement**. Give both, attributed.
- **Kopper $12M vs. $4M:** **not** a disagreement ($4M forfeiture + $8M to the SEC = $12M). Don't present it as a conflict.
- **Berardino, Dec 12, 2001:** the quote in the Powers Report is from his **written statement** in the hearing record. That hearing shows no oath. Name him now where the site said "Andersen's CEO" (ch. 5 or wherever the map points), e.g. "Andersen's chief executive, Joseph Berardino, in a written statement to a House hearing in December 2001, as quoted in the Powers Report". Keep "sworn witness" only for the Feb. 5, 2002 hearing.
- **Andersen's full Supreme Court opinion:** where the site cites only the Syllabus, cite the full opinion (`andersen-scotus-full-usreports`) instead or as well. Keep the text accurate: unanimous; reversed because the jury instructions were flawed; not a finding of innocence.

**Story Writer:** chapters (edit `work/drafts/story-src/`, regenerate with `expand.py`; add G-card support to `expand.py` if needed). **Reference Writer:** `js/cast-data.js` (update `outcome_status` where the new cards justify it, e.g. Glisan "pleaded guilty"), `js/timeline-data.js` (add dated events such as pleas, sentences, the 2011 Fifth Circuit ruling, and the 2002 indictment; the 2010+ items are epilogue), and `js/glossary-data.js` if a new term is needed.

**Both:** run `python3 work/tools/integrate.py --no-log` and `python3 work/tools/test_site.py`. If the test complains about links into `sources/candidates/`, report it to the coordinator; don't work around it. Append old and new text to `work/facts/fixes-revision.md` under your own heading. Report briefly.
