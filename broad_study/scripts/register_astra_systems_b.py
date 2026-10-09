from astra_review_tools import *
ids=['N0933','E0592','N0988','E0534','E0317']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why,**v):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**v))
R['N0933']['judgment']='物理AI架构包含端到端设计与扩散策略应用；策略路线图不自动等于控制算法研发。明确optimal control上位要求保留，未说明列表关系的括号内具体方法保留未知，不推所有细项必需。'
ov('N0933','N0933:O8','应用策略到操作任务，原句没有本人研发操作算法。',metric='DUTY_OWN_USE')
ov('N0933','N0933:2:0','定义方法如何组合的技术路线图是架构应用，未明示研发控制方法本体。',metric='DUTY_OWN_USE')
for eid in ['N0933:O18','N0933:O19','N0933:O20','N0933:3:1']:
 ov('N0933',eid,'具体子方法括号列举未说明全部、例示或任选，上位optimal control明确要求另保留。',branch='UNRESOLVED')
R['E0592']['judgment']='机器人平台集成明确包含实际舰队健康维护、测试执行与验收方案，不把mobile manipulator这一机器人类型自动当作操作算法要求。修复including分支并补测试执行和标准程序。'
ov('E0592','E0592:O6','负责跨机械/电气/软件接口的集成问题闭环，不等于研发机械本体。',metric='DUTY_OWN_USE')
for eid in ['E0592:O9','E0592:O11']:ov('E0592',eid,'including引出细项，按示例分支。',branch='EXAMPLE')
ov('E0592','E0592:O14','移动操作机器人或其他多自由度系统是集成对象类型，不足以推出操作算法技能。',metric='SEPARATE',branch='INTEGRATION_OBJECT')
add('E0592','TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL','Drive and execute fleet acceptance testing','本人明确执行验收测试。')
add('E0592','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','bring-up procedures','本人创建启动程序与故障指南；上下文完整源文支持。')
R['N0988']['judgment']='区分本人需求拆解/追溯工作、辅助设定性能目标和Desired项目。Jama配置属于使用；Desired中多个新项误落GENERAL并已纠正。参数图本身是可靠性方法，不直接替代需求工程。'
ov('N0988','N0988:O1','facilitate包括DFMEA的工程活动，属于组织应用的例示，无研发FMEA方法。',branch='EXAMPLE')
ov('N0988','N0988:O8','验证规划处在同一个活动例示清单。',branch='EXAMPLE')
ov('N0988','N0988:1:0','配置和定制现有Jama工具，不是开发Jama工具本体。',metric='DUTY_OWN_USE')
ov('N0988','N0988:5:0','参数图列在可靠性方法下，不能仅由名称推出需求工程。',metric='SEPARATE',branch='RELIABILITY_METHOD_OBJECT')
ov('N0988','N0988:5:1','位于Desired experience；including引出RCA等。',metric='PREFERRED',branch='EXAMPLE')
for eid in ['N0988:7:0','N0988:7:1','N0988:7:2','N0988:7:3']:
 ov('N0988',eid,'Desired下的软件工具由including引出，原GENERAL/CHOICE不符。',metric='PREFERRED',branch='EXAMPLE')
for eid in ['N0988:12:0','N0988:12:1']:ov('N0988',eid,'电气标准与EMI相关知识处于Desired。',metric='PREFERRED')
add('N0988','V2_REQUIREMENTS_ENGINEERING','DUTY_OWN_USE','UNCONDITIONAL','derive system requirements that guide the development of compute and sensing systems','本人在联合团队中拆解系统需求。')
add('N0988','V2_REQUIREMENTS_ENGINEERING','PREFERRED','UNCONDITIONAL','Authoring, reviewing, and approving a wide variety of requirements','Desired明确要求需求编审经验。')
R['E0534']['judgment']='实习岗位是电力系统集成和调试；示波器等是such as示例。跨热/控制接口协作不直接等于本人开发这些子系统。补明确根因分析方法，开发调试不推在役事故支持。'
for eid in ['E0534:O1','E0534:O2']:ov('E0534',eid,'such as引出仪表例示。',branch='EXAMPLE')
for eid in ['E0534:O5','E0534:O7']:ov('E0534',eid,'集成性能测试/嵌入式调试属于该技术使用，未写开发该子系统本体。',metric='DUTY_OWN_USE')
for eid in ['E0534:O8','E0534:O9']:ov('E0534',eid,'桥接热/控制团队接口是工作对象，不足以定本人开发这些子系统。',metric='SEPARATE',branch='INTERFACE_OBJECT')
add('E0534','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','document root causes','本人排查集成问题、分析日志并记录根因。')
R['E0317']['judgment']='诊断经理负责技术调查和根因分析；工程问题是否已部署运行未指明，不把所有排障算在役维护。一般控制/可靠性任选要求要定位到Experience而非职责或协作句；补明确RCA开发/使用/经验。'
for eid in ['E0317:O6','E0317:O7']:
 ov('E0317',eid,'原定位协作或职责；一般经验任选清单在Experience。',metric='GENERAL',branch='CHOICE',quote='8+ years of experience in systems engineering, diagnostics, integration, test, reliability, software, controls, or related engineering disciplines supporting complex electromechanical systems.')
for eid in ['E0317:1:0','E0317:2:0','E0317:3:0']:
 ov('E0317',eid,'工程故障调查横跨开发/制造/集成，缺少明确在役运行边界。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
add('E0317','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','Drive issue triage, fault isolation, root cause analysis, and ownership attribution.','明确本人领导根因分析执行。')
add('E0317','V2_RCA','GENERAL','UNCONDITIONAL','Strong expertise in system-level debugging, root cause analysis, fault isolation, and technical investigations','明确普通能力要求。')
register(list(R.values()),'Astra_systems_fullread_b')
