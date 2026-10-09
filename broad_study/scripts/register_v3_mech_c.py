from astra_review_tools import *
JUD={
'N0670':'机电原型、治具和增材制造本人交付；SolidWorks或其他CAD属工具选择，CAD上位类明确。全部资格Preferred。',
'N0937':'机械设计及量产现场改进，OnShape仅资格preferably而非本人职责工具；注塑额外加分需独立保存，不由加工大类一般经验覆盖。',
'N0955':'FAR结构机电主责，协作仿真管线分开；热主责可由开头own architecture明确支持。Ansys/FEA不同层级斜线未解，普通工程调试不算现场事件支持。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0670','N0670:O2','SolidWorks or other CAD软件明确任选。',branch='CHOICE')
ov('N0670','N0670:O4','SolidWorks和其他CAD均为CAD，上位能力明确。',branch='UNCONDITIONAL')
ov('N0670','N0670:3:0','3D printing经验处于Preferred Qualifications。',metric='PREFERRED')
ov('N0937','N0937:O2','所有允许替代均是CAD，上位类要求明确。',branch='UNCONDITIONAL')
for e in ['O3','O4']:ov('N0937',f'N0937:{e}','other CAD tools like SolidWorks or Creo同时任选和例示。',branch='CHOICE_AND_EXAMPLE')
ov('N0937','N0937:1:0','preferably in OnShape位于经验要求，不能作为本人职责使用；直接优先标记明确。',metric='PREFERRED',branch='UNCONDITIONAL')
add('N0937','V2_CNC_PROCESS','PREFERRED','UNCONDITIONAL','injection molding experience is a plus','注塑经验额外优先；目录代码涵盖成型，不能把该项命名为CNC专门偏好。')
for e in ['N0955:O2','N0955:2:0']:ov('N0955',e,'e.g.且or equivalent，具体CAD工具兼例示与任选。',branch='CHOICE_AND_EXAMPLE')
ov('N0955','N0955:O6','Partner with AI research team建立管线，属于协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0955','N0955:O7','贡献热策略不能单独支持独立责任；开头明确own机械架构含thermal management可支持，重新定位。',metric='DUTY_OWN_DEVELOP',quote='You will own the mechanical architecture of our robotics platform end-to-end: actuator selection, joint design, thermal management, cable routing, sensing integration, and structural optimization')
ov('N0955','N0955:5:0','任职一般段FEA/Ansys不同层级的斜线未解，不虚构优先。',metric='GENERAL',branch='UNRESOLVED')
ov('N0955','N0955:O27','FEA与工程Ansys都为仿真分析范畴，其内部关系不影响上位方法作为e.g.例示出现。',metric='GENERAL',branch='EXAMPLE')
ov('N0955','N0955:4:0','原型搭建集成中的机械调试不等同生产运行事故响应或现场运维。',metric='SEPARATE',branch='ENGINEERING_DEBUG')
ov('N0955','N0955:O23','thermal是environmental factors括号例示。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_mech_c')
