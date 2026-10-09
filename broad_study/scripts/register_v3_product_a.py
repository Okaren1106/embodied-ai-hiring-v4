from astra_review_tools import *
JUD={
'N0479':'技术概念作为产品管理对象与加分背景分开；补明确风险与敏捷方法，市场切入计划为营销规划，不从全周期管理推本人软件开发。',
'N0062':'人机交互用户调研与体验路径是明确方法，虽无关键词队列仍可编码；PRD不直接等系统需求工程。',
'N0514':'导航产品规划非导航算法开发；一般导航/SLAM/感知技术与优先数据平台经验保留，PRD不补工具名称。',
'N0409':'TPM支持含具体计划里程碑与敏捷知识，前者配合关系、后者一般要求；不能凭支持职衔全部置零。',
'N0397':'AI产品技术理解不等模型研发；post-training原理在职责句但明确认知要求，补后训练。AI Agent为应用对象，修复与LLM/VLM任选关系。',
'N0229':'Scrum/Kanban及WBS在必须项应硬性；推行方法是使用，不是发明敏捷方法；PMP认证和SAFe实践不能混同。',
'N0040':'功能测试原参与句需重锚能独立完成方案验证；未写语言名，不从基础代码补Python等。',
'N0113':'基模项目解决方案管理，补明确风险范围/进度方法；模型是管理对象，商务拓展是支持。',
'N0022':'机器人场景产品实习，明确用户需求和体验调研，独立报告与协助市场研究分开；AI用户不等Agent工作流。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
add('N0479','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','协调硬件、软件、算法、测试等多团队资源，制定项目计划，跟踪关键节点，识别并管控风险','明确计划节点和风险管理。')
add('N0479','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','熟悉常见项目管理工具及敏捷/瀑布开发流程','二者均属于上位项目方法，具体方法内部关系不拆值。')
add('N0479','V2_MARKETING','DUTY_OWN_DEVELOP','UNCONDITIONAL','制定快速有效的产品市场切入计划','明确市场切入策略制定。')
add('N0062','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','持续跟踪具身智能、人机交互领域的技术发展，开展用户调研与竞品分析，打造差异化交互体验优势','明确用户研究。')
add('N0409','V2_PROJECT_METHOD','SEPARATE','COLLABORATION_OBJECT','拆解项目阶段任务，配合制定初步项目计划（含关键里程碑）','配合制定计划。')
add('N0409','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','3 年项目管理相关工作经验，了解敏捷开发基本流程','明确敏捷基本知识要求。')
ov('N0397','2:0','LLM、VLM、AI Agent或相关AI产品，Agent为任选。',branch='CHOICE')
add('N0397','V2_AGENT_WORKFLOW','GENERAL','UNCONDITIONAL','深入理解大模型、Agent、强化学习、多模态融合及语音交互等核心技术原理','独立一般资格理解Agent原理；与上条任选经历区分。')
add('N0397','V2_POSTTRAINING','GENERAL','UNCONDITIONAL','深入理解大模型预训练、微调、对齐、多模态理解、Agent框架、具身智能等核心技术','明确要求理解模型微调与对齐，不能以候选未列排除。')
for e in ['5:0','8:0']:ov('N0229',e,'该句在必须项。',metric='REQUIRED')
ov('N0229','2:0','推行已有Scrum/Kanban方法，非开发这些方法。',metric='DUTY_OWN_USE')
add('N0229','V2_PROJECT_METHOD','PREFERRED','CHOICE','拥有大规模敏捷（SAFe / LeSS）实践经验，或 PMP、ACP 等相关认证','明确敏捷实践与资格任选；方法上位分支为CHOICE。')
ov('N0040','O1','旧证据明确参与测试；另句独立方案验证可支持本人测试，重锚该句。',metric='DUTY_OWN_USE',quote='有基础代码能力，能独立完成方案验证')
add('N0113','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','负责项目全过程管理，跟踪进度、质量、风险及需求变更，推动关键问题及时闭环','明确风险与变更管理方法。')
add('N0113','V2_SALES_CRM','SEPARATE','COLLABORATION_OBJECT','支持重点客户拓展、方案宣讲、商务交流及标杆项目建设','支持商务拓展，非独立销售职责。')
add('N0022','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','独立完成用户需求分析、竞品调研、需求文档、项目进度跟踪与管理','结合F5场景体验分析，明确用户研究方法。')
register(list(R.values()),'Astra_v3_product_a')
register([dict(reading_id='N0853',review_mode='FOLLOWUP',judgment='复查冻结目录发现V2_GIT明示包含GitHub/GitLab托管平台别名；Actions是该平台工作流使用，本次恢复平台口径正例，报告不得狭称Git命令行要求。',evidence_overrides=[dict(evidence_id='N0853:33:0',metric='PREFERRED',branch='EXAMPLE',reason='依据冻结GitHub平台别名而非Git子串；与GitHub Actions例示一致。')],catalog_gap_notes=['V2_GIT包含GitHub/GitLab平台，报告标签须说明，不能等同Git命令行熟练度。'])],'Astra_v3_git_platform_scope')
