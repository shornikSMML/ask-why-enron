# Site notes: how to hand content to the site

From the Site Builder. The site is plain HTML/CSS/JS with no build step, and it must open straight from disk (file://). Browsers block `fetch()` of local files there, so **all data reaches the site as `.js` files that set a `window.` variable**. Don't hand over bare `.json` for the site to read. Either write the `.js` file yourself, or give JSON and the coordinator runs:

```
python3 work/tools/wrap_json.py <file.json> <VARIABLE> <js/file.js>
```

Every string is inserted as **plain text** (HTML-escaped), except the chapter fragments, which are HTML.

## What goes where

| Content | Owner | File the site loads | Variable |
|---|---|---|---|
| Chapters 1–7 | Story Writer | `chapters/chN.html` (fragment spliced in) | n/a |
| Cast of Characters | Reference Writer | `js/cast-data.js` | `window.CAST` |
| Timeline | Reference Writer | `js/timeline-data.js` | `window.TIMELINE` |
| Glossary | Reference Writer | `js/glossary-data.js` | `window.GLOSSARY` |
| The Footnote | Footnote Annotator | `js/footnote-data.js` (from `work/drafts/footnote.json`) | `window.FOOTNOTE` |
| Image credits | Image Researcher | `images/credits.js` | `window.IMAGE_CREDITS` |
| Build log | Scribe | `build-log/log.js` | `window.BUILD_LOG` |
| Source list | generated | `js/sources-data.js` (run `python3 work/tools/make_sources_js.py`) | `window.SOURCES` |

The current `cast-data.js`, `timeline-data.js` and `footnote-data.js` hold **SAMPLE** data, marked on screen as "Sample data". Replace the whole file. Remove the `window.CAST_SAMPLE` / `window.TIMELINE_SAMPLE` lines and the `"sample": true` field so the label disappears.

## Chapters (Story Writer)

Each `chapters/chN.html` contains:

```html
<!-- CONTENT START: ... -->
   ...placeholder...
<!-- CONTENT END -->
```

The fragment `work/drafts/chN.html` replaces everything between these two comments. The comments stay. The fragment starts with `<h1>`, then an optional `<p class="dek">`, then the body. Don't include `<html>`, `<head>`, the header, the chapter nav, or the margin column. The page supplies those.

Markup inside a fragment (from `00-common-rules.md`):

- **Citation:** `<a class="cite" data-src="MANIFEST_ID" data-page="PDF_PAGE_OR_EMPTY" data-loc="p. 4, Executive Summary" data-card="A-001">source</a>`, placed right after the words it supports with no space before it. The site numbers these, builds the margin notes (wide screens), tap-to-open notes (phones), and the "Sources for this page" endnotes (print). `data-src` must be a manifest id. An unknown id shows "[Unknown source id]" and logs a console warning. `data-page` is the **PDF page** and is used only for PDFs (`#page=N`). Leave it empty for .txt/.htm sources and put the location in `data-loc`.
- **Glossary term (first use):** `<span class="term" data-term="mark-to-market">mark-to-market accounting</span>`. Use the same id as the glossary key.
- **Lens tags:** `data-lens="money auditors board knew"` on `<p>` (any subset). No styling yet. `applyLens(name)` exists as a stub.
- **Figure:** `<figure data-image="IMAGE_ID"></figure>`. The site inserts the image and the credit line from `images/credits.js`. You may add your own `<figcaption>` inside, and the credit is appended to it. For alt text specific to that spot, add `data-alt="..."`. If the id isn't in the credits file, a dashed "[Image coming: ID]" box shows.
- **Closing question:** `<aside class="ask-why"><h2>Ask Why</h2><p>…</p></aside>`.

## `window.CAST` (Reference Writer)

```js
window.CAST = [
  { "id": "person-id",                       // used as the anchor: cast.html#person-id
    "name": "Full Name",
    "role": "Role, with dates",
    "summary": "2–4 neutral sentences.",
    "outcome_status": "pleaded guilty",       // see list below
    "outcome_text": "Exactly what happened, with the right verbs.",
    "cites": [ { "source_id": "manifest-id", "page": 12, "loc": "p. 12, ¶ 3", "card": "B-014" } ],
    "image": "IMAGE_ID"                       // optional; id from images/credits.js
  }
];
```

`outcome_status` is shown as a label. Every label has the same neutral style: no red for convicted, no green for anyone else. The site knows these values exactly, as worded in brief 10: `convicted`, `convicted — later narrowed on appeal`, `conviction vacated (died before appeal)`, `conviction reversed`, `pleaded guilty`, `SEC settlement`, `charged — outcome not in library`, `not charged (per source)`, `no charges shown in library`, `not accused of wrongdoing`. Any other value is shown as written, with a console warning. Cites use `page` (or `pdf_page`) for the PDF page. The citations appear as numbered notes after `outcome_text`.

## `window.TIMELINE` (Reference Writer)

```js
window.TIMELINE = [
  { "date": "2001-10-16",        // "YYYY", "YYYY-MM" or "YYYY-MM-DD"; sorted automatically
    "title": "Short title",
    "text": "1–2 sentences.",
    "cites": [ { "source_id": "…", "page": null, "loc": "…", "card": "A-020" } ],
    "tags": ["company", "accounting"],   // from: company, accounting, spe, people, markets, auditors, legal, government, reform
    "epilogue": false }                  // true for the 2010 Skilling item
];
```

Filter buttons are built from the tags actually used. Year jump links are built from the dates.

## `window.GLOSSARY` (Reference Writer)

```js
window.GLOSSARY = {
  "mark-to-market": { "term": "Mark-to-market accounting",
                      "short": "≤ 25 words; shown in the pop-up.",
                      "long": "2–4 sentences with one everyday example; glossary page only.",
                      "see_also": ["restatement"],
                      "cites": [] }      // optional, same cite format as above
};
```

The key is the `data-term` id, and it's also the anchor: `glossary.html#mark-to-market`.

## `window.FOOTNOTE` (Footnote Annotator)

Exactly the `work/drafts/footnote.json` structure in brief 04: `{title, source, paragraphs:[{n, text, annotations:[{id, phrase, said, left_out, found, cites:[{source_id, pdf_page, loc, quote}], glossary_terms:[…]}]}]}`. Optional extras: `intro` (a lede under the title), and `source` may contain `source_id` and `loc` for the "Source:" line (the 10-K's manifest id is `enron-10k-2000`). Each `phrase` must be an **exact substring** of its paragraph. A phrase that isn't found, or that overlaps an earlier phrase in the same paragraph, is skipped with a console warning, so check the browser console after loading. Annotations are numbered in reading order.

## `window.IMAGE_CREDITS` (Image Researcher)

The array from brief 05. The site uses `id`, `file` (e.g. `"diagram-spe-basic.svg"` or `"images/diagram-spe-basic.svg"`; both work), `title` (default caption), `description` (default alt text; add an `alt` field to override), `author`, `license`, `license_url`, `source_url`, and `is_original_diagram` (credit reads "Original diagram for this site"). The chapter skeletons already reference `diagram-mark-to-market` (ch2) and `diagram-spe-basic` (ch3). Keep those ids if possible. Until `images/credits.js` exists, each page logs one "file not found" console message for it. That is expected.

## Build log (Scribe)

`how-built.html` reads `window.BUILD_LOG` in the shape `build_log.py` already writes: `before_the_agents` (summary, fingerprint_explained, fingerprint_check, lessons), `coordinator.decisions`, `agents[].runs/handoffs/reviews/brief`, `common_rules`, `briefs_not_yet_assigned` (shown as dashed "planned" boxes in the team diagram), `timeline`, `corrections`, `web_sources`. `corrections` and `web_sources` are shown as tables with whatever keys the rows have.

## Other tools

- `work/tools/test_site.py`: Playwright smoke test (file://, at 1440×900, 1920×1080, 390×844 and 360 px; light and dark). It checks for console errors and horizontal scrolling and saves screenshots to `work/screens/`. Run: `PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 work/tools/test_site.py`.
- Add `?cards` to any page URL (e.g. `chapters/ch3.html?cards`) to show fact-card ids next to each note. This is for the fact-checker.
