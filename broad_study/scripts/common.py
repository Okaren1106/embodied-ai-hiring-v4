from pathlib import Path
from collections import Counter,defaultdict
import csv,json,hashlib,statistics,re
ROOT=Path(__file__).resolve().parents[1]
C=ROOT/'inputs/stage_c';A=C/'inputs/rules_v1/inputs/stage_a';B=ROOT/'inputs/stage_b'
def read(p):
    with Path(p).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def js(x):return json.dumps(x,ensure_ascii=False,sort_keys=True)
def dump(name,rows):
    p=ROOT/name;p.parent.mkdir(exist_ok=True,parents=True)
    if not rows:raise ValueError('Empty table requires explicit schema: '+name)
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def save_json(name,data):
    p=ROOT/name;p.parent.mkdir(exist_ok=True,parents=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
def lock_check(originals=False):
    m=json.loads((ROOT/'input_manifest.json').read_text(encoding='utf-8'))
    for r in m['files']:
        p=ROOT/r['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],'INPUT_DRIFT '+r['path']
        if originals:assert hashlib.sha256(Path(r['source']).read_bytes()).hexdigest()==r['sha256'],'ORIGINAL_DRIFT '+r['source']
    return len(m['files'])
jobs=read(A/'jobs.csv');J={r['identity_key']:r for r in jobs}
RAW={r['identity_key']:r for r in (json.loads(x) for x in (ROOT/'inputs/accepted_jobs.jsonl').read_text(encoding='utf-8').splitlines())}
assert len(J)==1654 and set(J)==set(RAW)
CO={r['company_id']:r for r in read(C/'tables/T1_company_sample.csv')}
ALL=sorted(CO);WHOLE=[c for c in ALL if CO[c]['scope_main_company']=='YES']
assert len(ALL)==24 and len(WHOLE)==23
admitted={k for k,j in J.items() if j['activities_status'] in ['CODED','NOT_MENTIONED']}
structures=read(C/'tables/T4_role_structures.csv');ST={r['identity_key']:r for r in structures}
def role(j):return j['primary_code'] if j['primary_status']=='CODED' else 'STATUS_'+j['primary_status']
RN={role(j):j['primary_name'] if j['primary_status']=='CODED' else j['primary_status'] for j in jobs}
CONCRETE=sorted(r['class_code'] for r in read(C/'tables/T2_company_primary_roles.csv') if r['class_kind']=='concrete')
CONCRETE=sorted(set(CONCRETE));assert len(CONCRETE)==17
activities=read(C/'tables/T4_activity_lineage.csv');AN={r['label_code']:r['label_name'] for r in activities};ACTS=sorted(AN)
OWN={a:set() for a in ACTS};PART={a:set() for a in ACTS};AE=defaultdict(list)
for r in activities:
    assert r['relation'] in ['OWNED','PARTICIPATES']
    (OWN if r['relation']=='OWNED' else PART)[r['label_code']].add(r['identity_key']);AE[r['identity_key'],r['label_code'],r['relation']].append(r)
def ratio(p,n):return p/n if n else None
def ids(cs,eligible=False):return {k for k,j in J.items() if j['company_id'] in cs and (not eligible or k in admitted)}
def summary(points):
    # tuples company, P, U, B; genuine zero denominators never become zero rates
    vals=[(c,p,u,b,b-u) for c,p,u,b in points];valid=[v for v in vals if v[4]>0]
    p=sum(v[1] for v in vals);u=sum(v[2] for v in vals);b=sum(v[3] for v in vals);n=b-u
    assert 0<=p<=n and n>=0
    maxp=max((v[1] for v in vals),default=0);maxn=max((v[4] for v in vals),default=0)
    return dict(P=p,U=u,Z=n-p,B=b,N=n,n_valid_companies=len(valid),n_positive_companies=sum(v[1]>0 for v in vals),company_equal=statistics.mean(v[1]/v[4] for v in valid) if valid else None,ad_weighted=ratio(p,n),unknown_low=ratio(p,b),unknown_high=ratio(p+u,b),max_positive_companies=js([v[0] for v in vals if v[1]==maxp]) if p else '[]',max_positive_count=maxp if p else None,max_positive_contribution=ratio(maxp,p),max_den_companies=js([v[0] for v in vals if v[4]==maxn]) if n else '[]',max_den_count=maxn if n else None,max_den_contribution=ratio(maxn,n),group_eligible=len(valid)>=3 and n>=20)
def locate(k,r):
    q=r.get('quote','');field=r.get('field','');txt=RAW[k].get(field,'') or ''
    start=r.get('start','');end=r.get('end','')
    if q and str(start).isdigit():
        s=int(start)
        if str(end).isdigit() and txt[s:int(end)]==q:return dict(field=field,start=s,end=int(end),method='EXACT_OFFSETS',quote=q)
        if txt[s:s+len(q)]==q:return dict(field=field,start=s,end=s+len(q),method='RECOVER_END_FROM_QUOTE',quote=q)
    fields=list(dict.fromkeys([field,'duties','requirements','full_description']))
    for f in fields:
        t=RAW[k].get(f,'') or ''
        if q and t.count(q)==1:
            s=t.index(q);return dict(field=f,start=s,end=s+len(q),method='UNIQUE_EXACT_QUOTE',quote=q)
    if q:
        pattern=r'\s+'.join(re.escape(s) for s in q.split())
        for f in fields:
            t=RAW[k].get(f,'') or '';matches=list(re.finditer(pattern,t))
            if len(matches)==1:
                m=matches[0];return dict(field=f,start=m.start(),end=m.end(),method='UNIQUE_WHITESPACE_MATCH',quote=m.group())
    return dict(field=field,start=start,end=end,method='UNRESOLVED_LOCATION',quote=q)
