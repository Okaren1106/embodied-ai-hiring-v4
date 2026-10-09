"""Make a private portable archive, verify every member, then reproduce from it."""
from pathlib import Path
import hashlib,json,zipfile,tempfile,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
ZIP=ROOT/'Embodied_AI_IJM_Research_v4.0.zip'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files=[ROOT/p for p in ['README.md','RESEARCH_PROTOCOL.md','REPRODUCE.py']]
for folder in ['source_snapshot','data','analysis','audit','literature','stages','extensions','release','work','review']:
    files.extend(p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
files.extend(p for p in (ROOT/'verification').iterdir() if p.is_file() and p.suffix in ['.json','.log'] and p.name!='final_package_verification.json')
files=sorted(set(files),key=lambda p:p.relative_to(ROOT).as_posix())
manifest={'package':'Embodied AI IJM research upgrade v4.0','private':True,
    'reproduction_entrypoint':'REPRODUCE.py','numeric_steps':20,
    'scope':'Current scientific working package; no submission or public release.',
    'files':[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]}
manifest_bytes=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
(ROOT/'PACKAGE_MANIFEST.json').write_bytes(manifest_bytes)
with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,p.relative_to(ROOT).as_posix())
    z.writestr('PACKAGE_MANIFEST.json',manifest_bytes)
target=Path(tempfile.mkdtemp(prefix='z_',dir=ROOT/'verification'))
with zipfile.ZipFile(ZIP) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(files)+1 and len(set(z.namelist()))==len(z.namelist())
    for name in z.namelist():
        dest=(target/name).resolve();assert target.resolve() in dest.parents
    z.extractall(target)
member_checks=[{'path':r['path'],'pass':(target/r['path']).stat().st_size==r['bytes'] and sha(target/r['path'])==r['sha256']} for r in manifest['files']]
assert all(r['pass'] for r in member_checks)
run=subprocess.run([sys.executable,'-X','utf8',str(target/'REPRODUCE.py')],cwd=target,text=True,encoding='utf-8',capture_output=True)
expected=json.loads((ROOT/'verification/isolated_reproduction.json').read_text(encoding='utf-8'))
comparisons=[{'path':r['path'],'identical':sha(target/r['path'])==r['expected']} for r in expected['comparisons']]
report={'pass':run.returncode==0 and all(r['identical'] for r in comparisons),
    'archive':ZIP.name,'archive_sha256':sha(ZIP),'archive_bytes':ZIP.stat().st_size,
    'archive_members':len(files)+1,'member_hash_checks':len(member_checks),'all_members_verified':all(r['pass'] for r in member_checks),
    'extracted_directory':str(target),'entrypoint_exit_code':run.returncode,
    'numeric_outputs_compared':len(comparisons),'comparisons':comparisons,'stdout':run.stdout,'stderr':run.stderr,
    'external_original_project_inputs_used':False,
    'report_location':'This report is adjacent to the archive, avoiding a self-referential archive checksum.'}
(ROOT/'verification/final_package_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['comparisons','stdout','stderr']}))
if run.returncode:print(run.stdout,run.stderr)
assert report['pass']
