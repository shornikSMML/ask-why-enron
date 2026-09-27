# Brief: Site Builder (first pass: design and skeleton)

**Role:** Build the static website's structure, design, and shared code. Follow `00-common-rules.md` (especially "Site markup conventions") and the TECHNICAL section of `CLAUDE.md`. Content is not ready yet, so use clearly marked placeholder text ("[Draft text coming]"). **Do not write any factual content about Enron.**

**Hard constraints**
- Plain HTML, CSS, and JS only. No build step, no frameworks from CDNs, no outside services, fonts, or analytics. It must work by opening `index.html` directly from disk (file://) **and** from GitHub Pages. So: **no fetch() of local JSON.** Data comes in as `<script src="...js">` files that set `window.X = ...`.
- **Equal priority for computer and phone.** On a computer (and a classroom projector), a wide reading layout with **margin notes** beside the text, like an annotated edition. On a phone, the same notes open when tapped. Also:
  - a **"Presentation" toggle** that enlarges text for projecting (remembered with localStorage, wrapped in try/catch);
  - **keyboard navigation:** left and right arrows move between chapters; on the Footnote page, j/k or the arrows step through annotations;
  - print styles for chapters (margin notes print as endnotes);
  - light and dark themes (following the system setting, plus a manual toggle);
  - accessible: semantic HTML, focus styles, alt text, good contrast, no horizontal scroll at 360px wide.
- A tasteful, readable, "annotated edition" look: a serif body font from system fonts, generous line height, restrained colors. The title is "Ask Why: The Rise and Fall of Enron."

**Build**
- `index.html` (home), `chapters/ch1.html` ... `chapters/ch7.html` (placeholder bodies, using the chapter titles in the plan below), `cast.html`, `timeline.html`, `glossary.html`, `footnote.html`, `how-built.html`, `sources.html`, `credits.html`.
- `css/site.css`; `js/site.js`, which:
  - numbers `a.cite` elements and builds the margin or tap notes from `data-src`, `data-page`, and `data-loc`, looking up `window.SOURCES` (title, file path) and linking to `../sources/<folder>/<file>` (+`#page=N` for PDFs);
  - handles glossary pop-ups for `.term[data-term]`, using `window.GLOSSARY`;
  - places `figure[data-image]` from `window.IMAGE_CREDITS`, showing the credit line (author, license, source link);
  - builds the prev/next chapter navigation, the Presentation toggle, and the theme toggle;
  - has a hook for Phase 2 lenses: elements with `data-lens` get no special styling yet, but put a stub function `applyLens(name)` in the code.
- `js/sources-data.js`: generate it now **from `sources/manifest.csv` and `sources/download_log.csv`** with a small Python script, `work/tools/make_sources_js.py` (commit the script; the site itself has no build step). Include id, title, date, source_body, folder, filename, official URL, and sha256. `sources.html` lists them all, grouped by folder, with their fingerprints and a short plain-language explanation of what a fingerprint is.
- `js/glossary-data.js`: a placeholder `window.GLOSSARY = {}` (the Reference Writer fills it later).
- `js/footnote.js`: renders `window.FOOTNOTE` (format: see `work/briefs/04-footnote.md`, output section) into `footnote.html`. Make a tiny sample `js/footnote-data.js` with one fake paragraph clearly labeled SAMPLE so you can test it. On wide screens, the annotation panel sits beside the text; on phones, it's a bottom sheet. Each annotation shows "What it said / What it left out / What investigators found," with citation links.
- `how-built.html` + `js/how-built.js`: render `window.BUILD_LOG` (from `build-log/log.js`, which the Scribe produces; its format is in `work/briefs/07-scribe.md`). Sections: (1) "Before the agents" (placeholder heading; the coordinator will supply the text), (2) a team diagram (SVG generated from the agents list: the coordinator in the center, the agents around it), (3) a build timeline, (4) one expandable card per agent showing its role, brief, result, and decision, (5) websites used. Use a small sample `build-log/log.js` if the real one doesn't exist yet. **Don't overwrite it if it exists.**
- `timeline.html` + `js/timeline.js`: render `window.TIMELINE` (array of `{date, title, text, cites:[...], tags:[...], epilogue:bool}`), with tag filters and year jumps. Use a small SAMPLE data file.
- `cast.html` + `js/cast.js`: render `window.CAST` (array of `{id, name, role, summary, outcome_status, outcome_text, cites, image?}`), with outcome labels that are neutral in wording and color. Use SAMPLE data.

Chapter titles: 1 "Origins", 2 "The Business Model and Mark-to-Market Accounting", 3 "The Special Purpose Entities", 4 "Warning Signs and the Whistleblower", 5 "The Collapse", 6 "Arthur Andersen", 7 "Aftermath and Reform".

**Test:** use Playwright with the pre-installed Chromium (`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers`; don't run `playwright install`; install the Python `playwright` package with pip if needed) to load the pages via file:// at 1440×900, 1920×1080 (projector), and 390×844 (phone). Check for console errors and horizontal overflow. Save screenshots to `work/screens/`.

**Outputs:** the files above, plus `work/drafts/site-notes.md`, which explains to the writers exactly how to hand over content (the file names and `window.` variable names you expect).
