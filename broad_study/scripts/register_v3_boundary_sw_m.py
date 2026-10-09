from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0387':'平台软件；支持移植与直接测试分开，明确持续集成参与不能漏掉。',
'E0423':'实时控制软件，策略网络集成斜线未解；测试文档不等于开发测试框架。',
'E0424':'与E0423可见主体相同，仍保留独立广告身份；采用相同语境裁决。',
'N1019':'全栈some or all要求，AWS/GCP内部未解，Node.js不补JavaScript。',
'N1025':'遥操接口开发与协作集成分开；学习方法为采集数据用途。',
'N1031':'Atlassian业务系统出现三条制造职责，视作来源内不一致，相关能力保留未知而不直接确认。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('E0387','O7','Support移植优化保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['4:0','4:1']:ov('E0387',e,'协议e.g.且继承drivers/protocols/or sensor外层任选。',branch='CHOICE_AND_EXAMPLE')
add('E0387','V2_CI_CD','SEPARATE','COLLABORATION_OBJECT',20,'原文明确contributing to continuous integration，不以代码评审否认这一独立分句。')
for r in ['E0423','E0424']:
 ov(r,'O2','C++资格改锚F18，原为职责。',metric='GENERAL',quote=ln(r,18))
 for e in ['O13','O14']:ov(r,e,'RL locomotion/motion imitation裸斜线未解。',branch='UNRESOLVED')
 ov(r,'O15','开发的是对接仿真与硬件的API，未明开发仿真器。',metric='SEPARATE',branch='INTEGRATION_TARGET')
 for e in ['O16','2:0']:ov(r,e,'维护设计文档含测试覆盖，并不直接证明本人执行/开发HIL测试。',metric='SEPARATE',branch='DOCUMENTATION_OBJECT')
ov('N1019','2:1','原文只有TypeScript、Node.js、React、Three.js，没有JavaScript独立原词。',metric='SEPARATE',branch='INFERRED_LANGUAGE')
for e in ['2:4','2:5']:ov('N1019',e,'AWS/GCP内部裸斜线未解。',branch='UNRESOLVED')
ov('N1025','O6','低延迟高带宽不自动为明确实时系统。',metric='SEPARATE',branch='LATENCY_NOT_EXPLICIT_REALTIME')
for e in ['O10','9:0']:ov('N1025',e,'Support integration保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O16','O17','O18']:ov('N1025',e,'任职要求的是数据采集能力，学习控制/基础模型是数据用途。',metric='SEPARATE',branch='DATA_PURPOSE')
ov('N1025','1:0','岗位名称非完整职责证据，改锚本人设计实现遥操系统F3。',metric='DUTY_OWN_DEVELOP',quote=ln('N1025',3))
ov('N1025','3:1','遥操接口使用动捕设备采集演示，未明开发动捕系统；e.g.与or兼具。',metric='DUTY_OWN_USE',branch='CHOICE_AND_EXAMPLE')
for e in ['O4','O5','9:0']:ov('N1031',e,'制造验证/精益职责与Atlassian主要职责及资格不一致，无法确认来源适用；不把疑似模板误作确定正例。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for e in ['2:0','2:1','3:0','7:0']:ov('N1031',e,'配置、集成及定制企业应用属于使用Atlassian工具，未明开发Jira/Confluence本体。',metric='DUTY_OWN_USE')
for e in ['25:0','25:1','30:0']:ov('N1031',e,'Nice to have优先段，Agile框架括号并列没有任选词。',metric='PREFERRED',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_sw_m')
