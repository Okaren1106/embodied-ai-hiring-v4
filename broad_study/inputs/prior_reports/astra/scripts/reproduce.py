"""Atomic, closed-input reproduction; every resulting directory is itself reproducible."""
from pathlib import Path
import json,sys,subprocess,shutil,tempfile,argparse,os
from integrity import verify,seal,verify_evidence,sha
def main():
 p=argparse.ArgumentParser();p.add_argument('--source');p.add_argument('--output',required=True);p.add_argument('--plot-deps');a=p.parse_args()
 root=Path(a.source).resolve() if a.source else Path(__file__).resolve().parents[1];out=Path(a.output).resolve()
 if out.exists():raise ValueError('REFUSE_OVERWRITE: '+str(out))
 if out.is_relative_to(root):raise ValueError('OUTPUT_MUST_BE_OUTSIDE_SOURCE')
 verify(root);verify_evidence(root)
 for rel,v in json.loads((root/'input_lock.json').read_text(encoding='utf-8'))['files'].items():
  if sha(root/rel)!=v['sha256']:raise ValueError('INPUT_DRIFT: '+rel)
 out.parent.mkdir(parents=True,exist_ok=True)
 with tempfile.TemporaryDirectory(prefix='astra_repro_',dir=out.parent) as d:
  temp=Path(d).resolve();assert temp.is_relative_to(out.parent)
  work=temp/'package';work.mkdir()
  for name in ['inputs','evidence','scripts']:
   shutil.copytree(root/name,work/name,ignore=shutil.ignore_patterns('__pycache__'))
  for name in ['input_lock.json','evidence_lock.json','ANALYSIS_DECISIONS.md','README.md']:shutil.copy2(root/name,work/name)
  (work/'verification').mkdir();(work/'tables').mkdir();(work/'charts').mkdir()
  scripts=['analyze_basics.py','analyze_joint.py','analyze_sensitivity.py','extract_case_jobs.py','build_T5.py','analyze_case_subsets.py','finalize_analysis.py','figures.py','write_report.py','verify_independent.py']
  for name in scripts:
   cmd=[sys.executable,'-X','utf8',str(work/'scripts'/name)]
   if name=='figures.py' and a.plot_deps:cmd+=['--plot-deps',str(Path(a.plot_deps).resolve())]
   env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env['PYTHONHASHSEED']='0'
   r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env)
   if r.returncode:
    sys.stderr.write(r.stdout[-3000:]+r.stderr[-5000:]);raise RuntimeError('BUILD_FAILED: '+name)
  verify_evidence(work)
  keys=sorted([p.relative_to(root).as_posix() for p in (root/'tables').glob('*.csv')]+[p.relative_to(root).as_posix() for p in (root/'charts').glob('*') if p.is_file()]+['REPORT.md','METHODS.md','DATA_DICTIONARY.md','verification/independent_checks.json','evidence/case_jobs_reading.md'])
  for rel in keys:
   if not (work/rel).is_file() or sha(root/rel)!=sha(work/rel):raise ValueError('REPRODUCTION_MISMATCH: '+rel)
  # Viewing export and author QA history are copied, never advertised as new independent review.
  shutil.copytree(root/'document',work/'document')
  for f in (root/'verification').iterdir():
   if f.is_file() and f.name not in ['independent_checks.json','reproduction.json']:shutil.copy2(f,work/'verification'/f.name)
  rec={'source_package':root.name,'n_byte_identical':len(keys),'files':keys,'independent_calculation_checks':21,'word_export':'copied sealed viewing artifact; not repaginated','external_network_used':False,'complete_continuation_package':True}
  (work/'verification/reproduction.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');seal(work);verify(work)
  if out.exists():raise ValueError('OUTPUT_APPEARED_DURING_BUILD')
  work.rename(out)
 print(json.dumps({'output':str(out),'n_byte_identical':len(keys),'status':'PASS'},ensure_ascii=False))
if __name__=='__main__':main()
