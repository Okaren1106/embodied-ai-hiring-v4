"""Independent arithmetic and source-join audit of the root paired analysis.

Does not import or execute paired_analysis.py. All calculations start from v4
derived states and frozen source inputs. Arithmetic verification is not independent coding.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict, Counter
import csv, hashlib, itertools, json, re, unicodedata

ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT/'source_snapshot'
PAIRED = ROOT/'analysis/paired'
OUT = ROOT/'analysis/empirical'
TARGETS = {'ROBOT_MODEL':('SK_PYTHON','SK_PYTORCH'),
           'ROBOT_RUNTIME':('SK_CPP','SK_LINUX'),
           'BOARD_CIRCUIT':('SK_ALTIUM','V2_EMC_SIPI')}

def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def check_close(a,b):
    assert abs(float(a)-float(b))<1e-10, (a,b)

def normalized(text):
    return ' '.join(unicodedata.normalize('NFKC',text).split()).casefold()

def build(rows,sources):
    by_ad = defaultdict(dict)
    for r in rows:
        by_ad[r['identity_key']][r['label_code']] = r
    results = []
    for identity, labels in by_ad.items():
        source = sources[identity]
        a,b = TARGETS[source['task']]
        assert set(labels)=={a,b}
        x,y=labels[a],labels[b]
        field='requirements' if normalized(source['fields']['requirements']) else 'full_description'
        template=hashlib.sha256(normalized(source['fields'][field]).encode()).hexdigest()
        results.append({'id':identity,'task':source['task'],'company':source['company_id'],
                        'qa':x['Q'],'qb':y['Q'],'ma':int(x['M']),'mb':int(y['M']),
                        'template':(source['company_id'],field,template)})
    return results

def estimate(rows,scheme):
    """Nested averaging, rather than importing the production weight function."""
    groups=defaultdict(list)
    for r in rows:
        # Pair difference endpoints use only Q states; shared unknown source
        # constraints are deliberately not assumed.
        r=dict(r)
        r['m_gap']=r['ma']-r['mb']
        r['p_gap']=(r['qa']=='P')-(r['qb']=='P')
        r['lower']=(r['qa']=='P')-(r['qb']!='Z')
        r['upper']=(r['qa']!='Z')-(r['qb']=='P')
        if scheme=='ad_equal':groups['all'].append(r)
        elif scheme=='firm_equal':groups[r['company']].append(r)
        else:groups[r['template']].append(r)
    groupmeans={g:{c:sum((F(r[c]) for r in rs),F(0))/len(rs)
                    for c in ['m_gap','p_gap','lower','upper']} for g,rs in groups.items()}
    if scheme=='firm_template_equal':
        firms=defaultdict(list)
        for g,means in groupmeans.items():firms[g[0]].append(means)
        groupmeans={g:{c:sum((m[c] for m in ms),F(0))/len(ms)
                        for c in ['m_gap','p_gap','lower','upper']} for g,ms in firms.items()}
    return {c:100*sum((m[c] for m in groupmeans.values()),F(0))/len(groupmeans)
            for c in ['m_gap','p_gap','lower','upper']}

def run():
    rows=read(ROOT/'analysis/v4_ad_technology_current.csv')
    sources=json.loads((OLD/'source_v2/data/inputs/records.json').read_text(encoding='utf-8'))
    sources={r['identity_key']:r for r in sources}
    base=build(rows,sources)
    assert len(base)==len(sources)==248
    assert len(rows)==496
    existing=read(PAIRED/'paired_advertisements.csv')
    assert len(existing)==248
    existing={r['identity_key']:r for r in existing}
    n=0
    for r in base:
        original=existing[r['id']]
        for original_col,our_col in [('M_a','ma'),('M_b','mb'),('Q_a','qa'),('Q_b','qb')]:
            assert str(r[our_col])==original[original_col]
            n+=1
        assert original['template_hash']==r['template'][2]
        n+=1
    diag=read(OLD/'source_v2/analysis/diagnostic_comparison.csv')
    flag={r['identity_key'] for r in diag if r['task_support']!='SUPPORTED'}
    columns={'mention_gap_pp':'m_gap','confirmed_gap_pp':'p_gap',
             'Q_difference_lo_pp':'lower','Q_difference_hi_pp':'upper'}
    for summary in read(PAIRED/'paired_summary.csv'):
        subset=summary['subset']
        selected=[r for r in base if r['task']==summary['task'] and
                  (subset=='all_ads' or (subset=='both_mentioned' and r['ma']==r['mb']==1)
                   or (subset in ['known_task_support','excluding_flagged_task_boundaries','exclude_flagged_task_boundaries'] and r['id'] not in flag))]
        assert len(selected)==int(summary['ads']), subset
        assert len({r['company'] for r in selected})==int(summary['firms'])
        assert len({r['template'] for r in selected})==int(summary['templates'])
        e=estimate(selected,summary['weighting'])
        for original_col,our_col in columns.items():check_close(summary[original_col],e[our_col]);n+=1
    for summary in read(PAIRED/'leave_one_firm_out.csv'):
        selected=[r for r in base if r['task']==summary['task'] and r['company']!=summary['omitted_company']]
        e=estimate(selected,summary['weighting'])
        for original_col,our_col in columns.items():check_close(summary[original_col],e[our_col]);n+=1
    groups=json.loads((OLD/'data/sensitivity_policy.json').read_text(encoding='utf-8'))['groups']
    dbyid={r['audit_id']:r for r in diag}
    outputs=defaultdict(list)
    for r in read(PAIRED/'semantic_reading_summaries.csv'):outputs[r['reading']].append(r)
    bounds=[]
    for bits in itertools.product([0,1],repeat=7):
        name='READING_'+''.join(map(str,bits))
        revised={(dbyid[x]['identity_key'],dbyid[x]['label_code']):dbyid[x]
                 for g,bit in zip(groups,bits) if bit for x in g['audit_ids']}
        updated=[]
        for r in rows:
            r=dict(r)
            if (r['identity_key'],r['label_code']) in revised:
                d=revised[r['identity_key'],r['label_code']]
                r['Q']='P' if 'P' in (d['G_fresh'],d['R_fresh']) else 'Z' if d['G_fresh']==d['R_fresh']=='Z' else 'U'
                assert r['Q']==d['Q_fresh']
            updated.append(r)
        paired=build(updated,sources)
        for summary in outputs[name]:
            selected=[r for r in paired if r['task']==summary['task'] and
                      (summary['subset']=='all_ads' or r['ma']==r['mb']==1)]
            e=estimate(selected,summary['weighting'])
            for original_col,our_col in columns.items():check_close(summary[original_col],e[our_col]);n+=1
            bounds.append({'reading':name,'task':summary['task'],'subset':summary['subset'],
                           'weighting':summary['weighting'],'lower':e['lower'],'upper':e['upper']})
    for envelope in read(PAIRED/'semantic_envelopes.csv'):
        selected=[r for r in bounds if all(r[k]==envelope[k] for k in ['task','subset','weighting'])]
        assert len(selected)==128
        check_close(envelope['envelope_lo_pp'],min(r['lower'] for r in selected));n+=1
        check_close(envelope['envelope_hi_pp'],max(r['upper'] for r in selected));n+=1
    # Pairing does not alter the marginal-rate arithmetic on the SAME states.
    # Preserve v3 separately: the adopted v4 P->U correction changes its value.
    old=read(OLD/'analysis/current_task_summary.csv')
    old={r['label_code']:r for r in old}
    equivalences=[]
    for task,(a,b) in TARGETS.items():
        selected=[r for r in base if r['task']==task]
        e=estimate(selected,'ad_equal')
        for x in [a,b]:assert int(old[x]['B'])==len(selected)
        old_marginal=100*(F(int(old[a]['Q_P']),len(selected))-F(int(old[b]['Q_P']),len(selected)))
        marginal=100*F(sum(r['Q']=='P' for r in rows if r['task']==task and r['label_code']==a)-sum(r['Q']=='P' for r in rows if r['task']==task and r['label_code']==b),len(selected))
        assert marginal==e['p_gap'];n+=1
        equivalences.append({'task':task,'paired_confirmed_gap_pp':float(e['p_gap']),
                             'v4_marginal_difference_pp':float(marginal),'v3_historical_marginal_difference_pp':float(old_marginal),'same_version_identical':True})
    report={'status':'PASS','arithmetic_and_identity_checks':n,
            'source_coding_independently_validated':False,
            'unknown_bounds':'Unrestricted Q-state outer assignment bounds; no sharpness claim.',
            'full_sample_pairing_algebra':equivalences,
            'flagged_task_boundary_ads':len(flag),
            'diagnostic_ads':len({r['identity_key'] for r in diag}),
            'undocumented_task_support_must_not_be_called_verified':True,
            'conceptual_findings_file':'audit/paired_analysis_conceptual_audit.md'}
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'paired_independent_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
