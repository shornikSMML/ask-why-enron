# Fact-check, Phase 2: "The Banks" page and the prepay diagram

Agent: Fact-Checker (instance B). Date: 2026-09-27. Method as in Round 2. I did not edit any file.

## What I checked

- **The built page.** `work/drafts/banks.html` has 52 citations, one for each `{{...}}` marker in `work/drafts/story-src/banks.src.html`.
- **Every citation against its card.** Each card exists and is OK or FIXED. Each `data-src` is a manifest id. The page numbers are right.
- **Every sentence against the card and the source.** The sources are:
  - the Senate hearing text;
  - the Senate staff report text;
  - the SEC release and complaint;
  - the Fifth Circuit opinion;
  - the Batson pages (I had image-checked all of them for the Banks cards).
- **The two SVGs and their `credits.json` entry.** Fingerprints: `diagram-prepay.svg` and `-narrow.svg` match the `sha256` and `narrow_sha256` in `credits.json`. The library sources used all match `download_log.csv`.

**No candidate documents are cited. Neither Merrill nor CIBC is described as pleading guilty.** The Fifth Circuit's "plea agreements" (K-025) are not used on the page.

## Findings

| # | Location | Problem | Source | Required fix | Severity |
|---|---|---|---|---|---|
| 1 | Page, "How a prepay worked", 4th paragraph: "The examiner's figure for Citigroup is $4.7 billion." `{{K-004!batson-final-app-g@p. 62#64}}` | The citation borrows card K-004 but points to a different source, `batson-final-app-g` PDF 64. K-004's checked quote is Roach's testimony. The $4.7 billion appears only in K-004's notes (verified there, and on the page image). A citation must rest on a card whose own quote and locator support it. | batson-final-app-g PDF 64, printed p. 62: "Citigroup and Enron ($4.7 billion) or JPMorgan Chase and Enron ($3.7 billion)" (image-checked) | Add a checked card for the App. G figure (e.g. K-061). Cite it plainly: `data-src="batson-final-app-g"`, page 64, loc "App. G, p. 62". The Fact-Checker can write the card on request. | **must-fix** |
| 2 | Page, "Merrill Lynch": "while the Senate staff report says a guaranteed 15 percent." `{{K-019!rpt-psi-fishtail@p. 2, Introduction#6}}` | Same problem: K-019 is an SEC-complaint card; the Senate figure is only in its notes. | rpt-psi-fishtail PDF 6, printed p. 2 (line ~202): "secretly promising Merrill Lynch to arrange a resale of the assets within six months and guaranteeing a 15 percent return on the deal." | Add a checked card (e.g. K-062) for this sentence and cite it plainly (`rpt-psi-fishtail`, page 6). | **must-fix** |
| 3 | Page, "Ask Why" box: "Merrill Lynch, the SEC alleged, relied on Enron's word that Andersen had approved the accounting." | This reverses the SEC's allegation. The complaint alleges that Merrill got Enron to sign a "warranty letter" that Merrill itself drafted. Merrill's committee wanted this as a record that it thought would "shield itself from liability", and Merrill, Furst and Tilney never talked to Andersen. The complaint also alleges they knew the deal was a sham regardless of the letter. "Relied on Enron's word" presents Merrill as misled, which the SEC did not allege. | sec-merrill-complaint paras. 43-45 (lines 138-142): "Merrill Lynch attempted to create a record that it thought would shield itself from liability or exposure"; "Merrill Lynch prepared the letter"; "never talked to Andersen"; "fully knew ... regardless of the purported 'warranty letter,' that the transaction was a sham" (card K-023) | Rewrite, e.g.: "Citigroup said it relied on Arthur Andersen's review. Merrill Lynch, the SEC alleged, had Enron sign a letter saying Andersen had approved the accounting, without ever speaking to Andersen itself." | **must-fix** |
| 4 | Page, "Merrill Lynch": "and that Fastow said 'this guarantee could not be in writing as it would defeat Enron's ability to recognize a gain on the sale.'" | The quoted words are the SEC complaint's words ("Fastow stated that this guarantee could not be in writing ..."), not Fastow's. Inside quotation marks after "Fastow said", readers will take them as his words. | sec-merrill-complaint para. 27 (K-020) | "... and that Fastow told them the guarantee could not be put in writing because that would stop Enron from recognizing a gain on the sale." (paraphrase, no quotation marks). Or: "and, in the complaint's words, that 'Fastow stated that this guarantee could not be in writing ...'". | should-fix |
| 5 | Page, "Merrill Lynch": "after Enron 'assured us that we will be taken out of our investment within six months'" | The words come from an internal Merrill document quoted in the complaint ("The document stated that Enron had 'assured us ...'"). As written, they read as Enron's own words. | sec-merrill-complaint para. 19 (K-019) | "... after, according to an internal Merrill document the SEC quoted, Enron had 'assured us that we will be taken out of our investment within six months'". | should-fix |
| 6 | Page, "Merrill Lynch": "the SEC's complaint says 22.5 percent a year" | Correct, but incomplete. The same paragraph gives "$250,000 plus 15% per annum or a flat 22.5% per annum", and para. 35 says Merrill earned "approximately a 22% annualized return". | sec-merrill-complaint paras. 19, 35 | Optional: "the SEC's complaint says 22.5 percent a year (or $250,000 plus 15 percent)". | note |
| 7 | Page, "Merrill Lynch": Furst and Tilney "declined to answer questions, invoking their Fifth Amendment right." | Neutral and correct, and "not evidence of guilt" is stated. For fairness, add their stated reason and their earlier cooperation. Both said they had met the staff voluntarily. Both declined only after learning that the Justice Department was investigating one of the transactions. | hrg-psi-banks-v1 PDF 189-190 (K-013) | "... who had met voluntarily with the staff, declined to answer after learning that one of the deals was under Justice Department investigation, invoking their Fifth Amendment right." | should-fix |
| 8 | Page, "How a prepay worked", 2nd paragraph: "Chase sent cash to Mahonia, Mahonia paid Enron, and Enron's later 'deliveries' flowed back to Chase with interest built in." | This follows "he said" but is written in the page's own voice. Because Chase disputes this account, the flow should read as Roach's simplified description. | hrg-psi-banks-v1 PDF 33 (K-002: Roach called it a "simplified version") | "In his simplified version, Chase sent cash to Mahonia, ..." | should-fix |
| 9 | Page, "RBS, CSFB, and Toronto-Dominion" and "How it ended" | The sources spell it "Toronto Dominion", with no hyphen. | batson-final-app-g passim | Use "Toronto Dominion" (or "Toronto-Dominion Bank" consistently if the site prefers; the library never uses the hyphen). | note |
| 10 | Page, "How it ended": "It shows no SEC or criminal action against RBS, CSFB, or Toronto-Dominion" | True of the banks. The library does show a 2002 wire-fraud indictment of an RBS banker, David Bermingham, and two unnamed colleagues (K-053; allegations; outcome not in the library). The page does not mention it, and without it a reader could take the sentence as "no one at RBS was charged". | batson-final PDF 72, fn. 112 (image-checked) | Optional: add "(the examiner noted that one RBS banker had been indicted in 2002 over a separate LJM1-related sale; the outcome is not in the library)". | note |
| 11 | Diagram `<title>` and the `credits.json` title field: "How a bank 'prepay' worked: a loan dressed up as trades" | The tag line states a disputed conclusion as fact. Chase's sworn position is that "prepaid forwards are fundamentally different than funded debt". The visible heading is neutral; the accessible title is not. | K-001, K-014 (Roach; SEC alleged) vs K-009 (Dellapina) | "How a bank 'prepay' worked (as Senate investigators and the SEC described it)", or drop the tag line. | should-fix |
| 12 | Diagram, "Net effect" box, first line: "Net effect: Enron gets cash now and repays it later, with interest set in advance." | Stated in the diagram's own voice, while the second line is attributed ("The SEC alleged ..."). Interest "set at the time of the contract" is the SEC's allegation, and the characterization is disputed by Chase. | sec-jpm-citi-press ("The interest amount was set at the time of the contract ... As alleged"); K-014 | "Net effect, as Roach and the SEC described it: ..." | should-fix |
| 13 | Diagram, sources line: "printed pp. 14–16, 60–62 (Roach, Dellapina)" | Dellapina's quoted words ("prepaid forwards are fundamentally different than funded debt") are on printed p. **63** (PDF 81). | hrg-psi-banks-v1 PDF 81, line ~5049 | "printed pp. 14–16, 60–63". | should-fix |
| 14 | Diagram, `credits.json` `fact_cards` | Lists K-004 for the examiner's $4.7 billion, the same problem as #1. | as #1 | Add the new App. G card (e.g. K-061) to `fact_cards` once it exists. | should-fix |

