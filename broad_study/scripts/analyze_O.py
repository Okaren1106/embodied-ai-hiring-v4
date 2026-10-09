from common import *
import sys,random
sys.path.insert(0,str(ROOT/'configs'))
from O_manual import D
packet=json.loads((ROOT/'notes/O_full_reading_packet.json').read_text(encoding='utf-8'));codebook=json.loads((ROOT/'configs/O_codebook_v2.json').read_text(encoding='utf-8'));assert set(D)==set(range(1,85))
rows=[];evidence=[];links=[];status=[];problems=[];seqs={r['identity_key']:r['seq'] for r in packet}
def ev(k,kind,val,quote,relation='',note=''):
    # Include title for explicit named product/team in title; preserve the field actually matched.
    loc=locate(k,dict(field='duties',quote=quote))
    if loc['method']=='UNRESOLVED_LOCATION' and quote in J[k]['title']:
        s=J[k]['title'].index(quote);loc=dict(field='title',start=s,end=s+len(quote),method='TITLE_EXACT',quote=quote)
    if loc['method']=='UNRESOLVED_LOCATION':problems.append((seqs[k],kind,quote))
    row=dict(evidence_id=f'O_E{len(evidence)+1:04}',identity_key=k,reading_id=J[k]['reading_id'],company_id=J[k]['company_id'],role=role(J[k]),field_type=kind,value=val,responsibility=relation,evidence_strength='EXPLICIT',**loc,note=note,source_url=J[k]['source_url'],version=codebook['version']);evidence.append(row);return row
for r in packet:
    n=r['seq'];k=r['identity_key'];d=D[n]
    for code,quote,rel in d['objects']:ev(k,'OBJECT',code,quote,rel,d['task'])
    for label,quote in d['product']:ev(k,'PRODUCT_OR_UNIT',label,quote)
    for quote in d['years']:ev(k,'EXPERIENCE_RAW',quote,quote,note='PREFERRED' if n==81 else 'STATED_REQUIREMENT; preserve any alternatives within quote')
    for quote in d['degree']:ev(k,'DEGREE_RAW',quote,quote,note='PREFERRED' if n==81 else 'STATED_REQUIREMENT; degree alternatives retained')
    ev(k,'TITLE_RAW',r['title'],r['title'])
    for skill,task,quote,context in d['links']:
        e=ev(k,'SKILL_TASK_LINK',skill,quote,context,task);links.append({**e,'skill_or_method':skill,'task':task,'link_context':context,'scope':'Explicit local link recorded; not a measure of actual employee use'})
    full='\n'.join([r['title']]+list(r['fields'].values()))
    # This finite O sample was fully read. Detection here records explicit text only, never infers junior/senior.
    aud=[]
    if '实习' in r['title'] or re.search(r'\bintern(ship)?\b',r['title'],re.I):aud.append('INTERNSHIP')
    if re.search(r'27届|校招',r['title']) or n in [32,37]:aud.append('CAMPUS_OR_GRADUATE')
    snippets=[]
    for f,t in r['fields'].items():
        if f=='requirements' and t in r['fields'].get('duties',''):continue
        for ln in t.splitlines():
            if re.search('应届|校招|在校生|在读|每周5天实习|2027 届|27届',ln):snippets.append(ln)
    for sn in dict.fromkeys(snippets):ev(k,'AUDIENCE_RAW','TEXT_EXPLICIT',sn)
    status.append(dict(seq=n,identity_key=k,reading_id=r['reading_id'],company_id=r['company_id'],role=r['role'],title=r['title'],pilot=r['pilot'],processing_status='FULL_TEXT_CODED',objects_state='READABLE',product_state='EXPLICIT' if d['product'] else 'UNKNOWN',product_count=len(d['product']),n_object_values=len(set(o[0] for o in d['objects'])),years_state='STATED' if d['years'] else 'NOT_STATED',degree_state='STATED' if d['degree'] else 'NOT_STATED',audience=js(aud),n_explicit_skill_links=len(d['links']),task=d['task'],note=d['note'],seniority_inferred='NO',reviewer='Astra first pass'))
    for obj in codebook['objects']:
        oo=[o for o in d['objects'] if o[0]==obj]
        for rb in ['ANY_RESPONSIBILITY','OWNED','PARTICIPATES']:
            positive=bool(oo) if rb=='ANY_RESPONSIBILITY' else any(o[2]==rb for o in oo)
            rows.append(dict(identity_key=k,reading_id=r['reading_id'],company_id=r['company_id'],role=r['role'],object=obj,responsibility=rb,state='P' if positive else 'Z',note='Z=全文可读但未记录此对象/责任；不是公司没有这种工作'))
