from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0440':'并列框架等为示例，没有任选关系；专业学位不外推必须掌握所有算法。',
'N0421':'框架本人开发与参与轻量框架建设区分；RL等模块保留示例。',
'N0413':'VLA操纵预训练职责明确，后训练仅任职经验；RL在等方向列表。',
'N0412':'逐条修正错误原文锚点、参与承担、技术栈示例与真正任职要求的区别；未知斜线逐项保留。',
'N0401':'平台化推理部署；优先了解Orin架构不等于CUDA优先，另有真实CUDA优先证据。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
for e in ['O4','O5','O6']:ov('N0440',e,'等为示例，原文没有任选。',branch='EXAMPLE')
for e in ['O3','O4']:ov('N0421',e,'RL、模型精调等是核心模块示例。',branch='EXAMPLE')
ov('N0421','O5','参与框架用于支持模型微调部署，不证明本人模型使用。',metric='SEPARATE',branch='SUPPORTED_MODEL_OBJECT')
ov('N0421','O6','本人核心模块设计开发另有明确职责，以该句代替参与构建证据。',metric='DUTY_OWN_DEVELOP',quote=line('N0421',2))
ov('N0413','O7','RL处于等方向示例内。',branch='EXAMPLE')
for e in ['O2','O3']:ov('N0412',e,'框架之一明确任选，等同时保留示例。',branch='CHOICE_AND_EXAMPLE')
for e in ['O5','O6','O7']:ov('N0412',e,'不同工具斜线关系未解，未知优先于等示例。',branch='UNRESOLVED')
for e in ['O10','O11','O12']:ov('N0412',e,'原锚点是加分项；技术栈非限制示例另作提及，不能重复变成一般要求。',metric='SEPARATE',branch='ILLUSTRATIVE_TECH_STACK',quote=line('N0412',65))
ov('N0412','O15','正文明确参与设计，不保证本人独立研发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0412','O17','RL policy属于如所引的对接控制系统示例。',branch='EXAMPLE')
ov('N0412','O20','参与构建数据属于协作；本人数据采集另有明确句。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O22','O23','3:0']:ov('N0412',e,'学习策略列表仅斜线，无明确任选/全要语义。',branch='UNRESOLVED')
ov('N0412','O25','与各团队协作建立benchmark，不证明本人独立评测体系开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0412','O27','原锚点落到职责；改用任职至少一项下的RL/IL句，内部斜线仍未知。',metric='GENERAL',branch='UNRESOLVED',quote=line('N0412',42))
for e in ['O30','O31']:ov('N0412',e,'改用真正任职VLM/多模态模型句，类内斜线不改变上位模型，至少一项祖先为任选。',metric='GENERAL',branch='CHOICE',quote=line('N0412',44))
ov('N0412','O32','WBC/motion tracking关系未解，不把理解或参与过误作方法任选。',branch='UNRESOLVED')
for e in ['O35','O36','O37']:ov('N0412',e,'改用真正加分研究经历句；VLA/VLM/世界模型/Foundation Model同属此继承上位类别。',metric='PREFERRED',branch='UNCONDITIONAL',quote=line('N0412',60))
ov('N0412','6:0','原锚点跟踪前沿为职责；改用加分研究经历句，跨具体模型类型斜线未解。',metric='PREFERRED',branch='UNRESOLVED',quote=line('N0412',60))
for e in ['O38','O39','O40','O41','O42','O43','O44','O47','8:0','11:0','12:0','ADD1']:ov('N0412',e,'技术栈示例非限制单列描述，没有要求熟悉/使用或职责承担断言。',metric='SEPARATE',branch='ILLUSTRATIVE_TECH_STACK')
for e in ['O45','O46']:ov('N0412',e,'真正技术栈示例在F66；旧职责对接句不能充当一般要求。',metric='SEPARATE',branch='ILLUSTRATIVE_TECH_STACK',quote=line('N0412',66))
R['N0412']['additions'].append(dict(code='TC_DATA_PIPELINE',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote=line('N0412',19),reason='设计并实现统领的真机数据采集与回放是本人明确数据建设职责。'))
ov('N0401','O3','至少一套仅外层任选，TensorRT/CUDA内部斜线仍未解。',branch='UNRESOLVED')
ov('N0401','9:0','TensorRT/CUDA内部斜线未解，未知优先。',branch='UNRESOLVED')
ov('N0401','O4','原先Orin架构优先非CUDA；改用明确GPU API任一的加分句。',metric='PREFERRED',branch='CHOICE',quote=line('N0401',23))
ov('N0401','9:1','量化属于任选RKNN体系内，无示例词。',branch='CHOICE')
for e in ['O17','O19','14:0']:ov('N0401',e,'SLAM/标定跨类别斜线未解。',branch='UNRESOLVED')
ov('N0401','O20','隐私、权限和脱敏为信息安全，未明产品/系统/作业安全目标。',metric='SEPARATE',branch='INFORMATION_SECURITY')
ov('N0401','O21','端侧Linux/QNX和驱动经验未明嵌入式/固件/微控制器，保留系统语境。',metric='SEPARATE',branch='EDGE_SYSTEM_CONTEXT')
for e in ['22:0','22:1']:ov('N0401',e,'等任一同时标明示例和任选。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_ml_b')
