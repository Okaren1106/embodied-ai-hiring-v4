from astra_review_tools import *
ids=['N0449','N0410','N0034','N0544','N0358','E0066','E0280','E0079','N0417','N0215','N0494','E0081']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why,**v):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**v))
R['N0449']['judgment']='VLA复现评测写参与，验证框架构建可归本人交付；论文跟踪兴趣不升级成一般技能。RL/IL斜线保留未知。'
ov('N0449','N0449:O3','参与算法复现实验未给本人独立使用边界；框架构建另记。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0449','N0449:O6','对VLA/VLM论文有跟踪兴趣，非明确知识或能力要求。',metric='SEPARATE',branch='INTEREST_OBJECT')
R['N0410']['judgment']='本人产测与售后上位机开发清楚，Agent优先、程控电源示例分列。不把售后团队所用软件的开发误当本人售后维修。'
ov('N0410','N0410:9:0','仪器等清单为例示，与万用表/示波器一致。',branch='EXAMPLE')
R['N0034']['judgment']='仿真平台与自动测试脚本研发明确；实现域随机化策略可支持方法使用。C++/Python斜线未知，Isaac等经验任选优先保持。'
R['N0544']['judgment']='评测实习负责可复现场景方案和标准程序；参与平台不直接当本人平台研发，机器人操作是评测任务对象。岗位亮点的可能成果不属于优先要求。'
ov('N0544','N0544:O3','用独立持续完善评测体系的职责支持开发，而非单靠参与。',metric='DUTY_OWN_DEVELOP',quote='持续完善任务设计与评价体系')
ov('N0544','N0544:O4','操作任务是Benchmark研究对象，未写开发或使用操作算法。',metric='SEPARATE',branch='EVALUATION_OBJECT')
ov('N0544','N0544:O5','参与工具与平台建设未明确本人研发交付。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0544','N0544:1:0','制定SOP是程序开发，不是已明确执行程序。',metric='DUTY_OWN_DEVELOP')
ov('N0544','N0544:6:0','工作成果可形成SOP处于岗位亮点，非加分资格。',metric='SEPARATE',branch='POTENTIAL_OUTPUT')
R['N0358']['judgment']='设备开发与验证执行并存；精密设备校准及SOP研发有据。可靠性验证归使用，协议等示例分支修正。'
ov('N0358','N0358:O6','开展可靠性验证是使用；测试计划/设备研发另保留。',metric='DUTY_OWN_USE')
for e in ['N0358:6:0','N0358:6:1']:ov('N0358',e,'Modbus TCP/IP等协议由等引出。',branch='EXAMPLE')
R['E0066']['judgment']='评测方式与系统性能分析是本人任务，感知是评测覆盖对象而不是本人感知算法使用；方法优先斜线仍未知。未凭闭环字样补控制算法。'
ov('E0066','E0066:O2','评测体系覆盖感知，未表明本人使用感知技术。',metric='SEPARATE',branch='EVALUATION_OBJECT')
R['E0280']['judgment']='物理引擎二次开发与任选资历、必要条件、加分条件层次均保留；Isaac维护与数据清洗写参与。优先仿真能力的证据修回加分段。'
for e in ['E0280:O1','E0280:O6']:ov('E0280',e,'明确参与日常维护清洗，未明本人交付责任。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0280','E0280:O22','优先仿真知识定位回加分项，不能引用职责参与维护。',metric='PREFERRED',quote='对模拟有深度理解')
R['E0079']['judgment']='完整短正文包含实际数据运营、质量规则制定及运行故障支持，虽无候选关键词仍补明确方法。数据资产日常管理为使用，版本和质量方法制定另支持开发。'
ov('E0079','E0079:O1','全生命周期管理运营是使用；另有制定方法支持开发。',metric='DUTY_OWN_USE')
add('E0079','TC_DATA_PIPELINE','DUTY_OWN_DEVELOP','UNCONDITIONAL','数据版本控制方法','本人制定数据版本控制方法。')
add('E0079','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','负责制定和实施数据采集规范、质量评估标准、数采员培训教程','本人制定标准程序与采集规范。')
add('E0079','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','负责制定和实施数据采集规范、质量评估标准、数采员培训教程','实施明确，不仅制定。')
add('E0079','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','机器人数据采集软硬件问题的分析和解决，保障数据采集过程稳定运行','实际采集运行期软硬件故障闭环。')
R['N0417']['judgment']='端云实时数据系统和容错机制是本人研发；C++/Rust与Kafka/RabbitMQ关系未解，不能仅凭斜线推任选。TCP/IP本身为冻结协议族，不拆为未知。'
for e in ['N0417:O2','N0417:O3','N0417:4:0']:ov('N0417',e,'不同工具或语言斜线关系未解。',branch='UNRESOLVED')
R['N0215']['judgment']='数据闭环、模型质量体系与多模态数据平台职责清楚；深度学习框架斜线保留未知。跨部门明确需求描述不足以新增专门需求工程方法。'
R['N0494']['judgment']='自动标注算法、设计评测指标是本人工作；配合工具链建设仍分列协作，不因单个工具链字样增加研发责任。上位ML概念保留，各具体技术的等分支应另记。'
ov('N0494','N0494:O7','配合工具链建设提供算法支持，未明本人开发工具链。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
R['E0081']['judgment']='完整短正文为数据流水线、存储索引和研究工具开发；大模型团队明确协作对象。未凭无关键词推缺技能，也未把无具名的可视化工具补成具体软件。'
register(list(R.values()),'Astra_sim_data_fullread_a')
