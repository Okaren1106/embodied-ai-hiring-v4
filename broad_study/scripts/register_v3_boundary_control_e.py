from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0378':'灵巧手负责人：Python硬性要求原错误引用职责，重定位跨行原句；学习方法职责任选与遥操作加分分开。',
'E0379':'灵巧手负责人另一广告：相同职责资格按同义规则裁决，保留独立身份。',
'E0342':'Agility导航：仿真工具例示、RL协作、一般实时与加分MPC/状态估计分别定位。',
'E0439':'人形控制：跨栈示例不作无条件RL；控制与RL的上位分开，安全标准为加分任选例示。',
'E0440':'人形控制另一独立广告：同义语境一致处理，未因报酬段差异合并广告。',
'N0771':'人形操作：岗位交叉领域背景不等于明确遥操使用；支持遥操单列，操作经验必须实机只硬化实机条件。',
'N0800':'规划控制：使用基础模型驱动移动不等于开发基础模型；推理工具在加分栏，ONNX Runtime不等于格式。',
'N0804':'联邦规划控制：已回读全部缩略边界句；库举例与ROS斜杠、控制优化加分任选保留。',
'N0934':'规划负责人：本人算法生产化属于方法开发；CI明确语境但testing/CI分支未知，避免目录外即零。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why,**f):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**f))
for r in ['E0378','E0379']:
 for e in ['O1','O2']:ov(r,e,'C++/Python职责斜杠未解，硬性Python只作用于任职要求。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_USE_CHOICE'])
 ov(r,'O3','Must-Have中跨行Proficiency in Python，不引用职责代码段。',metric='REQUIRED',quote='Proficiency in\nPython\n, with experience building real-time robotic software stacks.')
 for e in ['O10','O11','1:0']:ov(r,e,'Whether ... or明确方法任选。',branch='CHOICE')
 for e in ['O20','O21']:ov(r,e,'flow与diffusion均生成策略，e.g.为例示，上位不因斜杠未知。',branch='EXAMPLE')
 ov(r,'O22','原误引职责，改Must-Have中实际RL例示。',metric='REQUIRED',branch='EXAMPLE',quote='Proficiency in learning-based control for robotics (e.g. flow/diffusion-based visiomotor policies, reinforcement learning, reward modeling, etc.).')
 ov(r,'5:0','Teleoperation标题在Good to Have内。',metric='PREFERRED',quote='Experience with VR/haptic interfaces and retargeting algorithms for human-in-the-loop control.')
 ov(r,'6:0','校准在Good to Have，不是一般要求。',metric='PREFERRED')
for e in ['O1','O2','O3']:ov('E0342',e,'e.g.模拟环境例示。',branch='EXAMPLE')
ov('E0342','O14','与AI/控制团队协作集成RL。',metric='SEPARATE',branch='COLLABORATION')
ov('E0342','O17','原误引职责，改一般要求的实时导航经历。',metric='GENERAL',quote='5+ years of professional experience in robotics, specifically developing and deploying real-time navigation and motion planning systems for autonomous mobile platforms (humanoids, quadrupeds, autonomous vehicles).')
ov('E0342','O24','MPC或类似优化控制均控制上位。',branch='UNCONDITIONAL')
ov('E0342','O27','原误引职责，改实际加分多机器人路径协调经验；上位均规划。',metric='PREFERRED',branch='UNCONDITIONAL',quote='Experience with multi-robot coordination/route planning and abiding by boundary constraints in a workcell map.')
ov('E0342','4:0','明确Bonus；MPC或类似优化控制同目录上位。',metric='PREFERRED')
ov('E0342','5:0','Bonus下e.g.EKF/粒子滤波。',metric='PREFERRED',branch='EXAMPLE')
for r in ['E0439','E0440']:
 ov(r,'O7','e.g.列最高影响问题，RL是例示。',branch='EXAMPLE')
 ov(r,'O8','重定位明确从仿真到硬件的本人方法迁移。',metric='DUTY_OWN_USE',quote='Translate state-of-the-art model-based and learning-based methods into robust capability, from simulation through hardware bring-up and deployment.')
 ov(r,'O14','learning control或robotics RL均是控制应用上位。',branch='UNCONDITIONAL')
 ov(r,'O19','原误引职责，改真实任职要求。',metric='GENERAL',quote='Strong software engineering: real-time C++ and Python for robotic systems.')
 ov(r,'O24','安全关键或列明安全认证均是安全上位，外层加分四方向or。',branch='CHOICE')
 ov(r,'2:0','e.g.跨栈问题例示含遥操。',branch='EXAMPLE')
 ov(r,'7:0','加分场景任选且括号列标准。',branch='CHOICE_AND_EXAMPLE')
ov('N0771','1:0','岗位位于多个领域交叉处，非明确本人使用遥操。',metric='SEPARATE',branch='ROLE_INTERSECTION')
ov('N0771','2:0','明确Support遥操工作流，非本人独立承担。',metric='SEPARATE',branch='SUPPORT')
ov('N0800','O18','开发的是基础模型驱动的移动能力，未写开发基础模型本身。',metric='DUTY_OWN_USE')
for e in ['O27','O28']:ov('N0800',e,'列举学习导航方法均属学习导航上位，要求本身明确。',branch='UNCONDITIONAL')
for e in ['1:0','1:1']:ov('N0800',e,'such as为具体方法例示。',branch='EXAMPLE')
for e in ['4:0','4:2']:ov('N0800',e,'The Extras内实时推理工具，非General。',metric='PREFERRED')
ov('N0800','4:1','ONNX Runtime未明确ONNX格式。',metric='SEPARATE',branch='RUNTIME_NOT_FORMAT')
ov('N0934','2:0','本人攻克算法问题并转为生产系统，明确开发。',metric='DUTY_OWN_DEVELOP')
add('N0934','V2_CI_CD','UNKNOWN','UNRESOLVED','experience architecting testing/CI and benchmarking for robotics','CI在机器人测试流程明确，testing/CI是否任选未明确。',affected_metrics=['GENERAL','GENERAL_CHOICE'])
register(list(R.values()),'Astra_v3_boundary_control_e')
