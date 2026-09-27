# Brief: Lens Writer (Phase 2)

Follow `00-common-rules.md`. **No new sources.** Use only fact cards checked OK or FIXED (`work/facts/*.json`: the A, B, C, F, G series) and the chapter drafts `work/drafts/ch1.html`–`ch7.html`.

**Four lenses:** `money` (Follow the Money), `auditors` (The Auditors), `board` (The Board), `knew` (Who Knew What, When). One lens is shown at a time.

**For each chapter and each lens:**
1. **Lens notes:** for every paragraph tagged with that lens (`data-lens` on the `<p>`; give each paragraph a stable key, e.g. the chapter number plus the paragraph index within the chapter body counted among `<p>` elements, **and** the first 8 words of the paragraph so the site can match it), write a 1–3 sentence note reading the paragraph through the lens, with a citation to a card. Notes point out what matters for that lens. They make **no new accusations** and use the cards' verbs. Not every tagged paragraph needs a note; about 60% is fine. Skip where there's nothing useful to say.
2. **Lens summary:** 3–4 bullet points, plus one lens-specific "Ask Why" question for the chapter (an open question for discussion).
3. **"Who Knew What, When" only:** a dated strip per chapter of 3–8 entries: {date, person or body, what the documents show they knew or were told, cite}. Only where a card documents it, and phrased carefully ("was told", "received", "testified that he did not recall").

**Output:** `work/drafts/lenses.json`: `{ "ch1": { "money": {"notes": [{"para_index", "para_start", "text", "cites": [{"card", "source_id", "page", "loc"}]}], "summary": [...], "ask_why": "..."}, "auditors": {...}, "board": {...}, "knew": {..., "strip": [...]}}, ... }`. Also `work/drafts/lens-requests.md` for facts without cards. Final report as usual.
