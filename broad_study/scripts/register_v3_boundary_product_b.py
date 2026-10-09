from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0092':'算法项目：工具如/等为例示；PMP和PRINCE2同项目资格上位。',
'N0136':'解决方案：需求研究是真实专业能力但本职能冻结目录未纳VOC分析，保留目录缺口；PMP/敏捷均项目资格上位。',
'N0534':'Agent产品：本人评测体系明确，基础模型是知识要求，多个评测/数据闭环经验任选保留。',
'N0342':'机器人产品：产品规格与算法研发主体区分成立，一般技术理解不因产品职能而排除。',
'N0354':'力触觉产品：C/C++/Python其中一种明确任选；优先修饰后半示例代码能力，不把C单独放加分。',
'N0340':'项目支持：本人识别风险/更新清单支持方法使用，协助计划不独立承担；工具列举修正。',
'N0343':'另一力触觉产品：同义语言要求与加分作用范围同口径处理。',
'N0304':'分公司研发管理：回读管理体系/知识方法全文句，补本人项目管理机制开发；证书与方法知识分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['4:0','4:1','4:2','4:3']:ov('N0092',e,'如/等工具列举，无任选。',branch='EXAMPLE')
ov('N0092','10:0','PMP与PRINCE2均属项目资格上位。',branch='UNCONDITIONAL')
ov('N0136','1:0','PMP与敏捷认证均为项目管理资格。',branch='UNCONDITIONAL')
R['N0136']['catalog_gap_notes']=['原文明示客户痛点/需求调研并输出报告，但SK_VOC_ANALYSIS不适用于冻结RF_PRODUCT_PROGRAM，不能静默扩展目录；项目职能专业能力覆盖存在限制。']
for r in ['N0354','N0343']:ov(r,'2:0','其中一种明确任选，前半语言能力是一般要求；后半代码理解测试能力才优先。',metric='GENERAL',branch='CHOICE')
ov('N0340','1:0','原引用协助制定计划；重定位本人识别/更新风险与记录的实际方法使用。',metric='DUTY_OWN_USE',quote='◦ 识别项目中的常见风险（如驱动芯片缺货、算法延期、散热瓶颈），更新风险清单并协助制定预案。')
for e in ['3:0','3:1','3:2']:ov('N0340',e,'如或括号列协作工具，没有任选词。',branch='EXAMPLE')
add('N0304','V2_PROJECT_METHOD','DUTY_OWN_DEVELOP','UNCONDITIONAL','负责完成分公司的项目管理机制搭建','明确本人搭建项目管理机制。')
ov('N0304','1:1','PMP/ACP都为项目管理证书上位；证书举例不使整个资格上位任选。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_product_b')
register([dict(reading_id=r,review_mode='FOLLOWUP',judgment='核对冻结V2_PM_CREDENTIAL定义为项目资格上位；不同项目证书之间任选不等于资格本身任选。',evidence_overrides=[dict(evidence_id=r+':'+e,branch='UNCONDITIONAL',reason='所有列明证书/同等认证均属项目管理资格上位；保留原具体证书清单。')]) for r,e in [('N0256','7:0'),('N0086','4:1'),('N0072','1:0')]],'Astra_v3_pm_credential_upper_scope')
