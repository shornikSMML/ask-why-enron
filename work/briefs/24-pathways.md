# Brief: Pathways Designer (Phase 2)

Follow `00-common-rules.md`. **No new facts:** bridges only connect stops, and any fact in a bridge must carry a card citation. Owner decisions: **seven pathways** (the owner chose to exceed the original 4–6), and one lens at a time.

**Pathways** (ids in brackets):
1. A First Reading [`first-reading`]: about 45 minutes.
2. Mark-to-Market Explained [`mark-to-market`].
3. The Special Purpose Entities [`spes`].
4. Andersen's Fall and the Big Five to Big Four [`andersen`].
5. From Enron to Sarbanes-Oxley and the PCAOB [`sox`]: its last stops will be on the new page `why-it-matters.html`. Use placeholder stop anchors (`why-it-matters.html#s302`, `#s404`, `#pcaob`, `#independence`, `#whistleblowers`); they'll be created later.
6. Reading the Footnotes [`footnotes`]: builds on the new cards and map coming from Reader A (`work/facts/footnotes-map.md`). **Draft its stops last.** If that file isn't ready yet, write the other pathways first and check again.
7. The Banks [`banks`]: stops on a new page `banks.html` (sections `#prepays`, `#deals`, `#institutions`, `#outcomes`), plus Cast, Timeline, and chapter stops. The page is being written later, so use those anchors.

**Each pathway:**
- `id`, `title`, `for_whom`, `minutes`, `intro` (2–3 sentences).
- `stops`: 5–10, each `{page, anchor, label, bridge}`. The bridge is 1–2 sentences on what to notice at the stop. `page` may include a lens to switch on, e.g. `chapters/ch3.html?lens=money`.
- A `closing_question`.
- A `handout`: a one-page printable summary (the stops as a numbered list plus 3 discussion questions).

Anchors must exist. Check chapter headings and ids in `chapters/*.html`, footnote annotation ids (`fn-NN`), Cast ids in `js/cast-data.js`, and timeline items. List every anchor you need that doesn't exist yet in `work/drafts/pathway-anchor-requests.md` for the Site Builder.

**Output:** `work/drafts/pathways.json`, `work/drafts/pathway-anchor-requests.md`. Final report as usual.
