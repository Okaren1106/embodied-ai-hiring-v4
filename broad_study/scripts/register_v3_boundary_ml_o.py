from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0341':'Required标题作用全部资历工具；团队期望不是一般要求，构建平台中的辅助承担单列。',
'N1014':'Required工具与括号并列明确，ONNX在runtime语境存在格式/运行时别名歧义；压缩与后训练不能漏。',
'N0878':'生产ML工程，条件C++、可选感知开发与必备云平台工具分开；补正确Triton服务端。',
'N0798':'足式RL与仿真任务明确，全文相同的三条要求已展开核对；ONNX Runtime不当格式双计，已有动作数据不当采集工具使用。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why,**x):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why,**x))
for e in ['O6','O7','O8']:ov('E0341',e,'help architect/build的平台层工作，保留辅助承担；不把平台使用者的仿真评测推成本人。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0341','O12','用直接Develop reliable workflows句替代讨论架构句。',metric='DUTY_OWN_DEVELOP',quote=ln('E0341',12))
ov('E0341','O13','Required Qualifications下ML infra、data或MLOps经历。',metric='REQUIRED',branch='CHOICE')
ov('E0341','2:0','What we are aiming for是目标状态，不是候选人的一般要求。',metric='SEPARATE',branch='TEAM_TARGET')
for e in ['3:0','4:0','4:1','4:2','4:3']:ov('E0341',e,'Required Qualifications标题统领该工具要求。',metric='REQUIRED')
for e in ['O1','O2','O17']:ov('N1014',e,'括号并列无示例词，RL上位工具箱能力明确。',branch='UNCONDITIONAL')
ov('N1014','1:0','域随机化属于including栈内容，未明开发随机化方法。',metric='DUTY_OWN_USE',branch='EXAMPLE')
ov('N1014','9:0','ONNX被称推理runtime，无法判清格式知识或ONNX Runtime；不直接归格式。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['REQUIRED'])
ov('N1014','9:1','Required段括号并列，无任选或示例词。',metric='REQUIRED',branch='UNCONDITIONAL')
for e in ['13:0','13:1']:ov('N1014',e,'Required标题统领。',metric='REQUIRED')
add('N1014','V2_ONNX_RUNTIME','UNKNOWN','UNRESOLVED',16,'ONNX runtime语境但未写全名，格式/运行时别名不清。',affected_metrics=['REQUIRED'])
add('N1014','V2_TRITON_SERVER','UNKNOWN','UNRESOLVED',16,'仅Triton、runtime而未写Inference Server/NVIDIA serving，保留别名未知。',affected_metrics=['REQUIRED'])
add('N1014','V2_MODEL_COMPRESSION','DUTY_OWN_USE','UNCONDITIONAL',8,'明确distill large policies。')
add('N1014','V2_POSTTRAINING','DUTY_OWN_DEVELOP','UNCONDITIONAL',8,'整合RL与VLA作fine-tune明确后训练职责。')
ov('N0878','O3','where required为条件执行，不能计无条件C++。',branch='CONDITIONAL')
ov('N0878','O12','perception在including but not limited to列表。',branch='EXAMPLE')
ov('N0878','O16','Collaborate closely to integrate实时系统为协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O19','O20']:ov('N0878',e,'may work明确条件任务。',branch='CONDITIONAL')
ov('N0878','3:0','work closely with各团队改善world model，仅协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['5:0','5:1','5:2']:ov('N0878',e,'Required标题，云平台括号无或/示例词。',metric='REQUIRED',branch='UNCONDITIONAL')
for e in ['9:0','9:1']:ov('N0878',e,'Required Skills标题统领Git/CI/CD。',metric='REQUIRED')
add('N0878','V2_TRITON_SERVER','PREFERRED','CHOICE_AND_EXAMPLE',45,'NVIDIA Triton serving stack明确服务端，like和or并存。')
for e in ['O9','O10','O11']:ov('N0798',e,'原文框架括号无示例词或任选词。',branch='UNCONDITIONAL')
for e in ['6:0','6:1']:ov('N0798',e,'部署工具括号无示例词。',branch='UNCONDITIONAL')
ov('N0798','6:2','原词是ONNX Runtime，不能增加ONNX格式能力。',metric='SEPARATE',branch='RUNTIME_NOT_FORMAT')
for e in ['11:0','11:1']:ov('N0798',e,'从动捕或遥操数据构建模仿pipeline，不证明本人采集或使用设备系统。',metric='SEPARATE',branch='DATA_SOURCE')
ov('N0798','O54','维护simulation infrastructure而非开发新的仿真系统。',metric='DUTY_OWN_USE')
add('N0798','V2_MODEL_COMPRESSION','DUTY_OWN_USE','UNCONDITIONAL',13,'明确把策略蒸馏成紧凑策略。')
register(list(R.values()),'Astra_v3_boundary_ml_o')
