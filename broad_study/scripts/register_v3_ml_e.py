from astra_review_tools import *
JUD={
'N0868':'视觉模型职责与Required Skills分开。服务架构上下文足以确定NVIDIA Triton为推理服务器；原只拒绝GPU编译器却漏了服务器。真实现场模型排障也不能被低延迟句的候选拒绝覆盖。',
'N0821':'操作模型本人主责；基础模型贡献与独立训练实验设施分开，后者另句明确。优先的强化学习微调应补后训练方法。',
'E0452':'WBC训练发布支撑设施主责，不等于本人开发RL策略；现成仿真引擎评估集成为使用。修正控制资格错锚和PhysX要求语境。',
'N0909':'Nimble模型研发与数据收集独立主责，支持生产实施不当作另外的独立部署职责；没有具体编程语言不补。',
'N0710':'Skild全部资格段标Preferred，云平台和CI也必须随之；构建训练平台不自动证明本人开发CI系统。',
'N0663':'全资格段Preferred，仿真上位类与具体平台的例示层级分开，Blender受外层任选约束。MLOps保留上位ML系统，不新建项。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','O2']:ov('N0868',f'N0868:{e}','platforms like及etc明确例示。',branch='EXAMPLE')
for e in ['N0868:5:0','N0868:13:0','N0868:13:1','N0868:13:2','N0868:17:0']:ov('N0868',e,'原句处于Required Skills标题下，应记硬性要求。',metric='REQUIRED')
add('N0868','V2_TRITON_SERVER','REQUIRED','EXAMPLE','Experience with serving architectures like NVIDIA Triton, TorchServe and Tensorflow Serving, Flask and others','serving architectures明确服务对象；并非只因邻近工具猜测。')
add('N0868','V2_CI_CD','REQUIRED','UNCONDITIONAL','Experience with Git and modern CI pipelines','明确CI经验。')
add('N0868','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','training, deploying and troubleshooting models on the field will be under your purview.','现场模型排障明确本人职责，不是仅优化推理速度。')
add('N0868','TC_REALTIME','DUTY_OWN_DEVELOP','UNCONDITIONAL','our use cases require low latency inference that approaches real time and therefore you must be able to build highly performant models and serving architectures.','明确低时延近实时模型及服务架构本人建设。')
for e in ['O15','O16','O17']:ov('N0821',f'N0821:{e}','Contribute to foundation models说明贡献承担关系，不能直接把列举全部变成本人独立开发；其他独立实验设施句另保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0821','V2_POSTTRAINING','PREFERRED','EXAMPLE','Experience with reinforcement-learning fine-tuning, offline RL, and related policy training methods.','明确RL微调且and related methods形成开放列举。')
ov('E0452','E0452:O6','此句描述本人支撑的RL控制系统，交付是training backbone，没有本人策略研发动作。',metric='SEPARATE',branch='SUPPORTING_INFRASTRUCTURE_OBJECT')
ov('E0452','E0452:O8','Evaluate and integrate现成物理引擎与仿真环境是使用，不证明开发新环境。',metric='DUTY_OWN_USE')
for e in ['O3','O4']:ov('E0452',f'E0452:{e}','such as工具列表有or，任选及例示同时保留。',branch='CHOICE_AND_EXAMPLE')
ov('E0452','E0452:3:0','该句在Requirements而非Bonus，且such as工具列表包含or。',metric='GENERAL',branch='CHOICE_AND_EXAMPLE')
ov('E0452','E0452:O16','控制一般要求原锚职责，为真实任职要求重新定位。',metric='GENERAL',quote='Working knowledge of dynamics, controls, and robotics systems')
ov('E0452','E0452:O23','优先要求原锚职责，改引Bonus下明确模型或控制策略。',metric='PREFERRED',quote='Experience deploying ML models or control policies to real-world systems')
add('E0452','V2_MODEL_COMPRESSION','GENERAL','CHOICE','Experience with reinforcement learning, imitation learning, or policy distillation','策略蒸馏明确，or任选。')
for e in ['N0710:4:0','N0710:4:1','N0710:4:2']:ov('N0710',e,'全部Qualifications明确Preferred；云括号无or，属于平台例示。',metric='PREFERRED',branch='EXAMPLE')
ov('N0710','N0710:8:0','该CI经验处于Preferred Qualifications范围。',metric='PREFERRED')
ov('N0710','N0710:2:0','通过自动测试与CI确保平台可靠性，未指本人开发CI工具系统，按使用既有工程方法。',metric='DUTY_OWN_USE')
for e in ['O24','O25','O26']:ov('N0663',f'N0663:{e}','simulation environments自身与robotics或real-time系统任选，平台举例不把上位环境也变为例示。',branch='CHOICE')
ov('N0663','N0663:2:0','Blender是仿真环境括号例示，同时受外层robotics或simulation或real-time任选约束。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_ml_e')
