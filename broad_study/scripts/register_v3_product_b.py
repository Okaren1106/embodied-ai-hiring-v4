from astra_review_tools import *
JUD={
'N0608':'机器人硬件产品规划与体验指标跟踪；用户体验分析有明文，未从专业背景推机械技术。',
'N0596':'人形产品实习全部协助或参与；用户操作手册整理作协作SOP，不补具体项目方法和软件工具。',
'N0536':'交付项目管理明确计划、里程碑、风险与回款节点；无关键词不等无方法，商务客户关系独立责任明确。',
'N0533':'系统平台产品定义包含明确Eval指标及系统工程约束，不能仅凭产品职能拒绝其测量设计职责；Agent平台一般认知有任选。',
'N0307':'项目范围风险方法本人使用，另有管理机制建设；PMP知识不等证书，实际证书句独立优先。',
'N0278':'软件算法项目管理，Jira/Git等是例示而非任选；补明确计划风险职责。原文末尾截断，优先语境的未提及格不能全部当可靠零。',
'E0036':'MaaS产品定义，MES对接不等研发MES；WMS/MES斜杠未解，技术原理资格重锚实际任职要求；模型微调认知补后训练。',
'E0020':'多模态产品体验研究，感知一般知识重锚要求段；交互指标定义和用户研究是本人具体方法，不能从一般AI Native工作流推Agent。',
'E0267':'软件产品用户研究本人主导，控制/导航/感知要求明确一项或几项，保留任选。',
'E0263':'整机软件项目管理包含自己主导端到端验证，应是执行而非开发评测工具；项目方法明确且另有机制开发。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
add('N0608','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','跟踪产品效果，包括用户体验、满意度等指标，确保产品符合需求定义','产品体验指标研究，非服务运营满意度。')
add('N0596','V2_SOP_OPERATION','SEPARATE','COLLABORATION_OBJECT','协助整理产品技术文档，包括用户操作手册等','明确协助整理操作手册。')
add('N0536','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','对接客户需求，拆解交付里程碑，协调研发、算法、测试、部署等团队资源，推动项目按期高质量交付','明确里程碑方法。')
add('N0536','V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL','负责项目商务相关事项的跟进，包括交付范围确认、验收签字及回款节点把控','明确商务交付及回款管理。')
ov('N0533','O2','本人定义系统Eval评价指标，不仅作为管理对象提及；按测量设计职责。',metric='DUTY_OWN_DEVELOP')
add('N0533','V2_REQUIREMENTS_ENGINEERING','DUTY_OWN_DEVELOP','UNCONDITIONAL','定义系统级 Eval，包括端到端任务成功率、链路时延、稳定性、资源消耗、异常恢复、兼容性和版本回归','明确系统指标和验证设计，超过一般需求文档。')
add('N0533','V2_AGENT_WORKFLOW','GENERAL','CHOICE','对大模型、Agent平台或AI研发交付流程有一定理解','AI Agent平台认知，明确任选。')
add('N0307','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','负责专项项目的目标、范围、计划、质量、资源管理','明确范围计划方法。')
ov('N0307','1:1','具有PMP、ACP等证书是例示，没有或。',branch='EXAMPLE')
for e in ['2:0','2:1']:ov('N0278',e,'Jira、Git、Tapd等例示。',branch='EXAMPLE')
add('N0278','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','负责主导制定软件及算法类研发项目的的整体计划、预算、资源需求和风险评估','明确计划与风险方法。')
R['N0278']['source_limits']=[dict(metrics=['PREFERRED'],codes=['ALL_APPLICABLE'],reason='冻结正文最后止于持有PMP、ACP或同等项目管理认证者优，优先句截尾；已明确优先正例保留，未提及不全视零。')]
ov('E0036','1:0','产品工具链对接MES是产品管理对象，不是开发MES系统。',metric='SEPARATE',branch='UNRESOLVED')
ov('E0036','2:0','MES/WMS对接斜杠关系未解，不强判任选。',branch='UNRESOLVED')
ov('E0036','O2','同句MES/WMS关系未解。',branch='UNRESOLVED')
for e in ['O8','O9']:ov('E0036',e,'原误引职责，实际一般资格有模型微调和数据采集。',metric='GENERAL',quote='深度理解 MaaS、模型微调、数据采集、端云部署全流程')
add('E0036','V2_POSTTRAINING','GENERAL','UNCONDITIONAL','深度理解 MaaS、模型微调、数据采集、端云部署全流程','明确模型微调认知。')
ov('E0020','O3','改用一般资格原句，非职责产品定义。',metric='GENERAL',quote='深度理解多模态交互：语音对话、视觉感知、动作控制、Channel 协同的设计逻辑与技术边界。')
add('E0020','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','完成用户调研、流程设计、故事板与 Demo 方案输出','明确用户研究与体验路径。')
add('E0020','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','制定交互指标（响应时延、理解准确率、意图匹配、动作流畅度等）','本人定义可测交互效果指标。')
add('E0267','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','主导竞品调研、用户调研、需求洞察','明确用户研究职责。')
ov('E0263','O5','主导端到端验证是测试执行，没有写开发工具/评测方法。',metric='DUTY_OWN_USE')
add('E0263','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','进行风险评估，制定缓解计划，并确保项目在预算内按时、按质交付','明确风险方法实施。')
add('E0263','V2_PROJECT_METHOD','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立和优化软件项目管理流程、工具和模板','本人项目管理方法工具模板建设。')
register(list(R.values()),'Astra_v3_product_b')
