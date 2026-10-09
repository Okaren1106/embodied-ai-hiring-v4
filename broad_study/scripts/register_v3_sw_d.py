from astra_review_tools import *
JUD={
'N1036':'混合云基础设施独立交付，云/IaC平台是运用而非开发厂商工具；Required下新增项需一致。候选误拒的HIL原文明确，补优先例示任选。',
'N0860':'PLM文档和变更流程，保持冻结主职能；Support配置ERP集成不当本人开发，修改流程不等于开发PLM软件。',
'N0837':'开发工具与构建基础设施，What Sets You Apart支配Bazel与CI，不是一般。上位编程语言确定，Python可替换。',
'N0732':'Web平台发布和生产排障独立主责，具体web栈是一般例示而非优先；服务对象Node/React不等于本人写应用。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N1036','N1036:O7','与产品安全工程师协作实施安全方案，按协作对象保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['N1036:1:0','N1036:2:0']:ov('N1036',e,'在GCP设计和运行基础设施不是开发GCP平台本体。',metric='DUTY_OWN_USE')
for e in ['N1036:5:0','N1036:5:1']:ov('N1036',e,'使用IaC工具执行标准；括号列举没有or。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for e in ['N1036:14:0','N1036:14:1','N1036:17:0','N1036:17:1','N1036:21:0','N1036:22:0','N1036:22:1','N1036:24:0','N1036:27:0']:ov('N1036',e,'Required标题涵盖所有这些经验工具条目。',metric='REQUIRED')
for e in ['N1036:17:0','N1036:17:1']:ov('N1036',e,'括号IaC工具列表无or，仅例示。',metric='REQUIRED',branch='EXAMPLE')
ov('N1036','N1036:22:0','CI/CD系统上位要求明确，e.g.仅修饰具体工具。',metric='REQUIRED',branch='UNCONDITIONAL')
add('N1036','V2_HIL','PREFERRED','CHOICE_AND_EXAMPLE','such as high-throughput telemetry ingestion, large-scale simulation pipelines, or managing hardware-in-the-loop (HIL) testing environments.','整句实际明确HIL，候选仅看前段遥测的拒绝不成立。')
add('N1036','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','lead post-mortem reviews, and drive systemic improvements that reduce recurrence across on-prem and cloud systems.','事故复盘本人主导，虽前面oncall参与，但此动作明确独立。')
for e in ['N0860:O2','N0860:6:0']:ov('N0860',e,'Support when identified的配置集成按协作承担，不作本人独立开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0860','N0860:5:0','更新发布和变更管理流程不等于开发PLM软件平台。',metric='DUTY_OWN_USE')
ov('N0837','N0837:O2','programming or scripting均属上位语言能力，必有语言技能。',branch='UNCONDITIONAL')
ov('N0837','N0837:1:0','What Sets You Apart是优先；such as Bazel or Nx兼任选例示。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
ov('N0837','N0837:4:0','优先CI/CD上位经验明确，e.g.只作用GitHub Actions。',metric='PREFERRED',branch='UNCONDITIONAL')
ov('N0837','N0837:4:1','该项位于What Sets You Apart。',metric='PREFERRED')
for e in ['O1','O2','O3','O4']:ov('N0732',f'N0732:{e}','containerized infrastructure/environments后的括号具体平台按例示。',branch='EXAMPLE')
for e in ['N0732:1:1','N0732:1:2']:ov('N0732',e,'Node/React描述CI/CD服务的应用对象，未明确本人用它们开发应用。',metric='SEPARATE',branch='SOFTWARE_OBJECT')
ov('N0732','N0732:8:0','上位CI/CD经验直接要求，不是e.g.具体软件例示。',branch='UNCONDITIONAL')
ov('N0732','N0732:8:1','GitHub Actions or similar明确可替代且e.g.例示。',branch='CHOICE_AND_EXAMPLE')
for e in ['N0732:10:0','N0732:10:1','N0732:10:2']:ov('N0732',e,'Familiarity with web stacks在What You Bring一般段，括号列举具体工具。',metric='GENERAL',branch='EXAMPLE')
add('N0732','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Debug and resolve production issues across application, infrastructure, and deployment layers','明确生产故障排查。')
add('N0732','V2_INCIDENT_SUPPORT','GENERAL','UNCONDITIONAL','Experience managing production systems and debugging real-world issues','明确生产系统实际排障经验。')
register(list(R.values()),'Astra_v3_sw_d')
