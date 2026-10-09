from astra_review_tools import *
JUD={
'N0930':'机器人后端架构，Python and/or C++職责任选；C++明确preferred不能被允许其他语言抹掉优先属性。中间件是优先任选项里的例示。',
'N0665':'机器人模型安全防护软件，所有资格Preferred；语言e.g.列表有or。明确威胁评估及风险缓解本人工作，模型是防护对象而非机器人策略研发。',
'N0706':'部署基础设施，模型训练平台只是所建后端例示；协作模型集成不证明独立模型开发，本人轮值生产响应明确。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O1','O2']:ov('N0930',f'N0930:{e}','Python and/or C++职责明确任选。',branch='CHOICE')
ov('N0930','N0930:O4','C++ preferred是明确偏好；允许其他语言不使该偏好本身成为有条件。',branch='UNCONDITIONAL')
for e in ['N0930:4:0','N0930:4:1']:ov('N0930',e,'e.g.中间件具体例示，外层one or more任选。',branch='CHOICE_AND_EXAMPLE')
for r,ids in [('N0665',['O1','O2','O3']),('N0706',['O2','O3','O4'])]:
 for e in ids:ov(r,f'{r}:{e}','e.g.列举有or，同时保留任选与例示。',branch='CHOICE_AND_EXAMPLE')
ov('N0706','N0706:O7','model training infrastructure位于e.g.后端服务举例中。',branch='EXAMPLE')
ov('N0706','N0706:O10','与ML等团队协作使模型集成，未独立承担模型使用交付。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0706','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Share an on-call rotation with the engineering team to ensure system reliability and quick issue resolution.','轮值是明确本人承担的响应职责，不因轮班与团队共享而排除。')
register(list(R.values()),'Astra_v3_sw_f')
