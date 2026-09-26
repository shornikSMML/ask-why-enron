# Brief: Scribe (first run)

**Role:** Keep the build log. The coordinator appends timestamped notes to `build-log/inbox.jsonl` (one JSON object per line, with `type` one of decision | agent_start | agent_finish | handoff | review | web_source | correction). The exact briefs sent to agents are the files in `work/briefs/`. Your job is to turn these into the official log.

**Do this:**
1. Write `work/tools/build_log.py`, a deterministic script that reads `build-log/inbox.jsonl`, the brief files in `work/briefs/`, and `build-log/corrections.md`, and writes:
   - `build-log/log.json` with this structure:
     ```json
     {"project": "Ask Why: The Rise and Fall of Enron",
      "generated": "ISO time",
      "coordinator": {"name": "Coordinator", "role": "...", "plan": [...decisions whose title starts with 'Original plan'...], "decisions": [...all decision records, in order...]},
      "before_the_agents": {"summary": "...", "fingerprint_check": "..."},
      "agents": [{"id", "name", "role", "brief_file", "brief" (full text of the brief file, plus common rules referenced by file name), "runs": [{"started", "finished", "inputs" (manifest ids and page ranges), "outputs" (files), "decision": "accepted|sent back|pending", "reason"}], "handoffs": [{"time", "from", "to", "what"}]}],
      "reviews": [...], "corrections": [...parsed rows of corrections.md...], "web_sources": [{"site", "url", "used_by", "purpose"}],
      "timeline": [...every record in time order, with a short label...]}
     ```
     Agent records come from `agent_start` and `agent_finish` notes (fields: `agent_id`, `name`, `role`, `brief_file`, `inputs`, `outputs`, `decision`, `reason`). Handoffs come from `handoff` notes (fields: `from`, `to`, `what`).
   - `build-log/log.js`, which contains `window.BUILD_LOG = <the same JSON>;` so the website can load it from file://.
   The script must be idempotent: re-running it regenerates both files from the inbox. Don't hand-edit `log.json`.
2. Fill in `before_the_agents` from `sources/README.md` and `CLAUDE.md`: the owner assembled and verified the library before any agent ran; the three lessons (the annotated advocacy copy of the Batson Final Report nearly used in place of the clean court copy; three different documents each labeled Batson "Appendix E"; fingerprints confirmed the downloaded files matched the originals). Put this text in a constant in the script. Plain language.
3. Run the script, and check the output is valid JSON and that `log.js` parses (`node -e` if node exists, otherwise Python).
4. Also write `build-log/README.md` (replace the existing short one), explaining in two short paragraphs what each file is.

**Outputs:** `work/tools/build_log.py`, `build-log/log.json`, `build-log/log.js`, `build-log/README.md`.
