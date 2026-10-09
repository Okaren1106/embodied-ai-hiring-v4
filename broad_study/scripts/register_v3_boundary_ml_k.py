from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0100':'大模型预训练与控制自研，真机测试是评测执行，LoRA用于训练效率提升。',
'E0082':'训练资源和基础设施优化不是基础模型研发，协作支持运控模型另列。',
'E0300':'训练推理infra与自研压缩方法明确，补模型压缩算法经验要求。',
'E0289':'机器人RL/VLA自研，核对仿真工具示例、任职错引与数据接口/虚实迁移区别。',
'E0288':'云原生AI平台职责明确，C/C++未知；K8s在两处不同语境分别记录。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('E0100','O4','真机部署测试为评测执行，未明评测体系开发。',metric='DUTY_OWN_USE')
ov('E0100','1:0','如LoRA用于提升训练效率，未明自研LoRA方法。',metric='DUTY_OWN_USE')
ov('E0082','O3','优化训练GPU利用率与吞吐是模型训练基础设施优化，不是模型架构研发。',metric='SEPARATE',branch='SUPPORTED_MODEL_OBJECT')
ov('E0082','O4','与团队密切合作支持模型训练优化为协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0082','1:0','明确应用量化、蒸馏等现有技术。',metric='DUTY_OWN_USE',branch='EXAMPLE')
add('E0300','V2_MODEL_COMPRESSION','GENERAL','UNCONDITIONAL',12,'明确具备模型压缩算法经验。')
for e in ['O1','O2']:ov('E0289',e,'仿真平台如所列示例。',branch='EXAMPLE')
ov('E0289','O4','包括Linux管理等计算机基础内容，保留示例。',branch='EXAMPLE')
for e in ['O3','O8']:ov('E0289',e,'改用明确任职ROS2通信框架熟悉句。',metric='GENERAL',quote=ln('E0289',19))
ov('E0289','O9','原引职责仿真句；改用真正任职平台任选句。',metric='GENERAL',branch='CHOICE',quote=ln('E0289',20))
ov('E0289','O15','扩散模型/VLA不同策略基础斜线未解。',branch='UNRESOLVED')
ov('E0289','O19','实时推理部署为包括列表的具体pipeline环节。',branch='EXAMPLE')
ov('E0289','O31','改用明确任职VLA架构理解句，而非负责训练职责。',metric='GENERAL',branch='UNCONDITIONAL',quote=ln('E0289',18))
ov('E0289','1:0','数据流对接不证明开发虚实迁移方法，迁移执行另有F6。',metric='SEPARATE',branch='DATAFLOW_INTERFACE')
ov('E0289','2:0','进行迁移是方法应用，未明方法自研。',metric='DUTY_OWN_USE')
add('E0289','V2_POSTTRAINING','DUTY_OWN_DEVELOP','EXAMPLE',2,'包括强化学习微调策略，明确属于后训练方法研发。')
ov('E0288','O1','深入研究清单含等，K8s此处为示例；下一独立熟悉句仍无条件。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_ml_k')
