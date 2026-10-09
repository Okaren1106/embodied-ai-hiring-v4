from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0308':'内容主编本人写作编辑与团队招聘；一般AI辅助出版不推Agent工作流或具体模型工具，营销一般资格重锚真实内容能力。',
'N0861':'整体营销负责人本人创作与运营，明确硬性和优先经历分开；AI营销工作流和数据审校治理不等机器人作业安全。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0308','1:0','Partner with为协作；本人内容创作另有具体句补入。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0308','3:0','原generic corporate marketing为不希望的反例，改真实专业要求。',metric='GENERAL',quote='Mastery of modern content ecosystems (web, newsletters, social, video, distribution loops) and how to package stories for maximum reach and impact.')
add('E0308','V2_MARKETING','DUTY_OWN_DEVELOP','UNCONDITIONAL','Write, edit, and oversee a diverse portfolio of written, video, and audio content including long-form essays, short-form takes, technical explainers, customer case studies, clips, newsletters, and flagship industry reports.','本人写作编辑，非仅部门合作。')
add('E0308','V2_HR','DUTY_OWN_USE','UNCONDITIONAL','Recruit, manage, and mentor a world-class team of internal content strategists and creatives','本人招聘团队。')
for e in ['O5','O6']:ov('N0861',e,'人类审校、来源验证、保密与数据处理治理，并无明确产品系统或作业安全技术目标。',metric='SEPARATE',branch='INFORMATION_GOVERNANCE')
ov('N0861','1:0','标题不足，重锚本人创作动作。',metric='DUTY_OWN_DEVELOP',quote='Personally create content across videos, demos, technical explainers, launches, web, presentations, and sales enablement.')
ov('N0861','2:0','Role Scope标题不足，重锚本人营销活动。',metric='DUTY_OWN_USE',quote="Design and run focused account-based and industry campaigns that connect Dexterity's technical differentiation to real operational problems.")
for e in ['9:0','10:0']:ov('N0861',e,'Qualifications Required段。',metric='REQUIRED')
R['N0861']['catalog_gap_notes']=['明确AI-driven营销自动化和人工审校要求；目录V2_AGENT_WORKFLOW要求智能体/检索增强/工具调用等，不把所有AI工具自动视作Agent。报告保留原文案例但不混进Agent比例。']
register(list(R.values()),'Astra_v3_commercial_d')
