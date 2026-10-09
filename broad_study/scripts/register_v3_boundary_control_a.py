from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0652':'实习电机控制：参与FOC不作本人独立开发；电机研究或开发同控制上位；RTOS括号例示。',
'E0050':'轮式RL：本人RL与协同传统控制融合分开；语言/框架斜杠未知保留。',
'E0294':'控制系统：一般规划要求定位要求句；CANopen/EtherCAT并列明确，安全参与与本人测试分开。',
'E0006':'机械臂：ROS1/2未知；通讯方式如且至少一种为举例加任选。',
'N0356':'双臂规控：本人搭建仿真环境，协作标定不当独立承担；双语言及ROS版本未知保留。',
'N0624':'全身运控：工具链括号例示；全身控制或QP/MPC同经典控制上位，加分语境修正。',
'N0476':'FOC电机：职责FOC/无感估算关系未明，具体经典控制方法不强判无条件；一般FOC明确。',
'N0648':'运控实习：迁移仿真协作与独立仿真使用分开；控制方法保持上位。',
'N0167':'全身规划：编程语言斜杠关系未解；至少一种仿真软件为任选加例示，上位仿真知识明确。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O2','O3','1:0']:ov('N0652',e,'明确参与算法开发，未作本人独立承担。',metric='SEPARATE',branch='PARTICIPATION')
ov('N0652','O6','参与伺服软件框架，不等于电力电子设计或使用。',metric='SEPARATE',branch='SOFTWARE_FOR_DRIVER')
for e in ['O7','O9']:ov('N0652',e,'电机控制开发或研究方向均属控制上位。',branch='UNCONDITIONAL')
for e in ['16:0','16:1']:ov('N0652',e,'括号RTOS产品列举没有任选词。',branch='EXAMPLE')
ov('E0050','1:0','协同完成RL与WBC/MPC融合，未独立承担传统控制。',metric='SEPARATE',branch='COLLABORATION')
ov('E0294','O10','安全开发是参与；本人主导的安全性性能测试可支持使用。',metric='DUTY_OWN_USE',quote='6.主导系统联调与性能测试，聚焦抖动、实时性、安全性、精度、响应特性，以及为控制落地服务的动力学辨识与动力学参数标定/验证，制定调优策略；')
ov('E0294','O14','重定位要求句，避免职责当资格。',metric='GENERAL',quote='4.熟悉 ROS 2 开发及底层通信机制，熟练使用 ros2_control；具备离线规划能力；')
for e in ['4:0','4:1']:ov('E0294',e,'如SOEM/IgH只修饰主站实现；EtherCAT与CANopen本身明确并列。',branch='UNCONDITIONAL')
for e in ['O4','O5','1:0','5:0','5:1','5:2']:ov('E0006',e,'如且至少一种，应同时记录例示与任选。',branch='CHOICE_AND_EXAMPLE')
ov('N0356','O16','负责仿真环境搭建是开发。',metric='DUTY_OWN_DEVELOP')
ov('N0356','2:0','与其他团队紧密协作完成标定，未明确独立承担。',metric='SEPARATE',branch='COLLABORATION')
for e in ['O4','O5','O6','O13']:ov('N0624',e,'工具链括号列举为例示。',branch='EXAMPLE')
for e in ['O14','O15']:ov('N0624',e,'两种选项均是控制，控制上位无条件。',branch='UNCONDITIONAL')
ov('N0624','5:0','加分项；QP/MPC或WBC均属目录经典控制上位。',metric='PREFERRED',branch='UNCONDITIONAL')
ov('N0624','O9','与团队合作迁移，并未明确独立承担仿真操作。',metric='SEPARATE',branch='COLLABORATIVE_TRANSFER')
ov('N0476','1:0','FOC与无感估算斜杠关系未明，具体方法分支未知。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP','DUTY_OWN_DEVELOP_CHOICE'])
ov('N0648','O7','与团队合作迁移，不自动推定本人独立仿真使用。',metric='SEPARATE',branch='COLLABORATIVE_TRANSFER')
for e in ['O1','O2']:ov('N0167',e,'C/C++/Python斜杠关系不明确，等不解决语言之间关系。',branch='UNRESOLVED')
ov('N0167','O3','掌握编程语言上位明确，不是仅例示。',branch='UNCONDITIONAL')
for e in ['O4','O5']:ov('N0167',e,'至少一种且如/等举例。',branch='CHOICE_AND_EXAMPLE')
for e in ['O10','O11']:ov('N0167',e,'任选具体软件不削弱机器人运动控制仿真这一上位要求。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_control_a')
