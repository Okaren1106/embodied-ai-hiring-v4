from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0314':'FP&A金融回报建模和Office/Google套件要求明确；公司宣传和薪资美元保持排除。',
'E0372':'总薪酬总监核心薪酬制度设计及一般HR经验漏标；与招聘团队合作另记，HR资格全部选项属于上位。',
'E0450':'前台设施职场角色边界明确；访客系统/Jira或同类系统为任选例示，办公室与高管C级不误标技术。',
'E0370':'税务经理本人建立税务政策并进行税务报告管理明确，补读全文职责找到直接依据；Avatax保持目录外。',
'N1023':'Atlas培训内容开发与执行培训均明确；Required段动捕能力需同口径；遥操属于被培训人员，非本人操作。',
'E0454':'商业法务法律策略与要求漏标；数据许可为法律对象，不是数据管道技能；硬件供货合同有明确职责原文。',
'E0473':'Finance经理现有财务模型和Excel/Sheets任选、SQL加分可保留；另有财务报告专业要求。',
'E0469':'墨西哥设施文档维护与外部承包商协作，本人建立playbook明确；补SOP而非只保留安全主题。',
'E0474':'巴西财务：成本建模支持实体搭建属协作，财务模型职责另有独立证据；ERP具体品牌为例示，补监管财务流程。',
'N0718':'技术文档：撰写排障手册不是本人排障；软件经验属于Preferred，Git/Jira/Confluence都不能记一般。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0372','3:0','Partner with Talent Acquisition明确协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0372','5:0','CCP、CEBS和PHR/SPHR都是人力资格，上位明确。',branch='UNCONDITIONAL')
add('E0372','V2_HR','DUTY_OWN_DEVELOP','UNCONDITIONAL','Own job architecture, leveling frameworks, and salary structures across engineering, business, and operations functions','本人建立职位职级薪资结构。')
add('E0372','V2_HR','DUTY_OWN_USE','UNCONDITIONAL','Lead compensation cycles (merit, equity refresh, promotions), including modeling, calibration, and manager communications','本人薪酬周期管理。')
add('E0372','V2_HR','GENERAL','UNCONDITIONAL','10+ years in compensation, total rewards, or a combined people operations role','全部经验选项属于人力工作。')
ov('E0450','5:0','e.g. Jira or comparable systems。',branch='CHOICE_AND_EXAMPLE')
add('E0370','V2_ACCOUNTING','DUTY_OWN_DEVELOP','UNCONDITIONAL','You will establish and maintain the company’s tax policies, processes, and governance','本人建立税务制度流程。')
add('E0370','V2_ACCOUNTING','DUTY_OWN_USE','UNCONDITIONAL','Manage income tax accounting and reporting under ASC 740, including tax provision preparation, deferred tax calculations and reconciliations, and related disclosures.','实际税务核算与报告责任。')
ov('N1023','O1','Develop training content是本人开发课程。',metric='DUTY_OWN_DEVELOP')
add('N1023','SK_CURRICULUM','DUTY_OWN_USE','UNCONDITIONAL','Deliver training on commercially available BD product-lines, software, APIs, and solution infrastructures.','另有直接授课执行。')
ov('N1023','6:0','Required Skills & Experience段与其他必需能力统一。',metric='REQUIRED')
ov('E0454','O3','数据收集处理合同经验不等于数据管道技能。',metric='SEPARATE',branch='LEGAL_APPLICATION_OBJECT')
ov('E0454','4:0','原标题重锚实际法律供货合同责任。',metric='DUTY_OWN_USE',quote='Act as the legal lead for manufacturing, distribution, and vendor agreements. Navigate international trade and Asian supplier ecosystems to secure physical components, lock in supply continuity, and protect our IP.')
add('E0454','V2_LEGAL','DUTY_OWN_DEVELOP','UNCONDITIONAL','Define our legal strategy for AI training data. Structure novel agreements for real-world data collection and ownership, ensuring Figure strictly controls its proprietary datasets while navigating global privacy regimes.','本人制定法律策略及数据许可合同。')
add('E0454','V2_LEGAL','GENERAL','UNCONDITIONAL','Ability to frame complex legal issues succinctly for executive leadership','明确法律问题分析能力。')
add('E0473','V2_ACCOUNTING','GENERAL','UNCONDITIONAL','Strong understanding of budgeting, forecasting, long-range planning, and financial reporting','财务报告知识明确。')
for e in ['O1','O2']:ov('E0469',e,'junto a los contratistas externos明确与外部承包商共同建立维护安全文档。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('E0469','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Construir el playbook (manual de procesos) de facilities, incluyendo procesos, proveedores y presupuestos, conforme a los estándares de Figure.','本人建立设施流程手册。')
ov('E0474','O2','Apoiar a estruturação为支持本地实体筹建，协作语境。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['2:0','2:1']:ov('E0474',e,'ERP括号etc.是例示，无任选词。',branch='EXAMPLE')
add('E0474','V2_ACCOUNTING','DUTY_OWN_USE','UNCONDITIONAL','Garantir que os processos financeiros cumpram os requisitos regulatórios brasileiros (e.g., Receita Federal, eSocial, INSS, FGTS).','本人保证财务流程符合当地法规；只记文本要求。')
for e in ['O1','O2']:ov('N0718',e,'e.g.和or similar并存。',branch='CHOICE_AND_EXAMPLE')
ov('N0718','O4','原引用公司背景，实际要求仅行业经历，不能推出ML技术知识。',metric='SEPARATE',branch='INDUSTRY_EXPERIENCE_OBJECT')
for e in ['1:0','2:0']:ov('N0718',e,'编写给操作者使用的排障手册，不是本人运行排障。',metric='SEPARATE',branch='DOCUMENTATION_OBJECT')
ov('N0718','4:0','Preferred段Git文档工作流e.g.例示。',metric='PREFERRED',branch='EXAMPLE')
for e in ['7:0','7:1','7:2']:ov('N0718',e,'Preferred段such as例示，无任选词。',metric='PREFERRED',branch='EXAMPLE')
add('N0718','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Author clear deployment, configuration, maintenance, and troubleshooting documentation that enables operators and customers to run and manage fleets of robots in production environments','本人编制运行操作规程，不是亲自维护机器人。')
register(list(R.values()),'Astra_v3_boundary_corporate_c')
