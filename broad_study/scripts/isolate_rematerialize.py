"""Isolated rematerialize into a sibling directory. Does not overwrite this RUN's tables."""
from pathlib import Path
import os, shutil, subprocess, json, hashlib
from datetime import datetime, timezone
SRC=Path(__file__).resolve().parents[1]
DST=SRC.parent/'run_20260916_grok_m6_isolated'
PY=os.environ.get('RESEARCH_PYTHON','C:/Users/bestl/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe')
def unlink_junction(p: Path):
    if p.exists():
        subprocess.check_call(['cmd','/c','rmdir',str(p)])
if DST.exists():
    marker=DST/'ISOLATED_COMPARE.json'
    if marker.exists() and 'PASS' in marker.read_text(encoding='utf-8'):
        raise SystemExit('REFUSE_OVERWRITE '+str(DST))
    for name in ['inputs','configs','notes']:
        unlink_junction(DST/name)
    shutil.rmtree(DST)
DST.mkdir(parents=True)
def junction(name):
    src=SRC/name; dst=DST/name
    subprocess.check_call(['cmd','/c','mklink','/J',str(dst),str(src)])
for name in ['inputs','configs','notes']:
    junction(name)
shutil.copytree(SRC/'scripts', DST/'scripts')
shutil.copy2(SRC/'input_manifest.json', DST/'input_manifest.json')
(DST/'tables').mkdir()
need=['Q3_coding_frame.csv','Q1_role_coverage.csv','R_source_membership.csv',
      'Q1_prefixed_comparison_plan.csv','Q2_catalog_bridge.csv','Q2_role_catalog.csv','Q_v1_fixed_display_items.csv']
for f in need:
    shutil.copy2(SRC/'tables'/f, DST/'tables'/f)
env=os.environ.copy(); env['PYTHONIOENCODING']='utf-8'
def run(script):
    r=subprocess.run([PY,'-B','-X','utf8',str(DST/'scripts'/script)], cwd=str(DST/'scripts'), env=env)
    if r.returncode!=0: raise SystemExit('FAILED '+script)
run('materialize_Q_partial.py')
run('compute_Q2_v2.py')
# compare statistical counts, ignore timestamps
src_mat=json.loads((SRC/'verification/Q_partial_materialization.json').read_text(encoding='utf-8'))
dst_mat=json.loads((DST/'verification/Q_partial_materialization.json').read_text(encoding='utf-8'))
src_cmp=json.loads((SRC/'verification/Q2_v2_comparison_receipt.json').read_text(encoding='utf-8'))
dst_cmp=json.loads((DST/'verification/Q2_v2_comparison_receipt.json').read_text(encoding='utf-8'))
cmp={
    'isolated':str(DST),
    'coded_ads':[src_mat['coded_ads'], dst_mat['coded_ads']],
    'pending_ads':[src_mat['pending_ads'], dst_mat['pending_ads']],
    'states':[src_mat['explicit_ad_label_slice_states'], dst_mat['explicit_ad_label_slice_states']],
    'state_counts':[src_mat['states'], dst_mat['states']],
    'evidence':[src_mat['semantic_evidence'], dst_mat['semantic_evidence']],
    'aggregates':[src_cmp['aggregates'], dst_cmp['aggregates']],
    'display':[src_cmp['display_items'], dst_cmp['display_items']],
    'duplicates':[src_cmp['duplicate_clusters'], dst_cmp['duplicate_clusters']],
    'created_utc_isolated':datetime.now(timezone.utc).isoformat(),
}
# qc_status may differ because original states file predates mark; isolated materialize uses marked JSON
stat_ok=all([
    src_mat['coded_ads']==dst_mat['coded_ads']==1576,
    src_mat['pending_ads']==dst_mat['pending_ads']==0,
    src_mat['explicit_ad_label_slice_states']==dst_mat['explicit_ad_label_slice_states'],
    src_mat['states']==dst_mat['states'],
    src_mat['semantic_evidence']==dst_mat['semantic_evidence'],
    src_cmp['aggregates']==dst_cmp['aggregates'],
    src_cmp['display_items']==dst_cmp['display_items'],
    src_cmp['duplicate_clusters']==dst_cmp['duplicate_clusters'],
])
cmp['status']='PASS_STATISTICAL' if stat_ok else 'FAIL'
(DST/'verification').mkdir(exist_ok=True)
(DST/'ISOLATED_COMPARE.json').write_text(json.dumps(cmp,ensure_ascii=False,indent=2),encoding='utf-8')
(SRC/'verification/isolated_rematerialize.json').write_text(json.dumps(cmp,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(cmp,ensure_ascii=False))
if not stat_ok: raise SystemExit('ISOLATED_MISMATCH')
