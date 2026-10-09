from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0024':'类ROS不是明确使用ROS产品，主职能不变；具体总线裸斜线未解。',
'N0607':'生产运维与故障处理，明确一般要求和任选示例，监控审查不等于开发可靠性机制。',
'N0587':'Agent运行时，多个一般要求原被误加任选；任务规划与运动规划分开。',
'N0561':'导航系统集成；具体框架任选不影响导航类别；Costmap不自动等于SLAM。',
'N0554':'财务ERP集成，工具与专业能力分开；接口列表保留等。',
'N0539':'应用直接开发测试，语言明确任选，Git一般要求成立。',
'N0525':'Agent参与开发但明确负责维护稳定；C/C++未知与其他语言任选分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('N0024','O7','应用功能包括且以等列举。',branch='EXAMPLE')
ov('N0024','O8','参与现场优化保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0024','1:0','类ROS只说明相似系统；且该句是职责非任职资格。',metric='SEPARATE',branch='SIMILAR_SYSTEM')
for e in ['3:0','3:1','3:2','3:3','3:4']:ov('N0024',e,'总线之间裸斜线未解。',branch='UNRESOLVED')
for e in ['O2','O3','4:0']:ov('N0607',e,'至少一种和等共同作用。',branch='CHOICE_AND_EXAMPLE')
ov('N0607','O7','监控审查稳定性并推动解决，按使用而非开发机制。',metric='DUTY_OWN_USE')
ov('N0607','1:0','GitLab CI属于以等列举的具体流水线。',branch='EXAMPLE')
for e in ['6:0','11:0','11:1']:ov('N0607',e,'不同工具之间裸斜线未解。',branch='UNRESOLVED')
add('N0607','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',3,'明确生产系统故障响应、排查、解决。')
for e in ['O1','O2','O13','O14','O15','O17','O18','O19','O20','6:0']:ov('N0587',e,'该资格明确并列/整体要求，无对应任选分支；LLM/VLM同一大模型类别。',branch='UNCONDITIONAL')
for e in ['O8','O9']:ov('N0587',e,'原子能力以等列举。',branch='EXAMPLE')
ov('N0587','O16','本条明确高层任务规划，不能把通用任务规划自动当运动规划；F18另有运动规划。',metric='SEPARATE',branch='TASK_PLANNING_CONTEXT')
ov('N0587','O21','本条是机器人软件栈开发经验，不由MoveIt/Drake工具补运动规划概念。',metric='SEPARATE',branch='TOOL_CONTEXT')
ov('N0587','12:0','ROS Action/BehaviorTree不同框架裸斜线未解。',branch='UNRESOLVED')
for e in ['O20','O21','O22']:ov('N0561',e,'三个候选都明确属于导航框架，上层导航类别非任选。',branch='UNCONDITIONAL')
ov('N0561','O30','Costmap知识不能自动推出SLAM/定位建图。',metric='SEPARATE',branch='COSTMAP_ONLY')
for e in ['O2','1:0','1:1']:ov('N0554',e,'接口集成系统清单以等结尾。',branch='EXAMPLE')
ov('N0525','O5','本人维护及稳定性保障，不是明示开发可靠性机制。',metric='DUTY_OWN_USE')
add('N0525','V2_AGENT_WORKFLOW','SEPARATE','COLLABORATION_OBJECT',2,'参与Agent系统模块开发保留技术提及和参与承担。')
register(list(R.values()),'Astra_v3_boundary_sw_g')
