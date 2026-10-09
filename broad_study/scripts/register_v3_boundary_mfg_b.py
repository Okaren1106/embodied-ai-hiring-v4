from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0446':'采购库存：ERP/MRP为两个冻结类别，职责斜线与要求相同须保留未知；供应商谈判、SOP和库存审计明确。',
'N0482':'资深测试：至少五年测试经验属硬性；语言上位确定，测试框架、根因分析和规范编写分别记录。',
'N0426':'软件QA：计划用例开发和执行均明示；语言任选是GENERAL，开发能力优先为局部条款。',
'N0424':'NPI：MES流程数据维护为使用而非MES开发；本人流程标准文件编制补录。',
'N0190':'关节试验：被测电机、驱动和控制功能不直接当相应技术使用；台架机械安装另有实际使用证据。',
'N0219':'安全测试：计划开发与执行分开；关节和控制功能是被测对象；CE/FCC/CCC同认证族可确定，EMC与其他安全维度斜线仍未知。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for e in ['O3','9:0']:ov('E0446',e,'ERP/MRP为不同目录类别，职责power-user仍未解除斜线关系不清。',branch='UNRESOLVED')
ov('N0482','O2','至少一种语言仍必然属于编程语言上位。',branch='UNCONDITIONAL')
ov('N0482','O7','至少五年为明示最低经验。',metric='REQUIRED')
add('N0482','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL',12,'本人主导根因分析。')
add('N0482','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','EXAMPLE',14,'编写审核测试规范及标定流程等质量规程。')
add('N0426','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',3,'明确制定测试计划。')
add('N0426','V2_SOP_OPERATION','GENERAL','UNCONDITIONAL',12,'明确研发质量管控流程理解。')
add('N0424','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',3,'明确制定改善NPI流程及标准文件。')
for e in ['O6','O7','O9','O10']:ov('N0190',e,'对应电机、控制性能、减速器与驱动为被测对象，不替代本人运用该项设计/操作方法。',metric='SEPARATE',branch='TEST_OBJECT')
add('N0190','TC_MECHANICAL','DUTY_OWN_USE','UNCONDITIONAL',7,'明确本人完成试验台架机械安装。')
add('N0190','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',9,'明确编制测试大纲与用例。')
ov('N0219','O2','本条建立测试方案，执行测试另条有直接证据。',metric='DUTY_OWN_DEVELOP')
for e in ['O5','O6']:ov('N0219',e,'关节力矩限制和急停等是功能安全被验证对象。',metric='SEPARATE',branch='TEST_OBJECT')
ov('N0219','8:0','CE、FCC、CCC均为同一产品认证合规类别。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_mfg_b')
