# Brief: Image Researcher & Diagrammer (first pass)

**Role:** Find and download images for the site, and draw original diagrams. Follow `00-common-rules.md` and the IMAGES section of `CLAUDE.md`. **You may use the web, but only for images.**

**Allowed:** public domain or Creative Commons images from Wikimedia Commons, the Library of Congress, or U.S. government sites (for example the Congress, SEC, White House, or GPO sites). **Not allowed:** AP, Getty, or Reuters photos (check Commons file pages: some are mislabeled), screenshots from film or TV, or hot-linking. Use a photo of a real person only if the source clearly identifies who it is. Prefer images whose license is unambiguous.

**Wanted, one or more per chapter:**
1. Origins: Enron's Houston headquarters or the Houston skyline (Commons); the Enron logo, only if Commons marks it public domain (text logo, below the threshold of originality)
2. Business model: something like a natural-gas pipeline or a trading floor (public domain or CC)
3. SPEs: an **original diagram** (see below)
4. Warning signs: an **original diagram** or a relevant government image (for example a Senate hearing room)
5. Collapse: the stock price is best as an original chart, but only with data from the library, so skip it for now; instead a relevant public domain image (for example Enron's headquarters)
6. Andersen: an Arthur Andersen office or building photo if CC or public domain, or the Supreme Court building
7. Aftermath: President Bush signing Sarbanes-Oxley (White House photos are public domain), the U.S. Capitol, or the SEC building

**Original diagrams:** draw clean SVGs by hand (simple shapes and labels, readable in the site's light and dark themes, readable at phone and projector sizes, and using `currentColor` or CSS variables where practical):
- `images/diagram-spe-basic.svg`: how a special purpose entity moves money and assets off a company's balance sheet (generic concept; no specific numbers)
- `images/diagram-mark-to-market.svg`: mark-to-market vs. waiting for the cash (a generic 10-year contract example; clearly marked "illustration")
- `images/diagram-team.svg` will be made later by the Site Builder; skip it.
Diagrams that show specific Enron facts (the Raptors) wait for Wave 2, when the fact cards exist.

**Outputs:**
- Downloaded files in `images/` (reasonable size: resize to at most ~1600px wide; keep the original filename meaningful)
- `images/credits.json`: an array of `{"id", "file", "title", "description", "source_url", "author", "license", "license_url", "is_original_diagram", "person_identified_by_source": true|false|null, "suggested_chapter", "retrieved": "YYYY-MM-DD"}`
- `images/credits.js`: the same data as `window.IMAGE_CREDITS = [...]` (for the site; keep the two in sync)
- `work/facts/images-websites.md`: every website you visited and what you took from it
