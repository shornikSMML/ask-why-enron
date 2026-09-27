# Brief: Scribe, Phase 2 update

Update `work/tools/build_log.py` (keep it deterministic):
1. **Phases.** Group the log into **Phase 1**, **Revision pass** (owner added 11 documents), and **Phase 2**. Use the `wave` values in the `agent_start` notes (`1`, `1-review`, `2`, `3`, `4`, `revision`, `phase2-A`, `phase2`) and the decision titles. Add a `phases` list with each phase's start and end times, its agents, and a one-sentence plain summary.
2. **Corrections numbering.** `build-log/corrections.md` has overlapping row numbers, because two Fact-Checkers appended at the same time (for example, two sets of rows numbered 122+). Don't edit the file's history. In the log, give each correction a unique sequential `log_no` in file order, and keep the original `#` as `row_label`. Count corrections by `log_no`.
3. **Summary.** Recompute the summary block for all phases: agents, runs, fact cards written and checked (across **all** `work/facts/*.json` card files, including the S, K, N, F, and G series), corrections, websites, candidates (Phase 1 and Phase 2 separately), and library size (manifest rows). Add a per-phase breakdown.
4. **Owner decisions.** Add an `owner_decisions` list, taken from decision notes whose title starts with "Owner" or contains "owner", so the page can show the human's choices clearly.
5. Run the script, validate the output, and report briefly.
