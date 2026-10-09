from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N1007':'楼宇设施维修：机械维护与安全要求限于设施对象，不解释为机器人技术；校准未在本职能目录适用，不借此补值。',
'N0775':'法务商业合同独立主责与知识要求漏标；政府合同或采购经验在What You Have，不能记优先。',
'N0721':'职场经理工具在Preferred，Google Workspace并列必备于该段，Jira为任选例示；补轻量SOP建设。',
'N0120':'总账会计正文确有会计执行；学历专业与专业能力分开；财务软件如和或同时出现。',
'N0122':'FP&A自动化Python/SQL斜杠不能肯定；全部证书属会计证书上位，财务专业来自能力条款而非学历。',
'N0154':'与总账广告正文一致但身份独立：CPA与中级会计师明确or，CPA资格阶段斜杠不取消CPA存在；补账务执行。',
'N0155':'投资尽调建模与法律规则知识都有明确证据，估值具体方法目录外不补造新项。',
'N0082':'招聘算法人才不等于具备算法研发技术；保留HR实际技能，把招聘活动参与与独立策略区分。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0775','3:0','What You Have段government contracts or federal procurement。',metric='GENERAL',branch='CHOICE')
add('N0775','V2_LEGAL','DUTY_OWN_DEVELOP','UNCONDITIONAL','Build and refine standard contract templates for different customer segments and deployment models','独立形成法律合同模板。')
add('N0775','V2_LEGAL','DUTY_OWN_USE','UNCONDITIONAL','Negotiate liability caps, indemnification provisions, insurance requirements, and limitation of liability clauses','本人合同条款谈判。')
add('N0775','V2_LEGAL','GENERAL','UNCONDITIONAL','Familiarity with international commercial law and cross-border transactions','明示商业法律知识。')
ov('N0721','17:0','Preferred段Google Workspace与Slack并列，非工具例示。',metric='PREFERRED',branch='UNCONDITIONAL')
ov('N0721','17:1','Preferred段such as及or。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
add('N0721','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Build lightweight workplace processes, checklists, vendor documentation, office standards, and recurring routines.','本人建立办公操作规范和检查清单。')
for r in ['N0120','N0154']:
 ov(r,'1:0','财会学历专业不是本人实际会计方法能力；后文另有会计准则要求。',metric='SEPARATE',branch='FIELD_OF_STUDY')
 for e in ['3:0','3:1']:ov(r,e,'如用友或金蝶，例示和任选同时。',branch='CHOICE_AND_EXAMPLE')
 add(r,'V2_ACCOUNTING','DUTY_OWN_USE','UNCONDITIONAL','负责账务核算、编制月度、季度、年度财务报表，确保账务处理准确、及时','本人会计核算执行明确。')
ov('N0154','O1','中级职称或CPA明确任选，CPA内部全科/阶段证书不改变CPA能力上位。',branch='CHOICE')
for e in ['O1','O2']:ov('N0122',e,'VBA/Python/SQL/多维表格关系未解。',branch='UNRESOLVED')
ov('N0122','3:0','学历专业不能代替会计方法能力。',metric='SEPARATE',branch='FIELD_OF_STUDY')
ov('N0122','3:1','列出的CPA/ACCA/CMA均属会计专业证书。',branch='UNCONDITIONAL')
for e in ['O4','O5']:ov('N0082',e,'了解相应岗位招聘，技术为招聘对象，不是本人基础模型研发/知识要求。',metric='SEPARATE',branch='HIRING_OBJECT')
for e in ['4:0','4:1']:ov('N0082',e,'参与策划组织招聘活动。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
register(list(R.values()),'Astra_v3_boundary_corporate_a')
