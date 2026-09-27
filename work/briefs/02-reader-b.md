# Brief: Reader B: The People & the Law

**Role:** You produce fact cards (see `00-common-rules.md`) about the **people**: each person's role at Enron or elsewhere, and **precisely what happened to them legally, as far as the library documents it**. These feed the Cast of Characters, Chapter 4 (warning signs and the whistleblower), Chapter 7 (aftermath: trials and outcomes), and the Timeline. You write no prose for the site.

**People to cover (at least):** Kenneth Lay, Jeffrey Skilling, Andrew Fastow, Michael Kopper, Richard Causey, Ben Glisan Jr., Sherron Watkins, David Duncan (Andersen), Joseph Berardino (Andersen CEO, testimony), William Powers Jr. (Powers Committee), Neal Batson (examiner), key outside directors named in the PSI report (e.g. Robert Jaedicke, audit committee chair) and whether they were charged. Also the Merrill Lynch executives, only as the SEC complaint names them. Add others who appear prominently in the documents.

**For each person, make cards for:** title and role with dates; what the SEC alleged; what the DOJ charged; any plea, verdict, or sentence **that a library document states**; appeals; and, where true, "not charged," which you may only state if a document says it. Otherwise say the library doesn't show charges.

**Documents (manifest ids) and roughly which sections:**
- SEC complaints (the summary and the "defendants" paragraphs, plus a few key allegation paragraphs): `sec-fastow-complaint`, `sec-kopper-complaint`, `sec-skilling-causey-complaint`, `sec-lay-complaint`, `sec-glisan-complaint`, `sec-merrill-complaint`, `sec-duncan-complaint`
- `sec-jpm-citi-press`; `sec-enron-spotlight` (the index of actions; outcomes it lists, e.g. pleas, judgments)
- `doj-skilling-indictment` (the introduction and a summary of the counts), `doj-skilling-charged-press`, `doj-lay-charged-press`
- `ca5-skilling-2009`: background and procedural history (the 2006 trial, which counts Skilling was convicted on, the sentence, anything about Lay's death and vacatur, Fastow's plea if mentioned)
- `skilling-scotus-2010`: the Syllabus and holding (honest-services fraud)
- `batson-final-app-d`: the conclusions on Lay, Skilling, and the outside directors (use the table of contents; OCR text in `work/text/batson-final-app-d.txt` when ready)
- `rpt-psi-board`: findings. `hrg-psi-board`: directors' testimony, selectively.
- `hrg-commerce-skilling-watkins`: Watkins's testimony (her August 2001 letter to Lay, what she said to him) and Skilling's testimony. `hrg-commerce-lay-powers`: Lay invoking his Fifth Amendment right; Powers's testimony.

**Outputs:** `work/facts/reader-b.json` (ids B-001 ...), `work/facts/reader-b-readlog.md`, `work/facts/reader-b-gaps.md`. Also write `work/facts/people-outcomes.md`: a one-row-per-person table (Person | Role | SEC | Criminal | Final outcome as documented | Card ids | What's missing). The Fact-Checker and the Reference Writer will use it.
