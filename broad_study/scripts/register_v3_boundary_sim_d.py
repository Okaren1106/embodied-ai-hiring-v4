from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N1012':'制造测试开发：such as Python是必备语境的例示；DFT与可靠性为团队合作；DFX在优先标题下，电源仪器在必备标题下。',
'N0968':'SQA：ideally Playwright及highly desirable语言是优先；JS/TS斜杠未知；React不能直接当JavaScript语言；Git泛称版本控制上位可保留。',
'N0969':'热流仿真：一般核心技能与Required Experience标题分别保留；热科学学位领域不当技术操作要求。',
'N0978':'测试软件：库示例、版本控制例示及MES任选修正；同类测试工具上位不随示例变为选择。',
'N1005':'电气产测：床针与翻盖均测试上位；DFT目录包含bed-of-nails，保留该方法；LabVIEW/TestStand为例示、MES为选择。',
'N0797':'传感器标定：Ceres/GTSAM/g2o在What You Have一般要求下，且such as；标题证据修正为实际标定职责。',
'E0483':'测试实习：C单独明列为编程例示，非C/C++未解；优先机械/执行器要求错引一般或职责需修定位。',
'E0573':'执行器测试：Simulink一般要求误引职责，重定位F18；actuation与motor同上位；补明示标定与测功机一般要求。',
'N0680':'物理仿真：只列Preferred；跨团队Sim2Real合作与亲自物理求解器研发分开；DR为优先非一般。',
'N0713':'系统辨识控制：标定/控制优先经验应引用F22；所有资格均Preferred；补FOC和经典控制方法明确知识。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
for e in ['O1','O4']:ov('N1012',e,'such as Python具体例示。',branch='EXAMPLE')
for e in ['O17','3:0','4:0']:ov('N1012',e,'DFT实施和可靠性优化为Partner with团队合作。',metric='SEPARATE',branch='COLLABORATION',**({'quote':line('N1012',10)} if e=='3:0' else {}))
for e in ['O21','O22']:ov('N1012',e,'选择COTS或定制硬件均属测试上位。',branch='UNCONDITIONAL')
ov('N1012','5:0','Required Skills下including仪器列举。',metric='REQUIRED',branch='EXAMPLE')
ov('N1012','8:0','Preferred Skills标题下DfX知识。',metric='PREFERRED')
ov('N0968','7:0','ideally using Playwright明确优先。',metric='PREFERRED')
for e in ['9:0','9:1']:ov('N0968',e,'highly desirable且两语言间斜杠关系未明。',metric='PREFERRED',branch='UNRESOLVED')
ov('N0968','9:2','e.g. pytest为具体例示。',branch='EXAMPLE')
ov('N0968','O12','physical robotics or embedded platforms。',branch='CHOICE')
ov('N0968','24:0','React.js工具名不能直接证明JavaScript语言知识。',metric='SEPARATE',branch='FRAMEWORK_NOT_LANGUAGE')
ov('N0968','24:1','modern web frameworks括号内React是示例，并无or。',branch='EXAMPLE')
ov('N0968','1:0','developing HIL testing strategies，属于测试能力开发。',metric='DUTY_OWN_DEVELOP')
ov('N0968','O16','including simulation, field testing, or stress testing兼选择和例示。',branch='CHOICE_AND_EXAMPLE')
for e in ['O17','O18']:ov('N0968',e,'所有选项均是测试经验，上位评测明确。',branch='UNCONDITIONAL')
ov('N0969','O25','学位及研究专业字段，与技术能力和使用要求分开。',metric='SEPARATE',branch='DEGREE_FIELD')
ov('N0978','O13','actuation subsystems or related tech跨具体领域选择。',branch='CHOICE')
ov('N0978','4:0','e.g. Git为版本控制工具示例。',branch='EXAMPLE')
for e in ['8:0','8:1']:ov('N0978',e,'e.g.框架示例，无or。',branch='EXAMPLE')
ov('N0978','14:0','SPC,yield tracking,or MES任选。',branch='CHOICE')
ov('N0978','O19','明确测试执行框架经验，上位评测不受具体框架例示影响。',branch='UNCONDITIONAL')
for e in ['O21','O22']:ov('N1005',e,'全部选项均是PCBA测试夹具，上位评测明确。',branch='UNCONDITIONAL')
for e in ['9:0','9:1']:ov('N1005',e,'e.g.框架示例，无or。',branch='EXAMPLE')
ov('N1005','16:0','SPC,yield tracking,or MES任选。',branch='CHOICE')
ov('N1005','O27','测试执行框架上位明确。',branch='UNCONDITIONAL')
for e in ['11:0','11:1']:ov('N0797',e,'such as列举工具，无or。',branch='EXAMPLE')
for e in ['15:0','15:1','15:2']:ov('N0797',e,'What You Have一般要求，such as例示。',metric='GENERAL',branch='EXAMPLE')
ov('N0797','1:0','职位标题不足，重定位明确标定研发F15。',metric='DUTY_OWN_DEVELOP',quote=line('N0797',15))
ov('E0483','2:1','C与C++分别逗号列举，e.g.例示，不是未解斜杠。',branch='EXAMPLE')
ov('E0483','O11','Facilitate电机控制器集成，属于促进协作而非本人控制闭环。',metric='SEPARATE',branch='INTEGRATION_SUPPORT')
ov('E0483','O14','优先机械设计能力在F23。',metric='PREFERRED',quote=line('E0483',23))
ov('E0483','O17','优先执行器经验在F27。',metric='PREFERRED',quote=line('E0483',27))
for e in ['O4','O5']:ov('E0573',e,'一般要求应引F18而非职责F7；Simulink Real-Time独立列举保留正例。',metric='GENERAL',quote=line('E0573',18))
ov('E0573','O7','开发测试系统职责在F6，F9只校准测量。',metric='DUTY_OWN_DEVELOP',quote=line('E0573',6))
for e in ['O15','O16']:ov('E0573',e,'actuation or motor都在执行器上位。',branch='UNCONDITIONAL')
add('E0573','V2_CALIBRATION','GENERAL','UNCONDITIONAL',line('E0573',17),'明确传感器集成标定经验。')
add('E0573','SK_DYNAMOMETER','GENERAL','UNCONDITIONAL',line('E0573',15),'包括测功机的测试建设经验明确。')
for e in ['1:0','2:0','3:0','3:1','4:0']:ov('N0680',e,'与外部/内部团队合作或贡献策略，不独立承担迁移标定。',metric='SEPARATE',branch='COLLABORATION')
ov('N0680','6:0','Preferred Qualifications内的DR方法。',metric='PREFERRED')
for e in ['O8','O9','O10']:ov('N0680',e,'备选均属于仿真上位。',branch='UNCONDITIONAL')
for e in ['O29','O30']:ov('N0713',e,'优先标定或控制跨机群经验实际F22，原F10是职责。',metric='PREFERRED',quote=line('N0713',22))
ov('N0713','8:0','原文Preferred Qualifications。',metric='PREFERRED')
ov('N0713','11:0','calibration or controls。',branch='CHOICE')
add('N0713','V2_CLASSICAL_CONTROL','PREFERRED','UNCONDITIONAL',line('N0713',18),'field-oriented control是目录明示FOC方法。')
add('N0713','V2_CLASSICAL_CONTROL','DUTY_OWN_USE','UNCONDITIONAL',line('N0713',10),'本人应用经典控制，列状态估计、校准及稳定性/带宽分析。')
register(list(R.values()),'Astra_v3_boundary_sim_d')
