# Fact-check, Phase 2: "The Banks" cards K-001 to K-060

Agent: Fact-Checker (instance B). Date: 2026-09-27. I checked each card as in Round 1: the quote at its locator, the claim against the source, the verb and source type, oaths, and disagreements. The verdicts and notes are also written into each card (`checked`, `checker_note`) in `work/facts/reader-banks.json`.

## How I checked

- **Fingerprints.** All library files used match `sources/download_log.csv`.
- **Quotes: all 60 found at their stated pages.** A script normalized every quote and searched the text copies page by page. For the two SEC HTML files it searched the original HTML. Every quote was found at its stated PDF page; one (K-012) runs across a page break as the card says. Hyphens at line breaks were rejoined.
- **Page images: all 21 OCR cards checked.** For every card from the OCR'd Batson reports I opened the page image myself, as follows.

  | Document | PDF pages opened |
  |---|---|
  | Final Report App. E (RBS) | 5-6, 102 |
  | Final Report App. F (CSFB) | 35, 95 |
  | Final Report App. G (Toronto Dominion) | 4-6, 64-65 |
  | Final Report | 7-8, 15-16, 20, 66, 72-75, 80-83, 97-98, 104, 106 |

  All quotes match the images.
- **Oaths: every "testified" card has an oath on the record.**

  | Witnesses | Where sworn |
  |---|---|
  | Roach, Brown | PDF 31 |
  | Rating-agency panel, including Stumpp | PDF 43-44 |
  | McCree, Traband, Dellapina | PDF 76 |
  | Hendricks, Bushnell, Reilly, Caplan | PDF 109 |
  | Furst, Tilney | PDF 189 |

  Senator Levin's statements are correctly labelled as not testimony.
- **Report and letter always named.** The Batson appendix cards say "Final Report, Appendix E (RBS) / F (CSFB) / G (Toronto Dominion)". None is confused with the Second or Third Interim appendices.

## Verdicts

| Card | Verdict | Note |
|---|---|---|
| K-001 | OK | |
| K-002 | OK | |
| K-003 | OK | |
| K-004 | OK | $4.8B vs $4.7B confirmed; see the points below. |
| K-005 | OK | |
| K-006 | OK | |
| K-007 | OK | |
| K-008 | OK | |
| K-009 | OK | |
| K-010 | FIXED (notes) | Added Levin's reading of the 1986 Chase letter (Exhibit 118); see Mahonia below. |
| K-011 | OK | |
| K-012 | OK | |
| K-013 | OK | Fifth Amendment presented neutrally. |
| K-014 | OK | |
| K-015 | OK | |
| K-016 | OK | |
| K-017 | OK | |
| K-018 | OK | |
| K-019 | OK | 15% vs 22.5% confirmed; see below. |
| K-020 | OK | |
| K-021 | OK | |
| K-022 | OK | |
| K-023 | OK | |
| K-024 | OK | |
| K-025 | FIXED | The "free to testify" statement was the district court's, relied on by the Fifth Circuit. |
| K-026 | OK | |
| K-027 | OK | |
| K-028 | OK | |
| K-029 | OK | |
| K-030 | OK | |
| K-031 | OK | |
| K-032 | OK | |
| K-033 | FIXED (notes) | "may have provided the final oral approval" is the staff's summary, not Bushnell's words. |
| K-034 | FIXED | $1.5M "breakage costs" went to the Caymus Trust and was "apparently passed along" to Citigroup. Hedge restored. |
| K-035 | OK | |
| K-036 | OK | |
| K-037 | OK | |
| K-038 | OK | |
| K-039 | OK | |
| K-040 | OK | |
| K-041 | OK | |
| K-042 | OK | |
| K-043 | OK | |
| K-044 | OK | |
| K-045 | OK | |
| K-046 | OK | |
| K-047 | OK | |
| K-048 | FIXED (notes) | The note implied Rob Furst wrote the "aid/abet Enron income stmt. manipulation" notes. The examiner says only "one Merrill Lynch employee's notes" (fn. 200 cites a fax from Furst to Brown). Do not attribute the words to either man. |
| K-049 | OK | |
| K-050 | OK | |
| K-051 | OK | |
| K-052 | OK | |
| K-053 | OK | |
| K-054 | OK | |
| K-055 | OK | |
| K-056 | OK | |
| K-057 | FIXED (notes) | "Toronto Dominion argued" corrected: the examiner anticipated that it "may argue". |
| K-058 | OK | |
| K-059 | OK | |
| K-060 | OK | |

