from astra_review_tools import *
ids=['N0938','E0356','N0829','E0409']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
for r in ['N0471','N0299']:R[r]=dict(reading_id=r,review_mode='FOLLOWUP',judgment='',evidence_overrides=[],additions=[])
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['N0938']['judgment']='生产感知、实时点云与标定本人研发明确。including工具清单新旧项统一为示例；优化库括号未明示是示例还是逐项能力，分支保留未知；PCL在外层and并列，明确优先要求。'
for eid in ['N0938:4:0','N0938:4:1','N0938:4:2']:ov('N0938',eid,'industry-standard tools including中的命名工具为示例，与同句OpenCV一致。',branch='EXAMPLE')
for eid in ['N0938:9:0','N0938:9:1']:ov('N0938',eid,'括号Ceres/GTSAM逗号列举未明确例示、全需或择一，不擅自判任选。',branch='UNRESOLVED')
ov('N0938','N0938:9:2','PCL位于外层and并列，不受优化库括号内不明关系影响。',branch='UNCONDITIONAL')
R['E0356']['judgment']='感知算法、MLOps与工具示例成立；两条标签引用了职责中的同词，改为真正一般/优先要求原文。部署嵌入式不自动推新模型压缩方法，Faster/Mask R-CNN斜线保留。'
ov('E0356','E0356:O17','原引用职责pose estimation，修到一般能力明确示例句。',metric='GENERAL',quote='Proficiency in related technical areas such as (but not limited to) deep convolutional neural networks, multi-object tracking, data association, supervised learning and pose estimation')
ov('E0356','E0356:O25','原引用职责pose estimation，修到Bonus中的实际要求，3 or 6 dof路径明确。',metric='PREFERRED',branch='CHOICE',quote='Experience developing ML models for 3 or 6 dof pose estimation')
R['N0829']['judgment']='点云与三维算法、C++/Python本人使用明确；学历专业不替代方法能力。such as/or工具保持任选示例；优化框架括号关系不明，不能强推or；方法子型bundle adjustment或pose graph另有明确任选。'
ov('N0829','N0829:O20','硕博学科方向为学历条件，另有CV工作经验要求。',metric='SEPARATE',branch='EDUCATION_FIELD')
for eid in ['N0829:8:0','N0829:8:1','N0829:8:2','N0829:8:3']:ov('N0829',eid,'libraries such as ... or ...同时具有例示和任选。',branch='CHOICE_AND_EXAMPLE')
for eid in ['N0829:17:0','N0829:17:1','N0829:17:2']:ov('N0829',eid,'括号工具清单没有明确例示/任选词，框架关系未知；后半句or连接优化方法而非软件名称。',branch='UNRESOLVED')
ov('N0829','N0829:O18','neural implicit representations为e.g.模型示例。',branch='EXAMPLE')
add('N0829','V2_KALMAN_FACTOR','PREFERRED','CHOICE','for bundle adjustment or pose graph optimization','明确图优化方法经验，局部方法由or连接。')
add('N0829','V2_3D_RECONSTRUCTION','DUTY_OWN_USE','EXAMPLE','Evaluate and integrate emerging 3D vision methods (e.g., neural implicit representations, advanced meshing techniques)','本人集成明确神经隐式三维方法，e.g.子方法为示例。')
R['E0409']['judgment']='系统性修复标题强度和引用位置；贡献管线与下游导航/操作对象不能全部升为本人研发。world modeling可能是空间世界表征，缺少动态预测/生成界定，保持V2世界模型对象未知。Isaac为合成数据关联来源，未证明实际使用仿真器。'
ov('E0409','E0409:O1','e.g. IsaacSim修饰合成数据来源；本人集成该数据不充分证明使用该仿真器。',metric='UNKNOWN',branch='EXAMPLE',affected_metrics=['DUTY_OWN_USE'])
for n in [3,4,5]:ov('E0409',f'E0409:O{n}','现代AI框架括号清单无明确例示或全需关系，保留分支不明。',branch='UNRESOLVED')
ov('E0409','E0409:O9','such as ROS2, GStreamer, or...同时任选及示例。',branch='CHOICE_AND_EXAMPLE')
for n in [15,16]:ov('E0409',f'E0409:O{n}','Contribute to只确认参与建设，未明确本人交付管线/基础设施。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0409','E0409:O19','指导集成合成数据与实测数据是数据使用，未写生成合成数据。',metric='DUTY_OWN_USE')
for n in [22,23,24]:ov('E0409',f'E0409:O{n}','世界表征支持下游导航/操作/安全，未证明本人研发这些下游技术。',metric='SEPARATE',branch='DOWNSTREAM_OBJECT')
ov('E0409','E0409:O25','原引文是工作简介；改到专业经验段的实际SLAM知识条款。',metric='GENERAL',quote='SLAM, VIO, probabilistic state estimation')
for n in [29,30]:ov('E0409',f'E0409:O{n}','原引文是职责说明；实际经验资格明确perception and/or SLAM。',metric='GENERAL',quote='3–5+ years building and shipping perception and/or SLAM systems in robotics or real-time vision applications.')
ov('E0409','E0409:O36','原引文是职位工作简介；改到Preferred的具体CV方法能力。',metric='PREFERRED',quote='Strong classical computer vision skills (geometry-based methods, feature extraction) complementing learning-based approaches.')
ov('E0409','E0409:1:0','多传感统一world models可能为空间表征；未明示冻结定义的环境动态/预测生成世界模型。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP'])
for eid in ['E0409:5:0','E0409:5:2']:ov('E0409',eid,'位于Preferred；TensorRT/ONNX Runtime括号工具关系未明，不能从方法or套到工具。',metric='PREFERRED',branch='UNRESOLVED')
ov('E0409','E0409:5:1','ONNX Runtime软件名不能重复推出ONNX格式能力。',metric='SEPARATE',branch='ALIAS_ONLY')
ov('E0409','E0409:5:3','Preferred段且acceleration, quantization, or compression明确任选。',metric='PREFERRED',branch='CHOICE')
for r,ee in [('N0471',['N0471:11:0','N0471:11:1']),('N0299',['N0299:18:0','N0299:18:1','N0299:18:2'])]:
 R[r]['judgment']='统一复核括号工具清单：不能把未写or直接解释为必须全部会；也不能凭括号当作举例。无明确关系词且示例/并列两义仍存，改分支未知。'
 for eid in ee:ov(r,eid,'仅类别后的括号多工具清单，示例与逐项要求无法确定；保留未知而非臆断任选或全需。',branch='UNRESOLVED')
register(list(R.values()),'Astra_perception_fullread_b_and_list_scope')
