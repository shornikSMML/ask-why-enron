# enron-dryrun

Dry run of the Enron annotated build.

This project will become a website for undergraduates from any major. It tells the story of Enron's collapse, a major accounting scandal, and explains the accounting terms along the way. The site will be built by a team of AI **agents** led by a **coordinator**. Every step they take will be recorded so readers can see how the site was made.

**Status:** Phase 1 and Phase 2 are complete and fact-checked. Open `index.html` (or the GitHub Pages address) to read the site.

## What's in this repository

| Item | Purpose |
|---|---|
| `CLAUDE.md` | Standing instructions the coordinator and agents must follow: audience, content, sourcing rules, image rules, the build log, and technical limits. |
| `sources/` | Primary source documents (for example, the Powers Report, SEC filings, court opinions). Agents use these before anything else. |
| `images/` | Public-domain or Creative Commons images and original diagrams used on the site. |
| `build-log/` | The build log (`log.json`), which records every agent, its brief, its results, and the coordinator's decisions. |

## The plan

- **Phase 1:** The Story (6–8 chapters), Cast of Characters, Timeline (1985–2006), Glossary, and a "How This Was Built" page. Everything is fact-checked before Phase 1 counts as done.
- **Phase 2:** Lenses the reader can switch on, guided reading Pathways, and "Why This Matters to You" (what Sarbanes-Oxley changed).

The site is plain HTML, CSS, and JavaScript with no build step. Open `index.html` directly, or view it on GitHub Pages. Everything the agents did is recorded in `build-log/` and shown on the site's "How This Was Built" page. Working files (fact cards, drafts, fact-check reports, and the tools that assemble the site) are in `work/`.
