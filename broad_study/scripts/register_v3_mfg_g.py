from astra_review_tools import *
JUD={
'E0345':'制造系统接口架构使用ERP/MES/PLM既有平台，不等于开发这些平台；要求中架构概念后的括号是具体子系统例示。NetSuite优先与迁移协作分开；FMEA两子型仍同类。',
'E0396':'自制工装和DAQ架构开发明确；寿命/疲劳是评测目标，不能等同研发可靠性机制。LabVIEW在NI/LabVIEW内部斜线关系不明，保留U。学历with截断局限在学历子句，未补造该条件。',
'E0390':'电气持续改进与DFM/DFT流程开发成立。Define and support且as needed的测试句不能确认本人执行/开发安全可靠性方法，改为条件关系下的责任未知；另有明确装配指引开发不受影响。',
'N1010':'本人CNC编程与操作、工艺知识明确，CAM品牌保留任选示例。优先regulated quality systems是直接质量体系经验，上位类不因括号标准例子降级。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
for eid in ['E0345:O1','E0345:1:0','E0345:2:1','E0345:2:2']:
 ov('E0345',eid,'设计制造系统架构及平台间接口表明集成应用，不证明开发所命名ERP/MES/PLM平台本身。',metric='DUTY_OWN_USE')
for eid in ['E0345:O3','E0345:O5','E0345:O13','E0345:O14','E0345:4:0','E0345:4:1']:
 ov('E0345',eid,'具体系统/工具位于上位能力后的括号列举，未明示全部；按既定括号例示边界。',branch='EXAMPLE')
ov('E0396','E0396:O16','开发测试脚本、执行寿命疲劳测试，可靠性是评估目标；非本人研发可靠性机制。',metric='DUTY_OWN_USE')
ov('E0396','E0396:5:0','外层like/or不消除National Instruments/LabVIEW内部关系歧义；不强推该具体软件被任选。',branch='UNRESOLVED')
for eid in ['E0390:O6','E0390:O7','E0390:O8','E0390:3:0']:
 ov('E0390',eid,'Define and support测试没有确定本人执行还是协助的具体方法责任；as needed条件保留，未知仅作用于该职责条件语境。',metric='UNKNOWN',branch='CONDITIONAL',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP'])
ov('N1010','N1010:21:0','直接要求regulated quality systems经验；例示是内部标准编号，不是上位质量体系经验的存在。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_mfg_g')
