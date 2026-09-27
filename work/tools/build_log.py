#!/usr/bin/env python3
"""Scribe: build the official build log from the coordinator's notes.

Reads:
  build-log/inbox.jsonl       coordinator's append-only notes (one JSON object per line)
  work/briefs/*.md            the exact briefs sent to agents (00-common-rules.md applies to all)
  build-log/corrections.md    the Fact-Checker's corrections table
  build-log/messages.jsonl    follow-up messages the coordinator sent to running or resumed agents (optional)
  sources/manifest.csv, work/facts/*, work/drafts/*, sources/candidates/candidates.csv   (for the summary counts)

Writes:
  build-log/log.json          the official log
  build-log/log.js            the same data as `window.BUILD_LOG = {...};` (loads from file://)

Deterministic and idempotent: the output depends only on the input files. The
"generated" field is the time of the newest note in the inbox, not the clock
time, so re-running with the same inbox produces identical files.
Never hand-edit log.json; add a note with work/tools/note.py and re-run this.

Usage (from anywhere):  python3 work/tools/build_log.py
"""
import csv
import glob
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
INBOX = os.path.join(ROOT, 'build-log', 'inbox.jsonl')
BRIEFS_DIR = os.path.join(ROOT, 'work', 'briefs')
CORRECTIONS = os.path.join(ROOT, 'build-log', 'corrections.md')
OUT_JSON = os.path.join(ROOT, 'build-log', 'log.json')
OUT_JS = os.path.join(ROOT, 'build-log', 'log.js')
MESSAGES = os.path.join(ROOT, 'build-log', 'messages.jsonl')
MANIFEST = os.path.join(ROOT, 'sources', 'manifest.csv')
DOWNLOAD_LOG = os.path.join(ROOT, 'sources', 'download_log.csv')
CANDIDATES = os.path.join(ROOT, 'sources', 'candidates', 'candidates.csv')              # Phase 1 Scout
CANDIDATES_P2 = os.path.join(ROOT, 'sources', 'candidates', 'phase2', 'candidates.csv')  # Phase 2 Scout
FACTS_DIR = os.path.join(ROOT, 'work', 'facts')
DRAFTS_DIR = os.path.join(ROOT, 'work', 'drafts')
FOOTNOTE = os.path.join(DRAFTS_DIR, 'footnote.json')
COMMON_RULES = 'work/briefs/00-common-rules.md'

PROJECT = 'Ask Why: The Rise and Fall of Enron'

COORDINATOR_ROLE = (
    'Plans the work, writes each agent\'s brief, starts the agents, passes files between them, '
    'reviews what they hand back (accepting it or sending it back), and reports to the project owner. '
    'Agents never talk to each other directly; everything goes through the coordinator.'
)

# ---------------------------------------------------------------------------
# "Before the agents": the human work that came first. Plain language, drawn
# from sources/README.md and CLAUDE.md.
# ---------------------------------------------------------------------------
BEFORE_THE_AGENTS = {
    'summary': (
        'Before any AI agent ran, the project owner (a person, not an AI) built and checked the '
        'library of source documents by hand. The owner listed 76 primary sources (74 of them downloaded as files): the Enron board\'s '
        'own investigation (the Powers Report), the bankruptcy examiner\'s reports (by Neal Batson), '
        'Enron\'s filings with the SEC, SEC enforcement complaints, congressional hearings and reports, '
        'the Sarbanes-Oxley Act and its legislative history, and court decisions. Each one is listed in '
        'a master list (manifest.csv) with its title, date, publisher and web address. Most are U.S. '
        'government works in the public domain. The agents were allowed to rely only on this library. '
        'The lesson for anyone using AI: an agent\'s work can only be as trustworthy as its sources.'
    ),
    'fingerprint_explained': (
        'A SHA-256 fingerprint is a short code (64 letters and digits) calculated from every byte of a '
        'file. Change even one comma in the file and the fingerprint comes out completely different. '
        'Two files with the same fingerprint are, for all practical purposes, identical. So by recording '
        'each file\'s fingerprint when it was downloaded, and checking it again later, you can prove that '
        'the file an agent read is exactly the file that came from the official source, with nothing '
        'added, removed or altered.'
    ),
    'fingerprint_check': (
        'When each document was downloaded, its fingerprint was recorded in download_log.csv. Before the '
        'agents started (Step 0), the coordinator recomputed the fingerprint of every file: all 74 of 74 '
        'matched. The only two documents with no file were the ones already known to be missing (the '
        'Batson Second and Third Interim Reports, which are not freely available online). Every agent is '
        'also told to re-check the fingerprint of each file it uses and to stop and report any mismatch.'
    ),
    'lessons': [
        {
            'title': 'An annotated copy almost replaced the real one',
            'text': (
                'A copy of the Batson Final Report found on an advocacy website nearly got used in place of '
                'the clean court copy. The report\'s text was genuine, but the website had added 56 '
                'highlights and 63 comments of its own. An AI agent reading that copy could easily have '
                'mistaken an advocate\'s comment for the examiner\'s official finding. The library uses '
                'the clean court scans instead.'
            ),
        },
        {
            'title': 'Three different documents were each called "Appendix E"',
            'text': (
                'The bankruptcy examiner wrote several reports, and three of them each have an "Appendix E" '
                'on a completely different subject: in the Second Interim Report it covers prepays (loans '
                'disguised as trades), in the Third Interim Report it covers JPMorgan Chase, and in the Final '
                'Report it covers the Royal Bank of Scotland. A label alone is not enough; you must always '
                'name the report as well as the letter.'
            ),
        },
        {
            'title': 'Fingerprints proved the files were the originals',
            'text': (
                'Every downloaded file\'s SHA-256 fingerprint was recorded and later re-checked. All 74 '
                'files matched, confirming that the documents the agents read were exactly the ones that '
                'were downloaded from the original sources.'
            ),
        },
    ],
    'sources': ['sources/README.md', 'CLAUDE.md', 'sources/manifest.csv', 'sources/download_log.csv'],
}


