from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0723':'AR/VR软件，Unity及Unreal一般经验并列；遥操与用户研究属于优先，CI遗漏补齐。',
'N0845':'Web开发用Node/React；数据库继承such as和or。',
'N0841':'产品Web断行句恢复完整，AWS一般要求允许equivalent，AWS SDK优先另列。',
'N0730':'数据平台底座，Kubernetes一般要求改锚任职，Terraform资格补齐，Spark/Databricks未解。',
'N0782':'实时网络，TCP/UDP在冻结同类中，遥操背景是优先经验。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('N0723','O3','语言上层类别本身明确要求。',branch='UNCONDITIONAL')
for e in ['6:0','6:1']:ov('N0723',e,'工具列表为and并列，没有任选词。',branch='UNCONDITIONAL')
for e in ['13:0','14:0']:ov('N0723',e,'Extras优先经验段。',metric='PREFERRED')
add('N0723','V2_CI_CD','GENERAL','UNCONDITIONAL',34,'一般资格明确continuous-integration workflows。')
add('N0723','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL',16,'本人通过user studies评估交互原型。')
for e in ['1:0','4:0']:ov('N0845',e,'用Node/React构建服务或前端，不是开发工具本体。',metric='DUTY_OWN_USE')
for e in ['11:0','11:1']:ov('N0845',e,'such as与or similar兼具。',branch='CHOICE_AND_EXAMPLE')
for e in ['1:0','4:0']:ov('N0841',e,'用Node/React构建服务或前端，不是开发工具本体。',metric='DUTY_OWN_USE')
ov('N0841','18:0','下一行or equivalent clouds不能遗漏，合并完整资格片段。',branch='CHOICE',quote='\n'.join(RAW[RID['N0841']]['full_description'].splitlines()[35:38]))
R['N0841']['additions'].append(dict(code='V2_AWS',metric='PREFERRED',branch='UNCONDITIONAL',quote='\n'.join(RAW[RID['N0841']]['full_description'].splitlines()[53:55]),reason='优先段明确Proficiency using AWS SDK。'))
ov('N0730','O3','Kubernetes一般资格改锚F27至F33完整句，原为职责。',metric='GENERAL',quote='\n'.join(RAW[RID['N0730']]['full_description'].splitlines()[26:33]))
ov('N0730','O21','数据或ML平台经验明确任选；括号无示例词。',branch='CHOICE',quote='\n'.join(RAW[RID['N0730']]['full_description'].splitlines()[44:47]))
for e in ['12:0','12:1']:ov('N0730',e,'Spark/Databricks不同工具裸斜线未解。',branch='UNRESOLVED')
R['N0730']['additions'].append(dict(code='V2_TERRAFORM',metric='GENERAL',branch='CHOICE',quote='\n'.join(RAW[RID['N0730']]['full_description'].splitlines()[30:33]),reason='明确IaC Terraform or similar一般资格。'))
ov('N0782','3:0','TCP与UDP同属冻结V2_TCPIP，e.g.为示例。',branch='EXAMPLE')
ov('N0782','13:0','What Will Set You Apart优先段。',metric='PREFERRED')
register(list(R.values()),'Astra_v3_boundary_sw_p')
