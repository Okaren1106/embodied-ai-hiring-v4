"""Record the coordinator-adopted five corrections after full-source review.

This is a one-time authoring utility, not an automatic recoding algorithm.
REPRODUCE consumes the resulting declarative ledger as an input.
"""
from pathlib import Path
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
proposed=read(ROOT/'analysis/empirical/current_u_proposed_corrections.csv')
assert {r['reading_id'] for r in proposed}=={'N0508','N0634','E0071','E0549','E0560'}
ev=read(ROOT/'source_snapshot/source_v2/data/inputs/context_evidence.csv')
records=json.loads((ROOT/'source_snapshot/source_v2/data/inputs/records.json').read_text(encoding='utf-8'))
src={r['identity_key']:r for r in records}
changes=[]
for i,r in enumerate(proposed,1):
    ids=json.loads(r['evidence_ids'])
    e=next(e for e in ev if e['identity_key']==r['identity_key'] and e['evidence_id']==ids[0])
    text=src[r['identity_key']]['fields'][e['field']]
    start,end=int(e['parent_start']),int(e['parent_end'])
    assert text[start:end]==e['parent_text']
    c={k:r[k] for k in ['identity_key','reading_id','company_id','task','label_code','reason']}
    c.update(audit_id=f'V4_{i:03}',source_review_id=r['review_id'],
             G_before=r['G'],R_before=r['R'],Q_before=r['Q'],G_after='Z',R_after='Z',Q_after='Z',
             governing_relation=r['governing_modifier_if_corrected'],source_field=e['field'],
             source_start=start,source_end=end,source_quote=text[start:end],
             source_field_sha256=hashlib.sha256(text.encode()).hexdigest(),
             source_evidence_ids=ids,analysis_revision_date='2026-09-26',
             authorization='User authorized substantive research upgrades. Model source review and coordinator adjudication; not an independent human code.')
    if r['reading_id']=='N0508':c['identical_full_source_to']='N0486'
    changes.append(c)
ledger={'revision':'4.0','origin':'Complete review of all 46 v3-current U pairs in 44 advertisements',
        'v3_states_sha256':hashlib.sha256((ROOT/'source_snapshot/analysis/ad_technology_current.csv').read_bytes()).hexdigest(),
        'changes':changes,'changed_pairs':5,'fixed_frame_pairs':496,
        'does_not_modify_original_v3':True,'independent_human_recoding':False}
folder=ROOT/'data';folder.mkdir(exist_ok=True)
p=folder/'v4_source_corrections.json'
assert not p.exists(),'Do not silently replace a declared revision ledger.'
p.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(str(p))
