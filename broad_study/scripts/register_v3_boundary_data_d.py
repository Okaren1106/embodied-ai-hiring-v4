from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0991':'一班数采主管：监管遥操人员不等于本人遥操；明确开发SOP，Jira未来工作流与加分经验分开。',
'N1022':'二班数采主管：同义语境相同裁决，班次与薪酬仍保留独立身份。',
'N0901':'数据运营主管：服务模型/安全的目的不转成本人模型研发；外部标注供应商SLA履约属于供货流程。',
'N0729':'数据管线：回读缩略职责；工具括号例示与明确or分开，MCAP/rosbag和dbt位于加分栏。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for r in ['N0991','N1022']:
 ov(r,'O5','与Engineering/IT共同开发解决方案，未明确独立开发数据管道。',metric='SEPARATE',branch='COLLABORATION')
 ov(r,'2:0','监管遥操人员，不是本人操作机器人。',metric='SEPARATE',branch='TEAM_OVERSIGHT')
 ov(r,'3:0','句子描述Jira将参与工作流，没有Jira任职技能要求。',metric='DUTY_OWN_USE')
 for e in ['6:0','6:1']:ov(r,e,'GoogleWorkspace/Jira and other tools例示，无or。',branch='EXAMPLE')
 add(r,'V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Develop and deploy new SOPs as needed.','明确本人编制与发布操作规程。')
add('N0901','V2_PROCUREMENT','DUTY_OWN_USE','UNCONDITIONAL','Manage relationships and SLAs with external labeling/annotation vendors, including onboarding, training, and performance management.','外部数据服务供应商履约和绩效管理，而非单纯提及供应商。')
for e in ['8:0','15:0','15:1']:ov('N0729',e,'括号列流处理/仓库产品，无产品任选词。',branch='EXAMPLE')
ov('N0729','12:0','such as Airflow or Dagster，例示加任选。',branch='CHOICE_AND_EXAMPLE')
for e in ['25:0','25:1']:ov('N0729',e,'Extras内such as且or；应为加分任选例示。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('N0729','28:0','Extras内dbt or similar frameworks。',metric='PREFERRED',branch='CHOICE')
register(list(R.values()),'Astra_v3_boundary_data_d')
