"""Apply declared source-supported corrections in a new analysis layer.

The v3 source snapshot is immutable. This step never re-estimates labels or
infers a correction from an aggregate. Each change requires a saved full-source
quote, original state, after state, reason and governing relation.
"""
from pathlib import Path
from collections import Counter
import csv, json, hashlib

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'source_snapshot'

def main():
    ledger_path = ROOT / 'data/v4_source_corrections.json'
    ledger = json.loads(ledger_path.read_text(encoding='utf-8'))
    source_path = SNAPSHOT / 'analysis/ad_technology_current.csv'
    with source_path.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    records = json.loads((SNAPSHOT / 'source_v2/data/inputs/records.json').read_text(encoding='utf-8'))
    sources = {r['identity_key']:r for r in records}
    lookup = {(r['identity_key'],r['label_code']):r for r in rows}
    assert len(lookup)==len(rows)==496
    before = Counter(r['Q'] for r in rows)
    changed = []
    seen = set()
    for c in ledger['changes']:
        key = c['identity_key'],c['label_code']
        assert key not in seen
        seen.add(key)
        r=lookup[key];src=sources[c['identity_key']]
        assert r['reading_id']==c['reading_id']
        text=src['fields'][c['source_field']]
        assert hashlib.sha256(text.encode('utf-8')).hexdigest()==c['source_field_sha256']
        assert text[c['source_start']:c['source_end']]==c['source_quote']
        assert c['reason'] and c['governing_relation'] in ['EXAMPLE','CHOICE','CHOICE_AND_EXAMPLE','UNCONDITIONAL_OR_EXAMPLE']
        if c.get('identical_full_source_to'):
            other=next(x for x in records if x['reading_id']==c['identical_full_source_to'])
            assert src['fields']['full_description']==other['fields']['full_description']
        old=dict(r)
        for state in ['G','R','Q']:
            assert r[state]==c[state+'_before']
            assert c[state+'_after'] in ['P','Z','U']
            r[state]=c[state+'_after']
        assert r['Q']==('P' if 'P' in [r['G'],r['R']] else 'Z' if r['G']==r['R']=='Z' else 'U')
        r['revised']='1';r['revision_audit_id']=c['audit_id']
        # Historical flags and original states remain explicit provenance.
        assert all(r[k]==old[k] for k in old if k not in ['G','R','Q','revised','revision_audit_id'])
        changed.append({'reading_id':r['reading_id'],'label_code':r['label_code'],
                        'audit_id':c['audit_id'],'Q_before':old['Q'],'Q_after':r['Q']})
    out=ROOT/'analysis';out.mkdir(exist_ok=True)
    with (out/'v4_ad_technology_current.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    report={'rows':len(rows),'advertisements':len(sources),'before':dict(before),
            'after':dict(Counter(r['Q'] for r in rows)),'changes':changed,
            'frozen_source_unchanged':hashlib.sha256(source_path.read_bytes()).hexdigest()==ledger['v3_states_sha256'],
            'independent_human_recoding':False,'failures':0}
    assert report['frozen_source_unchanged']
    (out/'v4_overlay_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
