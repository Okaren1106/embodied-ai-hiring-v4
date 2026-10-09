from astra_review_tools import *
R=[dict(reading_id='N0862',review_mode='FULL_SOURCE_AND_CODING',judgment='物料整理与库存本人负责，测试和可靠性支持不提升本人研发；叉车资格是优先但目录外，仓库场地不证明软件工具。'),
 dict(reading_id='N0900',review_mode='FULL_SOURCE_AND_CODING',judgment='采购与供货战略、谈判成本知识明确；sourcing/procurement同属上位采购方法。制造子工艺列表含非加工物料，因此仍有真实方法任选；没有把采购板卡经验变成PCB设计。',evidence_overrides=[dict(evidence_id='N0900:2:0',branch='UNCONDITIONAL',reason='sourcing与procurement都在同一采购方法类别内，类别自身不是任选。')]),
 dict(reading_id='N0948',review_mode='FULL_SOURCE_AND_CODING',judgment='FAR原型实验室范围单列；普通原型调试不当生产运维，优先资格明确含实际运行监测诊断可保留。漏记本人根因分析、实验室作业指南开发及资格经验，补证据。',additions=[
 dict(code='V2_RCA',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote='Troubleshoot & root-cause across the full robot platform',reason='明确本人根因诊断，不因排除运行事故标签而一并漏掉根因方法。'),
 dict(code='V2_SOP_OPERATION',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote='author runbooks, FA reports, assembly guides and troubleshooting guides',reason='本人编制作业与装配/诊断操作指南，符合冻结SOP方法。'),
 dict(code='V2_SOP_OPERATION',metric='GENERAL',branch='UNCONDITIONAL',quote='Proven track record developing assembly procedures, test protocols, and technical documentation for prototype hardware',reason='资格明确包含装配规程和测试流程编制，非仅性格要求。')])]
register(R,'Astra_v3_mfg_f')
