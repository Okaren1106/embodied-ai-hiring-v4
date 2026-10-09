from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0689':'应用部署：全部资格在Preferred；软件连接基础模型不直接证明本人模型研发/使用；现场调试是明确排障。',
'N0858':'FDE：回读被缩略的全部职责与要求；贡献脚本不升格独立开发；一般/优先工具标题及具体例示、斜杠未知修正。',
'N0993':'现场维修：职责BASH/Python明确，资格BASH在Desired Skills，不是一般要求。',
'E0453':'维修学徒：常规检查是评测使用非开发；排障经验属于一般任选，软件例示与并列工具分开；SOP执行补录。',
'N0907':'维修技师：帮助库存与独立维修分开；SOP职责误记一般，Google Suite受must且including工具例示；核读重复原文。',
'N0498':'售后维修：协助完善SOP不记独立开发，万用表等例示；明确诊断与排障分别补职责和要求。',
'N0531':'实验室运维：报修厂商对接非采购；标定工具台账非本人标定使用；保留直接标定执行、库存补货与安全流程开发。',
'E0076':'技术支持：ROS2一般要求重定位；协助客户验证与本人节点能力分开；协议为等例示，PMP与项目经验斜杠未知。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0689','O6','开发连接模型与部署的软件，基础模型是接口对象。',metric='SEPARATE',branch='INTEGRATION_OBJECT')
add('N0689','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line('N0689',8),'明确跨层故障调试。')
ov('N0858','O1','SQL/NoSQL关系未明。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for e in ['O2','O16','15:0']:ov('N0858',e,'contribute to工具脚本，非独立承担。',metric='SEPARATE',branch='PARTICIPATION')
ov('N0858','O11','Partner with Product and Engineering。',metric='SEPARATE',branch='COLLABORATION')
for e in ['5:0','5:1','5:2','19:0','19:1','19:2']:ov('N0858',e,'such as/e.g.例示，无or。',branch='EXAMPLE')
for e in ['11:0','11:1']:ov('N0858',e,'工单Jira/Zendesk关系未明。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for e in ['24:0','24:1','24:2']:ov('N0858',e,'Nice-to-Have内云服务斜杠关系未明。',metric='PREFERRED',branch='UNRESOLVED')
for e in ['24:3','24:4']:ov('N0858',e,'Nice-to-Have父标题。',metric='PREFERRED')
for e in ['32:0','32:1']:ov('N0858',e,'括号所列CI工具例示，无or。',branch='EXAMPLE')
add('N0858','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line('N0858',31),'本人定位修复现场事故。')
ov('N0993','8:0','BASH一般能力在Desired Skills。',metric='PREFERRED')
ov('E0453','O1','维护检查是使用评测，非开发测试体系。',metric='DUTY_OWN_USE')
ov('E0453','2:0','Requirements内机器人经验或机械排障。',metric='GENERAL',branch='CHOICE')
ov('E0453','4:0','such as but not limited to工具示例。',branch='EXAMPLE')
for e in ['5:0','5:1']:ov('E0453',e,'并列列工具，没有任选词。',branch='UNCONDITIONAL')
add('E0453','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',line('E0453',10),'明确遵循维护与启停程序。')
ov('N0907','O1','Help to maintain并与管理配送团队合作库存。',metric='SEPARATE',branch='SUPPORT')
ov('N0907','1:0','原文是Responsibilities内阅读SOP，且such as。',metric='DUTY_OWN_USE',branch='EXAMPLE')
ov('N0907','2:0','must使用系统，including but not limited to。',metric='REQUIRED',branch='EXAMPLE')
add('N0907','V2_SOP_OPERATION','GENERAL','EXAMPLE',line('N0907',39),'资格中的操作维护指引及程序手册例示。')
ov('N0498','O2','万用表等工具示例。',branch='EXAMPLE')
ov('N0498','1:0','协助完善标准作业流程。',metric='SEPARATE',branch='SUPPORT')
add('N0498','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line('N0498',3),'直接负责故障诊断维修。')
add('N0498','V2_INCIDENT_SUPPORT','GENERAL','UNCONDITIONAL',line('N0498',19),'明确排查机电故障能力。')
ov('N0531','3:0','售后报修厂商对接，不是采购合同/供应商交易。',metric='SEPARATE',branch='AFTERSALES_CONTACT')
ov('N0531','5:0','管理标定工具资产台账，不证明工具使用；F7直接使用另保留。',metric='SEPARATE',branch='ASSET_MANAGEMENT_OBJECT')
for e in ['O3','O5']:ov('E0076',e,'一般要求应引本人ROS2功能验证能力F11。',metric='GENERAL',quote=line('E0076',11))
ov('E0076','O4','协助新版本测试现场验证。',metric='SEPARATE',branch='SUPPORT')
ov('E0076','O6','等核心零部件例示。',branch='EXAMPLE')
ov('E0076','O7','人形/机械臂技术支持是产品经验，不是操作算法。',metric='SEPARATE',branch='SUPPORTED_PRODUCT')
for e in ['3:0','3:1','3:2','3:3']:ov('E0076',e,'等常见通信协议例示，没有任选词。',branch='EXAMPLE')
ov('E0076','4:0','项目经验/PMP关系未明，不能推PMP任选或必需。',branch='UNRESOLVED')
add('E0076','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line('E0076',2),'独立根因定位和问题闭环。')
register(list(R.values()),'Astra_v3_boundary_deploy_a')
