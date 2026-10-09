"""Within-advertisement contrasts on the immutable v3 technology sample.

DECISIONS LOG, 2026-09-26
User authorized substantive method extensions; no frozen input is modified.
Unit: advertisement x target in input; reshape two targets to one advertisement.
Cross-section, not a panel. Join 248 source records 1:1 to the 248 paired ads.
Keep all identities; common-mention and task-boundary subgroups are explicit
diagnostics, not replacements for the primary sample. No outcome imputation.
Weights: ads equal; firms equal within task; Unicode-NFKC/casefold/whitespace-normalized exact
qualification-text clusters equal within firm, then firms equal. Source text
remains local; output template IDs contain hashes, not full source text.
Bounds enumerate unresolved Q as 0/1 without probability interpretation.
Semantic alternatives use the already documented seven coupled switches.
"""
from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction as F
import csv, json, hashlib, itertools, re, unicodedata

ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/'source_snapshot'
OUT=ROOT/'analysis'/'paired'
PAIRS={'ROBOT_MODEL':('SK_PYTHON','SK_PYTORCH'),
       'ROBOT_RUNTIME':('SK_CPP','SK_LINUX'),
       'BOARD_CIRCUIT':('SK_ALTIUM','V2_EMC_SIPI')}

def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def write(name,rows):
    assert rows,name
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def norm(text):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',text).strip()).casefold()
def lo(q):return int(q=='P')
def hi(q):return int(q!='Z')

def paired(rows,sources):
    groups=defaultdict(dict)
    for r in rows:
        k=r['identity_key'];l=r['label_code']
        assert l not in groups[k]
        groups[k][l]=r
    assert set(groups)==set(sources), 'Source join is not 1:1 and complete'
    out=[]
    for k,g in sorted(groups.items()):
        task=sources[k]['task']; a,b=PAIRS[task]
        assert set(g)=={a,b}
        x,y=g[a],g[b]; src=sources[k]
        assert x['company_id']==y['company_id']==src['company_id']
        assert x['task']==y['task']==task
        field='requirements' if norm(src['fields']['requirements']) else 'full_description'
        text=norm(src['fields'][field]);assert text
        h=hashlib.sha256(text.encode()).hexdigest()
        out.append({'identity_key':k,'reading_id':x['reading_id'],'company_id':x['company_id'],
                    'task':task,'target_a':a,'target_b':b,'M_a':int(x['M']),'M_b':int(y['M']),
                    'Q_a':x['Q'],'Q_b':y['Q'],'both_mentioned':int(x['M'])&int(y['M']),
                    'template_field':field,'template_hash':h,'observation_wave':src['observation_wave'],
                    'delta_M':int(x['M'])-int(y['M']),
                    'delta_confirmed':lo(x['Q'])-lo(y['Q']),
                    'delta_Q_lo':lo(x['Q'])-hi(y['Q']),
                    'delta_Q_hi':hi(x['Q'])-lo(y['Q'])})
    return out

def weights(rows,scheme):
    firms=Counter(r['company_id'] for r in rows)
    templates=Counter((r['company_id'],r['template_field'],r['template_hash']) for r in rows)
    byfirm=Counter(k[0] for k in templates)
    if scheme=='ad_equal':return [F(1,len(rows)) for r in rows]
    if scheme=='firm_equal':return [F(1,len(firms)*firms[r['company_id']]) for r in rows]
    if scheme=='firm_template_equal':
        return [F(1,len(firms)*byfirm[r['company_id']]*templates[r['company_id'],r['template_field'],r['template_hash']]) for r in rows]
    raise ValueError(scheme)

