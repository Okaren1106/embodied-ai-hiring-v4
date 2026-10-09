from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0029':'本人整机测试和测试方法优化成立；关节为被测对象，统筹安全可靠性专项不等于直接执行其技术方法。',
'E0025':'半实物仿真是实际测试手段，感知控制和执行系统是被测对象；脚本语言明确至少一种。',
'E0014':'算力与模型API为采购对象；修正多个技术与要求引文错位，以原字段精确引用为准。',
'E0303':'采购订单、供应方履约与ERP/SRM使用知识明确；证书优先按类别与示例分列。',
'E0271':'本人开发CI和测试方案、执行用例成立；可靠性安全性是测试覆盖目标，不等同本人相关技术方法。',
'E0270':'总体测试负责、具体与研发配合测试分开，系统策略设计为本人评测开发。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
ov('E0029','O2','关节模组为测试对象。',metric='SEPARATE',branch='TEST_OBJECT')
for e in ['O3','O4','1:0','ADD2']:ov('E0029',e,'统筹专项未证实本人执行该可靠性或安全技术方法。',metric='SEPARATE',branch='COORDINATION_OBJECT')
for e in ['O7','O8','O9']:ov('E0025',e,'感知、控制和执行器为明确被测系统；实际采用的仿真方法另计。',metric='SEPARATE',branch='TEST_OBJECT')
add('E0025','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',2,'明确制定集成测试流程规范。')
for e,n,m,b in [('O3',14,'GENERAL','UNCONDITIONAL'),('O4',15,'GENERAL','UNCONDITIONAL'),('O5',15,'GENERAL','UNCONDITIONAL'),('O9',13,'SEPARATE','PROCUREMENT_OBJECT'),('O10',17,'SEPARATE','BACKGROUND'),('12:1',17,'GENERAL','UNCONDITIONAL')]:
 ov('E0014',e,'旧引用行未实际支持该项，重新定位支持该指标的完整原句。',metric=m,branch=b,quote=RAW[RID['E0014']]['full_description'].splitlines()[n-1])
add('E0014','V2_PROCUREMENT','PREFERRED','UNCONDITIONAL',12,'算力租赁、服务器硬件、云服务接触经验明确优先。')
for e in ['O5','O6']:ov('E0271',e,'测试方案覆盖的质量目标与实际测试方法分列。',metric='SEPARATE',branch='TEST_OBJECT')
add('E0271','TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL',4,'本人明确执行测试用例。')
register(list(R.values()),'Astra_v3_boundary_mfg_k')