# ---------------------------------------------------------------------------
# Phases. A brief run belongs to the phase of its agent_start `wave`; every other
# record belongs to the phase whose time window contains it. Windows come from
# the coordinator's decision notes:
#   Phase 1 ends at the decision titled "Phase 1 complete..."
#   the Revision pass starts with the first note after that and ends at "Revision pass complete"
#   Phase 2 starts at "Phase 2 approved..." (or its first phase2 agent_start) and runs to the newest note.
# ---------------------------------------------------------------------------
PHASES = [
    {'id': 'phase1', 'name': 'Phase 1',
     'waves': ['1', '1-review', '2', '3', '4'],
     'plain': ('The agents read the source library, wrote and fact-checked fact cards, and built the Story, '
               'the Cast of Characters, the Timeline, the Glossary, the annotated Footnote and this page; '
               'the phase ended with a check-in with the project owner.')},
    {'id': 'revision', 'name': 'Revision pass',
     'waves': ['revision'],
     'plain': ('The project owner approved the Source Scout\'s 10 candidate documents and added them, plus one more '
               'hearing, to the library (11 documents in all); the agents then used them to fill in claims that '
               'Phase 1 had left out or marked as not yet verified.')},
    {'id': 'phase2', 'name': 'Phase 2',
     'waves': ['phase2-A', 'phase2'],
     'plain': ('The agents added the reading lenses, the pathways, a page on the banks, notes on other footnotes '
               'in the same report, and "Why This Matters to You", each checked by a Fact-Checker.')},
]
WAVE_PHASE = {w: ph['id'] for ph in PHASES for w in ph['waves']}

# Fact-card series (the letter before the number in a card id) and the phase that wrote them.
CARD_SERIES_PHASE = {'A': 'phase1', 'B': 'phase1', 'C': 'phase1', 'F': 'phase1',
                     'G': 'revision', 'N': 'phase2', 'K': 'phase2', 'S': 'phase2'}


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, '/')


