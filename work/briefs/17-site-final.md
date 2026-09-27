# Brief: Site Builder, final assembly (Wave 4)

Follow `00-common-rules.md`. **Don't change content wording** in chapters, the Cast, the Timeline, the Glossary, or the footnote (fact-checking is finishing in parallel; your integrate script will pick up their final text).

1. **How This Was Built** (`js/how-built.js`, `how-built.html`). `build-log/log.json` now has several runs per agent, resumed runs, coordinator messages, and a computed `summary` block (see `work/tools/build_log.py`). For a non-technical workshop audience:
   - Open with "Before the agents" (as the Scribe wrote it; it covers the SHA-256 explanation and the three lessons). Check that it reads clearly, and style it prominently.
   - Then an "At a glance" band built from `summary.text` and its numbers.
   - The team diagram (coordinator and agents). Show how many runs each agent had.
   - The build timeline.
   - Agent cards: each run shows its brief (or the coordinator's follow-up message summary for resumed runs), what the agent read, what it produced, and the coordinator's decision and reason. Use collapsible sections so it isn't overwhelming.
   - "How facts were checked": a short explanation of fact cards → writers → fact-checker → fixes → re-check, with the corrections list (from the log).
   - "What the sources couldn't tell us": render `build-log/gaps.md` (convert the markdown tables to a JS data file with a small script in `work/tools/`, run by `integrate.py`) and the candidate list from `sources/candidates/candidates.csv` (title, source, which gap it fills, "awaiting the owner's approval, not used on this site"). **Don't link to the candidate files.**
   - The reader tips: how the two tips were handled (from the gaps file's Reader tips section).
   - Websites used (from the log).
2. Re-run `python3 work/tools/integrate.py` (full, including the log) at the end.
3. Final tests: `work/tools/test_site.py` at 1440×900, 1920×1080, 390×844, and 360 wide, light and dark. Add a check that no page links into `sources/candidates/`. Save fresh screenshots of every page.
4. Polish: consistent headings, no leftover placeholder text anywhere (search for "coming", "SAMPLE", "TODO", "[Draft"), footer on every page, a working 404-free set of links. Check `index.html` opens straight from disk.

Output: the updated files and a final report (test results; anything that looks wrong in the content, reported rather than fixed).