**Totals:** 60 cards; 54 OK, 6 FIXED, 0 rejected. Corrections are logged as rows 122-127 in `build-log/corrections.md`.

## The points to watch

1. **Merrill and CIBC "plea agreements" (K-025).**
   - The Fifth Circuit (PDF 60-61) uses the words "the government's plea agreements with Merrill Lynch and Canadian Imperial Bank of Commerce". It gives no terms, dates or charges.
   - No card says either bank pleaded guilty or was convicted. I scanned all 60 claims and notes.
   - **Site rule:** if the page mentions these agreements at all, it must quote "plea agreements" as the Fifth Circuit's term and must never say either bank pleaded guilty or was convicted. Better still, leave them out until the agreements are in the library (Reader E's gap 3).
   - The CIBC card (K-018) rests only on an SEC index title: "charged ... simultaneously settles ... $80 million". It adds nothing about admission.
2. **Fifth Amendment (K-013).**
   - Furst and Tilney were sworn. Both said they had met voluntarily with staff. They then declined to answer after learning of a Justice Department investigation. The card states this neutrally.
   - Furst's own "even innocent witnesses may assert" point is in the notes.
   - **Site rule:** say plainly that invoking the Fifth is not evidence of guilt.
3. **Mahonia control (K-002, K-010, K-045): the sources disagree, and the library does not settle it.**

   | Source | What it says |
   |---|---|
   | Roach (sworn) and Levin | "one of its shell corporations" |
   | Dellapina, for Chase (sworn) | "beneficially owned by a charitable trust"; officers "neither appointed nor controlled by Chase or Enron" |
   | The examiner | "shell entities set up by JPMorgan Chase and Citigroup" |
   | Levin reading a 1986 Chase Jersey letter (Exhibit 118) | SPVs to be "controlled by Chase" but owned through a "charitable trust". The portion read names East Moss, not Mahonia. The Chase witnesses said they had never seen it. |

   Show all positions, attributed.
4. **Citigroup's prepay total ($4.8B vs $4.7B).**
   - Roach, sworn: $4.8 billion from 14 deals (K-004).
   - Batson Final App. G, printed p. 62 (image-checked): $4.7 billion.
   - Both give JPMorgan Chase $3.7 billion.
   - Say "about $4.7-4.8 billion" or cite each source.
5. **Merrill's promised return (15% vs 22.5%).**
   - The SEC complaint gives "$250,000 plus 15% per annum or a flat 22.5% per annum" (para. 19) and "22.5%" (paras. 18, 26). It says Merrill actually earned "approximately a 22% annualized return" (para. 35).
   - The Senate staff report says "guaranteeing a 15 percent return" (p. 2).
   - Cite each source for its own figure (K-019 and K-021 do); never merge them.

## Other notes for the writer

- Every Batson conclusion is civil: "sufficient evidence for a fact-finder to conclude". It is not a finding that a bank did anything. The examiner is "not the ultimate decision maker" (Final Report PDF 16).
- K-053 (the RBS bankers) rests on an indictment: use "allegedly" and "charged". The outcome is not in the library.
- The library shows no SEC or criminal action against RBS, CSFB or Toronto Dominion. That is not proof that none occurred (K-060). Write "The library documents show no ..." and never "never charged".
- Reader E's gaps file is appropriate. No new gaps.

## Verdict

**`work/facts/reader-banks.json`: PASS.** All 60 cards are usable after today's six fixes, with the site rules above on the Merrill/CIBC agreements and the Fifth Amendment.
