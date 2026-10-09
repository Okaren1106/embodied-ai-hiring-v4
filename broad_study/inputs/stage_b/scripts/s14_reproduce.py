"""Offline reproduction in the current copy. Verify the sealed lock before any write."""
import os,subprocess,sys
from pathlib import Path
RUN=Path(__file__).resolve().parent.parent
steps=['s01_lock_inputs.py','s02_build_facts.py','s03_build_tables.py','s05_grouping.py',
       's03b_company_profile.py','s09_search_log.py','s04_verify.py','s07_cards_and_html.py',
       's06_rebuild_and_fault.py','s11_release_gate.py']
if __name__=='__main__':
 for step in steps:
  print('Running '+step,flush=True)
  result=subprocess.run([sys.executable,'-B','-X','utf8',str(RUN/'scripts'/step)],cwd=RUN,
                        env=dict(os.environ,PYTHONIOENCODING='utf-8',PYTHONDONTWRITEBYTECODE='1'))
  if result.returncode:raise SystemExit(result.returncode)
