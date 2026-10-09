"""Locate all old_overrides quotes."""
import json
from pathlib import Path
from common import locate
root = Path(__file__).resolve().parents[1]
bad=[]
for p in sorted((root/'configs/Q_adjudications').glob('*.json')):
    data=json.loads(p.read_text(encoding='utf-8'))
    for store,a in data['ads'].items():
        k=a['identity_key']
        for oid,ov in (a.get('old_overrides') or {}).items():
            q=ov.get('quote') or ''
            loc=locate(k,ov if q else dict(quote=q))
            if loc['method']=='UNRESOLVED_LOCATION':
                bad.append('%s %s %s | %s' % (store, oid, loc['method'], q[:120]))
out=root/'notes/override_locate_bad.txt'
out.write_text('\n'.join(bad) if bad else 'NONE', encoding='utf-8')
print('bad', len(bad))
