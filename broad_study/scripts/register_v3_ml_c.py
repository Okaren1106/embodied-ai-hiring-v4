from astra_review_tools import *
JUD={
'N0294':'触觉视觉多模态传感器算法，非机器人动作模型；Python/Pytorch一般要求与大模型加分项区分，信号处理保留目录外。',
'N0350':'3D视觉模型研发与既有网络优化经验；小型化加分未给压缩方法，不自动扩展到限定量化等的目录项。',
'E0064':'后训练算法本人主责成立；数据闭环为主导或深度参与，承担关系未知。预研并沉淀算法方案与只跟踪文献分开。',
'E0299':'核心参与的语音模型工作不升级本人独立研发；要求存在但原证据锚到职责，重新定位明确至少一项与优先原句。',
'E0275':'导航生成模型、数据与评测体系主责；部署工具是等例示，没有任选。工具要求是一般，末尾平台或自动驾驶经验才优先；修正多个跨段错锚。',
'E0258':'双目模型职责完整；框架使用的斜线未解，而资格段或明确任选。标准评估指标不自动等于开发评测方法；FP16/INT8明确低精度方法。',
'E0205':'硬性要求标题支配仿真或真机选项；Isaac/MuJoCo内层斜线仍未知。简写数据训练评测闭环不证明开发数据管线、仿真器或评测工具。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why,**f):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**f))
for e in ['E0064:O3','E0064:2:0']:ov('E0064',e,'主导或深度参与存在本人承担与协作的不同路径，不能确认独立开发。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP'])
ov('E0064','E0064:3:0','预研后明确创新实践及沉淀核心算法方案；后训练为例示研究方向。',metric='DUTY_OWN_DEVELOP')
for e in ['E0299:O1','E0299:O2']:ov('E0299',e,'核心参与研发涵盖后续优化和测试，非直接独立承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0299','E0299:O3','原引用职责，改锚明确资格任选列表。',metric='GENERAL',branch='CHOICE_AND_EXAMPLE',quote='具备以下至少一项核心算法优化经验：语音信号处理、语音唤醒、拒识或交互意图识别、语音识别、声纹识别、语音合成、语音大模型、对话管理系统等；')
ov('E0299','E0299:O4','原引用职责，改锚明确优先要求。',metric='PREFERRED',quote='扎实的语音信号处理基础，深入理解语音识别、语音大模型核心原理者优先；')
ov('E0275','E0275:O1','CUDA位于等工具链例示。',branch='EXAMPLE')
ov('E0275','E0275:O11','资格证据原锚到职责，改为任职要求。',metric='GENERAL',quote='熟悉模型部署与优化流程，掌握 TensorRT、ONNX、CUDA 等加速工具')
ov('E0275','E0275:O22','一般规划要求原锚在职责，按实际资格原句定位。',metric='GENERAL',quote='熟悉机器人局部轨迹规划、动态避障与控制策略，有室内外复杂环境下自主导航系统的研发经验')
for e in ['E0275:1:0','E0275:1:1']:ov('E0275',e,'该工具列表仅等，没有任选。',branch='EXAMPLE')
for e in ['E0275:5:0','E0275:5:1']:ov('E0275',e,'掌握加速工具为一般要求；优先只修饰后面平台或自动驾驶经验。',metric='GENERAL',branch='EXAMPLE')
for e in ['E0258:O1','E0258:O2']:ov('E0258',e,'职责PyTorch/TensorFlow不同框架斜线关系未解。',branch='UNRESOLVED')
for e in ['E0258:O3','E0258:O4']:ov('E0258',e,'一般要求原错锚职责，资格段或明确任选。',metric='GENERAL',branch='CHOICE',quote='熟练使用 PyTorch 或 TensorFlow，具备独立搭建训练、调参、评估能力。')
ov('E0258','E0258:O7','职责原错锚资格段，改引双目模型研发实际动作。',metric='DUTY_OWN_DEVELOP',quote='负责双目深度估计的模型研发，包括网络结构设计、损失函数设计、cost volume 模型、Transformer/Attention 模型等。')
ov('E0258','E0258:O10','此处构建EPE等既有指标以评估误差，未证明开发新的评测方法或工具。',metric='DUTY_OWN_USE')
ov('E0258','E0258:O18','这行是职责下实现模型的子项，且全部是机器学习模型；不作为一般要求未知。',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE')
for e in ['E0258:O19','E0258:O20']:ov('E0258',e,'CNN、GRU与Transformer都在同一机器学习模型类，斜线不影响上位类知识出现。',branch='UNCONDITIONAL')
add('E0258','V2_MODEL_COMPRESSION','GENERAL','EXAMPLE','加速推理优化（FP16、INT8、卷积优化）','低精度FP16/INT8明确，处于模型落地如的例示中。')
for e in ['E0205:O3','E0205:O4','E0205:O10']:ov('E0205',e,'整段明确硬性要求，内层斜线未知仍保留。',metric='REQUIRED')
for e in ['E0205:O7','E0205:O8','E0205:O9']:ov('E0205',e,'模型的数据评测及仿真真机闭环未明确研发相关管线、工具或仿真平台，按使用。',metric='DUTY_OWN_USE')
ov('E0205','E0205:O14','原错锚职责；实际硬性要求中仿真或真机明确任选。',metric='REQUIRED',branch='CHOICE',quote='有仿真（Isaac / MuJoCo）或真机联调经验。')
ov('E0205','E0205:O15','原错锚职责，优先段有明确灵巧手项目占比要求。',metric='PREFERRED',quote='灵巧手项目占比更高；分布式训练经验；有交付级工程产出。')
register(list(R.values()),'Astra_v3_ml_c')
register([dict(reading_id='N0148',review_mode='FOLLOWUP',judgment='核对压缩目录定义后修正先前补项：该项要求明确量化、蒸馏、裁剪或低秩适配，泛称模型压缩不足以断定限定方法。',evidence_overrides=[dict(evidence_id='N0148:ADD1',metric='SEPARATE',branch='UNSPECIFIED_COMPRESSION_METHOD',reason='仅模型压缩与加速，缺少冻结定义要求的具体方法。')])],'Astra_v3_compression_definition_followup')
