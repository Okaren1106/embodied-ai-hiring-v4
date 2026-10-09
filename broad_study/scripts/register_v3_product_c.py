from astra_review_tools import *
JUD={
'E0216':'云平台产品架构与标准/定制边界，ROS/ROS2要求保留未解；大模型优先原引职责错位，修回实际加分要求。',
'E0213':'PMO流程与风险机制明确本人开发，泛工具不补Jira；管理绩效不等机器人测试技术。',
'E0179':'数据交付项目，管理数据需求与质量不等独立开发数据管线；明确计划风险与协作工具、Agent斜杠待解。',
'E0321':'Principal TPM，职责有里程碑和依赖权衡，上位项目方法非Microsoft Project工具；研发经历是资格而非据职位推工具。',
'E0412':'仿真产品经理，技术要求须来自技能段，原仿真一般与感知优先误引职责；用户研究和产品营销协作区分。',
'N0974':'业务运营项目包含制造及企业系统实施，细任务保留BIZOPS；ERP/MRP/MES职责为支持，不能当本人系统开发或错记优先。',
'N0864':'零售3PL产品与商业化，测试和客户验收本人主责；商业/营销独立动作重锚具体职责，不只引用协作部门。',
'N0856':'航空硬件交付客户成功，原文否定传统SaaS岗位不可当正例；服务关系另有明确职责，安全合规支持与项目风险跟踪分开。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0216','O10','旧仅大模型定位在协作职责；改实际加分资格句。',metric='PREFERRED',branch='UNRESOLVED',quote='对传感器数据格式及大模型/具身智能的数据需求有基本认知')
add('E0216','V2_REQUIREMENTS_ENGINEERING','DUTY_OWN_DEVELOP','UNCONDITIONAL','主导划分平台标准底座与业务定制层的系统边界','明确系统接口和架构边界设计。')
add('E0213','V2_PROJECT_METHOD','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立项目准入准出机制、变更管理机制、风险预警机制，确保项目执行的规范性与可控性','明确范围变更和风险机制开发。')
ov('E0179','O1','组织需求评审和定义交付标准，不足以支持本人开发数据生产管线。',metric='SEPARATE',branch='PRODUCT_MANAGEMENT_OBJECT')
ov('E0179','2:0','等效率工具为例示。',branch='EXAMPLE')
for e in ['2:1','2:2','4:0']:ov('E0179',e,'斜杠未给定并用或任选，保留未知关系。',branch='UNRESOLVED')
ov('E0179','3:0','供应商管理、外包、基地或团队协作明确任选。',branch='CHOICE')
add('E0179','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','负责具身智能数据交付项目的全流程项目管理，包括项目计划、里程碑、风险、问题闭环和项目复盘','明确计划里程碑风险方法。')
add('E0179','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','具备较强的项目推进能力，能够管理计划、风险、资源冲突和跨团队协作','明确一般方法能力。')
add('E0321','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Continuous improvement  and utilization of project reporting KPIs, OKRs and milestones.','明确里程碑和管理指标使用。')
ov('E0412','O8','原引职责不能当一般要求；真实资格句列出仿真和其他工具任选。',metric='GENERAL',quote='Demonstrated experience in developing or managing simulation environments, simulation-in-the-loop testing frameworks, or developer tools.')
ov('E0412','O14','原感知优先错引职责，改Nice to Have生成感知用合成数据句。',metric='PREFERRED',quote='Experience generating synthetic data for perception, autonomy, and navigation stacks.')
for e in ['O1','10:0','10:1']:ov('N0974',e,'Support implementations属于协作对象，该引用不是优先要求。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for c in ['V2_MES','V2_MRP']:add('N0974',c,'PREFERRED','UNRESOLVED','ERP/MRP/MES implementations.','独立plus段有实际系统经验，但斜杠内部未解。')
for e in ['20:0','20:1']:ov('N0974',e,'Atlassian suite括号列举Confluence/Jira，无or。',branch='EXAMPLE')
add('N0974','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Manage scope, schedule, budget, resources, dependencies, risks, and deliverables.','本人明确项目范围与依赖风险管理。')
add('N0974','V2_PROCUREMENT','PREFERRED','CHOICE','Vendor/supplier vetting and management.','one or more of following列表，供应商尽调管理任选。')
ov('N0864','2:0','重锚本人客户关系经营责任，不只一般商业领导段。',metric='DUTY_OWN_USE',quote='Own the product relationship for developer-interface engagements and turn bespoke integrator delivery into a repeatable model')
ov('N0864','2:1','重锚市场细分与GTM投资方法。',metric='DUTY_OWN_USE',quote='Segment markets by customer, workflow, need, buying readiness, economics, and product fit to focus product and GTM investment')
add('N0864','V2_MARKETING','REQUIRED','UNCONDITIONAL','Outbound product management success in segmentation, customer and prospect discovery, prioritization, and evidence-based growth roadmaps','Required段明确市场方法。')
ov('N0856','3:0','本句明确不是传统SaaS客户成功岗位，不可抽作正例。',metric='SEPARATE',branch='NEGATED_CONTEXT')
ov('N0856','O2','Support alignment，协助符合航空安全规范。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0856','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Track dependencies, risks, and action items and escalate issues as needed','明确本人依赖与风险追踪。')
register(list(R.values()),'Astra_v3_product_c')
