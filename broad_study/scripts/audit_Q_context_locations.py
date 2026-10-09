"""Screen source locations for manual context review; never change labels."""
from common import *
import re

old=json.loads((ROOT/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
pat=re.compile(r'(?im)^\s*(?:[【\[（(]?[一二三四五六七八九十0-9]+[.、）)]?\s*)?[【\[（(]?\s*(岗位职责|工作职责|核心职责|职责描述|任职要求|岗位要求|任职资格|岗位资格|职位要求|加分项|优先条件|requirements|qualifications|minimum qualifications|preferred qualifications|what you.ll do|what you.ll bring|responsibilities|what we.re looking for)\s*[】\]）):：]?\s*$')
req={'任职要求','岗位要求','任职资格','岗位资格','职位要求','加分项','优先条件','requirements','qualifications','minimum qualifications','preferred qualifications',"what you'll bring","what we’re looking for","what we're looking for"}
counts=Counter();flags=[];adjud={}
for p in (ROOT/'configs/Q_adjudications').glob('*.json'):
 adjud.update(json.loads(p.read_text(encoding='utf-8'))['ads'])
for r in old:
 rid=r['reading_id'];counts[rid]+=1;oid=f'O{counts[rid]}'
 field=r['field'];t=RAW[r['identity_key']].get(field,'') or ''
 if str(r['start'])=='':
  flags.append(dict(reading_id=rid,old_item_id=oid,code=r['code'],role=r['role'],declared_context=r['prior_context'],location_context_candidate='LOCATION_UNRESOLVED',preceding_heading='',field=field,start='',quote=r['quote'],review_status='PENDING_MANUAL_CONTEXT_CHECK',first_pass_completed=rid in adjud,existing_override=js(adjud.get(rid,{}).get('old_overrides',{}).get(oid,{}))))
  continue
 start=int(r['start'])
 heads=[m for m in pat.finditer(t) if m.end()<=start]
 heading=heads[-1].group(1).lower() if heads else ''
 observed=('REQUIREMENT' if heading in req else 'DUTY') if heading else ('REQUIREMENT' if field=='requirements' else 'DUTY' if field=='duties' else '')
 if observed and r['prior_context'] in ['DUTY','REQUIREMENT'] and observed!=r['prior_context']:
  override=adjud.get(rid,{}).get('old_overrides',{}).get(oid,{})
  flags.append(dict(reading_id=rid,old_item_id=oid,code=r['code'],role=r['role'],declared_context=r['prior_context'],location_context_candidate=observed,preceding_heading=heading,field=field,start=start,quote=r['quote'],review_status='PENDING_MANUAL_CONTEXT_CHECK',first_pass_completed=rid in adjud,existing_override=js(override)))
if flags:dump('tables/Q_context_location_review_candidates.csv',flags)
save_json('verification/Q_context_location_screen.json',dict(status='SCREEN_ONLY_NOT_SEMANTIC_VALIDATION',inherited_items=len(old),flagged=len(flags),coded_flags=sum(r['first_pass_completed'] for r in flags)))
for r in flags:
 if r['first_pass_completed']:print(js(r))
print('Location candidates',len(flags),'coded',sum(r['first_pass_completed'] for r in flags))
