from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0809':'本体平台集成，协作验证单列；协议在优先段，TCP/UDP同冻结类。',
'N0839':'与N0838相同DevOps正文独立保留身份，采用一致语境裁决。',
'N0731':'人形研究DevOps，several of them覆盖一般技能；基础设施对象不等于CUDA编程/HIL执行。',
'N0833':'ROS应用集成与本人感知/控制实现；支持API工作单列，标定执行不升级方法开发。',
'N0813':'IT与安全运维，安全工具或框架的同类任选不影响安全能力整体；事件响应补齐。',
'N0773':'基础设施安全，所有安全方法同类内部选项与评测子集区分，help改进可靠性单列。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('N0809','O16','导航适配在such as示例中。',branch='EXAMPLE')
ov('N0809','O17','Partner with teams完成验证试验保留协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['7:0','7:1','7:2']:ov('N0809',e,'Extras优先段的such as协议，UDP/TCP同冻结TCPIP类。',metric='PREFERRED',branch='EXAMPLE')
add('N0809','V2_RS485','PREFERRED','EXAMPLE',36,'冻结别名包含serial/串口，保留such as。')
ov('N0839','O7','语言类别明确，具体语言才任选。',branch='UNCONDITIONAL')
for e in ['O16','O17']:ov('N0839',e,'支持测试/跨团队改进可靠性，保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0731','O1','CUDA是构建runner目标，未明编写CUDA。',metric='SEPARATE',branch='BUILD_TARGET')
for e in ['O2','O3']:ov('N0731',e,'测试后端或驱动协议明确or。',branch='CHOICE')
ov('N0731','O10','ROS2优先资格改锚F55，原为职责。',metric='PREFERRED',quote=ln('N0731',55))
for e in ['O11','O12']:ov('N0731',e,'Isaac Sim/Lab同冻结Isaac类，优先资格用F57而非职责。',metric='PREFERRED',branch='UNCONDITIONAL',quote=ln('N0731',57))
ov('N0731','8:0','部署运营Airflow栈是工具使用，非开发Airflow本体。',metric='DUTY_OWN_USE')
for e in ['10:0','10:1','58:0','58:1']:ov('N0731',e,'rosbag/MCAP不同工具裸斜线未解。',branch='UNRESOLVED')
ov('N0731','21:0','以代码管理AWS资源是使用云平台。',metric='DUTY_OWN_USE')
ov('N0731','29:0','管理HIL连通性未明本人执行HIL方法。',metric='SEPARATE',branch='INFRASTRUCTURE_TARGET')
for e in ['34:0','47:0','47:1','54:0']:ov('N0731',e,'you do not need every item; several of them明确外层候选集合。',branch='CHOICE')
for e in ['O1','O2']:ov('N0833',e,'ROS/ROS2职责版本关系未解。',branch='UNRESOLVED')
for e in ['O15','O16','O17']:ov('N0833',e,'including功能列表为示例；F4独立职责另存。',branch='EXAMPLE')
for e in ['O21','O22']:ov('N0833',e,'Help building APIs保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0833','O28','状态估计泛称不能自动补成SLAM，F21另有明确SLAM。',metric='SEPARATE',branch='GENERIC_STATE_ESTIMATION')
ov('N0833','1:0','实际集成标定传感器，未明开发标定方法。',metric='DUTY_OWN_USE')
for e in ['O12','O13','O14','O15']:ov('N0813',e,'所有列出的候选均是安全平台/合规框架，上层安全能力明确。',branch='UNCONDITIONAL')
add('N0813','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',18,'明确lead first response on endpoint security incidents。')
ov('N0773','O12','help drive remediation保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O18','O19','O21','O22','O26','O27','O28','O29','O30','O31','O33']:ov('N0773',e,'候选项均为安全方法，上层安全类别明确；评测子项仍保留任选。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_sw_o')
