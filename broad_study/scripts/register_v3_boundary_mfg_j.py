from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0334':'体系文件本人更新，审核、设备校准和检测监管是协助，CNAS证书优先与体系知识一般分离。',
'E0052':'结构采购仍明确要求结构设计经历；至少一种设计软件为任选示例，DFM采购建议为协作。',
'N0321':'质量体系和变更管理明确；变更效果验证不是直接测评系统证据，IPD/APQP及主导或组织根因分析保留关系未知。',
'N0333':'独立核对重复模板，按质量治理而非测试执行解释；未将广告去重冒作新增样本。',
'E0038':'电机规格定义和选型匹配属于技术应用，不证明电机开发；现场排障和下线测试标准开发另有明确证据。',
'E0032':'搭建测试体系成立；达成可靠性目标不证明本人可靠性技术执行，保留明确验证方法经验。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for r in ['N0321','N0333']:
 ov(r,'4:0','IPD/APQP跨类别裸斜线未明确关系。',branch='UNRESOLVED')
 ov(r,'ADD1','主导或组织根因分析未明确是否本人运用分析方法。',branch='UNRESOLVED')
 ov(r,'O6','变更管理中的效果验证确认未明确测试测量方法，不把管理核查等同评测技术。',metric='SEPARATE',branch='CHANGE_GOVERNANCE')
ov('E0038','O1','本人完成电机选型匹配及规格定义，属于技术应用，未直接开发电机产物。',metric='DUTY_OWN_USE')
ov('E0038','O3','可靠性为被测质量指标，原文技术出现与测试方法执行分离。',metric='SEPARATE',branch='TEST_OBJECT')
ov('E0038','O5','引用仅要求驱动功率电路及功率器件知识，不从电力电子自动推出执行器知识。',metric='SEPARATE',branch='DRIVE_CIRCUIT_OBJECT')
ov('E0032','O2','推动团队达成可靠性目标不证明本人使用可靠性技术。',metric='SEPARATE',branch='QUALITY_TARGET')
add('E0032','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',2,'本人搭建测试流程规范。')
register(list(R.values()),'Astra_v3_boundary_mfg_j')
