from astra_review_tools import *
ids=['N0217','N0601','E0087','N0326','N0174','E0108','N0672','E0419','N0772']
R={rid:dict(reading_id=rid,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for rid in ids}
def ov(rid,eid,reason,**fields):R[rid]['evidence_overrides'].append(dict(evidence_id=eid,reason=reason,**fields))
def add(rid,c,m,b,q,reason):R[rid]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=reason))
degree={'N0217':'N0217:6:0','N0601':'N0601:4:0','N0326':'N0326:3:0','N0174':'N0174:4:0','N0672':'N0672:3:0','N0772':'N0772:4:0'}
for rid,eid in degree.items():ov(rid,eid,'工业设计学历专业属于教育背景，不等同本人CMF/工业外观方法能力的明确要求。',metric='SEPARATE',branch='EDUCATION_FIELD')
R['N0217']['judgment']='外观设计职责有据，AI在设计工具并列中为Illustrator；职责栏熟练掌握仍属能力描述，要求中的如/等是示例，学历专业分开。'
for e in EB[RID['N0217']]:
 if e['code'] in ['V2_PHOTOSHOP','V2_RHINO','V2_KEYSHOT','V2_ILLUSTRATOR']:
  ov('N0217',e['evidence_id'],'熟练掌握/使用的能力表达按一般要求；等或如为示例，不含or。',metric='GENERAL',branch='EXAMPLE')
add('N0217','V2_CMF_DESIGN','GENERAL','UNCONDITIONAL','能够高效完成外观建模、渲染和效果图制作','明确外观表现能力，非以学历名称补能力。')
R['N0601']['judgment']='工业外观/CMF本人设计成立；与产品经理一起实际开展用户研究不等于只把用户研究团队列为协作对象。专业学历不充当CMF能力。'
add('N0601','V2_CMF_DESIGN','GENERAL','UNCONDITIONAL','有较强的手绘和3D造型功底','明确工业外观造型表现能力。')
R['E0087']['judgment']='三个字段为同一简短广告的标点差异；无明确具名工具、CMF或用户研究方法，不从标题补标签。产品设计用途仍笼统，细任务保留未解决。'
R['E0087']['task_override']=dict(task='UNRESOLVED',quote='独立完成或配合团队完成产品设计工作',reason='正文只说产品创意设计及跟进，无明确外观/数字界面/人因或交互硬件对象；不由工业设计标题强分CMF细任务。')
R['N0326']['judgment']='本人用户研究、人因与外观设计有据；共同开发并实际测试原型仍有本人执行证据，区别于仅支援别的团队。2D/AI语义不明不自动映射Illustrator。'
add('N0326','V2_CMF_DESIGN','DUTY_OWN_USE','UNCONDITIONAL','4.外观造型与美学: 通过草图绘制、2D/AI效果图、3D建模和渲染 , 创作视觉前瞻、与品牌契合的设计。','本人外观造型方法，原候选误只检查营销而漏补工业外观。')
R['N0174']['judgment']='CMF能力有独立正文证据；专业学历单列，外观交付责任含独立或共同完成，不能强制全部为无条件本人使用。泛称AIGC软件不补具体工具。'
ov('N0174','N0174:2:0','句中独立或与团队合作完成，明确存在不同责任路径，保留职责任选；精通CMF能力另记一般要求。',branch='CHOICE')
add('N0174','V2_CMF_DESIGN','GENERAL','UNCONDITIONAL','精通CMF及量产环节','职责栏内明确能力要求按语义记录，不因标题自动当本人动作。')
R['E0108']['judgment']='数字界面与视觉体验主任务成立；工业设计专业不是CMF。没有工具名不补Figma；正文体验规划、信息界面及交互经验支持体验设计方法。'
add('E0108','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','负责产品视觉呈现方案设计，结合产品定位及使用场景，完成整体视觉体验规划。','本人规划视觉体验路径，符合体验设计方法定义。')
add('E0108','V2_UX_RESEARCH','GENERAL','EXAMPLE','具备3年汽车座舱车载HMI、3D交互、数字产品等相关视觉设计经验。','等列举相关界面设计经验，保留示例而非任选。')
R['N0672']['judgment']='工业设计职责、用户研究及可用性测试有据；Preferred Qualifications标题支配全部后续经验工具，学历仅教育背景；括号工具示例非任选。'
ov('N0672','N0672:4:0','原文位于Preferred Qualifications。',metric='PREFERRED')
for eid in ['N0672:5:0','N0672:5:1','N0672:5:2','N0672:9:0']:
 ov('N0672',eid,'Preferred Qualifications下的具体工具/工艺括号示例，没有or。',metric='PREFERRED',branch='EXAMPLE')
