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
        return [{k: r.get(k, "") for k in ("id", "title", "date", "source_body", "fills_gap", "official_or_mirror")}
                for r in csv.DictReader(f)]


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
