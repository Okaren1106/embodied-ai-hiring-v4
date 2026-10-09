from astra_review_tools import *
JUD={
'N0998':'客户机电集成顾问，支持具体载荷工作之外有独立Owns delivery机械方案，重锚独立责任。实时适应力不推时延技术。',
'E0525':'手部结构与量产、失效改进主责；CATIA明确偏好，其他CAD允许替代。一般CAD/FEA能力引用应来自要求段，不从职责转写。',
'E0606':'快速机电原型及测试治具本人交付，现场环境与工程调试不直接等运行事件支持；控制/固件集成按跨团队协作。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0998','N0998:O1','原Support句不能单独支持独立责任，但Core Competencies明确Owns delivery，改锚该证据。',metric='DUTY_OWN_DEVELOP',quote='Owns delivery of impactful electrical and mechanical solutions & technical planning.')
ov('E0525','E0525:O4','原引职责，改一般资格中CAD经验。',metric='GENERAL',quote='Expert in 3D CAD (CATIA preferred; NX, SolidWorks, or equivalent accepted)')
ov('E0525','E0525:O5','CATIA preferred直接明确偏好，允许其他软件不取消这个偏好。',branch='UNCONDITIONAL')
for e in ['O8','O15']:ov('E0525',f'E0525:{e}','原错引职责，改一般资格结构分析和FEA知识。',metric='GENERAL',quote='Strong understanding of structural analysis, FEA, and material selection')
ov('E0525','E0525:O10','原验证动作是使用可靠性评价；本人独立结构设计耐久要求在F4，重锚设计目标。',metric='DUTY_OWN_DEVELOP',quote='Design structural parts and assemblies in 3D CAD that meet load, durability, manufacturability, and packaging requirements within a tightly constrained envelope')
for e in ['O17','O18']:ov('E0525',f'E0525:{e}','两个可选对象均为车身/产品本体结构，机械上位能力明确。',branch='UNCONDITIONAL')
ov('E0525','E0525:2:0','in accordance with ASME Y14.5为应用标准，不是开发标准。',metric='DUTY_OWN_USE')
for e in ['O10','O11']:ov('E0606',f'E0606:{e}','Collaborate with电气软件团队集成，按协作对象。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0606','E0606:O12','文档记录本身不是评测执行；另句本人端到端原型validation可支持使用。',metric='DUTY_OWN_USE',quote='Build end-to-end prototype systems: from concept sketches through CAD, fabrication, wiring, sensor integration, and validation.')
ov('E0606','E0606:O14','thermal effects在失效模式括号等的例示中。',branch='EXAMPLE')
ov('E0606','E0606:2:0','原型机电装配troubleshooting是工程调试，没有运行事件处理语境。',metric='SEPARATE',branch='ENGINEERING_DEBUG')
add('E0606','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Design and iterate on fixtures, jigs, test rigs, and custom tooling to enable research workflows.','明确可复用测试治具本人研发。')
register(list(R.values()),'Astra_v3_mech_e')
q='Creo and Windchill experience'; txt=RAW[RID['E0361']]['full_description']; pos=txt.rindex(q)
register([dict(reading_id='E0361',review_mode='FOLLOWUP',judgment='核对完整逐行位置发现同一Creo/Windchill句在一般段和Preferred段各出现一次；旧精简阅读器去掉同字段重复行，导致刚才错误撤优先。恢复第二处优先且给出明确位置。',evidence_overrides=[dict(evidence_id=f'E0361:{e}',metric='PREFERRED',branch='UNCONDITIONAL',quote=q,field='full_description',start=pos,end=pos+len(q),reason='同一句第二次出现位于Preferred Skills and Experience段，必须保留独立语境。') for e in ['O4','O5']])],'Astra_v3_intrafield_duplicate_E0361')
