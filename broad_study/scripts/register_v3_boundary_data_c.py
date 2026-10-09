from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0072':'大数据引擎：技术栈和存储系统为等举例；质量监控加分从任职要求定位，协作模型应用单列。',
'E0065':'数据模型：VLM/VLA同基础模型上位；框架具体版本未知但深度学习框架上位明确，vibe coding不猜品牌。',
'E0297':'多模态真值：具体任务任一或多项影响职责分支；数据处理上位资格明确，Pandas如举例。',
'E0162':'机器人数据平台：Python/Go双栈明确双方加分；存储和计算栈斜杠未解，标定管理在加分栏。',
'E0118':'另一多模态真值广告：同样任一任务分支，评估职责不再误引项目总述；Pandas例示。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['1:0','1:1','1:2','2:0']:ov('E0072',e,'技术栈/存储等列举，无任选词。',branch='EXAMPLE')
ov('E0072','O8','与算法团队深度协作转化模型预测能力。',metric='SEPARATE',branch='COLLABORATION')
ov('E0072','O13','原误引职责，改任职加分数据质量监控句。',metric='PREFERRED',branch='CHOICE',quote='6. 有机器学习数据 pipeline、MLOps或数据质量监控体系建设经验者优先。')
R['E0065']['additions'].append(dict(code='SK_GENERIC_ML_FRAMEWORK',metric='GENERAL',branch='UNCONDITIONAL',quote='熟悉PyTorch/TensorFlow等深度学习框架',reason='框架上位明确，具体工具斜杠仍未知。'))
R['E0065']['catalog_gap_notes']=['明示熟练vibe coding工具，未点名品牌，不补任何AI编程软件。']
for r in ['E0297','E0118']:
 ov(r,'O5','具体涉及以下任一或多项，数据处理流程是分支职责。',branch='CHOICE')
 ov(r,'O6','任一或多项第三条的本人数据评估使用；不引用项目总述。',metric='DUTY_OWN_USE',branch='CHOICE',quote='3. 系统性地评估数据的集中、离散程度和形状特征，使用高维数据降维技术 (PCA, t-SNE等) 可视化和量化潜在的流形结构和数据的内在维度。')
 ov(r,'2:0','如Pandas/NumPy等仅例示。',branch='EXAMPLE')
ov('E0297','O8','旧误引职责；清洗/标注/统计均数据处理上位，一般要求成立。',metric='GENERAL',branch='UNCONDITIONAL',quote='1、了解多模态大模型范式，熟悉多模态数据的清洗/标注/统计方式，对数据在训练中的作用和大模型能力边界有深刻理解。')
for e in ['O17','O18','O19','O20']:ov('E0162',e,'所有任选经验都属于数据管道上位。',branch='UNCONDITIONAL')
ov('E0162','1:0','支持rosbag等多个数据类型，格式为例示。',branch='EXAMPLE')
for e in ['4:0','4:1','4:2','5:0','5:1']:ov('E0162',e,'具体产品斜杠关系没有明确任选，保留未知。',branch='UNRESOLVED')
for e in ['O8','5:2']:ov('E0162',e,'上层数据库/存储/消息/调度or，内层如产品例示。',branch='CHOICE_AND_EXAMPLE')
ov('E0162','7:0','标定管理在加分项。',metric='PREFERRED')
register(list(R.values()),'Astra_v3_boundary_data_c')
