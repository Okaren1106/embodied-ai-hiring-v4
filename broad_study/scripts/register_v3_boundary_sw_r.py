from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0922':'机器人平台；云和CI在优先段，不是一般资格。',
'N0921':'SRE安全平台；云工具优先段与IaC一般段分开，安全类别内部替代不产生上层未知。',
'E0605':'制造测试软件；开发的是测试流程与系统，用到固件，偏好经历不作一般要求。',
'E0581':'机器人实时管线；作用于执行器的数据管线不是开发执行器本体，perf列表无例示词。',
'N0692':'操作软件；定位强化学习和控制资格至正确来源，框架继承至少一门与such as。',
'N0667':'Web全栈；Node用于应用开发，JS/TS裸斜线未解，MongoDB与AWS处于优先段。',
'N0693':'操作控制软件；同款正文逐条核对，纠正与N0692相同的资格错位和分支。',
'N0701':'DevOps；优先条款被写成一般要求，云平台裸斜线未解，HIL职责锚明确测试基础设施。',
'N0705':'机器人基础设施；优先云服务保留示例任选，实时数据管线是明确工作对象。',
'N0711':'制造测试软件；泛电机控制器不推出电力电子，ERP为可选系统示例。',
'N0668':'前端Android；JS/TS裸斜线未解，图形引擎继承or，感知输出可视化与开发感知区分。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
for e in ['4:0','4:1']:ov('N0922',e,'Nice to have段。',metric='PREFERRED')
for e in ['O17','O18','O19','O20','O21','O22','O23','O24','O25','O26','O27','O28','O29','O30','O31','O32']:
 ov('N0921',e,'列举对象均为同一安全类别，不由下位替代推上层未知或任选。',branch='UNCONDITIONAL')
