#!/usr/bin/env python3
"""Wrap a JSON file as a script the site can load from file://.

Usage: python3 work/tools/wrap_json.py work/drafts/footnote.json FOOTNOTE js/footnote-data.js
writes:  window.FOOTNOTE = <json>;
The JSON is parsed first, so a malformed file fails loudly instead of breaking the page.
"""
import json
import sys
from pathlib import Path

src, var, out = sys.argv[1], sys.argv[2], sys.argv[3]
data = json.loads(Path(src).read_text(encoding="utf-8"))
Path(out).write_text(
    f"// Generated from {src} by work/tools/wrap_json.py. Edit the JSON, then re-run.\n"
    f"window.{var} = {json.dumps(data, indent=1, ensure_ascii=False)};\n",
    encoding="utf-8",
)
print(f"wrote {out} (window.{var})")
