import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
cat=json.loads((root/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
roles=['RF_RESEARCH_SCIENCE','RF_ROBOT_OPERATIONS','RF_SIMULATION_EVALUATION','RF_SYSTEMS_ENGINEERING_INTEGRATION']
out=[]
for role in roles:
    inc=[x['code']+'\t'+x['name'] for x in cat['labels'] if role in x.get('applicable_roles',[])]
    out.append('==== '+role+' n='+str(len(inc)))
    out.extend(inc)
    out.append('')
Path('../notes/probe_rest_catalog.txt').write_text('\n'.join(out),encoding='utf-8')
print({r:sum(1 for x in cat['labels'] if r in x.get('applicable_roles',[])) for r in roles})
