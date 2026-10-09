from astra_review_tools import *
decisions={
'E0258':'PSMNet/GwcNet/GANet分别在职责模型清单和至少一种资格清单；均在TC_ML_MODELS上位类，已有独立一般模型要求及职责证据，无需再改状态。',
'E0317':'两处Provided for eligible roles分别是搬迁与年度奖金福利，无技术语境。',
'E0325':'两处Provided for eligible roles是福利，未作为研究技术要求。',
'E0326':'重复福利适用说明无技术测量影响。',
'E0328':'重复福利适用说明无技术测量影响。',
'E0329':'重复福利适用说明无技术测量影响。',
'E0345':'重复福利适用说明无技术测量影响。',
'E0348':'重复福利适用说明无技术测量影响。',
'E0353':'重复福利适用说明无技术测量影响。',
'E0355':'重复福利适用说明无技术测量影响。',
'E0356':'重复福利适用说明无技术测量影响。',
'E0358':'重复福利适用说明无技术测量影响。',
'E0365':'重复福利适用说明无技术测量影响。',
'E0419':'公司概况在广告开头重复，仍为背景，不变成本人职责或要求。',
'N0350':'职责被原采集正文重复放在第一个任职资格标题下，随后另有实际任职资格段；按动作/经验句语义区分。现有一般视觉模型资格在后面的真实经验段足以支持，模型小型化加分也已有，无新增状态。',
'N0918':'可靠性设计能力句在同一Qualifications段重复，无语境切换；广告-标签去重一次。',
'N0980':'CI全称在职位介绍连续重复，始终是持续改进；不存在由再次出现变为CI/CD。',
}
register([dict(reading_id=r,review_mode='FOLLOWUP',judgment=j) for r,j in decisions.items()],'Astra_v3_repeated_context_audit')
save_json('verification/V3_repeated_context_acceptance.json',dict(scope_full_reviews=372,screened_groups=22,screened_ads=18,content_reviewed_ads=18,changed_ad='E0361',other_decisions=decisions,correction='保留同字段每次出现及原行号，跨字段映射优先保留首次出现，不能去掉重复句所在标题语境。',limitation='这是阅读展示缺陷的定向复核，不是总体编码误差率；之后新增广告使用修正后的阅读器。'))
