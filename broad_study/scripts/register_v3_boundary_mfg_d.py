from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0468':'硬件测试实习：协助与在岗学习不当本人独立职责；查看原理图/PCB图中PCB能力路径不清保留未知。',
'N0637':'整机工艺：SOP和PFMEA实际输出明确；AutoCAD/SolidWorks跨软件斜线关系未知。',
'N0651':'模组测试实习：本广告明确制定并执行测试，不因实习头衔降级；平台搭建参与、根因协助分别保留。',
'N0638':'整机执行测试：测试设备熟练操作是能力陈述；Python/LabVIEW内部关系不清，测试脚本或自动测试仍同评测上位。',
'N0653':'结构SQE：展开相同来源句，审核/质量管控不等于本人加工或采购；APQP、PPAP本人实施。',
'N0625':'关节SQE：驻厂监督不等于实际标定加工；质量工具本人使用与供方使用FMEA区分。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
R['N0468']['additions'].append(dict(code='SK_PCB',metric='PREFERRED',branch='UNRESOLVED',quote=RAW[RID['N0468']]['full_description'].splitlines()[25],reason='查看PCB图为相关知识，但原理图/PCB图关系不清，限定优先能力未知。'))
for e in ['O3','7:0']:ov('N0637',e,'不同设计软件裸斜线，等不能决定同时或任选。',branch='UNRESOLVED')
ov('N0651','O4','同句前半明确制定测试计划用例；另一证据保存执行。',metric='DUTY_OWN_DEVELOP')
for e in ['O3','2:0']:ov('N0638',e,'外层脚本或自动测试有任选，但Python/LabVIEW内层裸斜线仍不清。',branch='UNRESOLVED')
ov('N0638','O10','脚本编写和自动化测试均为评测能力，上位无任选。',branch='UNCONDITIONAL')
ov('N0638','ADD1','熟练操作为能力陈述，不能仅凭所在职责栏当实际使用。',metric='GENERAL')
register(list(R.values()),'Astra_v3_boundary_mfg_d')
