from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0951':'FAR驱动电路：BLDC/PMSM同执行器上位，CE/FCC同产品合规上位；电机控制仅感测电路应用对象，不是控制算法经验。',
'E0048':'整机线束：工具之一任选、CATIA/SolidWorks关系未知；直接EMC验证及SOP/治具方案成立，未由高速接口推目录外技术。',
'N0739':'人形嵌入式：CAN/CAN-FD同协议族但仍受上层or约束；安全标准例子属于同一上位；保留上层模型协作与本人驱动开发差别。',
'N0444':'嵌入式实习：参与功能实现不能新增独立开发正例；Rust或其他语言上位明确，机器人/无人机等均是嵌入式项目经验。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('N0951','O24','BLDC和PMSM均执行器，上位要求明确。',branch='UNCONDITIONAL')
ov('N0951','O25','current sensing circuit/PCB integration用于motor control，不证明控制算法知识。',metric='SEPARATE',branch='CIRCUIT_APPLICATION_OBJECT')
ov('N0951','15:1','CE/FCC都在产品合规条目，斜杠不影响上位。',branch='UNCONDITIONAL')
ov('N0739','25:5','CAN和CAN-FD同协议族；受多类接口or选择约束。',branch='CHOICE')
ov('N0739','32:0','明确functional safety standards经验，所列ISO都属于该上位。',branch='UNCONDITIONAL')
ov('N0444','O3','Rust或其他编程语言都属语言泛称。',branch='UNCONDITIONAL')
ov('N0444','O16','机器人/无人机/智能车或类似嵌入式系统都在嵌入式经验上位。',branch='UNCONDITIONAL')
ov('N0444','ADD1','参与需求分析实现，没有独立负责声明；与O8支持边界一致。',metric='SEPARATE',branch='PARTICIPATION')
register(list(R.values()),'Astra_v3_boundary_hw_c')
