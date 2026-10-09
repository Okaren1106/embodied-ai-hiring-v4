from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0318':'生产排程与ERP操作明确；ERP/MRP关系未知，不把计划场景模拟自行归物理仿真。',
'E0332':'现场故障质量管理和处置协议建立明确；要求方法与证书分别记录，证书不重复扩为Lean方法要求。',
'E0327':'机器人机械装配、检验维修和安全作业本人负责；Minimum经验与Bonus工具要求分开。',
'E0383':'质量经理的团队测试监督不等于本人测试；本人审核PPAP、制定出货流程及工具要求可判。',
'E0381':'供应商制造工程仍有独立寻源证据，技术质量审核和采购不相互替代；资格证书与方法分列。',
'E0401':'工艺开发不等于评测方法开发，qualify/validate是评测执行；本人夹治具设计与采购另补。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for r,e in [('E0332','5:0'),('E0381','9:0')]:ov(r,e,'资格证书名称保留资格类别，不额外推方法经验。',metric='SEPARATE',branch='CREDENTIAL_OBJECT')
ov('E0327','O7','test bench of power是实验室电源工具要求，不直接是电力电子技术要求。',metric='SEPARATE',branch='INSTRUMENT_OBJECT')
add('E0327','TC_MECHANICAL','DUTY_OWN_USE','UNCONDITIONAL',5,'本人装配和维修机器人机电组件。')
add('E0327','V2_CNC_PROCESS','PREFERRED','UNCONDITIONAL',40,'明确电子部件焊接拆焊经验加分。')
ov('E0383','O4','负责团队、监督开发测试和推动处理问题，原句未证明本人测评执行。',metric='SEPARATE',branch='MANAGED_TEST_ACTIVITY')
ov('E0383','ADD2','主导问题解决流程和推动整改未具体表述本人运用根因分析；保留流程负责。',metric='SEPARATE',branch='COORDINATION_OBJECT')
add('E0383','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',13,'本人建立出货检验程序和客户审计流程。')
add('E0383','TC_MECHANICAL','GENERAL','UNCONDITIONAL',16,'明确机械工程基础要求。')
ov('E0401','O12','定义制造工艺与验证该工艺，不等于开发测评方法；原句qualify支持测试评价执行。',metric='DUTY_OWN_USE')
add('E0401','TC_MECHANICAL','DUTY_OWN_DEVELOP','UNCONDITIONAL',8,'本人设计定制装配夹治具。')
add('E0401','V2_PROCUREMENT','DUTY_OWN_USE','UNCONDITIONAL',8,'明确本人采购定制夹治具及生产工具。')
register(list(R.values()),'Astra_v3_boundary_mfg_o')