for e in ['9:0','9:1']:ov('N0921',e,'one or more与such as并存。',branch='CHOICE_AND_EXAMPLE')
for e in ['14:0','14:1','14:2']:ov('N0921',e,'Nice to Have优先云平台。',metric='PREFERRED')
for e in ['20:0','20:1']:ov('N0921',e,'Nice to Have，such as及or similar共同限定。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('E0605','O7','开发的是下载更新固件的机制，固件为本人处理使用对象。',metric='DUTY_OWN_USE')
ov('E0605','O11','preferably involving说明优先经历。',metric='PREFERRED')
ov('E0605','O15','一般测试资格改锚F43，原为职责。',metric='GENERAL',quote=ln('E0605',43))
ov('E0605','1:0','本人开发供技师执行标定的系统，不是本人执行标定。',metric='DUTY_OWN_DEVELOP')
ov('E0581','O14','开发执行器数据管线，非执行器本体；保留使用对象。',metric='DUTY_OWN_USE')
ov('E0581','2:0','括号列举没有示例或任选词。',branch='UNCONDITIONAL')
for r in ['N0692','N0693']:
 for e in ['O5','O6','O7']:ov(r,e,'at least one与such as共同限定。',branch='CHOICE_AND_EXAMPLE')
 ov(r,'O14','岗位概述明确本人部署学习算法，改锚直接责任句。',metric='DUTY_OWN_USE',quote=ln(r,4))
 ov(r,'O18','优先控制示例来自F15，原F4为一般概述。',metric='PREFERRED',quote=ln(r,15))
 ov(r,'O22','RL资格在F20，会议缩写RSS等不是RL证据。',metric='PREFERRED',quote=ln(r,20))
ov('N0667','1:0','使用NodeJS开发服务器应用。',metric='DUTY_OWN_USE')
for e in ['8:0','8:1']:ov('N0667',e,'不同语言裸斜线没有明确关系。',branch='UNRESOLVED')
ov('N0667','18:0','Preferred内括号没有任选词。',metric='PREFERRED',branch='UNCONDITIONAL')
ov('N0667','22:0','React Three Fiber不是冻结React/React.js/React Native明确别名，不自动补上游框架。',metric='SEPARATE',branch='RELATED_TOOL_NOT_EXACT_ALIAS')
ov('N0667','25:0','Preferred段AWS经验。',metric='PREFERRED')
for e,n in [('O2',16),('O11',16)]:ov('N0701',e,'优先资格原错锚职责，改F16。',metric='PREFERRED',quote=ln('N0701',n))
ov('N0701','O8','编译工具针对嵌入式平台，平台为使用对象。',metric='DUTY_OWN_USE')
ov('N0701','2:0','扩展build配置工具链，不开发Bazel本体。',metric='DUTY_OWN_USE')
ov('N0701','7:1','明确本人搭建HIL测试基础设施，移至无斜线的F4。',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote=ln('N0701',4))
for e in ['14:0','14:1','14:2']:ov('N0701',e,'AWS/GCP/Azure裸斜线无明确关系。',branch='UNRESOLVED')
for e in ['21:0','22:0','22:1','23:0']:ov('N0701',e,'Preferred Qualifications段。',metric='PREFERRED')
ov('N0701','22:0','SIL/HIL裸斜线未解。',branch='UNRESOLVED')
for e in ['6:0','6:1']:ov('N0705',e,'Preferred Qualifications，such as和or related。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('N0711','O1','such as及or引出的ERP例示。',branch='CHOICE_AND_EXAMPLE')
ov('N0711','O5','motor controllers没有明确电力电子技术，不从控制器名称推值。',metric='SEPARATE',branch='OBJECT_NOT_POWER_ELECTRONICS')
ov('N0711','O9','机械制造背景是跨行业偏好列表中的任选。',branch='CHOICE')
ov('N0711','1:0','HIL是自动测试软件的including示例。',branch='EXAMPLE')
ov('N0711','1:1','标定属于测试自动化开发的including示例。',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE')
for e in ['2:0','2:1']:ov('N0711',e,'破折号展开实物系统列表，没有示例词。',branch='UNCONDITIONAL')
ov('N0711','5:0','broader MES/factory systems上层明确，后续示例未把MES变成任选。',branch='UNCONDITIONAL')
ov('N0711','5:1','such as与or都限定PLM。',branch='CHOICE_AND_EXAMPLE')
for e in ['2:0','2:1','5:0','5:1','12:0','12:1']:ov('N0668',e,'JS/TS不同语言裸斜线，未明确各自要求关系。',branch='UNRESOLVED')
register(list(R.values()),'Astra_v3_boundary_sw_r')
# E0107 is two distinct frozen identities, never a reading-ID primary key.
rr=[]
for k,a in AD.items():
 if a['reading_id']!='E0107':continue
 row=dict(reading_id='E0107',identity_key=k,review_mode='FULL_SOURCE_AND_CODING',judgment='逐字段全文核对同文不同岗位ID；保留两个身份，修正职责/优先错锚与ROS裸斜线；不按阅读编号合并。',evidence_overrides=[],additions=[])
 def change(e,why,**f):row['evidence_overrides'].append(dict(evidence_id='E0107:'+e,reason=why,**f))
 for e in ['O1','O2']:change(e,'ROS/ROS2裸斜线关系未知。',branch='UNRESOLVED')
 change('O5','优先证据应在R11，原错锚D3。',metric='PREFERRED',quote=RAW[k]['requirements'].splitlines()[10])
 for e in ['O10','O11']:change(e,'相关经验列表带等，按示例保留。',branch='EXAMPLE')
 change('O12','优先VLA资格在F21，原错锚职责。',metric='PREFERRED',quote=RAW[k]['full_description'].splitlines()[20])
 change('O15','优先多模态资格在F22，原错锚职责。',metric='PREFERRED',quote=RAW[k]['full_description'].splitlines()[21])
 rr.append(row)
register(rr,'Astra_v3_full_E0107_distinct_identities')
