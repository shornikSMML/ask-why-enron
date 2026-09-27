# Common rules for every agent (read this first)

You are one agent on a team building "Ask Why: The Rise and Fall of Enron", a static website for undergraduates from any major. A **coordinator** assigns the work. You never talk to other agents. You get work through your brief, and you hand work back as files plus a short final report to the coordinator.

Repository root: `/home/user/enron-dryrun`. Read `CLAUDE.md` and `sources/README.md` (especially "Rules for the agents") before you start. They bind you.

## Sources
- Use only documents listed in `sources/manifest.csv`, and refer to them by their **manifest id** (the first column, e.g. `powers-report-sec`).
- **Never edit anything in `sources/`.**
- **Fingerprints:** before relying on a file, compute its SHA-256 (`sha256sum <file>`) and compare it with the `sha256` column of `sources/download_log.csv`. If they don't match, stop and report it to the coordinator. The coordinator checked all 74 files at Step 0 and they matched. Re-check the files you use anyway, and list them in your read log.
- **Searchable text copies** are in `work/text/<manifest id>.txt`. PDFs are split with `=== PAGE n ===` markers, where **n is the PDF page number** (the page a PDF viewer shows, and the number used in `#page=n` links). The page number printed on the document may be different. Record both when you can.
- `.txt` sources (the SEC filings, `powers-report-sec`) are read directly from `sources/`.
- **Scanned documents:** the Batson reports and the Joint Committee on Taxation report (`rpt-jct-vol1`) are scans. Their text is being produced by OCR (automatic text recognition) in the background. Check `work/ocr.log` to see which ones are finished. OCR makes mistakes, so **any quote you take from an OCR text must be checked against the page image.** Open the PDF with the Read tool using the `pages` parameter (for example `pages: "34"`). If an OCR text isn't ready yet, read the PDF pages directly with the Read tool, a few pages at a time.
- **Read efficiently.** Search the text copies (grep) to find sections, then read only what you need. Record every page range you read.
- **No web** unless your brief explicitly says so. **Never** use a copy of a document found online in place of the library copy.
- **Known gaps:** the Batson Second and Third Interim Reports are not in the library. Don't look for them. `andersen-scotus` contains only the Syllabus of the opinion; cite it as "Syllabus."
- **If you need a source the library doesn't have, don't search for it.** Write the gap to your own gaps file (named in your brief) with four things: the claim you wanted to make, what kind of document would support it, how important it is (critical, useful, or minor), and your agent name. Then leave the claim out and keep working.

## Accuracy rules (highest priority)
- Every fact about specific events, dates, dollar amounts, or people must come from the library. General explanations of concepts (what mark-to-market accounting is) may use general knowledge.
- **Use the right verb for the kind of source:**

  | Kind of source | Verb |
  |---|---|
  | SEC complaint or indictment | *alleged* / *charged* |
  | Guilty plea, jury verdict, or court judgment | *pleaded guilty* / *was convicted* / *the court held* |
  | Hearing testimony | *testified* / *told the committee under oath* |
  | Powers Report | *the board's special committee found* |
  | Batson | *the bankruptcy examiner concluded* |
  | Congressional staff report | *the Senate subcommittee staff found* |
  | Company filing | *Enron reported / disclosed / stated* |

- **Check how each case ended before calling anyone guilty.** Andersen's conviction was reversed (2005). Lay was convicted in 2006, died before his appeal, and his conviction was vacated. Skilling's convictions were narrowed by the Supreme Court in 2010. Many people named in hearings were never charged. You may state these outcomes only from library documents. If no library document covers an outcome, say so and log a gap.
- **Quotations:** verbatim only, short (a sentence or less where possible), from a cited library document. Never invent or paraphrase inside quotation marks. Don't quote copyrighted books, articles, or films.
- When sources disagree or are uncertain, say so explicitly.

## Fact cards (format used by the Readers and the Footnote Annotator)
A JSON array. One object per fact:
```json
{
  "id": "A-001",
  "topic": "short topic label, e.g. 'Chewco' or 'Fastow: outcome'",
  "claim": "The fact in one or two plain sentences.",
  "quote": "Short verbatim supporting text from the source (<= 50 words).",
  "source_id": "powers-report-sec",
  "file": "sources/01-internal-investigation/powers-report-sec-exhibit-99-2.txt",
  "locator": {"pdf_page": null, "printed_page": "p. 4", "section": "Executive Summary", "lines": "1200-1210"},
  "source_type": "board committee finding | SEC allegation | indictment allegation | sworn testimony | court holding | court's description of procedural history | company filing | statute | GAO report | congressional staff report | government press release | examiner conclusion",
  "verb": "found | alleged | testified | held | reported | stated | pleaded guilty | was convicted",
  "people": ["Andrew Fastow"],
  "event_date": "YYYY-MM-DD or YYYY-MM or YYYY or null",
  "from_ocr": false,
  "ocr_checked_against_image": false,
  "notes": "Uncertainties, disagreements between sources, anything the writer must know."
}
```

## Site markup conventions (used by writers and the Site Builder)
- Citation: `<a class="cite" data-src="MANIFEST_ID" data-page="PDF_PAGE_OR_EMPTY" data-loc="human-readable locator, e.g. 'p. 4, Executive Summary'" data-card="A-001">source</a>`. The site turns these into numbered notes: in the margin on wide screens, tap-to-open on phones. Each note links to the file in `sources/`, at `#page=N` for PDFs.
- Glossary term, first use: `<span class="term" data-term="mark-to-market">mark-to-market accounting</span>`. The `data-term` value is a glossary id.
- Phase 2 lens tags (writers add them now): `data-lens="money auditors board knew"` on any paragraph relevant to those lenses. The lenses are: Follow the Money (`money`); The Auditors (`auditors`); The Board (`board`); Who Knew What, When (`knew`).
- The closing question: `<aside class="ask-why"><h2>Ask Why</h2><p>...</p></aside>`.
- Figure: `<figure data-image="IMAGE_ID"></figure>`. The Site Builder fills in the image and credit from `images/credits.js`.

## Your final report to the coordinator
When you finish, reply with:
1. the files you produced;
2. every document you read, with page or line ranges, and whether its fingerprint matched;
3. anything uncertain, any disagreements between sources, and the gaps you logged;
4. any websites you used (only if your brief allowed the web).

Keep it concise.
