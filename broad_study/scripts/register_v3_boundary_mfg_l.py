from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0268':'结构模组测试与测试治具方案开发明确；电机概念本人测试不冒称电机开发。',
'E0257':'可靠性策略、执行和失效分析齐全；分号后Minitab/JMP及GRR不受上一仪器示例的等控制。',
'E0253':'库存和翻新物料计划明确；故障率是备件预测输入，不是本人可靠性工程；ERP跟进与实际操作未明。',
'E0221':'全链路测试开发执行、CI门禁及观测建立明确；语言至少一种，CI工具和ROS工具裸斜线未知。',
'E0203':'EMC测试设计与标准化流程制定不等于开发EMC技术，改为方法使用并补测试流程规范开发。',
'E0188':'CNC程序和工艺设计、操机及设备维护分别明确；上游3D图档软件不直接映射本人使用。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
for e in ['O9','O10','3:0']:ov('E0257',e,'分号后掌握Minitab/JMP/GRR/CPK独立要求，前句仪器等不跨分号生效。',branch='UNCONDITIONAL')
ov('E0257','4:0','明确要求安全与可靠性标准这个上位类别，标准编号为类别内示例。',branch='UNCONDITIONAL')
add('E0257','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'本人制定验证规范与验收准则。')
add('E0257','TC_EVALUATION','DUTY_OWN_USE','UNCONDITIONAL',7,'本人主导执行整机和部件的可靠性验证。')
ov('E0253','O5','产品设备故障率是供应备件预测的数据输入，不是本人承担系统可靠性目标。',metric='SEPARATE',branch='DATA_INPUT_OBJECT')
ov('E0253','O2','跟进ERP物料与BOM编制未明确本人操作还是流程跟进。',branch='UNRESOLVED')
add('E0253','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',2,'首分句本人制订优化售后备件流程，后分句与外部共同制订另不提升。')
add('E0221','TC_EVALUATION','DUTY_OWN_USE','EXAMPLE',2,'测试方案设计与执行均明确，核心场景列举以等结束。')
ov('E0221','ADD1','建立根因分析机制并组织跨团队定位，未明确本人直接运用根因分析方法。',metric='SEPARATE',branch='COORDINATION_OBJECT')
for e in ['2:1','3:0']:ov('E0203',e,'制定EMC测试计划/流程属于运用EMC方法，非开发EMC方法本身。',metric='DUTY_OWN_USE')
add('E0203','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',5,'本人建立标准化EMC流程。')
add('E0203','SK_PCB','GENERAL','UNCONDITIONAL',9,'明确具备读懂PCB能力，无工具品牌推断。')
register(list(R.values()),'Astra_v3_boundary_mfg_l')
