from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0469':'逐句审读与N0460相同的职责要求，保持不同广告身份；参与承担、兴趣、等示例按同一规则。',
'N0451':'逐句审读实习生版本，参与承担与方法探索分别判定，不以标题自动修改语境。',
'N0621':'本人预训练架构、数据pipeline明确；支持评估不是亲自评估，跟踪Agent不是实际使用。',
'N0618':'核对至少三项与加分至少一项祖先，内部斜线仍未知；源码定制属于开发。',
'N0646':'协助VLA研发、数据与测试是明确协作承担；技术兴趣不能提升为能力要求。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0469','O3','PyTorch等为示例。',branch='EXAMPLE')
for e in ['O5','O6','O7','O8','O9','O10','O11']:ov('N0469',e,'参与式承担保留，不宣称独立执行或开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0469','O19','浓厚兴趣不是知识/经验要求。',metric='SEPARATE',branch='INTEREST')
for e in ['O3','O4','O5','O6','O7','O9','1:0']:ov('N0451',e,'原文明示参与，保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0451','O8','具体机器人策略后训练不自动增加机器学习上位泛称。',metric='SEPARATE',branch='MODEL_SUBTYPE_ONLY')
for e in ['O13','O14','O15','O16']:ov('N0451',e,'等策略中的一种或多种同时示例与任选。',branch='CHOICE_AND_EXAMPLE')
R['N0451']['additions'].append(dict(code='TC_RL',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE',quote=ln('N0451',11),reason='探索真机RL等后训练方法明确。'))
for e in ['O1','O2']:ov('N0621',e,'等框架没有任选。',branch='EXAMPLE')
ov('N0621','O13','数据处理支持模型评估，不是本人评估执行。',metric='SEPARATE',branch='SUPPORTED_EVALUATION_OBJECT')
for e in ['O23','O24','O25']:ov('N0621',e,'仿真平台上位类使用经验明确，示例仅下层品牌。',branch='UNCONDITIONAL')
ov('N0621','2:0','仅跟踪Agent前沿，未明使用Agent工作流。',metric='SEPARATE',branch='BACKGROUND')
ov('N0621','3:0','世界模型、因果推理等原句实际上并列无示例词。',branch='UNCONDITIONAL')
ov('N0621','O21','世界模型泛称不自动证明基础模型或大规模预训练模型。',metric='SEPARATE',branch='WORLD_MODEL_ONLY')
for e in ['O1','1:0','1:1','2:0','2:1','2:2','2:3','8:0','11:0','O8','18:0','19:0','19:1','O9','O10','O11','20:0','20:1']:ov('N0618',e,'内部不同工具/技术斜线未解，外层至少几项不解析内部斜线。',branch='UNRESOLVED')
for e in ['O7','O21']:ov('N0618',e,'实时系统句整体为熟悉某方案或有开发经验者优先；不提升为硬性。',metric='PREFERRED',branch='CHOICE')
for e in ['O25','O26','O27']:ov('N0618',e,'仿真平台上位明确，外层加分至少一项为任选，品牌示例不传播到上位。',branch='CHOICE')
for e in ['O6','O7','O8','O9','O10']:ov('N0646',e,'参与/协助/配合明确，保留辅助承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O15','O16']:ov('N0646',e,'强烈兴趣不是技术知识能力要求。',metric='SEPARATE',branch='INTEREST')
register(list(R.values()),'Astra_v3_boundary_ml_e')
