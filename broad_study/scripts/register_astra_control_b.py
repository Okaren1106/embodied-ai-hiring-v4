from astra_review_tools import *
ids=['N0855','E0348','E0583','N0926','N0983','N0939','N0803']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why,**v):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**v))
R['N0855']['judgment']='仓储控制含嵌入式和控制开发，Minimum Qualifications明确最低要求，旧GENERAL改REQUIRED。记录故障结果未明确在役事故处理，相关方法保留未知；优先的已部署远程诊断另有直接证据。'
for e in EB[RID['N0855']]:
 if e['metric']=='GENERAL':ov('N0855',e['evidence_id'],'Minimum Qualifications管辖的最低任职条件。',metric='REQUIRED')
ov('N0855','N0855:3:0','记录排障结果本身未区分开发/在役。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
add('N0855','V2_INCIDENT_SUPPORT','PREFERRED','UNCONDITIONAL','remote diagnostics','优先条件明确已部署系统远程诊断。')
R['E0348']['judgment']='全身规划研发与技术协作边界分开。一般感知要求修回About You架构接口句；loco-manipulation优先证据修回Bonus；全身优化等任选条件保留。'
ov('E0348','E0348:O16','原引用职责，将一般经验定位回About You中跨感知架构接口。',metric='GENERAL',quote='Track record architecting large-scale autonomy systems and defining clean interfaces across perception, estimation, planning, and control')
ov('E0348','E0348:O18','与控制的接口集成未明确本人应用控制算法，保持协作对象。',metric='SEPARATE',branch='INTERFACE_OBJECT')
ov('E0348','E0348:O20','原指一般操作经验；优先loco-manipulation另句有明确依据。',metric='PREFERRED',quote='Experience with loco-manipulation: combined planning of locomotion and manipulation')
for e in ['E0348:4:0','E0348:5:0','E0348:O26']:ov('E0348',e,'原句明确or，不能将单个替代项无条件化。',branch='CHOICE')
R['E0583']['judgment']='PI控制岗位，不是旧备注所写Apptronik。控制方法开发、参数模型和运行环路明确；采集数据不等于开发数据流水线。无关系词的协议括号清单保留未知，修要求引文位置。'
ov('E0583','E0583:O9','本人collect structured datasets属于采集使用，未明示开发采集平台。',metric='DUTY_OWN_USE')
ov('E0583','E0583:O16','一般仿真能力定位回要求。',metric='GENERAL',quote='Ability to validate control approaches in simulation and translate them to real hardware')
ov('E0583','E0583:O25','优先自定义执行器硬件能力定位回Bonus。',metric='PREFERRED',branch='CHOICE',quote='Ability to design or refine custom actuator or sensor hardware')
for e in EB[RID['E0583']]:
 if e['code'] in ['V2_CAN','V2_ETHERNET','V2_I2C','V2_SPI']:ov('E0583',e['evidence_id'],'括号列举未说明全部/例示/任选。',branch='UNRESOLVED')
R['N0926']['judgment']='仓库多机器人调度与在役软件on-call属于本人职责；现有CI使用成立，补排障支持和路径方法开发。Rust优先与至少一门语言的任选位置分列。'
add('N0926','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','production debugging, and on-call support','本人负责生产调试与值班。')
add('N0926','V2_PATH_SEARCH','DUTY_OWN_DEVELOP','UNCONDITIONAL','multi-agent path planning','明确多机器人路径规划算法开发。')
R['N0983']['judgment']='Spot操作控制岗位，C++开发与一般要求分列。路径优化位于Nice to Have，不能归GENERAL；强化学习示例和VLA斜线未知保留。'
ov('N0983','N0983:3:0','Nice to Have标题管辖的路径规划优化。',metric='PREFERRED')
R['N0939']['judgment']='导航研发职责明确。原文逐项required/plus与例示/任选均须保留；轨迹优化or MPC不得将专业方法无条件化。'
ov('N0939','N0939:6:0','trajectory optimization and/or MPC，至少是明确任选关系。',branch='CHOICE')
R['N0803']['judgment']='Field AI联邦版本导航控制。正文确有部署后现场问题调查、运行遥测及改进，补事件支持方法；没有把公司宣传基础模型计为岗位职责。ROS斜线未知保留。'
add('N0803','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Investigate and resolve issues arising from field deployments through structured data analysis and debugging','本人调查解决现场部署产生的问题。')
register(list(R.values()),'Astra_control_fullread_b')
