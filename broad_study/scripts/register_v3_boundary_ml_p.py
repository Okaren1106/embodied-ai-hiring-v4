from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0725':'FiFM洞察模型与机器人动作模型分开；断行要求重新定位，工具并列无示例词。',
'N0815':'ML平台与IaC；Airflow属于一般要求，框架括号并列和DDP/FSDP内部未知区分。',
'N0848':'分布式ML系统本人开发；所有具体框架继承正确强度及such as/or关系。',
'N0722':'三维点云模型工程，框架职责明确任选；协作集成与本人算法职责分开。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('N0725','O22','原锚点是训练职责，改用任职fine-tuning multimodal models完整句。',metric='GENERAL',quote='\n'.join(RAW[RID['N0725']]['full_description'].splitlines()[80:83]))
for e in ['10:0','10:1','10:2','10:3','10:4','17:0','21:0','29:0']:ov('N0725',e,'实际工具/概念并列原文无示例词；LoRA/QLoRA同一低秩适配类别。',branch='UNCONDITIONAL')
add('N0725','V2_MODEL_COMPRESSION','PREFERRED','UNCONDITIONAL',104,'优先要求明确量化模型部署，INT4/INT8同属量化。')
for e in ['O2','O4','O5','O6','1:0','21:0']:ov('N0815',e,'括号明确并列，无示例或任选词。',branch='UNCONDITIONAL')
ov('N0815','15:0','Airflow在What You Have一般要求，非Extras优先项。',metric='GENERAL',branch='UNCONDITIONAL')
for e in ['21:1','21:2']:ov('N0815',e,'DDP/FSDP具体工具斜线未解。',branch='UNRESOLVED')
ov('N0815','O18','通过监控告警保障可靠性是使用，未明开发可靠性机制。',metric='DUTY_OWN_USE')
add('N0815','V2_TERRAFORM','GENERAL','UNCONDITIONAL',48,'一般要求IaC括号明确Terraform，没有示例或任选词。')
for e in ['1:0','1:1']:ov('N0848',e,'与Ray同句such as和or similar，均为任选加示例。',branch='CHOICE_AND_EXAMPLE')
for e in ['5:0','5:1','5:2']:ov('N0848',e,'Extras优先段including与or同时成立。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
for e in ['O1','O2']:ov('N0722',e,'PyTorch、TensorFlow或equivalent frameworks明确任选。',branch='CHOICE')
for e in ['O6','O7']:ov('N0722',e,'改用真正任职框架经验F15，不引用职责F6。',metric='GENERAL',branch='CHOICE',quote=ln('N0722',15))
for e in ['O21','O22']:ov('N0722',e,'与软件/标注团队协作集成或定义策略，保留协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['16:0','19:0']:ov('N0722',e,'具体NeRF/Open3D-ML既有示例又有或的祖先。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_ml_p')