add('N0672','V2_UX_RESEARCH','PREFERRED','UNCONDITIONAL','Experience with human-centered design and ergonomic principles.','优先段明示人因设计方法。')
add('N0672','V2_DFM','DUTY_OWN_USE','UNCONDITIONAL','Ensure feasibility and manufacturability in collaboration with engineering teams.','本人把可制造性约束纳入设计，与工程团队共同执行，不是只列工程团队为对象。')
R['E0419']['judgment']='全文主要为跨物理/数字触点的服务、工作流与使用体验，修正窄数字界面细任务并补用户体验方法；公司背景安全不当本人的安全开发。'
R['E0419']['task_override']=dict(task='SERVICE_HUMAN_FACTORS',quote='Define operational workflows and end-to-end user experiences surrounding humanoid robot deployment, onboarding, servicing, maintenance, training, and day-to-day operation',reason='主交付为服务流程与端到端使用体验，不仅数字UI。')
add('E0419','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','Design and map user journeys, workflow definitions, interaction flows, and operational concepts across physical and digital touchpoints','本人用户旅程、服务与交互路径设计。')
add('E0419','V2_UX_RESEARCH','REQUIRED','UNCONDITIONAL','This role requires strong systems thinking, service and workflow design skills, and the ability to create clarity within complex and evolving operational environments.','明确requires服务和工作流设计能力。')
add('E0419','V2_UX_RESEARCH','GENERAL','UNCONDITIONAL','Strong portfolio demonstrating systems thinking, workflow architecture, service design, and operational experience design across complex environments','一般要求独立列出服务/体验设计能力。')
add('E0419','V2_UX_RESEARCH','PREFERRED','UNCONDITIONAL','Experience with service design, operational workflow design, or cross-touchpoint experience design','Nice to Have中方法经验；具体路径任选另在原文保留，同一上位体验方法亦有独立总括要求。')
add('E0419','V2_SAFETY_OPERATION','GENERAL','UNCONDITIONAL','Ability to safely use ladders, lifts, power tools, and other facility equipment','原文物理要求明示作业安全能力；保留源文本的非典型条款，不擅自删除。')
R['N0772']['judgment']='HRI硬件、音视频集成与CMF任务有据；工具斜线保留未知，Python or related language保持任选。标题和学历不能充当本人职责/方法要求；功能安全与法规为并列要求非任选。'
ov('N0772','N0772:1:0','标题只是角色命名，明确CMF职责有其他正文证据。',metric='SEPARATE',branch='TITLE_ONLY')
ov('N0772','N0772:9:0','动画工具为括号例示，外层or连接行为库，同时有任选和示例。',branch='CHOICE_AND_EXAMPLE')
for eid in ['N0772:12:0','N0772:12:1']:
 ov('N0772',eid,'functional safety and regulatory compliance为两个并列知识对象；括号SIL是安全等级，CE/FCC/UL为该上位法规知识的例子，无or。',branch='UNCONDITIONAL')
add('N0772','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL','Familiarity with CAD and 3D-print prototyping for rapid iteration on audio-visual hardware concepts.','明确3D打印增材制作方法一般要求，目录包含3D printing。')
register(list(R.values()),'Astra_design_seeded_fullread')
