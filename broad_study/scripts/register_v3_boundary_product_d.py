from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0368':'运营TPM：职责Excel不作一般要求；Smartsheet/Excel和ERP/MRP分支未知；CAPM/Agile是资格非方法知识。',
'N0970':'现场人员运营：岗位概要明确管理人员招聘排班，与协同招聘具体句分开；资源工具例示加任选。',
'N0987':'AI资源TPM：资源分配/监督数据管道是管理任务，不等于技术栈独立使用；采购合同真实，补计划方法。',
'N0872':'站点执行主管：Required父语境统摄风险项目能力；PMP与多种非项目领域证书任选保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','2:2']:ov('E0368',e,'Smartsheet/Excel仅斜杠关系未解。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_USE_CHOICE'])
ov('E0368','O2','原引用职责，无一般Excel要求。',metric='SEPARATE',branch='DUTY_NOT_REQUIREMENT')
for e in ['O4','7:0','7:1']:ov('E0368',e,'dashboards/automation之后括号工具例示。',branch='EXAMPLE')
ov('E0368','5:0','ERP/MRP相互关系未明。',branch='UNRESOLVED')
ov('E0368','6:0','CAPM或Agile certification是资格，不另加方法能力。',metric='SEPARATE',branch='QUALIFICATION_NOT_METHOD')
ov('E0368','6:1','CAPM/Agile均属项目资格上位。',branch='UNCONDITIONAL')
add('E0368','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Uphold the program management framework — single intake, written status, one source of truth — and help functional teams adopt it.','明确执行项目管理框架。')
for e in ['4:0','4:1','4:2']:ov('N0970',e,'e.g.与or同时存在。',branch='CHOICE_AND_EXAMPLE')
add('N0970','V2_HR','DUTY_OWN_USE','UNCONDITIONAL','This includes managing recruitment pipelines, overseeing shift schedules and site assignments, coordinating travel, and monitoring field labor expenses.','本人负责人员招聘排班全程；保留后文具体招聘协作而不覆盖。')
add('N0970','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Consolidate daily operational metrics and sync with the Early Access Program TPM to align field staffing with core project timelines.','本人汇总运营度量并对齐项目进度配置。')
for e in ['O2','O3']:ov('N0987',e,'分配资源/监督管道的管理责任，非本人训练系统或数据管道技术操作。',metric='SEPARATE',branch='RESOURCE_OR_TEAM_MANAGEMENT')
ov('N0987','4:0','JIRA/Atlassian产品组合未确定Jira本身与其他产品关系。',branch='UNRESOLVED')
ov('N0987','4:1','including/and similar systems为例示。',branch='EXAMPLE')
add('N0987','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Organize, sequence, and prioritize work across our training clusters, data processing pipelines, data operations teams, and other engineering groups so the organization operates at maximum efficiency.','本人制定跨团队优先顺序和资源计划。')
add('N0987','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','Proven capacity to leverage an array of project management tools, methodologies, and techniques throughout the AI/ML development lifecycle','明确一般项目方法能力。')
add('N0872','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Maintain an integrated execution plan across site readiness, installation, commissioning, training, support readiness, and operational handoff activities.','明确本人维护执行计划。')
add('N0872','V2_PROJECT_METHOD','REQUIRED','UNCONDITIONAL','Strong project execution, risk management, and escalation management skills.','Required下明确项目执行与风险方法。')
register(list(R.values()),'Astra_v3_boundary_product_d')
