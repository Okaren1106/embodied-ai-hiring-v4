from astra_review_tools import *
JUD={
'N0916':'整机机械与供应链量产交付，Required范围明确；普通原型调试不作运行事件优先。第二来源开发是明确供应职责，区别仅跑供应商。',
'E0361':'本人机电部件设计，热分析为应用；Creo/Windchill只有一般要求，旧记录跨段混进优先。Jira和Confluence职责并列、优先斜线未知。',
'E0433':'灵巧手结构与耐久本人设计，FEA及应力验证是使用评测；操作优先证据错锚职责，重新定位实际preferred经验。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
for e in ['O6','O7']:ov('N0916',f'N0916:{e}','such as与or equivalent兼例示任选。',branch='CHOICE_AND_EXAMPLE')
for e in ['N0916:9:0','N0916:11:0']:ov('N0916',e,'两条都在Required Qualifications。',metric='REQUIRED')
ov('N0916','N0916:12:0','原型测试集成中的troubleshooting没有生产事件或运维语境，而且原段为Required非Preferred；按工程调试另列。',metric='SEPARATE',branch='ENGINEERING_DEBUG')
ov('N0916','N0916:7:0','支持选供应商不是独立证据，但drive supplier development and second-sourcing明确本人推动供应来源开发，重锚此句。',metric='DUTY_OWN_USE',quote='drive supplier development and second-sourcing')
ov('E0361','E0361:O1','FEA位于including机械分析方法例示中。',branch='EXAMPLE')
q='Creo and Windchill experience'; pos=RAW[RID['E0361']]['full_description'].index(q)
for e in ['O2','O3','O4','O5']:ov('E0361',f'E0361:{e}','Creo和Windchill在About you一般段；本次明确定位该段的首次出现，不将Preferred下Jira/Confluence证据与其拼接。',metric='GENERAL',branch='UNCONDITIONAL',quote=q,field='full_description',start=pos,end=pos+len(q))
ov('E0361','E0361:O9','进行分析验证设计为热分析应用，不证明开发热管理机制；including具体分析例示。',metric='DUTY_OWN_USE',branch='EXAMPLE')
ov('E0361','E0361:O15','热分析位于including方法列表。',branch='EXAMPLE')
for e in ['E0361:4:0','E0361:4:1']:ov('E0361',e,'using Jira and Confluence明确并列。',branch='UNCONDITIONAL')
for e in ['E0361:7:0','E0361:7:1']:ov('E0361',e,'Preferred Skills标题且Jira/Confluence斜线未解。',metric='PREFERRED',branch='UNRESOLVED')
ov('E0433','E0433:O11','Own FEA and validation是应用评估，未开发新评测方法工具。',metric='DUTY_OWN_USE')
ov('E0433','E0433:O15','旧引文是技术领导职责，真实优先段另有手或灵巧操作经验。',metric='PREFERRED',quote='Direct experience with robotic hands, dexterous manipulation, or anthropomorphic mechanisms is preferred')
register(list(R.values()),'Astra_v3_mech_d')
