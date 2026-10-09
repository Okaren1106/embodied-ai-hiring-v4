from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0780':'机械硬件主责独立且明确采购；CAD上位不限SolidWorks，开发QA检查不能记执行已有检查。',
'N0781':'实习标题不自动降责任，此文实际写Design/Build；正文与正式岗相同部分逐段核对，采购和QA同口径。',
'E0456':'连接器工程：修复CAD/GD&T要求错引职责；EE协作SI与本人测试设计分开，原型协助排障不算运行维护。',
'E0587':'机械设计本人制造工艺优化；HALT/HASS和DOE在一般要求而非Preferred，成本供方选择明确；FEA要求重新定位。',
'E0405':'软体手套：软表面设计对象是机械部件，不能单凭用途推灵巧操作算法；热耐受评价与散热设计区分；生产协作与本人加工分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for r in ['N0780','N0781']:
 ov(r,'O8','所有替代工具都是机械CAD，上位无条件。',branch='UNCONDITIONAL')
 ov(r,'O23','Develop QA checks是本人开发质检方法。',metric='DUTY_OWN_DEVELOP')
 add(r,'V2_PROCUREMENT','DUTY_OWN_USE','UNCONDITIONAL','Work with vendors and contract manufacturers to procure mechanical hardware.','明确与供方采购机械硬件。')
ov('E0456','O3','原引职责，重锚一般CAD要求。',metric='GENERAL',quote='Strong 3D CAD proficiency (CATIA, SolidWorks, Creo, or equivalent)')
ov('E0456','O7','原引职责，重锚一般工程图要求。',metric='GENERAL',quote='Ability to create complete, manufacturing-ready 2D drawings with proper GD&T')
ov('E0456','O15','原引职责，改实际机械组件设计经验。',metric='GENERAL',branch='UNCONDITIONAL',quote='Demonstrated experience designing custom components: housings, overmolds, contacts, or electromechanical assemblies')
ov('E0456','3:0','Collaborate with EE属于协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0456','5:0','Support prototype bench troubleshooting不是本人运行维护。',metric='SEPARATE',branch='PROTOTYPE_COLLABORATION_OBJECT')
ov('E0456','7:0','Bonus段成型知识。',metric='PREFERRED')
ov('E0456','8:0','Bonus段PLM上位明确。',metric='PREFERRED')
for e in ['O4','O5','O6','O10']:ov('E0456',e,'括号列举及or equivalent/similar，任选和例示。',branch='CHOICE_AND_EXAMPLE')
ov('E0587','O4','原引职责，实际FEA一般要求另句。',metric='GENERAL',quote='Practical understanding of when and how to apply FEA tools, with the ability to make first-order engineering judgments')
ov('E0587','O6','actuator sizing or design，设计非无条件。',branch='CHOICE')
ov('E0587','O10','使用FEA热分析，不是开发热仿真系统。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for e in ['O14','O15','O16','O17']:ov('E0587',e,'原引职责，改实际可靠性测试方法要求，上位不因HALT/HASS下位斜杠未解。',metric='GENERAL',branch='UNCONDITIONAL',quote='Familiarity with HALT/HASS, FMEA, DOE methodologies, and test-to-failure approaches for robust mechanical design')
ov('E0587','3:0','Collaborate with EE and radio teams。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0587','2:0','reliability tests括号列举HALT/HASS，两者均在同上位目录。',branch='EXAMPLE')
for e in ['6:0','6:1']:ov('E0587',e,'一般要求并列方法，不是Preferred任选。',metric='GENERAL',branch='UNCONDITIONAL')
ov('E0587','5:0','manufacturing processes括号例示。',branch='EXAMPLE')
ov('E0587','7:0','including列举。',branch='EXAMPLE')
add('E0587','V2_PROCUREMENT','DUTY_OWN_USE','CONDITIONAL','own and drive supplier selection where needed.','明确按需负责供应商选择。')
ov('E0405','O6','机械抓握表面用于操作，不证明本人研究/实现机器人操作算法。',metric='SEPARATE',branch='MANIPULATION_APPLICATION_OBJECT')
for e in ['O9','O13']:ov('E0405',e,'温度耐受性能验证未明示散热/热仿真/热路径设计。',metric='SEPARATE',branch='THERMAL_PERFORMANCE_TEST_OBJECT')
ov('E0405','1:0','使用成型等工艺开发组件，including例示。',branch='EXAMPLE')
ov('E0405','3:0','标题重锚实际Partner closely优化DFM，是协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT',quote='Partner closely with Manufacturing, Supply Chain, Quality, and suppliers to optimize designs for manufacturability, assembly, cost, quality, scalability, and repeatable production.')
ov('E0405','6:0','一般机械工程原型排查能力，无明确运行排障对象。',metric='SEPARATE',branch='PROTOTYPE_DEBUGGING_SKILL')
register(list(R.values()),'Astra_v3_boundary_mech_c')
