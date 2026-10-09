from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0166':'相机：主导或参与的本人PCB方法使用未知；EMC/EMI同方法族已可确定；不能由高速电路经验补信号完整性要求。',
'E0155':'整机电气：安全回路本人设计；制定接地屏蔽规范是EMC方法应用，协同整改另列。',
'E0154':'实时固件：三种控制器经验均属控制上位；具体平台和接口任选保留。',
'E0147':'电子板卡：PCB与EMC为方法使用；支持电机驱动不证明开发电机；MCU/SoC外设知识同嵌入式上位。',
'E0142':'触觉硬件：本人感知算法及测试/标定设计执行明确；支持抓取功能不直接计本人抓取算法开发。',
'E0359':'Staff固件：回读完整敏捷工具句，Git/Jira/CI明确优先；HIL框架、通用PCB阅读和EtherCAT额外优先均保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('E0166','O1','PCB方法使用和本人承担分别判断，主导或参与仍未知。',metric='DUTY_OWN_USE',branch='UNRESOLVED')
ov('E0166','O2','PCB设计或Debug都需要PCB设计知识，不是是否具有PCB能力的任选。',branch='UNCONDITIONAL')
ov('E0166','3:0','EMC与EMI是同一冻结兼容方法族。',branch='UNCONDITIONAL')
ov('E0166','ADD3','高速信号或解串器电路设计经验未明示信号/电源完整性分析。',metric='SEPARATE',branch='CIRCUIT_DESIGN_OBJECT')
ov('E0155','ADD2','应用接地屏蔽设计方法制定具体规范。',metric='DUTY_OWN_USE')
for e in ['O17','O18','O19']:ov('E0154',e,'机器人控制器、关节控制器、工业运动控制均属控制条目。',branch='UNCONDITIONAL')
ov('E0147','O1','设计板卡是使用PCB设计方法。',metric='DUTY_OWN_USE')
ov('E0147','O7','支持电机驱动的电子硬件，不直接证明开发电机本体。',metric='SEPARATE',branch='SUPPORTED_OBJECT')
ov('E0147','O12','MCU和SoC外设知识属嵌入式上位。',branch='UNCONDITIONAL')
ov('E0147','1:0','EMC与ESD抗扰验证在同一冻结方法族。',branch='UNCONDITIONAL')
ov('E0142','O3','传感器集成支持抓取功能，未明确本人抓取算法开发。',metric='SEPARATE',branch='SUPPORTED_FUNCTION')
register(list(R.values()),'Astra_v3_boundary_hw_l')
