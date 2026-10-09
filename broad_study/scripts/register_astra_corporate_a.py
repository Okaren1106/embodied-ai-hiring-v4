from astra_review_tools import *
ids=['N0456','N0659','E0067','N0248','N0422','N0416','N0402','N0385','N0370','N0233','N0213','N0640','N0184','N0052']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['N0456']['judgment']='财务管培；参与轮岗/协助核算不提升为本人方法承担。财会学历与知识分开，普通要求明确会计准则；初级职称优先与CPA等部分科目通过分开，不声称持有CPA。'
for eid in ['N0456:O1','N0456:1:0','N0456:2:0']:ov('N0456',eid,'参与/协助条款保留学习与协作关系，非明确本人交付。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0456','N0456:3:0','本句为相关专业学历清单，另有独立会计知识要求。',metric='SEPARATE',branch='EDUCATION_FIELD')
ov('N0456','N0456:6:0','CPA/ACCA/CFA斜线未明，且原文仅部分科目通过；不得解释为持证。',branch='UNRESOLVED')
R['N0659']['judgment']='多地行政、制度与费用管理明确；采购成本优化未明示询报价/寻源/商务谈判，退出采购方法正例。行政流程编制可单列操作规程。'
ov('N0659','N0659:1:0','仅优化采购后勤成本，未明示冻结采购标签要求的流程动作。',metric='SEPARATE',branch='PROCUREMENT_COST_OBJECT')
add('N0659','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','搭建并优化公司行政管理制度、流程，推动制度落地执行，规范行政办公、后勤保障等各项工作','本人制定具体行政/后勤运行规范，非普通守时要求。')
R['E0067']['judgment']='技术政策情报、资料校对及辅助科研/标准活动明确；不因AI/自动控制学历或科研话题补机器人算法能力。政策研究方法尚属目录缺口，零编码不等于没有专业工作。'
R['N0248']['judgment']='政策与政府申报任务明确，项目策划、优先级与全生命周期工作是方法正例；协同财务审计材料未计本人会计审计。专业政策知识保留目录外限制。'
add('N0248','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','制定公司年度项目申报策略与优先级规划','明确本人项目优先级计划，未宣称发明项目管理方法。')
add('N0248','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','具备项目全周期管理经验','与前文项目策划、评审、实施、验收全周期动作共同定位的管理要求。')
R['N0422']['judgment']='融资规划、尽调谈判和资本运作为任务；不能把融资当采购，把一般项目管理能力推为PMP，资本市场方法在冻结目录下仍有覆盖缺口。'
R['N0416']['judgment']='海外政府关系与政策支持，未提个人使用软件或机器人技术方法；学历方向与业务政策对象保留，不能从海外资源推法律资格或销售技术。'
R['N0402']['judgment']='融资支持与研究、财务预测能力明确，但不等于会计核算或成本分析；无关键词记录经全文核对后保持，同时承认财务建模/尽调目录覆盖不足。'
R['N0385']['judgment']='战略、商业模式、行业数据分析与执行规划明确；没有具体软件或项目方法名称，不从宏观战略岗位泛化成每种管理技术；冻结目录对此工作覆盖有限。'
R['N0370']['judgment']='课程设计之外，本人还建立培训运营标准并承担收入与渠道，需补经营与操作流程方法。机器人培训不自动等于亲自开发机器人技术。'
add('N0370','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','搭建覆盖"需求、日程、接待、课程、讲师、考核、反馈"的标准化培训运营闭环','明确本人编制培训运营规程。')
add('N0370','V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL','制定定价策略，承担收入目标与渠道拓展','明确培训产品经营，不只是一般客户沟通。')
add('N0370','V2_SALES_CRM','GENERAL','UNCONDITIONAL','主导过认证体系整合统一、课程产品化与商业化转型','明确课程商业化经营经验。')
R['N0233']['judgment']='法律合同工作和知识明确；协助项目意见与法规更新保留协作，岗位职责标题不独立作本人方法证据。法律资格通过考试为显式条件；企业经验优先另补。'
for eid in ['N0233:5:0','N0233:6:0']:ov('N0233',eid,'此条仅协助/参与，其他独立法律职责证据仍存在。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0233','N0233:3:0','小节标题本身不独立证明动作；保留后文明确咨询服务证据。',metric='SEPARATE',branch='SECTION_HEADING')
add('N0233','V2_LEGAL','PREFERRED','UNCONDITIONAL','有企业法务工作经验者优先','此前同句只记录一般法务经验，漏优先分支。')
R['N0213']['judgment']='招聘与HRBP本人职责明确；招聘经验为一般要求，HRBP经验优先，劳动人事法规为明确法律方法要求，不能只保留HR关键词。'
add('N0213','V2_HR','PREFERRED','UNCONDITIONAL','有HRBP经验优先考虑','同句一般招聘与优先HRBP经验分开。')
add('N0213','V2_LEGAL','GENERAL','UNCONDITIONAL','熟悉招聘全流程及劳动人事相关法规政策','明确专业雇佣法规知识，区别普通遵纪守法。')
R['N0640']['judgment']='专利管理是明确法律方法，原关键词流程遗漏主体工作。机械/控制是专利保护对象而非本人研发要求；有代理资格或备考属于优先任选，不能写作全部已持证。'
ov('N0640','N0640:O2','机械结构专利经验的技术对象，不等价本人机械结构设计方法能力。',metric='SEPARATE',branch='IP_SUBJECT')
ov('N0640','N0640:1:0','有资格或正在备考明确任选，资格程度保留原文。',branch='CHOICE')
add('N0640','V2_LEGAL','DUTY_OWN_USE','UNCONDITIONAL','组织专利挖掘并形成成体系的专利布局，应申尽申','明确本人专利法律工作，目录包含专利职责。')
add('N0640','V2_LEGAL','GENERAL','UNCONDITIONAL','熟悉中国发明专利申请流程','明确专利法务专业要求。')
add('N0640','V2_LEGAL','PREFERRED','CHOICE','有机器人，机械结构，自动化设备或智能硬件相关专利经验','加分项专利经验按明确对象or保留。')
R['N0184']['judgment']='本人诉讼、证据、合同与法律风险工作成立，参与重大评估后另有本人提出建议，不删整条。补优先诉讼经历与仲裁/跨区域任选，法律学历不计资质。'
add('N0184','V2_LEGAL','PREFERRED','UNCONDITIONAL','有企业法务诉讼管理经验；有律师事务所诉讼经验','加分项内两个并列经验没有or。')
add('N0184','V2_LEGAL','PREFERRED','CHOICE','具备仲裁案件或跨区域纠纷处理经验者优先','明确任选子经验。')
R['N0052']['judgment']='本人搜索、沟通、评估与招聘有据；同事协作收集数据完成报告可保留本人工作。校招等在职责中是招聘对象，实习受众另有职位名证据，不能仅由招聘对象决定。'
register(list(R.values()),'Astra_corporate_fullread_a')
