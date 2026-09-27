# Pathway anchor requests (for the Site Builder)

From the Pathways Designer, 2026-09-27. `work/drafts/pathways.json` uses the anchors below. Anchors that already exist and need nothing: Cast ids (`cast.html#andrew-fastow` etc.), Glossary ids (`glossary.html#prepay` etc.), `#chapter` (the `<article>` on every chapter page), and the Footnote paragraph ids `footnote.html#fn-p0` to `#fn-p7`.

Everything else in this file does **not exist yet**. Anchors are case-sensitive and must match exactly.

## 1. Chapter headings: add an `id` to every `<h2>` (all 7 chapters)

Chapter `<h2>`s currently have no ids. Please add these, either in the Story Writer's fragments or with a small script at page load. A fixed table is safer than an automatic slug, because the pathways depend on the exact ids. **Bold** = used by a pathway now. The rest are for consistency and future use.

| Page | Heading | id |
|---|---|---|
| ch1 | Two pipeline companies | `two-pipeline-companies` |
| ch1 | Kenneth Lay takes charge | `lay-takes-charge` |
| ch1 | "From the reservoir to the burner tip" | `reservoir-to-burner-tip` |
| ch1 | Growing fast | **`growing-fast`** |
| ch2 | A trader, not just a pipeline | `a-trader` |
| ch2 | Revenue and profit | `revenue-and-profit` |
| ch2 | What mark-to-market accounting means | **`what-mark-to-market-means`** |
| ch2 | Marking investments to market | **`marking-investments`** |
| ch2 | Why the balance sheet mattered | `balance-sheet` |
| ch3 | Chewco | **`chewco`** |
| ch3 | The LJM partnerships | **`ljm`** |
| ch3 | Rhythms: a hedge with Enron's own stock | **`rhythms`** |
| ch3 | The Raptors | **`raptors`** |
| ch3 | What it added up to | **`what-it-added-up-to`** |
| ch4 | "Many push limits" | **`many-push-limits`** |
| ch4 | Andersen weighs its client | `andersen-weighs-its-client` |
| ch4 | A sudden resignation | `a-sudden-resignation` |
| ch4 | Sherron Watkins | `sherron-watkins` |
| ch4 | An error comes to light | `an-error-comes-to-light` |
| ch4 | The watchdogs outside | **`watchdogs-outside`** |
| ch5 | October 16: the third quarter | `october-16` |
| ch5 | Questions multiply | `questions-multiply` |
| ch5 | November 8: the restatement | **`november-8-restatement`** |
| ch5 | A rescue attempt | **`rescue-attempt`** (used as a fallback stop) |
| ch5 | The watchdogs | `the-watchdogs` |
| ch5 | November 28 to December 2 | **`november-28-to-december-2`** |
| ch5 | The tip of the iceberg | **`tip-of-the-iceberg`** |
| ch6 | Enron's auditor | `enrons-auditor` |
| ch6 | The fees | **`the-fees`** |
| ch6 | Errors and what the examiner concluded | `errors-and-examiner` |
| ch6 | The shredding | **`the-shredding`** |
| ch6 | Conviction, collapse, reversal | **`conviction-collapse-reversal`** |
| ch6 | The Big Four | **`big-four`** |
| ch7 | The investigations | `the-investigations` |
| ch7 | The trials | `the-trials` |
| ch7 | The employees' savings | `employees-savings` |
| ch7 | A new law | **`a-new-law`** |

Also on every chapter:
- The closing `<aside class="ask-why">`: id **`ask-why`** (used: `chapters/ch2.html#ask-why`).
- Every `<figure data-image="X">`: id `fig-X`. Used: **`chapters/ch3.html#fig-diagram-raptor`**, **`chapters/ch3.html#fig-diagram-chewco-ljm`**, **`chapters/ch5.html#fig-chart-restatement`**.

Note: a chapter URL may carry both a lens and a pathway, e.g. `chapters/ch3.html?lens=money&path=spes&stop=6#raptors`. The lens bar and the pathway bar must both read their own parameter and ignore the other.

