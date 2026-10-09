from astra_review_tools import *
JUD={
'E0563':'内部基础设施与事故响应计划本人建设；云/IaC/监控平台是括号例示，没有or。Linux/Unix不同系统保留未知。',
'N0918':'机器人任务行为与可靠恢复本人主责，语言明确至少一种；现场问题triage可作为独立排障，help后续诊断另不提升。',
'N0925':'云物流业务应用，不是机器人算法；生产支持与全栈交付明确，Terraform/Gitlab位于Nice to have且没有任选标记。',
'E0599':'遥操界面、实时视频与性能工具明确本人开发；通用语言任选，perf是工具例示，部署名称不直接推出运维岗位。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['E0563:3:0','E0563:3:1','E0563:3:2','E0563:4:0','E0563:4:1','E0563:5:0','E0563:5:1','E0563:6:0']:ov('E0563',e,'具体平台工具及协议在括号举例，没有明确or，不推定任选。',branch='EXAMPLE')
ov('E0563','E0563:1:0','CI/CD是such as任务对象列举中的一种。',branch='EXAMPLE')
ov('E0563','E0563:O5','firewalls是networking fundamentals括号内容，安全知识属例示。',branch='EXAMPLE')
ov('N0925','N0925:11:0','Nice to have独立Terraform项目是优先无条件，未出现任选。',metric='PREFERRED',branch='UNCONDITIONAL')
ov('N0925','N0925:13:0','Gitlab CI处于Nice to have。',metric='PREFERRED')
add('N0925','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Be available for production support','本人生产支持职责明确。')
add('N0925','V2_CI_CD','DUTY_OWN_USE','UNCONDITIONAL','Be able to ship a feature end to end: frontend, backend, CI, infrastructure','本人端到端功能发布含CI，未明确开发CI工具本体。')
ov('E0599','E0599:O14','实时传输优化在Streaming栈括号例示；F51另有无条件实时数据要求。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_sw_e')
