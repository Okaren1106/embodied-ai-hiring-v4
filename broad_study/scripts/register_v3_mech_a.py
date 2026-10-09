from astra_review_tools import *
JUD={
'E0011':'机械设计与测试工装独立交付，工具未具体定名不补品牌；生产指导现场问题不自动称客户部署。',
'E0062':'底盘结构与选型仿真、SOP明确；Solidworks和AutoCAD及Office为普通并列，无任选。',
'E0145':'本人交付散热与热保护，电机电池是热设计对象，非整套器件开发；参与驱动器布局不能独立化。多项一般要求原错锚职责，重新定位。',
'E0095':'结构和减速器设计本人明确；项目交付效率稳定性不等于产品系统可靠性，撤对应技术正例。',
'N0425':'机械本体与量产、可靠性设计闭环，软件例示；可靠性一般要求重锚真实产品失效风险能力。',
'N0437':'结构总监独立设计/主导仿真，寿命分析是应用可靠性评价，非开发可靠性方法；供应商技术合作不等采购。',
'N0234':'结构零件及工艺知识，供应商评审参与不等独立采购或工艺执行；明确可制造性设计另保留DFM。',
'N0477':'电机研发与电磁仿真、样机验证独立主责；学历专业不等技术要求，技术交底不等采购。',
'N0641':'整机结构主责，SolidWorks等例示；必须只修饰整机项目经历，后面的熟悉测试流程仍一般。',
'N0622':'精密齿轮设计仿真主责，装配配合不冒称独立承担；SolidWorks例示与仿真上位要求成立。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0062','E0062:2:0','机械设计软件Solidworks、AutoCAD及Office普通并列，没有任选。',branch='UNCONDITIONAL')
for e in ['O2','O4']:ov('E0145',f'E0145:{e}','本人交付这些器件的散热方案，不直接证明开发电机或电池本体。',metric='DUTY_OWN_USE')
ov('E0145','E0145:O3','参与驱动器布局按协作对象。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O10','O11','O13']:ov('E0145',f'E0145:{e}','一般资格证据错锚职责，按真实任职要求定位。',metric='GENERAL',quote='熟悉传热学、热仿真、散热结构设计和温升测试。')
ov('E0145','E0145:O14','电机知识一般要求原错锚职责，改真实了解条目。',metric='GENERAL',quote='了解电机、功率器件、导热材料、风冷、液冷、自然冷却和热保护策略。')
ov('E0095','E0095:O2','稳定性修饰项目交付，未明示系统可靠性寿命或故障目标。',metric='SEPARATE',branch='DELIVERY_GOAL')
ov('N0425','N0425:O9','一般要求原错引职责寿命分析，真实资格有产品失效风险能力。',metric='GENERAL',quote='能熟练对产品进行结构力学分析，有较强的产品失效风险分析能力')
ov('N0437','N0437:O3','寿命分析是在结构设计中应用可靠性分析，未指开发新可靠性方法机制。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for e in ['N0234:2:0','N0234:2:1']:ov('N0234',e,'对接供应商并参与模具评审，不直接本人承担全部工艺方法。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0234','N0234:2:2','技术评审合作不证明采购寻源谈判下单；供应商按合作对象。',metric='SEPARATE',branch='TECHNICAL_SUPPLIER_COLLABORATION')
add('N0234','V2_DFM','DUTY_OWN_USE','UNCONDITIONAL','负责零部件的强度、刚度、装配、可靠性、成本及可制造性设计','本人可制造性设计，DFM方法应用明确。')
for e in ['O6','O7']:ov('N0477',f'N0477:{e}','此处是本科专业列表，不是技术知识能力要求。',metric='SEPARATE',branch='EDUCATION_FIELD')
for e in ['O10','O11']:ov('N0477',f'N0477:{e}','软件举例不影响电磁仿真上位能力明确。',branch='UNCONDITIONAL')
ov('N0477','N0477:1:0','供应商技术交底、样机验证和设计成本平衡，没有明确采购过程职责。',metric='SEPARATE',branch='TECHNICAL_SUPPLIER_COLLABORATION')
ov('N0477','N0477:2:0','ansoft、Maxwell等软件列表没有or，按例示。',branch='EXAMPLE')
ov('N0641','N0641:O1','SolidWorks等明确例示。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_mech_a')
