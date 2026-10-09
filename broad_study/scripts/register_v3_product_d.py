from astra_review_tools import *
JUD={
'N0893':'机器人自主能力产品规划，技术不是本人开发；优先技术清单含such as/including加or应保留双分支，明确指标设计职责补入。',
'N0896':'履约设施施工主管，职能内任务OTHER_DOMAIN保留；安全Required与工具Preferred不得混成General。',
'N0788':'旗舰客户项目，有具体范围依赖风险和预算方法；熟悉客户采购流程是资格认知，可以记要求但不推本人采购职责。',
'N1002':'CX战略组合与产品团队管理，Salesforce为被孵化产品对象，不能据此说本人使用CRM工具；旅程映射一般认知和敏捷方法保留。',
'E0092':'短文仅研发周期规划及协作交付；不推编程或特定认证，具体周期计划方法有原文。',
'E0602':'研究项目资源和计划管理，不是模型研发岗位；补具体计划依赖方法与一般要求，遥操环境熟悉保持优先认知，不称操作履历。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','O6','O7','O8','O9','O10','O11','O12']:ov('N0893',e,'such as/including列举加or，双重关系。',branch='CHOICE_AND_EXAMPLE')
add('N0893','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Develop product metrics that measure adoption, reliability, autonomy performance, operational efficiency, and customer outcomes.','明确本人定义测量指标，非仅关注质量目标。')
ov('N0896','14:0','Required Qualifications段。',metric='REQUIRED')
for e in ['20:0','20:1','20:2']:ov('N0896',e,'Preferred Qualifications段。',metric='PREFERRED')
add('N0896','V2_PROJECT_METHOD','SEPARATE','COLLABORATION_OBJECT','Assist with project planning, scheduling, and site logistics.','明示协助计划，不能据主管名义改成独立承担。')
add('N0788','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Develop and maintain integrated program plans covering scope, schedules, budgets, resources, dependencies, risks, and deliverables.','明确项目范围计划依赖风险。')
add('N0788','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','Strong financial and commercial judgment, including experience managing program budgets, scope changes, and contractual deliverables.','明确一般资格项目范围变更。')
add('N0788','V2_PROCUREMENT','PREFERRED','CHOICE','Familiarity with industrial operating environments, safety requirements, and customer procurement or governance processes.','客户采购流程知识是明确资格；不代表本人承担采购，or保留。')
ov('N1002','3:0','孵化迭代enterprise tools是管理对象，无本人使用或实现证据。',metric='SEPARATE',branch='PRODUCT_MANAGEMENT_OBJECT')
ov('N1002','5:1','journey mapping是括号方法例示。',branch='EXAMPLE')
add('E0092','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','规划及跟进产品研发周期，协调研发同事，跟踪产品开发进度','明确周期规划和进度跟踪，不从标题取值。')
add('E0602','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Build execution plans that define staffing, robot allocation, dependencies, milestones, and delivery timelines.','明确计划、依赖和里程碑。')
add('E0602','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','Strong track record of translating ambiguous goals into executable plans and successful outcomes.','一般要求可执行计划能力。')
register(list(R.values()),'Astra_v3_product_d')
