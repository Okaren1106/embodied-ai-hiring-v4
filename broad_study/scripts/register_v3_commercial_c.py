from astra_review_tools import *
JUD={
'N0743':'建筑行业销售全流程本人职责与一般/优先销售经验均明确，不能因候选器只抓project误报而漏销售方法。',
'N1039':'战略财务建模和Excel硬性要求，三表建模优先；并购sourcing非采购，内部呈现不补PowerPoint。',
'N0884':'医院客户成功经营、运行问题闭环与项目方法明确；优先账户经验旧误记一般，dashboard不推Excel具体品牌。',
'E0574':'内部软件用户支持含AI代理工作流、工单机制和招聘团队；Jira在Bonus段，软件Agent不同于人工代理。',
'E0444':'视频创作和项目统筹、一般脚本能力明确；Marketing专业学历不是营销技能；剪辑软件任选而非Linear工具。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
add('N0743','V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL','Lead complex sales cycles from initial engagement through contract execution','明确销售闭环。')
add('N0743','V2_SALES_CRM','GENERAL','UNCONDITIONAL','3+ years of quota-carrying sales experience','明确一般销售经验。')
add('N0743','V2_SALES_CRM','PREFERRED','UNCONDITIONAL','Experience selling construction technology, robotics, automation, or other solutions used directly in field operations and project execution','What Sets You Apart段明确销售产品领域优先。')
ov('N0884','6:0','Preferred Qualifications段。',metric='PREFERRED')
add('N0884','V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL','Manage client success operations across multiple hospitals in your territory','明确本人客户成功经营。')
add('N0884','V2_CUSTOMER_SERVICE','GENERAL','UNCONDITIONAL','you can hold a room with hospital executives, tell a crisp story with data, and handle hard conversations directly','医院客户沟通能力明确，不是通用跨团队沟通。')
add('N0884','V2_CUSTOMER_SERVICE','PREFERRED','UNCONDITIONAL','Hospital or healthcare operations experience is a strong plus','明确医院运营流程经验。')
add('N0884','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL',"you scope, sequence, track, escalate, and follow through. Details don't get lost on your watch.",'明确范围顺序和追踪方法。')
add('N0884','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Run a prioritized book of work per account — open issues, improvement projects, use case activations — with clear owners, dates, and status visible internally and to the client.','明确工作优先级、责任人和时序方法。')
for e in ['7:0','7:1']:ov('E0574',e,'Bonus Qualifications段。',metric='PREFERRED')
ov('E0574','5:0','such as、or与e.g.明确例示及任选。',branch='CHOICE_AND_EXAMPLE')
ov('E0574','4:0','原Partner句为协作，改本人escalation point。',metric='DUTY_OWN_USE',quote='Serve as the escalation point for complex, sensitive, or high-priority issues')
ov('E0574','O3','原quality泛指支持服务，不足以独立证明测试执行；改明确设计bug测量指标，属方法开发。',metric='DUTY_OWN_DEVELOP',quote='Define and report on key metrics for both support performance (CSAT, first response time, resolution time) and bug discovery (time to reproduction, escalation accuracy, defect signal quality)')
add('E0574','V2_AGENT_WORKFLOW','GENERAL','UNCONDITIONAL','Experience deploying and tuning AI-powered support agents, including flow design, guardrails, and escalation logic','明示AI工作流要求，不能只保留职责。')
add('E0574','V2_HR','DUTY_OWN_USE','UNCONDITIONAL','Build the team: hire, onboard, coach, and manage support specialists as volume and scope grow','本人招聘及入职团队责任。')
add('E0574','V2_CUSTOMER_SERVICE','GENERAL','UNCONDITIONAL','5+ years of experience in user or customer support for a software product, including 2+ years building or leading a support team','明确客户/用户支持经验。')
ov('E0444','6:0','Marketing仅学位专业选项，不是专业技能要求。',metric='SEPARATE',branch='EDUCATION_FIELD')
add('E0444','V2_MARKETING','DUTY_OWN_DEVELOP','UNCONDITIONAL','Write, script, storyboard, and pitch high-impact video concepts for product launches, digital campaigns, and narrative brand storytelling.','本人传播内容创作。')
add('E0444','V2_MARKETING','GENERAL','UNCONDITIONAL','Advanced scriptwriting, storyboarding, narrative pacing, and pitching high-impact video concepts for digital campaigns and product launches.','实际一般创作能力，与学历区分。')
add('E0444','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','Project planning, scheduling, budget/logistics management, and directing projects from pitch to final delivery.','明确计划预算方法。')
register(list(R.values()),'Astra_v3_commercial_c')
