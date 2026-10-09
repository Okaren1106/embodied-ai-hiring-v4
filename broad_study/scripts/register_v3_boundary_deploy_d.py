from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0857':'现场服务：Linux/UNIX职责也未知；读CAD模型不证明具体品牌软件使用；培训排障与本人操作分开，工具列表无or不作任选。',
'N0879':'服务支持主管：逐一回读缩略句；培训标定不等于本人标定；create or contribute存在独立承担歧义；观测工具是例示。',
'N0767':'Irvine现场维修：明确使用标定与Shell；support文档改进非独立开发，Jira是such as加or。',
'N0770':'联邦FDE：Jira/Confluence在Extras加分而非一般；Python/C++/ROS仍一般并列明确，直接故障处理补录。',
'N0811':'高级Autonomy联邦：标题不替代任务原文；现场部署与通用代码能力明确，ROS版本斜杠未解，加分工具语境修正。',
'N0768':'Irvine FDE：与其他模板广告分广告核对，一般代码与加分项目软件不混合。',
'N0805':'Perception标题广告：正文是现场部署，不从标题补感知算法责任；加分工具语境修正。',
'N0794':'Robot Autonomy联邦：合并段落内技术动作逐项核对，云泛称不补具体云品牌；加分工具修正。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
def line(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
ov('N0857','O3','Linux/UNIX关系未明，职责不豁免。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for e in ['O6','O7']:ov('N0857',e,'scripting or troubleshooting，具体括号工具例示。',branch='CHOICE_AND_EXAMPLE')
for e in ['O9','O10']:ov('N0857',e,'阅读品牌CAD模型/图纸不明确本人软件使用能力。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['PREFERRED'])
ov('N0857','5:0','原引小标题，重定位具体诊断动作F16。',metric='DUTY_OWN_USE',quote=line('N0857',16))
ov('N0857','8:0','培训他人故障处理，非本人排障技术动作。',metric='SEPARATE',branch='TRAINING_OBJECT')
ov('N0857','11:0','scripting or troubleshooting为任选。',branch='CHOICE')
for e in ['13:0','13:1','13:2']:ov('N0857',e,'括号列工具示例，无or。',branch='EXAMPLE')
add('N0857','V2_GIT','UNKNOWN','UNRESOLVED',line('N0857',41),'GitHub处于软件排障清单，但版本控制/代码协作用途未明。')
R['N0857']['additions'][-1]['affected_metrics']=['PREFERRED']
for e in ['5:0','5:1']:ov('N0879',e,'培训现场人员，不是本人执行所授技术。',metric='SEPARATE',branch='TRAINING_OBJECT')
ov('N0879','6:0','Create or contribute两种承担并存，无法确定独立开发。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_DEVELOP'])
for e in ['8:0','8:1','11:0','11:1','11:2']:ov('N0879',e,'like/e.g.工具示例。',branch='EXAMPLE')
ov('N0879','16:0','EtherCAT,Beckhoff,or Elmo。',branch='CHOICE')
for e in ['O15','O16','O17']:ov('N0879',e,'列举可靠性建模/FMEA/MTTR和MTBF等服务指标，均属可靠性上位。',branch='UNCONDITIONAL')
ov('N0767','4:0','Support continuous improvement文档，不明确独立建设。',metric='SEPARATE',branch='SUPPORT')
ov('N0767','10:0','tools such as Jira, dashboards,or fleet systems。',branch='CHOICE_AND_EXAMPLE')
for r,n in [('N0770',13),('N0811',15),('N0768',13),('N0805',14),('N0794',9)]:
 for e in ['4:0','4:1']:ov(r,e,'Extras/Set You Apart下工具经验为优先。',metric='PREFERRED')
 add(r,'V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',line(r,n),'本人排障解决技术问题，要求证据不能代替职责证据。')
register(list(R.values()),'Astra_v3_boundary_deploy_d')
