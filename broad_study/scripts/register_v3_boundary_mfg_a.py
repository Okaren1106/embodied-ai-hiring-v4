from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0046':'平台测试：ETL是被测管线，评测开发与实际执行分别补证；Postman示例、Python/Java优先未知保持。',
'N0631':'整机工艺：明确标准化工艺文件开发和流程能力补录；外协质量管控不直接当采购。',
'E0593':'整机验收技师：遵照规程配置软硬件/固件明确本人操作，开发集成排障不等于运行维护。',
'N0977':'制造工程：回读Nice to have标题；工艺规程编写能力和加工成型实践补录；工具验证不是再开发机械工具。',
'N0284':'结构件采购：采购对象与制造工艺要求分离；订单、供应商、库存与议价按本人承担分别保留。',
'N0138':'系统性能测试：实时和可靠性为被测系统指标，perf工具使用明确；至少一种脚本语言关系有明示。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
ov('E0046','O4','验证ETL准确性是被测对象关系，非本人构建或运营数据管线。',metric='SEPARATE',branch='TEST_OBJECT')
add('E0046','TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL',2,'明确负责全流程测试，区别测试方案开发。')
add('N0631','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',3,'本人输出标准化工艺文件。')
add('N0631','V2_SOP_OPERATION','GENERAL','UNCONDITIONAL',12,'明确工艺体系流程与工艺文件审核能力。')
add('E0593','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',13,'本人按照文档规程配置机器人。')
add('N0977','V2_SOP_OPERATION','GENERAL','UNCONDITIONAL',22,'明确撰写SOP与作业说明经验。')
add('N0977','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL',21,'明确增材、加工和成形实践；具体铣车焊等为下位示例。')
ov('N0977','O9','本条是工具验证，被验证对象并非该条的本人机械开发。',metric='SEPARATE',branch='TEST_OBJECT')
for e in ['O5','O6']:ov('N0138',e,'调度实时性和网络可靠性是性能测试指标，不直接当实时系统或可靠性技术使用。',metric='SEPARATE',branch='TEST_OBJECT')
register(list(R.values()),'Astra_v3_boundary_mfg_a')
