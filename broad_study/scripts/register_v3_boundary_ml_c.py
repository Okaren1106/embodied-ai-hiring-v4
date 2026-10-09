from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0399':'独立模型结构设计有证据；参与模型研发下的后训练/RL不能自动作本人独立承担。',
'N0395':'训练流水线与蒸馏压缩明确，修正职责/任职错引、模型和工具斜线以及方法开发与应用。',
'N0387':'语音同步动作生成非已明示生成式机器人策略；没有Diffusion Policy等策略对象证据。',
'N0386':'原文主导/参与责任未解，不强推独立承担；claude/codex关系同样保留未知。',
'N0379':'视听融合网络开发，模型评测执行不等于评测体系开发；框架泛称要求明确。',
'N0202':'GPU集群运维边界明确，Shell/Python/Ansible职责仅斜线未解，非必须自研ML平台。',
'N0492':'本人训练微调与参与模型架构、协助数据平台分开；跟踪世界模型仅背景。',
'N0489':'语言至少一种明确任选；RL/深度学习上位职责与控制操作等应用示例分别保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0399','O2','本人设计多模态模型结构的独立职责更明确，替代参与句。',metric='DUTY_OWN_DEVELOP',quote=ln('N0399',3))
for e in ['O3','1:0']:ov('N0399',e,'参与研发环节不证明本人独立后训练/RL开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0395','O6','大模型/专家模块两个对象关系未知。',branch='UNRESOLVED')
ov('N0395','O10','任职经验应引用F12而不是F4职责；至少两项为任选集合。',metric='REQUIRED',branch='CHOICE',quote=ln('N0395',12))
ov('N0395','O14','Jetson/ARM/嵌入式AI不同对象斜线未解。',branch='UNRESOLVED')
for e in ['1:1','1:2']:ov('N0395',e,'ONNX/TensorRT不同工具斜线未解，不强行任选。',branch='UNRESOLVED')
ov('N0395','1:0','应用已有PTQ/QAT量化等压缩方法，F4未说明自研方法。',metric='DUTY_OWN_USE')
R['N0395']['additions'].append(dict(code='V2_MODEL_COMPRESSION',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote=ln('N0395',3),reason='另一职责明确设计蒸馏目标及Loss和Hard-negative机制，支持本人方法开发。'))
ov('N0387','ADD1','普通Diffusion/VAE/GAN/Flow-based生成模型不等于明示Diffusion Policy等机器人策略。',metric='SEPARATE',branch='GENERIC_GENERATIVE_MODEL')
ov('N0386','O3','主导/参与斜线使本人独立开发责任未解。',branch='UNRESOLVED')
ov('N0379','O5','至少一种框架并不使编程框架上位类任选。',branch='UNCONDITIONAL')
ov('N0379','O9','完成模型评测和误差分析是应用评测，不是研发评测方法。',metric='DUTY_OWN_USE')
for e in ['O2','10:0','10:1']:ov('N0202',e,'职责仅Shell/Python/Ansible等，未有至少一种限定；斜线未知优先。',branch='UNRESOLVED')
for e in ['O2','O3','5:0']:ov('N0492',e,'等为示例，无任选词。',branch='EXAMPLE')
ov('N0492','O7','本人负责大模型训练微调有明确证据，以F11代替参与架构句。',metric='DUTY_OWN_DEVELOP',quote=ln('N0492',11))
ov('N0492','O11','一般动作生成未明Diffusion Policy、Flow Matching或ACT等策略。',metric='SEPARATE',branch='GENERIC_ACTION_GENERATION')
ov('N0492','O12','仿真或真实平台是明确任选。',branch='CHOICE')
for e in ['O15','O16','1:0']:ov('N0492',e,'协助构建/参与架构不能直接计为本人独立开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0492','2:0','跟踪进展并非本人使用世界模型。',metric='SEPARATE',branch='BACKGROUND')
for e in ['O12','O13']:ov('N0489',e,'控制、规划、操作等为算法应用领域示例。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_ml_c')
# Follow-up preserves the earlier decisions and explains the rule correction.
register([
dict(reading_id='N0401',review_mode='FOLLOWUP',judgment='按冻结安全类别包含系统安全目标，不能另造信息安全排除条款。',evidence_overrides=[dict(evidence_id='N0401:O20',metric='PREFERRED',branch='UNCONDITIONAL',reason='端侧权限治理、敏感数据脱敏和安全意识为明确系统安全，冻结定义未排除信息安全。')]),
dict(reading_id='E0590',review_mode='FOLLOWUP',judgment='冻结TC_CONTROL明确包括技术控制器，不额外要求运动控制理论。',evidence_overrides=[dict(evidence_id='E0590:O14',metric='GENERAL',branch='UNCONDITIONAL',reason='原文明确electrical controllers技术器件能力；定义含控制器。'),dict(evidence_id='E0590:O11',metric='DUTY_OWN_USE',branch='EXAMPLE',reason='本人修复机器人的电气control systems，技术控制系统对象明确；不是一般管理控制。')]),
dict(reading_id='N0412',review_mode='FOLLOWUP',judgment='具体子型不自动补机器学习上位重复计数。',evidence_overrides=[dict(evidence_id='N0412:O31',metric='SEPARATE',branch='MODEL_SUBTYPE_ONLY',reason='F44仅VLM/多模态模型，不明示机器学习/神经网络泛称，不重复推ML上位类。')])
],'Astra_v3_frozen_definition_followup')
