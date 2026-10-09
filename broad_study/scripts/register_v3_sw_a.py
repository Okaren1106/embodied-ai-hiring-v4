from astra_review_tools import *
JUD={
'N0200':'数据平台全栈主责明确，Go或Python职责任选；辅助编码工具与数据生态例示保留，不能因框架多样推断全用。',
'N0406':'Java控制面后端及机器人Agent二开SDK，Go/Python资格斜线未知；明确Agent交付补工作流项，不把协作部署和主导或参与工具链当独立开发。',
'E0008':'嵌入式Linux SDK，C/C++未知但另句C明确；修复系统稳定性是本人动作，补宽可靠性目标。',
'E0098':'完整可见职责为APP/Web前端和开发组件，无具体目录工具；空候选仍全文核对，不补猜前端框架或AI模型。',
'N0393':'Golang后端独立负责，可靠性及安全相关优先语境明确；GitHub开源项目不自动推出Git。',
'N0504':'本人机器人软件涵盖控制和感知，独立正例应锚主责句；后面共同研发鲁棒性仍是协作。不同协议斜线未知，而嵌入式平台上位类明确。',
'N0511':'机器人Agent应用和任务编排系统，正文明确本人工具调用与记忆系统，补职责工作流。资格、加分与协作分开。',
'N0461':'参与Agent模块与本人基于模型API搭建智能体分开；测试评估体系建设为开发，非只执行测评。',
'N0473':'端侧应用集成，ROS/ROS2职责与要求均斜线未知；现场问题排查本人负责，协助项目交付不抹去明确排障。',
'N0633':'Qt上位机与测试辅助工具开发；Qt Widgets/QML同Qt家族，上位工具明确使用而非开发Qt本身。RS485代码冻结别名包含泛串口，不可把该代码统计直接命名物理RS485。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','O2']:ov('N0200',f'N0200:{e}','职责Go或Python明确任选。',branch='CHOICE')
ov('N0200','N0200:O5','SQL执行是等模块列表内例示。',branch='EXAMPLE')
add('N0406','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL','主要负责灵心平台的后端开发(机器人交互的控制面)，机器人Agent的二开SDK','明确本人负责机器人Agent软件开发工具包。')
add('E0008','TC_RELIABILITY','DUTY_OWN_DEVELOP','EXAMPLE','解决系统中的疑难问题，包括但不限于:稳定性、性能、功耗等','本人修复系统稳定性，例示目标。')
for e in ['O5','O6']:ov('N0504',f'N0504:{e}','原协作句不是独立证据；岗位首句明确本人软件涵盖控制和传感器融合。',metric='DUTY_OWN_DEVELOP',quote='负责足式机器人软件系统的设计与实现，覆盖运动控制、传感器融合、自主决策与人机交互。')
ov('N0504','N0504:O7','共同设计开发的目标是鲁棒性，按协作对象保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O10','O11','O12']:ov('N0504',f'N0504:{e}','所列厂商及MCU均为嵌入式开发，上位类不因子型斜线而未知。',branch='UNCONDITIONAL')
for e in ['N0504:6:0','N0504:6:1','N0504:6:2','N0504:6:3','N0504:16:0','N0504:16:1']:ov('N0504',e,'不同协议或工具直接斜线关系未解，不猜并列或任选。',branch='UNRESOLVED')
add('N0511','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL','基于大模型能力实现工具调用、任务拆解、技能编排和多轮任务推理，提升复杂任务执行效果。','明确本人Agent应用和工具调用工作流实现。')
for e in ['N0461:1:0','N0461:5:0']:ov('N0461',e,'参与应用或模块研发不是本人独立责任，其他独立搭建句另保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0461','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL','基于 OpenAI、Claude、Gemini 或国产大模型 API 搭建智能体能力','基础模型供应商可任选但搭建Agent能力本身明确。')
ov('N0461','N0461:O3','建设测试评估体系是明确产出，不仅执行既有评测。',metric='DUTY_OWN_DEVELOP')
for e in ['O1','O2']:ov('N0473',f'N0473:{e}','ROS/ROS2斜线关系未解，与资格段同规则。',branch='UNRESOLVED')
for e in ['O8','O9','O10']:ov('N0473',f'N0473:{e}','包括及等列出的集成模块是例示。',branch='EXAMPLE')
for e in ['N0473:8:0','N0473:8:1','N0473:8:2']:ov('N0473',e,'等常用开发工具为例示。',branch='EXAMPLE')
ov('N0473','N0473:2:0','等一种或多种同时具有开放例示与任选。',branch='CHOICE_AND_EXAMPLE')
ov('N0473','N0473:2:1','TCP/UDP均属于冻结TCPIP协议家族，上位关系已解；外层一种或多种且等。',branch='CHOICE_AND_EXAMPLE')
add('N0473','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','负责机器人端软件的部署、配置、升级及现场问题排查','本人现场问题排查明确。')
ov('N0633','N0633:O1','Linux/Windows不同系统斜线未解。',branch='UNRESOLVED')
for e in ['N0633:2:0','N0633:3:0']:ov('N0633',e,'Widgets或QML都使用Qt家族能力；交付应用界面不是开发Qt工具。',metric='DUTY_OWN_USE',branch='UNCONDITIONAL')
ov('N0633','N0633:4:2','串口列于等协议例示，代码按冻结别名涵盖串口，不猜物理RS485。',branch='EXAMPLE')
ov('N0633','N0633:13:3','至少一种的串口属于冻结代码别名，按明确任选；不能由该编码推出特定RS485标准。',branch='CHOICE')
register(list(R.values()),'Astra_v3_sw_a')
