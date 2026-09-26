#!/usr/bin/env python3
"""Turn build-log/gaps.md and sources/candidates/candidates.csv into js/gaps-data.js.

The "How This Was Built" page shows them under "What the sources couldn't tell us".
Only titles and descriptions of candidates are carried over: no file names and no
links, because candidates are not part of the library and must not be used.

    window.GAPS = {
      intro: ["paragraph", ...],               # markdown text before the first ## heading
      sections: [{title, intro:[...], columns:[...], rows:[{col: text}]}],
      candidates: [{id, title, date, source_body, fills_gap, official_or_mirror}]
    }
Cell text keeps light markdown (**bold**, *italic*, `code`); the page renders it safely.
Run: python3 work/tools/gaps_to_js.py   (integrate.py runs it)
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GAPS = ROOT / "build-log" / "gaps.md"
CANDS = ROOT / "sources" / "candidates" / "candidates.csv"
OUT = ROOT / "js" / "gaps-data.js"


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)]


def parse_gaps(text):
    intro, sections, cur = [], [], None
    lines = text.splitlines()
    i = 0
    para = []

    def flush():
        if para:
            (cur["intro"] if cur else intro).append(" ".join(para).strip())
            para.clear()

    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            i += 1
            continue
        if line.startswith("## "):
            flush()
            cur = {"title": line[3:].strip(), "intro": [], "columns": [], "rows": []}
            sections.append(cur)
            i += 1
            continue
        if line.strip().startswith("|"):
            flush()
            cols = split_row(line)
            i += 1
            if i < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i]):
                i += 1
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = split_row(lines[i])
                rows.append({c: (cells[k] if k < len(cells) else "") for k, c in enumerate(cols)})
                i += 1
            if cur is None:
                cur = {"title": "", "intro": [], "columns": [], "rows": []}
                sections.append(cur)
            cur["columns"], cur["rows"] = cols, cur["rows"] + rows
            continue
        if line.strip():
            para.append(line.strip())
        else:
            flush()
        i += 1
    flush()
    return intro, sections


def parse_candidates():
    if not CANDS.exists():
        return []
    with CANDS.open(newline="", encoding="utf-8") as f:
        rows = [{k: r.get(k, "") for k in ("id", "date", "source_body", "fills_gap", "official_or_mirror")}
                for r in csv.DictReader(f)]
    # Candidate titles can state facts the library does not yet support (e.g. an outcome).
    # Until the owner approves a candidate, the site shows only a neutral description.
    for r in rows:
        r["title"] = NEUTRAL_TITLES.get(r["id"], "Candidate document (description withheld until approved)")
    return rows


NEUTRAL_TITLES = {
    "doj-fastow-plea-press-2004": "Justice Department press release about Andrew Fastow's criminal case (2004)",
    "doj-fastow-sentenced-press-2006": "Justice Department press release about Andrew Fastow's criminal case (2006)",
    "doj-glisan-plea-press-2003": "Justice Department press release about Ben Glisan's criminal case (2003)",
    "sec-duncan-litrel-20441": "SEC litigation release about its civil case against David Duncan",
    "ca5-skilling-2011-remand": "Fifth Circuit opinion in Skilling's case after the 2010 Supreme Court decision",
    "doj-skilling-sentencing-agreement-2013": "Court filing in Skilling's case (2013)",
    "doj-andersen-indictment-2002": "Indictment of Arthur Andersen LLP (2002)",
    "andersen-scotus-full-usreports": "Full Supreme Court opinion in Arthur Andersen LLP v. United States (2005)",
    "doj-dag-kopper-plea-transcript-2002": "Justice Department news conference transcript about Michael Kopper (2002)",
    "doj-causey-sentenced-press-2006": "Justice Department press release about Richard Causey's criminal case (2006)",
}


def main():
    intro, sections = parse_gaps(GAPS.read_text(encoding="utf-8")) if GAPS.exists() else ([], [])
    data = {"intro": intro, "sections": sections, "candidates": parse_candidates()}
    text = ("// Generated from build-log/gaps.md and sources/candidates/candidates.csv by work/tools/gaps_to_js.py. Do not edit.\n"
            f"window.GAPS = {json.dumps(data, indent=1, ensure_ascii=False)};\n")
    if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
        OUT.write_text(text, encoding="utf-8")
    n = sum(len(s["rows"]) for s in sections)
    print(f"wrote js/gaps-data.js: {len(sections)} sections, {n} rows, {len(data['candidates'])} candidates")


if __name__ == "__main__":
    main()
