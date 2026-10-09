from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0198':'本人基座模型与分布式预训练开发明确；同属基座模型的斜线不使整个类别未知。',
'E0562':'机载异构推理优化属于训练推理基础设施；热约束不是散热设计，模型压缩是方法应用。',
'N0562':'学习型导航与轨迹策略；语言明确任选、ROS版本关系未知，等字列出的算法为示例。',
'N0388':'核心技术栈必备与基础要求、加分区分，语音服务并不自动归机器人动作模型。',
'N0830':'GPU基础设施与MLOps，括号局部任选不可传播到外层Kubernetes；ROS数据格式是经验要求。',
'N0874':'Required下multiple following为任选；括号无示例词，协作收集与本人模型训练区分。',
'N0315':'预训练模型架构与框架优化为本人主责；语言斜线未知、硬性背景局部作用。',
'E0078':'本人负责框架迭代；参与建设不能单独证明模型使用，训练对象保留。',
'N0509':'上位大模型要求不因类内任选而变任选；应用学习方法与自研算法分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('N0198','O12','多模态大模型/具身基座模型均属同一类别。',branch='UNCONDITIONAL')
ov('N0830','O2','Python或similar languages均属编程语言，上位语言能力明确。',branch='UNCONDITIONAL')
ov('N0830','O3','or限定AWS括号内服务，不是外层Kubernetes任选；such as和etc保留示例。',branch='EXAMPLE')
ov('N0830','1:0','AWS外层为such as示例，内部服务选择不改变AWS示例的性质。',branch='EXAMPLE')
ov('N0830','O14','evaluation属于including的具体工作流，保留示例。',branch='EXAMPLE')
ov('N0830','5:0','rosbags括号并列无示例词。',branch='UNCONDITIONAL')
for e in ['O10','O11']:ov('N0874',e,'manipulation、force control等是模型任务示例。',branch='EXAMPLE')
ov('N0874','O12','work closely with各团队收集数据属于协作，不保证本人独立数据收集使用。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O18','O19','O20','O21']:ov('N0874',e,'AI括号无示例词；保留multiple of following祖先的任选。',branch='CHOICE')
ov('E0078','O9','本人负责的框架架构迭代有独立证据，改用该句；参与建设不作独立承担证据。',metric='DUTY_OWN_DEVELOP',quote=RAW[RID['E0078']]['full_description'].splitlines()[2])
ov('E0078','O10','训练Infra服务于模型，参与基础设施建设不证明本人训练或使用模型。',metric='SEPARATE',branch='SUPPORTED_MODEL_OBJECT')
for e in ['O5','O6']:ov('N0509',e,'只有如，没有或/任选；斜线语言不向后续独立框架要求传播。',branch='EXAMPLE')
for e in ['O8','O9','O10','O11','O12','O13']:ov('N0509',e,'功能列表等、方法列表包括均保留示例语境。',branch='EXAMPLE')
for e in ['O16','O17']:ov('N0509',e,'大语言模型或多模态大模型均属基座大模型类别。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_ml_a')
