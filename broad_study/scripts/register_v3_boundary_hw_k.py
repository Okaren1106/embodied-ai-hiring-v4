from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0285':'SoC硬件：看护设计域的承担方式不足以确认本人使用USB，限该职责未知；仅SoC硬件不自动推嵌入式固件概念。',
'E0283':'关节固件：实际开发为电机软件及SDK；电机对象使用和嵌入式软件开发区分，C/C++与通信斜线未知保留。',
'E0272':'线束：明确售后分析及CREO能力，供应商沟通不推采购；行业标准原名保留。',
'E0226':'音频电路：PCB布局为指导，声学结构为协同；频谱仪要求明确，音频杂音不自动推EMC。',
'E0184':'RTOS：嵌入式平台开发与单元/集成测试明确；通过测试保证可靠性不等于另行开发可靠性方法或功能。',
'E0173':'电源硬件：实体电机开发有直接证据，功率器件与测试电源仪器区分；功率电源或无刷电机保留跨概念任选。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('E0285','1:0','看护USB等设计域未明确本人实际使用动作；不把责任管理直接变为技术使用。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
ov('E0283','O4','开发对象明确为电机软件；使用电机对象，不据此声称开发电机本体。',metric='DUTY_OWN_USE')
ov('E0184','O6','可靠性是本人测试目的，无另行开发可靠性功能或方法的动作。',metric='DUTY_OWN_USE')
register(list(R.values()),'Astra_v3_boundary_hw_k')
