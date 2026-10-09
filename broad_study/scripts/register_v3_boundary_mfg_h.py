from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0285':'电子采购的物料对象、协助谈判与本人采购职责分别记录；要求和ERP示例成立。',
'N0323':'端到端测试方案开发与执行分列；中间件、模型和驱动为被测对象，原文技术出现仍保留。实时专项还明确优化，保留本人使用。',
'N0335':'独立核对相同职责和资格符号差异；采用与N0323相同对象边界，非新增独立样本。',
'N0274':'SDK语言是接口被测对象，不据此证明本人用该语言；一般要求的Python或C++仍为明确任选。',
'N0269':'工艺设计、DOE与可制造性评审成立，Creo/SW工程软件示例与采购对象分开。',
'N0287':'质量监测指标不等于本人执行测试；APQP与IPD斜线关系未知，根因分析有主导或组织之别。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for r in ['N0323','N0335']:
 for e in ['O1','O2','O8','O10','O11','O12','1:0','4:0','4:1','4:2','4:3']:
  ov(r,e,'仅证实本人测试该系统、协议或指标；被测对象保留技术出现，不自动等同本人以其为工具执行。',metric='SEPARATE',branch='TEST_OBJECT')
 add(r,'TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',2,'明确设计全场景性能测试方案，不只有测试执行。')
for e in ['O1','O2','O6']:ov('N0274',e,'SDK语言或稳定性是明确被测对象/指标，保留出现，不推断技术使用。',metric='SEPARATE',branch='TEST_OBJECT')
add('N0274','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',4,'本人设计端到端场景化测试用例。')
ov('N0287','O6','收集分析测试覆盖率等质量指标不直接证明本人测试执行。',metric='SEPARATE',branch='METRICS_OBJECT')
ov('N0287','4:0','IPD/APQP跨方法裸斜线未能确定并列或任选；外层如不消除此未知。',branch='UNRESOLVED')
ov('N0287','ADD1','主导或组织根因分析未确定本人分析方法执行与仅组织的关系。',branch='UNRESOLVED')
register(list(R.values()),'Astra_v3_boundary_mfg_h')
