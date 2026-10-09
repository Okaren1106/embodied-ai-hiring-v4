from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0238':'IT资产全生命周期采购与SOP明确；Linux/Windows未知保留。',
'N0347':'控制软件直接负责与协作算法区分，数据采集系统为明确本人开发。',
'N0320':'BSP与Linux集成，ROS斜线及协同算法模块区分。',
'N0301':'软件集成；低延迟不自动是实时系统，现代C++独立证据已保留。',
'N0306':'服务器运维要求，数据库列表保留等，安全与稳定为运行职责。',
'N0242':'用Node/TypeScript开发服务不等于开发语言；AI编码工具是一般资格。',
'N0289':'BSP岗位附优先项，要求任一项者优先覆盖整个加分段。',
'N0314':'助理调试与本人搭建仿真测试环境分开；具体平台斜线未解。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('N0347','O5','控制软件明确本人整体架构及核心开发，改锚F2，不借协作算法句。',metric='DUTY_OWN_DEVELOP',quote=ln('N0347',2))
ov('N0347','O6','运动规划为与算法工程师协作实现，保留协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O4','3:0']:ov('N0347',e,'不限所列操作系统，允许候选且列表为开放示例。',branch='CHOICE_AND_EXAMPLE')
add('N0347','TC_DATA_PIPELINE','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'明确负责数据采集与分析系统设计开发。')
for r,ros,collab,tools in [('N0320',['O1','O2'],['O11','O12','O13'],['1:1','1:2','7:0','7:1']),('N0289',['O1','O2'],['O16','O17','O18'],['3:1','3:2','12:0','12:1'])]:
 for e in ros+tools:ov(r,e,'具体ROS、开发工具或构建框架之间裸斜线未解。',branch='UNRESOLVED')
 for e in collab:ov(r,e,'该分句协同算法团队部署模块，保留协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for r,e in [('N0301','O10'),('N0289','O14')]:ov(r,e,'原文只有低延迟/抖动或性能优化，冻结实时系统要求明确实时执行/系统/调度。',metric='SEPARATE',branch='LATENCY_NOT_EXPLICIT_REALTIME')
for e in ['O8','O9']:ov('N0301',e,'算法模块以等列举。',branch='EXAMPLE')
for e in ['12:0','12:1']:ov('N0306',e,'中间件数据库以等列举。',branch='EXAMPLE')
for e in ['1:0','1:1']:ov('N0242',e,'用语言/运行时开发服务，非开发工具本体；Node.js/TypeScript关系未解。',metric='DUTY_OWN_USE',branch='UNRESOLVED')
ov('N0242','12:0','MongoDB/Mongoose不同工具裸斜线未解。',branch='UNRESOLVED')
ov('N0242','12:1','Redis在等列举中。',branch='EXAMPLE')
for e in ['16:0','16:1','16:2']:ov('N0242',e,'F17仍在任职资格，且如与或类似共同作用。',metric='GENERAL',branch='CHOICE_AND_EXAMPLE')
for e in ['25:0','26:0','26:1']:ov('N0242',e,'Node.js C++ Addon经验与性能优化或底层能力开发任选。',branch='CHOICE')
for e in ['17:0','17:1']:ov('N0289',e,'模型部署与异构编程或，且加分任一项；括号本身无示例词。',branch='CHOICE')
for e in ['O1','O2']:ov('N0314',e,'MuJoCo/ROS2具体平台裸斜线未解。',branch='UNRESOLVED')
ov('N0314','O7','协助算法工程师测试保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
register(list(R.values()),'Astra_v3_boundary_sw_h')
