from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0344':'机器人数据科学：预测物理部件寿命不等于开发/使用执行器或电力电子；一般生存分析重定位，加分质检重定位；Safety空标题不确证工作内容。',
'N0959':'FAR数据平台：云栈与前端是全栈岗位的实际技术环境；回读一般/加分经验，补明确版本管理要求。',
'N0812':'高级数据运营：明确本人采集与传感器套件建设；技能任取数项的一般要求不能记加分，补本人SOP编制。',
'N0836':'数据工程：AWS服务上位明确；Airflow或同类工具任选；仓库产品such as并or。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0344','O1','明确本人构建寿命预测模型。',metric='DUTY_OWN_DEVELOP')
q='Deep expertise in some combination of: reliability/survival analysis, time-series and anomaly detection, predictive maintenance, and causal/observational inference.'
ov('E0344','O4','原引用加分学历句，改一般some combination；reliability/survival内部仍未解。',metric='GENERAL',branch='UNRESOLVED',quote=q)
ov('E0344','O17','原误引职责标题，改一般能力组合；可靠性为可选领域。',metric='GENERAL',branch='CHOICE',quote=q)
ov('E0344','O7','制造质量体系括号例示SPC。',branch='EXAMPLE')
for e in ['O10','O11']:ov('E0344',e,'部件是寿命预测对象，非本人开发/操作执行器或电力电子。',metric='SEPARATE',branch='RELIABILITY_MODEL_OBJECT')
ov('E0344','O15','Beyond charter may help shape下只有Safety statistics标题及句点，不能确定具体安全统计任务。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP','DUTY_OWN_USE_CONDITIONAL','DUTY_OWN_DEVELOP_CONDITIONAL'])
ov('E0344','O18','原误引职责，改Bonus制造质量系统知识。',metric='PREFERRED',quote='Exposure to manufacturing quality systems (end-of-line test, SPC, yield/defect analytics).')
add('N0959','V2_GIT','GENERAL','UNCONDITIONAL','source control management','冻结版本控制条目包含明确source control管理；不推特定平台。')
ov('N0812','O10','本人构建传感器套件及安装夹具，不能因主职能是数据而排除机械对象。',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE')
ov('N0812','2:0','several of them上层任选，MOCAP上位是明确选项，具体品牌才例示。',branch='CHOICE')
for e in ['7:0','7:1']:ov('N0812',e,'What You Bring一般任选技能列表，不是加分。',metric='GENERAL',branch='CHOICE')
add('N0812','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Write and maintain SOPs and other supporting documentation for data collection, annotation, and lab operations.','明确本人编写维护SOP。')
add('N0812','V2_SOP_OPERATION','GENERAL','UNCONDITIONAL','Strong documentation habits: you leave SOPs and processes better than you found them.','列表后独立一般操作文档要求。')
ov('N0836','5:0','Airflow or similar tools明确任选。',branch='CHOICE')
ov('N0836','7:0','任一所列AWS服务仍属AWS上位，不能把服务例示转成平台例示。',branch='UNCONDITIONAL')
for e in ['22:0','22:1']:ov('N0836',e,'such as且or。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_data_e')
