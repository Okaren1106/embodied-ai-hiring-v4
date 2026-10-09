"""Verify the complete pre-upgrade v3 baseline without rewriting it."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
old=ROOT.parent/'analysis_E_english_v3_0'
manifest=json.loads((ROOT/'verification/v3_protection_baseline.json').read_text(encoding='utf-8'))
checks=[]
for r in manifest:
    p=old/r['path']
    actual=hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None
    checks.append({'path':r['path'],'sha256':actual,'unchanged':actual==r['sha256'] and p.stat().st_size==r['bytes']})
report={'protected_files':len(checks),'all_unchanged':all(r['unchanged'] for r in checks),'files':checks}
(ROOT/'verification/v3_protection_verified.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'protected_files':len(checks),'all_unchanged':report['all_unchanged']}))
assert report['all_unchanged']
