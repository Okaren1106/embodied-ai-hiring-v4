"""Suggest unique quotes for empty inherited fields."""
import json,sys,re
from pathlib import Path
p=Path(sys.argv[1])
data=json.loads(p.read_text(encoding='utf-8'))
for ad in data:
    txt=ad['fields'].get('full_description') or ''
    empties=[x for x in ad['inherited'] if not x.get('field')]
    if not empties: continue
    print('===',ad['reading_id'],ad['title'])
    for x in empties:
        q=x['quote']
        idxs=[m.start() for m in re.finditer(re.escape(q), txt)]
        print(' ',x['id'],x['code'],repr(q),'hits',len(idxs))
        if idxs:
            i=idxs[0]
            snippet=txt[max(0,i-40):i+len(q)+60].replace('\n',' ')
            print('   snip:',snippet)
