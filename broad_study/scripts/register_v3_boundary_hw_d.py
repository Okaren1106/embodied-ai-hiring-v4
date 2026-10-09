from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0932':'电气主管：架构定义本人承担，带团队做固件不能替代本人开发/PLC使用；EMI/EMC同一上位，DFM/DFT仍是不同条目。',
'E0464':'电机驱动电路：PCBA设计和完整性设计为方法使用；控制器硬件与电机本体开发分开；BLDC/PMSM同执行器上位。',
'N0435':'嵌入式经理：原文明确负责功能开发与主导SDK设计，保留本人技术开发，不仅根据职位名称推领导关系；RTOS仅泛称。',
'N0433':'数字板卡：负责或指导调测在本人执行关系上未解；可生产/可测试性是设计方法使用，板卡设计不作评测执行。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O8','1:0']:ov('N0932',e,'Lead firmware team to develop是团队技术管理对象，未明确本人固件开发或PLC操作。',metric='SEPARATE',branch='TEAM_MANAGEMENT_OBJECT')
ov('N0932','11:0','EMI与EMC同完整性兼容方法条目。',branch='UNCONDITIONAL')
ov('E0464','O1','SK_PCB为PCB设计方法，本人使用该方法设计板卡。',metric='DUTY_OWN_USE')
ov('E0464','O4','设计电机控制板卡，不是开发电机/执行器本体。',metric='SEPARATE',branch='CIRCUIT_APPLICATION_OBJECT')
ov('E0464','O12','BLDC/PMSM均属电机/执行器上位。',branch='UNCONDITIONAL')
ov('E0464','1:0','使用完整性设计方法管理信号/噪声，没有开发该方法本身。',metric='DUTY_OWN_USE')
ov('N0433','ADD3','负责或指导不能判断是本人调测还是指导他人；不作为本人使用任选技术正例。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
register(list(R.values()),'Astra_v3_boundary_hw_d')
