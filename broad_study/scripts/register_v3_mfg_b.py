from astra_review_tools import *
JUD={
'N0203':'已读完整制造质量职责与资格。根因方法、首件、质量工具及MES/MOM关系分开；加分段不回填一般要求。SIP巡检规范由本人制定优化，补操作质量流程开发。',
'N0521':'本人测试策略、用户视角质量与测试执行有据；liunx在明确系统语境沿用Linux拼写归一。未把方法协助提升为本人独立开发。',
'N0519':'设计FMEA本人主导，控制/融合/结构是推动研发预防的对象。质量数据库保留数据概念但不补数据库品牌、训练管线或SQL。',
'N0457':'校招执行与协助层次已核；测试执行本人明确，平台搭建、标定与SOP仅协助参与。至少一种加如限定语言分支；断句由第二条接续，未当截尾。',
'N0454':'学习与执行分开：标定明确执行，8D、根因、质量体系学习/辅助不提升。办公软件未命名厂商，不填微软。',
'N0636':'供应商质量职责不等于采购谈判；APQP/PPAP明确。加工方法上位族要求直接成立；三坐标是设备举例，保持示例。',
'N0657':'物料供货结果与库存责任明确，供应计划并非仓库搬运。Ofhce按明确办公软件语境保留归一，但不推出Excel。供货、库存与采购协同分开。',
'N0018':'完整文本主体是协助/参与测试，未把协作部门的机械控制嵌入式技术计为本人使用；资格中的辅助测试经验可保持一般要求。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
R['N0636']['evidence_overrides']=[dict(evidence_id='N0636:9:1',branch='UNCONDITIONAL',reason='压铸注塑CNC钣金均为加工成型族组成；熟悉工艺上位能力直接被要求，不把整个族降为示例。')]
R['N0203']['additions']=[dict(code='V2_SOP_OPERATION',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote='制定和优化SIP、巡检标准、缺陷判定标准及质量控制方案',reason='明确编制检验规范和质量操作流程，符合冻结操作规程与数据质量方法项。')]
register(list(R.values()),'Astra_v3_mfg_b')
