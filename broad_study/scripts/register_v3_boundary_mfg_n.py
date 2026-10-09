from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0323':'Python脚本运行和熟练度期待分别是职责使用与一般要求；SOP执行、网络配置和Jira记录明确。',
'E0330':'手臂岗位内保留原文torso矛盾，测试平台与执行完整；control electronics和实验室电源不能自动泛化算法与功率电路知识。',
'E0334':'供应商使用8D和本人工具应用分开；实验室监督不等同本人测量或SOP执行，资格证书不替代方法经验。',
'E0346':'CAD产物设计、GDT应用与DFM并存；机械开发原引文仅GDT应用，重定位本人模型图纸创作。',
'E0312':'支援团队仍有本人测试执行、环境修改和PCBA修理，May开发保留条件；实验室电源仅工具。',
'E0335':'独立设计更新、测试标准和现场故障处理有证据；协作脚本及支持RCA保持协作，DFM/DFT关系未知。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
ov('E0330','O9','control electronics仅指被测电子硬件，不自动证明运动控制概念。',metric='SEPARATE',branch='ELECTRONIC_TEST_OBJECT')
for r,e in [('E0330','O20'),('E0312','O6')]:ov(r,e,'power supplies在实验室工具清单中为测试仪器，不自动扩为电源电路技术知识。',metric='SEPARATE',branch='INSTRUMENT_OBJECT')
for e in ['O7','3:0']:ov('E0334',e,'Oversee实验室并确保仪器/SOP优化是监督对象，未明确本人测试或执行SOP。',metric='SEPARATE',branch='MANAGED_LAB_OBJECT')
ov('E0334','9:0','证书要求保留质量资格类别；不以证书名称再推导方法经验要求。',metric='SEPARATE',branch='CREDENTIAL_OBJECT')
ov('E0346','O9','GDT应用句不能单独证明机械开发，改用本人创建CAD模型和工程图纸的明确职责。',metric='DUTY_OWN_DEVELOP',quote=RAW[RID['E0346']]['full_description'].splitlines()[10])
add('E0346','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',16,'本人持续改进设计流程和标准。')
add('E0312','SK_PCB','DUTY_OWN_USE','UNCONDITIONAL',12,'本人构建修改诊断修理PCBA，属于电路板工程应用。')
add('E0312','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL',23,'明确电子原型焊接经验，冻结类别包含加工装联。')
add('E0335','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',8,'明确本人诊断解决field运行现场问题，区别开发调试。')
register(list(R.values()),'Astra_v3_boundary_mfg_n')
