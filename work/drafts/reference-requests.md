# Reference Writer: requests to the coordinator

Agent: Reference Writer. These are things I left out or need decided. I did not read sources to fill them.

## People left out of the Cast (need an absence check first)
| Person | Why left out | What is needed |
|---|---|---|
| Nancy Temple (Andersen in-house lawyer) | Central to the shredding story (cards C-001, C-018), but no card says whether the library shows charges against her. Without that, I can't give her an accurate `outcome_status`. | A Reader or the Fact-Checker confirms whether any library document shows charges against her (an absence card like B-058). If none, add her with "no charges shown in library". |
| Lea Fastow, Richard Buy, Greg Whalley, Vince Kaminski, Raymond Troubh | Named in cards, but no card covers their legal status. | Same absence check if the coordinator wants them in the Cast. |

## Images
- The Cast uses no images: `images/credits.json` has no photos of individual people. No placeholder ids are used in the Cast or Timeline.
- Optional: an original diagram of "who was on both sides of the LJM deals" (Fastow, Kopper and Glisan as Enron officers and LJM managers, per cards A-040, A-042, B-037) would suit the Cast page. Suggested id: `diagram-ljm-both-sides`.

## Test script
- `work/tools/test_site.py` line 119 clicks a timeline filter `data-tag="law"`, a tag from the old sample data. The brief's tag list uses `legal`, so the test now times out at that step. The Site Builder should change `law` to `legal`. My own browser check of cast.html, timeline.html and glossary.html (1440 px and 360 px) found no console errors, no horizontal scrolling, and no "Sample data" label. The failed test run overwrote screenshots in `work/screens/`; I restored them with `git checkout`.

## Glossary ids for the Story Writer
The glossary has 120 terms. Besides the Footnote terms and the brief's list, it includes ids the chapters are likely to need, so the Story Writer can reuse them instead of making new ones: `chapter-11`, `bankruptcy-examiner`, `fiduciary-duty`, `fifth-amendment`, `off-balance-sheet`, `three-percent-rule`, `prepay`, `credit-rating`, `investment-grade`, `going-concern`, `whistleblower`, `document-retention-policy`, `securities-fraud`, `insider-trading`, `wire-fraud`, `conspiracy`, `superseding-indictment`, `count`, `civil-case`, `sec-complaint`, `settlement`, `disgorgement`, `convicted`, `reversed`, `remand`, `board-of-directors`, `outside-director`, `special-committee`, `conflict-of-interest`, `chief-executive-officer`, `chief-operating-officer`, `chief-accounting-officer`, `treasurer`, `cpa`, `audit-opinion`, `auditor-independence`, `non-audit-services`, `partner-rotation`, `hhi`, `blackout-period`, `internal-control`, `analyst`, `earnings-per-share`, `dilution`, `funds-flow` (cash flow from operations), `market-capitalization`, `fair-value`, `form-10-q`, `form-8-k`, `footnote`.

## Presentation choices the coordinator may want to review
- **Fastow, Glisan, Delainey** are labeled "convicted" because the Justice Department's 2004 releases list them as "convicted to date." Each entry says the library does not show whether by plea or trial, the charge, or the sentence.
- **Lay** is labeled "conviction vacated (died before appeal)" as the brief specifies. His entry adds: "The library does not say whether he had filed an appeal" (card B-011 note).
- **McMahon** is labeled "charged — outcome not in library" for the 2007 SEC civil charge, and the entry says the library documents show no criminal charges against him.
- **David Duncan** is labeled "SEC settlement" (the SEC's list calls his case a "settled action"); the entry says the library has no documents on any criminal case.
- **Seventh-largest:** used only in the ruled wording, in the timeline (2001-04), citing `rpt-jct-vol1` p. 58 (PDF 86) and `batson-final` n. 27 (PDF 18). No "at its peak," no "in the world." Buffett is not mentioned anywhere.
- **Andersen's CEO quote (Dec 12, 2001):** not used anywhere in my files. Berardino's Cast entry cites only his Feb 5, 2002 testimony.
- Timeline date for the Fortune ranking is "2001-04" (Fortune's list dated April 16, 2001, per card A-014).