def read_text(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def load_inbox():
    records = []
    if not os.path.exists(INBOX):
        return records
    with open(INBOX, encoding='utf-8') as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                sys.exit('inbox.jsonl line %d is not valid JSON: %s' % (n, e))
            rec['_seq'] = n  # original order, used to break ties between equal times
            records.append(rec)
    # Stable sort by time; notes with the same time keep inbox order.
    records.sort(key=lambda r: (r.get('time', ''), r['_seq']))
    return records


def load_briefs():
    briefs = {}
    if os.path.isdir(BRIEFS_DIR):
        for name in sorted(os.listdir(BRIEFS_DIR)):
            if name.endswith('.md'):
                p = os.path.join(BRIEFS_DIR, name)
                briefs[rel(p)] = read_text(p)
    return briefs


def split_row(line):
    line = line.strip()
    if line.startswith('|'):
        line = line[1:]
    if line.endswith('|'):
        line = line[:-1]
    return [c.strip() for c in re.split(r'(?<!\\)\|', line)]


def load_corrections():
    """Parse the markdown table in corrections.md into a list of dicts."""
    if not os.path.exists(CORRECTIONS):
        return []
    rows, header = [], None
    for line in read_text(CORRECTIONS).splitlines():
        if not line.strip().startswith('|'):
            continue
        cells = split_row(line)
        if header is None:
            header = cells
            continue
        if all(re.fullmatch(r':?-+:?', c) for c in cells if c):
            continue  # separator row
        if not any(cells):
            continue
        keys = [slug(h) for h in header]
        row = {k: (cells[i] if i < len(cells) else '') for i, k in enumerate(keys)}
        # Two Fact-Checkers sometimes appended at the same time, so the file's own '#' repeats.
        # log_no is a unique number in file order; row_label keeps the file's '#' unchanged.
        label = row.pop('number', '')
        row = dict({'log_no': len(rows) + 1, 'row_label': label}, **row)
        row['recorded_in'] = 'build-log/corrections.md'
        rows.append(row)
    return rows


def slug(h):
    h = h.strip().lower().replace('#', 'number')
    return re.sub(r'[^a-z0-9]+', '_', h).strip('_') or 'col'


def clean(rec):
    return {k: v for k, v in rec.items() if not k.startswith('_')}


def label_for(rec, names):
    t = rec.get('type')
    who = names.get(rec.get('agent_id'), rec.get('name', rec.get('agent_id', 'agent')))
    if t == 'decision':
        return 'Coordinator decision: ' + rec.get('title', '')
    if t == 'agent_start':
        return 'Started: %s (brief %s)' % (who, os.path.basename(rec.get('brief_file', '')) or '?')
    if t == 'agent_finish':
        d = rec.get('decision')
        return 'Finished: %s%s' % (who, ' (%s)' % d if d else '')
    if t == 'handoff':
        return 'Handoff: %s to %s' % (rec.get('from', '?'), rec.get('to', '?'))
    if t == 'review':
        return 'Review by %s: %s' % (who, rec.get('result', ''))
    if t == 'web_source':
        return 'Web source used: ' + rec.get('site', rec.get('url', ''))
    if t == 'correction':
        return 'Correction: ' + rec.get('title', rec.get('what', ''))
    return str(t)


def load_messages():
    """Follow-up messages the coordinator sent (verbatim records, file order)."""
    out = []
    if os.path.exists(MESSAGES):
        with open(MESSAGES, encoding='utf-8') as f:
            for n, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError as e:
                    sys.exit('messages.jsonl line %d is not valid JSON: %s' % (n, e))
    return out


def split_targets(text):
    """'Reference Writer, Image Researcher and X' -> ['Reference Writer', 'Image Researcher', 'X']"""
    text = re.sub(r'^(.*?)\s*\(Parts ([A-Z])((?:,\s*[A-Z])*)\s+and\s+([A-Z])\)$',
                  lambda m: ', '.join('%s (Part %s)' % (m.group(1), x)
                                      for x in [m.group(2)] + re.findall(r'[A-Z]', m.group(3)) + [m.group(4)]),
                  str(text or '').strip())
    parts = re.split(r',\s*|\s+and\s+|\s*&\s+(?=[A-Z][a-z]+ [A-Z])', str(text or ''))
    return [p.strip() for p in parts if p.strip()]


def match_agents(target, agents, order):
    """Agent ids a handoff/message target names. Exact name or id first; otherwise the target
    is a shortened form of the name ('Image Researcher' -> 'Image Researcher & Diagrammer',
    'Fact-Checker (Part B)' -> 'Fact-Checker (Part B: cast, ...)')."""
    t = target.strip().lower()
    if not t:
        return []
    exact = [a for a in order if agents[a]['name'].lower() == t or a.lower() == t]
    if exact:
        return exact
    out = []
    for a in order:
        n = agents[a]['name'].lower()
        if n.startswith(t) and n[len(t):len(t) + 1] in (' ', ':', '('):
            out.append(a)
        elif t.endswith(')') and n.startswith(t[:-1]) and n[len(t) - 1:len(t)] == ':':
            out.append(a)
    return out


def agents_for(end, agents, order):
    ids = []
    for t in split_targets(end):
        for a in match_agents(t, agents, order):
            if a not in ids:
                ids.append(a)
    return ids


def new_run(kind, **kw):
    run = {'run': None, 'kind': kind, 'brief_file': None, 'brief': None, 'brief_summary': None,
           'started': None, 'finished': None, 'inputs': [], 'outputs': [],
           'decision': 'pending', 'reason': '', 'handoffs_in': [], 'messages': [], 'reviews': []}
    run.update(kw)
    return run


# ---------------------------------------------------------------------------
# Summary counts, computed from files
# ---------------------------------------------------------------------------
def manifest_ids():
    if not os.path.exists(MANIFEST):
        return []
    with open(MANIFEST, encoding='utf-8', newline='') as f:
        return [r['id'] for r in csv.DictReader(f) if r.get('id')]


def count_csv_rows(path):
    if not os.path.exists(path):
        return 0
    with open(path, encoding='utf-8', newline='') as f:
        return sum(1 for r in csv.DictReader(f) if any((v or '').strip() for v in r.values()))


def fact_card_counts():
    written = checked = 0
    files = []
    series = {}
    for path in sorted(glob.glob(os.path.join(FACTS_DIR, '*.json'))):
        try:
            data = json.load(open(path, encoding='utf-8'))
        except (ValueError, OSError):
            continue
        if not (isinstance(data, list) and data and all(isinstance(c, dict) and 'claim' in c for c in data)):
            continue
        files.append(rel(path))
        written += len(data)
        checked += sum(1 for c in data if str(c.get('checked') or '').strip())
        for c in data:
            m = re.match(r'([A-Z]+)-', str(c.get('id', '')))
            k = m.group(1) if m else '?'
            s = series.setdefault(k, {'series': k, 'file': rel(path), 'written': 0, 'checked': 0})
            s['written'] += 1
            s['checked'] += 1 if str(c.get('checked') or '').strip() else 0
    return written, checked, files, [series[k] for k in sorted(series)]


def annotation_counts():
    if not os.path.exists(FOOTNOTE):
        return 0, 0
    data = json.load(open(FOOTNOTE, encoding='utf-8'))
    anns = [a for p in data.get('paragraphs', []) for a in (p.get('annotations') or [])]
    return len(anns), sum(1 for a in anns if str(a.get('checked') or '').strip())


def sources_read(records, ids):
    """Library documents named (by manifest id) in the agents' finish notes, read logs and
    fact-check reports: the documents the agents actually opened."""
    texts = [' '.join(map(str, r.get('inputs', []))) for r in records if r.get('type') == 'agent_finish']
    for pat in ('*readlog*.md', 'factcheck-*.md'):
        for path in sorted(glob.glob(os.path.join(FACTS_DIR, pat))):
            texts.append(read_text(path))
    blob = '\n'.join(texts)
    return [i for i in ids if re.search(r'(?<![\w-])' + re.escape(i) + r'(?![\w-])', blob)]


def sources_cited(ids):
    blob = ''
    for path in sorted(glob.glob(os.path.join(DRAFTS_DIR, '*.html'))):
        blob += read_text(path)
    cited = set(re.findall(r'data-src="([^"]+)"', blob))
    for path in sorted(glob.glob(os.path.join(FACTS_DIR, '*.json'))) + [FOOTNOTE]:
        if os.path.exists(path):
            cited.update(re.findall(r'"source_id":\s*"([^"]+)"', read_text(path)))
            cited.update(re.findall(r'"src":\s*"([^"]+)"', read_text(path)))
    return [i for i in ids if i in cited]


def candidate_ids(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding='utf-8', newline='') as f:
        return [r.get('id', '') for r in csv.DictReader(f) if any((v or '').strip() for v in r.values())]


# Decisions made by the project owner (not the coordinator's own decisions that mention the owner):
# the title starts with "Owner" or contains one of these phrases.
OWNER_TITLE_PHRASES = ['owner approved', 'Owner decisions', 'Plan change requested by the project owner']


def is_owner_decision(d):
    t = str(d.get('title', ''))
    return t.startswith('Owner') or any(ph.lower() in t.lower() for ph in OWNER_TITLE_PHRASES)


def plural(n, one, many=None):
    return '%d %s' % (n, one if n == 1 else (many or one + 's'))


def main():
    records = load_inbox()
    briefs = load_briefs()
    messages = load_messages()
    common_text = briefs.get(COMMON_RULES, '')

    decisions, reviews, web_sources, note_corrections, handoffs_all = [], [], [], [], []
    agents, order = {}, []
    finishes = []  # (seq, agent_id, rec) for 'handled by another agent' detection

    def agent(aid, rec):
        if aid not in agents:
            agents[aid] = {'id': aid, 'name': rec.get('name', aid), 'role': rec.get('role', ''),
                           'brief_file': '', 'brief_files': [], 'common_rules_file': COMMON_RULES,
                           'brief': '', 'wave': rec.get('wave'), 'decision': 'pending', 'reason': '',
                           'decision_time': None, 'runs': [], 'handoffs': [], 'reviews': [],
                           'messages': []}
            order.append(aid)
        a = agents[aid]
        for k in ('name', 'role', 'wave'):
            if rec.get(k):
                a[k] = rec[k]
        return a

    def open_run(a):
        runs = [r for r in a['runs'] if r['finished'] is None and not r.get('_orphan')]
        return runs[-1] if runs else None

    for rec in records:
        t = rec.get('type')
        c = clean(rec)
        if t == 'decision':
            decisions.append(c)
        elif t == 'agent_start':
            a = agent(rec.get('agent_id', rec.get('name', 'unknown')), rec)
            # A resumed run that a handoff opened but no finish note ever closed is not
            # continued by a new brief: set it aside (resolved after the loop).
            for r in a['runs']:
                if r['finished'] is None and r['kind'] == 'resumed':
                    r['_orphan'] = True
            bf = rec.get('brief_file', '')
            text = briefs.get(bf)
            a['runs'].append(new_run(
                'brief', brief_file=bf or None,
                brief=(text.rstrip() if text is not None else ('(Brief file %s not found.)' % bf if bf else None)),
                started=rec.get('time'), inputs=rec.get('inputs', []), outputs=rec.get('outputs', []),
                wave=rec.get('wave')))
            if bf and bf not in a['brief_files']:
                a['brief_files'].append(bf)
        elif t == 'agent_finish':
            aid = rec.get('agent_id', rec.get('name', 'unknown'))
            a = agent(aid, rec)
            run = open_run(a)
            if run is None:  # resumed by a message: no new agent_start
                run = new_run('resumed', brief_summary='Resumed by a message from the coordinator (no new brief file).')
                a['runs'].append(run)
            run['finished'] = rec.get('time')
            for k in ('inputs', 'outputs'):
                if rec.get(k):
                    run[k] = rec[k]
            run['decision'] = rec.get('decision') or 'pending'
            run['reason'] = rec.get('reason', '')
            # The agent's current decision always comes from its latest finish note.
            a['decision'] = run['decision']
            a['reason'] = run['reason']
            a['decision_time'] = rec.get('time')
            finishes.append((rec['_seq'], rec.get('time'), aid, rec))
        elif t == 'handoff':
            h = {'time': rec.get('time'), 'from': rec.get('from'), 'to': rec.get('to'), 'what': rec.get('what')}
            handoffs_all.append(h)
            for aid in agents_for(rec.get('to'), agents, order):
                a = agents[aid]
                run = open_run(a)
                if run is None and a['runs']:
                    # The agent had finished; this handoff resumes it without a new brief.
                    run = new_run('resumed', started=rec.get('time'), brief_summary=rec.get('what'),
                                  _opened_by=h, _target_seq=rec['_seq'])
                    a['runs'].append(run)
                elif run is not None and run['kind'] == 'resumed' and not run['started']:
                    run['started'] = rec.get('time')
                if run is not None:
                    run['handoffs_in'].append(h)
        elif t == 'review':
            reviews.append(c)
            aid = rec.get('agent_id')
            if aid in agents:
                a = agents[aid]
                a['reviews'].append(c)
                run = open_run(a)
                last = a['runs'][-1] if a['runs'] else None
                if run is not None and run['kind'] == 'resumed':
                    run['finished'] = rec.get('time')
                    run['decision'] = 'done (closed by a review note)'
                    run['reason'] = rec.get('result', '')
                    run['reviews'].append(c)
                elif run is None and last is not None and (last['finished'] or '') < rec.get('time', ''):
                    a['runs'].append(new_run('resumed', finished=rec.get('time'),
                                             brief_summary='Resumed by a message from the coordinator (no new brief file).',
                                             decision='done (closed by a review note)',
                                             reason=rec.get('result', ''), reviews=[c]))
                elif (run or last) is not None:
                    (run or last)['reviews'].append(c)
        elif t == 'web_source':
            web_sources.append({'site': rec.get('site', ''), 'url': rec.get('url', ''),
                                'used_by': rec.get('used_by', ''), 'purpose': rec.get('purpose', ''),
                                'time': rec.get('time')})
        elif t == 'correction':
            note_corrections.append(dict(c, recorded_in='build-log/inbox.jsonl'))

    # A handoff that opened a resumed run which never finished, but whose work another agent's
    # later finish note says it covered (e.g. "... (Footnote Annotator and Image Researcher roles)"),
    # was handled by that other agent: drop the empty run and say who handled it.
    for aid in order:
        a = agents[aid]
        keep = []
        for run in a['runs']:
            h = run.get('_opened_by')
            if h is not None and run['finished'] is None:
                aliases = [t for t in split_targets(h.get('to')) if aid in match_agents(t, agents, order)]
                handler = None
                for seq, _, other, frec in finishes:
                    if other != aid and seq > run['_target_seq']:
                        txt = ' '.join([str(frec.get('reason', ''))] + list(map(str, frec.get('outputs', []))))
                        if any(al and al in txt for al in aliases):
                            handler = other
                            break
                if handler:
                    h.setdefault('handled_by', [])
                    if agents[handler]['name'] not in h['handled_by']:
                        h['handled_by'].append(agents[handler]['name'])
                    continue
                if run.get('_orphan'):
                    run['decision'] = 'no finish note'
                    run['reason'] = 'No finish note was recorded before this agent started its next brief.'
            keep.append(run)
        a['runs'] = keep

    # Follow-up messages (build-log/messages.jsonl), stored verbatim. Each is attached to the agent
    # it was sent to. Messages to an agent are matched to its resumed runs in order, aligned from
    # the end (the last message goes with the last resumed run); earlier messages were sent while
    # an earlier run was in progress.
    for i, m in enumerate(messages):
        m = dict(m, message_no=i + 1)
        for aid in agents_for(m.get('to'), agents, order):
            agents[aid]['messages'].append(m)
    # Only resumed runs that had started by the time the message was recorded can be its target.
    for aid in order:
        a = agents[aid]
        msgs = a['messages']
        cutoff = max([m.get('recorded') or m.get('time') or '' for m in msgs] or [''])
        resumed = [r for r in a['runs'] if r['kind'] == 'resumed'
                   and (not cutoff or (r['started'] or r['finished'] or '') <= cutoff)]
        k = min(len(msgs), len(resumed))
        for m, r in zip(msgs[len(msgs) - k:], resumed[len(resumed) - k:]):
            r['messages'].append(dict(m, matched='resumed this run'))
        firsts = [r for r in a['runs'] if r['kind'] == 'brief']
        for m in msgs[:len(msgs) - k]:
            target = firsts[-1] if firsts else (a['runs'][-1] if a['runs'] else None)
            if target is not None:
                target['messages'].append(dict(m, matched='sent while this run was in progress'))

    # Tidy runs: number them, fill brief summaries, drop internal fields.
    for aid in order:
        a = agents[aid]
        for n, run in enumerate(a['runs'], 1):
            run['run'] = n
            for k in [k for k in run if k.startswith('_')]:
                del run[k]
            if run['kind'] == 'resumed':
                parts = [h['what'] for h in run['handoffs_in'] if h.get('what')]
                parts += [m.get('summary') or m.get('text') or m.get('message') or '' for m in run['messages']
                          if m.get('matched') == 'resumed this run']
                if parts:
                    run['brief_summary'] = ' | '.join(p for p in parts if p)
            if run['finished'] is None and run['decision'] == 'pending':
                run['reason'] = run['reason'] or 'Still working: no finish note yet.'
        # Agent-level brief (kept for the page): every brief file this agent ran with, in order.
        bruns = [r for r in a['runs'] if r['kind'] == 'brief' and r['brief']]
        if bruns:
            a['brief_file'] = bruns[0]['brief_file']
            if len(bruns) == 1:
                a['brief'] = bruns[0]['brief']
            else:
                a['brief'] = '\n\n'.join('=== Run %d brief: %s ===\n\n%s' % (r['run'], r['brief_file'], r['brief'])
                                         for r in bruns)
            a['brief'] += '\n\n---\nThis agent was also bound by the common rules for every agent, in %s.' % COMMON_RULES
        if not a['decision_time'] and a['runs']:
            a['decision'] = 'working'

    # Attach handoffs to the agents they involve (either end, or a wave / all agents).
    for h in handoffs_all:
        involved = set(agents_for(h.get('from'), agents, order)) | set(agents_for(h.get('to'), agents, order))
        for e in (str(h.get('from') or ''), str(h.get('to') or '')):
            m = re.match(r'wave\s*(\d+)\s+agents', e, re.I)
            if m:
                involved |= {a for a in order if str(agents[a].get('wave')) == m.group(1)}
            if e.lower() in ('all agents', 'every agent'):
                involved |= set(order)
        for aid in order:
            if aid in involved:
                agents[aid]['handoffs'].append(h)

    used = {r['brief_file'] for a in agents.values() for r in a['runs'] if r.get('brief_file')}
    unused_briefs = [{'file': f, 'text': t} for f, t in briefs.items()
                     if f not in used and f != COMMON_RULES]

    corrections = load_corrections() + note_corrections

    names = {aid: agents[aid]['name'] for aid in order}
    timeline = [{'time': r.get('time'), 'type': r.get('type'), 'label': label_for(r, names),
                 **({'agent_id': r['agent_id']} if r.get('agent_id') else {})}
                for r in records]

    # ---- Phases ----
    def first_time(pred):
        return next((r.get('time') for r in records if pred(r)), None)

    def dec_time(prefix):
        return first_time(lambda r: r.get('type') == 'decision' and str(r.get('title', '')).startswith(prefix))

    last_time = records[-1]['time'] if records else None
    p1_end = dec_time('Phase 1 complete') or first_time(
        lambda r: r.get('type') == 'agent_start' and WAVE_PHASE.get(str(r.get('wave'))) != 'phase1')
    rev_start = first_time(lambda r: p1_end and r.get('time', '') > p1_end)
    rev_end = dec_time('Revision pass complete')
    p2_start = dec_time('Phase 2 approved') or first_time(
        lambda r: r.get('type') == 'agent_start' and WAVE_PHASE.get(str(r.get('wave'))) == 'phase2')

    def phase_of_time(t):
        if not t or not p1_end or t <= p1_end:
            return 'phase1'
        if p2_start and t >= p2_start:
            return 'phase2'
        return 'revision'

    for aid in order:
        for run in agents[aid]['runs']:
            w = run.get('wave')
            run['phase'] = WAVE_PHASE.get(str(w)) if w is not None and str(w) in WAVE_PHASE \
                else phase_of_time(run['started'] or run['finished'])
    for item in timeline:
        item['phase'] = phase_of_time(item['time'])
    for d in decisions:
        d['phase'] = phase_of_time(d.get('time'))
    for w in web_sources:
        w['phase'] = phase_of_time(w.get('time'))
    for r in reviews:
        r['phase'] = phase_of_time(r.get('time'))

    # Corrections carry a date, not a time. Rows dated on or before the day Phase 1 ended are Phase 1.
    # Later rows are appended in order. The Revision pass's rows come first: the unbroken run of rows
    # that mention the revision pass or a G-card (the revision pass's card series). Everything after
    # that run is Phase 2.
    p1_day = (p1_end or '')[:10]
    later = [c for c in corrections if 'log_no' in c and p1_day and str(c.get('date', ''))[:10] > p1_day]
    rev_last = 0
    for c in later:
        if re.search(r'revision pass|\bG-\d', ' '.join(str(v) for v in c.values()), re.I):
            rev_last = c['log_no']
        else:
            break
    for c in corrections:
        if c.get('recorded_in') != 'build-log/corrections.md':
            c['phase'] = phase_of_time(c.get('time'))
        elif not p1_day or str(c.get('date', ''))[:10] <= p1_day:
            c['phase'] = 'phase1'
        else:
            c['phase'] = 'revision' if c['log_no'] <= rev_last else 'phase2'

    # ---- Summary block (all counts computed from files) ----
    ids = manifest_ids()
    read = sources_read(records, ids)
    cited = sources_cited(ids)
    cards_written, cards_checked, card_files, card_series = fact_card_counts()
    anns, anns_checked = annotation_counts()
    all_runs = [r for a in agents.values() for r in a['runs']]
    n_runs = len(all_runs)
    n_resumed = sum(1 for r in all_runs if r['kind'] == 'resumed')
    n_open = sum(1 for r in all_runs if r['finished'] is None)
    sites = sorted({w['site'] for w in web_sources if w['site']})
    cand1, cand2 = candidate_ids(CANDIDATES), candidate_ids(CANDIDATES_P2)
    idset = set(ids)
    cand1_ok = [c for c in cand1 if c in idset]
    cand2_ok = [c for c in cand2 if c in idset]
    n_candidates = len(cand1) + len(cand2)
    n_corr = len(corrections)  # every row counted once, by log_no
    dup_labels = sorted({c['row_label'] for c in corrections if c.get('row_label')
                         and sum(1 for d in corrections if d.get('row_label') == c['row_label']) > 1},
                        key=lambda x: (len(x), x))

    windows = {'phase1': (records[0]['time'] if records else None, p1_end),
               'revision': (rev_start, rev_end),
               'phase2': (p2_start, last_time)}
    phases = []
    for ph in PHASES:
        pid = ph['id']
        pruns = [(aid, r) for aid in order for r in agents[aid]['runs'] if r['phase'] == pid]
        p_agents = []
        for aid, _ in pruns:
            if aid not in p_agents:
                p_agents.append(aid)
        p_open = sum(1 for _, r in pruns if r['finished'] is None)
        p_series = [s for s in card_series if CARD_SERIES_PHASE.get(s['series']) == pid]
        p_sites = sorted({w['site'] for w in web_sources if w['phase'] == pid and w['site']})
        p_cands = cand1 if pid == 'phase1' else (cand2 if pid == 'phase2' else [])
        st, en = windows[pid]
        status = 'in progress' if (pid == 'phase2' and p_open) else ('complete' if en else 'not started')
        if pid == 'phase2' and not p_open and pruns:
            status = 'complete (as of the newest note)'
        phases.append({
            'id': pid, 'name': ph['name'], 'start': st,
            'end': None if status == 'in progress' else en,
            'last_note': en if status == 'in progress' else None,
            'status': status, 'waves': ph['waves'],
            'summary': ph['plain'],
            'agents': [{'id': a, 'name': agents[a]['name']} for a in p_agents],
            'counts': {
                'agents': len(p_agents),
                'runs': len(pruns),
                'runs_resumed_by_message': sum(1 for _, r in pruns if r['kind'] == 'resumed'),
                'runs_still_open': p_open,
                'coordinator_decisions': sum(1 for d in decisions if d['phase'] == pid),
                'fact_card_series': [s['series'] for s in p_series],
                'fact_cards_written': sum(s['written'] for s in p_series),
                'fact_cards_checked': sum(s['checked'] for s in p_series),
                'corrections': sum(1 for c in corrections if c.get('phase') == pid),
                'web_sites': p_sites,
                'candidates_found': len(p_cands),
            },
        })
    for ph in phases:
        c = ph['counts']
        c_text = '%s ran %s in %s' % (ph['name'], plural(c['agents'], 'agent'), plural(c['runs'], 'run'))
        c_text += (' (%d still working)' % c['runs_still_open']) if c['runs_still_open'] else ''
        extras = []
        if c['fact_cards_written']:
            extras.append('%s written (%d checked)' % (plural(c['fact_cards_written'], 'fact card'), c['fact_cards_checked']))
        extras.append(plural(c['corrections'], 'correction'))
        if c['candidates_found']:
            extras.append(plural(c['candidates_found'], 'candidate source'))
        ph['counts_text'] = c_text + ': ' + ', '.join(extras) + '.'

    summary = {
        'agents': len(order),
        'runs': n_runs,
        'runs_from_a_brief': n_runs - n_resumed,
        'runs_resumed_by_message': n_resumed,
        'runs_still_open': n_open,
        'coordinator_decisions': len(decisions),
        'owner_decisions': len([d for d in decisions if is_owner_decision(d)]),
        'library_documents': len(ids),
        'sources_read': len(read),
        'sources_read_ids': read,
        'sources_cited': len(cited),
        'fact_cards_written': cards_written,
        'fact_cards_checked': cards_checked,
        'fact_card_files': card_files,
        'fact_card_series': card_series,
        'footnote_annotations': anns,
        'footnote_annotations_checked': anns_checked,
        'corrections': n_corr,
        'corrections_note': ('Counted by log_no. The file\'s own row numbers repeat (%s) because two '
                             'Fact-Checkers appended rows at the same time.' % ', '.join(dup_labels))
                            if dup_labels else 'Counted by log_no.',
        'web_sources': len(sites),
        'web_sites': sites,
        'candidates_found': n_candidates,
        'candidates_phase1': len(cand1),
        'candidates_phase1_approved': len(cand1_ok),
        'candidates_phase2': len(cand2),
        'candidates_phase2_approved': len(cand2_ok),
        'candidates_awaiting_approval': (len(cand1) - len(cand1_ok)) + (len(cand2) - len(cand2_ok)),
        'phases': [{'id': ph['id'], 'name': ph['name'], **ph['counts']} for ph in phases],
        'phases_note': ('Fact cards are assigned to a phase by their series letter (A, B, C, F: Phase 1; '
                        'G: Revision pass; K, N, S: Phase 2); a few later F-cards were added in follow-ups. '
                        'Corrections are assigned by date and order in corrections.md.'),
        'counted_from': ['build-log/inbox.jsonl', 'sources/manifest.csv', 'work/facts/*.json',
                         'work/facts/*readlog*.md', 'work/facts/factcheck-*.md', 'work/drafts/*',
                         'build-log/corrections.md', 'sources/candidates/candidates.csv',
                         'sources/candidates/phase2/candidates.csv'],
    }
    summary['text'] = [
        'The coordinator ran %s, in %s: %d started from a written brief and %d resumed by a follow-up message%s.'
        % (plural(len(order), 'agent'), plural(n_runs, 'run'), n_runs - n_resumed, n_resumed,
           ' (%d still working)' % n_open if n_open else ''),
        'The library now holds %s. The agents opened %d of them, and the site cites %d.'
        % (plural(len(ids), 'document'), len(read), len(cited)),
        'The Readers wrote %s: short, sourced notes of one fact each. The Fact-Checkers checked %d of them against the documents, plus %d of the %s on Note 16.'
        % (plural(cards_written, 'fact card'), cards_checked, anns_checked, plural(anns, 'annotation')),
        'The Fact-Checkers logged %s.' % plural(n_corr, 'correction'),
        'Agents used %s, only for images and for the Source Scout\'s searches: %s.'
        % (plural(len(sites), 'website'), ', '.join(sites) if sites else 'none'),
        'The Source Scout found %s in Phase 1 (the project owner approved %d and added them to the library) and %s in Phase 2 (%d approved so far). No agent may use a candidate until the owner approves it.'
        % (plural(len(cand1), 'candidate document'), len(cand1_ok), plural(len(cand2), 'candidate document'), len(cand2_ok)),
    ] + [ph['counts_text'] for ph in phases]

    owner_decisions = [dict(d) for d in decisions if is_owner_decision(d)]

    generated = records[-1]['time'] if records else None

    log = {
        'project': PROJECT,
        'generated': generated,
        'generated_note': 'Time of the newest coordinator note; the log is rebuilt from the notes by work/tools/build_log.py.',
        'summary': summary,
        'phases': phases,
        'owner_decisions': owner_decisions,
        'coordinator': {
            'name': 'Coordinator',
            'role': COORDINATOR_ROLE,
            'plan': [d for d in decisions if str(d.get('title', '')).startswith('Original plan')],
            'decisions': decisions,
        },
        'before_the_agents': BEFORE_THE_AGENTS,
        'common_rules': {'file': COMMON_RULES, 'text': common_text},
        'agents': [agents[a] for a in order],
        'handoffs': handoffs_all,
        'messages': messages,
        'reviews': reviews,
        'corrections': corrections,
        'web_sources': web_sources,
        'briefs_not_yet_assigned': unused_briefs,
        'timeline': timeline,
    }

    body = json.dumps(log, ensure_ascii=False, indent=2)
    with open(OUT_JSON, 'w', encoding='utf-8', newline='\n') as f:
        f.write(body + '\n')
    with open(OUT_JS, 'w', encoding='utf-8', newline='\n') as f:
        f.write('// Generated by work/tools/build_log.py from build-log/inbox.jsonl. Do not edit by hand.\n')
        f.write('window.BUILD_LOG = ' + body + ';\n')
    print('wrote %s and %s: %d notes, %d agents, %d runs (%d resumed, %d open), %d decisions '
          '(%d owner), %d corrections, %d messages, %d web sites, %d+%d candidates'
          % (rel(OUT_JSON), rel(OUT_JS), len(records), len(order), n_runs, n_resumed, n_open,
             len(decisions), len(owner_decisions), n_corr, len(messages), len(sites), len(cand1), len(cand2)))


if __name__ == '__main__':
    main()
