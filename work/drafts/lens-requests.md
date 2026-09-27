# Lens Writer: requests for facts without their own cards

From the Lens Writer (Phase 2). I used only cards checked OK or FIXED, plus the chapter drafts. No sources were opened and I used no web.

The items below would strengthen the lenses. Each one either appears only in a card's `notes` field (not its checked claim or quote, and sometimes at a different page from the card's locator) or is not in any card. I left all of them out of `lenses.json`. A Reader could turn them into cards if the coordinator wants them.

| # | Lens | Fact wanted | Where it seems to be | Importance |
|---|---|---|---|---|
| 1 | knew, board | At the October 2001 board meeting, officers described Watkins's letter as coming from an anonymous employee, and Lay "apparently did not disclose" its Raptor and accounting concerns to the other directors (a staff finding based on director interviews). | `rpt-psi-board` p. 45 (PDF 49); mentioned in F-002 notes only | useful |
| 2 | board, auditors | Duncan wrote in December 2000 that the Audit Committee presentation had to fit "about a 30 - 45 minute presentation." | `batson-final-app-b-part2` p. 131, n. 472; mentioned in C-035 notes only | useful |
| 3 | knew | The Powers Report says the partnerships were not "secret" and "all were disclosed to some extent," but the company tried "to say as little as possible." | `powers-report-sec` pp. 200-201; mentioned in A-064 notes only (the card's locator is p. 17) | useful |
| 4 | auditors, knew | The examiner concluded a fact-finder could find that Enron officers' failure to disclose side agreements did not prevent Andersen from discovering them. | `batson-final-app-b-part2` p. 166 (PDF 64); mentioned in C-029 notes only | useful |
| 5 | knew | Skilling told Kaminski that his group "acted more like cops," and moved the group out of risk control after the LJM deal (Kaminski's account, as the Fifth Circuit reports it). | `ca5-skilling-2009` PDF 9, n. 5; mentioned in F-014 notes only | useful |
| 6 | money | Lay waived about $60.6 million in change-of-control payments tied to the Dynegy merger. | `enron-10q-q3-2001` p. 14; mentioned in A-090 notes only (the card's locator is p. 13) | minor |
| 7 | money, knew | The special committee said the Southampton employees appear to have violated Enron's Code of Conduct. | `powers-report-sec` p. 27; mentioned in A-050 notes only | minor |
| 8 | knew | The first date any director or Audit Committee member was told of the $1 billion Raptor equity error (found in August 2001). No card covers this. | Unknown; may not be in the library | useful |
| 9 | knew, board | Whether and when the board was told about Lay's September 2001 stock sales or his credit-line repayments before October 2001. No card covers this. | Unknown; may not be in the library | minor |

## Conventions used in `lenses.json` (for the Site Builder)
- `para_index` counts the `<p>` elements in `work/drafts/chN.html`, starting at 1, in document order. It skips `<p class="dek">` and any `<p>` inside `<aside class="ask-why">`. `para_start` is the first 8 words of the paragraph's text with citation links removed. `para_key` is `chN-pI`.
- Each note's `cites` is a list of `{card, source_id, page, loc}`. `page` is the PDF page, or null for .txt and .htm sources.
- Each summary bullet is `{text, cites}`, not a bare string, so every fact in a bullet has a visible citation.
- Each `knew` strip entry is `{date, who, what, cites}`. Dates use `YYYY`, `YYYY-MM` or `YYYY-MM-DD`.
- A top-level `_meta` key describes these conventions. The site should ignore it, or the coordinator can strip it when wrapping the file.
- If a chapter has no paragraph tagged for a lens (ch1 board and knew, ch5 board, ch7 auditors), its `notes` list is empty. It still has a summary and an Ask Why question.
