from bootstrap import *
import csv
NEW=Path(json.loads((SCRATCH/'new_run.json').read_text(encoding='utf-8'))['run'])
p=NEW/'work/grouping_rules_source.json';r=json.loads(p.read_text(encoding='utf-8'))
facts=list(csv.DictReader((NEW/'company_facts.csv').open(encoding='utf-8-sig')))
for dim in r['dimensions']:
 if dim['dimension']=='deployment_status_actual':
  for f in facts:
   if f['field']=='deployment_status_actual' and f['fact_seq']=='2' and f['company_id'] in ['CN_AGIBOT','CN_DEEPROBOTICS','CN_SPIRITAI','CN_GALBOT']:
    label={'CN_AGIBOT':'DEPLOYMENT_SELF_REPORTED','CN_DEEPROBOTICS':'DEPLOYMENT_SELF_REPORTED','CN_SPIRITAI':'DEPLOYMENT_MEDIA_REPORTED','CN_GALBOT':'CUSTOMER_CONFIRMED_USE'}[f['company_id']]
    dim['group_bindings'].setdefault(f['company_id'],{})[f['value']]=[label]
save(p,r)
p=NEW/'scripts/s07_cards_and_html.py';s=p.read_text(encoding='utf-8');s=s.replace('返修版：24 家均有公司记录；逐字段未查/查后未找到仍展示。本页不是阶段 B 完成，待独立验收。','补充版：原修复包已通过独立验收；本版按用户授权新增公司证据，补充后验证与独立验收分开。阶段B业务组尚未固定。');p.write_text(s,encoding='utf-8')
p=NEW/'scripts/s05_grouping.py';s=p.read_text(encoding='utf-8');s=s.replace('可作组间比较','达到展示门槛；待业务组定义与口径确认');p.write_text(s,encoding='utf-8')
print(NEW)
