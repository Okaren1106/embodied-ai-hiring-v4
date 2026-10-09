from astra_review_tools import *
JUD={
'E0056':'全流程销售独立负责，与参与销售策略制定分开；客户采购联系人网络不是采购技能。',
'E0096':'ToG/KA新客开拓与公共关系，短正文无任职要求，不补一般要求或技术工具。',
'N0493':'渠道体系建设与本人方案营销，外语及出差是工作条件；不从销售标题推一般销售经验要求。',
'N0118':'开发者活动与社区技术传播，有明确营销专业方法和一般/优先经验；无关键词不能漏运营方法。',
'N0453':'校招销售辅助为主，策略反馈和交办支持不是独立销售闭环；记录协作关系，不改冻结职能。',
'N0616':'区域政企商机经营与基地活动本人负责，补明确销售/营销职责与商务一般能力。',
'N0398':'平台文档和社区运营，不是Agent研发；Agent兴趣不能转成技术经验要求；补技术传播与操作手册。',
'N0362':'公关内容规划本人交付，活动配合与独立传播物料分开；一般PR经历及优先独立深度稿件分别编码。',
'N0210':'产品营销具硬性经历、一般GTM能力及优先国际产品经验；不把大模型宣传对象计本人研发。',
'N0204':'销售运营流程本人执行，一般销售/商业分析/PMO经历有分支未解，具体ToB销售流程独立明确。',
'N0130':'视频创意与内容传播；脚本能力一般要求明确，配合总监策划不能默认本人独立开发；投递作品不是HR。',
'N0108':'售后体系与重大客诉管理，补标准流程/服务/工单方法，岗位负责人不等机器人算法技能。',
'N0524':'售前与销售配合；经销伙伴培训本人负责。编程一种加例示，语言叶项应兼记任选。',
'E0013':'高校销售与招投标；熟悉高校采购流程为明示一般知识，可记要求但不推本人采购责任。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0056','1:0','标题不足，锚本人闭环责任。',metric='DUTY_OWN_USE',quote='独立负责从线索挖掘、需求对接、方案呈现、商务谈判、合同签订到交付验收与回款的全流程闭环管理')
ov('E0056','2:0','参与制定、协助市场定位。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0056','O1','至少一领域并且如举例。',branch='CHOICE_AND_EXAMPLE')
add('N0493','V2_MARKETING','DUTY_OWN_USE','UNCONDITIONAL','负责辖区的产品和行业应用为核心的解决方案营销、推广','明确本人营销推广。')
add('N0118','V2_MARKETING','DUTY_OWN_DEVELOP','EXAMPLE','策划并执行黑客松、Workshop、赛事、技术沙龙等线上线下活动','技术传播活动策划和执行，活动类型例示。')
add('N0118','V2_MARKETING','GENERAL','CHOICE','3年以上开发者运营、技术社区、活动运营或相关工作经验','运营经验明确任选类别。')
add('N0118','V2_MARKETING','PREFERRED','CHOICE','有开发者社区、高校合作或技术活动经验者优先','技术活动经验为优先任选。')
for e in ['1:0','2:0']:ov('N0453',e,'提供信息支撑与团队交办支持，不足以记独立销售经营。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0616','V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL','统筹厦门及福建省内商机挖掘、线索跟进与项目协同','明确商机经营责任。')
add('N0616','V2_MARKETING','DUTY_OWN_DEVELOP','EXAMPLE','策划组织政企研学、产业观摩、行业沙龙、技术开放日等活动','本人活动传播策划。')
add('N0616','V2_SALES_CRM','GENERAL','UNCONDITIONAL','能独立撰写政企汇报方案，具备高层商务接待、商务谈判能力','明确商务经营技能。')
add('N0398','V2_MARKETING','DUTY_OWN_DEVELOP','EXAMPLE','负责官方内容运营，包括模板、案例、教程等内容的策划与发布','明确技术内容策划传播。')
add('N0398','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','负责平台使用手册及帮助中心的编写与维护，持续完善功能文档、FAQ及操作指南','明确操作手册编制。')
add('N0398','V2_SOP_OPERATION','GENERAL','CHOICE','具备良好的文档能力与结构化表达能力，能够独立编写产品文档或使用手册','文档或手册任选。')
ov('N0362','2:0','原标题无动词证据，锚本人内容规划编辑。',metric='DUTY_OWN_DEVELOP',quote='负责机构官方自媒体矩阵（微信公众号、小红书等）的内容规划、编辑排版与日常运营')
ov('N0362','3:0','活动配合，但本人负责对外传播方案物料，缩短明确本人责任证据。',metric='DUTY_OWN_USE',quote='负责活动全流程的对外传播方案与物料把控')
add('N0362','V2_MARKETING','PREFERRED','UNCONDITIONAL','有独立完成过高传播力深度稿件（单篇阅读/行业认可度高）者优先','独立稿件优先须与一般经历分开。')
add('N0210','V2_MARKETING','REQUIRED','UNCONDITIONAL','硬性条件： 5-7年产品市场/技术营销经验，特别优秀可放宽到3年','营销经历硬性；放宽的是年限，不取消经历要求。')
add('N0210','V2_MARKETING','GENERAL','UNCONDITIONAL','懂市场，能独立制定GTM策略；具备出色的包装和营销能力','一般策略营销能力。')
add('N0210','V2_MARKETING','PREFERRED','UNCONDITIONAL','做过知名国际硬件产品营销的加分','明确优先经验。')
ov('N0204','2:0','销售运营/商业分析/PMO斜杠未明确关系；另有ToB流程一般能力保持确定。',branch='UNRESOLVED')
add('N0130','V2_MARKETING','GENERAL','UNCONDITIONAL','具备极其优秀的文字功底和脚本撰写能力，能够独立完成分镜头脚本，文字表现力强','明确营销视频内容能力，不是软件脚本。')
add('N0108','V2_SALES_CRM','DUTY_OWN_DEVELOP','UNCONDITIONAL','搭建并落地全渠道售后标准：服务流程、维保规则、退换货、故障处理规范','本人服务经营体系搭建。')
add('N0108','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','搭建并落地全渠道售后标准：服务流程、维保规则、退换货、故障处理规范','明确服务流程与操作规范。')
add('N0108','V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','处理重大及疑难客诉，维护客户关系，降低售后风险','明确服务沟通与投诉处置。')
add('N0108','V2_SALES_CRM','GENERAL','UNCONDITIONAL','懂多渠道售后逻辑，能独立制定售后流程、落地服务标准','一般售后经营方法要求。')
add('N0108','V2_INCIDENT_SUPPORT','GENERAL','UNCONDITIONAL','擅长工单管理、问题闭环、跨部门沟通，能独立对接B端客户与项目售后','工单记录与问题升级在服务运行语境。')
for e in ['O2','O3']:ov('N0524',e,'一种编程语言，括号等举例。',branch='CHOICE_AND_EXAMPLE')
ov('N0524','1:0','与销售配合，售前支持协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('E0013','V2_PROCUREMENT','GENERAL','UNCONDITIONAL','熟悉高校采购流程','明确候选人应有采购流程知识，区别实际工作承担。')
add('E0013','V2_SALES_CRM','GENERAL','UNCONDITIONAL','3 年以上高校科研、教学设备、机器人实验室解决方案直销经验','明确销售经验，不由工具候选替代。')
register(list(R.values()),'Astra_v3_commercial_a')
