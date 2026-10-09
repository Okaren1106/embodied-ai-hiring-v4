from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0146':'力控操作：遥操作与力控为加分任选，非无条件。',
'N0139':'WBC/MPC：主导或参与的职责承担关系未知；仿真工具是例示，求解器至少一种并举例。',
'N0055':'规控实习：明确负责具体模块支持本人职责；各控制方法同上位，部分工具为例示，协作标定单列。',
'N0129':'电机开发：驱动电路优化为配合硬件；FOC/无感方法关系未明，明确PID调参单独保留。',
'N0043':'规划实习：参与研究/开发不作本人独立承担；语言和ROS边界保留。',
'N0164':'操作算法：参与研发分开，本人测试保留；加分仿真上位无条件，Sapien与其余工具同为举例。',
'N0077':'交互算法：工具斜杠关系保留未知；加分经验与论文任选，仿真上位不被具体工具斜杠污染。',
'N0063':'重定向：参与动作模型开发分开；仿真或控制约束任选；动捕/仿真数据为来源例示，非自动独立开发该系统。',
'N0142':'双臂规控：RL/IL职责斜杠未知；OMPL为至少一种且如举例。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('N0146','4:0','力控或遥操作者优先。',branch='CHOICE')
for e in ['O1','O2','O3']:ov('N0139',e,'MuJoCo/Isaac/Gazebo等环境为例示。',branch='EXAMPLE')
for e in ['O14','O15','1:0']:ov('N0139',e,'主导或参与，无法明确所有广告都独立承担。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP','DUTY_OWN_DEVELOP_CHOICE'])
for e in ['10:0','10:1']:ov('N0139',e,'至少一种且如。',branch='CHOICE_AND_EXAMPLE')
for e in ['O1','O2']:ov('N0055',e,'括号列举仿真环境。',branch='EXAMPLE')
for e in ['O18','O19','O20','O21','O22','O23','O24','O25','O26','O27','O28','O32']:ov('N0055',e,'具体方法/软件任选均属相同上位；上位要求明确。',branch='UNCONDITIONAL')
ov('N0055','2:0','配合硬件团队完成标定，未明确本人独立承担。',metric='SEPARATE',branch='COLLABORATION')
for e in ['10:0','10:1','10:2']:ov('N0055',e,'Git/CMake/GDB等常用工具是列举。',branch='EXAMPLE')
ov('N0129','O4','配合硬件优化驱动电路，非本人独立开发电力电子。',metric='SEPARATE',branch='COLLABORATION')
ov('N0129','1:0','FOC/无感算法斜杠关系未明。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP','DUTY_OWN_DEVELOP_CHOICE'])
ov('N0129','8:0','电机控制理论后括号方法列举。',branch='EXAMPLE')
for e in ['O6','O7']:ov('N0043',e,'职责明确为参与设计开发。',metric='SEPARATE',branch='PARTICIPATION')
for e in ['O11','O12','O13']:ov('N0164',e,'参与研发不能记为本人独立承担。',metric='SEPARATE',branch='PARTICIPATION')
for e in ['O20','O21','O22','O23','O24','O25']:ov('N0164',e,'具体仿真产品举例，上位仿真经验是明确加分要求。',branch='UNCONDITIONAL')
ov('N0164','2:0','Sapien与其他仿真产品同在等举例中，无任选词。',branch='EXAMPLE')
for e in ['O1','O2']:ov('N0077',e,'IsaacSim/MuJoCo斜杠不明确，不从等推断任选或兼具。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_USE_CHOICE','DUTY_OWN_USE_EXAMPLE','DUTY_OWN_USE_CHOICE_AND_EXAMPLE'])
for e in ['O18','O19']:ov('N0077',e,'两产品均仿真；外层经验或论文为任选。',branch='CHOICE')
for e in ['5:0','5:1','5:2']:ov('N0077',e,'Unity/Unreal/Blender/PyTorch3D仅斜杠，缺少明确任选词。',branch='UNRESOLVED')
ov('N0077','10:0','迁移经验与论文发表or。',branch='CHOICE')
for e in ['O5','O6']:ov('N0063',e,'NumPy/PyTorch斜杠，等不解决相互关系。',branch='UNRESOLVED')
ov('N0063','O10','明确参与动作生成模型开发。',metric='SEPARATE',branch='PARTICIPATION')
for e in ['O11','O12']:ov('N0063',e,'物理仿真或控制约束为明确任选。',branch='CHOICE')
for e in ['O22','O23']:ov('N0063',e,'上位仿真或动画工具链任选，不是仿真上位本身被例示。',branch='CHOICE')
for e in ['4:0','4:1']:ov('N0063',e,'至少一种且如列举。',branch='CHOICE_AND_EXAMPLE')
ov('N0063','O9','多源动作数据包括仿真数据等，是来源例示。',branch='EXAMPLE')
ov('N0063','1:0','使用动捕数据是多源数据列举中的一种。',branch='EXAMPLE')
for e in ['O10','O11']:ov('N0142',e,'强化/模仿学习之间斜杠未解。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP','DUTY_OWN_DEVELOP_CHOICE'])
ov('N0142','5:0','至少一种且如OMPL等。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_control_b')
