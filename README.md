# enron-dryrun

Dry run of the Enron annotated build.

This project will become a website for undergraduates from any major. It tells the story of Enron's collapse, a major accounting scandal, and explains the accounting terms along the way. The site will be built by a team of AI **agents** led by a **coordinator**. Every step they take will be recorded so readers can see how the site was made.

**Status:** Setup only. The website has not been built yet.

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

The finished site will be plain HTML, CSS, and JavaScript. You'll be able to open `index.html` directly or view it on GitHub Pages.
