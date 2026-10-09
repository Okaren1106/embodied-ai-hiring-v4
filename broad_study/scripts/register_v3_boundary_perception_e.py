from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0981':'SLAM空间AI：同上位VLA/行为大模型不构成上位任选；神经重建未指定高斯/辐射场表示，保留方法对象未知。',
'N0687':'视觉研究：Must each统摄子条目；云平台不能降为一般要求。NeRF与Gaussian明确属既有重建表示目录，补硬性要求；安全探索目的不等于本人安全工程。',
'E0408':'感知学习：一般与加分项重定位；合成数据来源不证明使用模拟器；支撑导航操控不等于本人开发该算法；世界模型含义未明确到动态预测。',
'N1024':'触觉：硬性要求统摄Git；ground-truth数据用途不等于本人标定或仿真能力；仿真器为举例，保留实际传感器模拟职责。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why,**f):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**f))
for e in ['O32','O33']:ov('N0981',e,'VLA与large behavior models均在基础模型上位，不以斜杠生成上位未知。',branch='UNCONDITIONAL')
add('N0981','V2_KALMAN_FACTOR','GENERAL','CHOICE_AND_EXAMPLE','Probabilistic state estimation and sensor fusion (factor graphs, filtering, optimization on manifolds)','one or more上级任选；括号因子图为例示。')
add('N0981','V2_3D_RECONSTRUCTION','UNKNOWN','UNRESOLVED','3D reconstruction (SfM, MVS, multi-view geometry, neural/implicit reconstruction)','神经/隐式重建未展开为目录指定的高斯/辐射场表示；不把全部三维重建自动纳入。',affected_metrics=['GENERAL_CHOICE_AND_EXAMPLE'])
ov('N0687','O1','e.g.示例中又有or。',branch='CHOICE_AND_EXAMPLE')
ov('N0687','O4','重定位本人维护导航栈职责，避免协作段落混义。',metric='DUTY_OWN_DEVELOP',quote='(viii) maintaining a camera and 2D lidar based navigation stack, including fixing bugs, adding new customer feature requests, and ensuring successful deployments.')
ov('N0687','O5','safe exploration为感知目标，并未独立承担安全工程。',metric='SEPARATE',branch='APPLICATION_SAFETY_GOAL')
for e in ['1:0','1:1']:ov('N0687',e,'Must each为硬性父语境，平台之间or保留。',metric='REQUIRED')
add('N0687','V2_3D_RECONSTRUCTION','REQUIRED','UNCONDITIONAL','Neural Radiance Fields, and Gaussian Splats','两种明确场景表示，属于冻结条目而非目录外。')
q='optimally merged pose-graphs';p=RAW[RID['N0687']]['full_description'].index(q)
add('N0687','V2_KALMAN_FACTOR','DUTY_OWN_USE','UNCONDITIONAL',q,'本人采用位姿图优化构建地图；定位职责总段首处。',field='full_description',start=p,end=p+len(q))
add('N0687','V2_HIL','REQUIRED','UNCONDITIONAL','with hardware-in-loop','Must each条目中明确硬件在环。')
for e in ['O1','O20']:ov('E0408',e,'IsaacSim是合成数据来源示例；本人集成数据不证明本人运行模拟器。',metric='SEPARATE',branch='SYNTHETIC_DATA_SOURCE')
ov('E0408','O19','明确集成合成数据，未写生成器开发。',metric='DUTY_OWN_USE')
for e in ['O23','O24','O25']:ov('E0408',e,'世界表示支撑下游任务，并未在此承担导航/操控/安全工程。',metric='SEPARATE',branch='APPLICATION_OBJECT')
q='Strong background in deep learning for computer vision, with practical expertise in detection, segmentation, multi-object tracking, and 3D perception.'
for e in ['O26','O27']:ov('E0408',e,'原引用职责，改定位实际一般要求。',metric='GENERAL',quote=q)
ov('E0408','O29','原误引职责；一般要求中的括号例示。',metric='GENERAL',branch='EXAMPLE',quote='Deep understanding of 3D geometry, camera models, and probabilistic estimation (EKF/UKF, SLAM, VIO).')
ov('E0408','O31','部署时热约束，不足以认定热管理方法能力。',metric='SEPARATE',branch='THERMAL_CONSTRAINT')
ov('E0408','O33','原误引职责，改加分项明确CV知识。',metric='PREFERRED',quote='Strong classical computer vision skills (geometry-based methods, feature extraction) complementing deep learning approaches.')
ov('E0408','O34','原误引职责，改加分项模型压缩方法。',metric='PREFERRED',quote='Expertise in model acceleration, quantization, or compression (TensorRT, ONNX Runtime).')
ov('E0408','O9','such as举例且or列任选。',branch='CHOICE_AND_EXAMPLE')
ov('E0408','1:0','统一世界表示也可能是空间地图，未明确环境动态预测生成。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP'])
ov('E0408','4:0','EKF/UKF在括号示例内。',branch='EXAMPLE')
for e in ['5:0','5:2']:ov('E0408',e,'Preferred项方法or，工具是括号示例。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('E0408','5:1','ONNX Runtime不等于显式ONNX格式。',metric='SEPARATE',branch='RUNTIME_NOT_FORMAT')
ov('E0408','5:3','加速、量化、压缩均属此上位，Preferred而非General。',metric='PREFERRED')
for e in ['O1','O2']:ov('N1024',e,'e.g.模拟环境举例。',branch='EXAMPLE')
ov('N1024','O10','以本人设计感知数据系统的明确句重定位，协作不自动等于独立承担。',metric='DUTY_OWN_DEVELOP',quote='In this role, you will design and develop sensing data systems that allow robots to physically interact with the world, transforming raw tactile signals into meaningful data representations that drive intelligent robot behavior.')
ov('N1024','O14','生成标定/建模数据的目的，不是开发评价工具。',metric='SEPARATE',branch='GROUND_TRUTH_DATA_PURPOSE')
for e in ['O21','O22','6:0']:ov('N1024',e,'经验是执行采集活动；标定/仿真是所产数据用途，未证明本人执行这些方法。',metric='SEPARATE',branch='GROUND_TRUTH_DATA_PURPOSE')
ov('N1024','1:0','ground truth供标定使用不等于开发标定程序。',metric='SEPARATE',branch='GROUND_TRUTH_DATA_PURPOSE')
ov('N1024','4:0','Required Experience与must possess父语境明确。',metric='REQUIRED')
register(list(R.values()),'Astra_v3_boundary_perception_e')
