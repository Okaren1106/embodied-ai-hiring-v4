from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0332':'实验室方法验证与设备校准协作分开，检验规范与方法验证方案的本人制定补录。',
'N0262':'导航和传感器为被测对象；测试用例设计为评测开发，算法知识与开发或测试经验保留各自语境。',
'N0300':'PFMEA本人完成，DFX前期建议与跨部门异常协调不扩大为本人技术开发；独立DFM报告可判。',
'N0263':'SDK语言与感知控制等被测对象单列；本人搭测试平台保留评测开发，要求语言任选明确。',
'N0241':'本人多端测试、策略和用例设计成立；三语言一种或多种明确任选。',
'N0268':'独立核对与N0263相近文本及不同排版，执行同一被测对象边界；职责方案设计和测试执行分别记录。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
add('N0332','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',3,'本人制定并更新产品检验规范。')
add('N0332','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'本人编制验证方案及流程和判定标准。')
for e in ['O4','O6']:ov('N0262',e,'导航是被测对象，不等于导航算法本人使用。',metric='SEPARATE',branch='TEST_OBJECT')
ov('N0262','O7','原句是设计测试用例，应记评测开发。',metric='DUTY_OWN_DEVELOP')
for r,n in [('N0263',3),('N0268',2)]:
 for e in ['O1','O2','O9','O10','O12','O13']:ov(r,e,'被测SDK语言、算法或质量指标与实际测试技术分离，出现仍保留。',metric='SEPARATE',branch='TEST_OBJECT')
 add(r,'TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',n,'本人设计端到端场景化测试用例。')
add('N0241','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',4,'本人制定测试策略、设计高覆盖用例；参与修饰前项需求评审。')
register(list(R.values()),'Astra_v3_boundary_mfg_i')
