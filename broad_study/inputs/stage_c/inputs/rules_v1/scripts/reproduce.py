"""Verify sealed version; rebuild in isolation; publish only to a new destination."""
from pathlib import Path
import json,hashlib,sys,subprocess,shutil,tempfile,argparse
R=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);a=ap.parse_args();dest=Path(a.output).resolve()
 if dest.exists():raise SystemExit('Refusing to overwrite existing output: '+str(dest))
 if dest==R or R in dest.parents:raise SystemExit('Output must be outside the sealed source package.')
 if not dest.parent.is_dir():raise SystemExit('Output parent must already exist.')
 lock=R/'release_checksums.json'
 if not lock.is_file():raise SystemExit('Missing release checksums.')
 release=json.loads(lock.read_text(encoding='utf-8'))
 actual={p.relative_to(R).as_posix() for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='release_checksums.json'}
 if actual!=set(release['files']):raise SystemExit('Release inventory drift: missing or unlisted files.')
 for rel,e in release['files'].items():
  p=R/rel
  if not p.is_file() or sha(p)!=e['sha256'] or p.stat().st_size!=e['bytes']:raise SystemExit('Release drift: '+rel)
 staging=Path(tempfile.mkdtemp(prefix='.'+dest.name+'-building-',dir=dest.parent)).resolve()
 # A checked single-parent temporary tree is the only cleanup target.
 assert staging.parent==dest.parent and staging.name.startswith('.'+dest.name+'-building-') and staging!=R
 try:
  shutil.copytree(R,staging,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
  expected={p.relative_to(R).as_posix():sha(p) for p in R.glob('*.csv')}
  expected.update({p.relative_to(R).as_posix():sha(p) for p in (R/'diagnostics').iterdir() if p.is_file()})
  expected.update({p.relative_to(R).as_posix():sha(p) for p in R.glob('*.md')})
  for n in ['index.html','comparison_registry.json']:expected[n]=sha(R/n)
  for script in ['build_rules.py','write_reports.py','verify_rules.py']:
   cp=subprocess.run([sys.executable,'-B','-X','utf8',str(staging/'scripts'/script)],cwd=staging,capture_output=True,text=True,encoding='utf-8')
   if cp.returncode:raise RuntimeError(script+' failed: '+cp.stdout+'\n'+cp.stderr)
  changed=[rel for rel,h in expected.items() if sha(staging/rel)!=h]
  if changed:raise RuntimeError('Rebuild differs: '+str(changed))
  if dest.exists():raise RuntimeError('Destination appeared during build; refusing to overwrite.')
  staging.rename(dest)
  print(json.dumps({'status':'REPRODUCED','output':str(dest),'identical_derived_files':len(expected),'verification':json.loads((dest/'verification/result.json').read_text(encoding='utf-8'))['n_pass']},ensure_ascii=False))
 except BaseException:
  if staging.exists():
   assert staging.parent==dest.parent and staging.name.startswith('.'+dest.name+'-building-') and staging!=R
   shutil.rmtree(staging)
  raise
if __name__=='__main__':run()
