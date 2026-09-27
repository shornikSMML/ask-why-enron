# Brief: Site Builder, Phase 2 final assembly

Don't change content wording.
1. **How This Was Built.**
   - Show the build by phase (Phase 1 → Revision pass → Phase 2) from the log's new `phases` block.
   - Add an "Owner's decisions" panel from `owner_decisions`. It should make clear which choices the human made: approving sources, seven pathways, current documents, one lens at a time.
   - Update "At a glance" with totals and a per-phase breakdown.
   - Show the Phase 2 candidates (from `sources/candidates/phase2/candidates.csv`) as "awaiting the owner's approval, not used on this site". Use neutral descriptions in the same way `gaps_to_js.py` handled the Phase 1 candidates, and **don't link to the candidate files**.
   - The gaps list now has a "Phase 2 (post-2003)" section. Make sure it renders.
2. **Home page.** Add Pathways, Lenses (a one-line explanation with the keyboard shortcut), The Banks, and Why It Matters to the welcome and section links. Use neutral wording with no new facts. Take the one-sentence descriptions for the new pages from their `<p class="dek">`.
3. **Run the full `python3 work/tools/integrate.py`, including the log, at the very end.** The Scribe is updating `build_log.py` in parallel, so run it after the Scribe finishes, or re-run at the end.
4. **Final tests:** everything at 1440×900, 1920×1080, 390×844 and 360 wide, light and dark; all lenses; all pathway stops; keyboard; print. Take fresh screenshots of every page, including one of each pathway's first stop and one of each lens on one chapter.
5. **Placeholder check:** confirm no placeholder or sample text remains anywhere.

Report test results and anything in the content that looks wrong. Report it; don't fix it.
