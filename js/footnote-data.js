/* SAMPLE ONLY — layout test data for footnote.html. Not real content.
   The Footnote Annotator's work/drafts/footnote.json replaces this file
   (as window.FOOTNOTE = {...}; see work/drafts/site-notes.md). */
window.FOOTNOTE = {
  "sample": true,
  "title": "The Footnote [SAMPLE]",
  "intro": "[Draft text coming] This page will show the related-party footnote in full, with plain-language annotations.",
  "source": { "source_id": "enron-10k-2000", "loc": "[SAMPLE locator]" },
  "paragraphs": [
    {
      "n": 1,
      "text": "SAMPLE PARAGRAPH. This placeholder sentence stands in for the footnote text. A second placeholder phrase shows how annotations stack, and a third placeholder phrase shows stepping with the keyboard.",
      "annotations": [
        { "id": "fn-s1", "phrase": "This placeholder sentence stands in for the footnote text",
          "said": "[SAMPLE] What the phrase said, in plain English.",
          "left_out": "[SAMPLE] What a reader could not learn from it.",
          "found": "[SAMPLE] What the investigations later found, with the right verb.",
          "cites": [ { "source_id": "powers-report-sec", "pdf_page": null, "loc": "[SAMPLE locator]", "quote": "[SAMPLE quote]" } ],
          "glossary_terms": ["related-party-transaction"] },
        { "id": "fn-s2", "phrase": "second placeholder phrase",
          "said": "[SAMPLE]", "left_out": "[SAMPLE]", "found": "[SAMPLE]",
          "cites": [ { "source_id": "powers-report", "pdf_page": 1, "loc": "[SAMPLE locator]" } ],
          "glossary_terms": [] },
        { "id": "fn-s3", "phrase": "third placeholder phrase",
          "said": "[SAMPLE]", "left_out": "[SAMPLE]", "found": "[SAMPLE]",
          "cites": [], "glossary_terms": [] }
      ]
    }
  ]
};
