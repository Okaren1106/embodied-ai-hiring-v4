from pathlib import Path
import json, hashlib, shutil
ROOT=Path(r'D:\Embod AI analysis')
REPO=ROOT/'embodied-ai-hiring-research'
BASE=REPO/'reports/2026-09-14_company_data_analysis'
OLD=BASE/'stage_b_targeted/run_20260915T030000Z'
AUDIT=BASE/'stage_b_targeted_acceptance/run_20260915T030000Z'
R2=BASE/'stage_b_repair_r2/run_20260915T020000Z'
RUN=BASE/'stage_b_evidence_integrated/run_20260915T064258Z'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def save(p,d):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':
 assert not RUN.exists(), 'Refuse overwrite'
 shutil.copytree(OLD,RUN,ignore=shutil.ignore_patterns('__pycache__'))
 (RUN/'repair_records').mkdir(exist_ok=True)
 before={str(p):sha(p) for d in [OLD,AUDIT,R2,BASE/'stage_a_r3',REPO/'data/research',REPO/'outputs/reference-expansion-2026-09-11/accepted-reference1654-v1-2026-09-14',REPO/'docs'] for p in d.rglob('*') if p.is_file() and '__pycache__' not in str(p)}
 save(RUN/'repair_records/protected_before.json',before)
 for i,p in enumerate([ROOT/'必读.md',REPO/'必读.md',BASE/'EXECUTION_PLAN.md']):shutil.copy2(p,RUN/f'repair_records/progress_before_{i}.md')
 for n in ['RELEASE_OK','release_gate_status.json','release_checksums.json','output_checksums.json']:
  (RUN/n).unlink(missing_ok=True)
 shutil.copy2(AUDIT/'supplement_sources.json',RUN/'work/supplement_sources.json')
 save(REPO/'.b5repair/paths.json',{'run':str(RUN),'old':str(OLD),'audit':str(AUDIT),'r2':str(R2)})
 print(json.dumps({'run':str(RUN),'protected':len(before)},ensure_ascii=False))
