from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0182':'白盒验证的计划、执行与EMC/SI方法明确；协议名称仅为被测信号对象，通用接口知识斜线保留未知。',
'E0172':'云平台质量测试与设计测试用例明确，回归验证定位到总体本人测试职责；数据库列举与中间件示例分开。',
'E0148':'工装、用例开发和直接测试区分，失效分析及可靠性目标保留概念层执行；语言明确任选。',
'E0124':'关节选型测试集成与机械接口对接为本人技术应用，不等同开发关节或机械部件；至少一方向要求保留任选。',
'E0367':'本人系统验证、仿真测试和安全协助分别成立；必备上位安全标准不随编号示例成为任选。',
'E0331':'独立测试开发执行与追溯明确；电控电子不等同运动控制算法，测试电源仪器不自动扩成电源技术要求。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for e in ['1:0','1:1','1:2']:ov('E0182',e,'协议是信号完整性被测对象；未据此证明用该协议实现测试或通信。',metric='SEPARATE',branch='TEST_OBJECT')
ov('E0182','O5','测试电机驱动单板直接指功率电路，而非执行器或电机本体。',metric='SEPARATE',branch='DRIVE_CIRCUIT_OBJECT')
add('E0182','SK_PCB','GENERAL','UNCONDITIONAL',12,'明确能独立阅读PCB。')
ov('E0172','ADD1','协助研发句存在承担关系歧义；以首条明确负责平台测试的完整职责为执行证据。',metric='DUTY_OWN_USE',quote=RAW[RID['E0172']]['full_description'].splitlines()[1])
for e in ['O2','O3']:ov('E0124',e,'原文明确选型、测试、集成或接口对接，未表述开发技术产物。',metric='DUTY_OWN_USE')
ov('E0367','3:0','functional safety standards为明确必备上位概念；编号such as不把该类别本身变成任选示例。',branch='UNCONDITIONAL')
ov('E0331','O10','control electronics未明确运动控制或控制器算法，不能只由control词推出该概念。',metric='SEPARATE',branch='ELECTRONIC_TEST_OBJECT')
ov('E0331','O20','此处power supplies为lab tools示例，不能由仪器名自动推出电源电路技术要求。',metric='SEPARATE',branch='INSTRUMENT_OBJECT')
register(list(R.values()),'Astra_v3_boundary_mfg_m')
