"""Reproduce from a fresh local directory and compare the published outputs."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(4*1024*1024), b''): h.update(block)
    return h.hexdigest()

def main():
    kind = sys.argv[1] if len(sys.argv)>1 else 'v4'
    assert kind in {'v4','broad'}, 'Use v4 or broad'
    runs = ROOT/'_reproduction'
    runs.mkdir(exist_ok=True)
    target = Path(tempfile.mkdtemp(prefix=kind+'-', dir=runs))
    if kind=='v4':
        source = ROOT/'paper_v4'
        for folder in ['source_snapshot','data','extensions','work']:
            shutil.copytree(source/folder, target/folder, ignore=shutil.ignore_patterns('__pycache__','outputs'))
        shutil.copy2(source/'REPRODUCE.py', target/'REPRODUCE.py')
        subprocess.run([sys.executable,'-B','-X','utf8',str(target/'REPRODUCE.py')],cwd=target,check=True)
        names = [p.relative_to(target).as_posix() for folder in ['analysis','extensions/framework_control/outputs']
            for p in (target/folder).rglob('*') if p.is_file() and p.suffix in {'.csv','.json'}]
    else:
        from restore_large_files import restore
        restore()
        source = ROOT/'broad_study'
        for folder in ['inputs','configs','notes','review','scripts']:
            shutil.copytree(source/folder, target/folder, ignore=shutil.ignore_patterns('__pycache__','*.gz'))
        shutil.copy2(source/'input_manifest.json',target/'input_manifest.json')
        for folder in ['tables','verification','reports']: (target/folder).mkdir()
        regenerated = {'Q3_ads_final.csv','Q3_evidence_final.csv','Q3_states_final.csv','Q3_astra_changes.csv','Q3_review_receipts.csv'}
        for p in (source/'tables').glob('*.csv'):
            if p.name.startswith(('Q4_','Q5_','V3_two_layer_')) or p.name in regenerated: continue
            shutil.copy2(p,target/'tables'/p.name)
        for script in ['materialize_astra_final.py','compute_astra_final.py','compute_v3_two_layers.py']:
            print('REPRODUCE',script,flush=True)
            with (target/'verification'/('log_'+script+'.txt')).open('w',encoding='utf-8') as log:
                subprocess.run([sys.executable,'-B','-X','utf8',str(target/'scripts'/script)],cwd=target,stdout=log,stderr=subprocess.STDOUT,check=True)
        names = ['tables/'+name for name in sorted(regenerated)]
        names += ['tables/'+p.name for p in (source/'tables').glob('Q4_*final.csv')]
        names += ['tables/'+name for name in ['Q4_scope_membership.csv','Q4_scope_definitions.csv','Q4_dedup_membership.csv','Q4_display_selection.csv']]
        names += ['tables/'+p.name for p in (source/'tables').glob('V3_two_layer_*.csv')]
    rows = []
    for name in sorted(set(names)):
        expected,actual = sha(source/name),sha(target/name)
        rows.append({'path':name,'expected_sha256':expected,'actual_sha256':actual,'identical':expected==actual})
    report = {'study':kind,'status':'PASS' if all(x['identical'] for x in rows) else 'FAIL','outputs':len(rows),'working_directory':str(target),'comparisons':rows}
    (target/'REPRODUCTION_RECEIPT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='comparisons'},ensure_ascii=False))
    assert report['status']=='PASS', [x['path'] for x in rows if not x['identical']]

if __name__ == '__main__': main()
