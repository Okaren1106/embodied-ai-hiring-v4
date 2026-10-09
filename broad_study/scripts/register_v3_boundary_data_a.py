from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0404':'VLM自动标注：两种数据建设经验同数据上位，RLHF为微调技术例示；本人微调与协同迭代区分。',
'N0510':'导航自动标注：MCAP与ROS同属加分数据生态举例；CV/数据算法年限未知不污染另句明确建设经验。',
'N0316':'具身数据：职责内熟悉不误记任职要求；支持/参与训练评估单列，遥操来源与加分任选区分。',
'N0214':'湖仓：语言明确至少一门；计算引擎仅举例没有任选，目录外湖仓产品不擅自加目录。',
'N0430':'分布式数据：C++/Rust与Kafka/RabbitMQ斜杠未解；S3兼容对象存储不自动认定AWS。',
'N0407':'运营指标：Python/SQL明确，Docker等为加分工具举例；CI/CD本身是流程要求。',
'N0487':'数据算法：回读满足其一即可父语境，Unity/Unreal及Sim2Real属于一般分支而非加分；模型架构上位与具体软件分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O13','O14']:ov('N0404',e,'自动标注系统或数据流水线同数据上位。',branch='UNCONDITIONAL')
ov('N0404','O10','SFT、RLHF等微调技术中RLHF为RL例示。',branch='EXAMPLE')
ov('N0510','1:0','与ROS等数据生态同列举。',branch='EXAMPLE')
ov('N0316','O11','探索仿真生成数据来源，不等于本人开发生成器。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for e in ['O16','O35']:ov('N0316',e,'明确支持模型评估/benchmark，非独立承担。',metric='SEPARATE',branch='SUPPORT')
ov('N0316','O17','熟悉训练流程位于职责部分，不作为任职资格独立证据。',metric='SEPARATE',branch='DUTY_KNOWLEDGE_DESCRIPTION')
ov('N0316','O34','明确理解并参与模型训练。',metric='SEPARATE',branch='PARTICIPATION')
for e in ['1:0','2:0']:ov('N0316',e,'如/多源等为遥操采集途径例示。',branch='EXAMPLE')
ov('N0316','4:0','遥操数据或人类演示数据不保证都是遥操。',branch='CHOICE')
for e in ['2:0','2:1']:ov('N0214',e,'Spark/Flink等为例示，无任选词。',branch='EXAMPLE')
for e in ['O2','O3','4:0']:ov('N0430',e,'仅斜杠未明确任选还是兼具，保留未知。',branch='UNRESOLVED')
R['N0430']['catalog_gap_notes']=['S3在此仅对象存储协议/生态称呼，未写AWS平台，不能把兼容S3部署推成AWS；目录外RabbitMQ保留原文。']
ov('N0407','O3','Docker等工具是例示。',branch='EXAMPLE')
for e in ['O3','O4']:ov('N0487',e,'IsaacSim/Lab同Isaac上位，外层可选仿真方向且平台or/等。',branch='CHOICE_AND_EXAMPLE')
ov('N0487','O14','基于生成模型开发增强方案，未写开发模型本身。',metric='DUTY_OWN_USE')
for e in ['O20','O21','O22','O23','O24','O25']:ov('N0487',e,'算法基础满足其一，数据挖掘/生成方法属ML上位的可选分支。',branch='CHOICE')
for e in ['O30','O31']:ov('N0487',e,'Diffusion与视频生成模型同ML模型上位；外层与3D重建or。',branch='CHOICE')
for e in ['4:0','4:1']:ov('N0487',e,'实际一般能力仿真方向内，工具斜杠尚未明确。',metric='GENERAL',branch='UNRESOLVED')
ov('N0487','4:2','算法基础任选方向中一般要求，不是加分。',metric='GENERAL',branch='CHOICE')
ov('N0487','7:0','机器人操作/遥操作数据关系未明，外层有其他来源or。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['PREFERRED','PREFERRED_CHOICE'])
ov('N0487','8:0','NeRF和Gaussian同重建表示，上层与模型经验任选，括号具体表示举例。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_data_a')
