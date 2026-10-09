"""Rebuild the packaged numerical workflows with no original project inputs."""
from pathlib import Path
import json,hashlib,shutil,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]
target=Path(tempfile.mkdtemp(prefix='v4-isolated-',dir=ROOT/'verification'))
shutil.copytree(ROOT/'source_snapshot',target/'source_snapshot')
shutil.copytree(ROOT/'data',target/'data')
shutil.copytree(ROOT/'extensions',target/'extensions',ignore=shutil.ignore_patterns('outputs','__pycache__'))
shutil.copytree(ROOT/'work',target/'work',ignore=shutil.ignore_patterns('__pycache__','sol','discordant_source_packet.json'))
shutil.copy2(ROOT/'REPRODUCE.py',target/'REPRODUCE.py')
# Only generated outputs of the declared numeric entrypoint are compared.
r=subprocess.run([sys.executable,'-X','utf8',str(target/'REPRODUCE.py')],cwd=target,text=True,encoding='utf-8',capture_output=True)
report={'isolated_directory':str(target),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,
        'comparisons':[],'original_project_inputs_used':False}
generated=list((target/'analysis').rglob('*'))+list((target/'extensions/framework_control/outputs').rglob('*'))
for p in sorted(generated):
    if not p.is_file() or p.suffix not in ['.csv','.json']:continue
    name=p.relative_to(target).as_posix()
    original=ROOT/name
    digest=hashlib.sha256(original.read_bytes()).hexdigest() if original.exists() else None
    report['comparisons'].append({'path':name,'expected':digest,
                                  'actual':hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None,
                                  'identical':original.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==digest})
report['pass']=r.returncode==0 and all(x['identical'] for x in report['comparisons'])
(ROOT/'verification/isolated_reproduction.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pass':report['pass'],'files':len(report['comparisons']),
                  'mismatches':[x['path'] for x in report['comparisons'] if not x['identical']]}))
assert report['pass']
