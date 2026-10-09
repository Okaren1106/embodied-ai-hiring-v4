from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0590':'营销PMO：标题不能替代独立执行证据；供应商商务谈判实际在职责，CRM推广不等于本人用指定软件；加分段工具已校正。',
'N0583':'产品售后：维修结构、基础技术、任选仿真和未解Python/C++保留；上位仿真一般能力不随具体平台任选变成未知。',
'N0568':'在线售后客服：工单响应与升级为本人服务工作，非独立深度技术排障；工作说明中的飞书CRM是职责，不是Preferred。',
'N0565':'BI战略研究：Excel/Python/BI斜杠未解保留，不把BI泛称补成特定平台。',
'N0545':'遥操售前：咨询/方案/参与交付不是本人遥操作；保留遥操知识和开发经历，不将产品技术对象当使用。',
'E0214':'供应链情报：供应商画像与采购策略报告是分析对象，不能宣称本人采购；任职采购寻源为列举经验。',
'E0181':'VOC全流程方法在要求段，修复误记职责的SOP；原源分行及斜杠关系保留。',
'N1004':'Atlas营销：营销或产品管理经验任选，另有明确发布活动能力；Photoshop是加分任选例示，补本人策略制定。',
'N0681':'仓储售前：Preferred段覆盖AutoCAD；WMS集成数据不等于使用WMS，错引职责的WMS要求重锚。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0590','O1','谈判能力位于职责段明确负责资源库商务管理。',metric='DUTY_OWN_USE')
ov('N0590','3:0','原只有标题，重锚实际搭建管理供应商资源库。',metric='DUTY_OWN_DEVELOP',quote='搭建并管理涵盖空间设计、搭建制作、活动执行的供应商资源库，具备强势的商务谈判与绩效管理能力，确保项目高质量、高效率交付。')
ov('N0590','6:0','标题重锚实际无须动手的品质指导，不是本人开发内容。',metric='SEPARATE',branch='MANAGED_CREATIVE_OBJECT',quote='无需亲自动手，但需具备极高的审美标准，精准指导内外部团队，确保所有交付物严格符合品牌VI，维持统一的科技专业调性。')
for e in ['9:0','9:1','9:2']:ov('N0590',e,'规划数字化过渡未明示本人实施/使用该平台。',metric='SEPARATE',branch='PLANNED_TOOL_OBJECT')
for e in ['14:1','18:0']:ov('N0590',e,'对供应商有审美说服或沟通能力，不是商务采购方法。',metric='SEPARATE',branch='GENERIC_VENDOR_COLLABORATION')
ov('N0590','13:0','营销流程或供应商体系任选。',branch='CHOICE')
ov('N0590','19:0','加分项CRM或营销自动化工具，目录对象为任选。',metric='PREFERRED',branch='CHOICE')
for e in ['19:1','19:2']:ov('N0590',e,'加分段等列举，无工具任选词。',metric='PREFERRED',branch='EXAMPLE')
for e in ['O14','O15']:ov('N0583',e,'所有平台选项均为仿真，上位经验无条件。',branch='UNCONDITIONAL')
ov('N0583','2:1','会使用rqt、rviz及各类日志工具是明确并列，不是例示。',branch='UNCONDITIONAL')
ov('N0568','5:0','CRM或相关系统是任选。',branch='CHOICE')
for e in ['7:0','7:1']:ov('N0568',e,'等系统例示，无or。',branch='EXAMPLE')
for e in ['14:0','14:1']:ov('N0568',e,'工作说明需持续关注，是职责段等列举。',metric='DUTY_OWN_USE',branch='EXAMPLE')
ov('N0568','11:0','面对升级情绪稳定是一般态度，不能记专业事件技能。',metric='SEPARATE',branch='GENERIC_WORK_ATTRIBUTE')
add('N0568','V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','维护日常售后沟通秩序，提升客户对售后响应效率与服务体验的感知','本人客户服务职责明确。')
add('N0568','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','按要求收集客户问题的关键信息，包括但不限于设备型号、序列号、软件版本、故障现象、复现步骤、图片、视频、日志等','本人故障信息收集工单流程，不能扩称独立深度排障。')
for e in ['1:0','2:0','4:0']:ov('N0545',e,'遥操作为技术咨询/预研对象，未明示本人操作机器人。',metric='SEPARATE',branch='TECHNICAL_SOLUTION_OBJECT')
ov('N0545','3:0','参与项目交付且列举环境部署等，没有本人遥操作动作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O17','O18']:ov('N0545',e,'VLA/VLM均属上位基础模型；在列举中作为例示，不沿用下位斜杠未知。',branch='EXAMPLE')
add('N0545','V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL','输出技术方案文档、演示方案与POC计划，支撑商务拓展与项目立项','售前技术方案与POC计划明确。')
for e in ['1:0','2:0','3:0']:ov('E0214',e,'供应链情报/采购模式分析与决策支持，不是本人商务采购执行。',metric='SEPARATE',branch='PROCUREMENT_ANALYSIS_OBJECT')
ov('E0214','4:0','协同采购研发计划部门，采购属协作对象。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0214','5:0','供应链分析、行业研究、采购寻源、市场情报等经验列举，非仅采购经历。',branch='EXAMPLE')
ov('E0181','1:0','能独立设计标准作业流程位于任职要求。',metric='GENERAL')
ov('N1004','3:0','marketing or product management明确备选经验。',branch='CHOICE')
ov('N1004','5:0','such as和or并存。',branch='CHOICE_AND_EXAMPLE')
add('N1004','V2_MARKETING','DUTY_OWN_DEVELOP','UNCONDITIONAL','Own the strategy and execution of Atlas announcements, developing go-to-market plans','本人制定营销方案明确。')
add('N1004','V2_MARKETING','GENERAL','UNCONDITIONAL','Demonstrated ability to execute high-level launches and campaigns','另有无条件活动发布能力。')
ov('N0681','O3','将客户WMS集成数据转成方案，未明确本人操作WMS。',metric='SEPARATE',branch='CUSTOMER_SYSTEM_INTERFACE_OBJECT')
ov('N0681','O7','旧误引职责，改Preferred内实际WMS/WCS语句，斜杠仍未解。',metric='PREFERRED',quote='Familiarity with WMS/WCS systems and integration requirements (API, EDI, SOAP/REST).')
ov('N0681','9:0','全部资格在Preferred Qualifications段。',metric='PREFERRED')
ov('N0681','O11','simulation or modeling tools是备选关系。',branch='CHOICE')
register(list(R.values()),'Astra_v3_boundary_commercial_b')
