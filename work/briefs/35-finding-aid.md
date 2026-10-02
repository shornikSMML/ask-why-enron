# Brief: Finding-aid search of *Enron Bankruptcy News* (private repository)

**Background.** The owner has given the team a private, copyrighted archive: *Enron Bankruptcy News* (Bankruptcy Creditors' Service, Inc.), 233 issues, Dec 2001 to 2012. It is at `/home/user/enron-private/enron-bankruptcy-news-by-issue/`. Read its `README.md` first; its "Rules for agents" bind you. The coordinator verified all 233 issue fingerprints, and the joined files match the original archive's SHA-256.

**The archive is a finding aid, not a source.** It tells us which court orders, filings, opinions, settlements, and official releases exist, with their dates, courts, docket numbers, and where they might be obtained. The site may cite only the underlying documents, after the owner adds them to the library.

**Hard rules:**
1. **Copy no newsletter text anywhere in the public repository** (`/home/user/enron-dryrun`). Write your output **only** to the scratchpad path named in your prompt. Describe everything in your own words. Don't quote more than a few words, and only for identifiers such as case captions or document titles.
2. **No web.** Don't try to fetch any link the newsletter gives. Just record it.
3. **Facts are "as the newsletter reported".** Never present them as established.
4. **Don't edit** anything in either repository.

**Start from what exists:**
- `build-log/gaps.md` (the open gaps; use their numbers);
- the owner's own pointer notes in `research-notes/enron-bankruptcy-news-notes.md` (don't redo them, but extend or correct them if you find more);
- `work/facts/*-gaps.md`.

**Method:**
1. Search `index-articles.csv` headlines (grep, case-insensitive, with name and topic variants).
2. Grep the full text in `issues/` for names, case captions, docket numbers ("Cr. No.", "H-02", "H-04", "Case No.", "Adv. Pro."), and terms.
3. Open only the articles you need.

**Output.** A markdown report. For each gap you're assigned, give:
- **status:** "newsletter points to a document" / "newsletter reports the outcome but names no document" / "nothing found";
- issue number(s), date(s), and article ID(s);
- **in your own words**, what the newsletter reports;
- **the underlying document(s)** to obtain: type, court, case caption, docket or case number, filing date, and the likely official source (PACER; justice.gov; sec.gov litigation release number; uscourts opinion; govinfo), plus any link the newsletter gives, recorded but not fetched;
- confidence (high / medium / low) and any conflict with what our library or site currently says (check `js/cast-data.js`, `js/timeline-data.js`, and the chapter drafts in `work/drafts/` where relevant);
- importance for the site (critical / useful / minor).

End with a short list of **other leads** worth the owner's attention that aren't in `gaps.md`. Final report to the coordinator: a summary, plus any conflicts with the site.
