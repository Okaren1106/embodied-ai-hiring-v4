from astra_review_tools import *
JUD={
'N0148':'本人VLA推理接口压缩与参与数据、配合合成分开；PyTorch/Jax斜线未知，不猜任选。模型后训练经验有明确微调，补一般语境。',
'N0100':'训练平台工程主责明确；支持RL链路不升级为本人RL算法使用，优先任选保持。',
'N0001':'校招模型主责及工具例示明确；要求中的微调工作经验是原文信息，补后训练例示，不能由标题推断。',
'N0102':'北京条与校招职责相近但没有微调流程要求；不套用另一广告补值。计算机视觉只出现在学历领域，不当一般技术要求。',
'N0029':'参与算法与独立负责迭代分开，后者含明确微调；协助测试及配合稳定性不能提升本人承担。PyTorch/Jax内部未知。',
'N0057':'RL或IL显式任选、真实或仿真任选；设计实验验证不证明开发评测方法工具。仅职责，无任职要求段不补造。',
'N0588':'本人基础模型训练部署、预研落地明确；RL或多模态要求与优先项目例示保持。BFM/WBT具体名称不增目录。',
'N0526':'参与研究后另有训练部署动作与方案输出，主任务仍模型；sim2real本人部分工作明确，电机只是例示，全身跟踪器等优先为例示。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for r,ids in [('N0148',['O3','O4']),('N0029',['O2','O3'])]:
 for e in ids:ov(r,f'{r}:{e}','不同工具之间只有斜线，不能推定任选。',branch='UNRESOLVED')
for r,ids in [('N0148',['O7','O8','O9','O12']),('N0029',['O7','O8','O10'])]:
 for e in ids:ov(r,f'{r}:{e}','此句明确参与、配合或协助，不直接证明本人独立承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0100','N0100:O5','本人交付RL训练推理链路工程支撑，不等于直接使用RL算法。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0148','V2_POSTTRAINING','GENERAL','UNCONDITIONAL','有完整的VLA/WAM/VLM训练、部署、微调经验','模型子类斜线未知不影响明列微调经验；微调本身为普通并列流程。')
add('N0001','V2_POSTTRAINING','GENERAL','EXAMPLE','具备预训练、微调、部署等流程的工作经验','明确微调流程经验，等列举中的后训练方法。')
ov('N0102','N0102:O10','计算机视觉是硕士学历相关领域，不能转写一般技能要求。',metric='SEPARATE',branch='EDUCATION_FIELD')
q='负责数据驱动的模型迭代全流程工作，涵盖多模态数据采集、清洗、增强，以及模型训练、微调、性能优化，探索具身智能模型优化方案，提升机器人操作决策能力与模型泛化性、鲁棒性。'
add('N0029','TC_FOUNDATION_MODEL','DUTY_OWN_DEVELOP','UNCONDITIONAL',q,'另句明确负责模型迭代，保留本人承担证据。')
add('N0029','V2_POSTTRAINING','DUTY_OWN_DEVELOP','UNCONDITIONAL',q,'明确负责模型微调而非仅标题后训练。')
add('N0029','V2_POSTTRAINING','GENERAL','UNCONDITIONAL','有完整的VLA/WAM/VLM训练、部署、微调经验','微调工作经验明确，模型子类斜线不影响此上位方法。')
ov('N0029','N0029:O21','原配合句不能证明本人承担；重新定位到明确负责模型迭代及提升鲁棒性的完整句。',metric='DUTY_OWN_DEVELOP',quote=q)
ov('N0057','N0057:O1','感知是包括列表中的一类研究内容。',branch='EXAMPLE')
for e in ['O2','O3']:ov('N0057',f'N0057:{e}','强化学习或模仿学习明确任选。',branch='CHOICE')
ov('N0057','N0057:O5','设计实验验证算法性能是评价应用，没有独立评测方法工具开发证据。',metric='DUTY_OWN_USE')
ov('N0057','N0057:O6','真实或仿真环境为显式任选。',branch='CHOICE')
ov('N0526','N0526:O5','电机建模位于例如列表。',branch='EXAMPLE')
ov('N0526','N0526:O8','全身运动跟踪器等相关项目为优先例示。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_ml_b')
