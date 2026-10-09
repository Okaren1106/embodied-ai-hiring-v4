"""Complete packaging reproduce for Stage C. Does not modify the original sealed package."""
COMPLETE_PACKAGING='COMPLETE_V1_REPRO01_FIX'
from pathlib import Path
import argparse,json,hashlib,sys,shutil,tempfile,subprocess
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root):
 return {str(p.relative_to(root)).replace('\\','/') for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=root/'release_checksums.json'}
def write_checksums(root):
 files={rel:{'sha256':sha(root/rel),'bytes':(root/rel).stat().st_size} for rel in sorted(inventory(root))}
 (root/'release_checksums.json').write_text(json.dumps({'n_files':len(files),'packaging':COMPLETE_PACKAGING,'files':files},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--plot-deps');p.add_argument('--source',help='Sealed source package; default is this file\'s package root')
 args=p.parse_args();here=Path(__file__).resolve();ROOT=Path(args.source).resolve() if args.source else here.parents[1];out=Path(args.output).resolve()
 if out.exists():raise ValueError('REFUSE_OVERWRITE: '+str(out))
 seal_path=ROOT/'release_checksums.json'
 if not seal_path.is_file():raise ValueError('MISSING_RELEASE_CHECKSUMS')
 seal=json.loads(seal_path.read_text(encoding='utf-8'))
 if set(seal['files'])!=inventory(ROOT):raise ValueError('RELEASE_INVENTORY_DRIFT')
 for rel,e in seal['files'].items():
  if sha(ROOT/rel)!=e['sha256']:raise ValueError('RELEASE_DRIFT: '+rel)
 out.parent.mkdir(parents=True,exist_ok=True)
 self_src=here.read_bytes()
 with tempfile.TemporaryDirectory(prefix='stage_c_repro_',dir=str(out.parent)) as temp:
  work=Path(temp)/'result';work.mkdir()
  shutil.copytree(ROOT/'inputs',work/'inputs');shutil.copytree(ROOT/'scripts',work/'scripts',ignore=shutil.ignore_patterns('__pycache__'))
  (work/'scripts'/'reproduce.py').write_bytes(self_src)
  shutil.copy2(ROOT/'input_lock.json',work/'input_lock.json')
  if (ROOT/'README.md').is_file():shutil.copy2(ROOT/'README.md',work/'README.md')
  (work/'verification').mkdir(exist_ok=True)
  for script in ['analyze.py','figures.py','write_report.py','verify.py']:
   cmd=[sys.executable,'-X','utf8',str(work/'scripts'/script)]
   if script=='figures.py' and args.plot_deps:cmd+=['--deps',str(Path(args.plot_deps).resolve())]
   r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8')
   if r.returncode!=0:
    sys.stderr.write(r.stdout or '');sys.stderr.write(r.stderr or '')
    raise SystemExit(script+' failed: '+str(r.returncode))
  names=['REPORT.md','METHODS.md','DATA_DICTIONARY.md','index.html','summary.json','figure_manifest.json','workbook_data.json']
  files=[p for p in ROOT.rglob('*') if p.is_file() and (p.parent in [ROOT/'tables',ROOT/'charts'] or (p.parent==ROOT and p.name in names))]
  checked=[]
  for f in sorted(files):
   rel=f.relative_to(ROOT)
   if sha(f)!=sha(work/rel):raise ValueError('REPRODUCTION_MISMATCH: '+str(rel))
   checked.append(str(rel).replace('\\','/'))
  shutil.copytree(ROOT/'outputs',work/'outputs')
  shutil.copy2(ROOT/'verification'/'REPORT.md',work/'verification'/'REPORT.md')
  (work/'verification'/'reproduction.json').write_text(json.dumps({'n_byte_identical':len(checked),'files':checked,'workbook':'copied sealed viewing export, not regenerated','packaging':COMPLETE_PACKAGING,'source':str(ROOT)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  readme=(work/'README.md').read_text(encoding='utf-8') if (work/'README.md').is_file() else '# Q1—Q3 正式分析接续包\n'
  if '## 完整接续包装（REPRO-01 另版修复）' not in readme:
   readme+='\n\n## 完整接续包装（REPRO-01 另版修复）\n\n本目录由完整包装复算入口生成，含 README、scripts、inputs、input_lock 及本目录自身的 release_checksums.json。表、图与报告与来源包逐字节一致；release_checksums.json 是新目录文件清单，不是来源包清单的复制。\n'
   (work/'README.md').write_text(readme,encoding='utf-8')
  write_checksums(work)
  if out.exists():raise ValueError('OUTPUT_APPEARED_DURING_BUILD')
  work.rename(out)
 print(json.dumps({'output':str(out),'n_byte_identical':len(checked),'packaging':COMPLETE_PACKAGING},ensure_ascii=False))
if __name__=='__main__':main()
