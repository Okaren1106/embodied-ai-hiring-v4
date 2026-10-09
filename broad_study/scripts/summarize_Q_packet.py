"""Dump compact candidate + empty-inherited index for a packet JSON."""
import json,sys
from pathlib import Path
p=Path(sys.argv[1])
data=json.loads(p.read_text(encoding='utf-8'))
out=[]
for ad in data:
    empty=[x for x in ad['inherited'] if not x.get('field')]
    cands=[{'id':c['id'],'codes':c['codes'],'quote':c['quote'][:180],'surface':(c.get('surface') or '')[:80]} for c in ad['candidates']]
    out.append({'order':ad['coding_order'],'rid':ad['reading_id'],'title':ad['title'],'n_inherited':len(ad['inherited']),'empty':[{'id':x['id'],'code':x['code'],'quote':x['quote']} for x in empty],'cands':cands})
Path(sys.argv[2]).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print('ads',len(out),'empty_fields',sum(len(x['empty']) for x in out),'cands',sum(len(x['cands']) for x in out))
