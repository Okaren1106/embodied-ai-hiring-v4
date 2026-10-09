from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N1015':'战略寻源和成本模型明确，机器人部件为采购对象；证书可由概念知识替代保留任选。',
'N1017':'加工部门管理仍明确刀路排障、技术标准和RCA本人责任；CAD/CAM、ERP/MES关系未知。',
'N0976':'制造过程与夹治具开发明确；补读You bring/Nice to have边界，工具验证总体无条件，局部能力研究才有必要时条件。',
'N0986':'需求计划和ERP/MRP运行维护明确，安全库存不解释产品安全；SQL/Python plus保留优先未知。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason=why))
ov('N1017','27:1','明确regulated quality systems，上位类别要求不因两个编号变为示例。',branch='UNCONDITIONAL')
ov('N1017','24:0','正规培训或认证语境，保留教育资格信息，不额外推导方法经验。',metric='SEPARATE',branch='TRAINING_CREDENTIAL_OBJECT')
add('N1017','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL',23,'本人制定改进编程标准、模板及文档流程。')
ov('N0976','O11','工具设备验证与合格确认无条件；where necessary仅限制其后能力研究示例。',branch='UNCONDITIONAL')
add('N0976','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL',25,'明确加工、增材和焊接成型等实践，类别有无条件经验要求。')
register(list(R.values()),'Astra_v3_boundary_mfg_q')
