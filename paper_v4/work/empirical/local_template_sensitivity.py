"""Exploratory sensitivity to exact repeated local target-qualification wording.

The signature keeps each target's complete set of GENERAL/REQUIRED parent
texts separately, together with original metric and observable heading scope.
It does not equate synonyms, remove experience years, or match near duplicates.
Missing evidence and unlocated heading scope receive an advertisement-specific
fallback. No parent or original Q code is rewritten. Fixed primary signatures
and weights are used in all 128 pre-existing Q semantic readings.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict, Counter
import csv, json, hashlib, unicodedata, re, itertools

ROOT=Path(__file__).resolve().parents[2]
V4=ROOT
V3=ROOT/'source_snapshot'
OUT=V4/'analysis/empirical'
INPUTS={
    'parent_evidence':V3/'source_v2/data/inputs/context_evidence.csv',
    'source_records':V3/'source_v2/data/inputs/records.json',
    'diagnostic':V3/'source_v2/analysis/diagnostic_comparison.csv',
    'semantic_policy':V3/'data/sensitivity_policy.json',
    'paired_primary':V4/'analysis/paired/paired_advertisements.csv',
    'scope_primary':V4/'analysis/paired/qualification_scope_states.csv',
}

def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def norm(value):
    return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',value).strip()).casefold()

def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def write(name,rows):
    assert rows,name
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def make_signatures(base, evidence, sources):
    bykey=defaultdict(list)
    spans=[]
    for e in evidence:
        if e['metric'] not in {'GENERAL','REQUIRED'}:continue
        raw=sources[e['identity_key']]['fields'][e['field']]
        start,end=int(e['parent_start']),int(e['parent_end'])
        assert raw[start:end]==e['parent_text'],(e['reading_id'],e['evidence_id'],'parent span')
        assert hashlib.sha256(raw.encode()).hexdigest()==e['source_field_sha256']
        assert start<=int(e['verified_start'])<int(e['verified_end'])<=end
        assert raw[int(e['verified_start']):int(e['verified_end'])]==e['quote']
        bykey[e['identity_key'],e['code']].append(e)
        spans.append({'identity_key':e['identity_key'],'reading_id':e['reading_id'],
                      'target':e['code'],'evidence_id':e['evidence_id'],'metric':e['metric'],
                      'branch_preserved_not_used_for_weight':e['branch'],'field':e['field'],
                      'parent_start':start,'parent_end':end,'parent_text':e['parent_text'],
                      'source_field_sha256':e['source_field_sha256'],'parent_exact':1,
                      'nearest_heading':e['nearest_heading_text'],
                      'normalized_parent_sha256':digest(norm(e['parent_text']))})
    membership=[]
    for r in base:
        identity=r['identity_key'];signature={};fallback=[];details={}
        for side in ['a','b']:
            label=r['target_'+side];ev=bykey[identity,label]
            atoms=set();text_only=set();unknown_scope=0
            if not ev:fallback.append('NO_QUALIFICATION_EVIDENCE_'+side.upper())
            for e in ev:
                heading=norm(e['nearest_heading_text'])
                if heading:scope=('CAPTURED_HEADING',heading)
                elif e['field']=='requirements':scope=('EXPLICIT_REQUIREMENTS_FIELD','')
                else:
                    scope=('UNLOCATED_SCOPE','')
                    unknown_scope+=1
                # Retain the full parent text including punctuation, list
                # numbering, proficiency wording, experience years and choices.
                atom=(e['metric'],scope[0],scope[1],norm(e['parent_text']))
                atoms.add(atom);text_only.add(norm(e['parent_text']))
            if unknown_scope:fallback.append('UNLOCATED_QUALIFICATION_SCOPE_'+side.upper())
            signature[label]=sorted(atoms)
            details.update({f'{side}_qualification_occurrences':len(ev),
                            f'{side}_distinct_parent_atoms':len(atoms),
                            f'{side}_unlocated_scope_occurrences':unknown_scope,
                            f'{side}_parent_text_set_sha256':digest(sorted(text_only)) if text_only else '',
                            f'{side}_scope_text_set_sha256':digest(sorted(atoms)) if atoms else '',
                            f'{side}_evidence_ids':json.dumps([e['evidence_id'] for e in ev])})
        signature_hash=digest(signature)
        # Missing or unlocated evidence must never turn absence into a shared
        # text cluster. A fallback remains unique even if its partial text matches.
        cluster=digest(['independent_fallback',identity]) if fallback else signature_hash
        membership.append({k:r[k] for k in ['identity_key','reading_id','company_id','task','target_a','target_b','M_a','M_b','Q_a','Q_b','both_mentioned']}|
                          {'local_signature_sha256':signature_hash,'local_cluster_sha256':cluster,
                           'independent_fallback':int(bool(fallback)),
                           'fallback_reasons':json.dumps(fallback),
                           'signature_json':json.dumps(signature,ensure_ascii=False,sort_keys=True),**details})
    return membership,spans

def weights(rows,scheme):
    firms=Counter(r['company_id'] for r in rows)
    clusters=Counter((r['company_id'],r['local_cluster_sha256']) for r in rows)
    counts=Counter(k[0] for k in clusters)
    if scheme=='ad_equal':return {r['identity_key']:F(1,len(rows)) for r in rows}
    if scheme=='firm_equal':return {r['identity_key']:F(1,len(firms)*firms[r['company_id']]) for r in rows}
    return {r['identity_key']:F(1,len(firms)*counts[r['company_id']]*clusters[r['company_id'],r['local_cluster_sha256']]) for r in rows}

def weighted_contrast(rows,ws,states,measure):
    assert sum(ws.values(),F(0))==1
    lower=F(0);upper=F(0);confirmed=F(0);p={'a':F(0),'b':F(0)};u={'a':F(0),'b':F(0)}
    for r in rows:
        for side in ['a','b']:
            state=states[r['identity_key'],r['target_'+side]][measure]
            if measure in {'M','H_qualification_context'}:state='P' if int(state) else 'Z'
            if state=='P':p[side]+=ws[r['identity_key']]
            elif state=='U':u[side]+=ws[r['identity_key']]
            else:assert state=='Z'
    confirmed=p['a']-p['b'];lower=confirmed-u['b'];upper=confirmed+u['a']
    assert lower<=confirmed<=upper
    return {'a_confirmed_pct':float(100*p['a']),'b_confirmed_pct':float(100*p['b']),
            'a_unknown_pct':float(100*u['a']),'b_unknown_pct':float(100*u['b']),
            'confirmed_gap_pp':float(100*confirmed),'difference_lo_pp':float(100*lower),'difference_hi_pp':float(100*upper)}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    hashes={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in INPUTS.items()}
    base=read(INPUTS['paired_primary']);assert len(base)==248
    sources=json.loads(INPUTS['source_records'].read_text(encoding='utf-8'))
    sources={r['identity_key']:r for r in sources}
    evidence=read(INPUTS['parent_evidence'])
    states=read(INPUTS['scope_primary'])
    states={(r['identity_key'],r['label_code']):r for r in states}
    assert len(states)==496
    members,spans=make_signatures(base,evidence,sources)
    write('local_template_membership.csv',members)
    write('local_template_parent_span_audit.csv',spans)
    summaries=[];weightrows=[];coverage=[];groups=[];frames={};schemes=['ad_equal','firm_equal','firm_local_target_equal']
    for task in sorted({r['task'] for r in base}):
        for subset in ['all_ads','both_mentioned']:
            rr=[r for r in members if r['task']==task and (subset=='all_ads' or int(r['both_mentioned']))]
            frames[task,subset]=rr
            clustered=defaultdict(list)
            for r in rr:clustered[r['company_id'],r['local_cluster_sha256']].append(r)
            for (firm,cluster),rs in sorted(clustered.items()):
                if any(r['independent_fallback'] for r in rs):assert len(rs)==1
                groups.append({'task':task,'subset':subset,'company_id':firm,'cluster_sha256':cluster,
                               'ads':len(rs),'reading_ids':json.dumps([r['reading_id'] for r in rs]),
                               'fallback':int(any(r['independent_fallback'] for r in rs)),
                               'primary_Q_patterns':json.dumps(sorted({r['Q_a']+'/'+r['Q_b'] for r in rs})),
                               'multiple_primary_Q_patterns':int(len({r['Q_a']+'/'+r['Q_b'] for r in rs})>1)})
            cv={'task':task,'subset':subset,'ads':len(rr),'firms':len({r['company_id'] for r in rr}),
                'local_groups':len(clustered),'repeated_groups':sum(len(rs)>1 for rs in clustered.values()),
                'ads_in_repeated_groups':sum(len(rs) for rs in clustered.values() if len(rs)>1),
                'independent_fallback_ads':sum(r['independent_fallback'] for r in rr),
                'reduction_from_ads':len(rr)-len(clustered)}
            coverage.append(cv)
            for scheme in schemes:
                ws=weights(rr,scheme)
                weightrows.extend({'task':task,'subset':subset,'weighting':scheme,
                                   'identity_key':r['identity_key'],'weight_numerator':ws[r['identity_key']].numerator,
                                   'weight_denominator':ws[r['identity_key']].denominator} for r in rr)
                for measure in ['M','H_qualification_context','Q','Q_plus_example','Q_plus_choice_example']:
                    value=weighted_contrast(rr,ws,states,measure)
                    summaries.append({**cv,'weighting':scheme,'measure':measure,**value})
                if scheme=='firm_local_target_equal':
                    # Independent nested cluster, then firm means. Verify both
                    # Q endpoints without using the per-ad weight formula.
                    firm_values=defaultdict(list)
                    for (firm,cluster),rs in clustered.items():
                        lo=sum(F(int(r['Q_a']=='P')-int(r['Q_b']!='Z')) for r in rs)/len(rs)
                        hi=sum(F(int(r['Q_a']!='Z')-int(r['Q_b']=='P')) for r in rs)/len(rs)
                        firm_values[firm].append((lo,hi))
                    lo=sum(sum(x[0] for x in vs)/len(vs) for vs in firm_values.values())/len(firm_values)
                    hi=sum(sum(x[1] for x in vs)/len(vs) for vs in firm_values.values())/len(firm_values)
                    q=weighted_contrast(rr,ws,states,'Q')
                    assert abs(float(100*lo)-q['difference_lo_pp'])<1e-10
                    assert abs(float(100*hi)-q['difference_hi_pp'])<1e-10
    write('local_template_coverage.csv',coverage)
    write('local_template_groups.csv',groups)
    write('local_template_weights.csv',weightrows)
    write('local_template_construct_contrasts.csv',summaries)
    diagnostic=read(INPUTS['diagnostic']);db={r['audit_id']:r for r in diagnostic}
    policy=json.loads(INPUTS['semantic_policy'].read_text(encoding='utf-8'))['groups']
    semantic=[]
    for bits in itertools.product([0,1],repeat=7):
        now={k:dict(v) for k,v in states.items()}
        for group,bit in zip(policy,bits):
            if not bit:continue
            for aid in group['audit_ids']:
                d=db[aid];k=d['identity_key'],d['label_code']
                now[k]['Q']='P' if 'P' in [d['G_fresh'],d['R_fresh']] else 'Z' if d['G_fresh']==d['R_fresh']=='Z' else 'U'
        for (task,subset),rr in frames.items():
            ws=weights(rr,'firm_local_target_equal')
            semantic.append({'reading':'READING_'+''.join(map(str,bits)),'task':task,'subset':subset,
                             'weighting':'firm_local_target_equal',**weighted_contrast(rr,ws,now,'Q')})
    write('local_template_semantic_readings.csv',semantic)
    envelopes=[]
    for task,subset in frames:
        sr=[r for r in semantic if r['task']==task and r['subset']==subset]
        assert len(sr)==128
        envelopes.append({'task':task,'subset':subset,'weighting':'firm_local_target_equal','readings':128,
                          'envelope_lo_pp':min(r['difference_lo_pp'] for r in sr),
                          'envelope_hi_pp':max(r['difference_hi_pp'] for r in sr),
                          'confirmed_gap_min_pp':min(r['confirmed_gap_pp'] for r in sr),
                          'confirmed_gap_max_pp':max(r['confirmed_gap_pp'] for r in sr)})
    write('local_template_semantic_envelopes.csv',envelopes)
    assert hashes=={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in INPUTS.items()}
    facts={'status':'PASS','input_hashes_unchanged':True,'paired_ads':len(members),'parent_evidence_occurrences_verified':len(spans),
           'weight_definition':'Equal firms; equal distinct joint local target-qualification text/scope groups within each firm; equal ads within group.',
           'normalization':'NFKC, casefold and whitespace only; years, numbering, punctuation, target order and scope atom preserved.',
           'missing_treatment':'Advertisement-specific fallback if any target lacks GENERAL/REQUIRED evidence or any retained parent has unlocated scope outside requirements field.',
           'semantic_weights_fixed':True,'broad_constructs_primary_only':True,'coding_changes':False,
           'same_signature_different_primary_Q_groups':sum(g['multiple_primary_Q_patterns'] for g in groups),
           'unique_scope_groups_with_different_primary_Q':len({(g['task'],g['company_id'],g['cluster_sha256']) for g in groups if g['multiple_primary_Q_patterns']}),
           'coverage':coverage,'Q_semantic_envelopes':envelopes,
           'robot_model_primary_contrasts':[r for r in summaries if r['task']=='ROBOT_MODEL' and r['weighting']=='firm_local_target_equal'],
           'inputs':[{ 'name':k,'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashes[k]} for k,p in INPUTS.items()]}
    (OUT/'local_template_checks.json').write_text(json.dumps(facts,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:facts[k] for k in ['status','parent_evidence_occurrences_verified','same_signature_different_primary_Q_groups','coverage','Q_semantic_envelopes','robot_model_primary_contrasts']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
