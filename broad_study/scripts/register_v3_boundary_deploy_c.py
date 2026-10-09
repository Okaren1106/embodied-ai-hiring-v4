from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0992':'二班维修：BASH在Desired，与N0993同文边界一致但不合并广告。',
'N1028':'技术支持：帮助建立流程与开头明确拥有客户问题解决分开；补VOC直接职责，编程语言斜杠保持未知。',
'N1018':'法语FAE：技术TypeScript在Nice to Have；现场验证辅助、网络工具安全目标不足、AutoCAD或等效选择需保留。',
'N1030':'高级技术支持：与N1028同证据边界；直接解决客户问题与协助流程分开。',
'N1029':'车队应用：Minimum资格全部Required；合作工具开发不记独立；补操作规程和版本控制明示知识。',
'N1006':'RMAC应用：Desired Skills父标题，Tableau为like示例；curriculum为机器人数据任务而非明确人类课程，目录用途不明保留未知。',
'N1032':'现场服务：Desired技能属于优先，CRM职责明确；补直接紧急维修和服务指标经营方法。',
'N1013':'现场服务：Desired Linux与机械能力优先；与N1032分别核对，补直接维修和服务指标。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0992','8:0','Desired Skills内BASH。',metric='PREFERRED')
for r in ['N1028','N1030']:
 for e in ['O5','1:0']:ov(r,e,'Helps establish/assist流程，原句属于支持承担。',metric='SEPARATE',branch='SUPPORT')
 add(r,'V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line(r,1),'开头明确take ownership resolving customer issues。')
 add(r,'SK_VOC_ANALYSIS','DUTY_OWN_USE','UNCONDITIONAL',line(r,1),'明确作为客户之声识别上报客户需要。')
ov('N1018','O5','assisting with field validation。',metric='SEPARATE',branch='SUPPORT')
for e in ['O7','O8']:ov('N1018',e,'仅网络协议/工具清单，无明确安全目标。',metric='SEPARATE',branch='NETWORKING_NOT_EXPLICIT_SAFETY')
ov('N1018','13:0','Technical Skills Nice to Have。',metric='PREFERRED')
ov('N1018','16:0','AutoCAD or equivalent。',branch='CHOICE')
ov('N1029','O6','Partner with engineering改进工具。',metric='SEPARATE',branch='COLLABORATION')
for e in ['10:0','11:0','12:0']:ov('N1029',e,'Minimum Qualifications标题。',metric='REQUIRED',**({'branch':'CHOICE_AND_EXAMPLE'} if e=='12:0' else {}))
for e,n in [('1:0',12),('2:0',12),('4:0',18)]:ov('N1029',e,'原引概述或标题，重定位直接动作。',metric='DUTY_OWN_USE',quote=line('N1029',n))
add('N1029','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',line('N1029',26),'本人开发故障处理与运营程序。')
add('N1029','V2_SOP_OPERATION','PREFERRED','UNCONDITIONAL',line('N1029',53),'明确运营程序和手册开发经验。')
add('N1029','V2_GIT','PREFERRED','UNCONDITIONAL',line('N1029',52),'冻结版本控制上位定义含version control，非具体Git品牌率。')
ov('N1006','O1','curriculum指机器人任务与数据课程，是否满足课程设计条目用途无法由简短定义裁决。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for e in ['O2','O3','O4','3:0','5:0']:ov('N1006',e,'Desired Skills & Qualifications父标题。',metric='PREFERRED',**({'branch':'EXAMPLE'} if e=='5:0' else {}))
ov('N1006','1:0','标题不足，重定位具体本人分诊F19。',metric='DUTY_OWN_USE',quote=line('N1006',19))
add('N1006','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Create detailed playbooks\nfor each data collection task, ensuring high-quality, consistent data generation that meets strict QA standards.','明确数据采集任务标准手册开发。')
for r,es,d,m,p in [('N1032',['O1'],4,6,12),('N1013',['O1','O2','O3'],6,8,17)]:
 for e in es:ov(r,e,'Desired skills父标题。',metric='PREFERRED')
 add(r,'V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line(r,d),'直接执行紧急维修。')
 add(r,'V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL',line(r,m),'本人确保客户满意度及首次修复/时效服务指标。')
 add(r,'V2_SALES_CRM','PREFERRED','EXAMPLE',line(r,p),'服务指标跟踪经验，such as具体指标。')
register(list(R.values()),'Astra_v3_boundary_deploy_c')
