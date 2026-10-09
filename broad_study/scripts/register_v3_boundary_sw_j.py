from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0261':'双段任职原样保留；至少一门解除语言候选关系未知，Agent职责与优先经历补齐。',
'E0239':'本体WebUI/BFF；服务开发使用Node，不是开发Node；参与基建与本人工作分开。',
'E0238':'客户定制嵌入式开发，Linux和评测要求改用任职证据，具体仪器为示例。',
'E0235':'遥操集成与验证框架；参与实时平台、视觉链路区分，工业总线了解为一般要求。',
'E0211':'机器人云平台，Spark/ClickHouse属于加分且关系不同。',
'E0191':'本体容器运行时，Linux知识明确，嵌入式/系统经验关系未解。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
for e in ['O2','O3','O4']:ov('E0261',e,'等至少一门明确任选加示例，而非裸斜线。',branch='CHOICE_AND_EXAMPLE')
ov('E0261','O11','一般要求改锚真实资格F12，原为职责。',metric='GENERAL',quote=ln('E0261',12))
for e in ['O12','O13']:ov('E0261',e,'LLM/VLA是上层大模型的例子，上层类别明确要求。',branch='UNCONDITIONAL')
add('E0261','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL',3,'明确Agent架构研发。')
add('E0261','V2_AGENT_WORKFLOW','PREFERRED','UNCONDITIONAL',11,'有Agent落地项目开发经验者优先。')
ov('E0239','O1','ROS/rosbridge均ROS生态但通信工具以等列举。',branch='EXAMPLE')
ov('E0239','O4','Node.js BFF、设备服务或实时网关明确或。',branch='CHOICE')
for e in ['O5','2:0']:ov('E0239',e,'参与自动化测试/CI建设保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0239','O6','地图、模型或实时数据可视化经验明确任选。',branch='CHOICE')
ov('E0239','1:0','用Node开发BFF服务，且服务类别明确或。',metric='DUTY_OWN_USE',branch='CHOICE')
for e in ['3:0','3:1']:ov('E0239',e,'本句MySQL/PostgreSQL裸斜线未解，F19明确或证据另存。',branch='UNRESOLVED')
ov('E0239','6:0','React与其他技术以等列举，F12明确React另存。',branch='EXAMPLE')
for e in ['O2','O3']:ov('E0238',e,'仪器熟练使用明确，但以等列举。',branch='EXAMPLE')
ov('E0238','O4','一般Linux资格改锚F10，原引用职责。',metric='GENERAL',quote=ln('E0238',10))
ov('E0238','O11','一般测试用例撰写能力改锚F13，原为职责。',metric='GENERAL',branch='EXAMPLE',quote=ln('E0238',13))
ov('E0238','O8','明确集成电机外设，属于本人实际使用而非背景。',metric='DUTY_OWN_USE',branch='EXAMPLE')
add('E0238','TC_DATA_PIPELINE','DUTY_OWN_DEVELOP','EXAMPLE',4,'本人开发数据采集链路，业务模块以等列举。')
for e in ['O6','2:0']:ov('E0235',e,'参与平台架构及设备链路设计保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['5:0','5:1']:ov('E0235',e,'了解工业总线为一般要求，EtherCAT/CANopen裸斜线未解。',metric='GENERAL',branch='UNRESOLVED')
ov('E0211','O9','自动调度任务中训练属于如的示例。',branch='EXAMPLE')
for e in ['O12','O13','O14','O15']:ov('E0211',e,'优先平台清单兼有或与等。',branch='CHOICE_AND_EXAMPLE')
ov('E0211','2:0','加分段Hadoop/Spark裸斜线未解。',metric='PREFERRED',branch='UNRESOLVED')
ov('E0211','2:1','加分段OLAP引擎以等列举且与前半句或。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('E0191','O3','嵌入式/边缘修饰Linux，Linux本身并不在任选中。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_sw_j')
