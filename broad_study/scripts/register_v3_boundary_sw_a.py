from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0643':'实习应用开发的协助、参与与本人编写测试工具分开，任职串口为一般要求。',
'N0501':'机器人智能体应用工作流；职责、一般要求及加分项分别定位。',
'N0543':'软件集成主任务成立，ROS/ROS2斜线在一般及优先语境均未解。',
'N0684':'移动端应用使用React生态，不等于开发React框架；JS/TS未解。',
'E0018':'明确ROS2及DDS中间件开发，任职证据与职责分开，等字保留示例。',
'E0192':'端侧交付流水线；构建对象不等于独立ROS开发，跟踪技术不等于使用工具。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
for e in ['O2','O3']:ov('N0643',e,'Python/C++具体语言之间斜线未解。',branch='UNRESOLVED')
ov('N0643','O9','配合团队功能验证，另有本人编写测试工具。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0643','2:0','参与设备协议对接保留协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0643','6:0','了解串口是一般要求，只有上位机经验优先。',metric='GENERAL')
add('N0501','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'明确建设智能体记忆和任务执行框架。')
for e in ['O6','O7']:ov('N0543',e,'优先经验承接ROS/ROS2，斜线不能变成两者均必需。',branch='UNRESOLVED')
for e in ['1:0','4:0','7:0']:ov('N0684',e,'使用React技术构建应用，不是开发React框架本体。',metric='DUTY_OWN_USE')
ov('N0684','13:0','React与React Native同属冻结React类别。',branch='UNCONDITIONAL')
for e in ['O2','1:0']:ov('E0018',e,'具体核心模块列举以等结尾。',branch='EXAMPLE')
ov('E0018','O4','改引任职核心机制条款，原引用职责。',metric='GENERAL',branch='EXAMPLE',quote=ln('E0018',13))
ov('E0018','2:0','ROS2/DDS/Middleware本条不同类别斜线未解；其他明确DDS条款另存。',branch='UNRESOLVED')
for e in ['3:0','4:0','6:0']:ov('E0018',e,'具体模块/经验列举含等。',branch='EXAMPLE')
for e in ['O10','O11']:ov('E0192',e,'一般要求引用任职研发流程，原职责不能当资格要求。',metric='GENERAL',quote=ln('E0192',16))
ov('E0192','O14','推动自动化测试等实践未明设计测试方法，按使用。',metric='DUTY_OWN_USE',branch='EXAMPLE')
ov('E0192','4:0','跟踪前沿技术未明实际采用，保留技术关注。',metric='SEPARATE',branch='TECHNOLOGY_MONITORING')
add('E0192','TC_RELIABILITY','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'版本回滚方案、可靠发布机制明确本人建设管理。')
register(list(R.values()),'Astra_v3_boundary_sw_a')
