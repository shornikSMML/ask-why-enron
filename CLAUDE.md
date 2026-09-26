VOCABULARY
On the site and in the build log, call every worker an "agent" and yourself the "coordinator." (In a Project, each agent is a thread; in a single session, each agent is a subagent.)

AUDIENCE AND TONE
- Readers are undergraduates from any major. Explain every accounting term in plain language the first time it appears, and link it to a glossary.
- Tell it as a story, but stay neutral and factual. No sensationalism.

WHAT TO BUILD, IN TWO PHASES
Phase 1 must be complete, fact-checked, and working before any Phase 2 work starts.

Phase 1:
1. The Story: 6–8 short chapters (origins; the business model and mark-to-market accounting; the special purpose entities; warning signs and the whistleblower; the collapse; Arthur Andersen; aftermath and reform).
2. Cast of Characters: each person's role, and precisely what happened to them legally.
3. Timeline, 1985–2006.
4. Glossary.
5. "How This Was Built" page (see BUILD LOG).
6. The Footnote: the related-party footnote from Enron's 2000 Form 10-K (sources/03-sec-filings/enron-10k-fy2000.txt), shown in full and annotated phrase by phrase in plain language, the way an annotated edition explains a difficult poem: what each phrase said, what it left out, and what the investigations later found. Every annotation links to its source.

Phase 2:
6. Lenses the reader can switch on over the Story: Follow the Money; The Auditors; The Board; Who Knew What, When.
7. Four to six Pathways, e.g. A First Reading; Mark-to-Market Explained; The Special Purpose Entities; Andersen's Fall and the Big Five to Big Four; From Enron to Sarbanes-Oxley and the PCAOB.
8. "Why This Matters to You": what Sarbanes-Oxley changed (CEO/CFO certification, internal control reporting, the PCAOB, auditor independence) and what that means for anyone entering business or accounting today.

SOURCES AND ACCURACY (highest priority)
- The source library in sources/ is complete and verified. manifest.csv lists every document; download_log.csv holds each file's SHA-256 fingerprint. Base every factual claim on documents in this library.
- The rules in sources/README.md ("Rules for the agents") apply to every agent, not just the fact-checker.
- Use only files listed in manifest.csv. Do not substitute copies found on the web, even of the same document: some online copies are annotated by advocacy groups, and some documents exist in several versions (for example, three different Batson "Appendix E"s). If unsure which file is right, ask the coordinator rather than guessing.
- Before relying on a file, confirm its fingerprint matches download_log.csv. A mismatch means stop and report it.
- Known gaps: the Batson Second and Third Interim Reports are not in the library. Do not look for them online. If a claim would need them, leave it out or mark it unverified.
- Explaining concepts (what mark-to-market accounting is, what a special purpose entity does) may draw on general knowledge. Anything about specific events, dates, dollar amounts, or people must come from the library.
- Use the web only for images (see IMAGES) and for the Source Scout's work (see MISSING SOURCES). Log every web source used.
- Every factual claim about a real person must carry a citation a reader can see: document and page or section.
- Never invent quotations. Quote only verbatim from a cited source, briefly. Do not reproduce text from copyrighted books, articles, or films.
- When sources disagree or are uncertain, say so instead of guessing.
- One agent acts as fact-checker and reviews all Phase 1 content against the sources before Phase 1 is marked done. Log every correction it makes.
- Read efficiently. Many documents run hundreds or thousands of pages. Read only the documents and sections a task needs, and record page ranges in the build log.

MISSING SOURCES
- When an agent needs a source the library doesn't have, it does not search for one itself. It records the need in build-log/gaps.md: the claim it wanted to make, what kind of document would support it, and how important it is (critical, useful, or minor). Then it leaves the claim out or marks it unverified, and keeps working.
- One agent, the Source Scout, works through gaps.md, starting with critical gaps. It looks first on official sites (sec.gov, justice.gov, govinfo.gov, supremecourt.gov, uscourts.gov, congress.gov). It downloads each candidate into sources/candidates/ and adds a row to sources/candidates/candidates.csv, using the same columns as manifest.csv plus: which gap it fills, its SHA-256 fingerprint, whether it is an official copy or a mirror, and whether other versions of the document exist.
- Never use an annotated, advocacy, or unofficial copy when an official one exists.
- If a document is only available behind a paywall or login (for example, PACER), record that in gaps.md instead of looking for another copy.
- In the dry run, collect no more than 10 candidates.
- Candidates are NOT part of the library. No agent may cite or rely on them until I approve them.
- At the Phase 1 check-in, the coordinator reports gaps.md and the candidates. I will add approved documents to manifest.csv and download them through my GitHub Action. Then a revision pass fills in the claims that were marked unverified.
  
IMAGES (required)
- Every chapter should have at least one image or diagram.
- Use only images that are public domain or Creative Commons licensed. Good sources: Wikimedia Commons, the Library of Congress, and U.S. government works. No news-agency photos (AP, Getty, Reuters) and no screenshots from films or TV.
- Record each image's source, author, and license in a credits file, and show the credit where the image appears.
- Download images into the images/ folder; don't link to them on other websites.
- Only use a photo of a real person if the source clearly identifies who it is.
- Where no good image exists, draw an original diagram instead (for example, how money moved through a special purpose entity).

BUILD LOG (required from the very first step)
- Keep a file at build-log/log.json. Record every agent: its name, its role, the exact brief you sent it, when it started and finished, what it produced, whether you accepted its work or sent it back (and why), and any handoffs between agents.
- Also record your own decisions as coordinator: your original plan, any changes to it, and why.
- Record which websites the agents actually used for sources and images.
- The "How This Was Built" page reads this log and shows, for a non-technical audience: a diagram of the coordinator and its agents, a timeline of the build, and each agent's brief and result.

BEFORE THE AGENTS (for the "How This Was Built" page)
This site will be shown in a workshop on AI agents, so "How This Was Built" matters as much as the story. It should open with the human work that came first: I assembled and verified the source library before any agent ran. Explain in plain language what a SHA-256 fingerprint is and why it matters, and include these lessons:
- An annotated copy of the Batson Final Report from an advocacy website nearly got used in place of the clean court copy.
- Three different documents were each labeled Batson "Appendix E."
- Fingerprints confirmed the downloaded files matched the originals.

TECHNICAL
- Plain static website: HTML, CSS, and JavaScript only. No build step, no server, no outside services. It must work by opening index.html or from GitHub Pages, and it must read well on a phone.

HOW TO WORK WITH ME
- I am not a programmer. Keep updates short and in plain language.
- Before starting any agents, propose your plan: which agents, each one's role, what runs in parallel, and what order. Wait for my approval.
- Check in with me when Phase 1 is done, before starting Phase 2.
