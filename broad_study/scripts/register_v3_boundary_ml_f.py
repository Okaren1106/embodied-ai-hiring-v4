from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0628':'双足策略研发与仿真环境开发明确；完成虚实迁移是迁移方法应用。',
'N0159':'感知模型服务导航规划；参与3D研发保留参与承担，仿真品牌斜线未解。',
'N0038':'按工业全栈原文逐句区分参与与明确设计/构建动作，修正标题充证据和后训练斜线。',
'N0090':'本人工业预训练与数据管线；具体LoRA属于冻结低秩适配目录，泛Diffusion不自动变机器人策略。',
'N0070':'灵巧操作与数据采集系统自研，参与感知规划协作单列，技术示例和上位仿真经验区分。',
'N0098':'工业操作策略和迁移评测系统自研；等示例的算法和框架不变无条件。',
'N0158':'操作RL独立研发与协作VLA框架分开，真实测试为评测应用；工具斜线未知。',
'N0163':'3D人体生成与算法验证，语言关系未解；实际测试保障稳定性属于使用。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('N0628','1:0','完成迁移和真机调试，未明研发迁移方法。',metric='DUTY_OWN_USE')
for e in ['O4','O5','O6']:ov('N0159',e,'Isaac/Mujoco/Gazebo内部斜线未解。',branch='UNRESOLVED')
ov('N0159','O13','参与拓扑地图等研发，不宣称独立SLAM开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O16','O17','O18','O19']:ov('N0159',e,'至少一种模型并有等，任选和示例同时成立。',branch='CHOICE_AND_EXAMPLE')
for e in ['O23','O24','O25']:ov('N0159',e,'感知、定位、路径规划等是工作模块示例。',branch='EXAMPLE')
for e in ['O29','O30','O31']:ov('N0159',e,'仿真软件上位经验明确，具体软件才有斜线关系。',branch='UNCONDITIONAL')
for e in ['O8','O9','1:0','1:1','3:0']:ov('N0038',e,'仅参与具身研发/策略研发，保留参与承担，不推独立责任。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0038','2:0','章节标题本身不证明独立后训练职责。',metric='SEPARATE',branch='SECTION_HEADING')
ov('N0038','O13','独立构建数据飞轮闭环有明确职责，改用F27。',metric='DUTY_OWN_DEVELOP',quote=ln('N0038',27))
ov('N0038','O14','仿真合成只在协助构建数据流水线句中。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['5:0','5:1']:ov('N0038',e,'利用域随机化完成部署为迁移方法应用，无自研该方法断言。',metric='DUTY_OWN_USE')
ov('N0038','11:0','预训练/SFT/RLHF斜线跨前后训练阶段未解。',branch='UNRESOLVED')
ov('N0038','13:2','推理优化在加分任一组内，同时等示例。',branch='CHOICE_AND_EXAMPLE')
add('N0038','V2_MODEL_COMPRESSION','GENERAL','EXAMPLE',49,'冻结目录明收低秩适配LoRA，原文等示例须纳入。')
for e in ['O11','O12']:ov('N0090',e,'从感知到控制的端到端策略学习无示例词。',branch='UNCONDITIONAL')
ov('N0090','O14','真机、仿真合成、互联网等是输入数据示例。',branch='EXAMPLE')
ov('N0090','O24','一般扩散模型训练机制不等于生成式机器人策略。',metric='SEPARATE',branch='GENERIC_GENERATIVE_MODEL')
for e in ['O42','O43','O44']:ov('N0090',e,'仿真平台上位要求明确，品牌才是示例。',branch='UNCONDITIONAL')
add('N0090','V2_MODEL_COMPRESSION','GENERAL','UNRESOLVED',20,'LoRA冻结收录，但LoRA/Adapter内部斜线关系不明，保留未知。')
for e in ['O6','O7','O8']:ov('N0070',e,'基于IL、RL、大模型等为技术示例。',branch='EXAMPLE')
for e in ['O11','O12']:ov('N0070',e,'参与感知和规划研究保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O19','O20','O21']:ov('N0070',e,'具身仿真环境上位使用开发经验明确。',branch='UNCONDITIONAL')
for e in ['O3','O4','O5']:ov('N0098',e,'至少一种仿真工具且列等示例。',branch='CHOICE_AND_EXAMPLE')
for e in ['O11','O12','O13','O24','O25','O26']:ov('N0098',e,'算法原句等为示例。',branch='EXAMPLE')
for e in ['O34','O35']:ov('N0098',e,'视觉语言大模型或VLA均支持同一基础模型类别。',branch='UNCONDITIONAL')
for e in ['O1','O2','O3','O4']:ov('N0158',e,'工具内部斜线无明确选择关系。',branch='UNRESOLVED')
for e in ['O10','1:0']:ov('N0158',e,'与团队紧密协作共同设计，独立承担不明，保留协作技术提及。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0158','O12','通过真实场景测试为执行评测。',metric='DUTY_OWN_USE')
for e in ['O14','O15']:ov('N0158',e,'感知-决策-控制闭环无示例词。',branch='UNCONDITIONAL')
for e in ['O17','O18']:ov('N0158',e,'特别是操作、移动控制属于优先经验中的特举。',branch='EXAMPLE')
ov('N0163','O8','实际测试确保稳定性，未明研发可靠性机制。',metric='DUTY_OWN_USE')
register(list(R.values()),'Astra_v3_boundary_ml_f')
