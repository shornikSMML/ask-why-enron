#!/usr/bin/env python3
"""Scribe: build the official build log from the coordinator's notes.

Reads:
  build-log/inbox.jsonl       coordinator's append-only notes (one JSON object per line)
  work/briefs/*.md            the exact briefs sent to agents (00-common-rules.md applies to all)
  build-log/corrections.md    the Fact-Checker's corrections table

Writes:
  build-log/log.json          the official log
  build-log/log.js            the same data as `window.BUILD_LOG = {...};` (loads from file://)

Deterministic and idempotent: the output depends only on the input files. The
"generated" field is the time of the newest note in the inbox, not the clock
time, so re-running with the same inbox produces identical files.
Never hand-edit log.json; add a note with work/tools/note.py and re-run this.

Usage (from anywhere):  python3 work/tools/build_log.py
"""
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
        row['recorded_in'] = 'build-log/corrections.md'
        rows.append(row)
    return rows


def slug(h):
    h = h.strip().lower().replace('#', 'number')
    return re.sub(r'[^a-z0-9]+', '_', h).strip('_') or 'col'


def clean(rec):
    return {k: v for k, v in rec.items() if not k.startswith('_')}


def label_for(rec):
    t = rec.get('type')
    if t == 'decision':
        return 'Coordinator decision: ' + rec.get('title', '')
    if t == 'agent_start':
        return 'Started: ' + rec.get('name', rec.get('agent_id', 'agent'))
    if t == 'agent_finish':
        d = rec.get('decision')
        return 'Finished: %s%s' % (rec.get('name', rec.get('agent_id', 'agent')),
                                   ' (%s)' % d if d else '')
    if t == 'handoff':
        return 'Handoff: %s to %s' % (rec.get('from', '?'), rec.get('to', '?'))
    if t == 'review':
        return 'Review: ' + rec.get('title', rec.get('name', rec.get('agent_id', '')))
    if t == 'web_source':
        return 'Web source used: ' + rec.get('site', rec.get('url', ''))
    if t == 'correction':
        return 'Correction: ' + rec.get('title', rec.get('what', ''))
    return str(t)


def main():
    records = load_inbox()
    briefs = load_briefs()
    common_text = briefs.get(COMMON_RULES, '')

    decisions, reviews, web_sources, note_corrections, handoffs_all = [], [], [], [], []
    agents, order = {}, []

    def agent(aid, rec):
        if aid not in agents:
            bf = rec.get('brief_file', '')
            agents[aid] = {'id': aid, 'name': rec.get('name', aid), 'role': rec.get('role', ''),
                           'brief_file': bf, 'common_rules_file': COMMON_RULES,
                           'brief': '', 'wave': rec.get('wave'), 'runs': [], 'handoffs': [],
                           'reviews': []}
            order.append(aid)
        a = agents[aid]
        for k in ('name', 'role', 'brief_file', 'wave'):
            if rec.get(k):
                a[k] = rec[k]
        return a

    for rec in records:
        t = rec.get('type')
        c = clean(rec)
        if t == 'decision':
            decisions.append(c)
        elif t == 'agent_start':
            a = agent(rec.get('agent_id', rec.get('name', 'unknown')), rec)
            a['runs'].append({'started': rec.get('time'), 'finished': None,
                              'inputs': rec.get('inputs', []), 'outputs': rec.get('outputs', []),
                              'decision': 'pending', 'reason': rec.get('reason', '')})
        elif t == 'agent_finish':
            a = agent(rec.get('agent_id', rec.get('name', 'unknown')), rec)
            open_runs = [r for r in a['runs'] if r['finished'] is None]
            if open_runs:
                run = open_runs[-1]
            else:
                run = {'started': None, 'finished': None, 'inputs': [], 'outputs': [],
                       'decision': 'pending', 'reason': ''}
                a['runs'].append(run)
            run['finished'] = rec.get('time')
            for k in ('inputs', 'outputs'):
                if rec.get(k):
                    run[k] = rec[k]
            run['decision'] = rec.get('decision') or 'pending'
            run['reason'] = rec.get('reason', run['reason'])
        elif t == 'handoff':
            h = {'time': rec.get('time'), 'from': rec.get('from'), 'to': rec.get('to'),
                 'what': rec.get('what')}
            handoffs_all.append(h)
        elif t == 'review':
            reviews.append(c)
        elif t == 'web_source':
            web_sources.append({'site': rec.get('site', ''), 'url': rec.get('url', ''),
                                'used_by': rec.get('used_by', ''), 'purpose': rec.get('purpose', ''),
                                'time': rec.get('time')})
        elif t == 'correction':
            note_corrections.append(dict(c, recorded_in='build-log/inbox.jsonl'))

    # Attach handoffs and reviews to the agents they involve.
    for h in handoffs_all:
        ends = [str(h.get('from') or ''), str(h.get('to') or '')]
        for aid in order:
            a = agents[aid]
            hit = any(e and (e == a['name'] or e == aid or e.lower() == a['name'].lower()) for e in ends)
            for e in ends:
                m = re.match(r'wave\s*(\d+)\s+agents', e, re.I)
                if m and str(a.get('wave')) == m.group(1):
                    hit = True
                if e.lower() in ('all agents', 'every agent'):
                    hit = True
            if hit:
                a['handoffs'].append(h)
    for r in reviews:
        aid = r.get('agent_id')
        if aid in agents:
            agents[aid]['reviews'].append(r)

    # Full brief text (the exact file sent), with the common rules referenced by file name.
    for aid in order:
        a = agents[aid]
        text = briefs.get(a['brief_file'])
        if text is None:
            a['brief'] = '(Brief file %s not found.)' % a['brief_file'] if a['brief_file'] else ''
        else:
            a['brief'] = text.rstrip() + (
                '\n\n---\nThis agent was also bound by the common rules for every agent, in %s.' % COMMON_RULES)

    used = {agents[a]['brief_file'] for a in order}
    unused_briefs = [{'file': f, 'text': t} for f, t in briefs.items()
                     if f not in used and f != COMMON_RULES]

    corrections = load_corrections() + note_corrections

    timeline = [{'time': r.get('time'), 'type': r.get('type'), 'label': label_for(r),
                 **({'agent_id': r['agent_id']} if r.get('agent_id') else {})}
                for r in records]

    generated = records[-1]['time'] if records else None

    log = {
        'project': PROJECT,
        'generated': generated,
        'generated_note': 'Time of the newest coordinator note; the log is rebuilt from the notes by work/tools/build_log.py.',
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
    print('wrote %s and %s: %d notes, %d agents, %d decisions, %d corrections, %d web sources'
          % (rel(OUT_JSON), rel(OUT_JS), len(records), len(order), len(decisions),
             len(corrections), len(web_sources)))


if __name__ == '__main__':
    main()
