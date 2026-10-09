from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0145':'工业仿真：编程语言关系未知不影响扩展仿真器上位能力；CI集成支持训练，不足以确认本人训练基础设施开发。',
'N0027':'校招仿真：参与与明确建设评测分开；资产格式是加分要求且例示；HIL与遥操受或选择，Git软件方法等例示。',
'N0170':'运控仿真系统：控制算法是参与且MPC为所支撑对象；同类仿真引擎任选不削弱仿真上位；系统辨识有直接职责与优先分支。',
'N0283':'计算物理：参与实验不升格独立验证；SciPy同时受或与等约束，有限元/差分关系未明但数值方法明确。',
'N0295':'仿真器扩展：USD/Omniverse为使用基础，不能写成开发标准或平台本身；补敏捷流程一般要求；代码API语言斜杠仍保留不明。',
'N0359':'CAE求解器：必须掌握iFEM不扩成C/C++语言必备；Eigen等是优先例示；补明确数值求解方法。',
'E0255':'产测软件：软件/工具同属评测上位；shell/LabVIEW兼具至少一种和如；电机控制及ROS为等经验例示加分。',
'E0360':'HiL软件基建：Core Requirements覆盖新旧全部条目；优先Linux引用回正确语境；建电机仿真模型和测试固件不等于开发实物执行器/固件。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0145','O7','本人集成仿真与CI，训练是支持目标。',metric='SEPARATE',branch='SUPPORTED_TRAINING_OBJECT')
ov('N0145','O9','仿真器扩展能力明确，语言斜杠只影响具体语言。',branch='UNCONDITIONAL')
for e in ['O1','O2','O3','O25','O28','O29','1:0','1:1','4:0','4:1']:ov('N0027',e,'原文参与研发/建设，无独立承担声明。',metric='SEPARATE',branch='PARTICIPATION')
ov('N0027','O27','参与接口封装且控制器是平台对象。',metric='SEPARATE',branch='PLATFORM_OBJECT')
ov('N0027','6:0','Git、构建调试、自动化测试等为例示。',branch='EXAMPLE')
for e in ['8:0','8:1']:ov('N0027',e,'至少一种加如，二重分支。',branch='CHOICE_AND_EXAMPLE')
for e in ['11:0','17:0']:ov('N0027',e,'等例示，没有任选词。',branch='EXAMPLE')
for e in ['19:0','19:1','19:2','19:3']:ov('N0027',e,'加分项下等格式示例。',metric='PREFERRED',branch='EXAMPLE')
for e in ['24:0','25:0','25:1']:ov('N0027',e,'优先经验清单有或。',branch='CHOICE')
add('N0027','V2_HIL','PREFERRED','CHOICE',line('N0027',43),'硬件在环明确列为任选加分经验。')
for e in ['O1','O2','O3']:ov('N0170',e,'基于等软件为例示。',branch='EXAMPLE')
ov('N0170','O17','参与控制算法设计实现。',metric='SEPARATE',branch='PARTICIPATION')
ov('N0170','4:0','MPC为中间件所支持的上层对象。',metric='SEPARATE',branch='SUPPORTED_ALGORITHM_OBJECT')
for e in ['O20','O21','5:0']:ov('N0170',e,'跟踪并引入如可微物理/学习辨识等技术，属于方法使用示例。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for i in range(23,27):ov('N0170','O'+str(i),'全部备选均属仿真上位。',branch='UNCONDITIONAL')
ov('N0170','12:0','等库示例。',branch='EXAMPLE')
ov('N0170','15:0','如控制框架是例示，未明任选。',branch='EXAMPLE')
ov('N0170','18:0','可微物理或学习辨识。',branch='CHOICE')
add('N0170','V2_SYSID','DUTY_OWN_USE','UNCONDITIONAL',line('N0170',13),'负责系统动力学参数辨识，有直接职责，不仅跟踪前沿。')
ov('N0283','O9','参与传感器实验验证。',metric='SEPARATE',branch='PARTICIPATION')
ov('N0283','1:0','NumPy/SciPy或TensorFlow等，具体库是选择兼例示。',branch='CHOICE_AND_EXAMPLE')
ov('N0283','14:0','如Git具体例示。',branch='EXAMPLE')
for e in ['1:0','1:1']:ov('N0295',e,'基于Kit和USD开发自有扩展，非修改Omniverse平台或USD标准本身。',metric='DUTY_OWN_USE')
for e in ['O2','O3']:ov('N0295',e,'API语言斜杠关系未明，Python独立证据另保留。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
add('N0295','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','熟悉设计模式与敏捷开发流程。','敏捷流程在冻结项目方法定义内。')
ov('N0359','8:1','等开源库例示无任选词。',branch='EXAMPLE')
add('N0359','V2_FE_TOPOLOGY','DUTY_OWN_DEVELOP','UNCONDITIONAL',line('N0359',3),'明确开发有限元数值求解模块。')
add('N0359','V2_FE_TOPOLOGY','GENERAL','UNCONDITIONAL',line('N0359',11),'稀疏矩阵求解与数值算法优化能力明确。')
add('N0359','V2_FE_TOPOLOGY','REQUIRED','UNCONDITIONAL','必须掌握反有限元方法（iFEM）理论基础与实现原理（应变场最小二乘重构、正则化方法、病态问题处理、载荷反演与边界条件识别）','必须掌握数值求解研究方法。')
ov('E0255','O10','软件与工具均属评测上位。',branch='UNCONDITIONAL')
for e in ['1:0','1:1']:ov('E0255',e,'至少一种且如。',branch='CHOICE_AND_EXAMPLE')
for e in ['O7','O13']:ov('E0255',e,'等相关经验为优先例示。',branch='EXAMPLE')
ov('E0360','O6','Linux优先要求在F32，不能引用职责F16。',metric='PREFERRED',quote=line('E0360',32))
for e in ['O15','O16']:ov('E0360',e,'电机是仿真模型对象、固件是回归测试对象。',metric='SEPARATE',branch='SIMULATION_OR_TEST_OBJECT')
for e in ['O18','O19','O20']:ov('E0360',e,'所有选项均为测试验证，上位评测明确。',branch='UNCONDITIONAL')
ov('E0360','O22','robotic or embedded限定系统经验任选。',branch='CHOICE')
for e in ['8:0','9:0','9:1','10:0','10:1','10:2','10:3','10:4','10:5']:ov('E0360',e,'受Core Requirements标题约束。',metric='REQUIRED')
ov('E0360','1:0','原引职位名称不足，重定位职责F5。',metric='DUTY_OWN_DEVELOP',quote=line('E0360',5))
ov('E0360','3:0','原引小标题，重定位具体管线建设F10。',metric='DUTY_OWN_DEVELOP',quote=line('E0360',10))
register(list(R.values()),'Astra_v3_boundary_sim_c')
