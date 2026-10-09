"""Reconstruct the historical discovery frame from immutable source ledgers.

This helper is used only by the two historical source-review reports. It does
not import any production analysis or depend on previously generated outputs.
"""
from pathlib import Path
from collections import defaultdict,Counter
import csv,json
ROOT=Path(__file__).resolve().parents[2]

def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def states():
    rows=read(ROOT/'source_snapshot/analysis/ad_technology_current.csv')
    changes=json.loads((ROOT/'data/v4_source_corrections_phase4.json').read_text(encoding='utf-8'))['changes']
    by={(r['identity_key'],r['label_code']):r for r in rows}
    assert len(changes)==5
    for c in changes:
        r=by[c['identity_key'],c['label_code']]
        for f in ['G','R','Q']:
            assert r[f]==c[f+'_before']
            r[f]=c[f+'_after']
        r['revised']='1';r['revision_audit_id']=c['audit_id']
    assert Counter(r['Q'] for r in rows)=={'P':170,'Z':285,'U':41}
    return rows

def example_increments(rows,evidence):
    branches=defaultdict(set)
    for e in evidence:
        if e['metric'] in ['GENERAL','REQUIRED']:branches[e['identity_key'],e['code']].add(e['branch'])
    old=json.loads((ROOT/'source_snapshot/data/analysis_revision_ledger.json').read_text(encoding='utf-8'))['changes']
    new=json.loads((ROOT/'data/v4_source_corrections_phase4.json').read_text(encoding='utf-8'))['changes']
    for c in old:branches[c['identity_key'],c['label_code']].add('EXAMPLE')
    for c in new:branches[c['identity_key'],c['label_code']].add(c['governing_relation'])
    result=[r for r in rows if r['task']=='ROBOT_MODEL' and r['Q']!='P' and 'EXAMPLE' in branches[r['identity_key'],r['label_code']]]
    assert len(result)==43
    return result
