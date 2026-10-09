from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ['N0875','E0449','N1035']}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['N0875']['judgment']='Required、Strongly Preferred与首年成功目标需分别编码；原文多处强度错置。具体工具such as/or为优先任选示例。普通保密品格不构成专业安全方法，辅助HRIS责任无法确认本人承担。'
ov('N0875','N0875:O1','Support HRIS administration且广义HR支持受容量/业务条件限制，无法确定本人使用。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
ov('N0875','N0875:O7','敏感信息保密是一般职业素质，不明确安全工程/信息安全方法。',metric='SEPARATE',branch='GENERAL_CONFIDENTIALITY')
ov('N0875','N0875:5:0','招聘职责小标题不是独立工作动作。',metric='SEPARATE',branch='SECTION_HEADING')
ov('N0875','N0875:8:0','Help improve仅协助改进，保留协作方法对象。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for n in [9,10,12]:ov('N0875',f'N0875:{n}:0','Required小节支配该明确经验条款。',metric='REQUIRED')
ov('N0875','N0875:10:0','Required段中的招聘领域or；招聘对象并非本人领域研发。',metric='REQUIRED',branch='CHOICE')
for eid in ['N0875:13:0','N0875:13:1']:ov('N0875',eid,'Strongly Preferred小节；such as加or为任选示例。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('N0875','N0875:17:0','位于Strongly Preferred小节。',metric='PREFERRED',branch='CHOICE')
ov('N0875','N0875:21:0','Within your first year成功目标指未来本人招聘交付，不是入职一般经验。',metric='DUTY_OWN_USE')
ov('N0875','N0875:22:0','首年成功结果不独立证明既有要求或方法开发承担。',metric='SEPARATE',branch='SUCCESS_OUTCOME')
add('N0875','V2_HR','REQUIRED','UNCONDITIONAL','Practical experience with People Operations and employee lifecycle processes.','Required中独立完整人力经验要求。')
add('N0875','V2_HR','PREFERRED','UNCONDITIONAL','Experience coordinating employment-based immigration.','优先雇佣流程经验。')
R['E0449']['judgment']='寻访、现场面试流程设计与Greenhouse本人使用明确。LinkedIn在including子清单，Lever/Ashby在e.g.清单，不能写作无条件或任选；GitHub寻访不计Git。'
ov('E0449','E0449:O1','including中的命名渠道为示例。',branch='EXAMPLE')
for eid in ['E0449:10:0','E0449:10:1']:ov('E0449',eid,'e.g.列表无or，新旧ATS工具一致采用示例。',branch='EXAMPLE')
ov('E0449','E0449:11:0','technical sourcing or full-cycle recruiting为明确经验路径任选。',branch='CHOICE')
add('E0449','V2_HR','DUTY_OWN_DEVELOP','UNCONDITIONAL','design, coordinate, host, and continuously improve all CA-specific on-site interview loops','本人共同设计并组织面试流程，不只是与招聘团队沟通。')
R['N1035']['judgment']='公司支持HRBP，技术/销售是支持对象。Required中HR专业能力漏编，法律应用与优先薪酬结构经验也应纳入。上位HR认证优先明示，命名证书举例不消除上位资格要求。'
ov('N1035','N1035:4:0','上位HR certification独立明确；such as/or仅说明可能的证书子型，本目录标签为上位HR资格。',branch='UNCONDITIONAL')
add('N1035','V2_HR','REQUIRED','UNCONDITIONAL','8+ years of progressive HR experience, including significant experience as an HR Business Partner supporting business leaders.','Required段的独立上位HR经验；HRBP子型为including说明。')
add('N1035','V2_HR','REQUIRED','EXAMPLE','Strong employee relations expertise, including conducting investigations and resolving complex workplace issues.','具体调查与纠纷处理方法处于including例示范围，上位HR能力另有无条件证据。')
add('N1035','V2_HR','PREFERRED','UNCONDITIONAL','Experience with sales compensation structures, including variable pay programs, commission plans, and incentive design principles in partnership with Finance, Sales, and Compensation teams','明确薪酬专业经验；子方法举例不消除薪酬结构上位经验。')
add('N1035','V2_LEGAL','DUTY_OWN_USE','UNCONDITIONAL','Ensure consistent application of employment laws, company policies, and People Operations practices.','本人作为HR专业角色应用雇佣法律。')
register(list(R.values()),'Astra_corporate_fullread_d')
