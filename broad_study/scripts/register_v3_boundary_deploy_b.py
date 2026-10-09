from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0448':'生产工程主管：一般经验错引加分处须改回F41；FAT标准有直接建设语句；DDS/TCP和MES斜杠未知，后训练受or选择。',
'N0546':'前沿部署：讲解模型接口与亲自抓取策略调试区分，协助采集不作独立使用；补明示SOP、微调加分和现场排障。',
'N0535':'操作部署：串联模块确属本人集成使用；AI视觉上位明确，深度学习具体关系仍未知；标定等为示例。',
'E0269':'售后导入：Ubuntu属于Linux明示别名，不能因候选短语未单列而漏计；保留维修流程与工具开发。',
'E0254':'FAE：Ubuntu/Linux补漏，故障排查、库存与VOC直接职责保留。',
'E0220':'FAE：与E0254同正文逐证据核对，保持独立广告身份；Ubuntu/Linux补漏。',
'E0340':'维修服务：支持团队与明确流程开发分开；补SOP能力；Google/MS分支及Jira/Confluence任选保留。',
'N1026':'Staff FAE：网络经验不能归安全技术；数据集成是顾问角色；服务经营熟悉度不作已承担职责。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('E0448','O9','定义FAT标准的明确建设职责在F21。',metric='DUTY_OWN_DEVELOP',quote=line('E0448',21))
ov('E0448','O16','一般经验在F41，非加分F31。',metric='GENERAL',quote=line('E0448',41))
for e in ['1:1','1:2','4:0']:ov('E0448',e,'不同技术/系统斜杠关系未明。',branch='UNRESOLVED')
ov('E0448','3:0','fine-tuning,post-training or dispatching jobs。',branch='CHOICE')
ov('E0448','7:0','EDUCATION and/or EXPERIENCE一般资历，非Bonus。',metric='GENERAL')
ov('E0448','O11','ML/MLOps斜杠，具体系统能力关系未明。',branch='UNRESOLVED')
add('E0448','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',line('E0448',21),'本人定义部署手册及可重复流程。')
R['E0448']['catalog_gap_notes']=['sprint cadence项目方法明确，但V2_PROJECT_METHOD冻结适用职能不含部署现场；仅记录，不扩目录。']
ov('N0546','O7','协助客户采集标注。',metric='SEPARATE',branch='SUPPORT')
for e in ['O10','O11']:ov('N0546',e,'概述深度参与与推动落地，无法替代明确独立技术承担；抓取策略直接职责另有。',metric='SEPARATE',branch='PARTICIPATION')
add('N0546','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',line('N0546',11),'制定数据采集标准规范。')
add('N0546','V2_POSTTRAINING','PREFERRED','EXAMPLE',line('N0546',40),'大模型Fine-tuning等技术加分。')
add('N0546','V2_INCIDENT_SUPPORT','GENERAL','UNCONDITIONAL',line('N0546',36),'现场问题排查能力明确。')
add('N0546','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line('N0546',16),'本人解决现场算法适配问题。')
for e in ['O25','O26']:ov('N0535',e,'AI视觉技术应用的上位感知明确，具体算法仍保留关系未知。',branch='UNCONDITIONAL')
ov('N0535','2:0','相机、手眼标定、视觉伺服等技术示例。',branch='EXAMPLE')
for r,n in [('E0269',12),('E0254',11),('E0220',11)]:add(r,'SK_LINUX','GENERAL','UNCONDITIONAL',line(r,n),'Ubuntu为冻结Linux别名且明确熟悉操作系统。')
for e in ['1:0','2:0']:ov('E0340',e,'Support服务运营/SLA遵循，保留支持承担关系。',metric='SEPARATE',branch='SUPPORT')
add('E0340','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',line('E0340',3),'本人开发实施改进机器人维修流程。')
add('E0340','V2_SOP_OPERATION','GENERAL','UNCONDITIONAL',line('E0340',25),'明确高准确执行标准作业/SOP能力。')
ov('N1026','O5','技术顾问建议企业数据集成，不是本人数据管线使用。',metric='SEPARATE',branch='ADVISORY_OBJECT')
ov('N1026','O6','CAD/网络/PythonAPI句无安全概念，不作安全技术证据。',metric='SEPARATE',branch='NON_SAFETY_CONTEXT')
ov('N1026','5:0','Familiarity with GTM/customer success是能力熟悉度，非实施动作。',metric='GENERAL')
register(list(R.values()),'Astra_v3_boundary_deploy_b')
