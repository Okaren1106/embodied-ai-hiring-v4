from pathlib import Path
import subprocess,sys,tempfile,json
from integrity import sha,seal
R=Path(__file__).resolve().parents[1];BASE=R.parent
records=[]
def probe(src,out,reason,name):
 existed=out.exists();p=subprocess.run([sys.executable,str(R/'scripts/reproduce.py'),'--source',str(src),'--output',str(out)],capture_output=True,text=True,encoding='utf-8')
 assert p.returncode and reason in p.stderr,(name,p.stdout,p.stderr)
 if not existed:assert not out.exists()
 records.append({'test':name,'reason':reason,'rejected':True,'no_new_output':not out.exists() if not existed else 'existing directory left unchanged'})
probe(R,R,'REFUSE_OVERWRITE','existing_output')
with tempfile.TemporaryDirectory(prefix='astra_d_faults_',dir=BASE) as d:
 t=Path(d).resolve();assert t.is_relative_to(BASE.resolve())
 for test,expected in [('release_inventory','RELEASE_INVENTORY_DRIFT'),('input_release_hash','RELEASE_DRIFT'),('input_inner_lock','INPUT_DRIFT'),('evidence_inner_lock','EVIDENCE_DRIFT')]:
  src=t/test;src.mkdir();(src/'inputs').mkdir();(src/'evidence').mkdir();inp=src/'inputs/probe.txt';ev=src/'evidence/probe.txt'
  inp.write_text('locked input');ev.write_text('locked evidence')
  (src/'input_lock.json').write_text(json.dumps({'files':{'inputs/probe.txt':{'sha256':sha(inp)}}}),encoding='utf-8')
  (src/'evidence_lock.json').write_text(json.dumps({'files':{'evidence/probe.txt':{'sha256':sha(ev)}}}),encoding='utf-8');seal(src)
  if test=='release_inventory':(src/'unexpected.txt').write_text('extra')
  elif test=='input_release_hash':inp.write_text('drift')
  elif test=='input_inner_lock':inp.write_text('drift');seal(src)
  else:ev.write_text('drift');seal(src)
  probe(src,t/(test+'_output'),expected,test+'_minimal_sealed_fixture')
(R/'verification/release_faults.json').write_text(json.dumps({'passed':len(records),'failed':0,'fixture_scope':'minimal sealed fixtures exercise pre-execution guards; no live research input mutated','checks':records},ensure_ascii=False,indent=2),encoding='utf-8')
print('D fault guards',len(records),'passed')
