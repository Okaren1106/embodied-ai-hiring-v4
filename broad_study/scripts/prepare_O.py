from common import *
import random
frame=read(ROOT/'inputs/protocol_v2/tables/planning_object_frame.csv');kk=[r['identity_key'] for r in frame];assert len(kk)==84 and len(set(kk))==84
groups=defaultdict(list)
for k in kk:groups[J[k]['company_id'],role(J[k])].append(k)
rng=random.Random(20260916);pilot=[]
for g,v in sorted(groups.items()):pilot.extend(rng.sample(sorted(v),min(2,len(v))))
ordered=pilot+sorted(set(kk)-set(pilot),key=lambda k:(J[k]['company_id'],role(J[k]),J[k]['reading_id']))
pack=[]
for n,k in enumerate(ordered,1):
    raw=RAW[k];j=J[k];parts=[]
    for f in ['duties','requirements','full_description']:
        t=raw.get(f,'') or ''
        if t and not any(t==old for _,old in parts):parts.append((f,t))
    pack.append({'seq':n,'identity_key':k,'reading_id':j['reading_id'],'company_id':j['company_id'],'role':role(j),'title':j['title'],'pilot':k in pilot,'fields':dict(parts)})
save_json('notes/O_full_reading_packet.json',pack)
dump('tables/O1_frame.csv',[{k:v for k,v in r.items() if k!='fields'} for r in pack])
for start in range(0,84,8):
    texts=[]
    for r in pack[start:start+8]:texts.append(f"### {r['seq']:02d} {r['reading_id']} {r['company_id']} {r['role']} {r['title']}\n"+'\n'.join(f'[{f}]\n{t}' for f,t in r['fields'].items()))
    (ROOT/f'notes/O_read_{start//8+1:02d}.md').write_text('\n\n'.join(texts),encoding='utf-8')
print('pilot',[(p['seq'],p['reading_id']) for p in pack if p['pilot']]);print('batches',[(p.name,p.stat().st_size) for p in sorted((ROOT/'notes').glob('O_read_*.md'))])
