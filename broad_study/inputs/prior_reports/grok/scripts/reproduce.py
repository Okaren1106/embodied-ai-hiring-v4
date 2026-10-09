"""Stage D packaging reproduce. Refuses overwrite and input/release drift. Does not modify sealed A/B/C."""
COMPLETE_PACKAGING='STAGE_D_COMPLETE_V1'
from pathlib import Path
import argparse,json,hashlib,sys,shutil,tempfile,subprocess,os
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root):
 skip={'__pycache__'}
 return {str(p.relative_to(root)).replace('\\','/') for p in root.rglob('*') if p.is_file() and not any(x in p.parts for x in skip) and p.name!='release_checksums.json'}
def write_checksums(root):
 files={rel:{'sha256':sha(root/rel),'bytes':(root/rel).stat().st_size} for rel in sorted(inventory(root))}
 (root/'release_checksums.json').write_text(json.dumps({'n_files':len(files),'packaging':COMPLETE_PACKAGING,'researcher':'Cursor Grok 4.6','report_mark':'grok4.6研究','files':files},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
 p=argparse.ArgumentParser();p.add_argument('--output');p.add_argument('--plot-deps');p.add_argument('--source');p.add_argument('--seal-current',action='store_true')
 args=p.parse_args();here=Path(__file__).resolve();ROOT=Path(args.source).resolve() if args.source else here.parents[1]
 if args.seal_current:
  if not (ROOT/'REPORT.md').is_file() or not (ROOT/'verification'/'REPORT.md').is_file():raise ValueError('SEAL_REQUIRES_COMPLETED_RUN')
  write_checksums(ROOT)
  print(json.dumps({'sealed':str(ROOT),'n_files':json.loads((ROOT/'release_checksums.json').read_text(encoding='utf-8'))['n_files'],'packaging':COMPLETE_PACKAGING},ensure_ascii=False))
  return
 if not args.output:raise ValueError('output required unless --seal-current')
 out=Path(args.output).resolve()
 if out.exists():raise ValueError('REFUSE_OVERWRITE: '+str(out))
 seal_path=ROOT/'release_checksums.json'
 if not seal_path.is_file():raise ValueError('MISSING_RELEASE_CHECKSUMS')
 seal=json.loads(seal_path.read_text(encoding='utf-8'))
 if set(seal['files'])!=inventory(ROOT):raise ValueError('RELEASE_INVENTORY_DRIFT')
 for rel,e in seal['files'].items():
  if sha(ROOT/rel)!=e['sha256']:raise ValueError('RELEASE_DRIFT: '+rel)
 out.parent.mkdir(parents=True,exist_ok=True)
 self_src=here.read_bytes()
 with tempfile.TemporaryDirectory(prefix='stage_d_repro_',dir=str(out.parent)) as temp:
  work=Path(temp)/'result';work.mkdir()
  shutil.copytree(ROOT/'inputs',work/'inputs');shutil.copytree(ROOT/'scripts',work/'scripts',ignore=shutil.ignore_patterns('__pycache__'))
  (work/'scripts'/'reproduce.py').write_bytes(self_src)
  shutil.copy2(ROOT/'input_lock.json',work/'input_lock.json')
  if (ROOT/'README.md').is_file():shutil.copy2(ROOT/'README.md',work/'README.md')
  (work/'verification').mkdir(exist_ok=True)
  env=os.environ.copy();env['PYTHONHASHSEED']='0'
  for script in ['analyze.py','figures.py','write_report.py','verify.py']:
   cmd=[sys.executable,'-X','utf8',str(work/'scripts'/script)]
   if script=='figures.py' and args.plot_deps:cmd+=['--deps',str(Path(args.plot_deps).resolve())]
   r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env)
   if r.returncode!=0:
    sys.stderr.write(r.stdout or '');sys.stderr.write(r.stderr or '')
    raise SystemExit(script+' failed: '+str(r.returncode))
  names=['REPORT.md','METHODS.md','DATA_DICTIONARY.md','index.html','summary.json','figure_manifest.json','case_selection.json']
  files=[p for p in ROOT.rglob('*') if p.is_file() and (p.parent in [ROOT/'tables',ROOT/'charts'] or (p.parent==ROOT and p.name in names) or (p.parent==ROOT/'verification' and p.name in ['REPORT.md','data_checks.json','plot_environment.json']))]
  checked=[]
  for f in sorted(files):
   rel=f.relative_to(ROOT)
   if not (work/rel).is_file():raise ValueError('MISSING_IN_REPRODUCTION: '+str(rel))
   if sha(f)!=sha(work/rel):raise ValueError('REPRODUCTION_MISMATCH: '+str(rel))
   checked.append(str(rel).replace('\\','/'))
  (work/'verification'/'reproduction.json').write_text(json.dumps({'n_byte_identical':len(checked),'files':checked,'packaging':COMPLETE_PACKAGING,'source':str(ROOT),'researcher':'Cursor Grok 4.6'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  readme=(work/'README.md').read_text(encoding='utf-8') if (work/'README.md').is_file() else '# 阶段D结果包\n'
  if COMPLETE_PACKAGING not in readme:
   readme+='\n\n## 完整接续包装\n\n本目录由阶段D复算入口生成，含 README、scripts、inputs、input_lock 及本目录自身的 release_checksums.json。表、图、报告与核验文件与来源包逐字节一致；release_checksums.json 是新目录清单。研究标记：grok4.6研究。\n'
   (work/'README.md').write_text(readme,encoding='utf-8')
  write_checksums(work)
  if out.exists():raise ValueError('OUTPUT_APPEARED_DURING_BUILD')
  work.rename(out)
 print(json.dumps({'output':str(out),'n_byte_identical':len(checked),'packaging':COMPLETE_PACKAGING},ensure_ascii=False))
if __name__=='__main__':main()
