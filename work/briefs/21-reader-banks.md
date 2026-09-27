# Brief: Reader E: The Banks (Phase 2)

Follow `00-common-rules.md`. Card ids `K-001`… in `work/facts/reader-banks.json`. No web. Target: 40–60 cards.

**Purpose:** a new short page, "The Banks", and a Banks pathway. It should explain how financial institutions helped Enron (prepays that looked like trading but worked like loans; FAS 140 "sales"; the specific deals), what each institution was alleged to have done or agreed to, and how the regulators' cases ended **as the library shows**.

**Documents:**
- `rpt-psi-fishtail`: the full report, which is short. Cover the four transactions.
- `hrg-psi-banks-v1` / `-v2`: search, then read opening statements and key testimony (the prepays; Citigroup, JPMorgan Chase, Merrill Lynch witnesses).
- `sec-jpm-citi-press`: the settlements and amounts.
- `sec-merrill-complaint`: the Nigerian barge allegations.
- `batson-final`: the summary sections on the banks.
- `batson-final-app-e` (RBS), `-app-f` (CSFB), `-app-g` (Toronto-Dominion): **their conclusions sections only**. These are scans. Run OCR first with `work/tools/ocr.sh <id> <pdf>` (OMP_THREAD_LIMIT is already set in the script), or read the page images. **Always name the report and the letter** (e.g. "Batson Final Report, Appendix E (RBS)"), because three different reports each have an Appendix E.
- Existing cards already mention the banks (search `work/facts/*.json` for "bank", "prepay", "Citigroup", "JPMorgan", "Merrill"). Don't duplicate them; refer to them in notes.

**Verbs:** SEC complaint = alleged; settlement = agreed (usually "without admitting or denying"); examiner = concluded that a fact-finder could find; PSI staff = found; testimony = testified (only if the record shows an oath).

**Also:** `work/facts/reader-banks-gaps.md`. Final report as usual.
