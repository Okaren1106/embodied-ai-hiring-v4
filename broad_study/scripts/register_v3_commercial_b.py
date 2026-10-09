from astra_review_tools import *
JUD={
'N0247':'战略研究而非技术论文科研；PPT明确要求，情报/竞争方法未被目录完整覆盖，不强填营销条目。',
'N0292':'海外生态商务，具体落地谈判与展会公关明确；合规意识本身不同于法务实务知识。',
'E0063':'模型应用方案与客户赋能，LLM/VLA均属于基础模型上位，感知和规划优先例示；本人客户指导不等模型研发。',
'E0028':'政企产业生态合作，研究课题及公共合作不能直接等销售流程，目录对此专业方法覆盖有限。',
'E0084':'售前与销售协作，但另句明确本人端到端方案销售；技术资料与行业传播有本人职责。',
'E0246':'物流方案售前协作，商机判断一般资格明确，客户服务意识不是具体服务沟通方法；两段任职要求均保留。',
'N0700':'品牌视觉策略和独立制作交付明确，虽无工具词仍有专业营销内容能力；Preferred段品牌建设经验不能漏。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['N0247']['catalog_gap_notes']=['竞争地图、战略情报与专家访谈明示；现有17职能目录没有等价的战略研究专业方法，不把它们替换成营销能力。']
ov('N0292','2:0','仅法律合规意识，没有具体法务、合规流程知识或职责。',metric='SEPARATE',branch='GENERAL_AWARENESS')
add('N0292','V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL','负责海外重点项目的落地谈判及合同签订','明确商务成交行为。')
add('N0292','V2_MARKETING','DUTY_OWN_USE','EXAMPLE','统筹安排海外高层互访、展会（如德国汉诺威工博会、美国CES、日本IROS）参展等重大公关活动','明确公关活动统筹。')
for e in ['O2','O3']:ov('E0063',e,'LLM和VLA均满足基础模型上位类别，原文替代不取消上位明确性。',branch='UNCONDITIONAL')
ov('E0063','O4','等技术领域是例示。',branch='EXAMPLE')
add('E0063','TC_PERCEPTION','PREFERRED','EXAMPLE','加分项：熟悉机器人硬件、感知、运动规划等技术领域','感知优先例示原漏。')
add('E0063','V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','为客户提供系统性的技术咨询与实操指导','本人用户协助责任明确。')
R['E0028']['catalog_gap_notes']=['公共创新生态/课题合作方法未被目录充分覆盖；没有销售成交流程证据，不以V2_SALES_CRM替代所有商务合作。']
ov('E0084','1:0','与销售同事对接和技术支持是协作；O2已有独立销售责任。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('E0084','V2_MARKETING','DUTY_OWN_USE','UNCONDITIONAL','负责解决方案行业推广，包括销售推广使用的技术资料库建设','明确行业传播及技术资料建设。')
ov('E0246','1:0','与销售团队合作挖掘机会，不能当独立销售流程。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0246','3:0','仅服务意识佳，不是具体服务沟通或操作技能。',metric='SEPARATE',branch='GENERAL_ATTITUDE')
add('N0700','V2_MARKETING','DUTY_OWN_DEVELOP','UNCONDITIONAL','Design and deliver production-ready assets across website, digital, social, and out-of-home.','明确传播资产本人制作交付。')
add('N0700','V2_MARKETING','PREFERRED','UNCONDITIONAL','Proven track record of building brands from zero — identity, campaign, print, and digital.','Preferred Qualifications段品牌内容开发经验。')
register(list(R.values()),'Astra_v3_commercial_b')
