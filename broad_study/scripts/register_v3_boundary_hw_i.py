from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0140':'网络BSP：使用Ethernet开发驱动不等于开发Ethernet协议；Linux职责任选和经验确定分别保留。',
'N0019':'硬件校招：本人核心电路设计和主导测试有明确动词，不能因校招下调；控制器符合冻结控制条目。',
'N0609':'大功率驱动：热管理、安规及EMC设计明确；测试规范开发和供应商协作分列。',
'N0325':'触觉产品硬件：外购部件只作采购/被测对象，CAN与CANFD在同一协议族不再未知。',
'N0290':'嵌入式模块：本人功能验证与协助产品测试分开；协议跨类斜线保持未知。',
'N0338':'线束：职责栏中能力语句仍属一般要求；屏蔽接地用于制定具体线束规范，不等于开发EMC方法本体。',
'N0322':'线束：与另一广告分别保留；一般知识和优先资格清楚，EMC方法应用与新方法开发分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('N0325','5:0','CAN/CANFD为冻结同一CAN协议族，上位确定；如为示例。',branch='EXAMPLE')
for r in ['N0338','N0322']:ov(r,'ADD3','应用屏蔽接地原则制定线束规范，未明确开发电磁兼容新方法。',metric='DUTY_OWN_USE',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_hw_i')
