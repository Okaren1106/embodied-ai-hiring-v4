from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0071':'遥操算法开发与跟踪技术分开；一般和优先遥操经历补齐。',
'E0061':'Agent及模型推理工程化，框架间斜线未解，一般资格不误标优先。',
'E0047':'HMI移动端，USB为一般了解而非优先，稳定通信及可靠运行明确。',
'E0031':'VR示教采集应用用Unity，职责与资格分离；用任职原句定位。',
'E0026':'CI/CD流水线开发使用GitLab CI；支撑大模型迭代不等于模型本人开发。',
'E0282':'应用SDK开发，功能示例与真实用途分开，CI/CD为一般工程实践示例。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('E0071','O7','力反馈等控制功能在包括列表内。',branch='EXAMPLE')
ov('E0071','O9','包括但不限于所列技术。',branch='EXAMPLE')
ov('E0071','4:0','跟踪前沿技术不是使用遥操。',metric='SEPARATE',branch='TECHNOLOGY_MONITORING')
add('E0071','V2_TELEOP','GENERAL','UNCONDITIONAL',9,'明确两年以上遥操系统及算法开发经验。')
add('E0071','V2_TELEOP','PREFERRED','UNCONDITIONAL',13,'明确具身或医疗行业遥操系统经验优先，同类别内部场景不拆任选。')
ov('E0061','4:0','上层Agent开发框架明确要求；具体框架同类别内斜线不使上层变示例。',branch='UNCONDITIONAL')
for e in ['6:0','6:1']:ov('E0061',e,'大模型工程化一般要求，框架裸斜线未解。',metric='GENERAL',branch='UNRESOLVED')
ov('E0047','2:0','了解USB为一般资格，优先只修饰后半句低延迟实时处理。',metric='GENERAL',branch='EXAMPLE')
add('E0047','TC_RELIABILITY','DUTY_OWN_DEVELOP','UNCONDITIONAL',3,'设计通信方案保障稳定性与一致性。')
ov('E0031','2:0','基于Unity开发VR应用为工具使用，Unity/OpenXR/SDK裸斜线未解。',metric='DUTY_OWN_USE',branch='UNRESOLVED')
ov('E0031','3:0','F13开发经验明确或，另有F14直接要求Unity。',branch='CHOICE')
add('E0031','V2_UNITY','GENERAL','UNCONDITIONAL',14,'F14明确熟悉Unity开发。')
for e in ['O8','O9']:ov('E0031',e,'改锚任职数据对接经验，原引用职责。',metric='GENERAL',quote=ln('E0031',17))
ov('E0031','O10','数据采集或相关工具经验明确或，非示例词范围。',branch='CHOICE')
ov('E0031','O11','SLAM地图与其他三维经验明确或。',branch='CHOICE')
for e in ['O4','5:0','5:1']:ov('E0031',e,'任职一般要求一种或多种且等，TCP/UDP同一类别不引入额外未知。',metric='GENERAL',branch='CHOICE_AND_EXAMPLE')
for e in ['6:0','7:0']:ov('E0031',e,'加分经验中明确或。',branch='CHOICE')
ov('E0026','O5','建设自动化质量门禁及评测集成，属于评测机制开发。',metric='DUTY_OWN_DEVELOP')
ov('E0026','O6','要求支撑大模型迭代的流水线经验，模型为支撑对象。',metric='SEPARATE',branch='TOOLCHAIN_TARGET')
ov('E0026','O8','优先要求改锚F13真实任职句，原句为职责。',metric='PREFERRED',quote=ln('E0026',13))
ov('E0026','1:1','基于GitLab搭建流水线为使用GitLab CI，非修改平台本体。',metric='DUTY_OWN_USE')
for e in ['7:0','11:0']:ov('E0026',e,'Shell/Python裸斜线未解。',branch='UNRESOLVED')
for e in ['O6','O7','O8','1:0','1:1']:ov('E0282',e,'功能包括且以等结尾。',branch='EXAMPLE')
ov('E0282','2:0','通信场景以等结尾。',branch='EXAMPLE')
for e in ['O17','5:0']:ov('E0282',e,'工程实践以等列举。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_sw_i')
