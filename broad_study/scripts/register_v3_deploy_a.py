from astra_review_tools import *
JUD={
'E0085':'售前协作与自己承担客户培训、维修、流程制定分别判断；补运行排障和明确服务能力。',
'N0308':'工厂设备维修管理，不直接等客户现场；主导或参与可靠性改进关系未解，根因和运行事件独立责任明确。',
'N0371':'服务经营总监。规模售后经历明确硬性，满意度体系是一般经验要求，不能误作优先。',
'N0369':'交付体系总监，无关键词候选仍全文核对；明确交付标准与验收质量流程，不从管理经验推PMP资格或编程。',
'N0502':'机器人售前培训、故障维修及客户协助；C/C++内关系仍未解，Linux/ROS明确优先。',
'N0110':'机器人维修与精度校准本人职责；维修手册配合研发编写按协作，出差抢修安排不转换技术工具要求。',
'N0538':'景区现场运行和游客服务；标定/建图/验证是配合工程师，应保留协作对象而非本人独立实施。',
'E0265':'客户维修与培训本人职责；Ubuntu不在冻结Linux别名中，保留目录覆盖限制；ROS明示一般要求。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
add('E0085','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','负责设备交付后的技术答疑、故障诊断处理、安排售后维修等工作','明确交付后运行排障。')
add('E0085','V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','负责对客户进行产品软硬件培训（硬件操作、软件使用以及二次开发等），完成设备交付','明确客户培训协助。')
add('E0085','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','负责制定售后标准化服务流程，并完成过程管控','明确标准作业流程编制。')
ov('N0308','O2','主导或参与并列，无法唯一确定本人独立使用或开发可靠性改进。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP'])
add('N0308','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','全面负责工厂所有设备（机器人、数据采集硬件、传感器、采集平台、工装等）的维护保养、故障诊断与修复工作','本人运行设备维修责任。')
add('N0308','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','快速响应并组织处理设备突发故障，进行根因分析，实施纠正与预防措施，最大限度减少非计划停机','明确根因方法，非一般故障词。')
ov('N0371','3:0','一般任职要求没有优先措辞。',metric='GENERAL')
ov('N0371','O1','构建满意度闭环体系明确本人开发服务分析机制。',metric='DUTY_OWN_DEVELOP')
add('N0371','V2_SALES_CRM','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立服务成本模型与费效管理，规划增值服务产品，在保障服务质量的前提下持续优化服务成本','明确服务经营方法的体系建设。')
add('N0371','V2_SALES_CRM','GENERAL','UNCONDITIONAL','有服务业务经营管理经验：成本管控、服务定价、服务产品化（延保／服务合同／增值服务），有推动服务组织改善经营结果的实际案例','明确经营方法一般要求。')
add('N0371','V2_CUSTOMER_SERVICE','REQUIRED','UNCONDITIONAL','规模化量产设备售后管理经验（硬性要求）：必须具备 10 万台以上存量设备规模化的售后管理经验，熟悉服务网络布局、备件运营、维修产能规划与质量闭环等量产服务体系运作','明确硬性售后服务流程经验。')
add('N0369','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','统筹产品全生命周期交付管理（售前支持→部署→验收→转维），制定并持续完善交付标准与验收规范，在业务快速上量背景下保障交付时效与交付质量','原文明确制定交付与验收质量流程。')
add('N0502','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','机器人常见故障诊断、排查、维修工作','明确运行维修。')
add('N0502','V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','负责客户机器人软硬件培训服务及沟通协调，完成售前交付','明确用户培训支持。')
add('N0110','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','负责公司机器人和相关产品的故障诊断、维修','明确维修职责，不仅一般能力要求。')
add('N0110','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','梳理高频故障根因，形成专业文档资料，同时优化备件库存结构','明确根因梳理。')
add('N0110','V2_SOP_OPERATION','SEPARATE','COLLABORATION_OBJECT','配合内部研发团队搭建机器人维修标准化操作手册','配合搭建手册，未转为独立开发。')
for e in ['O1','O2','2:0']:ov('N0538',e,'明确配合部署工程师完成，独立承担关系不足。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0538','V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','负责现场用户引导，解答游客基本问题，管理现场互动秩序','明确服务沟通职责。')
add('N0538','V2_CUSTOMER_SERVICE','PREFERRED','EXAMPLE','有服务行业、景区、展会等现场服务经验优先','现场服务经验明确优先，场景为例示。')
add('E0265','V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','负责为客户提供产品技术培训与支持，负责设备的安装、调试、保养等','明确客户培训。')
R['E0265']['catalog_gap_notes']=['Ubuntu明示但冻结SK_LINUX只有Linux别名，本版不新增别名；ROS已有独立证据。']
register(list(R.values()),'Astra_v3_deploy_a')
