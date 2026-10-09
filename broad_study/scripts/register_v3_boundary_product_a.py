from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0243':'信息化产品：Axure等列举，不是明确任选；不由职位名补项目管理方法。',
'E0042':'交付运营：Python/Shell同样斜杠未知；客户问题闭环不等于销售CRM，项目风险/进度与操作标准建设明确。',
'N0256':'海外硬件PM：本人计划风险管理、一般研发管理方法明确；Jira/Git等举例。',
'N0432':'软件版本PM：测试或开发经验为加分任选；项目方法明确，工具至少一种且如。',
'N0408':'交互产品：协同算法与产品规划分开；Figma/Axure等例示。',
'N0086':'硬件Infra项目：现有进度方法/SOP/供应商及工具任选成立；ROS斜杠保持未知。',
'N0008':'校招项目：协助项目经理与供应商沟通不独立承担采购；办公工具斜杠未明，飞书项目是举例。',
'N0072':'硬件项目：补明确计划方法；工具只是如/等，认证是独立加分维度。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0243','1:0','X-mind/Axure等仅举例。',branch='EXAMPLE')
ov('E0042','1:0','配合售前及反馈客户需求，未写销售漏斗或CRM使用。',metric='SEPARATE',branch='CUSTOMER_FEEDBACK_NOT_CRM')
ov('E0042','2:0','Python/Shell关系同样未明。',branch='UNRESOLVED')
for e in ['3:0','3:1']:ov('E0042',e,'Prometheus/Grafana等举例，无任选。',branch='EXAMPLE')
add('E0042','V2_PROJECT_METHOD','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立项目进度管理机制，识别交付风险问题并推进解决','明确本人建立进度风险管理流程。')
add('E0042','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','沉淀标准化交付流程、技术文档及验收规范','本人形成标准化操作/交付规范。')
add('E0042','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','作为客户技术对接接口，响应交付全流程技术问题','明确本人技术支持，不从团队背景推定。')
for e in ['3:0','3:1']:ov('N0256',e,'Jira/Git/Tapd等为工具例示。',branch='EXAMPLE')
add('N0256','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','包括计划制定、预算与资源调配、风险评估','项目方法的具体内容明确。')
add('N0256','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','精通敏捷开发、瀑布模型等研发管理方法论','同项目方法上位的一般要求。')
ov('N0432','O2','机器人/自驾测试或者开发经验，评价经验仅一分支。',branch='CHOICE')
for e in ['1:0','1:1']:ov('N0432',e,'至少一种且如，任选加例示。',branch='CHOICE_AND_EXAMPLE')
add('N0432','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','制定并跟进相应软件版本计划','明确本人制定跟进计划。')
add('N0432','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','了解如瀑布模型、敏捷开发、DevOps等主流软件开发模式','项目研发管理方法上位明确。')
for e in ['2:0','2:1']:ov('N0408',e,'Figma/Axure等仅举例。',branch='EXAMPLE')
for e in ['O1','O2','2:0','2:1']:ov('N0008',e,'Project/Visio/Excel/PPT只斜杠关系未明。',branch='UNRESOLVED')
ov('N0008','5:0','如飞书项目/TAPD等为例示。',branch='EXAMPLE')
for e in ['5:0','5:1','5:2']:ov('N0072',e,'如project/Jira/confluence等仅例示。',branch='EXAMPLE')
add('N0072','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','负责研发项目的整体规划，从项目启动到最终验收的全流程管理','明确项目全程计划管理。')
add('N0072','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','扎实的项目管理理论基础','方法基础一般要求，与PMP认证分开。')
register(list(R.values()),'Astra_v3_boundary_product_a')
