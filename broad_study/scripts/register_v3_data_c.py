from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0897':'采集场地运营负责人，招聘与recruiting合作但自己有offer决定权，独立责任成立；通用HR经验与规范执行补入。',
'E0608':'数据QA流程与软件工具本人建设；供应商反馈是质量管理，不直接等寻源采购。一般QA能力和优先评测工具知识应补全。',
}.items()}
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
add('N0897','V2_HR','GENERAL','UNCONDITIONAL',"A track record of hiring and onboarding at volume: you’ve run hiring waves, working interviews, and the first-90-days retention battle that follows.",'明确一般招聘入职与留存流程经验。')
add('N0897','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Quality standards are set centrally; making them real at your site is your job.','执行统一采集质量标准，不冒称开发标准。')
add('E0608','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Build and run the end-to-end QA process for multimodal data ingested from third-party vendors and partners — sampling strategy, review workflows, pass/fail decisions, and audit trails','本人定义抽样评估流程。')
add('E0608','TC_EVALUATION','GENERAL','UNCONDITIONAL',"Comfort being hands-on in the data: reviewing samples yourself, writing and refining rubrics, and spot-checking your own program's output.",'明确评估规则与复核一般能力。')
add('E0608','TC_EVALUATION','PREFERRED','UNCONDITIONAL','Experience defining requirements for QA/validation tooling or working with engineers on automated data quality checks.','两种选项均涉及质量评价上位方法/工具。')
add('E0608','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','enforce standards through review and acceptance processes','明确数据质量规范执行。')
register(list(R.values()),'Astra_v3_data_c')
q='Track deployment timelines, budgets, and status; proactively flag risks and resolve blockers'
register([dict(reading_id='E0458',review_mode='FOLLOWUP',judgment='核对冻结适用范围已确认数据职能包含项目方法，消除上一笔尚未确认的目录缺口提示，补入实际计划风险职责。',additions=[dict(code='V2_PROJECT_METHOD',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote=q,reason='明确部署时间预算风险管理，且冻结目录适用于本职能。')],catalog_gap_resolutions=['E0458上一笔V2_PROJECT_METHOD适用性疑问已解决：确实适用，已补正例。'])],'Astra_v3_data_project_scope')
