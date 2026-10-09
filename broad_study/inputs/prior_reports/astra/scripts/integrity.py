from pathlib import Path
import json,hashlib
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root):return {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=root/'release_checksums.json'}
def seal(root):
 fs={n:{'sha256':sha(root/n),'bytes':(root/n).stat().st_size} for n in sorted(inventory(root))}
 (root/'release_checksums.json').write_text(json.dumps({'package':'ASTRA_STAGE_D_V1','n_files':len(fs),'files':fs},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 return len(fs)
def verify(root):
 s=json.loads((root/'release_checksums.json').read_text(encoding='utf-8'))
 if set(s['files'])!=inventory(root):raise ValueError('RELEASE_INVENTORY_DRIFT')
 for rel,v in s['files'].items():
  p=(root/rel).resolve()
  if not p.is_relative_to(root.resolve()):raise ValueError('UNSAFE_RELEASE_PATH')
  if sha(p)!=v['sha256']:raise ValueError('RELEASE_DRIFT: '+rel)
 return len(s['files'])
def lock_evidence(root):
 fs={p.relative_to(root).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted((root/'evidence').rglob('*')) if p.is_file()}
 (root/'evidence_lock.json').write_text(json.dumps({'read_date':'2026-09-16','files':fs},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def verify_evidence(root):
 for rel,v in json.loads((root/'evidence_lock.json').read_text(encoding='utf-8'))['files'].items():
  if sha(root/rel)!=v['sha256']:raise ValueError('EVIDENCE_DRIFT: '+rel)

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('mode',choices=['seal','verify','lock-evidence']);a=p.parse_args();r=Path(__file__).resolve().parents[1]
 print(seal(r) if a.mode=='seal' else verify(r) if a.mode=='verify' else lock_evidence(r))
