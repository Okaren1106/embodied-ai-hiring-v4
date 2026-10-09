"""Reproduce numerical analyses and independent audits with standard Python.

Run from any working directory. Reads the packaged source_snapshot, declared
v4 correction ledger and local source-review annotations; does not require the
original project or any network request.
Figure and Word rendering are separate optional workflows.
"""
from pathlib import Path
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'source_snapshot/snapshot_manifest.json').read_text(encoding='utf-8'))
for r in manifest['files']:
    p=ROOT/'source_snapshot'/r['path']
    assert p.stat().st_size==r['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],r['path']
for folder in ['analysis/paired','analysis/empirical','audit']:(ROOT/folder).mkdir(parents=True,exist_ok=True)
scripts=['apply_v4_overlay.py','empirical/current_u_consistency_review.py','empirical/bare_parenthetical_review.py',
         'empirical/verify_v4_overlay_independent.py',
         'paired_analysis.py','paired_context.py','qualification_scope.py','paired_breakdown.py',
         'empirical/rebuild_company_comparisons.py','empirical/classification_breakdown.py',
         'empirical/discordant_source_review.py','empirical/local_template_sensitivity.py',
         'empirical/verify_paired_independent.py','empirical/verify_scope_independent.py',
         'empirical/verify_paired_breakdown_independent.py',
         'literature_validation/review_example_increments.py',
         'literature_validation/admission_rule_diagnostics.py',
         'extensions/framework_control/scripts/run_framework_control.py',
         'empirical/verify_framework_independent.py','empirical/finalize_empirical_facts.py']
for script in scripts:
    path=ROOT/script if script.startswith('extensions/') else ROOT/'work'/script
    r=subprocess.run([sys.executable,'-X','utf8',str(path)],cwd=ROOT,text=True,encoding='utf-8',capture_output=True)
    if r.returncode:
        print(r.stdout);print(r.stderr,file=sys.stderr);raise SystemExit(r.returncode)
    print('PASS',script)
for r in manifest['files']:
    assert hashlib.sha256((ROOT/'source_snapshot'/r['path']).read_bytes()).hexdigest()==r['sha256']
print('PASS frozen source snapshot unchanged; all numerical workflows finished.')
