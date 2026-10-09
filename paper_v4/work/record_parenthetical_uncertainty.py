"""Record the two coordinator-adopted symmetric parenthetical uncertainties."""
from pathlib import Path
import json,shutil,hashlib
ROOT=Path(__file__).resolve().parents[1]
current=ROOT/'data/v4_source_corrections.json'
history=ROOT/'data/v4_source_corrections_phase4.json'
ledger=json.loads(current.read_text(encoding='utf-8'))
assert len(ledger['changes'])==5 and not history.exists()
payload=json.loads((ROOT/'analysis/empirical/bare_parenthetical_correction_payload.json').read_text(encoding='utf-8'))
assert {r['reading_id'] for r in payload['changes']}=={'N0798','N1044'}
assert hashlib.sha256((ROOT/'analysis/v4_ad_technology_current.csv').read_bytes()).hexdigest()==payload['phase4_state_sha256']
shutil.copy2(current,history)
ledger['changes'].extend(payload['changes']);ledger['changed_pairs']=7
ledger['origin']='Complete review of 46 previous U pairs, followed by bounded peer-framework parenthetical consistency review'
ledger['previous_phase_ledger']='data/v4_source_corrections_phase4.json'
ledger['parenthetical_relation_set']=['UNCONDITIONAL','EXAMPLE']
ledger['parenthetical_relation_set_scope']='Named bounded interpretation set; not an exhaustive theory of reader interpretations.'
current.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Recorded seven declared changes; phase4 ledger preserved.')
