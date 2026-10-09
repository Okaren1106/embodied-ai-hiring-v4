from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0882':'基础设施Required段与Preferred段分开；IaC配置使用工具，Git工作流有明确原文。',
'N0846':'联邦现场集成，财务/程序管理按可见资格保留，项目工具在优先段。',
'N0838':'DevOps语言上层要求明确，测试支持与协作可靠性单列。',
'N0801':'安全层本人验证HIL，安全标准位于一般资格。',
'N0842':'云基础设施使用AWS及IaC工具，示例与任选继承完整。',
'N0834':'机器人平台；HIL属于优先经验，协议such as是示例非任选。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0882','O1','Python在such as工具列表中。',branch='EXAMPLE')
ov('N0882','3:0','使用Terraform配置IaC，未明开发Terraform本体。',metric='DUTY_OWN_USE')
ov('N0882','3:1','Git-based workflows同在such as列表。',branch='EXAMPLE')
for e in ['10:0','21:0','21:1']:ov('N0882',e,'Required Qualifications标题覆盖本条。',metric='REQUIRED')
for e in ['12:0','14:0','14:1','14:2']:ov('N0882',e,'Required段，such as与or/equivalent同时出现。',metric='REQUIRED',branch='CHOICE_AND_EXAMPLE')
for e in ['4:0','4:1']:ov('N0846',e,'Extras That Set You Apart为优先资格。',metric='PREFERRED')
ov('N0838','O7','语言泛称本身明确要求，具体语言才任选。',branch='UNCONDITIONAL')
for e in ['O16','O17']:ov('N0838',e,'Support测试/跨团队协作可靠性保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0801','O20','轨迹验证位于such as示例。',branch='EXAMPLE')
ov('N0801','2:0','仿真、HIL及现场试验由and连接，非任选。',branch='UNCONDITIONAL')
ov('N0801','4:0','F24在What You Have一般资格段。',metric='GENERAL')
ov('N0842','O5','语言上层类别明确要求。',branch='UNCONDITIONAL')
ov('N0842','1:0','在AWS上开发基础设施为使用云平台。',metric='DUTY_OWN_USE')
ov('N0842','1:1','such as且and列举，只有示例无任选。',branch='EXAMPLE')
ov('N0842','5:1','using GitHub Actions and ArgoCD明确并列，无示例词。',branch='UNCONDITIONAL')
for e in ['13:0','13:1','23:0','23:1']:ov('N0842',e,'such as与or共同作用。',branch='CHOICE_AND_EXAMPLE')
for e in ['8:0','8:1']:ov('N0834',e,'协议such as，and连接，没有任选。',branch='EXAMPLE')
for e in ['12:0','13:0']:ov('N0834',e,'HIL在Extras优先段；span多个环节非任选，改用完整F59。',metric='PREFERRED',branch='UNCONDITIONAL',quote=ln('N0834',59))
for e,n in [('O1',32),('O2',38),('O3',38)]:ov('N0834',e,'保留一般要求，补全标题及下一行能力说明。',metric='GENERAL',quote='\n'.join(RAW[RID['N0834']]['full_description'].splitlines()[n-1:n+1]))
register(list(R.values()),'Astra_v3_boundary_sw_n')
