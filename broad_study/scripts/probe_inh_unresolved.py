"""Inherited unresolved after effective override quote."""
import json
from collections import defaultdict
from pathlib import Path
from common import locate
root = Path(__file__).resolve().parents[1]
old=json.loads((root/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
obk=defaultdict(list)
for r in old: obk[r['identity_key']].append(r)
bad=[]
empty_ov_unresolved=[]
for p in sorted((root/'configs/Q_adjudications').glob('*.json')):
    data=json.loads(p.read_text(encoding='utf-8'))
    for store,a in data['ads'].items():
        k=a['identity_key']
        inh=obk[k]
        for i,r in enumerate(inh,1):
            override=(a.get('old_overrides') or {}).get(f'O{i}')
            q=(override or {}).get('quote') if override else None
            if q:
                loc=locate(k, override)
                if loc['method']=='UNRESOLVED_LOCATION':
                    bad.append('QUOTE %s O%s %s | %s'%(store,i,r.get('code'),q[:120]))
            else:
                loc=locate(k,r)
                if loc['method']=='UNRESOLVED_LOCATION':
                    empty_ov_unresolved.append('%s O%s %s ov=%s orig_q=%s'%(store,i,r.get('code'), bool(override), (r.get('quote') or '')[:80]))
out=root/'notes/inh_unresolved_detail.txt'
lines=['QUOTE_FAIL %d'%len(bad)]+bad+['','EMPTY_OR_NO_OV_UNRESOLVED %d'%len(empty_ov_unresolved)]+empty_ov_unresolved
out.write_text('\n'.join(lines), encoding='utf-8')
print('quote_fail', len(bad), 'unresolved_no_quote', len(empty_ov_unresolved))