## Checked and correct, no change needed

**On the page:**
- Roach's quotes and claims, all under oath (PDF 31 oath).
- The four tests; the tax-return point; the $8B / $3.7B / $4.8B figures.
- The Senate staff's end-2000 estimate, attributed.
- Levin reading the Chase e-mail (not testimony); McCree (managing director, sworn) "unfortunate statement".
- Moody's (Stumpp, sworn); the SEC's "in substance loans" (alleged).
- Staff findings on Fishtail, Bacchus, Sundance and Slapshot. The quotes are verbatim, and "found" is used for the staff.
- Fox's denial is included; the 11 percent figure is right; Sundance's end on Nov. 30, 2001.
- A-073 ("returned the $200 million ... six months later").
- **Mahonia paragraph:** all three positions, attributed, plus Levin's 1986 letter correctly described (it names a different vehicle; the witnesses had not seen it). "The library does not settle the question."
- Bushnell (sworn).
- The "one Merrill Lynch employee's notes" wording (not attributed to Furst).
- CIBC: charged and settled, from the index title only, with no suggestion of a guilty plea.
- **Examiner's standard:** stated correctly ("could conclude"; "actual knowledge ... 'should have known' or 'suspicion' will not suffice"; "could be equitably subordinated").
- The three appendices named by letter.
- JPM/Citi settlement figures with "without admitting or denying"; the Citigroup order with findings.
- The Fair Fund ($236M); the DA settlements and regulators' agreements.
- The Merrill SEC case outcome "not in the library"; the four unnamed Merrill employees convicted and reversed (B-085, unnamed).
- The estate's suit ($3B, outcome not in library); the recommendation and "not in the library".
- **Tone:** neutral throughout; no sensational words.

