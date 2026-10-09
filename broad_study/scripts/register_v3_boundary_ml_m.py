from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0217':'后训练场景交付，修正基础模型一般与优先要求引用职责的问题，验证为使用。',
'E0209':'灵巧操作策略、仿真与合成数据自研；评估策略为执行，动力学辨识是明确方法。',
'E0208':'移动操作学习策略本人研发，学习方法等示例与实际要求分开。',
'E0206':'补读全文核对短广告：优先灵巧手/真机部署原句定位，参与式职责独立保留。',
'E0195':'分层操作与控制框架，修正一般与优先要求引用职责的多处定位；技术方法等为示例。',
'E0175':'移动操作大模型，修正任职证据错引、世界模型背景和GitHub目录边界。',
'E0169':'独立核对产品落地版本；团队评测资源不是任职要求，本人后训练与协作转化区分。',
'E0168':'触觉强化微调与控制协同；RL/IL职责明确任选，补后训练和蒸馏具体目录项。',
'E0167':'触觉表征与具身模型融合任务，参与快慢架构和评测不推独立承担，修正优先操作证据位置。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('E0217','O7','实际功能验证为评测执行。',metric='DUTY_OWN_USE')
for e in ['O10','O11']:ov('E0217',e,'VLA或具身大模型同类别；引用真正要求句。',metric='GENERAL',branch='UNCONDITIONAL',quote=ln('E0217',12))
ov('E0217','O15','优先要求引用F19，不能引用职责。',metric='PREFERRED',branch='UNCONDITIONAL',quote=ln('E0217',19))
ov('E0217','4:0','微调/后训练关系未知，非明确任选。',branch='UNRESOLVED')
ov('E0209','O13','评估运动策略是执行评测，不是开发评测体系。',metric='DUTY_OWN_USE')
ov('E0209','O19','一般仿真要求改引真正熟悉仿真环境句。',metric='GENERAL',quote=RAW[RID['E0209']]['requirements'].splitlines()[4])
add('E0209','V2_SYSID','DUTY_OWN_USE','EXAMPLE',3,'包括动力学辨识，为仿真环境构建中应用的方法。')
for e in ['O8','O9']:ov('E0208',e,'行为克隆、RL等方法为示例。',branch='EXAMPLE')
ov('E0208','O15','评估运动策略是评测执行。',metric='DUTY_OWN_USE')
for e in ['O19','O20']:ov('E0208',e,'改引真正任职学习方法熟悉句，非职责。',metric='GENERAL',quote=RAW[RID['E0208']]['requirements'].splitlines()[2])
for e in ['O3','O4','O5','O6','O7','O8','1:0']:ov('E0206',e,'明确参与研发，保留参与承担；不把整段写成独立开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0206','O9','改引优先灵巧手/真机部署经历句，斜线仍未知。',metric='PREFERRED',branch='UNRESOLVED',quote=ln('E0206',11))
for e in ['O8','O9','O10']:ov('E0195',e,'学习方法等为示例，Diffusion/Flow同属明确生成式策略上位。',branch='EXAMPLE')
ov('E0195','O18','任职理解轨迹生成才是要求证据，非D5研发职责。',metric='GENERAL',quote=ln('E0195',11))
ov('E0195','O20','改引任职架构如VLA、WAM或Transformer策略句。',metric='GENERAL',branch='CHOICE_AND_EXAMPLE',quote=ln('E0195',12))
ov('E0195','O25','改引高频控制或System0优先经验句。',metric='PREFERRED',branch='CHOICE',quote=ln('E0195',18))
ov('E0195','O29','改引优先DP/VLA/WAM多模态模型经验句，斜线未知。',metric='PREFERRED',branch='UNRESOLVED',quote=ln('E0195',20))
ov('E0175','O19','迁移验证为评测执行。',metric='DUTY_OWN_USE')
for e in ['O23','O24']:ov('E0175',e,'改引任职VLA、VLN或移动操作经验，不引用职责。',metric='GENERAL',branch='CHOICE',quote=ln('E0175',12))
ov('E0175','O34','改用任职熟悉仿真到真实环境部署调优过程，非数据建设职责。',metric='GENERAL',quote=RAW[RID['E0175']]['requirements'].splitlines()[6])
ov('E0175','2:0','完成虚实迁移验证为方法应用。',metric='DUTY_OWN_USE')
ov('E0175','3:0','跟踪世界模型前沿是背景，不是一般知识要求。',metric='SEPARATE',branch='BACKGROUND')
ov('E0175','5:0','明确后训练上位要求，SFT/DPO等仅子型示例。',branch='UNCONDITIONAL')
add('E0175','V2_GIT','PREFERRED','CHOICE',26,'冻结类别包括GitHub代码贡献协作；或开源项目经验为任选。')
ov('E0169','O11','本体功能验证为评测执行。',metric='DUTY_OWN_USE')
ov('E0169','O16','改用任职能完成真机验证句，团队资源不能充要求。',metric='GENERAL',quote=ln('E0169',16))
ov('E0169','4:0','与数据团队协作推动后训练转化为协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0169','6:0','微调/后训练斜线未知。',branch='UNRESOLVED')
for e in ['O5','O6']:ov('E0168',e,'强化微调、IL或策略优化为方法任选。',branch='CHOICE')
ov('E0168','O11','与团队协作完成实验验证，仅协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0168','O16','改用任职一种或多种学习方法句。',metric='GENERAL',branch='CHOICE',quote=ln('E0168',16))
add('E0168','V2_POSTTRAINING','DUTY_OWN_DEVELOP','CHOICE',6,'真机强化微调为后训练明确子型。')
add('E0168','V2_POSTTRAINING','GENERAL','CHOICE',16,'强化微调是要求方法之一。')
add('E0168','V2_MODEL_COMPRESSION','PREFERRED','CHOICE',25,'策略蒸馏明确优先任选。')
add('E0168','V2_CLASSICAL_CONTROL','GENERAL','EXAMPLE',17,'力控和阻抗等基本概念。')
add('E0168','V2_CLASSICAL_CONTROL','PREFERRED','CHOICE',26,'阻抗/导纳同属经典控制上位类，外层或为任选。')
ov('E0167','O4','操作策略、世界模型或动作模型中建模为任选应用对象。',branch='CHOICE')
for e in ['O7','O8']:ov('E0167',e,'参与架构和实验评估仅保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O11','O12','O13','O14']:ov('E0167',e,'等相关方法中的一种或多种同时示例与任选。',branch='CHOICE_AND_EXAMPLE')
ov('E0167','O15','改用优先机器人操作或多模态学习经验句，非职责。',metric='PREFERRED',branch='CHOICE',quote=ln('E0167',21))
register(list(R.values()),'Astra_v3_boundary_ml_m')
