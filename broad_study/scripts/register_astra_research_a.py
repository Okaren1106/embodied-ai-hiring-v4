from astra_review_tools import *
ids=['N0047','N0288','N0600','E0589','E0301','N0032','N0400','N0046','E0237']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def suffix(r,s,why,**v):
 e=[e for e in EB[RID[r]] if e['evidence_id'].endswith(s)];assert len(e)==1,(r,s,e);ov(r,e[0]['evidence_id'],why,**v)
def codes(r,cc,why,**v):
 for e in EB[RID[r]]:
  if e['code'] in cc:ov(r,e['evidence_id'],why,**v)
R['N0047']['judgment']='本人灵巧操作算法与数据采集系统研究明确；双手控制和感知规划条款只写参与，保留协作关系，不能把参与自动升级成本人方法研发。'
for n in [4,5,6]:suffix('N0047',f':O{n}','参与研究的对象与明确本人研究的条款分开。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
R['N0288']['judgment']='拓扑优化理论、有限元、数值方法是实质工作；C/C++斜线及至少一种语言维持局部分支。Eigen与PETSc等为优先经验示例，关注前沿不等于本人使用某方法。'
ov('N0288','N0288:24:1','数值计算库Eigen、PETSc等是例子，未出现任选关系。',branch='EXAMPLE')
ov('N0288','N0288:11:0','跟踪研究进展属于研究关注对象，不能单凭该句计具体方法本人使用。',metric='SEPARATE',branch='RESEARCH_AWARENESS')
R['N0600']['judgment']='研究方向覆盖多类机器人问题，无法把方向清单当作每名博士后都本人承担的具体方法。保留MULTIAREA；机械臂抓取与全身控制优先经验为普通并列，未扩成任选。'
R['E0589']['judgment']='原文只有宽泛机器学习与机器人研究能力，未写具体工具或细方法；不能把简短但自洽的招聘正文当作来源截断，也不能从研究机构背景补工具。'
R['E0301']['judgment']='具身基础模型架构、训练及实机实验为本人工作；数据资源与团队介绍仍单列。PyTorch一般要求、预训练/模型工程优先经验有据，部署调试未自动计为在役故障支持。'
R['N0032']['judgment']='机器人学习研究任务成立；基于IL/RL/大模型等是方法应用的例子，参与双手及感知规划仍协作。虚实迁移技术研究需补本人开发语境；校园受众另做敏感性。'
for n in [5,6,7]:suffix('N0032',f':O{n}','基于列举方法研究操作算法，例子不计为无条件开发这些方法本身。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for n in [8,9,10]:suffix('N0032',f':O{n}','参与的研究对象，未明确主导或本人承担该方法交付。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0032','N0032:2:0','AI Habitat、Isaac等仿真环境是示例，无任选词。',branch='EXAMPLE')
R['N0032']['additions'].append(dict(code='V2_SIM2REAL',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote='研究虚实迁移技术',reason='原文明确研究该迁移技术，不仅执行迁移。'))
R['N0400']['judgment']='世界模型及VLA的直接上位要求保留；包括/等子方法改为示例，斜线控制与学习分支保留未知，主导或参与经历不消除对象明确的上位经验要求。'
for n in [6,7,8,10,12,13,15,16]:suffix('N0400',f':O{n}','本条子方法或子任务受包括、如或等列举限定。',branch='EXAMPLE')
for n in [5,9,18,19]:suffix('N0400',f':O{n}','本方法所在斜线组合未解决，未知限定于此语境。',branch='UNRESOLVED')
for eid in ['N0400:5:0','N0400:6:0','N0400:11:0','N0400:15:0']:
 ov('N0400',eid,'本标签为等或括号子方法示例，没有明确or。',branch='EXAMPLE')
R['N0046']['judgment']='仅有参与和协助研究条款；研究领域与本人承担方法分开，不从研究实习生职称推本人开发。来源虽短，不凭长度认定截断。'
codes('N0046',[e['code'] for e in EB[RID['N0046']]],'三条职责均以参与或协助表述，方法保留为协作研究对象。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
R['E0237']['judgment']='力触觉VLA研究的核心是操作实验、数据管线与评估；实验执行不自动等于开发评测工具。要求与职责分开，Python/ROS或ROS2的混合分支继续未知。'
for n in [4,7,8]:suffix('E0237',f':O{n}','原文负责操作验证评估，属于本人方法应用；不能计作一般要求或评测工具研发。',metric='DUTY_OWN_USE')
register(list(R.values()),'Astra_research_science_batch_a')
