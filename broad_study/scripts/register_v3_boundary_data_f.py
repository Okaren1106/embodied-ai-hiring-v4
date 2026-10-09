from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0511':'外部数据合作：一般要求错引职责需重定位；golden set/ground truth均数据真值上位；采购履约要求应补全。',
'E0538':'数据质量项目：培训加分引用真实加分句；数据审核上位去无意义未知；补一般SOP及项目方法。',
'N0899':'数据质量经理：数据标注与质检同上位，遥操作是领域加分任选；SOP设计经验为一般要求。',
'E0603':'标注负责人：一般ML知识重定位到任职理解句，训练或微调或与ML团队合作的加分分支保留。',
'N0703':'主标注员：Preferred父语境有效；SOP明确编写及能力要求，执行QC不误作开发。',
'N0682':'数采PM：Microsoft Project误命中拒绝不应掩盖真实项目计划与运营方法；Preferred语境不降为General。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0511','O4','原误引职责，改一般翻译技术要求为运营指南经验。',metric='GENERAL',branch='UNCONDITIONAL',quote='Comfort working with engineering and ML stakeholders to translate technical requirements into operational guidance.')
for e in ['O8','O9','O12','O13']:ov('E0511',e,'golden/ground truth均数据真值；multi-vendor/region均标注运营上位。',branch='UNCONDITIONAL')
add('E0511','V2_PROCUREMENT','GENERAL','UNCONDITIONAL','Direct experience selecting, contracting, and managing external data vendors, including defining and enforcing SLAs.','明确供应商选择合同和履约要求。')
add('E0511','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Plan capacity and ramp with vendors to meet project timelines, including surge needs and new regions.','明确制定项目产能与进度计划。')
ov('E0538','O2','原误引职责，改实际加分培训设计经验。',metric='PREFERRED',branch='CHOICE',quote='Experience designing training or calibration programs for review teams.')
ov('E0538','O7','原误引职责，改加分真值数据构建；两术语同数据上位。',metric='PREFERRED',branch='UNCONDITIONAL',quote='Experience with golden set / ground truth construction.')
ov('E0538','O8','golden set/ground truth同上位。',branch='UNCONDITIONAL')
ov('E0538','O12','原误引职责，改一般审核质量周期经验。',metric='GENERAL',branch='UNCONDITIONAL',quote='Experience running audit or QA cycles and translating findings into process or guideline changes.')
ov('E0538','O13','audit/QA均数据质量流程上位。',branch='UNCONDITIONAL')
add('E0538','V2_SOP_OPERATION','GENERAL','CHOICE','Experience writing review guidelines, acceptance criteria, or SOPs that other people executed against.','明确SOP与其他指南类型任选。')
add('E0538','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','demonstrated ownership of a project or workstream end-to-end','明确项目或工作流端到端负责经验。')
for e in ['O7','O8','O9','O10']:ov('N0899',e,'数据运营、标注、采集质检都在数据上位。',branch='UNCONDITIONAL')
ov('N0899','O13','IL/机器人学习的数据均数据流程知识，不因学习方法斜杠而未知。',branch='UNCONDITIONAL')
ov('N0899','2:0','robotics/autonomy/teleoperation data为领域任选。',branch='CHOICE')
add('N0899','V2_SOP_OPERATION','GENERAL','EXAMPLE','A track record of building quality standards from scratch — rubrics, SOPs, QC workflows — not just executing against existing ones.','明确质量规范设计经历，SOP是列举。')
ov('E0603','O6','原误引职责，改一般ML理解要求。',metric='GENERAL',quote='- Working understanding of ML and why annotation quality drives model performance.')
add('E0603','V2_POSTTRAINING','PREFERRED','CHOICE','Experience training or fine-tuning autolabeling models, or partnering closely with the ML teams that do.','微调是加分经验的一个分支，不由团队合作推定本人微调。')
ov('N0703','O7','Conduct QC audits与validate pilot batches是执行使用。',metric='DUTY_OWN_USE')
add('N0703','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Develop, document, version-control, and continuously refine annotation guidelines and SOPs based on disagreement patterns and quality findings','明确本人编写维护SOP。')
add('N0703','V2_SOP_OPERATION','PREFERRED','UNCONDITIONAL','Ability to translate ambiguous SOPs into precise, actionable annotation guidelines','Preferred父语境下的规范理解转化能力。')
add('N0682','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','Own timelines, quality, throughput, metrices and operational problem-solving across multiple programs','明确多项目进度/质量/产出管理。')
add('N0682','V2_PROJECT_METHOD','PREFERRED','UNRESOLVED','2–3 years of program management / operations experience in startups or high-growth environments','Preferred内项目管理/运营经验关系未明，保留分支未知。')
register(list(R.values()),'Astra_v3_boundary_data_f')
