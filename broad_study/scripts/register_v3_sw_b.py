from astra_review_tools import *
JUD={
'N0632':'内部金蝶业务系统与定制插件主责；规范建设不是开发金蝶软件本体，实际插件开发另保留。K3各版本同品牌，ERP各品牌同上位类。',
'N0166':'参与内核模块研发之外，另有独立解决内核性能稳定安全、优化内存管理动作；Linux本人开发正例重锚该动作。',
'N0175':'机器人系统软件主责一般，三个具体嵌入式实时可靠性方向均写参与，不冒称独立承担；DDS/ZeroMQ斜线未知。',
'N0584':'Go后台和时延优化本人交付，K8s集群参与不能升级本人使用。CI经验在一般段，上一句Service Mesh优先不支配下一句。',
'N0580':'交互与LLM任务规划应用明确；端侧量化剪枝本人独立执行，仿真真机验证为配合硬件。Agent要求是一般而非优先。',
'N0348':'灵巧手软件模块集成与性能优化，C++有独立正例但Python未知；感知控制为包括等的集成模块例示。',
'E0039':'Runtime参与职责与推动系统稳定性分开；C++无条件、Python或Go明确，ROS2/DDS优先内部未知。',
'E0017':'SoC系统性能优化和可复用性能分析体系，C/C++语言是代码编写使用而非语言本体开发，斜线未知；修复要求错锚。',
'E0094':'API集成测试不等于开发测试工具；标题C++不作为正文工具要求，软件修复目标明确。',
'E0091':'后台服务性能与数据安全维护完整可见；标题JAVA不能自动补正文语言使用要求。',
'E0080':'模型产品集成与数据平台、安全恢复、测试体系独立交付；降低系统延迟原漏实时目标，补录。',
'E0119':'平台SRE，PostgreSQL运行备份与恢复为使用既有数据库；监控工具内层斜线未解，至少两类不解决各类内部关系。明确事故指挥与生产事故经验补录。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0632','N0632:O2','WMS是OA等上下游系统列举之一。',branch='EXAMPLE')
ov('N0632','N0632:2:0','建立系统使用规范和审批月结SOP是运用平台，不是开发平台本体。',metric='DUTY_OWN_USE')
ov('N0632','N0632:5:0','对接金蝶厂商是合作方对象，不当作工具使用证据。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0632','N0632:6:0','WISE/Cloud等都是金蝶K3版本，明确该平台经验。',branch='UNCONDITIONAL')
ov('N0632','N0632:O8','云星空和其他ERP都属ERP，上位类经验明确。',branch='UNCONDITIONAL')
ov('N0166','N0166:O1','原参与句不能证明独立责任；随后独立解决内核问题、优化内存管理构成内核改进开发。',metric='DUTY_OWN_DEVELOP',quote='分析和解决内核层的性能瓶颈、稳定性及安全性问题')
for e in ['O4','O5','O6']:ov('N0175',f'N0175:{e}','具体研发方向明确参与，按协作对象保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0175','N0175:3:0','DDS/ZeroMQ不同中间件的斜线未知，与ZeroMQ既有判读一致。',branch='UNRESOLVED')
ov('N0584','N0584:O2','原文参与Kubernetes集群部署治理，不能直接赋本人独立使用。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0584','N0584:O8','独立端到端延迟分析调优句是本人实时系统优化证据。',metric='DUTY_OWN_DEVELOP',quote='针对音视频业务场景进行端到端延迟分析与调优，包括网络传输、服务处理、缓冲策略等各环节')
for e in ['N0584:1:0','N0584:1:1']:ov('N0584',e,'MySQL/PostgreSQL斜线未知。',branch='UNRESOLVED')
for e in ['N0584:9:0','N0584:9:1','N0584:9:2']:ov('N0584',e,'上一句优先不延伸到本句一般CI/CD经验。',metric='GENERAL')
for e in ['N0580:O10','N0580:O11','N0580:2:1']:ov('N0580',e,'配合硬件团队验证，不能升级独立承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0580','N0580:2:0','本人负责模型量化剪枝，是明确模型优化方法实施。',metric='DUTY_OWN_DEVELOP')
ov('N0580','N0580:4:0','一般Agent经验或规划工具调用相关项目，没有优先标记。',metric='GENERAL',branch='CHOICE')
add('N0580','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL','基于大语言模型（LLM）构建机器人的**任务规划（Task Planning）**系统，实现复杂指令的拆解、逻辑推理及多步骤长程任务的自主执行。','明确LLM工作流开发与多步骤任务执行。')
for e in ['O8','O9']:ov('N0348',f'N0348:{e}','感知规划控制等算法模块为例示。',branch='EXAMPLE')
ov('E0039','E0039:O6','开发经验句存在或，嵌入式是明确任选路径。',branch='CHOICE')
ov('E0039','E0039:2:0','本句为加分项且ROS2/DDS内层斜线未解。',metric='PREFERRED',branch='UNRESOLVED')
add('E0039','TC_RELIABILITY','DUTY_OWN_DEVELOP','UNCONDITIONAL','推动端侧系统逐步提升稳定性、可维护性和复用能力','独立推动系统稳定性改进，与前两条参与不同。')
ov('E0017','E0017:O1','使用C/C++优化业务代码，不是开发语言本体；两个语言斜线关系未知。',metric='DUTY_OWN_USE',branch='UNRESOLVED')
ov('E0017','E0017:O2','一般语言要求原错锚职责，改任职要求原句。',metric='GENERAL',quote='精通C/C++，具备较强的并发、Memory、Cache、SIMD等底层能力。')
add('E0017','TC_REALTIME','DUTY_OWN_DEVELOP','UNCONDITIONAL','定位系统性能瓶颈，降低端到端 Latency','本人降低系统端到端时延。')
ov('E0094','E0094:O1','集成和测试API是评测应用，没有新测试方法工具开发。',metric='DUTY_OWN_USE')
add('E0080','TC_REALTIME','DUTY_OWN_DEVELOP','UNCONDITIONAL','优化机器人软件架构,降低系统延迟,确保“感知-决策-执行”链路的高频、稳定响应。','独立系统架构时延优化明确。')
ov('E0119','E0119:O2','一般Kubernetes要求原引职责，重新定位真实经验要求。',metric='GENERAL',quote='3年以上 Kubernetes生产经验。')
ov('E0119','E0119:1:0','高可用备份恢复与升级维护是应用已有PostgreSQL，未开发数据库本身。',metric='DUTY_OWN_USE')
for e in ['E0119:5:0','E0119:5:1']:ov('E0119',e,'至少两类不解决Prometheus/Grafana同类内部斜线关系。',branch='UNRESOLVED')
add('E0119','V2_INCIDENT_SUPPORT','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立 SLI/SLO、错误预算、告警、值班、事故指挥和复盘机制。','本人建立事故响应机制，而非泛称技术问题排查。')
add('E0119','V2_INCIDENT_SUPPORT','GENERAL','UNCONDITIONAL','具备生产事故、变更、容量、灾备和跨团队沟通经验。','明确生产事故经验。')
register(list(R.values()),'Astra_v3_sw_b')