**In the diagram:**
- Steps 1-4 follow Roach's sworn simplified version. Step 5 (swap, risk back to Enron) is labelled "SEC alleged".
- Recording panel: each line is attributed.
- End-2000 figures ($4B; +40% to $14B; -50% to $1.7B) are labelled a Senate staff estimate.
- $4.7-4.8B, "sources differ".
- Both quotes are verbatim, with speakers and "under oath" correct.
- The Mahonia footnote gives all three positions, attributed.
- The wide and narrow versions carry the same facts. The second "5" in the narrow layout is a label marker, not an error.

## Verdicts

| Item | Verdict | Remaining |
|---|---|---|
| `work/drafts/banks.html` (and `story-src/banks.src.html`) | **FAIL until fixed** | Must-fix #1, #2 (two citations resting on card notes; new cards needed) and #3 (the Ask Why sentence misstates the SEC's allegation about Merrill). Should-fix #4, #5, #7, #8. |
| `images/diagram-prepay.svg` + `-narrow.svg` | **PASS AFTER FIXES** | No factual errors. Should-fix #11 (title), #12 (attribute "Net effect"), #13 (page range), #14 (`fact_cards`). |

The two new glossary terms (`aiding-and-abetting`, `equitable-subordination`) were ignored as instructed. Both are used correctly in context.