## 2. Timeline: item ids and a tag filter in the URL

Timeline items have no ids (only year headings `#y1985` etc.). Please give each `<li class="tl-item">` the id `tl-` + its date string, e.g. `tl-2002-07-30`, `tl-1992`, `tl-1999-12`. Two items share the date `2001-10`: give them `tl-2001-10-lockdown` (401(k) lockdown) and `tl-2001-10-special-committee` (board forms a special committee). Neither is used by a pathway. Alternatively, add an `id` field to `timeline-data.js` with the same values.

Used now: **`tl-1992`** (Mark-to-market accounting for trading), **`tl-1999-12`** (Year-end deals with Merrill Lynch), **`tl-2002-07-30`** (The Sarbanes-Oxley Act becomes law), **`tl-2003-04-25`** (The PCAOB is ready), **`tl-2003-07-28`** (Two banks settle with the SEC).

**Tag filter from the URL:** `timeline.html?tag=auditors` should start with that filter button pressed (the same effect as clicking it). Used by the Andersen pathway, stop 9, with an empty anchor.

## 3. The Footnote: annotation anchors

The annotation ids `fn-01` to `fn-33` exist in `footnote-data.js`, but the page renders them only as `data-anno` on `<mark>`. Please give each mark `id="fn-NN"`. When the URL has `#fn-NN`, scroll to that phrase **and open its annotation** (panel or bottom sheet), as if the reader had selected it. Used now: **`footnote.html#fn-03`**, **`footnote.html#fn-06`**.

## 4. The Footnote: new "Other notes" sections (needs content, not only ids)

The "Reading the Footnotes" pathway (from `work/facts/footnotes-map.md` and the N-cards) has six stops on notes that **no page shows yet**:

| Anchor | Content |
|---|---|
| `footnote.html#note-1` | Note 1, Summary of Significant Accounting Policies (10-K lines 4091-4266) |
| `footnote.html#note-3` | Note 3, Price Risk Management Activities (4356-4633) |
| `footnote.html#note-4` | Note 4, Merchant Activities (4634-4687) |
| `footnote.html#note-9` | Note 9, Unconsolidated Equity Affiliates (5014-5151) |
| `footnote.html#note-15` | Note 15, Commitments (5793-5862) |
| `footnote.html#q3-10q` | Q3 2001 Form 10-Q, Notes 3, 4 and 8 |

**Coordinator decision needed:** someone (the Footnote Annotator or the Story Writer) has to write short sections for these from the N-cards: the note's title, 1-3 short verbatim excerpts, what a reader could learn, and what later filings and investigations found. The obvious place is a new section on `footnote.html`, "Other notes in the same report", after the existing "Elsewhere in the same report." A separate page would also work; if so, tell me the page name and I'll change the stops.

**Until then**, each of these stops has a `fallback` `{page, anchor}` in `pathways.json`, pointing to an existing page that covers the same topic. The pathway engine should use `fallback` when the main anchor is missing, and the test should accept a stop if either one resolves.

## 5. New pages (shells from brief 25)

`why-it-matters.html`: **`#s302`**, **`#s404`**, **`#pcaob`**, **`#independence`**, **`#whistleblowers`**, **`#today`**.
`banks.html`: **`#prepays`**, **`#deals`**, **`#institutions`**, **`#outcomes`**.

## 6. Existing error found on the live Footnote page (not an anchor; please pass to the coordinator)

In `js/footnote-data.js` (from `work/drafts/footnote.json`), both `context_passages` (`ctx-1`, 10-K lines 5134-5136, and `ctx-2`, lines 5141-5143) are labeled "Note 15 (Unconsolidated Equity Affiliates)". In the 10-K, **Unconsolidated Equity Affiliates is Note 9** (heading at line 5014). Note 15 is "Commitments" (line 5793). I checked the headings in `sources/03-sec-filings/enron-10k-fy2000.txt` (fingerprint matches). The label should read "Note 9". The Footnote Annotator or the Fact-Checker should fix it. I did not edit it.
