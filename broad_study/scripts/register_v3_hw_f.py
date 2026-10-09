from astra_review_tools import *
R=[dict(reading_id='N0917',review_mode='FULL_SOURCE_AND_CODING',judgment='生产固件on-call与开发/HIL都明确，不能因实验工作排除运行支持。CAN/CAN-FD属同协议族，上位CAN有证据，保留外层including例示。语言at least one与安全标准子例区分。',evidence_overrides=[dict(evidence_id='N0917:2:0',branch='EXAMPLE',reason='CAN与CAN-FD均在CAN协议族内，同族斜线不造成该族未知；外层including仍是职责例示。')]),
dict(reading_id='N0936',review_mode='FULL_SOURCE_AND_CODING',judgment='电气系统要求规格与测试方案是应用工程方法；系统/PCB实际设计保留。现场发布后的故障例示受support支配，不能升级独立运行排障。',evidence_overrides=[
dict(evidence_id='N0936:O7',metric='DUTY_OWN_USE',reason='开发验证计划与测试程序文档，没有明确测试工具或新方法开发。'),
dict(evidence_id='N0936:ADD2',metric='DUTY_OWN_USE',reason='为电气产品编制规格和验证程序是需求工程应用，不是开发需求工程方法本身。'),
dict(evidence_id='N0936:1:0',metric='SEPARATE',branch='COLLABORATION_OBJECT',reason='support release to production and field deployment支配including troubleshooting；没有独立拥有现场排障责任的其他原句。')]),
dict(reading_id='N0661',review_mode='FULL_SOURCE_AND_CODING',judgment='Tegra相机Linux驱动本人开发，标定参数API不是执行标定。资格全部Preferred，内部C/C++未知；vendor requirements在Own end-to-end句另有本人责任，补独立例示方法，不只依合作句。',additions=[dict(code='V2_REQUIREMENTS_ENGINEERING',metric='DUTY_OWN_USE',branch='EXAMPLE',quote='Own camera systems end to end, including vendor requirements, sensor/module selection, hardware bring-up, software integration, debugging, calibration, validation, and long-term maintainability.',reason='本人端到端拥有范围明确包括供应商需求；详细相机接口约束在全文下一句给出，区别仅跨团队合作。')])]
register(R,'Astra_v3_hw_f')
