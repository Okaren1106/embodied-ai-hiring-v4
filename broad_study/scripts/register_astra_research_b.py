from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ['E0325','N0688','N0822','N0947','N1040']}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def old(r,n,why,**v):ov(r,f'{r}:O{n}',why,**v)
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['E0325']['judgment']='IL/RL与仿真环境本人研发明确，实际机器人实验有据。Sim2Real属于Bonus，修复新旧标签强度不一致；安全质量泛称不能替代专业安全方法。'
ov('E0325','E0325:3:0','原文位于Bonus Points。',metric='PREFERRED')
old('E0325',21,'safe, high-quality software仅为泛化质量目标，没有安全标准或专业方法要求。',metric='SEPARATE',branch='GENERAL_QUALITY_GOAL')
old('E0325',12,'evaluation frameworks在including子清单内，保留方法示例。',branch='EXAMPLE')
old('E0325',11,'scalable training pipelines在including子清单内，保留方法示例。',branch='EXAMPLE')
R['N0688']['judgment']='全体资格位于Preferred；库要求同时有at least one与such as，采用任选加示例。RL/IL职责斜线未解，其他研究方向只是括号举例；大模型训练系统本人使用另有明确条款。'
for n in [3,4,5]:old('N0688',n,'at least one library such as限定命名库。',branch='CHOICE_AND_EXAMPLE')
for n in [8,11]:old('N0688',n,'跨学科括号内带etc.，属于示例研究方向。',branch='EXAMPLE')
for n in [9,10]:old('N0688',n,'RL / IL的斜线未明；未知只限定本人研究语境。',branch='UNRESOLVED')
R['N0822']['judgment']='操作/VLA研究、实验评估和训练系统为明确工作；正文长但专业优先段可定位。修复方法举例、任务or和辅助定义的承担关系，补明确RL微调经验。'
for n in [34,35]:old('N0822',n,'上位操作理解明确，control/perception在including子清单内。',branch='EXAMPLE')
old('N0822',47,'humanoid robots, bimanual systems, or multi-fingered hands明确任选。',branch='CHOICE')
for n in [18,19]:old('N0822',n,'Help define只明确协助定义，保留协作对象，其他本人评测开发条款不受影响。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
old('N0822',17,'reliable robot capabilities为可靠结果的泛称，未具体说明可靠性方法。',metric='SEPARATE',branch='GENERAL_QUALITY_GOAL')
add('N0822','V2_POSTTRAINING','PREFERRED','CHOICE','Experience with reinforcement-learning fine-tuning, offline RL, reward modeling, preference learning, or autonomous policy improvement.','明确微调经验，方法清单由or连接；此前候选遗漏。')
R['N0947']['judgment']='FAR团队另列。任意语言加such as为任选示例；主职责包括明确系统辨识和虚实迁移，原reject称未写与原文矛盾。补漏并保留研究方向示例，不从团队数据资源补本人管线。'
for n in [2,3,4]:old('N0947',n,'any programming language such as明确任选与示例。',branch='CHOICE_AND_EXAMPLE')
for n in [8,9,10,11,12,13,14,15,16,17]:old('N0947',n,'主职责研究堆栈由including或for example引出具体方法，不能作为无条件方法。',branch='EXAMPLE')
add('N0947','V2_SYSID','DUTY_OWN_DEVELOP','EXAMPLE','state estimation, low-level control, system identification, reinforcement learning, sim-to-real transfer','本人独立研究条款中的including示例明示系统辨识。')
add('N0947','V2_SIM2REAL','DUTY_OWN_DEVELOP','EXAMPLE','state estimation, low-level control, system identification, reinforcement learning, sim-to-real transfer','本人独立研究条款明示虚实迁移；原候选拒绝理由错误。')
add('N0947','V2_POSTTRAINING','PREFERRED','CHOICE','Hands-on experience training or fine-tuning large-scale foundation models or large language models','训练或微调经验择一，保留方法路径分支。')
R['N1040']['judgment']='Atlas操作学习研发与系统辨识明确；Required与ideal candidate不可混用。Sim2Real知识改为Preferred；灵巧或接触丰富任务分支保留。后训练上位要求由fine-tuning独立支持。'
ov('N1040','N1040:5:0','The ideal candidate has段为优先经验。',metric='PREFERRED')
old('N1040',8,'dexterous or contact-rich manipulation明确任务子型任选。',branch='CHOICE')
register(list(R.values()),'Astra_research_science_batch_b')
