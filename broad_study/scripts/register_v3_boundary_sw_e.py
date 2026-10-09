from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0179':'前端框架括号并列，CI/CD流程含等。',
'N0111':'Qt产线工具，测试/采集为示例；Modbus/OPC UA关系未解。',
'N0012':'Agent实习直接开发模块和测试用例，标题RL不补强化学习。',
'N0134':'ES检索平台，语言内部未解不影响至少两门的泛称能力；参与实时流水线另列。',
'N0141':'相机应用和标定，Jetson平台不能自行补成明确嵌入式资格。',
'N0081':'遥操与数据系统本人开发，参与模型推理链路单列；协议及平台经验保留任选示例。',
'N0127':'本体交互应用；协作落地和场景验证不升级独立职责，大模型为列举能力。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('N0179','1:0','流程列举以等结尾。',branch='EXAMPLE')
for e in ['3:0','3:1']:ov('N0179',e,'框架括号并列无示例词。',branch='UNCONDITIONAL')
ov('N0111','O2','测试程序位于如和等的示例范围。',branch='EXAMPLE')
ov('N0111','1:0','Modbus/OPC UA裸斜线未解。',branch='UNRESOLVED')
add('N0111','TC_DATA_PIPELINE','DUTY_OWN_DEVELOP','EXAMPLE',1,'自动化工具示例包含数据采集系统。')
ov('N0012','O8','高性能编程语言类别明确要求，具体语言未知不传递到泛称。',branch='UNCONDITIONAL')
ov('N0012','O12','设计并实现自动化测试用例属于开发。',metric='DUTY_OWN_DEVELOP')
add('N0012','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL',4,'直接开发工具调用/记忆/执行模块，非仅参与F3。')
ov('N0134','O4','至少两门编程语言明确，Java与各语言的组合关系另保留未知。',branch='UNCONDITIONAL')
for e in ['O5','O6']:ov('N0134',e,'参与平台架构与流水线建设保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0141','O1','CUDA加速位于等的示例范围。',branch='EXAMPLE')
ov('N0141','O5','任职仅明确Jetson Orin平台，不由平台补写嵌入式系统/固件/MCU。',metric='SEPARATE',branch='PLATFORM_SPECIFIC')
for e in ['O1','12:0','12:1']:ov('N0081',e,'整份协议列表包含或与等，不只最后ROS一对。',branch='CHOICE_AND_EXAMPLE')
ov('N0081','O13','参与推理链路设计保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0081','17:0','遥操作与数据/标注/评测平台经验明确任选。',branch='CHOICE')
add('N0081','TC_RELIABILITY','DUTY_OWN_DEVELOP','UNCONDITIONAL',6,'直接优化传输，解决断线重连及数据一致性。')
ov('N0127','O7','语音和大模型等为列举的集成能力。',branch='EXAMPLE')
for e in ['O8','O9']:ov('N0127',e,'参与闭环落地/支持实验环境及团队验证保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
register(list(R.values()),'Astra_v3_boundary_sw_e')
