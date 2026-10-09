from astra_review_tools import *
register([dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0478':'滚齿刮齿为本人加工，CNC车铣仅as needed条件；机械图纸与标准知识、加工经验优先分层正确。',
'E0479':'电芯电池包是采购对象，供应链经验不推出技术研发；DFX泛称不自动当DFM，lean team非精益方法。',
'E0553':'危险品物流安全与电池货物对象分开；海关法务和成本分析本人承担，AI工具泛称未具体化成模型或工具品牌。',
'E0518':'物料计划中的MRP原理与MRP软件不同；采购缓缺为support，ERP/MRP未知及SAP/Oracle优先任选保留。',
'E0459':'供需预测模型和内部测试需求不是ML或本人评测；S&OP非SOP，软件评估协助与一般软件熟练度分离。',
'E0512':'物流流程建设、团队招聘和设备追踪明确；运输应急不推机器人技术维护，项目工具是具名示例。',
}.items()],'Astra_v3_boundary_mfg_w')
