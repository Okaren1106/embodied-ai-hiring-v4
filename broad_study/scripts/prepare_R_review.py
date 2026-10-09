from common import *
lock_check()
dsv=read(ROOT/'inputs/prior_reports/dsv/tables/D4_activity_pair_lineage.csv')
print('DSV states',Counter(r['status'] for r in dsv))
disputed=[r for r in dsv if r['status'] in ['UNRESOLVED','UNKNOWN']]
print('disputed',len(disputed),len({r['identity_key'] for r in disputed}))
assert len(disputed)==20 and len({r['identity_key'] for r in disputed})==15
pack=[];evidence=[]
for k in sorted({r['identity_key'] for r in disputed},key=lambda k:J[k]['reading_id']):
    j=J[k];raw=RAW[k];rows=[r for r in disputed if r['identity_key']==k]
    item={'identity_key':k,'reading_id':j['reading_id'],'company_id':j['company_id'],'title':j['title'],'tree':ST.get(k,{}),'pairs':rows,'activity_evidence':{}}
    for act in sorted({r[x] for r in rows for x in ['activity_a','activity_b']}):
        item['activity_evidence'][act]=[dict(original=e,recovered=locate(k,e)) for e in AE[k,act,'OWNED']]
        for e in item['activity_evidence'][act]:evidence.append({'identity_key':k,'reading_id':j['reading_id'],'activity':act,**e['recovered'],'original_end':e['original'].get('end','')})
    item['duties']=raw.get('duties','');item['requirements']=raw.get('requirements','')
    full=raw.get('full_description','') or ''
    if full not in [item['duties'],item['requirements']]:item['full_description']=full
    pack.append(item)
save_json('notes/R2_disputed_full_packet.json',pack)
dump('tables/R2_evidence_recovery.csv',evidence)
for ix in range(0,len(pack),5):
    out=[]
    for x in pack[ix:ix+5]:
        out.extend([f"## {x['reading_id']} {x['company_id']} {x['title']}",f"identity {x['identity_key']}",f"TREE {x['tree'].get('tree_json')}"])
        for a,ev in x['activity_evidence'].items():out.append(a+' '+js([e['recovered'] for e in ev]))
        for f in ['duties','requirements','full_description']:
            if x.get(f):out.extend([f.upper(),x[f]])
    (ROOT/f'notes/R2_read_batch_{ix//5+1}.md').write_text('\n\n'.join(out),encoding='utf-8')
mixed=[]
for k,s in ST.items():
    if s['has_mixed_branch']=='YES':mixed.append({'identity_key':k,'reading_id':J[k]['reading_id'],'structure':s,'raw':RAW[k],'owned':[a for a in ACTS if k in OWN[a]]})
save_json('notes/R2_mixed_tree_packet.json',mixed)
print('recovery',Counter(e['method'] for e in evidence),'mixed',[(x['reading_id'],x['owned']) for x in mixed])
print('source packets',[(p.name,p.stat().st_size) for p in (ROOT/'notes').glob('R2_read_batch*')])
