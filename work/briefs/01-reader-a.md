# Brief: Reader A: The Company & the Accounting

**Role:** You read source documents and produce fact cards (see `00-common-rules.md`) that the Story Writer and Reference Writer will use for Chapters 1, 2, 3 and 5, and for the Timeline and Glossary. You write no prose for the site.

**Chapters you supply:**
1. Origins (1985 merger that created Enron; early business)
2. The business model and mark-to-market accounting (energy trading, "asset light," how Enron booked future profits today)
3. The special purpose entities (Chewco and JEDI; LJM1 and the Rhythms hedge; LJM2; the Raptors; who ran them; how much Fastow and others earned; how they inflated earnings or hid debt)
5. The collapse (Oct 16, 2001 third-quarter loss and equity reduction; Nov 8, 2001 restatement of 1997–2000 amounts by year; Dynegy merger agreement and its end; Dec 2, 2001 bankruptcy filing)

**Documents (manifest ids) and roughly which sections:**
- `powers-report-sec`: Executive Summary; Chewco; LJM1/Rhythms; LJM2; Raptors; the sections on the board's oversight and on disclosure (except the disclosure of Note 16, which the Footnote Annotator covers; don't duplicate it). Cite this official SEC copy. Find a page number for key facts in `powers-report` (the PDF; text is in `work/text/powers-report.txt`) so readers can open the page.
- `enron-10k-2000`: Item 1 (business description), the note on significant accounting policies (look for mark-to-market / "price risk management"), revenue and net income figures in the selected financial data. Skip Note 16 (the Footnote Annotator has it).
- `enron-10q-q3-2001`: the Q3 2001 loss and charges; the equity reduction.
- `enron-8k-nov-2001` and `enron-8k-nov-2001-ex99-1`: the restatement amounts by year.
- `enron-8k-dynegy-merger`: the merger terms.
- `batson-1st-interim`: its summary or introduction only (what the examiner was asked to do; any headline findings).
- `batson-final`: introduction and summary of conclusions only (for example the "six accounting techniques"); plus `batson-final-app-a` for definitions you need.
- `rpt-jct-vol1`: company background and history (1985 origins, growth, headcount if given). Use the table of contents to find it.
- `rpt-psi-fishtail`: introduction or executive summary only, for 1–3 cards on the banks' role.
- Reader tip to test: "At its peak, Enron was America's seventh-largest company." `sec-kopper-complaint` says "reportedly the seventh largest corporation in the United States." Look for any other library text supporting a size ranking (for example "seventh largest" or "Fortune 500" in the texts you read) and make cards for what you find, including what "largest" was measured by if a source says so. Reader tip to test: "Warren Buffett read Enron's footnote, didn't understand it, and threw the 10-K away." Run `grep -il buffett work/text/*.txt sources/*/*.txt` once and report the result. Don't look anywhere else.

**Target:** about 60–90 cards. Include the key dollar amounts and dates.

**Outputs:**
- `work/facts/reader-a.json` (the cards, ids A-001 ...)
- `work/facts/reader-a-readlog.md` (documents, page or line ranges, fingerprint results)
- `work/facts/reader-a-gaps.md` (gaps, in the format described in the common rules)
