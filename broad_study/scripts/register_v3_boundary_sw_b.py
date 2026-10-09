from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0143':'本体应用参与职责与独立承担分层；Agent与Node.js优先经验属任选。',
'E0363':'遥操架构本人开发；XR/动捕均优先资格，示范学习是数据用途。',
'N0840':'基础设施开发，云平台并列无任选词；监控工具是一般要求。',
'N0311':'前端语言明确，框架为示例，服务器端语言中的Node.js保留候选关系。',
'N0434':'软件负责人主导端侧栈，EtherCAT抽象集成是应用协议。',
'N0431':'整机架构；技术任选专业与其他方面也需理解并存，C/C++未知保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
for e in ['O11','O12','O13','O14','O15']:ov('N0143',e,'原文明确参与模块开发/集成/优化，保留参与承担而不作独立直接职责。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0143','2:1','Node.js与前端工具等开发经验明确或。',branch='CHOICE')
ov('N0143','9:0','Agent经验与大模型/语音等项目经验明确或。',branch='CHOICE')
ov('N0143','10:0','工程化工具列表以等结尾。',branch='EXAMPLE')
add('N0143','V2_AGENT_WORKFLOW','GENERAL','UNCONDITIONAL',32,'一般要求明确通用智能体开发模式。')
ov('E0363','4:0','Bonus段中动捕为such as加or的输入系统。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
for e in ['5:0','5:1']:ov('E0363',e,'具体XR框架为示例，继承rendering或XR框架的外层任选。',branch='CHOICE_AND_EXAMPLE')
ov('E0363','6:0','such as与or other重建方法并存。',branch='CHOICE_AND_EXAMPLE')
ov('E0363','O16','要求示范学习用途的数据管线经验，不是本人模仿学习方法经验。',metric='SEPARATE',branch='DATA_PURPOSE')
ov('N0840','O2','语言类别明确要求，具体语言才是任选示例。',branch='UNCONDITIONAL')
ov('N0840','1:0','基础设施组件such as包括CI/CD。',branch='EXAMPLE')
ov('N0840','2:0','like Ansible or similar含示例和任选。',branch='CHOICE_AND_EXAMPLE')
for e in ['6:0','6:1','6:2']:ov('N0840',e,'云平台括号并列没有任选或示例词。',branch='UNCONDITIONAL')
for e in ['12:0','12:1']:ov('N0840',e,'What You Have为一般要求，尚未进入优先段。',metric='GENERAL')
for e in ['O4','O14']:ov('N0840',e,'具体例子继承robotics systems或infrastructure外层任选。',branch='CHOICE_AND_EXAMPLE')
ov('N0311','12:0','掌握一门服务器端语言，Node.js是含于候选集合的示例。',branch='CHOICE_AND_EXAMPLE')
ov('N0434','O2','包括多项模块的明确举例。',branch='EXAMPLE')
ov('N0434','1:0','EtherCAT抽象集成使用协议，并非开发协议本体，继承包括。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for e in ['O3','O4','O5','O6']:ov('N0431',e,'至少一方面专业但其他方面也要求理解；不比较熟练度的GENERAL层皆有要求。',branch='UNCONDITIONAL')
ov('N0431','4:0','流程列表以等结尾。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_sw_b')
