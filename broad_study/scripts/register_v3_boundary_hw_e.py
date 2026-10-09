from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0428':'计算平台硬件：SOR编写在任职要求中，保留一般能力；平台品牌目录外，无依据补软件/PCB工具。',
'N0423':'嵌入式模块：测试执行和测试用例开发分列；MCU任选都属嵌入式能力，不能形成上位任选。',
'N0376':'磁定位前端：EMC/EMI同方法条目；PCB Layout仅指导，不能直接作本人布局；量产动捕产品经验不等同动捕采集技能。',
'N0218':'机器人硬件：回读末尾涉及技术方向标题，无要求/职责归属；旧技术概念也应与新工具同样记语境未知，避免旧新标签不一致。',
'N0197':'无线BSP：Linux内核与C/Shell明确，ROS2是优先跨项目选择；频谱分析泛工具不推具体仪器。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O7','O8']:ov('N0423',e,'不同单片机开发均属嵌入式上位。',branch='UNCONDITIONAL')
ov('N0376','O1','原文仅PCB Layout指导，无本人布线设计；具体PCB能力要求另在评审能力。',metric='SEPARATE',branch='GUIDANCE_OBJECT')
ov('N0376','2:2','EMC与EMI在同一方法条目。',branch='UNCONDITIONAL')
R['N0376']['additions'].append(dict(code='SK_PCB',metric='GENERAL',branch='UNCONDITIONAL',quote='能主导高精度模拟板 Layout 评审。',reason='明确板级布局评审知识能力。'))
for e in ['O15','O16','O17','O18','O19']:ov('N0218',e,'末尾涉及技术方向未明确归属，不能用SEPARATE无条件漏掉未知。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED'])
register(list(R.values()),'Astra_v3_boundary_hw_e')
