from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0363':'多模态交互三选至少二祖先关系保留；TensorRT/ONNX Runtime在一般要求斜杠未解，Runtime不能推出ONNX格式；本人数据管线明确漏标。',
'N0150':'工业感知：PCL及Open3D明确并列，TensorRT括号例示，至少一种框架需保留选项；优化推理不等于改模型。',
'N0500':'空间重建：参与世界模型不能变独立使用，重建流程本人搭建可保留；加分世界模型与一般重建均有任选条件。',
'E0117':'感知项目：自身开发三维重建与标定、合成数据管线；抓取解决目标不等于独立操作算法，要求中抓取算法经历则保留。',
'N0394':'语音前端：数据清洗预处理为本人使用数据处理方法，未明示开发管道；量化部署有具体技术可保留压缩。',
'N0389':'声学负责人：硬件设计与质量风险协作不变独立责任；项目计划及验收主责明确，编码闭环与技术要求分别。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O9','O10']:ov('N0363',e,'原引职责，改实际三类能力中的视听融合要求。',metric='GENERAL',branch='CHOICE',quote='熟悉 VAD、ASR/TTS 接入、声源定位（DOA）、活跃发言人检测（ASD）、音视频融合算法（Audio-Visual Fusion）或声纹特征提取/说话人分离（Speaker Embedding / Speaker Diarization）。')
for e in ['11:0','11:2']:ov('N0363',e,'一般要求中的TensorRT / ONNX Runtime斜杠未解；上级任选不能消除内部未知。',metric='GENERAL',branch='UNRESOLVED')
ov('N0363','11:1','ONNX Runtime名称不能推出ONNX格式能力。',metric='SEPARATE',branch='RUNTIME_NOT_FORMAT')
add('N0363','TC_DATA_PIPELINE','DUTY_OWN_DEVELOP','UNCONDITIONAL','低延迟数据流管线（Data Pipeline）设计','本人设计端侧感知数据管线明示。')
ov('N0150','O2','至少一种框架的括号例示，保留任选祖先。',branch='CHOICE_AND_EXAMPLE')
ov('N0150','1:0','推理工具括号并列例示，无or。',branch='EXAMPLE')
for e in ['4:0','4:1']:ov('N0150',e,'熟悉PCL、Open3D，以及至少一种框架，前两者明确并列。',branch='UNCONDITIONAL')
ov('N0150','O11','优化推理速度属于模型部署工程，未证明修改模型结构/训练算法。',metric='SEPARATE',branch='DEPLOYMENT_MODEL_OBJECT')
ov('N0500','1:0','参与等方向研发，非本人独立世界模型使用。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0500','1:1','原参与句重锚独立搭建三维场景重建流程。',metric='DUTY_OWN_DEVELOP',quote='基于主流开源框架进行二次开发，搭建自动化三维场景重建、补全与评测流程。')
ov('N0500','2:0','优化三维重建相关算法训练渲染推理，为开发算法。',metric='DUTY_OWN_DEVELOP')
ov('N0500','3:0','至少一个方向，其中SLAM等不必都是三维重建。',branch='CHOICE')
ov('N0500','6:0','世界模型或其他生成模型/场景补全，明确任选。',branch='CHOICE')
ov('N0500','7:0','等基础算法是例示。',branch='EXAMPLE')
ov('N0500','18:0','等相关技术为例示。',branch='EXAMPLE')
ov('E0117','O10','本人开发视觉位姿估计及标定，抓取是应用问题，不独立推出操作算法开发。',metric='SEPARATE',branch='MANIPULATION_APPLICATION_OBJECT')
add('E0117','V2_3D_RECONSTRUCTION','DUTY_OWN_DEVELOP','UNCONDITIONAL','重点攻克在工业强光、反光、弱纹理等环境下的高精度检测、分割、配准与实时三维重建','本人研发实时三维重建明确。')
ov('N0394','O9','负责现有语音数据预处理，不等于构建数据管道。',metric='DUTY_OWN_USE')
for e in ['O10','O13']:ov('N0389',e,'分别协同硬件团队与协同质量团队完成。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
R['N0389']['catalog_gap_notes']=['原文明示统筹项目立项、推进与验收并制定项目计划；V2_PROJECT_METHOD未在感知职能适用，不修改冻结目录或强行统计，保留未覆盖证据。']
register(list(R.values()),'Astra_v3_boundary_perception_b')
