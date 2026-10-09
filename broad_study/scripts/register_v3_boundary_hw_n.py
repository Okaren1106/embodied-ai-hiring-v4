from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0437':'视觉硬件Staff：条件定制规格保留CONDITIONAL，标定标题仅GENERAL未知；GMSL2/3为同一协议族版本。',
'E0436':'视觉硬件Staff：独立身份回读同文职责要求；协议版本与跨语言斜线分别处理，算法与工具语境未知不扩全广告。',
'E0391':'HRI电子：PCB方法使用、测试计划开发/测试执行明确；DVT/PVT均为验证评测，供应商本人管理另补。',
'E0397':'互连经理：回读at least two标题，领域任选保留；FCC/CE同认证族但仍受外层任选；明确线束和屏蔽架构责任。',
'E0375':'执行器固件：回读EDUCATION and/or EXPERIENCE并无优先标题；BLDC及其他无刷电机同上位，安全故障机制为本人开发。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for r in ['E0437','E0436']:ov(r,'ADD2','GMSL2与GMSL3均为同一GMSL族；e.g.保留示例。',branch='EXAMPLE')
ov('E0391','O1','PCB为设计方法，电子板开发应用该方法。',metric='DUTY_OWN_USE')
ov('E0391','O8','DVT/PVT均为验证测试计划，不影响评测上位及明确develop动作。',branch='UNCONDITIONAL')
ov('E0391','1:0','EMI/EMC属于同一兼容方法族。',branch='UNCONDITIONAL')
R['E0391']['additions'].append(dict(code='V2_PROCUREMENT',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote='Manage 3rd party relationships with vendors, contract manufacturers, and external design services.',reason='明确本人供应商关系管理，区别仅沟通设计要求。'))
ov('E0397','O1','设计flex-PCB应用PCB设计方法。',metric='DUTY_OWN_USE')
ov('E0397','3:0','标题本身不证明开发方法，以下正文明确应用屏蔽接地。',metric='DUTY_OWN_USE',quote=RAW[RID['E0397']]['full_description'].splitlines()[16])
ov('E0397','ADD1','明确制定屏蔽接地架构，属于EMC设计方法应用。',metric='DUTY_OWN_USE')
ov('E0397','4:1','FCC与CE均为冻结产品合规族；外层至少两个领域仍使此项任选。',branch='CHOICE')
for e in ['O22','O23']:ov('E0375',e,'BLDC和其他无刷电机同属执行器/电机概念。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_hw_n')
