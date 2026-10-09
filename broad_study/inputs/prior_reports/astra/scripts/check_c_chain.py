from pathlib import Path
import json,hashlib,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent;PY=sys.executable
first=ROOT/'inputs/stage_c';second=BASE/'repro_c_second';third=BASE/'repro_c_third'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
for target in [second,third]:
 seal=json.loads((target/'release_checksums.json').read_text(encoding='utf-8'))
 assert all(sha(target/k)==v['sha256'] for k,v in seal['files'].items())
 r=json.loads((target/'verification/reproduction.json').read_text(encoding='utf-8'))
 assert r['n_byte_identical']==60
 assert all(sha(first/k)==sha(target/k) for k in r['files'])
 checks.append({'target':target.name,'data_report_chart_byte_identical':60,'self_manifest_valid':True})
assert (second/'README.md').read_bytes()==(third/'README.md').read_bytes()
r=subprocess.run([PY,str(ROOT/'scripts/c_reproduce.py'),'--source',str(second),'--output',str(third)],capture_output=True,text=True)
assert r.returncode and 'REFUSE_OVERWRITE' in r.stderr
faults=[{'test':'existing_output','rejected':True,'reason':'REFUSE_OVERWRITE'}]
# Minimal self-contained sealed fixture exercises the same pre-execution hash guard.
with tempfile.TemporaryDirectory(prefix='astra_c_fault_',dir=BASE) as d:
 t=Path(d).resolve();assert t.is_relative_to(BASE.resolve())
 src=t/'sealed';src.mkdir();(src/'inputs').mkdir();f=src/'inputs/probe.txt';f.write_text('frozen input',encoding='utf-8')
 (src/'release_checksums.json').write_text(json.dumps({'files':{'inputs/probe.txt':{'sha256':sha(f)}}}),encoding='utf-8')
 f.write_text('drifted input',encoding='utf-8');out=t/'must_not_exist'
 r=subprocess.run([PY,str(ROOT/'scripts/c_reproduce.py'),'--source',str(src),'--output',str(out)],capture_output=True,text=True)
 assert r.returncode and 'RELEASE_DRIFT' in r.stderr and not out.exists()
 faults.append({'test':'input_hash_drift_minimal_sealed_fixture','rejected':True,'reason':'RELEASE_DRIFT','no_output_published':True})
(ROOT/'verification/c_chain_checks.json').write_text(json.dumps({'checks':checks,'README_second_third_identical':True,'faults':faults,'originals_modified':False},indent=2),encoding='utf-8')
print('C chain 2 x 60; manifests; README; 2 fault tests passed')
