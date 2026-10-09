from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0432':'Staff机械：测试规划与执行均有本人责任，可靠性测试不等于开发可靠性方法；要求不能引用职责，DFMA一处任选一处明确。',
'E0434':'上身技术负责：实际负责机器人skin最终曲面符合工业外观设计，旧一律协作过窄；机械肢体服务操作用途不当算法开发。',
'N1000':'Spot维持机械：原文明确RCA故障分析，泛称troubleshooting能力不可直接算现场响应；工艺例示和DFM例示保留。',
'E0520':'Hands：ASME标准是使用不是开发；一般和加分评测错引职责，机械系统/modules上位明确；DOE括号例示。',
'E0521':'柔性Hands：同上修复但保留材料与注塑专门要求；开头背景明确是候选人材料工艺知识，非职责使用。',
'N0677':'Skild机械：本人遥操硬件开发明确，Onshape和制造方法在Preferred；遥操经验有or，不能记无条件。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0432','O6','执行可靠性测试，不是开发可靠性系统/方法。',metric='DUTY_OWN_USE')
ov('E0432','O7','work closely with partners确保符合安全约束，不是本人安全方案开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O9','O10']:ov('E0432',e,'原引职责，改本人实际测试经验要求。',metric='GENERAL',quote='Hands-on experience with prototyping, verification, validation, and reliability testing')
ov('E0432','O13','原引职责，改实际安全知识要求。',metric='GENERAL',quote='Knowledge of regulatory, safety, and compliance requirements')
ov('E0432','1:0','at least one core area e.g. DFMA，任选加例示。',branch='CHOICE_AND_EXAMPLE')
add('E0432','TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL','Plan and execute verification, validation, and reliability testing activities','本人执行测试，与规划开发分别。')
ov('E0434','3:0','实际本人负责skin复杂外表面，与只满足ID约束不同。',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote='Manage the complex surfacing of the robot\'s "skin," ensuring seamless transitions between structural elements and aesthetic covers while maintaining IP (Ingress Protection) and thermal venting requirements.')
ov('E0434','O7','机械肢体用于类人操作，未说明本人实现操作算法。',metric='SEPARATE',branch='MANIPULATION_APPLICATION_OBJECT')
ov('N1000','1:0','focusing on areas such as DFM为例示；DFA/DFM均同一上位。',branch='EXAMPLE')
for e in ['7:0','11:0']:ov('N1000',e,'including but not limited to明确例示。',branch='EXAMPLE')
ov('N1000','15:0','通用故障分析能力缺具体运行响应对象。',metric='SEPARATE',branch='GENERIC_TROUBLESHOOTING_SKILL')
add('N1000','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','Conduct root cause failure analysis to troubleshoot issues from the field and production.','本人根因分析明确，区别于一般排障能力。')
for r in ['E0520','E0521']:
 ov(r,'O9','build and test验证可靠性是评测执行，不是开发可靠性系统。',metric='DUTY_OWN_USE')
 ov(r,'O10','原引职责，改实际一般统计评价要求。',metric='GENERAL',quote='Strong understanding of statistical analysis methods')
 ov(r,'O16' if r=='E0520' else 'O15','原引职责，改Bonus中的验证经验。',metric='PREFERRED',quote='Experience in controls, integration, and validation' + ('.' if r=='E0521' else ''))
 for e in (['O17','O18'] if r=='E0520' else ['O16','O17']):ov(r,e,'systems/modules均为机械系统，不构成上位未知。',branch='UNCONDITIONAL')
 ov(r,'3:0' if r=='E0520' else '4:0','按ASME标准绘图是使用标准而非开发标准。',metric='DUTY_OWN_USE')
 ov(r,'4:0' if r=='E0520' else '7:0','e.g.列举DOE。',branch='EXAMPLE')
ov('E0521','2:0','开头ideal candidate has strong background是一般工艺知识要求。',metric='GENERAL')
ov('N0677','3:0','Preferred段括号工具or other。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('N0677','O3','括号工具or other。',branch='CHOICE_AND_EXAMPLE')
ov('N0677','6:0','Preferred段3D打印经验。',metric='PREFERRED')
ov('N0677','7:0','robotics, teleoperation, or digital twin备选经历。',branch='CHOICE')
ov('N0677','O10','Arduino或类似微控制器均属嵌入式上位。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_mech_d')
