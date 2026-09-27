# Brief: Reader B, revision pass (11 newly approved documents)

**Background:** The owner approved the Source Scout's 10 candidates and added one hearing. All 11 are now in `sources/manifest.csv`. Note that 10 of them are listed with folder `candidates`: **they are approved library documents now**, so cite them normally by manifest id. Fingerprints: all 85 files match `download_log.csv` (checked by the coordinator). Text copies are in `work/text/<id>.txt`.

**Follow `00-common-rules.md`.** Card ids `G-001`... in `work/facts/reader-revision.json`. No web.

**New documents (manifest ids):** `doj-fastow-plea-press-2004`, `doj-fastow-sentenced-press-2006`, `doj-glisan-plea-press-2003`, `doj-causey-sentenced-press-2006`, `doj-dag-kopper-plea-transcript-2002`, `doj-andersen-indictment-2002`, `doj-skilling-sentencing-agreement-2013`, `ca5-skilling-2011-remand`, `andersen-scotus-full-usreports`, `sec-duncan-litrel-20441`, `hrg-hfs-enron-investors-pt1`.

**What we need** (these fill gaps listed in `build-log/gaps.md`):
1. **Fastow:** the date and charge(s) of his guilty plea; the date and length of his sentence; anything else the releases state as fact (for example forfeiture). Use "DOJ announced" for statements made in the releases.
2. **Glisan:** the date and charge of his plea; his sentence, if stated.
3. **Kopper:** the date and charges of his plea, from the Deputy Attorney General's transcript. The date is unclear: the page title says 08-22-02 and the URL 082102. Say what the document itself shows.
4. **Causey:** his sentencing date and sentence.
5. **Skilling after 2010:** what the Fifth Circuit held on remand in 2011 (the harmless-error question; which convictions stood; resentencing). Then what the 2013 sentencing agreement provides (its terms). **Careful with verbs:** an agreement filed in court is not the same as the court's judgment, so say "agreed" or "the agreement provides".
6. **Andersen:**
   - From the indictment: the date, the charge, and 1–2 key allegation paragraphs. Remember that an indictment **alleges**.
   - From the full Supreme Court opinion: the holding, the vote, and 1–3 short verbatim sentences explaining why the jury instructions were flawed. Cite the opinion itself, not the Syllabus.
7. **Duncan:** what SEC Litigation Release 20441 says about how the SEC case was resolved (settlement terms; "without admitting or denying", if stated). Also anything it says about his criminal case.
8. **The Dec 12, 2001 House hearing:**
   - Find the testimony by Andersen's CEO that the Powers Report quotes: "Andersen's CEO" (see card A-048 and its checker note). Confirm the speaker's name and title and the exact wording as printed in the hearing record. Note any differences from the Powers quotation.
   - Record the hearing's official title, the subcommittees, and the serial number (Serial No. 107-51, Part 1).
   - Only 2–4 more cards from this hearing, and only if they're clearly useful.

**Also produce** `work/facts/revision-gap-map.md`: a table of gap number (from `gaps.md`) | resolved / partly resolved / still open | card ids | the exact site locations that currently say the fact is "not shown" or "not in the library". Search `work/drafts/ch*.html` and `js/cast-data.js`, `js/timeline-data.js`, `js/glossary-data.js`, and `work/drafts/footnote.json` for such phrases (e.g. "library does not", "not in library", "not shown", "Syllabus"). The writers will use this map.

**Output:** `work/facts/reader-revision.json`, `work/facts/revision-gap-map.md`, `work/facts/reader-revision-readlog.md`; final report.