save_json('verification/O_unresolved_quotes.json',problems)
if problems:
    print('UNRESOLVED',js(problems));raise SystemExit(1)
dump('tables/O1_processing_status.csv',status);dump('tables/O2_evidence_long.csv',evidence);dump('tables/O2_object_states.csv',rows);dump('tables/O3_skill_task_links.csv',links)
groups=sorted({(r['company_id'],r['role']) for r in packet});stats=[];sensitivity=[];missing=[]
S={r['identity_key']:r for r in status}
# Exact duties after trimming whitespace; identical bodies remain distinct in main results.
dedup=set();seen=set();dups=[]
for r in sorted(packet,key=lambda r:r['identity_key']):
    k=r['identity_key'];key=(r['company_id'],r['role'],re.sub(r'\s+',' ',RAW[k].get('duties','')).strip())
    if key[2] and key in seen:dups.append({'identity_key':k,'reading_id':r['reading_id'],'company_id':r['company_id'],'role':r['role']})
    else:dedup.add(k)
    seen.add(key)
if dups:dump('tables/O_exact_duplicate_exclusions.csv',dups)
for c,f in groups:
    kk={r['identity_key'] for r in packet if (r['company_id'],r['role'])==(c,f)}
    for o in codebook['objects']:
        for rel in ['ANY_RESPONSIBILITY','OWNED','PARTICIPATES']:
            pp={r['identity_key'] for r in rows if r['company_id']==c and r['role']==f and r['object']==o and r['responsibility']==rel and r['state']=='P'}
            base=dict(company_id=c,role=f,object=o,responsibility=rel,P=len(pp),U=0,B=len(kk),N=len(kk),share=ratio(len(pp),len(kk)),small_n=len(kk)<10)
            stats.append(base)
            for sn,allow in [('FULL',kk),('EXCLUDE_CAMPUS_INTERNSHIP',{k for k in kk if S[k]['audience']=='[]'}),('EXACT_DUTY_DEDUP',kk&dedup),('EXPLICIT_PRODUCT_ONLY',{k for k in kk if S[k]['product_state']=='EXPLICIT'}),('STATED_YEARS_ONLY',{k for k in kk if S[k]['years_state']=='STATED'})]:
                sensitivity.append({**base,'scenario':sn,'P':len(pp&allow),'B':len(allow),'N':len(allow),'share':ratio(len(pp&allow),len(allow)),'status':'POINT_ONLY_SMALL_N' if 0<len(allow)<10 else 'NA_NO_DENOMINATOR' if not allow else 'DESCRIPTIVE'})
    missing.append(dict(company_id=c,role=f,frame_N=len(kk),product_explicit=sum(S[k]['product_state']=='EXPLICIT' for k in kk),product_direct_link=0,product_unknown=sum(S[k]['product_state']=='UNKNOWN' for k in kk),years_stated=sum(S[k]['years_state']=='STATED' for k in kk),degree_stated=sum(S[k]['degree_state']=='STATED' for k in kk),campus_or_intern=sum(S[k]['audience']!='[]' for k in kk),ads_with_skill_link=sum(int(S[k]['n_explicit_skill_links'])>0 for k in kk)))
dump('tables/O4_company_role_object.csv',stats);dump('tables/O4_sensitivity.csv',sensitivity);dump('tables/O4_attribution_seniority_unknown.csv',missing)
# Same-object comparison: still descriptive, matching a broad object is not exact task matching.
same=[]
for f in sorted({r['role'] for r in packet}):
    for o in codebook['objects']:
        for c in sorted({r['company_id'] for r in packet}):
            kk={r['identity_key'] for r in rows if r['company_id']==c and r['role']==f and r['object']==o and r['responsibility']=='ANY_RESPONSIBILITY' and r['state']=='P'}
            for a in ACTS:same.append(dict(company_id=c,role=f,object=o,activity=a,P=len(kk&OWN[a]),N=len(kk&admitted),share=ratio(len(kk&OWN[a]),len(kk&admitted)),status='NA' if not kk else 'POINT_ONLY_SMALL_N' if len(kk)<10 else 'DESCRIPTIVE',limit='同对象不必然同任务，原活动对象范围依A01'))
dump('tables/O4_same_object_activity.csv',same)
checks={'frame_84':len(status)==84,'object_cells':len(rows)==84*8*3,'all_exact_evidence':not problems,'unknown_not_product':all(not D[r['seq']]['product'] for r in status if r['product_state']=='UNKNOWN'),'no_original_reclassification':lock_check()==909,'counts_by_cell':missing}
assert all(v for k,v in checks.items() if k!='counts_by_cell');save_json('verification/O_program_checks.json',checks)
print('O outputs',len(status),'ads',len(evidence),'evidence',len(links),'links');print(js(missing))
