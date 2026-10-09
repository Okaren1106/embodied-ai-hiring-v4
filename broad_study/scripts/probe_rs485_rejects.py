"""Find 串口/RS232/RS485 REJECT decisions in roles where V2_RS485 applies."""
import json, csv
from collections import defaultdict
from pathlib import Path
from common import ROOT
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
rs_roles={r for x in cat['labels'] if x['code']=='V2_RS485' for r in x['applicable_roles']}
queue=[]
for rec in json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8')):
    queue.append(rec)
qindex={(r['identity_key'], r['review_id'].split(':')[-1]): r for r in queue}
# also by reading_id
qindex_rid={(r['reading_id'], r['review_id'].split(':')[-1]): r for r in queue}
hits=[]
for p in sorted((ROOT/'configs/Q_adjudications').glob('*.json')):
    data=json.loads(p.read_text(encoding='utf-8'))
    role=p.stem
    if role not in rs_roles:
        continue
    for store,a in data['ads'].items():
        k=a['identity_key']; rid=a.get('reading_id') or store
        for ni, act in (a.get('new') or {}).items():
            if not isinstance(act,str) or not act.startswith('REJECT:'):
                continue
            if '串口' not in act and 'RS485' not in act and 'RS-485' not in act and 'RS232' not in act:
                continue
            rec=qindex.get((k,ni)) or qindex_rid.get((rid,ni)) or {}
            q=(rec.get('quote') or '')
            hits.append('%s %s cand%s | %s | %s'%(role, store, ni, act[:80], q[:80].replace('\n',' ')))
out=ROOT/'notes/rs485_reject_hits.txt'
out.write_text('\n'.join(hits) if hits else 'NONE', encoding='utf-8')
print('hits', len(hits), 'roles', len(rs_roles))
