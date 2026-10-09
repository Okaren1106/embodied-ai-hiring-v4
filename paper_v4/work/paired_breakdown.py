"""Resolved-label contamination thresholds for paired finite-corpus bounds.

An edit changes one resolved Q state P<->Z, keeping mentions, unknowns,
identities and weights fixed. It is hypothetical sensitivity, not recoding.
Q subset M is respected. Report label-edit cost and distinct-ad cost separately.
For each cost, exact positive influence weights yield the minimum needed to
lose original strict directional support. A discrete edit can jump across zero.
No confidence level or estimated error rate is asserted.
"""
from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction as F
import itertools,csv,json
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/'source_snapshot'
OUT=ROOT/'analysis/paired'
def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def weights(rows,scheme):
    counts=Counter(r['company_id'] for r in rows)
    clusters=Counter((r['company_id'],r['template_field'],r['template_hash']) for r in rows)
    perfirm=Counter(k[0] for k in clusters)
    if scheme=='ad_equal':return [F(1,len(rows))]*len(rows)
    if scheme=='firm_equal':return [F(1,len(counts)*counts[r['company_id']]) for r in rows]
    return [F(1,len(counts)*perfirm[r['company_id']]*clusters[r['company_id'],r['template_field'],r['template_hash']]) for r in rows]
def threshold(influences,margin):
    if margin<=0:return 0,[]
    sorted_impact=sorted(influences,key=lambda x:(-x[0],x[1]))
    acc=F(0);witness=[]
    for impact,identity in sorted_impact:
        if impact<=0:continue
        acc+=impact;witness.append(identity)
        if acc>=margin:
            assert acc-impact<margin
            return len(witness),witness
    return None,[]
def breakdown(rows,scheme):
    ws=weights(rows,scheme);assert sum(ws)==1
    lower=sum(w*(int(r['Q_a']=='P')-int(r['Q_b']!='Z')) for r,w in zip(rows,ws))
    upper=sum(w*(int(r['Q_a']!='Z')-int(r['Q_b']=='P')) for r,w in zip(rows,ws))
    sign=1 if lower>0 else -1 if upper<0 else 0
    margin=lower if sign==1 else -upper if sign==-1 else F(0)
    cells=[];ads=[]
    if sign:
        a,b=('a','b') if sign==1 else ('b','a')
        for r,w in zip(rows,ws):
            cap=0;k=r['identity_key']
            if r['Q_'+a]=='P':cells.append((w,k+'|'+a+'|P_to_Z'));cap+=w
            if r['Q_'+b]=='Z' and int(r['M_'+b]):cells.append((w,k+'|'+b+'|Z_to_P'));cap+=w
            if cap:ads.append((cap,k))
    nc,wc=threshold(cells,margin);na,wa=threshold(ads,margin)
    return {'direction':sign,'margin_pp':float(100*margin),'minimum_pair_state_edits':nc,
            'minimum_advertisements_edited':na,'pair_edit_witness_json':json.dumps(wc),
            'advertisement_edit_witness_json':json.dumps(wa)}
def main():
    base=read(OUT/'paired_advertisements.csv')
    diag=read(OLD/'source_v2/analysis/diagnostic_comparison.csv')
    groups=json.loads((OLD/'data/sensitivity_policy.json').read_text(encoding='utf-8'))['groups']
    db={(r['identity_key'],r['label_code']):r for r in diag}
    results=[]
    for bits in itertools.product([0,1],repeat=7):
        selected={a for g,b in zip(groups,bits) if b for a in g['audit_ids']}
        rr=[]
        for r in base:
            r=dict(r)
            for ab in ['a','b']:
                d=db.get((r['identity_key'],r['target_'+ab]))
                if d and d['audit_id'] in selected:r['Q_'+ab]=d['Q_fresh']
            rr.append(r)
        for task in sorted({r['task'] for r in rr}):
            for subset in ['all_ads','both_mentioned']:
                tr=[r for r in rr if r['task']==task and (subset=='all_ads' or int(r['both_mentioned']))]
                for scheme in ['ad_equal','firm_equal','firm_template_equal']:
                    results.append({'reading':'READING_'+''.join(map(str,bits)),'task':task,'subset':subset,
                                    'weighting':scheme,'ads':len(tr),**breakdown(tr,scheme)})
    write('paired_breakdown_readings.csv',results)
    summary=[]
    for task in sorted({r['task'] for r in results}):
        for subset in ['all_ads','both_mentioned']:
            for scheme in ['ad_equal','firm_equal','firm_template_equal']:
                rr=[r for r in results if r['task']==task and r['subset']==subset and r['weighting']==scheme]
                assert len(rr)==128
                summary.append({'task':task,'subset':subset,'weighting':scheme,'readings':len(rr),
                                'directions':'|'.join(map(str,sorted({r['direction'] for r in rr}))),
                                'minimum_pair_state_edits_over_readings':min(r['minimum_pair_state_edits'] for r in rr),
                                'maximum_pair_state_edits_over_readings':max(r['minimum_pair_state_edits'] for r in rr),
                                'minimum_advertisements_edited_over_readings':min(r['minimum_advertisements_edited'] for r in rr),
                                'maximum_advertisements_edited_over_readings':max(r['minimum_advertisements_edited'] for r in rr)})
    write('paired_breakdown_envelopes.csv',summary)
    print(json.dumps([r for r in summary if r['task']=='ROBOT_MODEL'],indent=2))
if __name__=='__main__':main()
