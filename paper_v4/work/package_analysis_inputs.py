"""Copy the exact required v3 inputs and make v4 analysis self-contained.

The snapshot is a private verification copy. Existing snapshot bytes must match;
there is no overwrite or refresh of frozen records. Script path changes concern
only this version's newly authored analysis files.
"""
from pathlib import Path
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[1]
V3=ROOT.parent/'analysis_E_english_v3_0'
manifest=json.loads((ROOT/'work/empirical/module_input_manifest.json').read_text(encoding='utf-8'))
names={r['relative_to_v3_or_source_snapshot'] for r in manifest['frozen_inputs']}
names.add('source_v2/data/inputs/context_index.csv')
names.update(['release/English_Manuscript_IJM.md','release/Supplementary_Material.md',
              'analysis/current_firm_cells.csv','analysis/current_pair_summary.csv',
              'analysis/main_company_comparisons.csv','work/provenance/diagnostic_adjudication_ledger.csv'])
snapshot=ROOT/'source_snapshot'
output=[]
for name in sorted(names):
    original=V3/name;dest=snapshot/name;dest.parent.mkdir(parents=True,exist_ok=True)
    b=original.read_bytes();h=hashlib.sha256(b).hexdigest()
    if dest.exists():assert dest.read_bytes()==b, 'Refuse changing frozen snapshot: '+name
    else:dest.write_bytes(b)
    output.append({'path':name,'bytes':len(b),'sha256':h})
(snapshot/'snapshot_manifest.json').write_text(json.dumps({'source_version':'v3.0','files':output},indent=2)+'\n',encoding='utf-8')
for name in ['paired_analysis.py','paired_context.py','paired_breakdown.py','qualification_scope.py']:
    p=ROOT/'work'/name;t=p.read_text(encoding='utf-8')
    t=t.replace("OLD=ROOT.parent/'analysis_E_english_v3_0'","OLD=ROOT/'source_snapshot'")
    t=t.replace('relative_to(ROOT.parent)','relative_to(ROOT)')
    p.write_text(t,encoding='utf-8')
for name in manifest['scripts']:
    p=ROOT/'work/empirical'/name;t=p.read_text(encoding='utf-8')
    t=t.replace('Path(__file__).resolve().parents[3]','Path(__file__).resolve().parents[2]')
    t=t.replace("ROOT / 'analysis_E_english_v3_0'","ROOT / 'source_snapshot'")
    t=t.replace("ROOT/'analysis_E_english_v3_0'","ROOT/'source_snapshot'")
    t=t.replace("ROOT/'analysis_E_english_v4_0'","ROOT")
    t=t.replace("ROOT / 'analysis_E_english_v4_0/analysis/empirical'","ROOT / 'analysis/empirical'")
    t=t.replace("ROOT/'analysis_E_english_v4_0/analysis/empirical'","ROOT/'analysis/empirical'")
    t=t.replace("ROOT/'analysis_E_english_v4_0/analysis/paired'","ROOT/'analysis/paired'")
    t=t.replace("'path':str(p)","'path':str(p.relative_to(ROOT)).replace('\\\\','/')")
    p.write_text(t,encoding='utf-8')
print(json.dumps({'snapshot_files':len(output),'snapshot_bytes':sum(r['bytes'] for r in output)}))
