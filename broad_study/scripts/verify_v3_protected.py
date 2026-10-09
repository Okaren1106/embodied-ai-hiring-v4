from common import *
from datetime import datetime,timezone
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
counts={};counts['frozen_inputs_and_originals']=lock_check(originals=True)
prev=ROOT.parent/'run_20260916_astra_m5_m6_final'
m=json.loads((ROOT/'baseline_v2/publication_manifest.json').read_text(encoding='utf-8'))
errors=[]
for x in m['files']:
 if sha(prev/x['path'])!=x['sha256']:errors.append(x['path'])
assert not errors,errors
counts['sealed_astra_v2_files']=len(m['files'])
assert sha(prev/'publication_manifest.json')==sha(ROOT/'baseline_v2/publication_manifest.json')
gm=json.loads((ROOT/'review/submission_baseline_manifest.json').read_text(encoding='utf-8'))
grok=ROOT.parent/'run_20260916_astra_v2'
for x in gm:assert sha(grok/x['path'])==x['sha256'],x['path']
counts['grok_submission_files']=len(gm)
save_json('verification/V3_protected_inputs.json',dict(status='PASS',counts=counts,drift=[],created_utc=datetime.now(timezone.utc).isoformat()))
print(js(counts))
