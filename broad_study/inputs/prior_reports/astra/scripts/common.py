from pathlib import Path
import csv,json,hashlib,statistics,collections,itertools
ROOT=Path(__file__).resolve().parents[1]
C=ROOT/'inputs/stage_c';A=C/'inputs/rules_v1/inputs/stage_a';B=ROOT/'inputs/stage_b'
def read(p): return list(csv.DictReader(Path(p).open(encoding='utf-8-sig',newline='')))
def dump(name,rs):
 p=ROOT/'tables'/name;p.parent.mkdir(exist_ok=True,parents=True)
 if not rs: p.write_text('',encoding='utf-8-sig');return
 fields=list(dict.fromkeys(k for r in rs for k in r))
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fields);w.writeheader();w.writerows(sorted(rs,key=lambda r:json.dumps(r,ensure_ascii=False,sort_keys=True)))
def js(x):return json.dumps(x,ensure_ascii=False,sort_keys=True)
def ratio(p,n):return p/n if n else None
def lock_check():
 for rel,v in json.loads((ROOT/'input_lock.json').read_text(encoding='utf-8'))['files'].items():
  assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==v['sha256'], 'INPUT_DRIFT '+rel
jobs=read(A/'jobs.csv');J={x['identity_key']:x for x in jobs};assert len(J)==1654
raw=[json.loads(x) for x in (ROOT/'inputs/accepted_jobs.jsonl').read_text(encoding='utf-8').splitlines()];RAW={x['identity_key']:x for x in raw};assert set(RAW)==set(J)
companies=read(C/'tables/T1_company_sample.csv');CO={x['company_id']:x for x in companies}
ALL=sorted(CO);WHOLE=[c for c in ALL if CO[c]['scope_main_company']=='YES']
FULL=[c for c in WHOLE if CO[c]['activities_SOURCE_UNASSESSABLE']=='0']
role_rows=read(C/'tables/T2_company_primary_roles.csv')
def role(j):return j['primary_code'] if j['primary_status']=='CODED' else 'STATUS_'+j['primary_status']
RN={role(j):j['primary_name'] if j['primary_status']=='CODED' else j['primary_status'] for j in jobs}
ROLES=sorted(RN);CONCRETE=[r for r in ROLES if r.startswith('RF_') and r not in ['RF_COMPOSITE_ROLE','RF_ALTERNATIVE_DIRECTIONS','RF_COMPOSITE']]
# Derive the structural code exclusion from the authoritative 30 trees as well.
structures=read(C/'tables/T4_role_structures.csv');ST={r['identity_key']:r for r in structures}
CONCRETE=[r for r in CONCRETE if r not in {s['primary_code'] for s in structures}]
activities=read(C/'tables/T4_activity_lineage.csv');AN={r['label_code']:r['label_name'] for r in activities};ACTS=sorted(AN)
admitted={j['identity_key'] for j in jobs if j['activities_status'] in ['CODED','NOT_MENTIONED']}
OWN={a:set() for a in ACTS};PART={a:set() for a in ACTS};AE=collections.defaultdict(list)
for r in activities:
 (OWN if r['relation']=='OWNED' else PART)[r['label_code']].add(r['identity_key'])
 AE[(r['identity_key'],r['label_code'],r['relation'])].append(r)
def ids(cs,eligible=False):return {k for k,j in J.items() if j['company_id'] in cs and (not eligible or k in admitted)}
def distribution(points):
 valid=[(c,p,n) for c,p,n in points if n];rates=[p/n for c,p,n in valid]
 positive=sum(p for c,p,n in valid);den=sum(n for c,p,n in valid)
 quart=statistics.quantiles(rates,n=4,method='inclusive') if len(rates)>1 else rates*3
 dp=max(valid,key=lambda x:x[2]) if valid else ('',0,0);pp=max(valid,key=lambda x:x[1]) if positive else ('',0,0)
 return {'n_base_companies':len(points),'n_interpretable_companies':len(valid),'n_positive_companies':sum(p>0 for c,p,n in valid),'P':positive,'N':den,'company_equal':statistics.mean(rates) if rates else None,'ad_weighted':ratio(positive,den),'median':statistics.median(rates) if rates else None,'q25':quart[0] if rates else None,'q75':quart[2] if rates else None,'max_den_company':dp[0],'max_den_contribution':ratio(dp[2],den),'max_positive_company':pp[0],'max_positive_contribution':ratio(pp[1],positive),'den_concentrated_over50':ratio(dp[2],den)>0.5 if den else None}
