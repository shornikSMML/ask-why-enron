#!/usr/bin/env python3
"""Put the writers' content into the site. Safe to re-run after every fix.

What it does (nothing else is touched; content wording is never changed):
  1. Splices work/drafts/chN.html (N = 1..7) into chapters/chN.html, between
         <!-- CONTENT START ... -->   and   <!-- CONTENT END -->
     and copies the draft's <p class="dek"> into the page's <meta name="description">.
  2. Copies each chapter's dek into the home page card (index.html, <p data-dek="N">).
  3. Wraps work/drafts/footnote.json as js/footnote-data.js (window.FOOTNOTE),
     using the same approach as work/tools/wrap_json.py.
  3b. Phase 2: wraps work/drafts/lenses.json as js/lenses-data.js (window.LENSES) and
     work/drafts/pathways.json as js/pathways-data.js (window.PATHWAYS). Until those
     drafts exist it writes clearly marked SAMPLE data instead (window.LENSES_SAMPLE /
     window.PATHWAYS_SAMPLE), built from the chapters so every lens and stop is testable.
     Splices work/drafts/why-it-matters.html and work/drafts/banks.html into the page
     shells when they exist (same CONTENT START / END markers as the chapters).
  4. Writes js/image-usage-data.js (window.IMAGE_USAGE: which pages show each image),
     used by credits.html.
  5. Regenerates js/sources-data.js (make_sources_js.py), js/gaps-data.js
     (gaps_to_js.py) and, unless --no-log, the build log (build_log.py).
  6. Prints a static check: unknown source ids, glossary ids, image ids,
     footnote phrases that are not exact substrings. The browser test
     (work/tools/test_site.py) repeats these checks on the rendered pages.

Run from anywhere:  python3 work/tools/integrate.py [--no-log]
Exit code 1 if a draft is missing or a check fails.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DRAFTS = ROOT / "work" / "drafts"
TOOLS = ROOT / "work" / "tools"
START_RE = re.compile(r"(<!-- CONTENT START[^>]*-->\n?)(.*?)(\s*<!-- CONTENT END -->)", re.S)
DEK_RE = re.compile(r'<p class="dek"[^>]*>(.*?)</p>', re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)

problems = []


def read(p):
    return Path(p).read_text(encoding="utf-8")


def write_if_changed(p, text):
    p = Path(p)
    if p.exists() and p.read_text(encoding="utf-8") == text:
        print(f"  unchanged {p.relative_to(ROOT)}")
        return
    p.write_text(text, encoding="utf-8")
    print(f"  wrote     {p.relative_to(ROOT)}")


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def load_js_var(path, var):
    """Read `window.VAR = <json>;` from a generated/data .js file."""
    text = read(path)
    m = re.search(r"window\." + var + r"\s*=\s*", text)
    if not m:
        return None
    dec = json.JSONDecoder()
    try:
        val, _ = dec.raw_decode(text[m.end():])
        return val
    except json.JSONDecodeError as e:
        problems.append(f"{path}: could not parse window.{var} as JSON ({e})")
        return None


# ---------- 1 + 2: chapters and home-page deks ----------
def splice_chapters():
    print("Chapters")
    deks = {}
    for n in range(1, 8):
        draft_p, page_p = DRAFTS / f"ch{n}.html", ROOT / "chapters" / f"ch{n}.html"
        if not draft_p.exists():
            problems.append(f"missing draft {draft_p.relative_to(ROOT)}")
            continue
        frag = read(draft_p).strip("\n")
        page = read(page_p)
        m = START_RE.search(page)
        if not m:
            problems.append(f"{page_p.relative_to(ROOT)}: CONTENT START/END markers not found")
            continue
        indent = "    "
        body = "\n".join((indent + line) if line.strip() else "" for line in frag.split("\n"))
        page = page[:m.start()] + m.group(1) + body + "\n" + indent + "<!-- CONTENT END -->" + page[m.end():]
        dek_m, h1_m = DEK_RE.search(frag), H1_RE.search(frag)
        dek = strip_tags(dek_m.group(1)) if dek_m else ""
        deks[n] = dek
        if dek:
            page = re.sub(r'<meta name="description" content="[^"]*">',
                          '<meta name="description" content="' + html.escape(dek, quote=True) + '">', page, count=1)
        else:
            problems.append(f"{draft_p.relative_to(ROOT)}: no <p class=\"dek\">")
        if h1_m:
            title = strip_tags(h1_m.group(1))
            page = re.sub(r"<title>[^<]*</title>", f"<title>Chapter {n}: {html.escape(title, quote=False)} · Ask Why</title>", page, count=1)
        write_if_changed(page_p, page)
    return deks


def fill_home(deks):
    print("Home page")
    p = ROOT / "index.html"
    page = read(p)
    for n, dek in deks.items():
        page, k = re.subn(r'(<p[^>]*data-dek="' + str(n) + r'"[^>]*>).*?(</p>)',
                          lambda m: m.group(1) + html.escape(dek, quote=False) + m.group(2), page, count=1, flags=re.S)
        if not k:
            problems.append(f'index.html: no <p data-dek="{n}"> placeholder')
    write_if_changed(p, page)


# ---------- 3: footnote ----------
def wrap_footnote():
    print("Footnote")
    src = DRAFTS / "footnote.json"
    data = json.loads(read(src))  # fails loudly on malformed JSON
    out = ROOT / "js" / "footnote-data.js"
    write_if_changed(out, "// Generated from work/drafts/footnote.json by work/tools/integrate.py. Edit the JSON, then re-run.\n"
                     f"window.FOOTNOTE = {json.dumps(data, indent=1, ensure_ascii=False)};\n")
    return data


# ---------- 3b: Phase 2 (lenses, pathways, new pages) ----------
P_RE = re.compile(r"<p[\s>][^>]*>|<p>", re.S)
PARA_RE = re.compile(r"<p(?:\s[^>]*)?>(.*?)</p>", re.S)
LENS_IDS = ["money", "auditors", "board", "knew"]


def draft_paragraphs(n):
    """<p> elements of work/drafts/chN.html in order (the dek counts; 0-based index)."""
    frag = read(DRAFTS / f"ch{n}.html")
    out = []
    for m in re.finditer(r"<p((?:\s[^>]*)?)>(.*?)</p>", frag, re.S):
        attrs, inner = m.group(1), m.group(2)
        lens = re.search(r'data-lens="([^"]*)"', attrs)
        text = strip_tags(re.sub(r'<a class="cite".*?</a>', "", inner, flags=re.S))
        out.append({"lens": (lens.group(1).split() if lens else []), "text": text})
    return out


def sample_lenses():
    data = {}
    for n in range(1, 8):
        paras = draft_paragraphs(n)
        ch = {}
        for lens in LENS_IDS:
            tagged = [(i, p) for i, p in enumerate(paras) if lens in p["lens"]]
            notes = [{"para_index": i, "para_start": " ".join(p["text"].split()[:8]),
                      "text": f"[Sample note] Layout test text for the {lens} lens on this paragraph. The real note is being written.",
                      "cites": [{"card": "SAMPLE", "source_id": "powers-report-sec", "page": None, "loc": "[sample locator]"}]}
                     for k, (i, p) in enumerate(tagged) if k % 2 == 0]
            entry = {"notes": notes,
                     "summary": ["[Sample] First summary point for this lens.", "[Sample] Second summary point.", "[Sample] Third summary point."],
                     "ask_why": "[Sample] An open discussion question for this lens will appear here."}
            if lens == "knew":
                entry["strip"] = [{"date": "[date]", "who": "[Sample] person or body", "what": "[Sample] what the documents show they knew or were told.",
                                   "cites": [{"card": "SAMPLE", "source_id": "powers-report-sec", "page": None, "loc": "[sample locator]"}]}] * 3
            ch[lens] = entry
        data[f"ch{n}"] = ch
    return data


SAMPLE_PATHWAYS = [
    ("first-reading", "A First Reading", 45, [("chapters/ch1.html", "", "Chapter 1: Origins"), ("chapters/ch2.html", "what-mark-to-market-accounting-means", "Chapter 2: mark-to-market"),
                                               ("chapters/ch3.html?lens=money", "the-raptors", "Chapter 3: the Raptors, with the money lens"), ("cast.html", "sherron-watkins", "Cast: Sherron Watkins"),
                                               ("timeline.html", "tl-2001-12-02", "Timeline: December 2, 2001"), ("footnote.html", "fn-05", "The Footnote, annotation 5"), ("chapters/ch7.html", "", "Chapter 7")]),
    ("mark-to-market", "Mark-to-Market Explained", 25, [("glossary.html", "mark-to-market", "Glossary: mark-to-market"), ("chapters/ch2.html", "what-mark-to-market-accounting-means", "Chapter 2"),
                                                       ("chapters/ch2.html?lens=money", "marking-investments-to-market", "Chapter 2, money lens")]),
    ("spes", "The Special Purpose Entities", 35, [("chapters/ch3.html", "chewco", "Chewco"), ("chapters/ch3.html?lens=board", "the-ljm-partnerships", "LJM, board lens"),
                                                  ("cast.html", "andrew-fastow", "Cast: Andrew Fastow"), ("footnote.html", "fn-10", "The Footnote")]),
    ("andersen", "Andersen's Fall and the Big Five to Big Four", 30, [("chapters/ch6.html?lens=auditors", "enrons-auditor", "Chapter 6, auditors lens"), ("cast.html", "david-duncan", "Cast: David Duncan"),
                                                                      ("timeline.html", "tl-2005-05-31", "Timeline: 2005"), ("chapters/ch6.html", "the-big-four", "The Big Four")]),
    ("sox", "From Enron to Sarbanes-Oxley and the PCAOB", 30, [("chapters/ch7.html", "", "Chapter 7"), ("timeline.html", "tl-2002-07-30", "Timeline: July 30, 2002"),
                                                               ("why-it-matters.html", "s302", "Section 302"), ("why-it-matters.html", "s404", "Section 404"), ("why-it-matters.html", "pcaob", "The PCAOB"),
                                                               ("why-it-matters.html", "independence", "Auditor independence"), ("why-it-matters.html", "whistleblowers", "Whistleblowers")]),
    ("footnotes", "Reading the Footnotes", 30, [("footnote.html", "fn-01", "The Footnote"), ("footnote.html", "fn-20", "Annotation 20"), ("glossary.html", "related-party-transaction", "Glossary")]),
    ("banks", "The Banks", 30, [("banks.html", "prepays", "Prepays"), ("banks.html", "deals", "The deals"), ("cast.html", "jpmorgan-citigroup", "Cast: JPMorgan and Citigroup"),
                                ("banks.html", "institutions", "Institutions"), ("banks.html", "outcomes", "Outcomes")]),
]


def sample_pathways():
    out = []
    for pid, title, mins, stops in SAMPLE_PATHWAYS:
        out.append({"id": pid, "title": title, "for_whom": "[Sample] who this pathway is for", "minutes": mins,
                    "intro": "[Sample] Layout test text. The real introduction is being written.",
                    "stops": [{"page": pg, "anchor": an, "label": lb, "bridge": "[Sample] What to notice at this stop."} for pg, an, lb in stops],
                    "closing_question": "[Sample] A closing question will appear here.",
                    "handout": {"questions": ["[Sample] Discussion question 1.", "[Sample] Discussion question 2.", "[Sample] Discussion question 3."]}})
    return out


def wrap_phase2():
    print("Phase 2")
    for name, var, js, sampler in (("lenses.json", "LENSES", "lenses-data.js", sample_lenses),
                                   ("pathways.json", "PATHWAYS", "pathways-data.js", sample_pathways)):
        src = DRAFTS / name
        if src.exists():
            data = json.loads(read(src))
            text = (f"// Generated from work/drafts/{name} by work/tools/integrate.py. Edit the JSON, then re-run.\n"
                    f"window.{var} = {json.dumps(data, indent=1, ensure_ascii=False)};\n")
        else:
            data = sampler()
            text = (f"// SAMPLE ONLY: work/drafts/{name} does not exist yet. Generated by work/tools/integrate.py\n"
                    f"// from the chapters so the site's {var.lower()} machinery can be built and tested.\n"
                    f"window.{var}_SAMPLE = true;\nwindow.{var} = {json.dumps(data, indent=1, ensure_ascii=False)};\n")
            print(f"  note: work/drafts/{name} not found; wrote SAMPLE data")
        write_if_changed(ROOT / "js" / js, text)
    for name in ("why-it-matters.html", "banks.html"):
        draft_p, page_p = DRAFTS / name, ROOT / name
        if not draft_p.exists():
            print(f"  note: work/drafts/{name} not found; {name} keeps its placeholder sections")
            continue
        page = read(page_p)
        m = START_RE.search(page)
        if not m:
            problems.append(f"{name}: CONTENT START/END markers not found")
            continue
        frag = read(draft_p).strip("\n")
        body = "\n".join(("    " + line) if line.strip() else "" for line in frag.split("\n"))
        page = page[:m.start()] + m.group(1) + body + "\n    <!-- CONTENT END -->" + page[m.end():]
        dek_m = DEK_RE.search(frag)
        if dek_m:
            page = re.sub(r'<meta name="description" content="[^"]*">',
                          '<meta name="description" content="' + html.escape(strip_tags(dek_m.group(1)), quote=True) + '">', page, count=1)
        write_if_changed(page_p, page)


# ---------- 4: image usage ----------
def image_usage():
    print("Image usage")
    usage = {}
    for n in range(1, 8):
        p = ROOT / "chapters" / f"ch{n}.html"
        for img in re.findall(r'<figure[^>]*data-image="([^"]+)"', read(p)):
            usage.setdefault(img, []).append({"href": f"chapters/ch{n}.html", "label": f"Chapter {n}"})
    for page, label, var in (("cast.html", "Cast of Characters", "CAST"),):
        data = load_js_var(ROOT / "js" / "cast-data.js", var) or []
        for person in data:
            if person.get("image"):
                usage.setdefault(person["image"], []).append({"href": f"{page}#{person.get('id', '')}", "label": f"{label}: {person.get('name', '')}"})
    write_if_changed(ROOT / "js" / "image-usage-data.js",
                     "// Generated by work/tools/integrate.py from the chapter pages and js/cast-data.js. Do not edit.\n"
                     f"window.IMAGE_USAGE = {json.dumps(usage, indent=1, ensure_ascii=False)};\n")
    return usage


# ---------- 5: other generated data ----------
def run_tool(name):
    r = subprocess.run([sys.executable, str(TOOLS / name)], cwd=ROOT, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(f"  {name}: " + (out[-1] if out else "(no output)"))
    if r.returncode:
        problems.append(f"{name} failed: {r.stderr.strip()[-400:]}")


# ---------- 6: static checks ----------
def static_checks(footnote, usage):
    print("Checks")
    sources = load_js_var(ROOT / "js" / "sources-data.js", "SOURCES") or {}
    glossary = load_js_var(ROOT / "js" / "glossary-data.js", "GLOSSARY") or {}
    credits = {c["id"]: c for c in (load_js_var(ROOT / "images" / "credits.js", "IMAGE_CREDITS") or [])}

    def check_src(where, sid, page=None):
        s = sources.get(sid)
        if not s:
            problems.append(f"{where}: unknown source id '{sid}'")
            return
        if not s.get("in_library"):
            problems.append(f"{where}: source '{sid}' is not in the library")
            return
        f = ROOT / "sources" / s["folder"] / s["filename"]
        if not f.exists():
            problems.append(f"{where}: file for '{sid}' missing on disk ({f.relative_to(ROOT)})")

    for n in range(1, 8):
        rel = f"chapters/ch{n}.html"
        page = read(ROOT / rel)
        for sid in re.findall(r'<a class="cite"[^>]*data-src="([^"]*)"', page):
            check_src(rel, sid)
        for t in re.findall(r'class="term"[^>]*data-term="([^"]*)"', page):
            if t not in glossary:
                problems.append(f"{rel}: glossary id '{t}' not in js/glossary-data.js")
        for img in re.findall(r'<figure[^>]*data-image="([^"]+)"', page):
            if img not in credits:
                problems.append(f"{rel}: image id '{img}' not in images/credits.js")
    for c in credits.values():
        for key in ("file", "narrow_file"):
            if c.get(key) and not (ROOT / ("" if c[key].startswith("images/") else "images/") / c[key]).exists():
                problems.append(f"images/credits.js: {c['id']} {key} '{c[key]}' not on disk")
    for gid, g in glossary.items():
        for s in g.get("see_also", []) or []:
            if s not in glossary:
                problems.append(f"glossary '{gid}': see_also '{s}' not in glossary")
        for c in g.get("cites", []) or []:
            check_src(f"glossary '{gid}'", c.get("source_id"))
    for name, var in (("cast-data.js", "CAST"), ("timeline-data.js", "TIMELINE")):
        for item in load_js_var(ROOT / "js" / name, var) or []:
            for c in item.get("cites", []):
                check_src(f"js/{name} '{item.get('id') or item.get('title')}'", c.get("source_id"))

    blocks = footnote.get("paragraphs", []) + footnote.get("context_passages", [])
    for b in blocks:
        text = b.get("text", "")
        for a in b.get("annotations", []):
            if a.get("phrase") not in text:
                problems.append(f"footnote {a.get('id')}: phrase is not an exact substring of its paragraph")
            for c in a.get("cites", []):
                check_src(f"footnote {a.get('id')}", c.get("source_id"))
                if c.get("pdf_source_id"):
                    check_src(f"footnote {a.get('id')} (pdf_source_id)", c["pdf_source_id"])
            for t in a.get("glossary_terms", []) or []:
                if t not in glossary:
                    problems.append(f"footnote {a.get('id')}: glossary id '{t}' not in js/glossary-data.js")
    for key in ("intro", "closing"):
        part = footnote.get(key)
        if isinstance(part, dict):
            for c in part.get("cites", []):
                check_src(f"footnote {key}", c.get("source_id"))

    unused = sorted(set(credits) - set(usage))
    if unused:
        print("  note: images in credits but not shown on any page: " + ", ".join(unused))


def main():
    deks = splice_chapters()
    fill_home(deks)
    fn = wrap_footnote()
    wrap_phase2()
    print("Generated data")
    run_tool("make_sources_js.py")
    if "--no-log" not in sys.argv:
        run_tool("build_log.py")
    run_tool("gaps_to_js.py")
    usage = image_usage()
    static_checks(fn, usage)
    for p in problems:
        print("PROBLEM", p)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
