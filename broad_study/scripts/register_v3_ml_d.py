from astra_review_tools import *
JUD={
'E0328':'AI管理岗位仍有明确战略和技术交付责任；模拟器和研究方向是例示。安全规范遵循不等于开发安全机制；Required标题范围明确。',
'E0326':'RL控制策略与新仿真场景、训练评估框架本人开发；控制概念原漏主责证据，策略蒸馏为明确优先方法，补录。',
'N0957':'FAR操作学习独立主责，real2sim2real含明确仿真迁移流程开发，应补目录项；团队模型宣传仍分开。',
'N0954':'FAR训练研究基础设施，不是本人模型算法研发；语言上位类必有，具体语言是至少一种示例，框架优先列表也有or。',
'E0435':'整篇交付MLOps平台、数据版本、模型注册和评测发布路径；主任务从机器人模型改为训练推理基础设施。模型注册器不是开发模型，遥操数据接入不是本人遥操。',
'N0984':'Spot模型部署岗位；Python and/or C++职责任选。模型具体RL职责可由开头明确and的本人职责支持，不能仅由后续斜线猜测。',
'N1034':'Orbit巡检模型属其他模型任务，原文确有模型微调职责与经验，补后训练；评测方法建立为开发，数据整理维持资产工作。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','O2','O5','O6','O12','O13','O22','O23','O24']:ov('E0328',f'E0328:{e}','对应e.g.、such as或including领域举例，不能把具体项目全部当无条件。',branch='EXAMPLE')
ov('E0328','E0328:O4','原句选择集成模型偏使用；重新定位另句明确交付生产模型的本人责任。',metric='DUTY_OWN_DEVELOP',quote='Deliver production-ready AI models that meet performance, latency, and reliability requirements for commercial deployment.')
for e in ['O8','O9']:ov('E0328',f'E0328:{e}','遵循AI安全伦理规范是应用约束，没有开发安全机制方法的动作。',metric='DUTY_OWN_USE')
add('E0326','TC_CONTROL','DUTY_OWN_DEVELOP','UNCONDITIONAL','Design, train, and deploy robust RL policies for locomotion, manipulation, whole body control, and dynamic interactions with the environment.','明确控制策略设计训练与部署，不仅团队介绍。')
add('E0326','V2_MODEL_COMPRESSION','PREFERRED','UNCONDITIONAL','Familiarity with policy distillation (e.g. teacher–student) for transferring state-based policies to perception-driven ones.','蒸馏方法本人能力明确，teacher student子方法例示不影响蒸馏上位类。')
add('N0957','V2_SIM2REAL','DUTY_OWN_DEVELOP','UNCONDITIONAL','Develop large-scale real2sim2real pipeline for manipulation','真实到仿真再真实的迁移管线包含明确sim2real。')
for e in ['O2','O3','O4']:ov('N0954',f'N0954:{e}','至少一种的e.g.语言列表，保留任选及例示。',branch='CHOICE_AND_EXAMPLE')
ov('N0954','N0954:O6','至少一种系统或后端语言保证上位语言要求，不等于语言类可有可无。',branch='UNCONDITIONAL')
for e in ['N0954:O5','N0954:7:0','N0954:7:1','N0954:O16','N0954:O17','N0954:O18','N0954:O19']:ov('N0954',e,'例示列表还有or，保留任选及例示两个属性。',branch='CHOICE_AND_EXAMPLE')
add('N0954','TC_REALTIME','DUTY_OWN_DEVELOP','UNCONDITIONAL','You will design systems that support volumes of training data, operate with strict latency requirements','本人设计系统明确严格时延约束。')
ov('E0435','E0435:O12','原引文无MLflow，另句experiment tracking括号确有MLflow。',metric='GENERAL',quote='experiment tracking (MLflow, W&B, Determined)')
ov('E0435','E0435:O19','开发模型注册与审批器不等于开发模型本身，模型作为管理对象使用。',metric='DUTY_OWN_USE')
ov('E0435','E0435:O22','一般经验原锚职责，改引资格段明确dataset lifecycle。',metric='GENERAL',quote='Proven experience owning and delivering an MLOps platform end-to-end — dataset lifecycle, experiment tracking, model registry, evaluation, and serving — at a company that ships models to production')
ov('E0435','E0435:O33','优先经验原锚职责，改引优先段RL基础设施。',metric='PREFERRED',quote='Experience with RL training and evaluation infrastructure for embodied agents (rollout workers, replay buffers, sim-eval harnesses)')
ov('E0435','E0435:1:0','平台接入遥操采集数据不证明本人执行遥操，相关团队及数据域分开。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0435','E0435:6:2','ONNX Runtime完整产品名称不自动成为ONNX格式经验；职责段明确ONNX另保留。',metric='SEPARATE',branch='NAME_OVERLAP')
R['E0435']['task_override']=dict(task='TRAIN_INFER_INFRA',quote='Apptronik is seeking a Staff MLOps Engineer to own the technical direction of our MLOps platform',reason='交付对象是数据实验模型生命周期平台与发布路径，非机器人模型算法。')
for e in ['O1','O2']:ov('N0984',f'N0984:{e}','and/or显式允许只采用其中语言。',branch='CHOICE')
ov('N0984','N0984:O10','后续ML/RL斜线不能定名，但开头岗位直接明确本人开发ML和RL解决方案，改锚此独立正例。',metric='DUTY_OWN_DEVELOP',quote='we are seeking a curious, driven team member to develop cutting-edge machine learning (ML) and reinforcement learning (RL) solutions that run directly on our robots.')
add('N1034','V2_POSTTRAINING','DUTY_OWN_USE','EXAMPLE','Identify and employ model performance improvement strategies - e.g. fine tuning, model selection, and prompt engineering.','本人采用微调策略，例示要求保留。')
add('N1034','V2_POSTTRAINING','GENERAL','UNCONDITIONAL','Experience training, fine tuning, and applying state of the art generative ai models.','并列要求明确微调模型经验。')
register(list(R.values()),'Astra_v3_ml_d')
