"""Record targeted location review and prepare mandatory full-semantic QC scope."""
from common import *
import copy,datetime
hid='Q-M5-CONTEXT-LOCATION-20260916-05'
hp=ROOT/'notes'/(hid+'.json')
assert not hp.exists()
p=ROOT/'configs/Q_adjudications/RF_MANUFACTURING_QUALITY_SUPPLY.json'
data=json.loads(p.read_text(encoding='utf-8'));before=copy.deepcopy(data['ads']['E0604'])
d=data['ads']['E0604']
d.setdefault('old_overrides',{})['O13']=dict(metric='SEPARATE',branch='EXAMPLE',relation='PROCUREMENT_OBJECT',reason='来源定位定向复核：原要求motors误指职责列表，移回带compute,motors,etc的要求原文；采购对象性质不变',quote='Experience sourcing constrained or allocation-sensitive components (compute, motors, etc)',field='requirements')
assert locate(d['identity_key'],d['old_overrides']['O13'])['method']!='UNRESOLVED_LOCATION'
d['notes']+=' 来源坐标定向复核修正O13，语义仍为采购对象；不代表整条二次复核完成。'
save_json('notes/'+hid+'.json',dict(scope='TARGETED_SOURCE_CONTEXT_ONLY',before=before,after=d))
p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
flags=[r for r in read(ROOT/'tables/Q_context_location_review_candidates.csv') if r['first_pass_completed']=='True']
reasons={
'N0468':'专业技能标题未被筛查识别，段内明确了解/掌握/能操作；真实要求',
'N0124':'职责段嵌入对电驱需求深入理解能力，按语义是要求',
'E0355':'原duties字段包含Key Qualities的资格段；已定向确认',
'N1015':'What You Bring标题未被规则识别，实际原位于资格段；精确窗口核对',
'N0980':'What You Bring及Technical Tools等标题未被识别，实际资格段',
'E0529':'duties字段包含葡语全文Requisitos/Diferenciais；真实要求',
'E0528':'duties字段包含西语全文Requisitos/Nice to have；真实要求',
'N0910':'Basic Qualifications/Preferred Skills and Experience/Additional Requirements未被筛查完整识别',
'N0912':'同文资格与物理要求段，筛查未识别标题',
'N0911':'同文资格与物理要求段，筛查未识别标题',
'E0586':'duties字段包含Competencies and Skills资格段',
'E0604':'已修复原要求词误定位到职责的来源坐标',
}
rows=[]
for r in flags:
 rid=r['reading_id'];oi=r['old_item_id'];ov=data['ads'][rid].get('old_overrides',{}).get(oi)
 if ov:
  disposition='FIRST_PASS_OVERRIDE_EXACT_LOCATION_VERIFIED'
  reason=ov['reason']
 else:
  assert rid in reasons,(rid,oi)
  disposition='TARGETED_REVIEW_KEEP_REQUIREMENT_CONTEXT';reason=reasons[rid]
 rows.append(dict(reading_id=rid,old_item_id=oi,disposition=disposition,reason=reason,full_semantic_second_pass_complete=False,reviewer='Astra'))
save_json('configs/Q_context_location_adjudications_215.json',rows)
print('context ledger',len(rows),'existing/new location overrides',sum(r['disposition'].startswith('FIRST_PASS') for r in rows))
