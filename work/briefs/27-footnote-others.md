# Brief: Footnote Annotator, Phase 2 ("Other notes in the same report")

Follow `00-common-rules.md`. Use only checked cards (OK or FIXED): `work/facts/reader-footnotes.json` (N-cards; read every `checker_note`), plus the existing A- and fn-cards. **You may copy short verbatim excerpts from `enron-10k-2000` and `enron-10q-q3-2001`, but every excerpt must be exact.**

1. **New section, "Other notes in the same report".** Write `work/drafts/footnote-others.json`, an array of entries `{id, title, source_id, lines, excerpt, said, left_out, found, cites}`. Entries (ids exactly as follows):
   - `note-1`: Accounting policies (mark-to-market; consolidation)
   - `note-3`: Price risk management
   - `note-4`: Merchant activities
   - `note-9`: Unconsolidated equity affiliates
   - `note-15`: Commitments (with the stock-price triggers from Notes 10–11 and the MD&A mentioned as "elsewhere", per the cards)
   - `q3-10q`: the Q3 2001 10-Q (Osprey and Marlin; the $3.9 billion)

   For each:
   - the excerpt: 1–3 short verbatim passages, with the line range;
   - "What it said", "What it left out", and "What the investigations found", in the same plain style as the Note 16 annotations;
   - citations.

   Also write a short intro (in `work/drafts/footnote-others-intro.txt`, 2–3 sentences). It should say there were about 20 notes; Note 16 drew the investigators' attention, but pieces of the story sat in several notes; and reading them together is the skill.
2. **Fix an error the Pathways Designer found.** In `work/drafts/footnote.json`, the two "elsewhere in the same report" context passages (`ctx-01`/`ctx-02`) are labelled "Note 15 (Unconsolidated Equity Affiliates)". In the 10-K, lines 5125–5145 fall inside **Note 9** (Note 9 runs from line 5014 to 5151; Note 15 is Commitments). Correct the label and any related text. Log the correction as a row in `build-log/corrections.md`.
3. Run `python3 work/tools/integrate.py --no-log` and the tests. The Site Builder is adding the renderer for `footnote-others.json`; if it isn't there yet, just check that your JSON is valid.

Final report as usual.
