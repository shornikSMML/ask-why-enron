# Brief: Site Builder (Phase 2 features)

Follow `00-common-rules.md` and your `work/drafts/site-notes.md`. Don't change content wording. Build the machinery now with **sample data**; real content arrives from other agents in `work/drafts/lenses.json` and `work/drafts/pathways.json` (formats in briefs 23 and 24).

1. **Lens bar** on every chapter: four buttons (Follow the Money, The Auditors, The Board, Who Knew What, When) plus Off. **One lens at a time.**
   - When a lens is on: highlight paragraphs whose `data-lens` includes it; show that lens's notes in the margin on wide screens, or as tap-to-open notes on phones (match paragraphs by `para_index`, confirmed by `para_start`); show the lens summary and Ask Why at the chapter end; for `knew`, show the dated strip at the top.
   - The lens state goes in the URL (`?lens=money`) and is remembered per browser (try/catch).
   - Keyboard: `1`–`4` choose a lens, `0` turns it off.
   - Readable when projected. Print: only the active lens's notes.
   - Implement the `applyLens(name)` stub.
2. **Pathways:** a `pathways.html` index (cards with title, for whom, minutes, intro). When a reader follows a pathway (`?path=id&stop=n` on any page), show a slim bar: "Pathway: <title> · stop n of N · bridge text · ← →". It must work across chapter, Cast, Timeline, Footnote, Glossary, `banks.html` and `why-it-matters.html`, including anchors inside the Cast or Timeline (scroll to and highlight the item). Also a printable handout view per pathway.
3. **New page shells** with the site's layout and placeholder text only: `why-it-matters.html` (sections `#s302`, `#s404`, `#pcaob`, `#independence`, `#whistleblowers`, `#today`) and `banks.html` (`#prepays`, `#deals`, `#institutions`, `#outcomes`). Content comes later through `integrate.py` splice markers, like the chapters. Add both pages and Pathways to the navigation, keeping the nav usable on phones.
4. **`integrate.py`:** wrap `work/drafts/lenses.json` → `js/lenses-data.js` and `pathways.json` → `js/pathways-data.js`; splice `work/drafts/why-it-matters.html` and `work/drafts/banks.html` when they exist.
5. **Tests:** extend `test_site.py`:
   - each lens on each chapter, with no overflow at 360px;
   - every lens note matches a paragraph;
   - every pathway stop resolves to an existing page and anchor;
   - the keyboard shortcuts work;
   - screenshots.

Output: files, and a final report.
