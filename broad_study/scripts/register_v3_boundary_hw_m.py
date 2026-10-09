from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0389':'Senior电子：回读重复条款和标题；will be expected to develop是明确未来本人文档职责。PCB/PCBA、DFM/DFA、EMC族内部不再未知。',
'E0426':'Staff电子：功能安全新增职责有效；PCB设计方法应用而非方法开发；供应商关系管理为明确本人工作。',
'E0398':'计算感知经理：招募与指导对象不当本人开发；直接定义电源架构和领导板卡开发分别有证据，PCB采用方法使用。',
'E0445':'Staff线束：寿命模型开发明确；屏蔽架构是EMC方法应用；供应商为与采购协作。',
'E0420':'Senior线束：参与DFMEA与本人hands-on验证区别清楚，EDA的任选示例保留，热降额不扩散热设计。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for r in ['E0389','E0426']:
 ov(r,'O1','设计PCBA实体是PCB设计方法使用。',metric='DUTY_OWN_USE')
 ov(r,'O4','PCB/PCBA设计均属于PCB设计能力。',branch='UNCONDITIONAL')
 for e in ['2:0','2:1']:ov(r,e,'斜线连接同一冻结方法族内各成员，上位关系确定。',branch='UNCONDITIONAL')
 R[r]['additions'].append(dict(code='V2_PROCUREMENT',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote='Manage 3rd party relationships with vendors, contract manufacturers, and external design services.',reason='明确本人管理供应商和合同制造关系，区别仅协作。'))
ov('E0398','ADD1','领导具体板卡开发使用PCB设计方法，不是开发方法本体。',metric='DUTY_OWN_USE')
ov('E0445','ADD2','屏蔽接地用于互连架构设计，为方法应用。',metric='DUTY_OWN_USE')
register(list(R.values()),'Astra_v3_boundary_hw_m')
