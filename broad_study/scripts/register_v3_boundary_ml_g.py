from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0085':'逐项区分实际用仿真、算法研发、协作感知与要求示例；策略蒸馏明确纳入目录。',
'N0071':'具身RL后训练自研明确；共同建设数据评测另列协作，偏好经验可任选。',
'N0149':'VLA和世界模型并列本人研发，工具框架斜线未知；括号工具无示例词。',
'N0030':'27届人体模型原文独立核对，技术经验与仿真/论文任选保留。',
'N0035':'工业RL协助岗位，所有协作技术对象仍可在提及层分析，不当成独立研发责任。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
for e in ['O1','O2']:ov('N0085',e,'平台并列加等，无任选。',branch='EXAMPLE')
for e in ['O7','O8']:ov('N0085',e,'与同句其他仿真软件同属或和等列表。',branch='CHOICE_AND_EXAMPLE')
ov('N0085','O20','与感知硬件等团队协作融合数据，保留协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O33','O34']:ov('N0085',e,'AMASS等与SMPL或SMPL-X同处任选和示例数据/模型清单。',branch='CHOICE_AND_EXAMPLE')
ov('N0085','O35','一般扩散模型原理不等于机器人生成式策略；后句优先经验另保留。',metric='SEPARATE',branch='GENERIC_GENERATIVE_MODEL')
for e in ['O38','O39','O40','O41']:ov('N0085',e,'仿真平台上位要求明确，任选示例只限制品牌。',branch='UNCONDITIONAL')
add('N0085','V2_MODEL_COMPRESSION','DUTY_OWN_DEVELOP','UNCONDITIONAL',7,'研究多技能策略蒸馏明确。')
add('N0085','V2_MODEL_COMPRESSION','PREFERRED','CHOICE',24,'多技能蒸馏为优先经验任选之一。')
for e in ['O10','O11']:ov('N0071',e,'与多个团队紧密合作完善闭环和建立评测，保留共同承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O14','O15','O16','O17','O18']:ov('N0071',e,'等方向中的一种或多种同时为任选与示例。',branch='CHOICE_AND_EXAMPLE')
ov('N0071','O35','RL/distributed rollout内部斜线未解，不确定是否分布式ML系统经验。',branch='UNRESOLVED')
for e in ['O1','O2']:ov('N0149',e,'PyTorch/TensorFlow斜线无任选解释。',branch='UNRESOLVED')
for e in ['2:0','4:0','4:1']:ov('N0149',e,'括号无示例词或任选词。',branch='UNCONDITIONAL')
ov('N0030','O8','实际测试确保稳定性属于可靠性目标应用，不证明开发可靠性方法。',metric='DUTY_OWN_USE')
for e in ['O4','O5','O6','O7','O8']:ov('N0035',e,'参与/协助/共同探索为明确协作承担，保留提及。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
register(list(R.values()),'Astra_v3_boundary_ml_g')
