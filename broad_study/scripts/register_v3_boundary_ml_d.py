from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0508':'语言至少一种仅作用语言，不延伸框架；优先经验并列无任选词。',
'N0499':'参与研发、流程建设与实际复现适配分开；修复未知与任选分支混记。',
'N0520':'运维集群与数据安全是本人职责；特定容器经验优先继承等示例。',
'N0486':'独立核对同模板另一身份原文；语言任选、框架斜线未知、优先经验并列。',
'N0460':'校招参与式研发保留为参与承担提及，不能全部推独立研发；技术兴趣不计知识经验要求。',
'N0467':'参与式训练与独立探索后训练方法分开；至少一种和等双重关系保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
for r in ['N0508','N0486']:
 for e in ['O5','O6']:ov(r,e,'框架斜线未解，语言至少一种不支配另一分句。',branch='UNRESOLVED')
 for e in ['O18','O19','O20','8:0']:ov(r,e,'并列经验清单无任选/示例词，不因旧节点缺失制造未知。',branch='UNCONDITIONAL')
ov('N0499','O6','F11明确完成算法复现、验证与适配，技术领域为等示例；F3仅参与。',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE',quote=ln('N0499',11))
for e in ['O10','O11','O12','1:0']:ov('N0499',e,'参与流程或参与研发仅保留参与承担，不宣称本人独立开发/使用。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O16','O18','O19','3:0']:ov('N0499',e,'等至少一个方向同时有示例和任选。',branch='CHOICE_AND_EXAMPLE')
for e in ['O17','O20']:ov('N0499',e,'World Model/端到端规划不自动增加未明示机器学习上位泛称。',metric='SEPARATE',branch='MODEL_SUBTYPE_ONLY')
for e in ['O27','O28','O29','5:0']:ov('N0499',e,'加分项目经验并列清单，无或或示例词。',branch='UNCONDITIONAL')
ov('N0499','O31','规控/端到端决策内部斜线未解，优先于外层任选。',branch='UNRESOLVED')
for e in ['O8','O9']:ov('N0520',e,'实际部署经验者优先回指Kubernetes、Docker等示例类。',branch='EXAMPLE')
ov('N0460','O3','PyTorch等为示例。',branch='EXAMPLE')
for e in ['O5','O6','O7','O8','O9','O10','O11']:ov('N0460',e,'明确参与训练/建模/部署，未断言本人独立承担；参与语境仍保留可检索。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0460','O17','浓厚兴趣和愿意探索不是知识、使用或经验要求。',metric='SEPARATE',branch='INTEREST')
for e in ['O3','O4','O5','O6','O7','O9','1:0']:ov('N0467',e,'职责明确参与，不提升为独立承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0467','O8','F11具体机器人策略后训练没有机器学习上位泛称，保留方法本身。',metric='SEPARATE',branch='MODEL_SUBTYPE_ONLY')
for e in ['O13','O14','O15','O16']:ov('N0467',e,'等策略中的一种或多种，同时示例与任选。',branch='CHOICE_AND_EXAMPLE')
R['N0467']['additions'].append(dict(code='TC_RL',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE',quote=ln('N0467',11),reason='探索真机RL等后训练方法是明确方法探索职责，区别于上文参与应用。'))
register(list(R.values()),'Astra_v3_boundary_ml_d')