def summary(rows,scheme,task,subset):
    w=weights(rows,scheme);assert sum(w)==1
    v=lambda f:float(100*sum(z*f(r) for r,z in zip(rows,w)))
    return {'task':task,'target_a':rows[0]['target_a'],'target_b':rows[0]['target_b'],
            'subset':subset,'weighting':scheme,'ads':len(rows),'firms':len({r['company_id'] for r in rows}),
            'templates':len({(r['company_id'],r['template_field'],r['template_hash']) for r in rows}),
            'M_a_pct':v(lambda r:r['M_a']),'M_b_pct':v(lambda r:r['M_b']),
            'Q_a_confirmed_pct':v(lambda r:lo(r['Q_a'])),'Q_b_confirmed_pct':v(lambda r:lo(r['Q_b'])),
            'Q_a_unknown_pct':v(lambda r:r['Q_a']=='U'),'Q_b_unknown_pct':v(lambda r:r['Q_b']=='U'),
            'mention_gap_pp':v(lambda r:r['delta_M']),
            'confirmed_gap_pp':v(lambda r:r['delta_confirmed']),
            'Q_difference_lo_pp':v(lambda r:r['delta_Q_lo']),
            'Q_difference_hi_pp':v(lambda r:r['delta_Q_hi']),
            'known_nondirect_mention_gap_pp':v(lambda r:int(r['M_a']==1 and r['Q_a']=='Z')-int(r['M_b']==1 and r['Q_b']=='Z'))}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    inputpaths=[ROOT/'analysis/v4_ad_technology_current.csv',OLD/'source_v2/data/inputs/records.json',
                OLD/'source_v2/analysis/diagnostic_comparison.csv',OLD/'data/sensitivity_policy.json']
    rows=read(inputpaths[0]);src=json.loads(inputpaths[1].read_text(encoding='utf-8'))
    sources={r['identity_key']:r for r in src};assert len(sources)==len(src)==248
    assert len(rows)==496 and len({(r['identity_key'],r['label_code']) for r in rows})==496
    for r in rows:
        assert r['Q'] in ['P','Z','U']
        assert r['Q']=='Z' or int(r['M'])==1
    primary=paired(rows,sources);assert len(primary)==248
    write('paired_advertisements.csv',primary)
    save('merge_audit.json',{'cardinality':'1:1 paired advertisement to captured source','matched':248,'master_only':0,'using_only':0,'excluded_primary':0})
    results=[];joint=[];loo=[];firm=[];weightrows=[]
    diag=read(inputpaths[2]);flags={r['identity_key'] for r in diag if r['task_support']!='SUPPORTED'}
    for task in PAIRS:
        tr=[r for r in primary if r['task']==task]
        for subset,rr in [('all_ads',tr),('both_mentioned',[r for r in tr if r['both_mentioned']]),
                          ('excluding_flagged_task_boundaries',[r for r in tr if r['identity_key'] not in flags])]:
            if not rr:continue
            for scheme in ['ad_equal','firm_equal','firm_template_equal']:
                results.append(summary(rr,scheme,task,subset))
                if subset=='all_ads':
                    weightrows.extend({'identity_key':r['identity_key'],'task':task,'weighting':scheme,'weight_numerator':w.numerator,'weight_denominator':w.denominator} for r,w in zip(rr,weights(rr,scheme)))
            for qa,qb in itertools.product(['P','Z','U'],repeat=2):
                joint.append({'task':task,'subset':subset,'Q_a':qa,'Q_b':qb,'ads':sum(r['Q_a']==qa and r['Q_b']==qb for r in rr)})
        for company in sorted({r['company_id'] for r in tr}):
            cr=[r for r in tr if r['company_id']==company]
            firm.append({'company_id':company,**summary(cr,'ad_equal',task,'all_ads')})
            other=[r for r in tr if r['company_id']!=company]
            for scheme in ['ad_equal','firm_equal']:
                loo.append({'omitted_company':company,**summary(other,scheme,task,'leave_one_firm_out')})
    write('paired_summary.csv',results);write('paired_joint_states.csv',joint)
    write('paired_firms.csv',firm);write('leave_one_firm_out.csv',loo);write('analysis_weights.csv',weightrows)
    groups=json.loads(inputpaths[3].read_text(encoding='utf-8'))['groups'];assert len(groups)==7
    dbykey={(r['identity_key'],r['label_code']):r for r in diag}
    scenarios=[]
    for bits in itertools.product([0,1],repeat=7):
        selected={a for g,bit in zip(groups,bits) if bit for a in g['audit_ids']}
        rr=[]
        for r in rows:
            r=dict(r);d=dbykey.get((r['identity_key'],r['label_code']))
            if d and d['audit_id'] in selected:r['Q']=d['Q_fresh']
            rr.append(r)
        pr=paired(rr,sources)
        for task in PAIRS:
            tr=[r for r in pr if r['task']==task]
            for subset,tt in [('all_ads',tr),('both_mentioned',[r for r in tr if r['both_mentioned']])]:
                if not tt:continue
                for scheme in ['ad_equal','firm_equal','firm_template_equal']:
                    scenarios.append({'reading':'READING_'+''.join(map(str,bits)),**summary(tt,scheme,task,subset)})
    write('semantic_reading_summaries.csv',scenarios)
    envelopes=[]
    for r in results:
        if r['subset']=='excluding_flagged_task_boundaries':continue
        s=[x for x in scenarios if all(x[k]==r[k] for k in ['task','subset','weighting'])]
        assert len(s)==128
        envelopes.append({k:r[k] for k in ['task','target_a','target_b','subset','weighting','ads','firms']}|{
            'readings':128,'envelope_lo_pp':min(x['Q_difference_lo_pp'] for x in s),
            'envelope_hi_pp':max(x['Q_difference_hi_pp'] for x in s),
            'confirmed_gap_min_pp':min(x['confirmed_gap_pp'] for x in s),'confirmed_gap_max_pp':max(x['confirmed_gap_pp'] for x in s)})
    write('semantic_envelopes.csv',envelopes)
    for r in results:
        assert abs(r['mention_gap_pp']-(r['confirmed_gap_pp']+r['known_nondirect_mention_gap_pp']+r['Q_a_unknown_pct']-r['Q_b_unknown_pct']))<1e-10
    facts={'primary':[r for r in results if r['subset']=='all_ads' and r['weighting']=='ad_equal'],
           'common_mentions':[r for r in results if r['subset']=='both_mentioned' and r['weighting']=='ad_equal'],
           'primary_semantic_envelopes':[r for r in envelopes if r['subset']=='all_ads' and r['weighting']=='ad_equal'],
           'leave_one_firm_out_ranges':[{'task':task,'weighting':scheme,'lo_min':min(r['Q_difference_lo_pp'] for r in loo if r['task']==task and r['weighting']==scheme),'hi_max':max(r['Q_difference_hi_pp'] for r in loo if r['task']==task and r['weighting']==scheme)} for task in PAIRS for scheme in ['ad_equal','firm_equal']],
           'checks':{'primary_ads':len(primary),'primary_pairs':len(rows),'source_records':len(src),'semantic_readings':128,'unknown_not_imputed':True,'primary_rows_excluded':0,'failures':0}}
    save('paired_facts.json',facts)
    save('input_manifest.json',[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputpaths])
    print(json.dumps(facts,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
