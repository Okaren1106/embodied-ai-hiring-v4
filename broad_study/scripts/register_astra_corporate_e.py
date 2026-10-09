from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ['N0994','N0881','N0849','N0699']}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['N0994']['judgment']='资金风险模型同时有开发与使用，明确must的Excel条件保留。会计准则维护分配给本人的账户是职责不是一般要求；参与SOX项目不计本人方法交付。资格要求保留示例与任选。'
add('N0994','SK_FINANCIAL_MODELING','DUTY_OWN_DEVELOP','UNCONDITIONAL','Develop, measure, and refine liquidity risk models and stress-testing frameworks','本人创建改进流动性风险模型，原仅记使用遗漏开发语境。')
ov('N0994','N0994:3:0','该语句位于职责：通过维护指定账户参与结账，本人账户责任明确。',metric='DUTY_OWN_USE')
ov('N0994','N0994:6:0','Participate in projects including引出SOX控制建立，未明确本人开发/实施。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0994','N0994:8:0','such as CFA, FRM, or CTP限定具体财会金融资格路径，记录任选示例，不称全部持证。',branch='CHOICE_AND_EXAMPLE')
R['N0881']['judgment']='会计本人结账、凭证和工资处理明确，不能只计工资HR。GAAP位于requires句，ERP与ADP同为highly preferred但or仅限定Netsuite。一般保密不是安全技术或人力方法。'
ov('N0881','N0881:O1','整句ERP and ADP由highly preferred共同支配。',metric='PREFERRED')
ov('N0881','N0881:O7','普通保密责任不能自动计入专业安全技术。',metric='SEPARATE',branch='GENERAL_CONFIDENTIALITY')
ov('N0881','N0881:17:0','普通保密品格，不是明确人力流程能力。',metric='SEPARATE',branch='GENERAL_CONFIDENTIALITY')
ov('N0881','N0881:5:0','小节标题本身不是动作；工资执行另有清楚正例。',metric='SEPARATE',branch='SECTION_HEADING')
for eid in ['N0881:3:0','N0881:4:0']:ov('N0881',eid,'This role requires明确支配GAAP知识。',metric='REQUIRED')
ov('N0881','N0881:14:1','Netsuite or similar仅修饰ERP工具，外层and连接ADP，ADP不任选。',branch='UNCONDITIONAL')
add('N0881','V2_ACCOUNTING','DUTY_OWN_USE','UNCONDITIONAL','Execute month-end, quarter-end, and year-end close activities according to the corporate schedule.','明确本人结账职责，避免关键词漏掉实质会计工作。')
add('N0881','V2_HR','PREFERRED','UNCONDITIONAL','Payroll experience is strongly preferred.','局部工资流程经验为优先要求。')
R['N0849']['judgment']='战略发展岗位的财务建模Required明确；AI/机器人好奇心不当技术经验。本人建立内部操作流程可入方法目录，其他资本市场/策略内容仍保留目录覆盖局限。'
add('N0849','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Build and improve internal processes to increase efficiency and scalability across the organization','明确内部操作流程设计改进，不是普通性格能力。')
R['N0699']['judgment']='所有资格段均Preferred，QuickBooks/会计/工资不能误作GENERAL。本人会计与工资、ERP操作明确；CPA可在考不等于全部持有，命名Rillet/Rootstock保留目录外对象。'
for eid in ['N0699:12:0','N0699:14:0','N0699:16:0']:ov('N0699',eid,'位于Preferred Qualifications，不能混同一般要求。',metric='PREFERRED')
add('N0699','V2_ACCOUNTING','PREFERRED','UNCONDITIONAL','5-8 years of hands-on accounting experience, with at least 2-3 years in a similar full-cycle role','补优先段完整核算经验，强调这是广告表达强度。')
register(list(R.values()),'Astra_corporate_fullread_e')
