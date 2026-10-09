from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0823':'现场感知：ROS/ROS2仍未解，C++/Python是括号列举；补明确加分标定，状态估计方法例示不作无条件SLAM。',
'N0825':'三维建图：such as与or须同时保留；PCL/Open3D仅例示；标定为加分任选，目录外格式不补工具。',
'E0490':'Helix感知：VIO/SLAM同SLAM上位，受至少一领域任选；Spark是like例示，VLM补基础模型领域任选。',
'E0565':'人体状态估计：职责/要求重定位；工具括号例示不作任选，补明确因子图方法；加分标定斜杠仍未解。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why,**f):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**f))
for e in ['O1','O2']:ov('N0823',e,'现代机器人软件开发后括号列语言。',branch='EXAMPLE')
ov('N0823','O21','VIO/LIO/mapping在括号方法列举中。',branch='EXAMPLE')
add('N0823','V2_CALIBRATION','PREFERRED','UNCONDITIONAL','Experience integrating and calibrating custom sensor rigs','明确加分标定经历，不是一般项重复。')
for e in ['6:0','6:1','6:2']:ov('N0825',e,'such as举例且or任选。',branch='CHOICE_AND_EXAMPLE')
for e in ['10:0','10:1']:ov('N0825',e,'such as仅举例，无任选词。',branch='EXAMPLE')
ov('N0825','23:0','survey control/calibration/measurement tools之间or。',branch='CHOICE')
for e in ['O8','O9']:ov('E0490',e,'VIO和SLAM同上位，整份领域列表at least one才是任选。',branch='CHOICE')
ov('E0490','3:0','like Spark and Ray是举例。',branch='EXAMPLE')
add('E0490','TC_FOUNDATION_MODEL','GENERAL','CHOICE','Vision-Language Model (VLM)','明确领域任选的VLM。')
ov('E0565','O2','原误引职责，重定位真实语言要求。',metric='GENERAL',quote='Proven ability to write high-performance, modular C++ for embedded or edge computing platforms alongside Python for data analysis and visualization.')
ov('E0565','O7','重定位本人诊断验证工具开发。',metric='DUTY_OWN_DEVELOP',quote='Build diagnostic tooling, validation pipelines, and error analysis workflows to evaluate accuracy for both online and offline algorithms.')
ov('E0565','O15','原误引职责，实际加分项包含多种ML应用任选。',metric='PREFERRED',branch='CHOICE',quote='Prior experience applying Machine Learning (ML) techniques to motion priors, trajectory smoothing, or learned state estimation/calibration.')
ov('E0565','O16','原误引一般要求，实际加分项estimation/calibration斜杠关系未解。',metric='PREFERRED',branch='UNRESOLVED',quote='Prior experience applying Machine Learning (ML) techniques to motion priors, trajectory smoothing, or learned state estimation/calibration.')
for e in ['6:0','6:1']:ov('E0565',e,'括号列优化工具，并无or。',branch='EXAMPLE')
ov('E0565','9:0','teleoperation/haptics/control三个用途or。',branch='CHOICE')
ov('E0565','10:0','estimation/calibration关系未明，外层又有or；不能无条件。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['PREFERRED','PREFERRED_CHOICE'])
add('E0565','V2_KALMAN_FACTOR','GENERAL','EXAMPLE','Hands-on expertise with both real-time filtering techniques ((E)KFs, sliding-window estimators) and offline batch optimization tools (Factor Graphs, GTSAM, Ceres, Non-Linear Least Squares).','明确卡尔曼和因子图方法的括号例示。')
register(list(R.values()),'Astra_v3_boundary_perception_f')
