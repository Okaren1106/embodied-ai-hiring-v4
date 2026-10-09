"""Find ads whose candidate quote has 串口/RS232/RS485 but V2_RS485 was not kept."""
import json
from common import ROOT
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
rs_roles={r for x in cat['labels'] if x['code']=='V2_RS485' for r in x['applicable_roles']}
queue=json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'))
qindex={(r['identity_key'], r['review_id'].split(':')[-1]): r for r in queue}
needles=('串口','RS232','RS-232','RS485','RS-485','RS 485')
miss=[]
for p in sorted((ROOT/'configs/Q_adjudications').glob('*.json')):
    role=p.stem
    if role not in rs_roles: continue
    data=json.loads(p.read_text(encoding='utf-8'))
    for store,a in data['ads'].items():
        k=a['identity_key']
        for ni,act in (a.get('new') or {}).items():
            rec=qindex.get((k,ni))
            if not rec: continue
            q=rec.get('quote') or ''
            if not any(n in q for n in needles): continue
            kept=[]
            if isinstance(act,list):
                kept=[x[0] for x in act]
            if 'V2_RS485' in kept: continue
            miss.append('%s %s cand%s act=%s | %s'%(role,store,ni, (act if isinstance(act,str) else kept)[:80] if isinstance(act,str) else ','.join(kept), q[:90].replace('\n',' ')))
(ROOT/'notes/rs485_missed.txt').write_text('\n'.join(miss) if miss else 'NONE', encoding='utf-8')
print('missed', len(miss))
