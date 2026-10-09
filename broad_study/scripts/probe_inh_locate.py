"""Find inherited items that still cannot locate after overrides."""
import json
from collections import defaultdict
from pathlib import Path
from common import locate, RAW
root = Path(__file__).resolve().parents[1]
old=json.loads((root/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
obk=defaultdict(list)
for r in old:
    obk[r['identity_key']].append(r)
bad=[]
for p in sorted((root/'configs/Q_adjudications').glob('*.json')):
    data=json.loads(p.read_text(encoding='utf-8'))
    for store,a in data['ads'].items():
        k=a['identity_key']; rid=a.get('reading_id') or store
        inh=obk[k]
        for i,r in enumerate(inh,1):
            override=(a.get('old_overrides') or {}).get(f'O{i}')
            if override and override.get('quote'):
                loc=locate(k, override)
                src='OV'
            else:
                loc=locate(k, r)
                src='INH'
            if loc['method']=='UNRESOLVED_LOCATION':
                q=(override.get('quote') if override else r.get('quote')) or ''
                bad.append('%s %s O%s %s %s | %s' % (store, r.get('code'), i, src, loc['method'], q[:100]))
out=root/'notes/inh_locate_bad.txt'
out.write_text('\n'.join(bad) if bad else 'NONE', encoding='utf-8')
print('bad', len(bad))
