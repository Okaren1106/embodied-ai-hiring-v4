from astra_review_tools import *
JUD={
'N0571':'Ego数据及真机评测基础设施；仿真和遥操是数据来源，福利段World Model不能当优先要求；LoRA符合冻结低秩适配定义。',
'N0101':'数据闭环主责和参与模型训练分开；Python/NumPy等并用关系未知，RLHF语境为必备要求，数据蒸馏不自动等模型压缩。',
'N0305':'数据采集场景与质量体系本人设计；库存数据库协助，不能记独立库存操作；补明确采集标准规范。',
'E0202':'采集团队运营与设备问题升级、精益流程优化均明示；班组管理不自动等专业招聘HR。',
'E0171':'触觉数据Infra而非控制算法；保留Python/C++与ROS/ROS2关系未知，不据触觉手套推遥操操作或动捕。',
'N0728':'数据平台工程，一般流工具与优先机器人格式分开；括号例示不随意改or，ROS/ROS2内部斜杠未知。',
'N0715':'数据标注产品规划与直接Build 0-1 data pipelines分别判断，重锚明确管线方案建设；原notes声称职责只有公司介绍不属实。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0571','O9','建设数据管理体系，仿真是数据来源，未明确本人仿真运行。',metric='SEPARATE',branch='DATA_SOURCE_OBJECT')
for e in ['O17','O25']:ov('N0571',e,'World Model本身不足以确定基础模型规模或预训练属性。',metric='SEPARATE',branch='UNSPECIFIED_FOUNDATION_MODEL')
ov('N0571','2:0','建立多源数据标准不等本人遥操或开发遥操系统。',metric='SEPARATE',branch='DATA_SOURCE_OBJECT')
for e in ['3:0','6:0']:ov('N0571',e,'等方向/经验列举。',branch='EXAMPLE')
ov('N0571','13:0','你将获得段属于发展机会，不是优先资格。',metric='SEPARATE',branch='DEVELOPMENT_OPPORTUNITY')
add('N0571','V2_MODEL_COMPRESSION','PREFERRED','EXAMPLE','熟悉 Transformers、LoRA、分布式训练、推理加速等技术','冻结定义明确包括低秩适配，不能以不是传统压缩排除LoRA。')
add('N0571','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','主导建立 UMI、遥操作、真机、仿真等多源机器人数据的标准化生产规范与评测体系','明确数据生产规范编制。')
for e in ['O2','O3','O4','O5','3:0','3:1']:ov('N0101',e,'斜杠内部并用或任选未明，不据工具列表确定。',branch='UNRESOLVED')
for e in ['O8','O9','O10','1:0']:ov('N0101',e,'负责训练大项下具体参与VLA训练，不能把其范式当本人独立开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O11','O12']:ov('N0101',e,'支持模型验证，属于协作对象。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O19','O20']:ov('N0101',e,'offline RL和RLHF均属强化学习上位，内部斜杠不取消上位RL明确性。',branch='EXAMPLE')
ov('N0101','2:0','RLHF在必备要求且与offline RL斜杠，后训练子项关系未解。',metric='REQUIRED',branch='UNRESOLVED')
for e in ['O21','O22']:ov('N0101',e,'pipeline或dataset均属于数据集/管线上位。',branch='UNCONDITIONAL')
ov('N0305','O1','协助搭建并维护物料数据库，不足以推独立库存操作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0305','O6','本人构建质量评估体系，非仅执行评估。',metric='DUTY_OWN_DEVELOP')
add('N0305','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立场景设计标准化流程，输出可落地的场景方案文档','明确采集场景规范。')
add('E0202','V2_LEAN','DUTY_OWN_USE','UNCONDITIONAL','用精益管理思路持续降本提效','明确应用精益方法。')
add('E0202','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','异常及时上报并推动快速修复，保障作业不停摆','采集设备运行异常升级与闭环。')
for e in ['8:0','15:0','15:1']:ov('N0728',e,'括号列举，无or关系。',branch='EXAMPLE')
ov('N0728','12:0','such as Airflow or Dagster，任选加例示。',branch='CHOICE_AND_EXAMPLE')
for e in ['25:0','25:1']:ov('N0728',e,'Extras段且such as ... or，优先双分支。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('N0715','O2','产品生命周期所有权原句不足，实际F8明确Build 0-1数据管线方案，重锚。',metric='DUTY_OWN_DEVELOP',quote='Build 0-1 solutions for large scale data pipelines')
register(list(R.values()),'Astra_v3_data_a')
