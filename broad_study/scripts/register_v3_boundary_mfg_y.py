from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0590':'原型装配维修与在役服务分开，括号具体器件没有示例词；本人测试仍属使用。',
'E0604':'机器人BOM供应为采购对象，DFM/DFA同类别不再作为未知；ERP/MRP继续未知。',
'E0586':'机器人构建和实验室维护明确；列出的Notion与Excel没有示例词。',
'N0675':'资历全部Preferred，设计工装和组装本人承担；同类别替代不使整个类别变任选。',
'N0712':'资历Preferred，采购电子和机械对象不推为研发；DFM/DFA同类别。',
'N0671':'资历全部Preferred，电池测试与BMS同属电池；无示例词的接口列表不是示例。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
ov('E0590','O13','括号列举没有示例词，AC/DC均是电机类别。',branch='UNCONDITIONAL')
ov('E0590','O14','仅电气controllers未明运动控制理论/规划控制能力，不从器件名称推能力。',metric='SEPARATE',branch='GENERIC_CONTROLLER_OBJECT')
ov('E0590','O11','被修电气control systems未明机器人运动控制方法，保留对象提及。',metric='SEPARATE',branch='GENERIC_CONTROLLER_OBJECT')
add('E0590','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL',29,'焊接为具体制造加工方法，按冻结上位类纳入。')
ov('E0604','7:1','DFM/DFA同属冻结DFM类别，不影响类别是否出现。',branch='UNCONDITIONAL')
for e in ['O3','5:0']:ov('E0586',e,'括号无示例或任选词，明确两项工具。',branch='UNCONDITIONAL')
add('E0586','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',11,'本人执行test protocols属于程序执行。')
for e in ['O2','2:0']:ov('N0675',e,'只有or similar而无示例词，保留任选。',branch='CHOICE')
for e in ['5:0','6:0']:ov('N0675',e,'替代项均属同一冻结上位类别，类别要求明确。',branch='UNCONDITIONAL')
ov('N0712','6:0','DFM/DFA同类别，类层无未知。',branch='UNCONDITIONAL')
for e in ['7:0','7:1','7:2','7:3','7:4']:ov('N0671',e,'括号接口并列，无示例或任选词。',branch='UNCONDITIONAL')
for e in ['O21','O23']:ov('N0671',e,'电池测试或BMS均为电池概念，上位类无任选。',branch='UNCONDITIONAL')
ov('N0671','O25','不同测试领域均属于测试评价上位类。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_mfg_y')
