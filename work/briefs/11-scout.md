# Brief: Source Scout

**Role:** Work through `build-log/gaps.md`, **critical gaps first**, and find candidate source documents. Follow `CLAUDE.md` MISSING SOURCES exactly. You may use the web, but only for this.

**Rules:**
- Look first on official sites: sec.gov, justice.gov, govinfo.gov, supremecourt.gov, uscourts.gov (including ca5.uscourts.gov and the district court sites), congress.gov, loc.gov. Never use an annotated, advocacy, or unofficial copy when an official one exists. If only an unofficial mirror exists, you may take it, but mark it `mirror` and say so.
- If a document is only behind a paywall or login (for example PACER), don't look for another copy. Mark the gap row "paywalled: <where>" instead.
- **At most 10 candidates in total.**
- Download each to `sources/candidates/` (create it; this is the only place in `sources/` you may write), with a descriptive filename. Add a row to `sources/candidates/candidates.csv` with the same columns as `sources/manifest.csv` (`id,folder,filename,title,date,source_body,url,public_domain,status,notes`) plus `fills_gap,sha256,official_or_mirror,other_versions_exist`. Set status to `candidate-unapproved`.
- Check each download is the real document, not an error page (look at its size and first page), and compute its SHA-256.
- **Candidates are not part of the library.** Don't summarize their contents for anyone. Nobody may cite them until the owner approves.
- Don't look for the Batson Second or Third Interim Reports. The owner has said they're not available free online (see `sources/README.md`).
- In `build-log/gaps.md`, update each gap's Status column (e.g. "candidate: <id>" / "not found on official sites" / "paywalled: PACER"). Don't delete rows.

**Output:** `sources/candidates/*`, `sources/candidates/candidates.csv`, the updated `build-log/gaps.md`, and `work/facts/scout-websites.md` (every site and URL you visited, and what you found).
