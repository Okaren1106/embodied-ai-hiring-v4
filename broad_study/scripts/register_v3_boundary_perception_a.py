from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0563':'空间算法：仿真数据不等于运行仿真，建立评测体系是开发；三维表征与Sim2Real加分均有任选，工具ROS斜杠保持未知。',
'E0146':'触觉力觉：建立测试体系与输出报告分开；数据质量报告不是数据管道开发，要求不能引用职责。',
'N0629':'双足融合：g2o/GTSAM斜杠未解，标定能力是一般要求；因子图本人用于融合明确。',
'N0282':'多模态感知：本人研发感知而机械抓取是应用任务；与硬件规控团队协作标定不等于独立校准。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0563','O10','等技术列举。',branch='EXAMPLE')
ov('N0563','O12','使用仿真数据建立训练体系，未写本人运行仿真。',metric='SEPARATE',branch='SIMULATION_DATA_OBJECT')
ov('N0563','O13','建立训练与评测体系是本人开发。',metric='DUTY_OWN_DEVELOP')
ov('N0563','1:0','等技术列举三维重建。',branch='EXAMPLE')
for e in ['7:0','9:0']:ov('N0563',e,'加分句明确或，不能无条件。',branch='CHOICE')
add('N0563','V2_KALMAN_FACTOR','GENERAL','CHOICE','熟悉点云匹配、图优化、视觉重定位或多传感器融合算法。','图优化是冻结方法之一，明确备选。')
ov('E0146','O7','原引输出报告，改实际建立测试体系。',metric='DUTY_OWN_DEVELOP',quote='建立接触检测、滑移检测、力信号处理、滤波、标定、补偿和可靠性测试体系。')
ov('E0146','O9','输出数据质量评估和问题清单不等于开发数据管道。',metric='SEPARATE',branch='ASSESSMENT_REPORT_OBJECT')
for e in ['O10','O11']:ov('E0146',e,'原引职责，改实际一般测试经验。',metric='GENERAL',quote='具备信号采集、滤波、标定、误差补偿和可靠性测试经验。')
for e in ['O15','O16']:ov('E0146',e,'原有错引；运动控制或抓取控制都属控制上位，重锚真实要求。',metric='PREFERRED',branch='UNCONDITIONAL',quote='有将触觉/力觉信号用于运动控制或抓取控制的项目经验。')
ov('E0146','2:0','输出标定报告不是开发标定方法/工具，开发体系另有明确证据。',metric='SEPARATE',branch='CALIBRATION_REPORT_OBJECT')
for e in ['4:0','4:1']:ov('N0629',e,'g2o/GTSAM斜杠未解。',branch='UNRESOLVED')
ov('N0629','13:0','可独立标定是一般要求，后半足式项目经验才优先。',metric='GENERAL')
ov('N0282','1:0','与硬件规控嵌入式团队紧密协作标定。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0282','O12','本人工作是感知算法，用于精细操作任务，未独立开发操作算法。',metric='SEPARATE',branch='MANIPULATION_APPLICATION_OBJECT')
register(list(R.values()),'Astra_v3_boundary_perception_a')
