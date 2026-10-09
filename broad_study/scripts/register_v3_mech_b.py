from astra_review_tools import *
JUD={
'N0093':'机械岗位职责仅新产品预研/测试/产品分支，没有具体结构交付对象；任务保持未知，不从学历或主职能反推本体结构。模型团队为协作，AI能力优先仍保留。',
'N0074':'本体结构主责、关节方案选型和需求输出，选型不等于研发执行器本体；模型与分析软件无品牌不补。',
'N0013':'机械实习广告含预研测试及机器人维修组装，无法确定主交付是结构设计；任务未知。有限元方法优先明确，补上位仿真。',
'N0075':'关节设计主责，参与力学仿真及热目标按协作；与控制团队接口调试不能抬成本人控制算法工作。',
'N0594':'结构专家全生命周期，至少60%知识是子项任选，上位机械能力另有明确句。供应商跑线意愿不是采购优先技能。',
'N0259':'灵巧手结构与设计制造约束、仿真明确；Ansys/Abaqus处于一般要求。外观结构兼顾工业设计不清楚是否本人CMF设计，按未知不直接正例。',
'E0291':'结构与装配测试工装设计独立明确，原只收样机测试漏工装开发，补完整职责。',
'E0278':'关节模组机械与热设计，力学评估只是方法应用；供应与驱动集成为协同，不升独立电力电子职责。',
'E0277':'齿轮设计、仿真及失效模型独立交付；仿真是应用，失效模型研发为明确可靠性开发，重锚该原句。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for r in ['N0093','N0013']:R[r]['task_override']=dict(task='UNRESOLVED',quote='新产品预研',reason='实际职责仅泛称新产品和分支研发，无法确定主体是机器人结构；不由学历和冻结主职能补任务。')
ov('N0074','N0074:O2','关节模组结构方案选型并输出需求是使用选型，不明确开发执行器本体。',metric='DUTY_OWN_USE')
add('N0013','TC_SIMULATION','PREFERRED','UNCONDITIONAL','对有限元计算分析软件熟悉的尤佳','有限元方法上位仿真经验明确优先。')
for e in ['O1','O5','O6','O8']:ov('N0075',f'N0075:{e}','原文参与仿真或与控制团队协作，不能将具体方法和目标全部升独立承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['N0594:O1','N0594:O4','N0594:O5','N0594:O9','N0594:4:0','N0594:5:0']:ov('N0594',e,'具体目标/工艺位于括号或等的开放列举，按例示。',branch='EXAMPLE')
for e in ['N0594:8:0','N0594:8:1']:ov('N0594',e,'至少60%任选知识项中的ANSYS/Abaqus等软件例示，双属性保留。',branch='CHOICE_AND_EXAMPLE')
ov('N0594','N0594:11:0','愿意跑产线供应商是工作意愿，不是采购方法或采购职责，且不在优先技能段。',metric='SEPARATE',branch='WORKING_CONDITION_WILLINGNESS')
add('N0594','TC_MECHANICAL','GENERAL','UNCONDITIONAL','该岗位既要求具备深度机械/结构设计能力','概述独立明确上位机械能力，不因下文子项60%而将整个类设为可选。')
ov('N0259','N0259:1:0','机械外观结构与CMF工业外观设计的承担边界未明，不能由兼顾ID需求直接判使用正例。',metric='UNKNOWN',branch='UNCONDITIONAL',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP'])
ov('N0259','N0259:2:0','线束装配维护方案应用DFM/DFA/DFS设计约束，未开发这些方法本身。',metric='DUTY_OWN_USE')
for e in ['N0259:5:0','N0259:5:1']:ov('N0259',e,'一般任职要求中的等CAE工具，无优先也无or。',metric='GENERAL',branch='EXAMPLE')
for e in ['O15','O16']:ov('N0259',f'N0259:{e}','钢丝绳与欠驱动机构均属机械类，上位机械优先经验存在可判。',branch='UNCONDITIONAL')
R['N0259']['catalog_gap_notes']=[dict(term='SW',quote='熟练使用Creo，SW等三维设计软件',reason='冻结SolidWorks别名未列SW，本版保留未展开缩写；不私增别名。')]
add('E0291','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','负责机器人产品装配和测试工装的设计','可复用测试工装明确本人开发。')
ov('E0278','E0278:O5','力学评估及刚度分析是评价应用，未开发评估方法或工具。',metric='DUTY_OWN_USE')
ov('E0277','E0277:O4','载荷分布仿真与接触分析是应用方法，未开发仿真器或仿真方法。',metric='DUTY_OWN_USE')
ov('E0277','E0277:O5','可靠性开发直接锚本人建立失效模型及预防性设计，非仅寿命预测。',metric='DUTY_OWN_DEVELOP',quote='失效与可靠性分析，建立齿轮失效模型，设计加速寿命测试方案。主导齿轮系统的设计失效模式分析，制定预防性设计策略')
register(list(R.values()),'Astra_v3_mech_b')
