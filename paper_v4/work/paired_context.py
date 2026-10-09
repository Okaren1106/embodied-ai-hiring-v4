"""Connect existing source-context flags to paired qualification discordance.

No fresh semantic coding: use frozen context flags and current Q states.
Context flags can overlap; membership in a flag is not a causal mechanism.
All 496 identity-target keys must match exactly before aggregation.
"""
from pathlib import Path
from collections import defaultdict
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/'source_snapshot'
OUT=ROOT/'analysis/paired'
def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
    context_path=OLD/'source_v2/data/inputs/context_index.csv'
    contexts=read(context_path); rows=read(ROOT/'analysis/v4_ad_technology_current.csv')
    key=lambda r:(r['identity_key'],r['label_code'])
    by={key(r):r for r in contexts};assert len(by)==len(contexts)==496
    assert set(by)=={key(r) for r in rows}
    paired=read(OUT/'paired_advertisements.csv')
    pairs={r['identity_key']:r for r in paired};assert len(pairs)==248
    out=[]
    flags=['only_preferred','only_duty','has_required','has_general_other_branch','has_choice','has_example','has_choice_and_example','has_conditional','has_unresolved_branch']
    for r in rows:
        c=by[key(r)];p=pairs[r['identity_key']]
        assert int(c['M_positive'])==int(r['M'])
        out.append({k:r[k] for k in ['identity_key','reading_id','company_id','task','label_code','M','Q']}|
                   {'both_mentioned':p['both_mentioned'],'paired_Q_pattern':p['Q_a']+'/'+p['Q_b'],
                    'choice_or_example_current':r['choice_or_example'],
                    'legacy_context_Q_alignment':'Context flags retained; Q uses v3 corrected layer',
                    **{k:int(c[k]) for k in flags}})
    write('source_context_linkage.csv',out)
    summary=[]
    for label in sorted({r['label_code'] for r in out}):
        for scope in ['all_mentions','common_mentions','common_P_Z','common_Z_P']:
            rr=[r for r in out if r['label_code']==label and int(r['M']) and
                (scope=='all_mentions' or int(r['both_mentioned'])) and
                (scope not in ['common_P_Z','common_Z_P'] or r['paired_Q_pattern']==('P/Z' if scope=='common_P_Z' else 'Z/P'))]
            for state in ['P','Z','U']:
                ss=[r for r in rr if r['Q']==state]
                summary.append({'label_code':label,'scope':scope,'Q':state,'ads':len(ss),
                                'choice_or_example':sum(int(r['choice_or_example_current']) for r in ss),
                                **{k:sum(r[k] for r in ss) for k in flags}})
    write('source_context_summary.csv',summary)
    check={'context_path':str(context_path.relative_to(ROOT)),
           'sha256':hashlib.sha256(context_path.read_bytes()).hexdigest(),
           'keys_joined':496,'source_text_recoded':False,'fresh_human_validation':False,
           'flags_are_overlapping':True,'failures':0}
    (OUT/'source_context_checks.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([r for r in summary if r['label_code'] in ['SK_PYTHON','SK_PYTORCH'] and r['scope'] in ['common_P_Z','common_Z_P'] and r['ads']],indent=2))
if __name__=='__main__':main()
