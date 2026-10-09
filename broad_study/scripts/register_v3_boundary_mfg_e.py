from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0124':'关节零部件测试：被测电机/机械/控制特性与本人评测方法分列；测试方案和标准开发补录。',
'N0125':'单板测试：测试方法开发与执行有据；232/485同宽串口族；能独立焊样是能力陈述。',
'N0177':'DQE：质量标准和测试标准本人建立；结构料质量把控不能直接替代机械设计/制造知识。',
'N0064':'认证协调：对接实验室不证明本人实验执行，认证流程本人负责保留。',
'N0006':'测试实习：本人用例脚本开发成立；MCU固件是被测对象；跨工具和跨协议裸斜线不能因等而确定。',
'N0115':'可靠性：明确寿命分析能力和仪器日常维护能力补录；实验标准原名与目录外缺口保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for e in ['O3','O4','O5']:ov('N0124',e,'关节机械和控制性能是被测对象；本人测试实施另有评测标签。',metric='SEPARATE',branch='TEST_OBJECT')
add('N0124','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'明确编制试验方案、用例与测试标准。')
ov('N0125','4:3','RS232/485均属于冻结宽串口组；同族斜线不改变上位，等保留示例。',branch='EXAMPLE')
ov('N0125','O3','电源与信号是测试对象，测试方法改进不等于电力电子设计使用。',metric='SEPARATE',branch='TEST_OBJECT')
add('N0125','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL',13,'能独立完成样品焊接是明确实践能力。')
ov('N0177','O6','物料质量把控是质量对象知识，不证明机械设计或制造方法能力。',metric='SEPARATE',branch='QUALITY_OBJECT')
add('N0177','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',7,'明确建立质量标准与测试规范。')
ov('N0064','O1','对接第三方处理认证测试，是协调对象，非本人实验执行。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O4','O5','10:0','10:1','10:2','10:3']:ov('N0006',e,'跨类裸斜线关系不清，等只标开放列举，不确认每项关系。',branch='UNRESOLVED')
ov('N0006','ADD2','MCU固件是测试脚本验证的对象，不是本人开发或使用嵌入式方法的直接证据。',metric='SEPARATE',branch='TEST_OBJECT')
add('N0115','SK_LIFETIME_PREDICTION','GENERAL','UNCONDITIONAL',24,'明确熟悉疲劳寿命分析方法。')
add('N0115','V2_INCIDENT_SUPPORT','GENERAL','UNCONDITIONAL',22,'明确能处理实验仪器日常故障与基本维护，属于在用设备维护能力。')
register(list(R.values()),'Astra_v3_boundary_mfg_e')
