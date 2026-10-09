from astra_review_tools import *
JUD={
'E0364':'数据平台工程的硬性大数据/云工具要求和优先工具分开；Databricks Unity Catalog不是Unity引擎；AWS职责引用不得变成优先要求。',
'N0956':'FAR数据策略和管线建设单列。安全隐私管线是合作责任；dataset pruning非模型压缩。',
'N1020':'Atlas标注运营有明确双供应商管理、商业合同经历与SOP，虽然Required标题，句内preferred优先于标题。',
'E0458':'外部住宅采集运营，GoogleWorkspace一般要求明确，项目方法目录覆盖限制单列，物流协调不等机器人控制研发。',
'E0457':'数据质量复核按已有标准执行，不是本人开发管线或测评方法；协助改进标准与独立评估执行区分。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['1:0','1:1']:ov('E0364',e,'such as与or equivalent，例示和任选。',branch='CHOICE_AND_EXAMPLE')
ov('E0364','2:0','AWS S3/Athena/Sagemaker虽举例但都是AWS，上位平台明确。',branch='UNCONDITIONAL')
for e in ['3:0','3:1','3:2']:ov('E0364',e,'Required段且like ... or。',metric='REQUIRED',branch='CHOICE_AND_EXAMPLE')
for e in ['4:0','4:1','4:2']:ov('E0364',e,'Required段like列举，无or。',metric='REQUIRED',branch='EXAMPLE')
for e in ['5:0','6:0']:ov('E0364',e,'Required Qualifications段。',metric='REQUIRED')
ov('E0364','7:0','括号为数据目录产品例示，无or。',branch='EXAMPLE')
ov('E0364','7:1','Databricks Unity Catalog是数据目录产品，不是Unity图形/仿真引擎。',metric='SEPARATE',branch='HOMONYM_FALSE_POSITIVE')
ov('E0364','9:0','Bazel/Blaze斜杠加其他build系统，内部关系未明。',branch='UNRESOLVED')
ov('E0364','11:0','like mcap ROS etc例示。',branch='EXAMPLE')
ov('E0364','15:0','原引职责AWS工具，不存在此优先要求；保持职责语境，与2:0最终按广告去重。',metric='DUTY_OWN_USE',branch='UNCONDITIONAL')
ov('N0956','O5','Partner with operations/privacy/legal/security明确共同建设。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N1020','V2_PROCUREMENT','DUTY_OWN_USE','UNCONDITIONAL','managing task allocation, performance accountability, and dual-source relationships to optimize cost, quality, and speed','明确外包供应商供货关系和双源管理。')
add('N1020','V2_PROCUREMENT','PREFERRED','UNCONDITIONAL','Prior experience managing business/contractual relations between third-party annotation vendors/labelling service or BPO service providers strongly preferred.','句内strongly preferred指定实际商务合同关系经验。')
add('N1020','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Write SOPs and technical documentation for the annotation team and vendors','明确本人SOP编写。')
for e in ['O1','O2']:ov('E0457',e,'按已有标准review并出报告是执行，非开发评测方法或数据管线。',metric='DUTY_OWN_USE')
add('E0457','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Review data collection sessions against established quality standards','明确数据质量规范执行。')
R['E0458']['catalog_gap_notes']=['原文明确部署时间预算风险方法；数据职能目录未必包含V2_PROJECT_METHOD，不能越过冻结适用范围，后续汇总覆盖限制。']
register(list(R.values()),'Astra_v3_data_b')
