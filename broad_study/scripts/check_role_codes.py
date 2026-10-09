"""Print whether codes are in a role catalog."""
import json, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
cat = json.loads((root/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
role = sys.argv[1]
codes = sys.argv[2].split(',')
by = {x['code']: x for x in cat['labels']}
out = []
for c in codes:
    d = by.get(c)
    if not d:
        out.append('MISSING '+c)
    elif role in d['applicable_roles']:
        out.append('IN '+c)
    else:
        out.append('OUT '+c+' roles='+','.join(d['applicable_roles']))
print('\n'.join(out))
