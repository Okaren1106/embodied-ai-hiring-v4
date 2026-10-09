from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0164':'全身RL与数据清洗平台自研；处理动捕/遥操产生的数据不等于本人操作采集工具。',
'E0161':'操作策略全链路，模型类型职责斜线未知；训练评测设施维护与开发区分，修复任职错引。',
'E0157':'后训练场景交付版本独立核对，修复优先要求错引职责和后训练斜线。',
'E0139':'明确评测体系开发，GitHub代码问题协作与HuggingFace平台关系未明。',
'E0121':'集群运维和故障处置为系统使用，不等于Kubernetes工具开发；NCCL至少一类无示例词。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
for e in ['1:0','ADD1']:ov('E0164',e,'清洗多来源已有数据，未明本人采集或使用动捕/遥操。',metric='SEPARATE',branch='DATA_SOURCE')
ov('E0164','O3','安全保护为等功能机制示例。',branch='EXAMPLE')
for e in ['O6','O7']:ov('E0161',e,'IL/VLA/WAM训练管线内部对象斜线未解。',branch='UNRESOLVED')
for e in ['O8','O9','O10']:ov('E0161',e,'维护既有基础设施、真机验证与保障稳定性是使用，未明新系统研发。',metric='DUTY_OWN_USE')
for e in ['O11','O12']:ov('E0161',e,'改引任职任一方向句，非模型侧职责。',metric='GENERAL',branch='CHOICE',quote=ln('E0161',15))
ov('E0161','O13','改引任职理解manipulation流程，非团队背景。',metric='GENERAL',branch='UNCONDITIONAL',quote=ln('E0161',15))
ov('E0157','O8','完整链路中评测执行，未明专门研发评测方法。',metric='DUTY_OWN_USE')
ov('E0157','O15','优先熟悉具身大模型应引用F19，而非职责。',metric='PREFERRED',branch='UNCONDITIONAL',quote=ln('E0157',19))
ov('E0157','4:0','微调/后训练内部关系未解。',branch='UNRESOLVED')
ov('E0139','1:0','github/huggingface两个平台斜线未解。',branch='UNRESOLVED')
R['E0139']['additions'].append(dict(code='V2_GIT',metric='DUTY_OWN_USE',branch='UNRESOLVED',quote=ln('E0139',5),reason='GitHub代码社区问题协作属于冻结类别，但平台斜线关系未知。'))
for e in ['O3','O9','O10']:ov('E0121',e,'资源池运维和故障处理未明Kubernetes或系统研发。',metric='DUTY_OWN_USE')
ov('E0121','5:0','至少一类明确任选，没有示例词。',branch='CHOICE')
register(list(R.values()),'Astra_v3_boundary_ml_n')
