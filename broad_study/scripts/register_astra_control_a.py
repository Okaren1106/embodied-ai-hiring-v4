from astra_review_tools import *
ids=['N0441','N0495','N0045','E0097','N0623','N0003','N0044','N0591','E0003','E0004','E0102','E0090','E0236']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why,**v):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**v))
R['N0441']['judgment']='本人力控开发明确。仿真器如且一种多种同时构成示例任选；语言裸括号关系不明。补系统辨识职责，控制/轨迹等细项按等例示；既有控制上位要求保留。'
for e in ['N0441:O1','N0441:O3','N0441:O4']:ov('N0441',e,'裸括号工具列举未说明关系。',branch='UNRESOLVED')
for e in ['N0441:O5','N0441:O6','N0441:O7','N0441:2:1']:ov('N0441',e,'如+一种或多种，两个关系同时存在。',branch='CHOICE_AND_EXAMPLE')
for e in ['N0441:O14','N0441:O15']:ov('N0441',e,'具体方法清单等等引出例示；上位控制要求另保留。',branch='EXAMPLE')
add('N0441','V2_SYSID','DUTY_OWN_USE','UNCONDITIONAL','动力学建模、辨识、仿真','明确本人建模辨识；没有据此推研发辨识工具。')
R['N0495']['judgment']='感控融合步态主体、RL/IL知识与视觉优先明确；Isaaclab为等主流仿真器示例，不应写成无条件指定品牌。'
ov('N0495','N0495:O6','Isaaclab等主流仿真器为示例。',branch='EXAMPLE')
R['N0045']['judgment']='协助参与移动操作和协助测试不充分支持独立本人交付；保留算法自主研究上位描述，不将实习协作硬化。IL/RL任选与ROS2/PyTorch示例要求有据。'
for e in ['N0045:O3','N0045:O4','N0045:O5']:ov('N0045',e,'明确协助参与/协助测试，未明确本人交付边界。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
R['E0097']['judgment']='短正文含完整职责，运动控制研发、测试程序研发和辅助机械建议边界明确。补本人执行算法测试；未展示要求不推不存在要求。'
add('E0097','TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL','运动控制算法的开发、调试和测试','测试算法本人执行，另有测试程序开发。')
R['N0623']['judgment']='导航规划、行为树及异常恢复是算法对象；代价地图不自动属于定位建图。等算法族保留上位方法正例，具体Nav2与传统控制方法的斜线关系未知。'
for e in ['N0623:O9','N0623:O16']:ov('N0623',e,'costmap/导航全链路未说明定位或建图算法，不当SLAM。',metric='SEPARATE',branch='NAVIGATION_OBJECT')
for e in ['N0623:O21','N0623:O22']:ov('N0623',e,'具体建图系统等例示；另补上位SLAM一般要求。',branch='EXAMPLE')
ov('N0623','N0623:2:0','MPC/MPPI与其它局部规划方法的斜线替代关系未定。',branch='UNRESOLVED')
ov('N0623','N0623:3:0','Nav2 / Move Base括号斜线关系未解。',branch='UNRESOLVED')
add('N0623','TC_SLAM','GENERAL','UNCONDITIONAL','SLAM 建图','上位建图知识明确；具体软件例示另记。')
R['N0003']['judgment']='人形RL控制校招。本人仿真测试用具由如引出；上位传统控制一般要求支持但PID等具体方法为示例。感知团队协作保持分列。'
R['N0044']['judgment']='足式RL控制实习仅有职责；逐段和校招职责相同但缺要求，仿真工具保留如例示，不从相似广告补要求。'
for rid in ['N0003','N0044']:
 for e in [rid+':O1',rid+':O2']:ov(rid,e,'职责中如引出仿真工具例示。',branch='EXAMPLE')
ov('N0003','N0003:2:0','控制策略如PID等为专业方法示例。',branch='EXAMPLE')
R['N0591']['judgment']='全局局部规划层次明确。Nav2更佳是优先要求；熟悉至少一类规划并不让MPC无条件必需。代价地图不直接等于SLAM，保留另句定位建图上位要求与斜线未知。'
ov('N0591','N0591:3:0','MPC是至少一类局部规划清单例示之一。',branch='CHOICE_AND_EXAMPLE')
ov('N0591','N0591:4:0','Nav2更佳明确优先。',metric='PREFERRED')
ov('N0591','N0591:O17','碰撞代价地图不是独立定位建图要求。',metric='SEPARATE',branch='NAVIGATION_OBJECT')
add('N0591','TC_SLAM','GENERAL','UNCONDITIONAL','理解定位与建图基本原理','上位知识明确，不以括号具体方案的未知抹去。')
R['E0003']['judgment']='RL/IL运控研发有据；优先IL原引用职责，改回加分原句。不把原文误称Pytorch为编程语言纠正成额外技能要求。'
ov('E0003','E0003:O15','优先证据必须定位到加分句。',metric='PREFERRED',quote='加分项：做过基于强化学习、模仿学习的机器人控制任务')
R['E0004']['judgment']='双足RL控制与传统控制要求清楚；C++/Python和ROS/ROS2保留未知。优先IL定位错到职责，修正原文，机械改进意见仍是协作对象。'
ov('E0004','E0004:O18','优先证据定位回相关经验优先句。',metric='PREFERRED',quote='有过基于强化学习、模仿学习的机器人控制任务相关经验优先')
R['E0102']['judgment']='机电控制及治具开发明确，可靠性测试是使用，不等于开发可靠性技术；另补测试执行。售后支持未明示具体排障过程，不自动补在役事件方法。'
R['E0090']['judgment']='嵌入式电机控制程序开发清楚，可靠性测试属于使用，测试台研发单列。未凭岗位名补语言或方法。'
for rid,eid in [('E0102','E0102:O4'),('E0090','E0090:O5')]:
 ov(rid,eid,'产品可靠性测试为技术使用，测试台研发另记评测开发。',metric='DUTY_OWN_USE')
 add(rid,'TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL','可靠性测试','明确执行可靠性测试。')
R['E0236']['judgment']='遥操作算法开发不同于操作员采集。职责仿真工具等为示例；参与多模态方案是协作。修复Gazebo要求定位，补参数辨识优先方法，不凭遥操作字样补数据操作。'
for e in ['E0236:O1','E0236:O2']:ov('E0236',e,'Gazebo/Mujoco等为职责例示。',branch='EXAMPLE')
ov('E0236','E0236:O7','一般要求证据应定位到任职段。',metric='GENERAL',quote='有ROS/ROS2、Gazebo、Isaac Sim等机器人仿真与实验经验')
ov('E0236','E0236:O16','参与多模态方案设计不明个人研发交付。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0236','E0236:4:0','PID/MPC等具体策略示例。',branch='EXAMPLE')
add('E0236','V2_SYSID','PREFERRED','EXAMPLE','动态建模与参数辨识','等经验者优先中明确参数辨识方法。')
register(list(R.values()),'Astra_control_fullread_a')
