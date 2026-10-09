from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0975':'DFX的DFM/DFT示例保留，与N0976差异已核；工具验证主句无条件，不由局部where necessary泛化条件。',
'N0973':'NPI物料库存协作与本人库存指标分析分别记录；ERP采购系统工具要求不等于专业采购方法。',
'N1021':'Atlas生产任务明确，试产支援与独立工艺和验收流程区分；验证主句无条件。',
'N0889':'逐段展开复读与N0888相同文本，地点差异保留；RCA旧标题引用改为实际完整职责。',
'N0802':'自主系统线上问题修复与测试职责成立；所有备选都属于测评的上位类别不应被降为任选。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
ov('N0975','O7','必要时仅修饰能力研究；主句工具验证及合格确认无条件。',branch='UNCONDITIONAL')
ov('N0975','ADD3','设计生产夹治具不直接证明开发测评系统；本句仅明确验证工具。',metric='DUTY_OWN_USE')
add('N0975','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL',25,'明确加工、增材制造及成型方法实践。')
ov('N0973','6:1','ERP或采购系统是工具熟练度，不自动扩成采购专业方法能力。',metric='SEPARATE',branch='TOOL_OBJECT')
add('N0973','SK_INVENTORY','DUTY_OWN_USE','UNCONDITIONAL',11,'本人分析库存周转和准确率指标，区别上一项协作库存管理。')
ov('N1021','O11','工具验证主句无条件，where necessary仅限制后项能力研究。',branch='UNCONDITIONAL')
add('N1021','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL',52,'一般要求独立列加工与增材制造实践，与优先CNC经验分开。')
ov('N0889','1:0','旧引用仅标题，改为实际lead root-cause职责句。',metric='DUTY_OWN_USE',quote=RAW[RID['N0889']]['full_description'].splitlines()[14])
add('N0889','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',7,'本人创建维护从来料到出货的测试协议及门禁标准。')
for e in ['O17','O22','O23']:ov('N0802',e,'所列测试/回归场景/HIL或仿真回归均属测评类别；子型任选不使上位概念未知或任选。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_mfg_r')
