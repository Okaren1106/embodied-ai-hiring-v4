"""Independently verify the seven v4 source corrections and complete state diff.

No overlay production code is imported. This is an arithmetic/provenance
verification of model source review, not an independent human recoding exercise.
"""
from pathlib import Path
from collections import Counter
import csv, json, hashlib

ROOT = Path(__file__).resolve().parents[2]
V3 = ROOT / 'source_snapshot'
OUT = ROOT / 'analysis/empirical'

def read(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def key(row):
    return row['identity_key'], row['label_code']

def main():
    before_path = V3/'analysis/ad_technology_current.csv'
    after_path = ROOT/'analysis/v4_ad_technology_current.csv'
    ledger_path = ROOT/'data/v4_source_corrections.json'
    source_path = V3/'source_v2/data/inputs/records.json'
    review_path = OUT/'current_u_proposed_corrections.csv'
    parenthetical_path = ROOT/'work/empirical/bare_parenthetical_correction_payload.json'
    paths = [before_path, after_path, ledger_path, source_path, review_path, parenthetical_path]
    hashes = {str(p.relative_to(ROOT)).replace('\\', '/'): sha(p) for p in paths}
    before, after = read(before_path), read(after_path)
    ledger = json.loads(ledger_path.read_text(encoding='utf-8'))
    source = json.loads(source_path.read_text(encoding='utf-8'))
    source = {r['identity_key']: r for r in source}
    changes = {key(r): r for r in ledger['changes']}
    proposed = {key(r): r for r in read(review_path)}
    bare_payload = json.loads(parenthetical_path.read_text(encoding='utf-8'))['changes']
    parenthetical = {key(r):r for r in bare_payload}
    old = {key(r): r for r in before}
    new = {key(r): r for r in after}
    checks = 0
    assert len(before) == len(after) == len(old) == len(new) == 496; checks += 1
    assert set(old) == set(new); checks += 1
    assert set(changes) == set(proposed)|set(parenthetical) and len(changes) == 7; checks += 1
    assert sha(before_path) == ledger['v3_states_sha256']; checks += 1
    assert {r['audit_id'] for r in changes.values()} == {f'V4_{i:03d}' for i in range(1,8)}; checks += 1
    rows = []
    changed = set()
    allowed = {'G', 'R', 'Q', 'revised', 'revision_audit_id'}
    for k, previous in old.items():
        current = new[k]
        assert set(previous) == set(current); checks += 1
        different = {f for f in previous if previous[f] != current[f]}
        if different: changed.add(k)
        if k not in changes:
            assert not different; checks += 1
        else:
            item = changes[k]
            proposal = proposed[k] if k in proposed else parenthetical[k]
            assert different <= allowed; checks += 1
            assert item['source_review_id'] == proposal['review_id' if k in proposed else 'source_review_id']; checks += 1
            assert item['governing_relation'] == proposal['governing_modifier_if_corrected' if k in proposed else 'governing_relation']; checks += 1
            for field in ['reading_id', 'company_id', 'task', 'label_code']:
                assert previous[field] == current[field] == item[field] == proposal[field]; checks += 1
            for field in ['G', 'R', 'Q']:
                assert previous[field] == item[field+'_before']; checks += 1
                assert current[field] == item[field+'_after']; checks += 1
            if k in proposed:
                assert previous['G'] == previous['Q'] == 'U'; checks += 1
                assert current['G'] == current['R'] == current['Q'] == 'Z'; checks += 1
            else:
                assert previous['Q'] in ['P','Z'] and previous['G']==previous['Q']; checks += 1
                assert current['G'] == current['Q'] == 'U' and current['R']=='Z'; checks += 1
                assert item['governing_relation']=='UNCONDITIONAL_OR_EXAMPLE'; checks += 1
            assert current['revised'] == '1' and current['revision_audit_id'] == item['audit_id']; checks += 1
            assert (json.loads(proposal['evidence_ids']) if k in proposed else proposal['source_evidence_ids']) == item['source_evidence_ids']; checks += 1
            raw = source[k[0]]['fields'][item['source_field']]
            start, end = int(item['source_start']), int(item['source_end'])
            assert raw[start:end] == item['source_quote']; checks += 1
            assert hashlib.sha256(raw.encode()).hexdigest() == item['source_field_sha256']; checks += 1
            if k in proposed:
                assert hashlib.sha256(source[k[0]]['fields']['full_description'].encode()).hexdigest() == proposal['full_description_sha256']; checks += 1
            else:
                for f in ['source_field','source_start','source_end','source_quote','source_field_sha256']:
                    assert item[f]==proposal[f]; checks += 1
            rows.append({f:item[f] for f in ['audit_id','source_review_id','identity_key','reading_id','label_code','governing_relation','source_field','source_start','source_end','source_quote','source_field_sha256']} |
                        {'changed_columns':json.dumps(sorted(different)), 'before_G_R_Q':'/'.join(previous[f] for f in ['G','R','Q']),
                         'after_G_R_Q':'/'.join(current[f] for f in ['G','R','Q']), 'exact_source_span':1})
        union = 'P' if 'P' in [current['G'],current['R']] else 'Z' if current['G'] == current['R'] == 'Z' else 'U'
        assert current['Q'] == union; checks += 1
        assert current['Q'] == 'Z' or current['M'] == '1'; checks += 1
    assert changed == set(changes); checks += 1
    assert Counter(r['Q'] for r in before) == {'P':170,'Z':280,'U':46}; checks += 1
    assert Counter(r['Q'] for r in after) == {'P':169,'Z':284,'U':43}; checks += 1
    a = next(r for r in source.values() if r['reading_id'] == 'N0508')
    b = next(r for r in source.values() if r['reading_id'] == 'N0486')
    assert set(a['fields']) == set(b['fields']); checks += 1
    equal_fields = {f:a['fields'][f] == b['fields'][f] for f in a['fields']}
    assert all(equal_fields.values()); checks += 1
    v3clar = next(r for r in before if r['reading_id'] == 'N0486' and r['label_code'] == 'SK_PYTORCH')
    assert v3clar['Q'] == 'Z' and v3clar['revision_audit_id'] == 'A099'; checks += 1
    assert hashes == {str(p.relative_to(ROOT)).replace('\\', '/'):sha(p) for p in paths}; checks += 1
    with (OUT/'v4_overlay_independent_diff.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    report={'status':'PASS','independent_checks':checks,'changed_pairs':len(changed),
            'unchanged_pair_rows':len(old)-len(changed),'all_other_columns_unchanged':True,
            'Q_before':dict(Counter(r['Q'] for r in before)), 'Q_after':dict(Counter(r['Q'] for r in after)),
            'before_after_and_inputs_sha256':hashes,'all_inputs_unchanged_during_verification':True,
            'five_corrections_match_complete_U_review':True,
            'two_corrections_match_bounded_parenthetical_review':True,
            'N0508_N0486_all_captured_body_fields_identical':equal_fields,
            'old_A099_propagation_verified':True,'independent_human_validation':False,
            'scope':'Arithmetic/source-provenance verification of seven adopted model-review corrections; no production script imported.'}
    (OUT/'v4_overlay_independent_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__ == '__main__': main()
