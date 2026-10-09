from astra_review_tools import *
JUD={
'N0885':'明确医院机群例行及事故维护；RCA为支持关系，Required段故障诊断经验补入硬性要求，不从临床背景推医院流程。',
'E0343':'方案集成本人工作；一般Python原错引职责，TypeScript在Bonus段。编写集成程序是使用Python和协议，不开发这些工具。',
'N1033':'实验室运作与测试基础设施自有职责；AutoCAD基础knowledge硬性且proficiency优先需两种语境；实验室运行排障不称客户现场。',
'N0769':'客户部署与持续运行；Jira/Confluence在Extras段是优先，monitoring实施工具不必然是开发新工具，按证据保留使用。',
'E0546':'机器人维修技术与工具经验；CAD为上位任选恒成立，GoogleSuite属举例，Jira/Confluence并列无任选词。',
'E0557':'无关键词队列仍有实质招聘团队责任，补HR。客户接触经历不足以推具体服务方法；现场维护没有明示排障不加该项。',
'E0558':'夜班同类现场主管，保留独立广告身份；团队招聘责任明确，日常运营与技术资格分开。',
'N0695':'内部机器人机群维修和局部硬件控制改进，要求全在Preferred段。Looker/Tableau是看板使用例示，非开发这些第三方系统。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
add('N0885','V2_RCA','SEPARATE','COLLABORATION_OBJECT','Provide support of Root Cause Analysis for major incidents in the Field.','明确支持分析，非独立承担。')
add('N0885','V2_INCIDENT_SUPPORT','REQUIRED','UNCONDITIONAL','Technical experience necessary to troubleshoot complex robotic systems.','Required段明示运行系统排障经验。')
ov('E0343','O2','一般Python应锚一般资格，不能用职责冒充要求。',metric='GENERAL',quote='Expertise inPython, networking, and hardware/software system interfacing')
ov('E0343','1:0','including及etc明确工具对象举例。',branch='EXAMPLE')
ov('E0343','6:0','Bonus段括号etc举例，无明确任选。',metric='PREFERRED',branch='EXAMPLE')
add('E0343','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','Identify root causes of systemic issues and partner with engineering for long-term resolution','Identify由本人承担；partner修复另为协作。')
add('E0343','V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','Deliver advanced training and documentation to both internal teams and external customers','明确客户培训服务。')
ov('N1033','7:0','Required Skills明确覆盖该句。',metric='REQUIRED')
ov('N1033','9:0','e.g.明确例示。',branch='EXAMPLE')
add('N1033','V2_AUTOCAD','REQUIRED','UNCONDITIONAL','Working knowledge of AutoCAD for layout planning (proficiency preferred).','基本知识硬性与熟练优先同时存在，原只编码优先漏前者。')
add('N1033','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Develop and revise lab and testbed layouts.','本人测试环境开发，非仅测试执行。')
add('N1033','V2_PROCUREMENT','DUTY_OWN_USE','UNCONDITIONAL','Submit and manage purchase requisitions.','本人提出并管理实验室项目采购申请。')
for e in ['4:0','4:1']:ov('N0769',e,'The Extras That Set You Apart段。',metric='PREFERRED')
for e in ['O5','O7']:ov('N0769',e,'Implement监控诊断工具可以是配置实施，未明确研发工具；使用工具保障可靠性明确。',metric='DUTY_OWN_USE')
add('N0769','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Troubleshoot and resolve technical issues quickly to maintain uptime and mission success.','本人维持运行排障职责，不能只保留一般资格。')
add('N0769','V2_CUSTOMER_SERVICE','SEPARATE','COLLABORATION_OBJECT','Partner with customer teams to train and support operators in achieving operational readiness.','原文共同培训操作员，保留协作。')
ov('E0546','O4','Catia或CAD两者都满足上位CAD能力。',branch='UNCONDITIONAL')
ov('E0546','2:0','such as but not limited to为例示。',branch='EXAMPLE')
for e in ['4:0','4:1']:ov('E0546',e,'Experience using A,B,C并列，无or或例示标志。',branch='UNCONDITIONAL')
add('E0546','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Develop tools and document diagnostic procedures for process improvement','明确诊断工具开发。')
for r in ['E0557','E0558']:add(r,'V2_HR','DUTY_OWN_USE','UNCONDITIONAL','Onsite team hiring, development, and leadership','本人现场团队招聘，非广告投递通用说明。')
ov('N0695','1:0','contribute to documentation是协作，不能推独立开发排障体系；另补明确运行排障职责。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['2:0','2:1']:ov('N0695',e,'用工具做看板，括号是工具例示，无or。',metric='DUTY_OWN_USE',branch='EXAMPLE')
add('N0695','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Diagnose, troubleshoot, and repair complex mechanical, electrical, software, and perception system issues across a large fleet of robots.','本人机群运行维修。')
add('N0695','V2_INCIDENT_SUPPORT','PREFERRED','UNCONDITIONAL','Strong experience in diagnosing and repairing mechanical, electrical, and software systems.','Preferred Qualifications段，维修经验。')
add('N0695','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','Conduct root cause analysis, debugging, and testing for sensors, edge compute devices, and control systems.','本人明确RCA方法。')
register(list(R.values()),'Astra_v3_deploy_b')
