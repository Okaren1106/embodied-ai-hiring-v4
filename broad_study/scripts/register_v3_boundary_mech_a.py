from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0260':'结构专家三维工具斜杠未解，各工具同口径；Anasys明确CAE上下文拼写误差，保留Ansys。',
'N0462':'电机研发主责独立，编制测试纲领与协助测试区分；供应商技术交底不算采购；学历专业不算技术能力。',
'N0445':'结构实习职责均协助或参与，不记独立开发/测试；成型知识是一般要求，Ansys为加分例示。',
'N0464':'机械校招本人设计明确；Ansys与simulation并列非任选，结构轻量化不记模型压缩。',
'N0647':'结构实习参与仿真与设计应与独立责任分开；工具等至少一种是任选加例示，机械技术上位不随子类任选消失。',
'N0650':'同系列另一学历广告独立审读；协助责任和工具任选处理一致，保留学历及兴趣方向原文差异。',
'N0079':'Proe与Creo同族但整列斜杠未解，不能新增一个阳性覆盖原未知。',
'N0277':'数采装置结构：材料工艺为设计/外协对象，不是亲自机加工；供应商技术对接非采购，实际模具验收可保留评价。',
'E0077':'PRO-E为ProE常见拼写变体可映射Creo；参与核心技术验证与本人独立设计分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['2:0','3:0']:ov('N0260',e,'Solidworks/Proe/UG斜杠整体未解。',branch='UNRESOLVED')
ov('N0462','O4','本人负责编制测试大纲，实际测试仅协助。',metric='DUTY_OWN_DEVELOP')
for e in ['O6','O7']:ov('N0462',e,'学历专业为教育背景，不能推出相应技术能力。',metric='SEPARATE',branch='FIELD_OF_STUDY')
for e in ['O10','O11']:ov('N0462',e,'软件均为电磁分析，上位仿真能力明确。',branch='UNCONDITIONAL')
ov('N0462','1:0','供应商技术交底及试制，未明示询报价寻源合同。',metric='SEPARATE',branch='TECHNICAL_VENDOR_INTERFACE')
ov('N0462','2:0','等软件例示，无任选。',branch='EXAMPLE')
for e in ['O4','O5','O6']:ov('N0445',e,'协助/参与而非本人独立承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0445','2:0','一般任职条款对制造工艺有基本了解，等例示。',metric='GENERAL',branch='EXAMPLE')
ov('N0445','3:0','加分经验工具等例示。',branch='EXAMPLE')
ov('N0464','3:0','simulation、ansys并列，无任选标志。',branch='UNCONDITIONAL')
for r in ['N0647','N0650']:
 for e in ['O1','O2','O4']:ov(r,e,'等至少一种，明确任选加例示。',branch='CHOICE_AND_EXAMPLE')
 for e in ['O6','O7','O8','O9']:ov(r,e,'参与、协助、辅助工作，非独立本人使用/开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
 for e in ['O12','O13']:ov(r,e,'绳驱和传动均属机械上位知识。',branch='UNCONDITIONAL')
ov('N0079','1:0','Proe所在整列斜杠未解，与原Creo一致。',branch='UNRESOLVED')
ov('N0277','5:0','SolidWorks/Creo/UG斜杠未解，与其他工具一致。',branch='UNRESOLVED')
for e in ['3:1','7:1']:ov('N0277',e,'开模评审及技术交底不是采购商务方法。',metric='SEPARATE',branch='TECHNICAL_VENDOR_INTERFACE')
for e in ['1:0','2:0']:ov('N0277',e,'结构零件加工类型/跟进外协，不是本人使用加工工艺。',metric='SEPARATE',branch='OUTSOURCED_MANUFACTURING_OBJECT')
ov('N0277','O10','原参与测试改实际负责模具验收，保持独立评价依据。',metric='DUTY_OWN_USE',quote='负责模具验收（T0~T1试模）及量产质量管控，解决缩痕、飞边等成型缺陷，确保零件尺寸，外观满足要求')
ov('N0277','O11','原参与寿命环境测试，不能独立执行。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0077','O4','深度参与核心技术验证，非明确独立测试责任。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('E0077','SK_CREO','GENERAL','EXAMPLE','熟练使用PRO-E、Matlab等软件。','PRO-E是ProE拼写变体，冻结Creo别名可涵盖，不能因短词匹配漏记。')
register(list(R.values()),'Astra_v3_boundary_mech_a')
