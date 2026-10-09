from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0347':'标定负责人确有亲自端到端交付；感知传感器是标定对象。招募他人做标定不能重复记为本人技术开发，一般数据基础设施要求修定位。',
'N0707':'仅Preferred Qualifications，语言为such as加or；无一般要求强制化。',
'N0915':'机器人回归测试：语言Python明确且Rust或C++；HIL自建测试与合作覆盖分开；CI有明确职责和一般经验。',
'N0942':'FAR测试基础设施：语言明确or；辅助实验室管理不升格独立库存/安全职责；仪器例示/任选与总线列举分别处理。',
'N0439':'仿真工程：等至少一种明确二重分支，ROS/DDS/AimRT斜杠不推任选；两种3D重建写法同上位类别。',
'N0380':'必备标题及至少两类父级有效；标注和感知评测对象区分；benchmark/评测同类，不因斜杠产生上位不明。',
'N0373':'RL仿真：操作是仿真对象；仿真软件至少一种，ROS中间件关系未明；系统辨识/DR为等方式示例。',
'N0056':'物理参数测量：CAD至少一种与语言或明确；仿真软件斜杠关系未明但上位仿真能力明确；补物理系统辨识要求。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('E0347','O6','感知传感器是标定对象，无感知算法使用开发责任。',metric='SEPARATE',branch='CALIBRATION_OBJECT')
ov('E0347','O9','一般要求在F20，原F9是职责。',metric='GENERAL',quote=line('E0347',20))
ov('E0347','10:0','协调供应商与制造商部署标定，是合作开展。',metric='SEPARATE',branch='COLLABORATION')
ov('E0347','11:0','招募培养做标定的工程师，是人才管理对象。',metric='SEPARATE',branch='TEAM_MANAGEMENT_OBJECT')
for e in ['O2','O3']:ov('N0707',e,'such as与or similar同时存在。',branch='CHOICE_AND_EXAMPLE')
ov('N0915','O10','测试新固件，不是本人嵌入式固件开发操作。',metric='SEPARATE',branch='TEST_OBJECT')
for e in ['2:0','4:0','5:0']:ov('N0915',e,'Partners或with HIL owners是合作对象，F35的本人HIL测试开发另保留。',metric='SEPARATE',branch='COLLABORATION')
ov('N0915','4:1','失败分诊与软件/嵌入式/HIL负责人共同开展。',metric='SEPARATE',branch='COLLABORATION')
add('N0915','V2_CI_CD','DUTY_OWN_USE','UNCONDITIONAL',line('N0915',38),'本人将回归测试接入CI。')
add('N0915','V2_CI_CD','GENERAL','UNCONDITIONAL',line('N0915',43),'一般CI管线建设经验明确。')
for e in ['O1','O2']:ov('N0942',e,'职责用Python,C++ or equivalent明确任选。',branch='CHOICE')
ov('N0942','O6','全部选项是编程语言，上位语言要求明确。',branch='UNCONDITIONAL')
for e in ['O3','O19']:ov('N0942',e,'Support实验室管理，不独立负责。',metric='SEPARATE',branch='SUPPORT')
ov('N0942','O13','vision systems是测试对象，未说明本人感知算法开发或运行。',metric='SEPARATE',branch='TEST_OBJECT')
ov('N0942','O15','测试软件对接控制接口，非本人闭环控制。',metric='SEPARATE',branch='INTERFACE_OBJECT')
for e in ['O7','O8','7:0']:ov('N0942',e,'仪器清单末尾or equivalent明确任选，无e.g.。',branch='CHOICE')
for e in ['9:0','9:1','9:2']:ov('N0942',e,'总线列举无选择词，不虚构任选。',branch='UNCONDITIONAL')
for e in ['O10','18:0','18:1']:ov('N0942',e,'e.g.与or equivalent并有。',branch='CHOICE_AND_EXAMPLE')
ov('N0942','4:0','原文明确building HIL test environments。',metric='DUTY_OWN_DEVELOP')
add('N0942','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line('N0942',8),'本人诊断定位故障，非仅写排障指南。')
ov('N0942','3:0','原引排障指南编写，改记方法文档开发；本人排障另有F8。',metric='DUTY_OWN_DEVELOP')
for e in ['O6','O7','O8','O9','3:0','3:1','3:2']:ov('N0439',e,'等至少一种兼具示例与选择。',branch='CHOICE_AND_EXAMPLE')
for e in ['O10','8:0','8:1']:ov('N0439',e,'不同中间件斜杠关系未明。',branch='UNRESOLVED')
ov('N0380','O4','建立感知指标而非使用或开发感知算法。',metric='SEPARATE',branch='EVALUATION_OBJECT')
for e in ['O6','O7']:ov('N0380',e,'探索合成数据和轻量仿真手段，没有开发相应平台的交付表述。',metric='DUTY_OWN_USE')
ov('N0380','O14','benchmark与评测是同一上位，受至少两类父级选择。',branch='CHOICE')
ov('N0380','O15','原F12评测平台明确属于跨方向选择，无不明斜杠。',branch='CHOICE')
ov('N0380','O16','回放/实验追踪均属评测上位，受至少两类父级选择。',branch='CHOICE')
ov('N0380','O22','视觉AI数据平台的视觉是所支持领域，不证明本人感知技术经验。',metric='SEPARATE',branch='DATA_PLATFORM_OBJECT')
for e in ['O5','O6','4:0']:ov('N0373',e,'等至少一种。',branch='CHOICE_AND_EXAMPLE')
ov('N0373','O13','操作交互是仿真对象。',metric='SEPARATE',branch='SIMULATION_OBJECT')
for e in ['O9','10:0','10:1']:ov('N0373',e,'中间件斜杠关系未明。',branch='UNRESOLVED')
for e in ['13:0','13:1']:ov('N0373',e,'等方式为示例。',branch='EXAMPLE')
for e in ['O1','O2']:ov('N0056',e,'不同仿真软件斜杠关系未明。',branch='UNRESOLVED')
for e in ['O12','O13','O14']:ov('N0056',e,'所有软件均属仿真，上位能力明确。',branch='UNCONDITIONAL')
add('N0056','V2_SYSID','GENERAL','CHOICE','物理参数测量、辨识或验证 经验。','物理参数系统辨识为测量/辨识/验证之一。')
register(list(R.values()),'Astra_v3_boundary_sim_b')
