from astra_review_tools import *
JUD={
'N0888':'全文以实际合同制造商产线、固件配置和量产测试为责任。现场及生产故障根因处理明确，不能因另一段泛称debug而把全广告运行排障漏掉；自动化框架开发成立。',
'E0355':'供应商审核/质量与采购独立。质量资格、IPC知识、根因经验和SOP体系知识在完整要求中存在，不应只依候选词命中。公司福利与USD不是工具证据。',
'N0678':'工程指导下仍明确本人装配、测试和制造测试设备，区别仅协助。全部资格位于Preferred。括号中的具体仪器例示，供应品在标准测试设备语境可指测试电源，采购依as needed为条件。',
'N0786':'建筑空间数据QA与软件测试，非机器人模型开发。Jira职责例示和Python等优先例示正确；根因方法一般要求漏记。拥有质量交付流程不等于本人开发数据管线。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
add('N0888','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Lead root-cause analysis for field and production failures; coordinate corrective actions with design, firmware, and CM engineering to close quality loops.','实际在场与生产故障处理明确，不能以其他一般debug句的拒收覆盖此正例。')
add('E0355','V2_IPC_STANDARDS','GENERAL','UNCONDITIONAL','Familiarity with IPC standards, supplier process audits, and acceptance criteria for electronic assemblies.','完整要求独立明确IPC标准知识。')
add('E0355','V2_RCA','GENERAL','UNCONDITIONAL','Extensive experience assessing and qualifying suppliers, performing audits, source inspections, driving RCAs, and implementing CAPA.','完整资格明确根因方法经验，无任选。')
add('E0355','V2_SOP_OPERATION','GENERAL','EXAMPLE','Strong understanding of QMS development, including supplier-facing policies, SOPs, and control requirements.','QMS知识下明确列举SOP，与普通质量性格区分。')
ov('E0355','E0355:7:0','ASQ质量资格本身明确为加分；所举证书为同一上位资格类别，不要求每个证书同时持有。',branch='UNCONDITIONAL')
for eid in ['N0678:O1','N0678:O2']:ov('N0678',eid,'仪器为standard test equipment后的括号子例。',branch='EXAMPLE')
add('N0678','V2_POWER_SUPPLY','DUTY_OWN_USE','EXAMPLE','Operate and set up standard test equipment (oscilloscopes, analyzers, supplies, DMMs)','标准测试设备中的supplies有仪器上下文，不与采购supplies混同。')
add('N0678','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Fabricate custom test equipment, boxes, and harnesses','本人制造定制测试设备明确。')
add('N0786','V2_RCA','GENERAL','UNCONDITIONAL','Exceptional organizational skills with a highly systematic approach to defect tracking, root-cause analysis, and technical documentation.','明确根因方法要求，不是仅软件排障泛称。')
ov('N0786','N0786:O12','own数据质量与交付流程仅说明应用管理；开发管线另句为协作，不证明本人开发数据工程。',metric='DUTY_OWN_USE')
for eid in ['N0786:O14','N0786:O15','N0786:O16']:
 ov('N0786',eid,'软件QA、测试工程或数据验证均属评测上位概念，要求该类经验本身无条件；保留具体子经验任选原文。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_mfg_e')
