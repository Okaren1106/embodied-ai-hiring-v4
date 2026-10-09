from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0783':'网络方案：Python/Bash具体语言关系未知；网络清单不擅自推TCP/IP；标题证据改为实际分诊。',
'N0778':'地图方案：Linux/Ubuntu同一目录上位；PCL/Open3D与项目工具受such as加or，标定是任选优先经验。',
'E0515':'制造设备：支持工程验证与本人操作验证设备分开；gauge R&R为合作验证；SOP建设和生产排障明确。',
'E0471':'设施维护：安全消防为等系统例示，Office一般要求明确；没有把设施系统当机器人算法。',
'E0564':'采集布景：库存职责、库存或物流加分与现场安全均有对应直接证据；没有把布景支持补成模型/采集工具研发。',
'E0472':'现场技师：稳定性验证是评测使用非开发；Proficient in为能力而非动作；并列工单软件不记任选。',
'E0570':'葡语技术协调：Diferenciais加分标题已核读；动捕与机器人/无人机经验是任选；写标定SOP不等于开发标定方法，实际校准另有直接证据。',
'E0569':'西语技术协调：Nice to have标题已核读；与葡语各自原文定位，不凭译文自动通过；标定实际执行与文档对象分开。',
'N0906':'设施维修：回读重复正文并与N0907校对；帮助库存为支持，SOP职责例示，Google Suite must例示。',
'N0908':'设施维修：同系列原文字节核对，独立保留广告；SOP语境与Google Suite强度一致处理。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0783','15:0','Python/Bash关系未明。',branch='UNRESOLVED')
ov('N0783','3:0','原为标题，改引具体根因定位F15。',metric='DUTY_OWN_USE',quote=line('N0783',15))
ov('N0778','O4','Linux和Ubuntu属于同一上位，不能因斜杠产生此条目未知。',branch='UNCONDITIONAL')
for e in ['6:0','6:1','22:0','22:1']:ov('N0778',e,'such as与or同时存在。',branch='CHOICE_AND_EXAMPLE')
ov('N0778','17:0','geospatial等或calibration workflows任选。',branch='CHOICE')
add('N0778','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line('N0778',13),'本人排查地图工作流。')
for e in ['O1','3:0']:ov('E0515',e,'Support engineering teams流程验证。',metric='SEPARATE',branch='SUPPORT')
add('E0515','TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL',line('E0515',8),'另有本人在初始流程验证中操作设备。')
add('E0515','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line('E0515',5),'本人为生产问题排查第一联系人。')
ov('E0471','O5','fire protection等建筑系统示例。',branch='EXAMPLE')
for e in ['O6','O7']:ov('E0472',e,'Verify现场稳定性与反馈，是验证使用非开发。',metric='DUTY_OWN_USE')
for e in ['O5','1:0']:ov('E0472',e,'Proficient in表述技能能力，虽列职责段，也非具体执行动作。',metric='GENERAL')
ov('E0472','O4','CATIA或CAD全部属于CAD上位。',branch='UNCONDITIONAL')
ov('E0472','2:0','such as but not limited to工具例示。',branch='EXAMPLE')
for e in ['4:0','4:1']:ov('E0472',e,'逗号并列无任选词。',branch='UNCONDITIONAL')
for r,e,n in [('E0570','4:1',11),('E0569','5:1',8)]:
 ov(r,e,'文档包含标定，不是开发标定算法方法。',metric='SEPARATE',branch='DOCUMENTATION_OBJECT')
 add(r,'V2_CALIBRATION','DUTY_OWN_USE','UNCONDITIONAL',line(r,n),'明确本人组装并校准采集站。')
ov('E0570','7:0','VR/AR、motion capture、robotica ou drones跨经验任选。',branch='CHOICE')
ov('E0569','9:0','VR/AR、motion capture、robotica o drones跨经验任选。',branch='CHOICE')
for r,n in [('N0906',38),('N0908',39)]:
 ov(r,'O1','Help to maintain库存，与团队协作。',metric='SEPARATE',branch='SUPPORT')
 ov(r,'1:0','such as SOP为职责例示。',branch='EXAMPLE')
 ov(r,'2:0','Must且including不限于软件示例。',metric='REQUIRED',branch='EXAMPLE')
 add(r,'V2_SOP_OPERATION','GENERAL','EXAMPLE',line(r,n),'一般资格含操作维护程序例示。')
register(list(R.values()),'Astra_v3_boundary_deploy_e')
# 已读系列全文定位表明N0907对象同为仓储设施维护；此为Q2任务层修订，冻结主职能不动。
r='N0907'; q=RAW[RID[r]]['full_description'].splitlines()[23]
assert q==line('N0908',24)
register([dict(reading_id=r,review_mode='FOLLOWUP',judgment='与N0906/N0908维修概述逐字节一致，主任务统一为设施与设备维护，不由公司机器人背景推机器人维修。',task_override=dict(task='FACILITY',quote=q,reason='主要对象明确为机械/物料搬运/自动化设备、工具、建筑和场地；与相同原文系列一致。'))],'Astra_v3_deploy_task_consistency')
