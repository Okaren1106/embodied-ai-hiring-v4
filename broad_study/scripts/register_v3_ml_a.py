from astra_review_tools import *
JUD={
'E0001':'VLA方案设计和持续迭代本人动作明确，训练基础设施参与另列；PyTorch或Jax例示任选，ROS/ROS2内部U，校社招合在一广告不拆。',
'E0093':'两句可见完整职责明确RL模型研发及真机验证；验证不证明开发评测工具，改应用。无资格段不自造工具或经验要求。',
'N0384':'端侧模型运行与推理系统交付，非上层Agent。工具职责列表及没有or，改回并列；模型量化方法明确。vLLM/SGLang内部关系未解；Triton未展开，服务器与GPU语言都不能靠相邻工具定名。纠正错误锚在职责段的资格证据。',
'N0199':'模型后训练与RL开发、基础设施与评测平台同在；熟悉模拟器不直接证明本人使用全部模拟器，保留资格未知。模拟器同上位类可判，评测平台服务后训练不等于本人开发后训练算法。',
'N0506':'参与模型/流程不自动归本人开发；另有本人完成模型复现验证适配的例示动作，单独保留。原注释世界模型斜线与此正文不符，纠正并列及承担关系。',
'N0490':'题为WM但世界模型正文仅调研；不证明实际采用。参与架构和协助管线不提升本人开发，另有明确本人训练微调模型。仿真或真机验证为真实任选；优先尾部等技截断，未观察格不能记零。',
'N0458':'校招Infra前四句参与，单独性能稳定问题优化本人明确，必须分句保存；对模型感兴趣不是一般能力要求，PyTorch等应例示，语言至少一种明确任选。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why,**f):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**f))
ov('E0093','E0093:O2','真机验证只是评价应用，无独立测试工具方法开发证据。',metric='DUTY_OWN_USE')
for eid in ['N0384:7:0','N0384:7:1','N0384:7:2','N0384:7:3']:
 ov('N0384',eid,'该职责句使用并列及，没有任选标识；括号斜线只在厂商平台子对象，不外推到已列后端。',branch='UNCONDITIONAL')
ov('N0384','N0384:7:4','开展模型导出、量化、精度对齐和性能优化为普通并列，量化方法本身明确。',branch='UNCONDITIONAL')
for eid in ['N0384:19:1','N0384:19:2']:
 ov('N0384',eid,'vLLM/SGLang内层关系未明，外层至少一种未解决这个组合内的工具关系。',branch='UNRESOLVED')
ov('N0384','N0384:19:4','Triton未展开，仅邻近推理和CUDA工具不足以区分服务器与GPU语言。',metric='UNKNOWN',branch='CHOICE',affected_metrics=['GENERAL'])
add('N0384','V2_TRITON_COMPILER','UNKNOWN','CHOICE','熟悉 TensorRT / TensorRT-LLM、vLLM / SGLang、ONNX Runtime、Triton、CUDA 或厂商 NPU/DSP 工具链中的至少一种。','Triton两种目录对象均可能；本项保留对象未知，仅影响一般任选语境。',affected_metrics=['GENERAL'])
for eid in ['N0384:O19','N0384:O20']:
 ov('N0384',eid,'原要求证据错锚在职责介绍；用真实任职要求中的模型列表定位。',metric='GENERAL',quote='理解 Transformer、LLM、VLM 或 Omni 模型的基本推理流程')
for eid in ['N0384:O8','N0384:O9']:
 ov('N0384',eid,'原引文是重点参与；用主责介绍和后续本人系统建设证据定位，不把参与当独立责任。',metric='DUTY_OWN_DEVELOP',quote='负责机器人端侧/边缘侧多模态模型运行系统的设计、开发与性能优化，将 LLM、VLM、Omni、ASR、TTS 等模型转化为可稳定运行、可双向流式调用、可低时延中断和可观测的系统级推理能力。')
ov('N0384','N0384:24:0','量化位宽均属同一压缩方法，整段与实际项目经验存在或；应优先任选而非例示。',branch='CHOICE')
for eid in ['N0199:O1','N0199:O2']:
 ov('N0199',eid,'此处熟悉模拟器为知识表达，未明确使用所列软件；其独立一般要求记录保留。',metric='SEPARATE',branch='KNOWLEDGE_STATEMENT')
ov('N0199','N0199:5:0','Genesis与Isaac/MuJoCo同在熟悉知识句，内层斜线未明；不因模型自行开发模拟器而补使用平台。',metric='GENERAL',branch='UNRESOLVED')
for eid in ['N0199:O24','N0199:O25','N0199:O26']:
 ov('N0199',eid,'所列全部为模拟器，上位仿真知识存在可判，软件具体任选不外推到上位概念。',branch='UNCONDITIONAL')
ov('N0199','N0199:O10','此句交付后训练分布式系统，非直接模型架构开发；另条神经网络架构研发证据保留。',metric='DUTY_OWN_USE')
ov('N0199','N0199:8:0','后训练评测平台是支持设施，未证明此句本人开发后训练算法；其他明确后训练算法证据不变。',metric='SEPARATE',branch='SUPPORTING_EVALUATION_INFRASTRUCTURE')
for eid in ['N0506:O6','N0506:O10','N0506:O11','N0506:O12','N0506:1:0','N0506:2:0']:
 ov('N0506',eid,'原句明确参与模型研发或流程建设，不直接证明本人独立承担；世界模型并无所称斜线。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0506','N0506:3:0','跟进方向后另有本人完成算法复现、验证与工程化适配；属于例示模型开发，不是仅使用模型。',metric='DUTY_OWN_DEVELOP')
add('N0506','TC_FOUNDATION_MODEL','DUTY_OWN_DEVELOP','EXAMPLE','跟进具身智能、VLA、世界模型等前沿方向，完成算法复现、验证与工程化适配。','独立完成模型复现适配的另句证据，与参与研发分开。')
for eid in ['N0506:O27','N0506:O28','N0506:O29','N0506:6:0']:
 ov('N0506',eid,'加分句为无or的普通并列领域项目经验，不能虚构斜线或任选；按固定普通并列规则。',branch='UNCONDITIONAL')
add('N0506','V2_POSTTRAINING','PREFERRED','UNCONDITIONAL','有大模型微调、模型推理加速、多模态模型部署经验。','明确大模型微调经验，属后训练方法，按普通并列保留。')
for eid in ['N0490:O6','N0490:O9','N0490:O10']:
 ov('N0490',eid,'原文参与架构或协助构建管线，不把支持责任提升为本人独立开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0490','TC_FOUNDATION_MODEL','DUTY_OWN_DEVELOP','UNCONDITIONAL','负责大模型在机器人数据集上的训练、微调与对齐','另句明确本人模型训练后训练，保留有据的独立开发正例。')
ov('N0490','N0490:O11','在仿真或真实机器人平台验证，仿真路径有明确任选。',branch='CHOICE')
ov('N0490','N0490:1:0','跟踪前沿进展与论文调研并不证明使用世界模型方法；不能以标题WM补值。',metric='SEPARATE',branch='LITERATURE_TOPIC')
R['N0490']['source_limits']=[dict(metrics=['PREFERRED'],codes='ALL_APPLICABLE',reason='三个冻结字段均在加分项末句“熟悉Diffusion、NeRF、3D视觉等技”截断；可见正例保留，优先未观察格来源排除，完整职责和一般要求不排除。')]
ov('N0458','N0458:O3','PyTorch等主流框架为显式例示，不是无条件。',branch='EXAMPLE')
for eid in ['N0458:O6','N0458:O7','N0458:O8']:
 ov('N0458',eid,'该句以参与为承担关系，不升级为本人独立使用或开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0458','N0458:O11','对方向有浓厚兴趣是兴趣陈述，不是一般技术能力要求。',metric='SEPARATE',branch='INTEREST')
ov('N0458','N0458:O12','相关经历指前述等方向，模型为其中例示；不把全部方向当本人必需经验。',branch='EXAMPLE')
add('N0458','TC_ML_SYSTEMS','DUTY_OWN_DEVELOP','UNCONDITIONAL','针对模型训练及推理过程中出现的性能和稳定性问题进行分析与优化，推动问题闭环。','独立句直接承担训练推理系统性能优化，不因前句参与而删掉有据本人工作。')
register(list(R.values()),'Astra_v3_ml_a')
