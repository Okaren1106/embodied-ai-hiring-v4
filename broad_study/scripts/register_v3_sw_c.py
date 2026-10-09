from astra_review_tools import *
JUD={
'N0929':'自主后端服务连接实际机器人任务，主任务运行软件可保留；C++ where needed为条件，Python无条件，消息框架要求有外层or。',
'E0609':'内部标注和研究运营工具，改归开发基础设施；Postgres we use只是当前栈说明，一般经验不能自动落到具体数据库，Bonus具体栈另有明确正例。',
'E0485':'消费者身份支付后台，不因Helix名称归模型；IaC及云平台主责，Terraform or similar为任选，CI平台运行按使用。',
'N0946':'FAR硬件至策略运行层；C++/Python interop明确组合且可选其他混合栈，保留CHOICE。协议和DDS在Preferred，原错为一般；补正文USB及嵌入式移植。',
'N0999':'客户集成咨询，独立跨平台软件框架和技术问题职责，不由real time适应力修辞推实时系统能力。',
'E0365':'硬件接口运行软件本人交付；总线一般例示与EtherCAT特别优先并存。Git/Jira/CI均位于Bonus，C++和Linux优先的引文需重定位。',
'E0385':'实习岗位明确支持协助；独立采集分析性能数据和编写单测保留，不能全抬升为本人实时控制开发。',
'E0373':'ECAD元件库和PLM集成维护，非电路设计任务；DFM标准遵循是使用，PLM运用不等于开发PLM本体。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0929','N0929:O2','where needed明确条件，不是每条职责都使用C++。',branch='CONDITIONAL')
ov('N0929','N0929:O5','C++或另一种强类型语言保证上位语言要求存在。',branch='UNCONDITIONAL')
ov('N0929','N0929:4:0','消息框架处于event-driven或message framework或SOA的任选，Kafka还是括号例示。',branch='CHOICE_AND_EXAMPLE')
R['E0609']['task_override']=dict(task='DEV_INFRA',quote='Fullstack builds the internal software the rest of Pi runs on.',reason='主要交付内部标注平台、研究需求和运营工具；非机器人云端控制或交互界面。')
ov('E0609','E0609:3:0','we use Postgres是公司当前技术栈说明；资格要求只明确关系数据库，具体栈优先另有正例。',metric='SEPARATE',branch='COMPANY_STACK')
ov('E0485','E0485:2:0','拥有与运行云平台及CI/CD不证明开发CI工具本体，按使用。',metric='DUTY_OWN_USE')
ov('E0485','E0485:3:2','Terraform or similar明确可替换。',branch='CHOICE')
for e in ['N0946:6:0','N0946:6:1','N0946:6:2','N0946:6:3','N0946:12:0']:ov('N0946',e,'这些条目在Preferred Qualifications标题范围。',metric='PREFERRED')
add('N0946','V2_USB','DUTY_OWN_USE','EXAMPLE','chasing a flaky USB camera at the kernel boundary','本人轮转任务例示，原候选声称未出现USB与正文不符。')
add('N0946','TC_EMBEDDED','DUTY_OWN_DEVELOP','UNCONDITIONAL','Port code onto the constrained edge-compute platforms our robots run. Make it work, then make it work well.','明确本人在资源受限边缘平台移植与优化代码。')
ov('E0365','E0365:O4','C++优先原引一般段，改引Bonus的嵌入式代码经验。',metric='PREFERRED',quote='Experience writing C++ code for embedded systems')
ov('E0365','E0365:O8','Linux优先原引一般段，改引Bonus下的网络配置经验。',metric='PREFERRED',quote='Knowledge of networking protocols and network configuration in a Linux environment (i.e. systemd / network)')
ov('E0365','E0365:O15','real-time或low-latency均为同一时延约束技术目标，整个上位类不是可有可无。',branch='UNCONDITIONAL')
for e in ['E0365:5:0','E0365:5:1','E0365:5:2']:ov('E0365',e,'该段处于About You一般要求，只有括号的EtherCAT特别优先。',metric='GENERAL')
add('E0365','V2_ETHERCAT','PREFERRED','UNCONDITIONAL','EtherCAT is highly desirable','一般总线列表之外明确额外优先。')
for e in ['E0365:7:0','E0365:7:1','E0365:7:2','E0365:7:3']:ov('E0365',e,'原语境在Bonus Points段。',metric='PREFERRED')
add('E0365','TC_REALTIME','DUTY_OWN_DEVELOP','UNCONDITIONAL','Own the design, development, and evolution of C++ software components that power our robots, interfacing with OS drivers and hardware to enable high-bandwidth, low-latency control','明确软件本人交付低时延控制能力。')
for e in ['O1','O6','O7','O8','O9']:ov('E0385',f'E0385:{e}','对应Support、Assist或Help，保留协作对象，不提升本人独立承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0385','E0385:O11','原概述协助建设；独立编写单测验证系统稳定为可靠性应用，非开发恢复机制。',metric='DUTY_OWN_USE',quote='Write unit tests and maintain clear documentation for software features to ensure system stability.')
ov('E0385','E0385:2:0','participate/contribute描述参与团队流程。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('E0385','TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL','Write unit tests and maintain clear documentation for software features to ensure system stability.','独立编写单测，是本人测试评价应用。')
ov('E0373','E0373:O7','Python or Perl只是两种语言任选，无开放例示标记。',branch='CHOICE')
ov('E0373','E0373:2:0','按制造商DFM标准制作元件库，是应用设计制造规则，未开发DFM方法。',metric='DUTY_OWN_USE')
ov('E0373','E0373:4:0','与其他团队协作并support审查，不直接本人独立应用；本广告其他明确DFM应用保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0373','E0373:5:0','维护库和PLM集成是使用既有平台，不是开发PLM工具。',metric='DUTY_OWN_USE')
ov('E0373','E0373:6:0','其他ECAD工具括号列举Allegro、Mentor等，未写任选。',branch='EXAMPLE')
ov('E0373','E0373:8:0','品牌可选，但PLM系统上位经验明确。',branch='UNCONDITIONAL')
add('E0373','SK_PCB','GENERAL','UNCONDITIONAL','Strong understanding of electronic components, package drawings, manufacturer datasheets, pinouts, land patterns, and PCB fabrication/assembly processes and constraints.','另句明确PCB制造装联过程知识，不仅资格任选经历。')
register(list(R.values()),'Astra_v3_sw_c')
