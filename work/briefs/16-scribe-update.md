# Brief: Scribe, second run (fix and complete the log)

Update `work/tools/build_log.py` (keep it deterministic) so that:
1. **An agent can have several runs, each with its own brief.** For example, "images" ran with `05-images.md` and then `12-images-pass2.md`; "footnote" ran once, then again for fixes. Each run stores its own `brief_file` and brief text. A brief counts as "assigned" if any `agent_start` note uses it. `briefs_not_yet_assigned` must be correct (right now it wrongly lists `05-images.md`).
2. **Runs started by message rather than a new brief** (resumed agents: an `agent_finish` or `review` with no new `agent_start`) are shown as a separate run, with the `handoff` note text as their brief summary. Check `inbox.jsonl` for such cases (e.g. the Fact-Checker's follow-up checks; the Story and Reference Writers' Round 2 fixes; the Round 3 re-checks). Also include the exact follow-up messages the coordinator sent, stored in `build-log/messages.jsonl`, if that file exists.
3. **Every agent's decision and reason come from its latest finish note.**
4. **`corrections.md` rows are parsed**, including any rows added later.
5. **There's a plain-language `summary` block** for the How This Was Built page: the number of agents, the number of runs, sources read, fact cards written and checked, the number of corrections, web sources used, and candidates found (count the rows in `sources/candidates/candidates.csv`). Compute these from files; don't type them by hand.

Then run the script and validate the output as before. Report what changed, briefly.
