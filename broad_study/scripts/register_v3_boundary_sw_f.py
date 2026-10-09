from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0091':'规控平台开发；列举关系与实际算法使用分开，协作排障不等于本人测试执行。',
'N0153':'服务端模型封装与数据管理；模型/数据库之间裸斜线保留未知。',
'N0133':'分布式存储与AI负载场景，Go/C++未解；一般和加分要求不同。',
'N0010':'校招各项职责均参与，明确本人任职技能另统计。',
'N0176':'生态Demo和Agent工作流本人产出，参与仿真适配和平台稳定另列。',
'N0169':'SDK职责参与与负责接口分句区别；ROS裸斜线保留。',
'N0011':'同句现代C++明确解除C++未知但不解除C语言未知；CI/CD属于加分。',
'N0050':'实习本人建设工具链和Agent；参与仿真另列，维护GitHub仓库可确认代码协作使用。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
for e in ['O6','O7','O8']:ov('N0091',e,'规划控制等功能/算法明确列举。',branch='EXAMPLE')
ov('N0091','O11','与开发者协作解决实机测试暴露缺陷，没有本人测试执行证据。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O6','O7','4:0','4:1','4:2','4:3']:ov('N0153',e,'不同模型/服务或数据库中间件之间裸斜线未解。',branch='UNRESOLVED')
for e in ['O1','O7','O8','O9','O10','1:0']:ov('N0010',e,'原文各句明确参与，保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0010','4:0','网络协议以等列举。',branch='EXAMPLE')
ov('N0010','7:0','DDS等经验列有或但没有示例词。',branch='CHOICE')
for e in ['O1','O7','O8']:ov('N0176',e,'开源生态或RL/IL范式以等列举。',branch='EXAMPLE')
for e in ['O6','O9']:ov('N0176',e,'参与平台建设/仿真适配保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0176','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL',3,'连续职责原文明确搭建Agent工作流。')
for e in ['O1','O2']:ov('N0169',e,'负责ROS/ROS2接口但具体版本关系未解。',branch='UNRESOLVED')
for e in ['O8','O9','O10']:ov('N0169',e,'参与SDK设计覆盖相关功能，保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0011','O1','同句明确了解现代C++常用特性，GENERAL层存在独立肯定证据。',branch='UNCONDITIONAL')
ov('N0011','O9','参与集成测试保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['3:1','3:2','3:3']:ov('N0011',e,'CMake/GDB/Git裸斜线未解。',branch='UNRESOLVED')
ov('N0011','8:0','加分段的CI/CD，等为示例。',metric='PREFERRED',branch='EXAMPLE')
add('N0011','V2_DDS','GENERAL','CHOICE_AND_EXAMPLE',27,'FastDDS属于DDS，至少一种与如共同作用。')
for e in ['O1','O2']:ov('N0050',e,'参与仿真集成适配保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O3','O6','O7']:ov('N0050',e,'开源生态及学习范式以等列举。',branch='EXAMPLE')
add('N0050','V2_AGENT_WORKFLOW','DUTY_OWN_DEVELOP','UNCONDITIONAL',7,'明确搭建Agent工作流。')
add('N0050','V2_GIT','DUTY_OWN_USE','EXAMPLE',11,'GitHub生态与维护开源仓库同句，能确认代码协作，不只是发表渠道。')
register(list(R.values()),'Astra_v3_boundary_sw_f')
