from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0033':'工业规划：职责全为参与；语言未知、至少一种仿真软件的关系保留。',
'N0025':'工业力控：抓取或操作均操作上位，力控或遥操才是加分任选。',
'N0144':'应用工程：ROS2或类似中间件是职责任选；运动规划方法上位明确。',
'N0036':'交互校招：与另一交互广告相同语义的工具斜杠、加分任选同口径修正。',
'N0065':'导航：本人使用定位感知输出；真机测试为协作，非开发评价工具。',
'N0605':'运控：职责C++不能消除一般要求C/C++未知；ROS与ROS2明确分开，仿真上位明确。',
'E0007':'电机控制：明确c语言保留；软件控制电机不作开发物理电机；经典控制方法为列举。',
'E0005':'动力学控制：C/C++未知、Python明确；补明确经典控制理论要求。',
'N0296':'双臂算法：使用感知输出而非开发感知；本人搭建仿真与协作标定分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O6','O7']:ov('N0033',e,'明确参与开发，不作独立承担。',metric='SEPARATE',branch='PARTICIPATION')
for e in ['O11','O12']:ov('N0025',e,'抓取和操作同操作上位。',branch='UNCONDITIONAL')
ov('N0025','4:0','力控或遥操作为加分任选。',branch='CHOICE')
ov('N0144','O1','ROS2或类似中间件。',branch='CHOICE')
ov('N0144','1:0','路径搜索/轨迹优化/采样规划均属冻结方法上位。',branch='UNCONDITIONAL')
for e in ['O1','O2']:ov('N0036',e,'IsaacSim/MuJoCo斜杠关系未解。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_USE_CHOICE','DUTY_OWN_USE_EXAMPLE','DUTY_OWN_USE_CHOICE_AND_EXAMPLE'])
for e in ['5:0','5:1','5:2']:ov('N0036',e,'工具仅斜杠列举，缺少任选关系。',branch='UNRESOLVED')
ov('N0036','10:0','经验或论文为加分任选。',branch='CHOICE')
ov('N0065','O13','联动其他团队完成真机测试，非独立开发评价系统。',metric='SEPARATE',branch='COLLABORATIVE_TESTING')
ov('N0605','O6','一般要求C/C++仍未解，职责明确C++只支持职责层。',branch='UNRESOLVED')
for e in ['O11','O12','O13','O14']:ov('N0605',e,'具体方法/平台列举不削弱控制理论、仿真平台上位要求。',branch='UNCONDITIONAL')
ov('E0007','O3','本人开发控制软件，电机是使用/作用对象，未开发物理执行器。',metric='DUTY_OWN_USE')
ov('E0007','2:0','包括PID等理论，为方法列举。',branch='EXAMPLE')
R['E0005']['additions'].append(dict(code='V2_CLASSICAL_CONTROL',metric='GENERAL',branch='UNCONDITIONAL',quote='熟练掌握经典控制理论和现代控制理论',reason='明确控制理论，不需靠算法别名反推。'))
ov('N0296','O14','操作算法结合感知与决策，不是明确开发感知。',metric='DUTY_OWN_USE')
ov('N0296','O17','负责仿真环境搭建是开发。',metric='DUTY_OWN_DEVELOP')
ov('N0296','2:0','与各团队紧密协作完成标定。',metric='SEPARATE',branch='COLLABORATION')
register(list(R.values()),'Astra_v3_boundary_control_c')
register([dict(reading_id='N0077',review_mode='FOLLOWUP',judgment='与逐字同义交互广告N0036统一：Transformer和Diffusion皆ML模型，上位要求明确。',evidence_overrides=[dict(evidence_id='N0077:'+e,branch='UNCONDITIONAL',reason='模型架构例示属于同一ML模型上位；具体工具层仍分别处理。') for e in ['O16','O17']])],'Astra_v3_hri_upper_concept_followup')
