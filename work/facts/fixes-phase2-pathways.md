# Fixes to the pathways after the Phase 2 fact-check

By the Pathways Designer, 2026-09-27. These respond to `work/facts/factcheck-phase2-pathways-footnotes.md` (items P-1 to P-5).

Each fix was made in `work/tools/build_pathways.py`, which was then re-run to regenerate `work/drafts/pathways.json`. Every handout is built from the same strings, so each fix also appears in the matching handout.

After the fixes:
- `python3 work/tools/integrate.py --no-log` rewrote `js/pathways-data.js` and reported 0 problems.
- `python3 work/tools/test_site.py` reported 0 problems.

| # | Where | Old wording | New wording |
|---|---|---|---|
| P-1 (should-fix) | footnotes pathway, stop 5 (Note 9): bridge and handout | "Note 9 listed JEDI and Whitewing, each 50% owned and not consolidated." | "Note 9 listed JEDI and Whitewing, each with a 50% voting interest and not consolidated." |
| P-2 (minor) | spes pathway: closing question, also in the handout | "…if an independent owner had at least 3% of its value at risk." | "…if an independent owner had at least 3% of its assets at risk." |
| P-3 (minor) | mark-to-market pathway, stop 1: bridge and handout | "Two related ideas, fair value and unrealized gain, come up at every later stop." | "Two related ideas, fair value and unrealized gain, come up again and again." |
| P-4 (minor) | andersen pathway, stop 9 (Timeline, auditor events): bridge and handout | "…to see the whole relationship, from the 1985 merger to the 2005 decision." | "…to see the whole relationship, from InterNorth's 1985 purchase of Houston Natural Gas to the 2005 decision." |
| P-5 (minor) | banks pathway: intro | "It explains \"prepays,\" deals that looked like trades but worked like loans, …" | "It explains \"prepays,\" deals that Senate investigators found looked like trades but worked like loans, …" |

**P-6** was information only. It needed no pathway change.

**Board wording:** the fact-check file has no separate pathway finding about wording on the board. P-2, on the 3% rule, is the only remaining pathway item, and it is applied above.
