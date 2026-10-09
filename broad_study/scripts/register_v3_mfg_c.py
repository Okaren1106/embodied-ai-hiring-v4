from astra_review_tools import *
JUD={
'N0103':'EMC测试本人执行，整改配合与委外跟进分开；CE在本文展开为骚扰电压，不能计认证。XMind与ADB目录外，不补品牌或安全标准。',
'N0004':'逐句核对实习生完整文本，协助测试和协作部门仍不算独立本人技术职责；与N0018存在措辞和受众差异，不当同一广告删并。',
'N0017':'MCU测试脚本是本人开发，固件为测试对象而非本人开发固件；要求及加分分段正确。通信协议及万用表/示波器斜线缺少任选或全部证据，应U；至少一种语言有明示任选可判。',
'N0606':'导航交互测试、Linux/ROS/RViz调查工具与优先测试经验区分。测试阶段故障定位不补生产运维事件项；仪器例示保留。',
'N0585':'全文重复段不重复计广告。APQP/IPD、8D/5Why仍关系U；FMEA两种子型同上位项，质量标准两种同项可判。PPAP参与另列，Minitab只优先。',
'N0237':'供应商质量与交货服务评价并存，后者支持供货管理；工艺物料范围不等于加工能力。质量体系类别要求直接成立，不应因其具体标准示例而把类别降为例示。',
'N0253':'本人Python使用与资格优先同时存在；测试平台开发、标定开发和一般要求分开。补本人制定研发测试规范/流程的SOP方法，研发排障未当运行事故。',
'N0250':'本人设计测试方法、工装并执行可靠性测试；优先工装开发经验与一般测试经验分开。工作原理仅例示部件，不补未命名工具。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
for eid in ['N0017:O3','N0017:O4','N0017:10:0','N0017:10:1','N0017:10:2','N0017:10:3']:
 R['N0017']['evidence_overrides'].append(dict(evidence_id=eid,branch='UNRESOLVED',reason='局部斜线连接具体工具/协议，外层等示例未解决内部任选或并列，按同目录规则保留关系未知。'))
R['N0237']['evidence_overrides'].append(dict(evidence_id='N0237:8:1',branch='UNCONDITIONAL',reason='熟悉质量管理体系标准这个上位类别直接明确；ISO9001/IATF16949均在该类，不用子型例示关系降低上位类别。'))
R['N0253']['additions'].append(dict(code='V2_SOP_OPERATION',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote='制定研发阶段测试流程、测试规范、性能验收标准、迭代准入/退出机制',reason='本人编制质量操作流程明确，补全非关键词的专业方法证据。'))
register(list(R.values()),'Astra_v3_mfg_c')
