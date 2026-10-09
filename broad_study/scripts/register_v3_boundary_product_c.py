from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0024':'科技申报项目：参与研发与一般技术理解分开；项目管理方法明确，工具例示与仿真迁移加分任选校正。',
'E0225':'商业化产品：执行器知识重定位真实任职要求；VLM/VLA同基础模型，但与端到端感知领域任选。',
'E0185':'AI Infra产品：后训练/模型压缩是平台产品对象，不能与已分开的MLOps职责口径矛盾；一般框架知识重定位。',
'E0110':'系统TPM：CI位于软件栈例示，项目工具例示；不同项目证书同资格上位。',
'E0413':'遥操作产品：产品定义不同于本人开发遥操算法；一般遥操经验纠正，加分在人因学历标题前结束。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('E0024','2:0','Python/Linux/Git等为同一工具例示。',branch='EXAMPLE')
ov('E0024','3:0','仿真平台经验或Sim2Real/集成/场景测试，迁移是加分分支。',branch='CHOICE')
add('E0024','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','开展任务分解、指标制定、进度跟踪、经费协调、阶段检查','明确具体项目计划与执行方法。')
add('E0024','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','熟悉项目申报、任务书编制、过程检查、经费管理及验收流程','一般项目流程知识明示。')
ov('E0225','O5','旧误引职责，改一般整机模块理解要求。',metric='GENERAL',quote='具备较强的整机产品理解能力，熟悉 ID 设计、结构设计、硬件选型、传感器、执行器、供应链、生产制造、测试验证等多个模块')
for e in ['O11','O12']:ov('E0225',e,'VLM和VLA同上位，外层其他技术领域or。',branch='CHOICE')
ov('E0185','O2','旧误引产品职责，改任职要求的训练框架知识。',metric='GENERAL',quote='熟悉主流分布式训练框架、推理引擎原理')
ov('E0185','1:0','建设后训练产品工具链不等于本人执行后训练/开发后训练算法，保留产品对象。',metric='SEPARATE',branch='PRODUCT_PLATFORM_OBJECT')
ov('E0185','2:0','统筹量化平台化沉淀是产品推动，不是本人开发模型压缩方法。',metric='SEPARATE',branch='PRODUCT_COORDINATION_OBJECT')
ov('E0110','3:0','如软件栈列表中的CI/CD。',branch='EXAMPLE')
for e in ['4:0','4:1']:ov('E0110',e,'括号项目工具等为例示。',branch='EXAMPLE')
ov('E0110','4:3','PMP与ACP同项目资格上位。',branch='UNCONDITIONAL')
for e in ['1:1','2:0','3:0']:ov('E0413',e,'本人定义产品路线图与界面要求，不等于开发遥操系统代码或操作机器人。',metric='SEPARATE',branch='PRODUCT_DEFINITION')
ov('E0413','7:0','SKILLS AND REQUIREMENTS内，尚未到NICE TO HAVE。',metric='GENERAL')
ov('E0413','8:0','EDUCATION and/or EXPERIENCE新标题结束Nice to Have。',metric='GENERAL')
ov('E0413','9:0','教育/经验段内的一般经验；动捕、手跟踪或触觉设备任选。',metric='GENERAL',branch='CHOICE')
register(list(R.values()),'Astra_v3_boundary_product_c')
