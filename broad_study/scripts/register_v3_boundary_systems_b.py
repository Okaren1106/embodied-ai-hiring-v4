from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0366':'功能安全系统岗：Jama为使用，方法能力与具体工具例示分开；修复要求证据误引职责，补独立需求分解与接口定义。',
'E0320':'首席安全：本人创建安全交付与监督外部实验室区分，合规团队协作分开；标准知识上位可成立，实验室管理不等于本人测试执行。',
'N0820':'实景捕获：PTP是使用而非开发协议，热像例示；危险区认证处在加分段，资料处理工作保留其真实对象。',
'N0774':'联邦安全岗：一般PLC能力确有漏标；标准处在Extras，ROS斜杠未知不硬解，C++括号例示。',
'N0734':'安全总监：补读全部全文，监督现场事件不等于本人技术排障；安全职责与领导要求不得错用开头公司介绍。',
'N0827':'传感器系统：本人校准、监测校准状态和开头contribute分开；复核全部总线例示并补一般要求，采购原文明示。',
'N0835':'联邦传感器同系列独立原文：校准、开发QA、采购责任明确；总线和时间协议例示，ROS斜杠保留未知。',
'N0810':'机器人集成：协作机械电气与本人适配策略不同；SIL/HIL斜杠未知，安全测试凭实际内容，任选控制与遥操不能无条件。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','O2','5:0','5:1','5:2','5:3']:ov('E0366',e,'括号列举/e.g.为示例，无任选词。',branch='EXAMPLE')
for e in ['O8','O10']:ov('E0366',e,'选项均具安全属性，上位安全知识不因下位任选而消失。',branch='UNCONDITIONAL')
for e in ['O9','O12']:ov('E0366',e,'原引用职责，改实际技能要求。',metric='GENERAL',branch='UNCONDITIONAL',quote='Expert-level skills in authoring safety requirements, managing traceability, and defining cross-functional safety interfaces')
ov('E0366','1:0','在Jama中编写需求，未开发Jama工具。',metric='DUTY_OWN_USE')
add('E0366','V2_REQUIREMENTS_ENGINEERING','DUTY_OWN_DEVELOP','UNCONDITIONAL','Define, own, and decompose detailed, verifiable requirements in Jama','独立定义与分解可验证系统需求。')
ov('E0320','O6','监督第三方实验室V&V不是本人执行测试。',metric='SEPARATE',branch='MANAGED_TEST_ACTIVITY')
ov('E0320','2:0','创建安全分析交付是应用分析方法，未开发分析方法。',metric='DUTY_OWN_USE')
ov('E0320','3:0','监督外部实验室认证工作。',metric='SEPARATE',branch='MANAGED_TEST_ACTIVITY')
for e in ['4:0','4:1']:ov('E0320',e,'Coordinate with compliance team属于协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0320','8:0','加分经验包括on-site troubleshooting等任选列举。',branch='CHOICE_AND_EXAMPLE')
add('E0320','TC_EVALUATION','DUTY_OWN_DEVELOP','EXAMPLE','Create and maintain core safety deliverables: risk assessments, safety requirement specifications (SRS), FMEDA, SISTEMA analyses, validation plans, and safety cases.','本人创建验证计划明确，区别于监督外部测试。')
for e in ['1:0','4:0']:ov('N0820',e,'传感器示例，不是无条件热像。',branch='EXAMPLE')
ov('N0820','5:0','PTP作为同步手段，不开发协议。',metric='DUTY_OWN_USE',branch='EXAMPLE')
ov('N0820','5:1','Own calibration为执行/负责标定，没有明确开发标定方法。',metric='DUTY_OWN_USE')
ov('N0820','14:0','What Will Set You Apart中危险区标准括号例示。',metric='PREFERRED',branch='EXAMPLE')
add('N0820','V2_THERMAL_CAMERA','PREFERRED','CHOICE_AND_EXAMPLE','Direct experience with sensors such as LiDAR, gas detection, thermal imaging, or PTZ camera systems.','加分传感器例示含热像且or任选。')
for e in ['7:0','9:0']:ov('N0774',e,'Extras段是加分标准能力，上位标准目录仍明确。',metric='PREFERRED')
ov('N0774','O3','software interfaces括号例示。',branch='EXAMPLE')
add('N0774','V2_PLC','GENERAL','UNCONDITIONAL','Deep, hands-on expertise in configuring, programming, and debugging Safety PLCs.','一般PLC技能明确，旧候选未纳入。')
ov('N0734','O11','开头产品安全介绍不是任职要求，该句应归本人安全领导职责。',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL')
ov('N0734','O9','Guide safety approaches监督可靠性对象，非本人实现容错系统。',metric='SEPARATE',branch='MANAGED_TECHNICAL_OBJECT')
ov('N0734','O14','领导机电软件产品系统安全不等于机械设计经验。',metric='SEPARATE',branch='SAFETY_APPLICATION_OBJECT')
ov('N0734','1:0','标准e.g.明示列举。',branch='EXAMPLE')
ov('N0734','6:0','全文明确Provide executive oversight，不是本人现场技术响应。',metric='SEPARATE',branch='MANAGED_INCIDENT_ACTIVITY')
for r in ['N0827','N0835']:
 for n in range(5):ov(r,'2:'+str(n),'electrical括号列举总线。',branch='EXAMPLE')
 for e in ['20:0','20:1','25:0']:ov(r,e,'时间协议/仿真环境括号示例，无任选词。',branch='EXAMPLE')
 ov(r,'1:0','开头contribute为参与，后文独立标定另有证据。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
 ov(r,'10:0','监测calibration status不同于执行标定。',metric='SEPARATE',branch='MONITORED_OBJECT')
 ov(r,'O28' if r=='N0827' else 'O25','Develop QA checks是本人开发质检方法。',metric='DUTY_OWN_DEVELOP')
 ov(r,'8:0','EMI noise在指标括号例示。',branch='EXAMPLE')
 ov(r,'O2' if r=='N0827' else 'O1','ROS nodes为软件集成内容括号例示。',branch='EXAMPLE')
 for c in ['V2_USB','V2_ETHERNET','V2_GMSL','V2_CAN','V2_I2C']:add(r,c,'GENERAL','EXAMPLE','Experience with protocols such as USB, Ethernet, GMSL, CAN, I2C, and CSI.','一般要求总线明示，旧证据仅职责不足。')
 add(r,'V2_PROCUREMENT','DUTY_OWN_USE','UNCONDITIONAL','Work with vendors to procure sensors.','与供应商采购传感器明确交易职责，区别于仅技术对接。')
for e in ['O1','O2']:ov('N0810',e,'such as ROS/ROS2斜杠关系未解。',branch='UNRESOLVED')
for e in ['O3','O4','O5']:ov('N0810',e,'simulation括号工具示例。',branch='EXAMPLE')
for e in ['O18','O19']:ov('N0810',e,'Work with mechanical and electrical engineers协作设计集成。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0810','3:0','SIL/HIL的斜杠关系未解，不能单独肯定HIL。',branch='UNRESOLVED')
ov('N0810','3:1','SIL此处软件在环，安全验证由下一句明确测试安全特征支持，不由SIL同名推出。',metric='DUTY_OWN_USE',quote='Test features such as safety features and operations under different Operational Design Domains (ODDs).',branch='EXAMPLE')
ov('N0810','4:1','实施安全层不是安全分析/验证方法，相关测试已有独立证据。',metric='SEPARATE',branch='SAFETY_IMPLEMENTATION_OBJECT')
for e in ['14:0','14:1','16:0']:ov('N0810',e,'明确or连接备选经验。',branch='CHOICE')
for e in ['8:0','8:1']:ov('N0810',e,'or similar同时表示任选及例示。',branch='CHOICE_AND_EXAMPLE')
add('N0810','V2_PROCUREMENT','DUTY_OWN_USE','UNCONDITIONAL','Identify, procure, test, and integrate diverse new robotic systems.','新机器人采购为本人明确责任。')
register(list(R.values()),'Astra_v3_boundary_systems_b')
