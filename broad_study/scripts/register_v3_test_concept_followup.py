from astra_review_tools import *
# Explicitly reviewed concepts: frozen concepts include problems, objects and quality goals.
decisions={
'E0046':['O4'], 'N0138':['O5','O6'], 'N0190':['O6','O7','O9','O10'],
'N0219':['O5','O6'], 'N0124':['O3','O4','O5'], 'N0125':['O3'],
'N0006':['ADD2'], 'N0104':['O4','O5','O6','O7'], 'N0073':['O3','O4','O6'],
'N0323':['O8','O10','O11'], 'N0335':['O8','O10','O11'], 'N0274':['O6'],
'N0262':['O4'], 'N0263':['O9','O10','O12','O13'], 'N0268':['O9','O10','O12','O13'],
'E0038':['O3'], 'E0029':['O2'], 'E0025':['O7','O8','O9'], 'E0271':['O5','O6'],
}
R=[]
for r,ids in decisions.items():
 ovs=[]
 for eid in ids:
  e=next(e for e in EB[RID[r]] if e['evidence_id']==r+':'+eid)
  assert e['code'].startswith('TC_') and e['metric']=='DUTY_OWN_USE'
  ovs.append(dict(evidence_id=e['evidence_id'],metric='DUTY_OWN_USE',branch=e['branch'],reason='复核冻结概念定义：本人明确执行该技术对象的测试或承担质量目标属于概念层技术执行；工具使用与技术概念不能混同。撤回过窄的TEST_OBJECT排除，不据此声称本人开发该对象。'))
 R.append(dict(reading_id=r,review_mode='FOLLOWUP',judgment='依据冻结技术概念包含问题、对象及质量目标的定义，纠正本轮将直接本人测试一律排除的过窄解释；工具和语言对象仍单列。',evidence_overrides=ovs))
register(R,'Astra_v3_test_concept_definition_followup')
