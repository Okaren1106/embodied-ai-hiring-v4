from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0087':'仿真平台：跨方向经验与具体软件例示分开；F51格式要求属于加分项；参与DR及Sim2Real不能升格本人独立承担。补硬件在环明确要求。',
'N0372':'物理引擎：灵巧操作和执行器是所模拟对象，SysID为合作承担；工具例示与至少一种、斜杠关系分别处理；一般要求重定位至要求正文。',
'N0627':'生产测试设备：核心硬性开发经验与一般/优先经验分别保留；外协仍为合作，补标准操作维护测试规范。',
'E0045':'整机评测：加分标题涵盖软件、标准和用户研究；Python/MATLAB及ROS版本关系未明；测试对象不拆成算法开发。',
'N0281':'仿真算法：仿真器是示例，快速原型验证是本人使用评测而非开发评测平台；实体部署稳定性为与团队合作。',
'E0160':'导航仿真：导航/操作/控制接口均是仿真评测对象；一般与优先要求错引职责须修定位，实例/至少一种/斜杠不混并。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0087','O25','平台对控制器对象封装，未称本人运动控制算法。',metric='SEPARATE',branch='PLATFORM_OBJECT')
for i in range(27,33):ov('N0087','O'+str(i),'至少一种选项全属于仿真，上位仿真能力明确。',branch='UNCONDITIONAL')
for e in ['1:0','1:1']:ov('N0087',e,'参与相关能力建设，独立承担不足。',metric='SEPARATE',branch='PARTICIPATION')
for e in ['4:0','4:1','7:0']:ov('N0087',e,'至少一项/或加类似工具示例均存在。',branch='CHOICE_AND_EXAMPLE')
ov('N0087','14:0','等示例，无至少一种或or。',branch='EXAMPLE')
for e in ['17:0','17:1','17:2','17:3']:ov('N0087',e,'F45加分标题内且等格式列举。',metric='PREFERRED',branch='EXAMPLE')
ov('N0087','22:0','经验方向受或约束。',branch='CHOICE')
add('N0087','V2_HIL','PREFERRED','UNCONDITIONAL','熟悉 ROS/ROS 2、遥操作、数据采集、硬件在环测试及仿真与真机系统对齐。','硬件在环为明确加分知识，并非泛称实机测试。')
for e in ['O1','O2']:ov('N0372',e,'如仿真器属于示例。',branch='EXAMPLE')
ov('N0372','O7','一般要求应引F12，而非职责F3。',metric='GENERAL',quote=line('N0372',12))
for e in ['O8','O9','12:0','12:1']:ov('N0372',e,'等至少一种同时体现例示与选择。',branch='CHOICE_AND_EXAMPLE')
for e in ['O13','16:0','16:1']:ov('N0372',e,'不同中间件斜杠关系未明。',branch='UNRESOLVED')
ov('N0372','O19','本人调物理引擎参数，操作是仿真应用对象。',metric='SEPARATE',branch='APPLICATION_OBJECT')
ov('N0372','O20','实现仿真模型中执行器建模，非执行器实物研发操作。',metric='SEPARATE',branch='SIMULATED_OBJECT')
for e in ['O25','5:0','5:1']:ov('N0372',e,'与科学家工程师协作开展辨识，未明确独立承担。',metric='SEPARATE',branch='COLLABORATION')
for e in ['2:0','2:1']:ov('N0372',e,'URDF/MJCF关系未明。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for e in ['8:0','8:1']:ov('N0372',e,'如物理引擎示例，未明任选。',branch='EXAMPLE')
add('N0627','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立标准化的设备操作、维护、测试规范','本人建立操作维护测试规范。')
R['E0045']['catalog_gap_notes']=['ISO 9283及ISO/TS 15066标准认证或测试经验明确在加分项，但冻结标准条目不适用仿真评测职能；不以无目录格解释为没有相关标准要求。']
for e in ['O1','O2']:ov('N0281',e,'如基于为软件示例。',branch='EXAMPLE')
ov('N0281','O14','F4仅建环境用于验证；F3本人快速原型验证支持使用评测。',metric='DUTY_OWN_USE',quote=line('N0281',3))
ov('N0281','O15','与其他团队紧密合作完成，非明确独立承担稳定性开发。',metric='SEPARATE',branch='COLLABORATION')
for e in ['O1','O2','O3']:ov('E0160',e,'例如列举的仿真器二次开发。',branch='EXAMPLE')
for e in ['O5','O6','O7']:ov('E0160',e,'一般要求原证据误引职责，重定位F15并保留现有分支。',metric='GENERAL',quote=line('E0160',15))
ov('E0160','O8','一般ROS2要求重定位F17。',metric='GENERAL',quote=line('E0160',17))
for e in ['O11','O12']:ov('E0160',e,'加分软件重定位F23。',metric='PREFERRED',quote=line('E0160',23))
for e,b in [('O16','EVALUATION_OBJECT'),('O17','CONTROL_INTERFACE_OBJECT'),('O18','SIMULATION_TASK_OBJECT')]:ov('E0160',e,'建设仿真评测及接口，不等于开发对应算法。',metric='SEPARATE',branch=b)
ov('E0160','O30','一般移动操作要求应引F16而非职责。',metric='GENERAL',quote=line('E0160',16))
ov('E0160','O40','优先Sim2Real经验应引F26而非职责。',metric='PREFERRED',quote=line('E0160',26))
ov('E0160','1:0','明确使用并二次开发，Habitat在例如列表中。',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE')
for e in ['2:1','2:2','2:3']:ov('E0160',e,'格式斜杠关系不明确。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for e in ['4:0','4:1','4:2']:ov('E0160',e,'至少一种且例如。',branch='CHOICE_AND_EXAMPLE')
for e in ['5:0','5:1']:ov('E0160',e,'等常用工具和格式例示。',branch='EXAMPLE')
for e in ['8:0','9:0','9:1','11:0']:ov('E0160',e,'不同环境/技术用斜杠连接，要求关系未明。',branch='UNRESOLVED')
register(list(R.values()),'Astra_v3_boundary_sim_a')
