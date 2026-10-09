from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ['E0395','N0931','E0596','E0353']}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['E0395']['judgment']='高管行政、行程及SAP Concur费用申报明确。SAP保留Concur具体子型，不概括为ERP实施；报销不是专业会计，日程优先级triage不是运行故障，不从office推Microsoft Office。'
R['N0931']['judgment']='招聘、人力制度设计及雇佣法律知识均明确，不能只保留招聘一次动作。工具由such as和or共同限制；People systems未确定为HRIS信息软件，保留对象未知。Agent自动化为明确开发工作。'
ov('N0931','N0931:O1','People systems可能指组织管理体系，未明确为人事信息软件；对象未知。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for eid in ['N0931:3:0','N0931:3:1']:ov('N0931',eid,'platforms such as ... or ...为任选加示例。',branch='CHOICE_AND_EXAMPLE')
add('N0931','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL','Build and implement agent-based automations to make day-to-day work more human.','明确Agent自动化流程开发，不是招聘代理人。')
add('N0931','V2_HR','DUTY_OWN_DEVELOP','UNCONDITIONAL',"Design and scale People programs and processes that support Pickle's continued growth.",'本人设计人力专业流程。')
add('N0931','V2_HR','GENERAL','CHOICE','10+ years of progressive People Operations or HR leadership experience','一般人力专业经验，or连接管理方向。')
add('N0931','V2_HR','GENERAL','UNCONDITIONAL','Experience leading organizational change, restructures, and scaling organizations through periods of growth or transformation.','明确组织变革经验；growth/transformation仅发生阶段，不构成不同方法的替代。')
add('N0931','V2_LEGAL','GENERAL','UNCONDITIONAL','Strong knowledge of multi-state employment law and HR compliance.','明确跨州雇佣法专业知识，不是普通法律声明。')
R['E0596']['judgment']='招聘协调流程开发和Ashby使用明确；局部Ashby preferred必须从一般ATS能力中拆出。兴趣不当专业经验，优先技术招聘经验另有原文。面试calibration排除传感器标定。'
ov('E0596','E0596:5:0','括号明确Ashby preferred；ATS上位普通要求不能让具体工具升级为普通要求。',metric='PREFERRED')
ov('E0596','E0596:4:0','recruiting coordination, executive assistance, or scheduling明确任选经历。',branch='CHOICE')
ov('E0596','E0596:9:0','兴趣于HR职业路径不是已具备HR技术或经验。',metric='SEPARATE',branch='CAREER_INTEREST')
add('E0596','V2_HR','PREFERRED','UNCONDITIONAL','Experience coordinating technical hiring (engineering, ML, research) where interview loops are complex, and interviewers are in high demand.','明确技术招聘协调经验，技术领域是招聘对象。')
add('E0596','V2_HR','PREFERRED','CHOICE','Exposure to offer operations: packet assembly, background checks, I-9 coordination, or onboarding handoff.','优先录用流程经验中的步骤任选。')
R['E0353']['judgment']='技术人才寻访不是采购，GitHub为人才来源不是Git代码协作。AI/ML是招聘对象不计本人模型经验；补普通寻访能力和优先经历的局部分支。'
ov('E0353','E0353:O4','招聘AI/ML人才的行业经验，不是本人机器学习模型知识。',metric='SEPARATE',branch='RECRUITMENT_OBJECT')
ov('E0353','E0353:13:0','行业经验清单含or，AI/ML内部斜线限定招聘行业，不是本人ML未知。',branch='CHOICE')
add('E0353','V2_HR','GENERAL','UNCONDITIONAL','4+ years of technical sourcing experience','明确人才寻访专业经验。')
add('E0353','V2_HR','PREFERRED','CHOICE','Experience sourcing engineering leadership or executive-level technical talent.','优先人才层级任选；招聘对象不转成工程领导能力。')
add('E0353','V2_HR','PREFERRED','UNCONDITIONAL','Ability to leverage talent market data to influence sourcing strategy.','明确使用人才市场数据制定招聘策略能力。')
register(list(R.values()),'Astra_corporate_fullread_c')
