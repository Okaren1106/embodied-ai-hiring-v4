from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0642':'驱动板：本人板卡及PCBA测试明确；通信斜线与产品/关节经验斜线保留未知；供应链导入不扩采购。',
'N0656':'嵌入式：裸机与RTOS均为嵌入式，上位不应未知，具体实时分支仍未知；协议拼写不擅自补正。',
'N0645':'实习硬件：配责动词不清所影响的测试本人承担仍未知；协助条款不改独立承担，宣传VLA不计岗位要求。',
'N0007':'硬件实习：协助职责与明确独立仪器使用能力分列；任意一种EDA和接口等示例保留。',
'N0016':'嵌入式校招：写测试报告只证明文档交付，不证明本人执行评测；Python经验与C/C++不清关系分列。',
'N0171':'BSP：Linux或RTOS是职责分支，但独立Linux驱动经验一般要求确定；协议使用而非协议开发。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O12','O13']:ov('N0656',e,'裸机和RTOS开发均为嵌入式上位，斜线不影响该上位概念。',branch='UNCONDITIONAL')
ov('N0016','O7','撰写测试报告是记录工作，不明示本人实施评测。',metric='SEPARATE',branch='DOCUMENTATION_OBJECT')
register(list(R.values()),'Astra_v3_boundary_hw_h')
