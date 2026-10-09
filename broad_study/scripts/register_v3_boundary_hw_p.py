from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0406':'PCB Layout：方法应用与IPC能力明确；DFM/DFA、EMC/EMI和CID级别不影响上位确定性；thermal reliefs不足以确定散热开发。',
'E0392':'电源：PMSM/BLDC均为电机控制且处于including示例；本人供应商管理明确，板卡方法应用。',
'N0972':'Atlas经理：管理团队开发执行器不能当本人执行器开发；失效修复另有明确责任，FMEA子类和EMC族内部确定。',
'N0738':'联邦嵌入式：已展开全部重复技术句回读；协议和仪器闭合列表不凭括号自动标示例，含and similar的要求另保留示例。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('E0406','O2','板卡设计应用PCB工程方法。',metric='DUTY_OWN_USE')
ov('E0406','O8','thermal reliefs具体对象不是明确热管理开发；仅该职责开发切片未知。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP'])
for e in ['4:0','9:0','10:0']:ov('E0406',e,'斜线为同一冻结方法族内部各项。',branch='UNCONDITIONAL')
ov('E0406','11:0','CID或CID+均为IPC体系资格，该上位不存在任选。',branch='UNCONDITIONAL')
ov('E0392','O1','板卡设计应用PCB工程方法。',metric='DUTY_OWN_USE')
ov('E0392','O7','PCB与PCBA同设计方法条目。',branch='UNCONDITIONAL')
for e in ['O17','O18']:ov('E0392',e,'PMSM/BLDC均为电机及控制，但处于including示例列表。',branch='EXAMPLE')
R['E0392']['additions'].append(dict(code='V2_PROCUREMENT',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote=RAW[RID['E0392']]['full_description'].splitlines()[14],reason='明确本人管理供应商和合同制造关系。'))
ov('N0972','O10','Manage a team to design明确为团队交付，不能当本人执行器技术开发。',metric='SEPARATE',branch='TEAM_DELIVERY')
for e in ['O6','O7']:ov('N0972',e,'DFMEA/PFMEA均为FMEA族；like保留示例。',branch='EXAMPLE')
for e in ['O17','O18']:ov('N0972',e,'功率电子和电机驱动均属功率电子上位。',branch='UNCONDITIONAL')
ov('N0972','1:0','EMC和EMI均为冻结兼容方法族。',branch='UNCONDITIONAL')
for e in ['O7','O25','O26','O27']:ov('N0738',e,'调试工具括号为并列清单，没有示例或任选标记。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_hw_p')
