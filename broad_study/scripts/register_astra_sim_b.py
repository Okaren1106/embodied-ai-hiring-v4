from astra_review_tools import *
ids=['E0443','N0843','N0979','N0854']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why,**v):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why,**v))
R['E0443']['judgment']='执行器测试方法研发不等于执行器本体研发，系统辨识明示Apply而非研发辨识方法。Required/Preferred标题需覆盖新增项，并修正多处要求引文误指职责。'
ov('E0443','E0443:O3','Required下including dynamometer or motor test stand。',metric='REQUIRED',branch='CHOICE_AND_EXAMPLE',quote='including operation of dynamometer or motor test stand systems')
ov('E0443','E0443:O4','Python必备应引用Required资格原句。',metric='REQUIRED',quote='Proficiency writing production-grade Python for test automation, data analysis, and post-processing.')
ov('E0443','E0443:O9','性能表征验证执行器，不是开发执行器本体。',metric='DUTY_OWN_USE')
for e in ['E0443:O13','E0443:O14','E0443:O15']:ov('E0443',e,'测试e.g寿命/热限值/驱动性能是测试应用例示。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for e in ['E0443:O20','E0443:O21','E0443:O22']:ov('E0443',e,'处在Required Qualifications。',metric='REQUIRED')
ov('E0443','E0443:O24','必备测试方法经验引用资格而不是工作摘要。',metric='REQUIRED',quote='Demonstrated experience designing test methods and procedures')
ov('E0443','E0443:O28','执行器优先经验引用Preferred原句。',metric='PREFERRED',quote='Experience with humanoid or legged robot actuator systems.')
for e in ['E0443:5:0','E0443:6:0']:ov('E0443',e,'Apply system identification明确使用方法。',metric='DUTY_OWN_USE')
ov('E0443','E0443:7:0','标定经验在Required。',metric='REQUIRED')
ov('E0443','E0443:8:0','系统辨识背景在Preferred。',metric='PREFERRED')
add('E0443','V2_CALIBRATION','DUTY_OWN_USE','EXAMPLE','including firmware deployment, motor and encoder calibration, and functional verification','本人lead bringup包括校准执行，不仅研发流程。')
R['N0843']['judgment']='测试基础设施研发和CI集成清楚，What Will Set You Apart明确优先；新CI要求原误归一般。'
ov('N0843','N0843:3:0','处于What Will Set You Apart。',metric='PREFERRED')
R['N0979']['judgment']='Atlas控制可靠性职责包含真正舰队排障和诊断工具研发，两者分列。修复具名工具关系：like例示、and共同要求、裸括号未明；不把所有工具清单看作任选。'
for e in ['N0979:O9','N0979:4:0']:ov('N0979',e,'Python括号中的Pandas Numpy无显式关系标记，保留未知。',branch='UNRESOLVED')
for e in ['N0979:6:0','N0979:6:1']:ov('N0979',e,'like引出示例而非or。',branch='EXAMPLE')
for e in ['N0979:9:0','N0979:9:1','N0979:9:2','N0979:9:3']:ov('N0979',e,'直接并列and，无任选关系词。',branch='UNCONDITIONAL')
add('N0979','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Lead investigations for complex controls and behavioral issues escalated from Fleet Operations','实际舰队升级问题调查与排障。')
R['N0854']['judgment']='标题Contract/Jr与正文Intern不同，保留原始受众。帮助设计/维护/记录和支持排障不自动等于本人独立开发与校准操作；本人RCA执行明确补入。PLC语言为such as例示。'
ov('N0854','N0854:O3','Assist设计实施验证，未明确本人研发交付。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0854','N0854:3:0','Help document calibration steps不等于执行校准。',metric='SEPARATE',branch='DOCUMENTATION_OBJECT')
ov('N0854','N0854:4:0','Support deployment troubleshooting未明确本人负责；保留协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['N0854:5:1','N0854:5:2','N0854:5:3']:ov('N0854',e,'such as语言清单例示，无or。',branch='EXAMPLE')
add('N0854','V2_RCA','DUTY_OWN_USE','UNCONDITIONAL','Perform root cause analysis on test failures','本人执行测试失败根因分析。')
register(list(R.values()),'Astra_sim_fullread_b')
