from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0455':'机床程序编写、操作和在用机床维修明确；补录焊接/制造经验优先。',
'E0536':'生产装配、检验和安全执行明确；未来面试时间保留，不当作已有员工数。',
'E0541':'过程检验与8D知识明确；CATIA/CAD的CAD上位类别成立，两个质量体系标准同属一类。',
'E0540':'机械或机电原型装配属于同一机械类别；IPC个人认证与标准应用区别保留。',
'E0467':'电气验证与Python工具开发均明确；灵巧手/夹爪硬件经验不自动成为抓取操作算法。',
'E0542':'本人尺寸功能检验与实验室管理分开；GD&T两个版本同属同一标准类别。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
add('E0455','V2_CNC_PROCESS','DUTY_OWN_DEVELOP','UNCONDITIONAL',6,'明确本人编制机床加工程序，与操机分别记录。')
add('E0455','V2_CNC_PROCESS','PREFERRED','UNCONDITIONAL',24,'fabrication和welding均属于冻结加工制造类别，and/or不改变上位类别出现。')
for e in ['O1','O3','5:0']:ov('E0541',e,'8D括号无示例词；CAD涵盖CATIA；两种质量体系标准均属同一类别，各按相应层级确定。',branch='UNCONDITIONAL')
for e in ['O6','O7','3:0']:ov('E0540',e,'列举的机械/机电原型装配或加工增材方法均属于各自同一上位类别。',branch='UNCONDITIONAL')
ov('E0540','2:0','IPC认证是个人资格要求，未独立要求标准使用或知识，资格类别保留。',metric='SEPARATE',branch='CREDENTIAL_OBJECT')
ov('E0467','O20','该段是灵巧手/夹爪/多自由度执行系统的硬件经验，不足以证明机器人操作或抓取技术。',metric='SEPARATE',branch='HAND_HARDWARE_OBJECT')
ov('E0542','2:0','ASME Y14.5两版本均为同一GD&T标准类别。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_mfg_u')
