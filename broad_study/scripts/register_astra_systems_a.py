from astra_review_tools import *
ids=['N0595','E0125','E0101','E0035','N0438','N0078','N0443']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why,**v):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**v))
R['N0595']['judgment']='系统架构与稳定性目标有据，跟踪测试未明确实际执行。CAN/EtherCAT与ROS/Linux同为等示例；补明确需求分析经验任选，不从协调专业团队推本人设计全部模块。'
for eid in ['N0595:1:0','N0595:1:1']:ov('N0595',eid,'同句等示例，无或。',branch='EXAMPLE')
ov('N0595','N0595:O5','跟踪测试/调试不充分确认本人执行测试。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
add('N0595','V2_REQUIREMENTS_ENGINEERING','GENERAL','CHOICE','有项目管理或需求分析经验','明确需求分析经验与项目管理任选。')
R['E0125']['judgment']='工作主体为关节选型、系统集成、验证与诊断；不等同开发关节本体。供应商技术评审/整改是技术质量对象，缺少询报价/商务/供货流程，退出采购正例。修复指向职责段的一般/优先引文，补风险与实际运行故障工作。'
ov('E0125','E0125:O2','本人选型、集成关节模组，没有明示开发模组本体。',metric='DUTY_OWN_USE')
ov('E0125','E0125:O3','控制系统接口定义无法确定本人开发闭环算法；不把接口对象自动升级。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP'])
ov('E0125','E0125:O4','本人定义机械接口与结构连接是运用机械知识集成系统，未写开发机械本体。',metric='DUTY_OWN_USE')
ov('E0125','E0125:O5','本人诊断线束供电等问题不是电力电子开发。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for eid in ['E0125:O6','E0125:O7']:ov('E0125',eid,'接口定义中包括散热/安全机制，具体方法为接口应用示例，未写开发该子系统。',metric='DUTY_OWN_USE',branch='EXAMPLE')
ov('E0125','E0125:O9','本句负责台架和整机工况测试，为方法使用；另以制定测试规范支持开发。',metric='DUTY_OWN_USE')
add('E0125','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立关节模组准入、验收和可靠性验证标准','本人建立验证标准与测试规范，独立支持评测开发。')
for eid in ['E0125:O14','E0125:O15']:ov('E0125',eid,'原引文是职责故障列举；改到要求的传动件原理。',metric='GENERAL',quote='熟悉电机、减速器、轴承、编码器、力矩传感器、制动器和嵌入式软件的基本原理及相互影响')
for eid in ['E0125:O25','E0125:O26','E0125:O27']:ov('E0125',eid,'原指职责评估/标准，修到实际优先要求的or清单。',metric='PREFERRED',quote='有批量质量问题处理、失效分析、可靠性验证或供应商整改经验者优先')
for e in EB[RID['E0125']]:
 if e['code']=='V2_PROCUREMENT' and e['metric']!='SEPARATE':ov('E0125',e['evidence_id'],'供应商技术评估、失效报告、技术改进、选型信息管理不自动等于采购商务/供货流程。',metric='SEPARATE',branch='SUPPLIER_TECHNICAL_OBJECT')
add('E0125','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','主导解决关节模组在整机开发和运行过程中出现的复杂问题','明确同时涉及开发与运行故障，运行部分单独支持；不据此推为客户现场。')
R['E0101']['judgment']='全文短但安全风险分析与安全需求评审明确，无关键词不代表无方法。补风险分析和安全需求工程应用，不补认证或法规名称。'
add('E0101','V2_SAFETY_ANALYSIS','DUTY_OWN_USE','UNCONDITIONAL','挖掘安全风险，向业务方输出具体解决方案','明确风险识别分析的本人工作。')
add('E0101','V2_REQUIREMENTS_ENGINEERING','DUTY_OWN_USE','UNCONDITIONAL','负责机器人场景的安全需求评审和技术方案安全评审','本人安全需求评审。')
R['E0035']['judgment']='整机系统集成与测试明确，实际测试不是开发测试工具；需求拆解和技术风险是方法工作。CAN/EtherCAT斜线未知，现场问题未确定在役或开发阶段。'
ov('E0035','E0035:O6','整机联调测试为方法执行，未明示评测平台/方法研发。',metric='DUTY_OWN_USE')
ov('E0035','E0035:O10','原引用职责导航调试；改为普通要求中的SLAM导航。',metric='GENERAL',branch='EXAMPLE',quote='精通运动控制、SLAM导航、传感检测、CAN/EtherCAT总线通讯等核心技术')
for eid in ['E0035:1:0','E0035:1:1']:ov('E0035',eid,'CAN/EtherCAT斜线关系未解，与同词其它广告一致。',branch='UNRESOLVED')
add('E0035','V2_REQUIREMENTS_ENGINEERING','DUTY_OWN_USE','UNCONDITIONAL','对接产品及客户需求，拆解技术指标与研发难点，输出规范的系统设计技术文档','本人把客户/产品需求分解为技术指标与系统设计。')
add('E0035','V2_INCIDENT_SUPPORT','UNKNOWN','UNRESOLVED','解决量产及现场应用技术问题','现场应用可能为初始开发调试或在役问题，运行边界不足。',affected_metrics=['DUTY_OWN_USE'])
R['N0438']['judgment']='系统架构、跨专业协调与带领团队验证明确；协调机械/力控不推各自本人开发。需求明确与路线图属于需求工程应用，没有凭职称补工具。'
add('N0438','V2_REQUIREMENTS_ENGINEERING','DUTY_OWN_USE','UNCONDITIONAL','明确产品需求并制定路线图和发展策略','本人需求明确与架构规划；不把宏观战略泛称当软件工具。')
R['N0078']['judgment']='嵌入式系统方案与稳定性问题定位明确；参与MCU开发另记协作。协议由如/等引出，CAN/CAN FD保留协议族的原始具体名，串口沿用冻结别名但不解释为确定RS485。现场问题是否在役未明。'
ov('N0078','N0078:O4','参与固件与工具开发未明确本人交付；独立系统扩展开发证据另保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in EB[RID['N0078']]:
 if e['code'] in ['V2_ETHERNET','V2_TCPIP','V2_CAN','V2_ETHERCAT','V2_RS485']:ov('N0078',e['evidence_id'],'如...等通信技术是示例，无明确or；CAN FD为同冻结协议族子型，保留原文避免混为同规格。',branch='EXAMPLE')
add('N0078','V2_INCIDENT_SUPPORT','UNKNOWN','UNRESOLVED','根据现场问题，结合日志、抓包、代码、波形及系统运行状态，定位软硬件边界和问题根因','明确排障但现场开发与在役维护边界未明，不自动判客户维护。',affected_metrics=['DUTY_OWN_USE'])
R['N0443']['judgment']='本体研发领导与系统设计经验明确；等结构/电机等知识作为例示保留。参与需求讨论和新方法跟踪不足以补本人需求工程或具名研发方法，未据高管岗位推工具。'
register(list(R.values()),'Astra_systems_fullread_a')
