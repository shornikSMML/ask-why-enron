# Brief: Reference Writer

**Role:** Write the Cast of Characters, the Timeline (1985–2006), and the Glossary. Follow `00-common-rules.md` and `CLAUDE.md`. Same fact rules as the Story Writer: use only cards marked "OK" or "FIXED" in `work/facts/*.json` and `work/facts/people-outcomes.md`; never use REJECTED cards; and put what's missing in `work/drafts/reference-requests.md` instead of looking it up.

**Cast of Characters:** `js/cast-data.js` → `window.CAST = [...]`, in the format in `work/drafts/site-notes.md` (from the Site Builder). For each person:
- their role, with dates;
- a 2–4 sentence neutral summary;
- `outcome_status`, one of: "convicted", "convicted — later narrowed on appeal", "conviction vacated (died before appeal)", "conviction reversed", "pleaded guilty", "SEC settlement", "charged — outcome not in library", "not charged (per source)", "no charges shown in library", "not accused of wrongdoing";
- `outcome_text`: exactly what happened, with the right verbs;
- `cites`: an array of `{source_id, page, loc, card}`.

Precision matters most here. If the library doesn't document how a case ended, say that plainly, and log a gap in `work/drafts/reference-gaps.md`.

**Timeline:** `js/timeline-data.js` → `window.TIMELINE = [...]`. Cover 1985–2006, 35–60 events, each with a date (as precise as the source allows), a title, 1–2 sentences, `cites`, and `tags` from: company, accounting, spe, people, markets, auditors, legal, government, reform. The 2010 *Skilling v. United States* decision appears as the last item, with `epilogue: true`.

**Glossary:** `js/glossary-data.js` → `window.GLOSSARY = { "term-id": {"term", "short" (≤ 25 words, plain), "long" (2–4 plain sentences, one everyday example), "see_also": [...]} }`. Include every term id in `work/drafts/story-terms.md` and `work/drafts/footnote-glossary-terms.md`, plus: form 10-K, footnote, related-party transaction, special purpose entity, mark-to-market accounting, restatement, auditor, audit committee, Sarbanes-Oxley Act, PCAOB, SEC, indictment, plea agreement, vacated, honest-services fraud, obstruction of justice, Big Five / Big Four, 401(k). Definitions are general knowledge; give no Enron-specific facts without a card citation.

**Outputs:** the three data files, plus `work/drafts/reference-requests.md` and `work/drafts/reference-gaps.md`.

## Coordinator addendum (after Fact-Checker Round 1)
- Read `work/facts/factcheck-round1.md` first. Its table of **26 source disagreements** says how each must be presented (for example, restatement figures: use the 10-Q; Q3 2001 loss: $618M announced vs. $644M filed; the bankruptcy date Dec 2 vs. Dec 3). Follow it. Where sources disagree, say so in plain words ("Enron's filings and the board's investigation give different figures: ...").
- Read `work/drafts/site-notes.md` (from the Site Builder) for the exact file names and data formats.
- Reader tips, as ruled: **Buffett is excluded. Don't mention it.** The ranking may appear only as: "In 2001, *Fortune* magazine ranked Enron seventh on its list of the 500 largest U.S. companies, measured by revenue," citing `rpt-jct-vol1` p. 58 (PDF 86) and `batson-final` n. 27 (PDF 18). Never say "at its peak" or "in the world."
- Andersen's CEO quote from the Dec 12, 2001 hearing: attribute it to "Andersen's CEO, as quoted in the Powers Report." Don't name him for that quote.
- Every card now carries `checked` and `checker_note`. Read the `checker_note` before using a card.
- Images: the Image Researcher is still working. Use ids from `images/credits.json` if it exists. Otherwise use descriptive placeholder ids (e.g. `diagram-raptor`, `photo-enron-hq`) and list them in your requests file.
