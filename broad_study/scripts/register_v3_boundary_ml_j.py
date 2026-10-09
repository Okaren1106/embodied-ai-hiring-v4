from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0068':'端侧推理自研明确，工具内部斜线未知；任职段构建系统句的职责/能力归属保留未知。',
'E0057':'VLA感知操作集成明确；工程栈优先包括示例，框架斜线仍未知。',
'E0055':'云端VLM推理开发，语言、容器与CUDA/Triton未知，至少一种引擎同时示例和任选。',
'E0043':'世界模型架构自研，修复多处把职责跟踪句误引作一般或优先要求的坐标；加分并列没有任选。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('E0068','1:0','深度参与加速算法研究保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['2:1','2:2']:ov('E0068',e,'PyTorch/ONNX/TensorRT跨工具斜线未解。',branch='UNRESOLVED')
ov('E0068','O10','任职段用构建动作而无知识/能力修饰，不能确定职责或能力要求。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP','GENERAL'])
ov('E0057','O3','工程栈者优先后有包括，Linux为优先示例。',branch='EXAMPLE')
for e in ['O6','O7']:ov('E0057',e,'PyTorch/TensorFlow斜线未解，未知优先于等。',branch='UNRESOLVED')
ov('E0057','O12','控制稳定性在真机实验等事项清单中。',branch='EXAMPLE')
for e in ['O5','O6']:ov('E0043',e,'参与数据/评测闭环保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0043','O8','一般要求应引用扎实大模型基础，不引用跟踪职责。',metric='GENERAL',branch='UNCONDITIONAL',quote=ln('E0043',13))
for e in ['O9','O10']:ov('E0043',e,'改用任职一个或多个方向，清单无示例词。',metric='GENERAL',branch='CHOICE',quote=ln('E0043',14))
for e in ['O13','O14','O15']:ov('E0043',e,'改用加分参与过研发的并列清单，原文无任选与示例。',metric='PREFERRED',branch='UNCONDITIONAL',quote=ln('E0043',19))
ov('E0043','1:0','岗位愿景概述，直接研发另有F4，不把我们希望作独立承担。',metric='SEPARATE',branch='BACKGROUND')
ov('E0043','4:0','跟踪前沿为职责背景，不能冒作一般要求。',metric='SEPARATE',branch='BACKGROUND')
ov('E0043','5:0','任职一个或多个方向无示例词。',branch='CHOICE')
ov('E0043','6:0','加分参与过研发清单并列，无任选或示例。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_ml_j')
