# Fixes, Round 2 Part B: Footnote (intro, closing, fn-05) and Chewco/LJM diagram

Agents: Footnote Annotator (`work/drafts/footnote.json`) and Image Researcher & Diagrammer (`images/diagram-chewco-ljm.svg`, `images/diagram-chewco-ljm-narrow.svg`). Date: 2026-09-26. Findings are from `work/facts/factcheck-round2-partB.md`. Nothing else was changed.

## Sources re-checked (fingerprints matched `sources/download_log.csv`)
- `powers-report-sec`: line 7085 (p. 199, the hedge wording for fn-05).
- `rpt-psi-board`: PDF 52 (printed p. 48), lines 3170-3193 of `work/text/rpt-psi-board.txt` ("about one page in length", "nearly unintelligible", "November 19, 2001, its 10-Q filing for the third quarter of 2001", "nine-page description").
- `enron-8k-nov-2001-ex99-1`: line 44 ("1997 through 2000 and the first two quarters of 2001").

## Footnote (`work/drafts/footnote.json`)

**#25 (intro): citation added.** The text is unchanged. I added a third cite to `intro.cites`:
- `rpt-psi-board`, PDF page 52, loc "Senate PSI staff report, printed p. 48, Finding (4), Inadequate Public Disclosure"
- quote: "The 1999 and 2000 footnotes, each of which is about one page in length ... The 2000 footnote, in particular, is nearly unintelligible"
- It supports "about one page long" and "almost no reader could tell what was going on."

**#26 (closing): Powers citations added.** I copied the two Powers cites from the intro into `closing.cites`, ahead of the existing `rpt-psi-board` cite:
- p. 201, PDF 207: "to some extent"
- p. 197, PDF 203: "understand what was going on"

Before, the closing cited only `rpt-psi-board`. It now has 3 cites.

**#27 and #29 (closing): one sentence rewritten.**
- Before: "After the scandal broke, Enron described the same dealings again in its filings of November 2001."
- After: "After Enron's problems became public, the company described the same dealings again in its quarterly report filed November 19, 2001."
- #29 was an optional tone note. I applied the wording the Fact-Checker suggested. I also changed "Enron described" to "the company described" so "Enron" is not repeated in the same sentence.

**#28 (fn-05, "found"): the committee's hedge restored.**
- Before: `It found that "many of them could only have been entered into with related parties."`
- After: `It said that "it seems likely that many of them could only have been entered into with related parties."`
- The cite quote was already the full hedged wording, so it is unchanged.

## Chewco/LJM diagram (both the wide and the narrow version)

**#22 (Chewco box and `<desc>`): absence of evidence, not fact.**
- Before: "The board was not told of Kopper's role."
- After: "The special committee found no evidence the board was told of Kopper's role."
- Layout, wide version: the Chewco text now runs 7 lines. All three bottom-row boxes grew from 176 to 214 tall so the row stays even. Their RESTATED tags moved down 38px. The footer moved down 38px. The canvas grew from 760 to 798.
- Layout, narrow version: the sentence now takes 2 lines. The Chewco box grew from 141 to 162. Its tag moved down 21px. Everything below it moved down 21px, including the timeline spine. The canvas grew from 1587 to 1608.
- I rendered both versions and checked them. No text overlaps.

**#23 (footer and `<desc>`, optional note, applied): the restatement period.**
- Footer before: "and that it would restate 1997–2000."
- Footer after: "and that it would restate 1997 through mid-2001."
- `<desc>` before: "and restated 1997 to 2000."
- `<desc>` after: "and that it would restate 1997 through mid-2001."

**Fingerprints.**
- I updated both fingerprints in `images/credits.json`:
  - `sha256`: 9eeb49f6... became 722a226bd2895b505082dd28b83e3caa48fe1d42e1c416f0d4ba958717572f21
  - `narrow_sha256`: 8c40e3ee... became c77ace35382585a0e104f23bcef65675158b57704613931ce7d284f5a54b035f
- I regenerated `images/credits.js` from the JSON. Only those two lines changed.

## Checks
- `python3 work/tools/integrate.py --no-log`: 0 problems. It rewrote `js/footnote-data.js` from the JSON.
- `python3 work/tools/test_site.py`: 0 problems (exit 0).
