from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0284':'商业场景后训练交付明确，团队资源与本人验证能力分开；修正一般要求背景错引。',
'E0266':'运控RL/IL明确研发，补蒸馏应用，逐项修正要求引用职责的错误及内部斜线。',
'E0251':'模型评测体系有明确自建证据，使用正确句；GitHub/HuggingFace社区工具关系未知。',
'E0230':'灵巧手算法、仿真与评测自建；要求引用正确任职段，遥操作继承优先任一。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('E0284','O11','模型适配和功能验证为执行评测，不是开发评测方法。',metric='DUTY_OWN_USE')
for e in ['O14','O15']:ov('E0284',e,'VLA或具身大模型同属明确上位基础模型。',branch='UNCONDITIONAL')
ov('E0284','O16','背景评测体系不能充要求，改用任职能独立完成真机验证句。',metric='GENERAL',quote=ln('E0284',16))
ov('E0284','4:0','与数据工程团队协作推动转化属于协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0284','6:0','微调/后训练内部关系未解，不强行任选。',branch='UNRESOLVED')
for e in ['O1','O2']:ov('E0266',e,'Isaac系列内部同类别，具体平台并列等为示例。',branch='EXAMPLE')
for e in ['O7','O8']:ov('E0266',e,'改用真正任职仿真平台经验句，非职责句。',metric='GENERAL',branch='EXAMPLE',quote=ln('E0266',14))
ov('E0266','O12','训练机器人全身运动控制是本人RL开发的具体技能目标，不是协作部门。',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE')
for e in ['O13','O14']:ov('E0266',e,'ACT、Diffusion Policy、OpenVLA等为应用模型示例。',branch='EXAMPLE')
ov('E0266','O21','一般控制要求应引用任职manipulation或运动控制句。',metric='GENERAL',branch='CHOICE',quote=ln('E0266',15))
for e in ['O22','O23','O24','O25']:ov('E0266',e,'改用明确任职端到端操作模型知识句。',metric='GENERAL',quote=ln('E0266',16))
ov('E0266','O29','强化学习/模仿学习内部斜线未知。',branch='UNRESOLVED')
ov('E0266','O30','优先IL原错引职责，改引真正优先项目经验句。',metric='PREFERRED',branch='UNRESOLVED',quote=ln('E0266',17))
ov('E0266','1:0','解决虚实迁移问题是迁移应用，未说明自研迁移方法。',metric='DUTY_OWN_USE')
R['E0266']['additions'].append(dict(code='V2_MODEL_COMPRESSION',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote=RAW[RID['E0266']]['duties'].splitlines()[5],reason='明确负责强化学习模型蒸馏，不应因服务RL而漏收冻结概念。'))
ov('E0251','O6','直接构造评测体系、设计任务的D5支持开发，不能用参与评测D4证明。',metric='DUTY_OWN_DEVELOP',quote=RAW[RID['E0251']]['duties'].splitlines()[4])
ov('E0251','1:0','github/huggingface内部斜线关系未解。',branch='UNRESOLVED')
R['E0251']['additions'].append(dict(code='V2_GIT',metric='DUTY_OWN_USE',branch='UNRESOLVED',quote=ln('E0251',4),reason='GitHub代码社区问题协作符合冻结Git/GitHub类别，但两平台斜线关系未知。'))
for e in ['O8','O9']:ov('E0230',e,'包括VLA、RL等方向，保留示例。',branch='EXAMPLE')
for e in ['O15','O17','O18']:ov('E0230',e,'改引真正任职VLA/IL/RL项目经验，不能引用职责或跟踪句。',metric='GENERAL',quote=ln('E0230',12))
ov('E0230','O23','RT-1/RT-2同属继承上位模型，原文如和等为示例。',branch='EXAMPLE')
ov('E0230','2:0','优先考虑具备任一经验，遥操作是其中一项。',branch='CHOICE')
register(list(R.values()),'Astra_v3_boundary_ml_l')
