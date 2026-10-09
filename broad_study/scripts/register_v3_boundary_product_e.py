from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0883':'硬件工程TPM：Desired Skills为优先技能；团队负责寻源不等于本人采购，资格经验不能作职责；补明确项目流程方法。',
'N0791':'联邦项目：项目计划与风险是实质专业方法；Jira/Asana为for example加or，PMP单独优先。',
'N0741':'ML工程PM：工具在What Sets You Apart，明确and；PMP/Scrum Master是资格上位，不另作方法要求。',
'E0579':'NPI TPM：回查F37至F51没有加分标题，ERP/MRP/PLM皆一般；采购/NPI/资本化经验任选，项目方法明确。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','O8','O9','O10','O11']:ov('N0883',e,'Desired Skills父标题为优先要求，保留原具体分支。',metric='PREFERRED')
for e in ['O2','O3']:ov('N0883',e,'CAD在1 or more技能方向中，具体两工具虽and，仍受上层选项约束。',branch='CHOICE')
ov('N0883','3:0','AE Group负责寻源的团队背景，并未明确该PM本人采购。',metric='SEPARATE',branch='TEAM_BACKGROUND')
ov('N0883','6:0','原引Desired Skills经验，不是职责。',metric='PREFERRED')
add('N0883','V2_PROJECT_METHOD','DUTY_OWN_DEVELOP','UNCONDITIONAL','Establish, improve, and execute program management methodologies and processes to improve development speed, design quality, and project tracking.','本人建立并改进项目方法。')
add('N0883','V2_PROJECT_METHOD','PREFERRED','UNCONDITIONAL','Working knowledge of project management tools, processes and procedures','Desired Skills一般项目方法知识。')
for e in ['5:0','5:1']:ov('N0791',e,'for example与or均有。',branch='CHOICE_AND_EXAMPLE')
add('N0791','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Drive strategic execution across multi‑project portfolios defining milestones, manage budgets, oversee resourcing across engineering, field ops, product, and business teams.','明示里程碑/预算/资源管理。')
add('N0791','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','Demonstrated ability to translate high-level requirements into structured task breakdowns and timelines.','明示任务分解及进度方法能力。')
for e in ['2:0','2:1']:ov('N0741',e,'What Sets You Apart内工具，and明确。',metric='PREFERRED',branch='UNCONDITIONAL')
ov('N0741','6:0','Certified Scrum Master等是资格，不作为方法能力附加正例。',metric='SEPARATE',branch='QUALIFICATION_NOT_METHOD')
ov('N0741','6:1','PMP/Scrum Master/同等Agile均项目资格上位。',branch='UNCONDITIONAL')
add('N0741','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Own the program-level picture across concurrent research and engineering workstreams: what is in flight, who owns it, what is due, and what is slipping.','明确跨项目责任人、到期和延期跟踪。')
for e in ['5:0','5:1']:ov('E0579',e,'such as Notion/Linear等工具例示，非明确任选。',branch='EXAMPLE')
ov('E0579','6:0','采购/NPI/资本化要求跨领域or。',branch='CHOICE')
ov('E0579','7:0','仍在一般要求；ERP/MRP斜杠关系未明。',metric='GENERAL',branch='UNRESOLVED')
ov('E0579','7:1','仍在一般要求，PLM或其他生产工具任选。',metric='GENERAL',branch='CHOICE')
add('E0579','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','development schedules, risk mitigation, build matrix management, material forecasting and planning, Clear-to-Build (CTB) analysis','明确本人项目日程/风险/计划执行。')
add('E0579','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','Strong organizational and project management skills, with a proven ability to drive process improvements and manage multiple priorities in a fast-paced environment.','明确一般项目管理方法能力。')
register(list(R.values()),'Astra_v3_boundary_product_e')
