"""Verify sealed release, build a new isolated result, compare data/docs/figures, publish last."""
from pathlib import Path
import argparse,json,hashlib,sys,shutil,tempfile,subprocess
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory():return {str(p.relative_to(ROOT)).replace('\\','/') for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=ROOT/'release_checksums.json'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--plot-deps');args=p.parse_args();out=Path(args.output).resolve()
 if out.exists():raise ValueError('REFUSE_OVERWRITE: '+str(out))
 seal=json.loads((ROOT/'release_checksums.json').read_text(encoding='utf-8'))
 if set(seal['files'])!=inventory():raise ValueError('RELEASE_INVENTORY_DRIFT')
 for rel,e in seal['files'].items():
  if sha(ROOT/rel)!=e['sha256']:raise ValueError('RELEASE_DRIFT: '+rel)
 out.parent.mkdir(parents=True,exist_ok=True)
 with tempfile.TemporaryDirectory(prefix='stage_c_repro_',dir=out.parent) as temp:
  work=Path(temp)/'result';work.mkdir();shutil.copytree(ROOT/'inputs',work/'inputs');shutil.copytree(ROOT/'scripts',work/'scripts',ignore=shutil.ignore_patterns('__pycache__'));shutil.copy2(ROOT/'input_lock.json',work/'input_lock.json');(work/'verification').mkdir()
  for script in ['analyze.py','figures.py','write_report.py','verify.py']:
   cmd=[sys.executable,'-X','utf8',str(work/'scripts'/script)]
   if script=='figures.py' and args.plot_deps:cmd+=['--deps',str(Path(args.plot_deps).resolve())]
   subprocess.run(cmd,check=True,capture_output=True,text=True,encoding='utf-8')
  files=[p for p in ROOT.rglob('*') if p.is_file() and (p.parent in [ROOT/'tables',ROOT/'charts'] or (p.parent==ROOT and p.name in ['REPORT.md','METHODS.md','DATA_DICTIONARY.md','index.html','summary.json','figure_manifest.json','workbook_data.json']))]
  checked=[]
  for f in sorted(files):
   rel=f.relative_to(ROOT);same=sha(f)==sha(work/rel)
   if not same:raise ValueError('REPRODUCTION_MISMATCH: '+str(rel))
   checked.append(str(rel).replace('\\','/'))
  # Workbook is a verified viewing export, copied unchanged. Core results above were recalculated.
  shutil.copytree(ROOT/'outputs',work/'outputs');shutil.copy2(ROOT/'verification/REPORT.md',work/'verification/REPORT.md')
  (work/'verification/reproduction.json').write_text(json.dumps({'n_byte_identical':len(checked),'files':checked,'workbook':'copied sealed viewing export, not regenerated'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  if out.exists():raise ValueError('OUTPUT_APPEARED_DURING_BUILD')
  work.rename(out)
 print(json.dumps({'output':str(out),'n_byte_identical':len(checked)},ensure_ascii=False))
if __name__=='__main__':main()
