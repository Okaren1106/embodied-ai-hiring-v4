from pathlib import Path
import hashlib,json,shutil
REPO=Path(r'D:\Embod AI analysis\embodied-ai-hiring-research')
BASE=REPO/'reports/2026-09-14_company_data_analysis'
RUN=BASE/'stage_b_evidence_integrated/run_20260915T064258Z'
AUDIT=BASE/'stage_b_evidence_integrated_acceptance/run_20260915T064258Z'
SCRATCH=REPO/'.b5accept'
COPY=SCRATCH/'reproduction'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':
 AUDIT.mkdir(parents=True,exist_ok=False)
 protected=json.loads((RUN/'repair_records/protected_before.json').read_text(encoding='utf-8'))
 bad=[p for p,h in protected.items() if not Path(p).is_file() or sha(Path(p))!=h]
 save(AUDIT/'prior_protection_check.json',{'n':len(protected),'mismatches':bad})
 for p in RUN.rglob('*'):
  if p.is_file():protected[str(p)]=sha(p)
 save(AUDIT/'protected_before.json',protected)
 for p,name in [(REPO.parent/'必读.md','workspace_必读_before.md'),(REPO/'必读.md','repo_必读_before.md'),(BASE/'EXECUTION_PLAN.md','EXECUTION_PLAN_before.md')]:shutil.copy2(p,AUDIT/name)
 shutil.copytree(RUN,COPY,ignore=shutil.ignore_patterns('__pycache__'))
 # Preserve the original 36 assertions verbatim, changing only the audit context.
 shutil.copy2(RUN/'repair_records/prior_audit_regression.py',AUDIT/'prior_audit_regression.py')
 (AUDIT/'regression_context.py').write_text('from pathlib import Path\nimport csv,json,hashlib\nHERE=Path(__file__).resolve().parent\nBASE=HERE.parent.parent\nRUN=BASE/"stage_b_evidence_integrated/run_20260915T064258Z"\ndef rows(p):return list(csv.DictReader(p.open(encoding="utf-8-sig",newline="")))\ndef sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()\ndef save(n,obj):(HERE/n).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")\n',encoding='utf-8')
 # Browser harness is replayed against the submitted original; outputs stay in this audit.
 browser=(RUN/'repair_records/browser_check.mjs').read_text(encoding='utf-8')
 browser=browser.replace('const short="D:\\\\Embod AI analysis\\\\embodied-ai-hiring-research\\\\.b5repair\\\\browser_tmp";', 'const short='+json.dumps(str(SCRATCH/'browser_tmp'))+';')
 (AUDIT/'browser_check.mjs').write_text(browser,encoding='utf-8')
 print(json.dumps({'audit':str(AUDIT),'copy':str(COPY),'protected':len(protected),'prior_changes':bad},ensure_ascii=False))
