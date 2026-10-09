from pathlib import Path
import json,hashlib,shutil,subprocess,sys,os,csv
from datetime import datetime,timezone
src=Path(__file__).resolve().parents[1]
suffix=sys.argv[1] if len(sys.argv)>1 else ''
assert not suffix or all(c.isalnum() or c=='_' for c in suffix)
dest=src.parent/('reproduction_astra_v3_20260918'+suffix)
assert not dest.exists(),'Use a fresh physical directory; never delete prior reproduction.'
dest.mkdir()
for folder in ['inputs','configs','notes','review','scripts']:
 for p in (src/folder).rglob('*'):
  assert not p.is_symlink() and not (hasattr(os.path,'isjunction') and os.path.isjunction(p)),str(p)
 shutil.copytree(src/folder,dest/folder)
for name in ['input_manifest.json']:
 shutil.copy2(src/name,dest/name)
(dest/'tables').mkdir();(dest/'verification').mkdir();(dest/'reports').mkdir()
# Seed and inherited module tables are physical copies; rebuilt outputs are excluded.
for p in (src/'tables').glob('*.csv'):
 if p.name.startswith(('Q4_','Q5_','V3_two_layer_')) or p.name in ['Q3_ads_final.csv','Q3_evidence_final.csv','Q3_states_final.csv','Q3_astra_changes.csv','Q3_review_receipts.csv']:continue
 shutil.copy2(p,dest/'tables'/p.name)
for name in ['materialize_astra_final.py','compute_astra_final.py','compute_v3_two_layers.py']:
 print('REPRODUCE',name,flush=True)
 subprocess.run([sys.executable,'-B','-X','utf8',str(dest/'scripts'/name)],check=True,stdout=(dest/'verification'/('log_'+name+'.txt')).open('w',encoding='utf-8'),stderr=subprocess.STDOUT)
names=['Q3_ads_final.csv','Q3_evidence_final.csv','Q3_states_final.csv','Q3_astra_changes.csv','Q3_review_receipts.csv']+[p.name for p in (src/'tables').glob('Q4_*final.csv')]+['Q4_scope_membership.csv','Q4_scope_definitions.csv','Q4_dedup_membership.csv','Q4_display_selection.csv']+[p.name for p in (src/'tables').glob('V3_two_layer_*.csv')]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
res=[]
for n in sorted(set(names)):
 a=sha(src/'tables'/n);b=sha(dest/'tables'/n);res.append(dict(file=n,working_sha256=a,isolated_sha256=b,equal=a==b));assert a==b,n
original=src.parent/'run_20260916_astra_v2'
baseline=json.loads((src/'review/submission_baseline_manifest.json').read_text(encoding='utf-8'))
drift=[a['path'] for a in baseline if sha(original/a['path'])!=a['sha256']]
assert not drift,drift
result=dict(status='PASS',method='Physical copied inputs configurations review transactions and scripts; full output byte hashes; no junctions',created_utc=datetime.now(timezone.utc).isoformat(),isolated_directory=str(dest),files=res,original_submission_files_checked=len(baseline),original_submission_drift=drift)
(src/'verification/astra_isolated_reproduction.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS',len(res),'output hashes;',len(baseline),'original hashes',flush=True)
