"""Rebuild v4 company eligibility and comparisons from advertisement states.

The definitions follow the frozen v3 fixed-base protocol (min M/G/Q evaluable
counts, exact rational signs), implemented here without importing old or new
production aggregation modules. The same code first reconstructs the frozen v3
comparison file, then applies the v4 overlay and all seven semantic switches.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
import csv,json,itertools,hashlib

ROOT=Path(__file__).resolve().parents[2]
SNAP=ROOT/'source_snapshot'
OUT=ROOT/'analysis/empirical'
ORDER=['SK_PYTHON','SK_PYTORCH','SK_CPP','SK_LINUX','SK_ALTIUM','V2_EMC_SIPI']
CATS=['SUPPORTED_RETENTION','SUPPORTED_REVERSAL','CONDITIONAL_REVERSAL_OVERLAP','CONDITIONAL_RETENTION_OVERLAP','MENTION_TIE','CONDITIONAL_TIE_OVERLAP']

def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def write(name,rows):
    assert rows,name
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def sign(x):return (x>0)-(x<0)
def pkey(p):return int(p['threshold']),p['task'],p['label_code'],p['company_a'],p['company_b']

def aggregate(rows):
    b=len(rows);d={'B':b,'M_P':sum(int(r['M']) for r in rows),'M_N':b}
    d['M_share']=float(F(d['M_P'],b))
    for m in ['G','R','Q']:
        c=Counter(r[m] for r in rows);p,z,u=c['P'],c['Z'],c['U'];n=b-u
        d.update({m+'_P':p,m+'_Z':z,m+'_U':u,m+'_N':n,m+'_confirmed':float(F(p,b)),
                  m+'_conditional':float(F(p,n)) if n else '',m+'_lo':float(F(p,b)),
                  m+'_hi':float(F(p+u,b)),m+'_unresolved_share':float(F(u,b))})
    return d

def cells(rows):
    groups=defaultdict(list)
    for r in rows:groups[r['task'],r['label_code'],r['company_id']].append(r)
    result=[]
    for (task,label,firm),rr in sorted(groups.items()):
        c={'task':task,'label_code':label,'company_id':firm,'company_name':rr[0]['company_name'],**aggregate(rr)}
        for n in [5,10]:
            c['eligible_'+str(n)]=int(min(c['M_N'],c['G_N'],c['Q_N'])>=n)
            c['B_only_eligible_'+str(n)]=int(c['B']>=n)
        result.append(c)
    return result

def comparison(a,b,n):
    out={'threshold':n,'task':a['task'],'label_code':a['label_code'],'company_a':a['company_id'],'company_b':b['company_id'],
         'name_a':a['company_name'],'name_b':b['company_name']}
    for prefix,c in [('A',a),('B',b)]:
        for k in ['B','M_P','M_N','G_P','G_U','G_N','Q_P','Q_U','Q_N']:out[prefix+'_'+k]=c[k]
    mgap=F(a['M_P'],a['B'])-F(b['M_P'],b['B']);md=sign(mgap)
    out.update(M_gap_pp=float(100*mgap),M_direction=md)
    for measure in ['G','Q']:
        confirmed=F(a[measure+'_P'],a['B'])-F(b[measure+'_P'],b['B'])
        conditional=F(a[measure+'_P'],a[measure+'_N'])-F(b[measure+'_P'],b[measure+'_N'])
        low=F(a[measure+'_P'],a['B'])-F(b[measure+'_P']+b[measure+'_U'],b['B'])
        high=F(a[measure+'_P']+a[measure+'_U'],a['B'])-F(b[measure+'_P'],b['B'])
        direction=1 if low>0 else -1 if high<0 else 0
        assert low<=confirmed<=high and low<=conditional<=high
        out.update({measure+'_confirmed_gap_pp':float(100*confirmed),measure+'_conditional_gap_pp':float(100*conditional),
                    measure+'_difference_lo_pp':float(100*low),measure+'_difference_hi_pp':float(100*high),
                    measure+'_confirmed_direction':sign(confirmed),measure+'_conditional_direction':sign(conditional),
                    measure+'_bounds_direction':direction,measure+'_bounds_touch_zero':int(low==0 or high==0),
                    measure+'_bounds_straddle_zero':int(low<0<high)})
        if measure=='Q':cq,condq,loq,hiq,bd=confirmed,conditional,low,high,direction
    qd=sign(condq)
    if md==0:category='MENTION_TIE'
    elif bd:category='SUPPORTED_RETENTION' if bd==md else 'SUPPORTED_REVERSAL'
    elif qd==0:category='CONDITIONAL_TIE_OVERLAP'
    elif qd==md:category='CONDITIONAL_RETENTION_OVERLAP'
    else:category='CONDITIONAL_REVERSAL_OVERLAP'
    out.update(classification=category,conditional_point_reversal=int(md*qd==-1),
               confirmed_share_reversal=int(md*sign(cq)==-1),
               conditioning_dependent_point_reversal=int(md*qd==-1 and md*sign(cq)!=-1),
               recorded_share_change_pp=float(100*(cq-mgap)),conditioning_increment_pp=float(100*(condq-cq)),
               total_M_to_conditional_change_pp=float(100*(condq-mgap)))
    return out

def pairs(cs):
    out=[]
    for n in [5,10]:
        for label in ORDER:
            eligible=sorted([c for c in cs if c['label_code']==label and c['eligible_'+str(n)]],key=lambda c:c['company_id'])
            out.extend(comparison(a,b,n) for a,b in itertools.combinations(eligible,2))
    return out

def summaries(ps,cs):
    out=[]
    for n in [5,10]:
        for label in ORDER+['ALL']:
            pp=[p for p in ps if p['threshold']==n and (label=='ALL' or p['label_code']==label)]
            cc=[c for c in cs if label=='ALL' or c['label_code']==label];count=Counter(p['classification'] for p in pp)
            out.append({'threshold':n,'label_code':label,'pairs':len(pp),
                        'eligible_cells':sum(c['eligible_'+str(n)] for c in cc),
                        'B_only_eligible_cells':sum(c['B_only_eligible_'+str(n)] for c in cc),
                        'distinct_firms':len({p[k] for p in pp for k in ['company_a','company_b']}),
                        **{cat:count[cat] for cat in CATS}})
    return out

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    old=read(SNAP/'analysis/ad_technology_current.csv');new=read(ROOT/'analysis/v4_ad_technology_current.csv')
    key=lambda r:(r['identity_key'],r['label_code'])
    assert len(old)==len(new)==len({key(r) for r in new})==496
    assert {key(r) for r in old}=={key(r) for r in new}
    oldcells=cells(old);oldpairs=pairs(oldcells)
    saved={pkey(p):p for p in read(SNAP/'analysis/current_firm_pairs.csv')}
    assert {pkey(p) for p in oldpairs}==set(saved)
    v3checks=0
    for p in oldpairs:
        for k,v in p.items():
            if k not in saved[pkey(p)]:continue
            want=saved[pkey(p)][k]
            if isinstance(v,(int,float)):assert abs(float(v)-float(want))<1e-10,(pkey(p),k)
            else:assert str(v)==want,(pkey(p),k)
            v3checks+=1
    currentcells=cells(new);currentpairs=pairs(currentcells);summary=summaries(currentpairs,currentcells)
    write('current_firm_cells.csv',currentcells);write('current_firm_pairs.csv',currentpairs);write('current_pair_summary.csv',summary)
    oldkeys={pkey(p) for p in oldpairs};primarykeys={pkey(p) for p in currentpairs}
    keychanges=[]
    for k in sorted(oldkeys|primarykeys):
        if (k in oldkeys)!=(k in primarykeys):
            keychanges.append({'threshold':k[0],'task':k[1],'label_code':k[2],'company_a':k[3],'company_b':k[4],
                               'in_v3':int(k in oldkeys),'in_v4':int(k in primarykeys)})
    if keychanges:write('company_eligibility_key_changes.csv',keychanges)
    else:
        with (OUT/'company_eligibility_key_changes.csv').open('w',encoding='utf-8',newline='') as f:
            csv.writer(f).writerow(['threshold','task','label_code','company_a','company_b','in_v3','in_v4'])
    oldby={pkey(p):p for p in oldpairs}
    deltas=[]
    for p in currentpairs:
        k=pkey(p)
        if k not in oldby:continue
        prev=oldby[k]
        for field in p:
            if p[field]!=prev[field]:
                deltas.append({'threshold':k[0],'task':k[1],'label_code':k[2],'company_a':k[3],'company_b':k[4],
                               'field':field,'v3_value':prev[field],'v4_value':p[field]})
    write('company_v3_v4_comparison_changes.csv',deltas)
    diagnostic=read(SNAP/'source_v2/analysis/diagnostic_comparison.csv');db={r['audit_id']:r for r in diagnostic}
    groups=json.loads((SNAP/'data/sensitivity_policy.json').read_text(encoding='utf-8'))['groups']
    readings=[];reading_summaries=[];reading_keys=[]
    for bits in itertools.product([0,1],repeat=7):
        name='READING_'+''.join(map(str,bits))
        changes={key(db[a]):db[a] for g,bit in zip(groups,bits) if bit for a in g['audit_ids']}
        rr=[]
        for row in new:
            r=dict(row)
            if key(r) in changes:
                d=changes[key(r)];r['G']=d['G_fresh'];r['R']=d['R_fresh']
                r['Q']='P' if 'P' in [r['G'],r['R']] else 'Z' if r['G']==r['R']=='Z' else 'U'
            rr.append(r)
        cc=cells(rr);pp=pairs(cc);keys={pkey(p) for p in pp}
        reading_keys.append({'reading':name,'primary_keys':len(primarykeys),'scenario_keys':len(keys),
                             'added_to_primary':len(keys-primarykeys),'removed_from_primary':len(primarykeys-keys)})
        readings.extend({'reading':name,**p} for p in pp)
        reading_summaries.extend({'reading':name,**r} for r in summaries(pp,cc))
    write('admissible_reading_pairs.csv',readings);write('admissible_reading_pair_summary.csv',reading_summaries)
    write('admissible_reading_company_keys.csv',reading_keys)
    envelopes=[]
    for k in sorted({pkey(p) for p in readings}):
        rr=[p for p in readings if pkey(p)==k]
        lo=min(p['Q_difference_lo_pp'] for p in rr);hi=max(p['Q_difference_hi_pp'] for p in rr)
        direction=1 if lo>0 else -1 if hi<0 else 0;md=rr[0]['M_direction']
        envelopes.append({'threshold':k[0],'task':k[1],'label_code':k[2],'company_a':k[3],'company_b':k[4],
                          'readings_present':len(rr),'M_direction':md,'envelope_lo_pp':lo,'envelope_hi_pp':hi,
                          'envelope_direction':direction,'supported_retention_all_readings':int(len(rr)==128 and md!=0 and direction==md),
                          'supported_reversal_all_readings':int(len(rr)==128 and md!=0 and direction==-md),
                          'classifications':'|'.join(sorted({p['classification'] for p in rr}))})
    write('admissible_comparison_envelopes.csv',envelopes)
    facts={'status':'PASS','v3_saved_comparison_values_reconstructed':v3checks,'v4_states':dict(Counter(r['Q'] for r in new)),
           'company_cells':len(currentcells),'primary_summary':[r for r in summary if r['label_code']=='ALL'],
           'main_comparisons':[p for p in currentpairs if p['threshold']==10],
           'new_company_comparison_keys':keychanges,
           'changed_comparison_values':len(deltas),
           'classification_changes':[d for d in deltas if d['field']=='classification'],
           'all_128_primary_key_sets_identical':all(r['added_to_primary']==r['removed_from_primary']==0 for r in reading_keys),
           'semantic_summaries':[{'threshold':n,'supported_retention_all_readings':sum(r['supported_retention_all_readings'] for r in envelopes if r['threshold']==n),
                                  'supported_reversal_all_readings':sum(r['supported_reversal_all_readings'] for r in envelopes if r['threshold']==n)} for n in [5,10]],
           'source_state_sha256':hashlib.sha256((ROOT/'analysis/v4_ad_technology_current.csv').read_bytes()).hexdigest()}
    (OUT/'company_rebuild_checks.json').write_text(json.dumps(facts,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(facts,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
