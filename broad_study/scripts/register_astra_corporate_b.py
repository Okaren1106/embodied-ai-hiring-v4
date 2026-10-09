from astra_review_tools import *
ids=['N0576','N0344','N0251','N0267','N0318','E0060','E0053','E0022','E0222','E0189','E0186','E0136']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['N0576']['judgment']='招聘体系开发、人才获取和雇主品牌为明确工作；HR专业学历退出方法能力。高级招聘经验的一般与行业优先分开，校园招聘为服务对象不作为申请受众。'
ov('N0576','N0576:5:0','相关专业学历不是方法经验。',metric='SEPARATE',branch='EDUCATION_FIELD')
add('N0576','V2_HR','GENERAL','UNCONDITIONAL','具备大批量研发团队招聘 + 高端技术人才引进双重实战经验','此半句为一般经验条件，后半句人形赛道优先独立。')
R['N0344']['judgment']='研发流程设计、梳理、实施和绩效改进是工作主体，不能仅保留PLM。项目理论为一般要求，IPD/CMMI名词保留目录外；流程规则编制补入明确方法。'
add('N0344','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','负责研发流程的梳理、编写、推广、实施与跟踪，解决流程无边界、职责交叉问题','本人编制与执行研发工作流程，非仅参与项目。')
add('N0344','V2_SOP_OPERATION','GENERAL','UNCONDITIONAL','5年以上研发流程设计经验','明确工作规程设计经验。')
add('N0344','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','熟悉项目管理理论与工具','明确理论与工具知识，上下文限定研发流程管理。')
R['N0251']['judgment']='战略研究没有独立冻结策略标签，但项目里程碑与实施节奏明确，不应全部零方法。理工/MBA背景不是机器人技术或会计资质。'
add('N0251','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','将公司战略重点和各部门年度工作规划拆解为可执行的项目与里程碑','明确本人项目计划与里程碑拆解。')
R['N0267']['judgment']='标准制修订与项目管控主任务成立；标准技术领域不是本人算法。补明确节点时间计划和具体标准法律约束应用，Office单项不推套件。'
add('N0267','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','统筹推进多标准项目并行，制定各节点时间表，确保按期完成','本人多项目节点计划。')
add('N0267','V2_LEGAL','DUTY_OWN_USE','UNCONDITIONAL','负责标准项目各阶段的技术材料准备，确保流程符合《标准化法》及行业管理要求','具体专业标准制定的法律流程应用，不是所有岗位普通守法条款。')
R['N0318']['judgment']='审计与准则知识成立；CPA优洗原文损坏，不当背景或擅自视为优先，明确资格强度未知。财务学历退出会计能力；未从融资资料推采购技能。'
ov('N0318','N0318:O1','CPA可识别，但优洗疑似文字损坏导致要求强度无法确定。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['REQUIRED','GENERAL','PREFERRED'])
ov('N0318','N0318:3:0','该句仅相关学历和CPA字样，专业知识由后文准则条款支持。',metric='SEPARATE',branch='EDUCATION_FIELD')
R['E0060']['judgment']='核算、税务及工具要求明确；中级会计持证为条件，CPA为优先，原复合句不得一起记优先。财会学位与能力分开，协作审计不是本人审计。'
ov('E0060','E0060:3:0','该句学历与资格不替代会计专业能力，能力另有完整证据。',metric='SEPARATE',branch='EDUCATION_FIELD')
ov('E0060','E0060:3:1','持有中级及以上证书与后句CPA优先分别判断。',metric='REQUIRED',quote='持有中级会计及以上证书')
ov('E0060','E0060:2:0','配合外部审计并提供资料是协作对象；本人的日常核算另有正例。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('E0060','V2_ACCOUNTING','GENERAL','CHOICE','有全盘账经验或制造业成本核算经验','特定核算经历明确任选，一般会计能力另有无条件证据。')
add('E0060','V2_ACCOUNTING','PREFERRED','CHOICE','有甲方和乙方（四大或八大）复合经验优先','优先雇主背景中审计机构路径明确or，不能当作全部持有某资格。')
R['E0053']['judgment']='政府关系为主，政策方法目录有限；重大展会/论坛组织与公关是明确传播工作，新增方法正例。不把政府关系等同销售或从规划能力推PMP。'
add('E0053','V2_MARKETING','DUTY_OWN_USE','UNCONDITIONAL','重大展会、论坛的组织与实施','本人组织对外公共传播活动。')
add('E0053','V2_MARKETING','GENERAL','UNCONDITIONAL','熟悉国家级重大活动、政府调研的流程与公关运作逻辑','明确公共关系活动专业知识，非一般沟通素质。')
R['E0022']['judgment']='技术政策、公文论证与政府沟通为任务，未写具体使用工具；政策研究仍为目录缺口。机构研究AI不推出岗位本人训练模型，公文写作不自动等于营销。'
R['E0222']['judgment']='无候选不等于无方法；原文明确招聘、雇佣流程、劳动关系专业工作以及普通/优先HR经验。补全文支持的HR与合同关系，研发是招聘对象。'
add('E0222','V2_HR','DUTY_OWN_USE','UNCONDITIONAL','负责业务部门面试筛选，聚焦研发、交付等核心岗位，推进人才引进、面试跟进及 landing','明确招聘流程本人执行。')
add('E0222','V2_HR','GENERAL','UNCONDITIONAL','3 年以上 HRBP 相关经验','明确专业经验一般要求。')
add('E0222','V2_HR','PREFERRED','UNCONDITIONAL','熟悉科技公司人才特点者优先','明确人才专业知识优先。')
add('E0222','V2_HR','PREFERRED','CHOICE','有科技公司、AI、智能制造、具身智能或工业机器人行业从业经验者优先','HRBP条款的行业经验任选，保留对象范围。')
add('E0222','V2_LEGAL','DUTY_OWN_USE','UNCONDITIONAL','负责入转调离、劳动合同管理、员工沟通及纠纷处理','雇佣合同与纠纷专业处理，不是行政签收合同。')
R['E0189']['judgment']='财务建模和成本分析有明确动作；学位与CPA不当作会计技能，准则知识另证。财务分析报告明确需要读取并解释财务报表，补本人会计财务报告应用。'
ov('E0189','E0189:1:0','此句学历与资格优先，不是普通会计知识要求。',metric='SEPARATE',branch='EDUCATION_FIELD')
add('E0189','V2_ACCOUNTING','DUTY_OWN_USE','UNCONDITIONAL','结合财务报表、业务数据，拆解营收、成本、利润、现金流等核心指标','本人财务报告专业分析；不声称本人完成全盘账或审计。')
R['E0186']['judgment']='成本模型、BOM核算、数据治理工作明确，补核算方法和成本模型开发。SQL/BI优先，但泛BI不自动补Tableau或Power BI。'
add('E0186','V2_ACCOUNTING','DUTY_OWN_USE','UNCONDITIONAL','【关键物料成本核算】主导关键物料成本模型搭建','明确财务成本核算，不从泛成本节省补核算。')
add('E0186','V2_ACCOUNTING','GENERAL','UNCONDITIONAL','熟悉成本核算流程','明确核算方法知识。')
add('E0186','SK_FINANCIAL_MODELING','DUTY_OWN_DEVELOP','UNCONDITIONAL','主导关键物料成本模型搭建','明确成本财务模型开发，而非只看财务数据。')
R['E0136']['judgment']='辅助课程开发中有明确本人完成大纲撰写的成果，保留课程开发；技术内容为教学对象。普通办公软件示例、技术知识优先任选示例均成立，课程经验普通并列不该未知。'
ov('E0136','E0136:O2','仅配合制作配套课件，未明确本人使用PowerPoint；明确使用能力已在一般要求中保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0136','E0136:O7','课程开发、教案编写、科普创作普通并列，无or与斜线。',branch='UNCONDITIONAL')
add('E0136','SK_CURRICULUM','GENERAL','UNCONDITIONAL','擅长将技术内容转化为易懂的课程内容','明确课程内容设计能力，不需精确词课程开发命中。')
register(list(R.values()),'Astra_corporate_fullread_b')
