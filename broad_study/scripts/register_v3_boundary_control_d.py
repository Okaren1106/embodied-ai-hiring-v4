from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0346':'轮式WBC：仿真器斜杠未知；动力学库至少一种且等，OSQP/Ipopt如举例。',
'N0329':'规控：Gbzeao疑似Gazebo但不擅自确证；本人仿真环境开发与协作标定分开。',
'N0324':'同任务另一独立广告：本人仿真开发与协作标定同口径，语言/ROS未知保留。',
'N0352':'力反馈振动控制：职责标定明确，语言C/C++未解，Python/Matlab例示及ML加分语境成立。',
'E0295':'运动控制：一般控制要求重定位，补明确QP-WBC加分；旧语言未知保留。',
'E0276':'关节电机：C语言/matlab斜杠仍未解，不能只因写全C语言便作明确要求；补本人系统辨识方法。',
'E0274':'导航：C、C++明确分列，不是C未知；经典控制与路径类方法任选，修正门槛语境。',
'E0183':'嵌入式控制：Ubuntu可支持Linux一般要求；URDF为如举例，EKF/UKF同状态估计方法上位。',
'E0143':'力反馈：遥操要求的年份、系统经验与加分场景有任选；错引职责的资格证据重定位。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why,**f):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**f))
for e in ['O1','O2']:ov('N0346',e,'MuJoCo/IsaacSim斜杠未解。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_USE_CHOICE','DUTY_OWN_USE_EXAMPLE','DUTY_OWN_USE_CHOICE_AND_EXAMPLE'])
for e in ['O5','O6']:ov('N0346',e,'等至少一种，例示和任选同时存在。',branch='CHOICE_AND_EXAMPLE')
for e in ['4:0','4:1']:ov('N0346',e,'如OSQP/Ipopt无任选词。',branch='EXAMPLE')
for r,e in [('N0329','O15'),('N0324','O16')]:ov(r,e,'负责搭建仿真环境是开发。',metric='DUTY_OWN_DEVELOP')
for r in ['N0329','N0324']:ov(r,'2:0','与其他团队紧密协作完成标定。',metric='SEPARATE',branch='COLLABORATION')
add('N0329','SK_GAZEBO','UNKNOWN','UNRESOLVED','Gbzeao','疑似Gazebo拼写，原词无法直接确证，保留条目未知而非目录外即零。',affected_metrics=['GENERAL_EXAMPLE'])
ov('E0295','O15','旧引用职责；重定位明确资格。',metric='GENERAL',quote='3、控制算法：熟悉传统控制（PID、LQR、阻抗控制、反馈线性化等）、最优控制（MPC、iLQR、DDP 等）、操作空间控制（OSC，WBC），有 QP-based WBC 经验者优先；')
add('E0295','V2_CLASSICAL_CONTROL','PREFERRED','UNCONDITIONAL','有 QP-based WBC 经验者优先','明确QP-based WBC加分与一般控制知识分开。')
ov('E0276','1:0','C语言/matlab之间斜杠未解。',branch='UNRESOLVED')
ov('E0276','O17','原误引职责，重定位关节电机开发加分经验。',metric='PREFERRED',quote='9、有人型机器人关节电机控制算法开发经验优先。')
ov('E0276','2:0','如FOC等是经典方法例示。',branch='EXAMPLE')
add('E0276','V2_SYSID','DUTY_OWN_DEVELOP','UNCONDITIONAL','开发实现电机在线、离线参数辨识算法','本人开发参数辨识算法。')
add('E0276','V2_SYSID','GENERAL','UNCONDITIONAL','熟悉常用的电机参数辨识方法','一般辨识方法明确。')
ov('E0274','3:0','C与C++逗号分列，等语言为例示；不存在斜杠歧义。',branch='EXAMPLE')
ov('E0274','4:0','至少1至2种跨路径规划/经典控制方法，不能保证特定经典控制类。',branch='CHOICE_AND_EXAMPLE')
add('E0183','SK_LINUX','GENERAL','UNCONDITIONAL','精通Ubuntu','明确Linux发行版语境。')
ov('E0183','5:0','如URDF等为例示。',branch='EXAMPLE')
q='4、熟悉机器人运动学、动力学、雅可比矩阵、奇异点分析与冗余度控制。熟悉阻抗/导纳控制、双边遥操作、力反射、接触控制、虚拟环境或虚拟墙等相关方法。'
for e in ['O22','O25']:ov('E0143',e,'旧误引职责，改同一条明确任职方法列表。',metric='GENERAL',quote=q)
for e in ['1:0','2:0','5:0']:ov('E0143',e,'遥操作是若干经验领域/系统/应用场景之一。',branch='CHOICE')
ov('E0143','3:0','方法列表或且等。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_control_d')
