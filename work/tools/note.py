"""Coordinator's append-only handoff notes. The Scribe agent folds these into build-log/log.json.
Usage: python3 work/tools/note.py <type> '<json object>'   (type: decision|agent_start|agent_finish|handoff|review|web_source|correction)"""
import json, sys, datetime
rec = {"time": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), "type": sys.argv[1]}
rec.update(json.loads(sys.argv[2]))
open('build-log/inbox.jsonl', 'a').write(json.dumps(rec, ensure_ascii=False) + '\n')
print('noted', rec['type'])
