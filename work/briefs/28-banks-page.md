# Brief: Story Writer, "The Banks" page (Phase 2)

Follow `00-common-rules.md` and your usual style. Use only checked cards (OK or FIXED): `work/facts/reader-banks.json` (K-cards; **read every `checker_note`**), plus the existing A, B, and C cards that mention the banks. Output: `work/drafts/banks.html`, a fragment in the same format as the chapters (`<h1>`, `<p class="dek">`, body, one `<aside class="ask-why">`), about 1,200–1,600 words, with at least two `<figure data-image>` placeholders (`diagram-prepay` will be drawn; you may also use `diagram-spe-basic`).

**Required section ids:**
- `<h2 id="prepays">`: how a prepay worked, and why it mattered that it looked like trading rather than a loan.
- `<h2 id="deals">`: Fishtail, Bacchus, Sundance, Slapshot, per the Senate staff.
- `<h2 id="institutions">`: what the documents say about each institution: Chase, Citigroup, Merrill Lynch, CIBC, RBS, CSFB, Toronto-Dominion.
- `<h2 id="outcomes">`: how the regulators' cases ended **as the library shows**, and plainly what it doesn't show.

**Fact-Checker rulings to follow exactly:**
- **Merrill Lynch and CIBC.** Never say either pleaded guilty or was convicted. Safer to omit the Fifth Circuit's "plea agreements" phrase; if used, quote it only as the court's term.
- **Merrill's promised return.** Give the SEC's 22.5% and the Senate staff's 15% separately, each with its source. Don't merge them.
- **Citigroup's prepay total.** About $4.7–4.8 billion, or cite each figure separately.
- **Mahonia.** Present every position with attribution. The library doesn't settle who controlled it.
- **Furst and Tilney.** They invoked the Fifth Amendment. Say that invoking it is not evidence of guilt.
- **K-048.** Say "one Merrill Lynch employee's notes"; attribute them to no one.
- **Settlements.** Use "agreed … without admitting or denying" where the source says so.
- **Examiner.** Keep his "a fact-finder could conclude" standard. Always name the Batson report and appendix letter.

Tag paragraphs with `data-lens` (`money`, `auditors`, `board`, `knew`) where apt, and wrap first uses of terms in `span.term` (list any new term ids in `work/drafts/banks-terms.md` with plain definitions). Build the citations with your `expand.py`, extended to accept K-cards. Keep the source in `work/drafts/story-src/banks.src.html`. Run `integrate.py --no-log` and the tests. Report briefly.
