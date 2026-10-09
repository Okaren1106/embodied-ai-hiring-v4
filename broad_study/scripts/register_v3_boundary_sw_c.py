from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0405':'云端音视频，Go/C++之一明确任选，可观测工具斜线未解；开源贡献渠道不足推Git使用。',
'N0390':'平台网关；愿转Go不是已具备Go，一般与优先经验分开。',
'N0452':'智能体应用，参与模块与本人搭建能力、建设评测体系分开。',
'N0483':'基于ROS2/DDS的中间件软件；工具基于使用和协议本体开发分开。',
'N0455':'机器人端集成，ROS斜线同样影响职责用途；工具列表保留等和一种或多种。',
'N0448':'系统研发实习，明确协助/参与不升级独立承担，Shell编脚本属于语言使用。',
'N0634':'交互应用架构与验证，技术供应商接入不作采购专业能力；C/C++保留未知。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('N0405','O4','音视频或实时通信经验明确任选。',branch='CHOICE')
for e in ['21:0','21:1']:ov('N0405',e,'Prometheus/Grafana/ELK不同工具之间斜线未解。',branch='UNRESOLVED')
ov('N0390','O1','熟悉Go即优先，不因允许其他语言而把优先项拆成任选。',branch='UNCONDITIONAL')
ov('N0390','O2','有其他语言且愿转Go不要求已掌握Go，一般要求正例撤回。',metric='SEPARATE',branch='WILLINGNESS_TO_LEARN')
for e in ['O3','O4','13:0']:ov('N0390',e,'原文列举以等结尾。',branch='EXAMPLE')
ov('N0390','O5','参与核心能力建设，保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0452','O3','建设评测体系明确开发评测方法。',metric='DUTY_OWN_DEVELOP')
for e in ['1:0','5:0']:ov('N0452',e,'参与模块开发，保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0452','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'明确基于模型API搭建智能体能力。')
ov('N0483','O1','ROS 2 / DDS不同类别斜线未解。',branch='UNRESOLVED')
ov('N0483','1:0','基于协议开发通信中间件，不是开发DDS协议；斜线未解。',metric='DUTY_OWN_USE',branch='UNRESOLVED')
for e in ['O1','O2']:ov('N0455',e,'职责ROS/ROS2斜线未解。',branch='UNRESOLVED')
for e in ['O8','O9','O10']:ov('N0455',e,'集成模块明确包括且以等结尾。',branch='EXAMPLE')
ov('N0455','O11','维护应用保障稳定，未明开发可靠性机制。',metric='DUTY_OWN_USE')
for e in ['2:0','2:1']:ov('N0455',e,'一种或多种及等共同作用。',branch='CHOICE_AND_EXAMPLE')
for e in ['8:0','8:1','8:2']:ov('N0455',e,'开发工具列表以等结尾。',branch='EXAMPLE')
for e in ['O1','O2','O8','O9','3:0']:ov('N0448',e,'职责明确参与或协助，保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0448','O3','使用语言编写工具，语言列举含等。',branch='EXAMPLE')
ov('N0448','5:0','用Shell编写脚本是语言使用，含等但无任选。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for e in ['O5','O6','7:0','7:1']:ov('N0448',e,'至少一种与如同时修饰具体语言。',branch='CHOICE_AND_EXAMPLE')
ov('N0448','O7','语言上层类别本身明确要求。',branch='UNCONDITIONAL')
ov('N0634','O6','导航为语音应用业务场景例子，保留示例。',branch='EXAMPLE')
for e in ['O8','O9','O10','O11']:ov('N0634',e,'其他主流嵌入式GUI框架明确上层类别，具体框架才任选。',branch='UNCONDITIONAL')
ov('N0634','O13','动作/导航不同技术类别斜线未解。',branch='UNRESOLVED')
for e in ['1:0','2:0']:ov('N0634',e,'SDK技术接入与评估没有询报价/寻源/谈判/供货管理证据。',metric='SEPARATE',branch='TECHNICAL_VENDOR_INTERFACE')
add('N0634','V2_C','GENERAL','UNRESOLVED',13,'C/C++显式C但关系未解，不作零提及。')
register(list(R.values()),'Astra_v3_boundary_sw_c')
