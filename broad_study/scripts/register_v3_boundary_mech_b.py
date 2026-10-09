from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0049':'CAE岗位错引职责到要求需修；实际运动动力学仿真为执行分析，安全校核不等于开发安全系统；工具等列举。',
'E0015':'底盘岗本人有限元使用与测试执行，修复要求误引职责；Ansys/Abaqus斜杠与CAD软件同口径。',
'E0250':'振动力学：等CAE工具示例与任选一个的要求不同；参与样机测试不能记独立评测开发，仿真模型迭代另有明文。',
'E0234':'机械臂动力学模型由本人搭建；力反馈实现为参与，仿真优先要求必须重锚要求段。',
'E0319':'Agility机械：Creo优先与一般工具任选分别有原文，Jira和Confluence职责明确and；热分析是支持，不是独立热设计。',
'E0338':'Agility高级机械：CAD要求与职责分别定位；Creo优先两处关系不同；嵌入式属于视技能而定的条件职责。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0049','O3','原误引分析报告职责，改实际CAE经验要求。',metric='GENERAL',quote='3-5 年及以上结构 + 热 CAE 仿真经验')
ov('E0049','O10','原误引职责，实际结构CAE经验。',metric='GENERAL',quote='3-5 年及以上结构 + 热 CAE 仿真经验')
ov('E0049','O5','执行动力学仿真并设定载荷工况，未说明开发仿真系统或模型。',metric='DUTY_OWN_USE')
ov('E0049','O8','完成安全性校核是应用分析，不开发安全系统。',metric='DUTY_OWN_USE')
ov('E0049','O13','优先的各种产品仿真均属上位仿真经验。',branch='UNCONDITIONAL')
for e in ['2:0','2:1','2:2']:ov('E0049',e,'等软件列举；Ansys子工具虽斜杠，均为同一目录上位。',branch='EXAMPLE')
ov('E0015','O5','原引职责，改实际有限元经验要求。',metric='GENERAL',quote='具备 ANSYS/Abaqus 等有限元仿真落地经验')
ov('E0015','O6','原引职责，改实际DFMEA要求。',metric='GENERAL',quote='掌握公差分析、可靠性测试、DFMEA')
ov('E0015','O11','原引职责，改实际有限元仿真经验。',metric='GENERAL',quote='具备 ANSYS/Abaqus 等有限元仿真落地经验')
ov('E0015','O8','明确使用有限元完成校核，不是开发仿真系统。',metric='DUTY_OWN_USE')
ov('E0015','O9','牵头试制测试验证，未明确开发测试系统/方法。',metric='DUTY_OWN_USE')
for e in ['1:0','1:1']:ov('E0015',e,'ANSYS/Abaqus斜杠未解。',branch='UNRESOLVED')
ov('E0015','2:0','机加工钣金压铸塑胶等工艺为例示。',branch='EXAMPLE')
for e in ['1:0','1:1','2:0']:ov('E0250',e,'等工具/手段为例示，无任选。',branch='EXAMPLE')
for e in ['3:0','3:1']:ov('E0250',e,'等软件中的一个，任选加例示。',branch='CHOICE_AND_EXAMPLE')
ov('E0250','3:2','包括拓扑优化等，例示。',branch='EXAMPLE')
ov('E0250','O6','参与样机测试非独立评测开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0250','O5','本人迭代优化仿真模型明确，重锚开发模型而非模拟载荷一句。',metric='DUTY_OWN_DEVELOP',quote='迭代优化仿真模型精度。')
ov('E0250','O7','静力模态疲劳分析为可靠性评价使用，非由该句证明开发可靠性系统。',metric='DUTY_OWN_USE')
ov('E0234','O5','参与力反馈工程实现且协同优化。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0234','O9','原引职责，改任职优先句。',metric='PREFERRED',quote='熟悉机器人建模、动力学仿真与性能评估者优先。')
ov('E0234','O13','原引职责，改实际加分任选句。',metric='PREFERRED',branch='CHOICE',quote='熟悉机器人构型设计或动力学仿真。')
ov('E0319','O6','Creo加分另有独立原文，不沿用一般任选句。',metric='PREFERRED',quote='Creo and Windchill experience')
ov('E0319','O22','执行器优先原误引一般段，改实际斜杠优先句。',metric='PREFERRED',quote='Transmission/actuator design experience')
ov('E0319','O11','supporting thermal analyses是支持热分析，不是本人独立热设计。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['4:0','4:1']:ov('E0319',e,'Jira and Confluence明确并列使用。',branch='UNCONDITIONAL')
add('E0319','V2_JIRA','PREFERRED','UNRESOLVED','Jira/Confluence experience','加分经验斜杠未解，不影响职责and。')
add('E0319','V2_CONFLUENCE','PREFERRED','UNRESOLVED','Jira/Confluence experience','加分经验斜杠未解，不影响职责and。')
ov('E0338','O3','原误引职责，改一般CAD能力。',metric='GENERAL',quote='Proficient in mechanical CAD software (PTC Creo preferred)')
ov('E0338','O6','原误引另一个明确Creo优先句，改斜杠优先句，保留各自关系。',metric='PREFERRED',quote='Creo/Windchill Experience')
ov('E0338','O12','You should be comfortable为能力要求，like为例示。',metric='GENERAL',branch='EXAMPLE')
ov('E0338','O13','may include ... depending on your skillset为条件职责。',branch='CONDITIONAL')
for e in ['O16','O17','O18','O19']:ov('E0338',e,'including加and/or，任选及例示。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_mech_b')
