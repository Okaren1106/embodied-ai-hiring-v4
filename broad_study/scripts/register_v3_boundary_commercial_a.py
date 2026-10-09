from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0708':'社媒实习：团队合作句不能独立使用营销方法，原文本人内容制作明确；Preferred平台运营理解保留目录上位。',
'N0365':'技术传播：世界模型为传播对象且另有概念知识要求；GitHub单纯传播按冻结Git排除条款保留不计。',
'N0227':'BD明确独立销售闭环、销售经验和机器人技术理解；无需修改当前边界。',
'N0230':'销售运营：协助负责人搭建与本人优化分别；CRM加分段误记一般，Tableau/PowerBI为例示；跨部门沟通不是销售专业能力。',
'N0188':'品牌视觉：字体版式色彩不等于工业CMF；Figma是做模板所用工具，不是开发Figma；供应商作品质量不是采购。',
'N0185':'海外传播策略主责明确；共同完成英文架构与本人策略不同，泛称供应商管理未见寻源交易要求。',
'N0123':'内容运营明确本人执行及独立方案策划；Photoshop可确认，Premiere未在现目录单列，不能上推整套Adobe能力。',
'N0126':'售前PPT是配合团队；客户采购决策链虽非本人采购职责，却明示采购知识要求，应计一般要求。',
'N0053':'销售实习本人制作PPT与销售文书，电话微信渠道不强行新增目录，当前边界可保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0708','3:0','原句collaborate，另句本人内容制作明确，重锚。',metric='DUTY_OWN_USE',quote='Create, shoot, and edit short-form video content across TikTok, Instagram, and emerging platforms')
add('N0708','V2_MARKETING','PREFERRED','UNCONDITIONAL','Deep familiarity with TikTok, Instagram, and short-form video culture','Preferred段明确社媒内容文化知识。')
for e in ['O6','O7']:ov('N0365',e,'等技术概念为例示。',branch='EXAMPLE')
ov('N0365','15:0','等技术概念为例示。',branch='EXAMPLE')
ov('N0230','O1','配合/协助制作材料不是独立承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['1:0','2:0']:ov('N0230',e,'标题不能超出协助搭建的责任，统一锚协助句。',metric='SEPARATE',branch='COLLABORATION_OBJECT',quote='协助商业化负责人搭建从线索挖掘、商机跟进、方案报价、合同审批到验收回款的端到端销售流程（LTC），建立标准化、可复制的销售运营体系。')
for e in ['10:0','15:0']:ov('N0230',e,'明确配合或协助销售。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0230','3:0','负责CRM搭建运维为配置使用，不是开发CRM软件。',metric='DUTY_OWN_USE')
for e in ['17:0','17:1']:ov('N0230',e,'等工具列举，无任选词。',branch='EXAMPLE')
ov('N0230','24:0','加分项CRM上位明确。',metric='PREFERRED',branch='UNCONDITIONAL')
for e in ['24:1','24:2']:ov('N0230',e,'加分段括号等列举。',metric='PREFERRED',branch='EXAMPLE')
for e in ['22:0','23:0']:ov('N0230',e,'一般协调/服务态度不足为销售专业方法。',metric='SEPARATE',branch='GENERIC_WORK_ATTRIBUTE')
ov('N0188','1:0','职位名重锚实际本人建设品牌设计系统。',metric='DUTY_OWN_DEVELOP',quote='建设Figma模板、组件、图标、素材和源文件管理机制，提升Social与营销团队的复用效率。')
for e in ['3:0','4:0']:ov('N0188',e,'参与建立/概念发想，非本人独立交付。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['3:1','12:1']:ov('N0188',e,'平面视觉色彩版式没有工业外观材料表面设计对象。',metric='SEPARATE',branch='GRAPHIC_DESIGN_NOT_CMF')
ov('N0188','6:0','建设Figma模板为使用设计工具。',metric='DUTY_OWN_USE')
ov('N0188','8:1','供应商作品质量把关没有询报价寻源商务供货内容。',metric='SEPARATE',branch='CREATIVE_VENDOR_QUALITY')
ov('N0185','4:0','与产品营销研发共同完成，协作语境。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0185','16:0','泛称管理供应商，未明示询报价寻源商务供货管理方法。',metric='SEPARATE',branch='GENERIC_VENDOR_MANAGEMENT')
ov('N0126','O1','配合团队支撑招投标。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0126','V2_PROCUREMENT','GENERAL','UNCONDITIONAL','熟悉教育行业客户的采购决策链条、资金属性及项目运作周期','明确采购知识要求；不等于该员工执行采购。')
register(list(R.values()),'Astra_v3_boundary_commercial_a')
