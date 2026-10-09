from astra_review_tools import *
JUD={
'E0388':'演示环境本人研发、运行、故障恢复和SOP；仿真工具duties为任选加例示，一般要求改引实际资格；没有将VIP产品演示推成营销技能。',
'N0943':'FAR实验室维护单列，不混整公司。补明确维护SOP和根因方法；协调厂商技术支持不当采购。',
'N0853':'生产现场应用支持含本人事件解决及校准；Python/Bash协作、SQL/NoSQL与云工具斜杠关系未解；GitHub Actions不自动等Git。',
'N0905':'履约设施维护而非机器人模型，inventory明确help关系；GoogleSuite为必须且举例，SOP及安全操作按职责和要求分开。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','O2','O3']:ov('E0388',e,'such as与or明确例示和任选。',branch='CHOICE_AND_EXAMPLE')
for e in ['O9','O10','O11','O19']:ov('E0388',e,'原错引职责段，重锚一般要求中仿真工具经验。',metric='GENERAL',quote='Extensive experience using robotics simulation tools (NVIDIA Isaac Sim, Gazebo, MuJoCo, or equivalent) to design, validate, and optimize robot behaviors and reduce integration risk prior to live deployment.')
ov('E0388','11:0','Skills and Requirements段的能力要求，非当前工作职责。',metric='GENERAL')
add('E0388','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Build and maintain comprehensive runbooks, SOPs, checklists, and software tools that enable trained colleagues and partners to execute standard demonstrations consistently and independently.','明确SOP本人编制。')
for e in ['O4','O6','O8','2:0']:ov('N0943',e,'括号组件或including列举，明确具体对象例示。',branch='EXAMPLE')
ov('N0943','8:0','培训句不等本人现场排障执行，重锚明确维修控制系统。',metric='DUTY_OWN_USE',quote='Troubleshoot and repair control systems including PLCs, motor controllers, embedded electronics, and sensor arrays; read and interpret electrical, mechanical, and pneumatic schematics')
add('N0943','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Develop and execute preventive and corrective maintenance processes, SOPs, and maintenance plans for robotic systems','明确开发维护SOP。')
add('N0943','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','Develop and implement failure-tracking systems to capture robotic failures, identify trends, perform root-cause analysis, and proactively reduce recurring issues','明确根因分析方法。')
ov('N0853','O1','SQL/NoSQL二者关系未明确，不能强判SQL确定使用。',branch='UNRESOLVED')
for e in ['O2','O16','14:0']:ov('N0853',e,'contribute to CLI tools and diagnostic scripts，协作贡献不能直接记本人独立开发或语言使用职责。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['4:0','4:1','4:2','26:0','26:1','26:2']:ov('N0853',e,'平台清单为such as或括号例示，无or。',branch='EXAMPLE')
for e in ['10:0','10:1','17:0','17:1','17:2']:ov('N0853',e,'斜杠未明示并用还是任选，保留关系未知。',branch='UNRESOLVED')
ov('N0853','17:3','networking括号协议列举。',branch='EXAMPLE')
ov('N0853','31:0','must be willing and able明确硬性校准能力要求。',metric='REQUIRED')
ov('N0853','33:0','原词只有GitHub Actions，不能补Git工具。',metric='SEPARATE',branch='SUBSTRING_FALSE_POSITIVE')
ov('N0853','33:1','括号例示两款工具，无or。',branch='EXAMPLE')
add('N0853','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Own Tier 2 application and software incidents—meet or beat targets for First Response, Containment, and Permanent Fix.','本人明确生产事件处理。')
ov('N0905','O1','Help to maintain和Working with管理团队。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0905','2:0','Must且including but not limited to。',metric='REQUIRED',branch='EXAMPLE')
add('N0905','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Effect repairs on machines, tools, building infrastructure, and other grounds equipment and resources.','明确日常设施运行维修。')
add('N0905','V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Follow appropriate safety procedures and work to applicable codes and guidelines, including making recommendations for improvements.','明确执行作业安全规程。')
add('N0905','V2_SOP_OPERATION','GENERAL','EXAMPLE','Read and interpret documents such as safety rules, operating and maintenance instructions, and procedure manuals. Write reports, correspondence and procedures.','一般要求包括规程阅读与编写，文档类型例示。')
register(list(R.values()),'Astra_v3_deploy_c')
