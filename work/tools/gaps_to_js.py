#!/usr/bin/env python3
"""Turn build-log/gaps.md and sources/candidates/candidates.csv into js/gaps-data.js.

The "How This Was Built" page shows them under "What the sources couldn't tell us".
Only titles and descriptions of candidates are carried over, never file names or links.
Candidates the owner has approved (listed in sources/manifest.csv, downloaded, fingerprinted)
are marked approved; the page then shows them as library documents.

    window.GAPS = {
      intro: ["paragraph", ...],               # markdown text before the first ## heading
      sections: [{title, intro:[...], columns:[...], rows:[{col: text}]}],
      candidates: [{id, title, date, source_body, fills_gap, official_or_mirror,
                    approved, in_manifest, scout_sha256, library_sha256, same_fingerprint, fingerprint_note}]
    }
A candidate counts as approved when its id is listed in sources/manifest.csv and the owner's
download (sources/download_log.csv) recorded a fingerprint for it. same_fingerprint compares the
Source Scout's fingerprint (candidates.csv) with the owner's fresh official download.
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
CAND_BATCHES = [("phase1", ROOT / "sources" / "candidates" / "candidates.csv"),
                ("phase2", ROOT / "sources" / "candidates" / "phase2" / "candidates.csv")]

# Unapproved candidates are shown with a neutral description only (kind of document,
# publisher, date, gap), never their title: a title can state a fact the library
# does not yet support.
KINDS = [(r"interpretive release", "guidance release"), (r"final rule", "rule"), (r"\bGAO-\d", "report"),
         (r"U\.S\.C\.|U\.S\. Code", "section of the U.S. Code"), (r"U\.S\. Reports|\d+ U\.S\. \d+|opinion", "court opinion"),
         (r"press release", "press release"), (r"indictment", "court filing"), (r"agreement", "court filing"),
         (r"transcript", "transcript"), (r"auditing standard|\bAS \d{3,4}\b", "auditing standard"),
         (r"litigation release", "litigation release"), (r"hearing", "hearing record"), (r"report", "report")]


def neutral_description(r):
    kind = "document"
    for rx, k in KINDS:
        if re.search(rx, r.get("title", ""), re.I):
            kind = k
            break
    date = re.match(r"\s*(\d{4}(?:-\d{2}(?:-\d{2})?)?)", r.get("date", "") or "")
    body = (r.get("source_body") or "an official source").strip()
    art = "An" if kind[0] in "aeiou" else "A"
    return f"{art} {kind} from {body}" + (f", dated {date.group(1)}" if date else "")
MANIFEST = ROOT / "sources" / "manifest.csv"
DLOG = ROOT / "sources" / "download_log.csv"

# Explanations for fingerprint differences, checked by hand.
# sec-duncan-litrel-20441: the Scout's copy (git commit bc9edfb) and the owner's download differ
# in exactly one line (diff: line 1454), a <script> tag near the end of the page whose file path is
# randomly generated on each visit. The text of the release is identical.
FINGERPRINT_NOTES = {
    "sec-duncan-litrel-20441": "The two copies differ only in a randomly generated tracking script at the bottom of the web page; the text is identical.",
}
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


def read_csv(path, key="id"):
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as f:
        return {r[key]: r for r in csv.DictReader(f) if r.get(key)}


def parse_candidates():
    manifest, dlog = read_csv(MANIFEST), read_csv(DLOG)
    out = []
    for batch, path in CAND_BATCHES:
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if not r.get("id"):
                    continue
                c = {k: r.get(k, "") for k in ("id", "date", "source_body", "fills_gap", "official_or_mirror")}
                c["batch"] = batch
                m, d = manifest.get(c["id"]), dlog.get(c["id"], {})
                lib_sha = d.get("sha256", "")
                c["in_manifest"] = bool(m)
                c["approved"] = bool(m) and bool(lib_sha)
                # the title is carried only once the document is in the library (the manifest's title)
                c["title"] = (m.get("title") or r.get("title", "")) if c["approved"] else ""
                c["description"] = neutral_description(r)
                c["scout_sha256"] = r.get("sha256", "")
                c["library_sha256"] = lib_sha
                c["same_fingerprint"] = bool(lib_sha) and lib_sha == c["scout_sha256"]
                c["fingerprint_note"] = FINGERPRINT_NOTES.get(c["id"], "") if lib_sha and not c["same_fingerprint"] else ""
                out.append(c)
    return out


def main():
    intro, sections = parse_gaps(GAPS.read_text(encoding="utf-8")) if GAPS.exists() else ([], [])
    data = {"intro": intro, "sections": sections, "candidates": parse_candidates()}
    text = ("// Generated from build-log/gaps.md and sources/candidates/candidates.csv by work/tools/gaps_to_js.py. Do not edit.\n"
            f"window.GAPS = {json.dumps(data, indent=1, ensure_ascii=False)};\n")
    if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
        OUT.write_text(text, encoding="utf-8")
    n = sum(len(s["rows"]) for s in sections)
    ap = sum(c["approved"] for c in data["candidates"])
    same = sum(c["same_fingerprint"] for c in data["candidates"])
    print(f"wrote js/gaps-data.js: {len(sections)} sections, {n} rows, {len(data['candidates'])} candidates "
          f"({ap} approved, {same} with the same fingerprint as the Scout's copy)")


if __name__ == "__main__":
    main()
