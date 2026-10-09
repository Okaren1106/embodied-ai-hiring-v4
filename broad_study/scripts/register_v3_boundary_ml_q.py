from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0492':'Helix强化学习职责与一般要求分别定位；基础设施including保留示例，离线学习优先要求不引用职责。',
'E0489':'模型本职、研究协作、优先经历分开；同类子类型不造成上层类别任选。',
'E0494':'训练性能工程；区分使用编译器写kernel和开发编译器，Profiler提及与框架要求分开。',
'N0709':'全部资格属于Preferred；无示例词的并列不自动示例化，框架at least one/such as同时保留。',
'N0662':'视觉感知模型与机器人策略任务有别；括号仿真工具无示例词，继承外围任选。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('E0492','O5','including仿真基础设施为示例。',branch='EXAMPLE')
for e,n,b in [('O9',16,'UNCONDITIONAL'),('O11',18,'CHOICE'),('O18',27,'CHOICE')]:ov('E0492',e,'改为同一要求强度的真正任职证据，原锚点是职责。',metric='PREFERRED' if e=='O18' else 'GENERAL',branch=b,quote=ln('E0492',n))
add('E0492','TC_RELIABILITY','GENERAL','UNCONDITIONAL',22,'一般要求明确构建可靠系统的能力。')
for e in ['O11','O12']:ov('E0489',e,'多模态模型及VLM/VLA同类内部子型任选不使上层类别变成任选。',branch='UNCONDITIONAL')
ov('E0489','O14','real-world ML systems与embodied AI、robotics明确or。',branch='CHOICE')
ov('E0494','O1','Triton/CUDA不同类别斜线未解。',branch='UNRESOLVED')
ov('E0494','O3','CUDA任职要求应引用F21，原F6是职责。',metric='GENERAL',quote=ln('E0494',21))
ov('E0494','O5','原句要求Profiler工具，不是通用PyTorch模型框架能力；技术出现层保留。',metric='SEPARATE',branch='PROFILER_NOT_FRAMEWORK')
ov('E0494','O10','与研究者共同设计模型，保留协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0494','2:0','用编译器写kernel非开发编译器；F11另有明确编译器开发。',metric='DUTY_OWN_USE')
ov('E0494','6:0','括号无示例词但有or similar。',branch='CHOICE')
add('E0494','SK_PYTORCH','PREFERRED','EXAMPLE',26,'开源ML项目贡献的etc示例中明确PyTorch。')
for e in ['O1','O2','O3','O14']:ov('N0709',e,'括号并列无示例词或任选词。',branch='UNCONDITIONAL')
for e in ['O6','O7','O8']:ov('N0709',e,'at least one与such as共同修饰具体框架。',branch='CHOICE_AND_EXAMPLE')
ov('N0709','4:0','Preferred Qualifications内明确C，与其他语言并列。',metric='PREFERRED',branch='UNCONDITIONAL')
for e in ['O7','O8','O24','O25','O26','2:0']:ov('N0662',e,'仿真环境与robotics或real-time任选，括号无示例词。',branch='CHOICE')
register(list(R.values()),'Astra_v3_boundary_ml_q')
