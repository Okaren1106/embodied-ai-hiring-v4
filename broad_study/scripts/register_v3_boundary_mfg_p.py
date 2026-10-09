from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0386':'自动化测试作者明确使用pytest/HIL，C++仅要求阅读而非职责编写；学习意愿不计现有实时能力。',
'E0377':'灵巧手研发项目的测试职责、数据采集和必备/优先工具要求分明；Dexterity不作为公司归属。',
'E0380':'CNC加工程序开发及操作，量具操作和安全作业成立；培训和资格不直接成为工艺实践经验。',
'E0422':'库存、物流采购综合任务保留；一般和硬性谈判要求可并存，不能当成纯仓库任务。',
'N0966':'质量程序、数据工作流与MES平台分开，开发MES之上的工作流不等于开发MES；质量标准上位要求明确。',
'N1009':'精密CNC程序与刀路仿真真实；质量体系标准上位要求明确，ERP/CAD/CAM斜线保留未知。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
add('E0377','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',10,'本人编制测试程序，含配置、判定标准和追溯。')
ov('E0380','10:0','CNC职业培训或证书为资历教育形式，不直接扩为本人加工方法实践；保留原文另列。',metric='SEPARATE',branch='TRAINING_CREDENTIAL_OBJECT')
for r,e in [('E0422','14:0'),('N0966','11:0')]:ov(r,e,'证书或正规培训保留资格及教育对象，不重复推导具体方法经验。',metric='SEPARATE',branch='CREDENTIAL_OBJECT')
ov('N0966','3:0','明确开发MES/Tulip上的缺陷数据工作流，不是开发MES软件本身；工具使用关系仍未知。',metric='DUTY_OWN_USE')
for e in ['O4','15:0']:ov('N0966',e,'括号列出方法，没有如/等或任选，按明确方法要求。',branch='UNCONDITIONAL')
for r,e in [('N0966','17:0'),('N1009','18:0')]:ov(r,e,'明确quality systems上位类别，编号列表不使类别本身成为任选/示例。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_mfg_p')
register([dict(reading_id='E0381',review_mode='FOLLOWUP',judgment='回查冻结APQP/PPAP定义包含FAI，纠正跨类误判。',evidence_overrides=[dict(evidence_id='E0381:2:0',branch='UNCONDITIONAL',reason='PPAP与FAI均属于冻结质量策划/生产件批准/首件检验同一类别，类别层可判，无须以斜线置未知。')])],'Astra_v3_fai_same_category')
