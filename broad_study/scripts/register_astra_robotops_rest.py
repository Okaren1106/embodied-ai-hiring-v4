from astra_review_tools import *
ids=['N0698','E0501','E0503','E0506','E0504','E0497','E0498','E0499','E0507','N0887','N0891']
R={rid:dict(reading_id=rid,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for rid in ids}
def ov(rid,eid,reason,**fields):R[rid]['evidence_overrides'].append(dict(evidence_id=eid,reason=reason,**fields))
def add(rid,c,m,b,q,reason):R[rid]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=reason))
R['N0698']['judgment']='新增Pittsburgh介绍与已读Skild文本逐段核对，示范数据采集任务不变；USD薪资排除，补采集规程与安全、数据质量。'
add('N0698','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Follow established procedures for teleoperation and data collection.','明示采集规程执行。')
add('N0698','V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Maintain efficiency, safety, and instructional accuracy in robotic operations.','作业安全本人执行。')
add('N0698','TC_DATA_PIPELINE','DUTY_OWN_USE','UNCONDITIONAL','You will be expected to meet a bar of performance on both the quality and quantity of the data you collect.','与N0696相同数据质量证据，统一保留。')
for rid in ['E0501','E0503','E0506','E0504','E0507']:
 R[rid]['judgment']='全文及重复段落位置已核对；保留实际任务，逐条区分Requirements与Bonus，不机械沿用其他班次的要求强度。修复运行排障分支、作业安全及规程漏读。'
 for e in EB[RID[rid]]:
  if e['code']=='V2_INCIDENT_SUPPORT':ov(rid,e['evidence_id'],'原文or明确任选；E0504/E0507位于Bonus，其余此句位于Requirements。',metric='PREFERRED' if rid in ['E0504','E0507'] else 'GENERAL',branch='CHOICE')
  if e['code']=='V2_TELEOP' and rid!='E0507':ov(rid,e['evidence_id'],'遵守设备安全规程并非本人遥操的充分证据。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
 if rid!='E0507':
  q='Track, document, and escalate issues to engineering teams using Jira' if rid=='E0504' else 'Track, document, and escalate issues to the appropriate engineering teams using Jira.'
  add(rid,'V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',q,'本人运行中的工单记录与升级。')
 else:
  add(rid,'V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',"Proactively identify issues during collection and report feedback daily to Figure's AI team",'正在采集运行过程中识别问题并向工程人员反馈。')
 q='Follow proper equipment and robot maintenance procedures, including bring-up, setup, and shutdown' if rid=='E0504' else 'Follow proper equipment and robot maintenance procedures, including bring-up and shutdown'
 add(rid,'V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',q,'执行明确操作维护规程。')
 q=next(e['quote'] for e in EB[RID[rid]] if e['code']=='TC_SAFETY')
 add(rid,'V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',q,'机器人本人作业安全；不当成持证。')
ov('E0504','E0504:O1','穿戴设备采集高质量数据为执行采集，不据此认定开发数据管线。',metric='DUTY_OWN_USE')
add('E0504','V2_MOCAP','DUTY_OWN_USE','UNCONDITIONAL','Wear sensor equipment to collect high-quality motion data used to train AI models','明示穿戴传感设备采集动作数据，不能因没有motion capture关键词而漏编。')
for rid in ['E0497','E0498','E0499']:
 R[rid]['judgment']='全文为穿戴传感设备生成机器人动作数据，包含SOP、安全与反馈；葡语E0499按原文语义判读，ou为任选。补漏动捕、示教、规程；采集执行与数据管线开发区分。'
 if rid!='E0499':
  q='Wear sensor suits to perform repetitive, precise physical movements (walking, lifting, reaching) that guide the robot and generate training data, for up to 8 hours per shift.' if rid=='E0497' else 'Wear sensor equipment to guide the robot through human-like motions'
  sop='Follow detailed "Ground Truth" movement protocols exactly, with zero deviation, to keep data consistent and high quality.' if rid=='E0497' else 'Follow proper equipment and robot maintenance procedures, including setup and shutdown'
  safe='follow ergonomic guidelines to stay safe during repetitive tasks' if rid=='E0497' else 'Maintain a safe and organized workspace during all operations'
  incident='promptly report any hardware issues to your Inventory Team Lead' if rid=='E0497' else 'Flag any issues or bugs during collection and share daily feedback with the team'
 else:
  q='vestir trajes de sensores e executar movimentos físicos repetitivos e precisos (caminhar, levantar, alcançar) que guiam o robô e geram dados de treinamento, por até 8 horas por turno.'
  sop='seguir à risca, sem desvios, os protocolos detalhados de movimento "Ground Truth" (nosso padrão de referência de como executar cada movimento), para manter os dados consistentes e com alta qualidade.'
  safe='seguir as orientações de ergonomia para se manter em segurança durante tarefas repetitivas'
  incident='reportar imediatamente qualquer problema de hardware ao seu Inventory Team Lead'
 for code in ['V2_MOCAP','V2_TELEOP']:add(rid,code,'DUTY_OWN_USE','UNCONDITIONAL',q,'本人穿戴传感器以动作引导机器人并采集示范数据；不推断具体品牌设备。')
 add(rid,'V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',sop,'完整操作规程句证明本人执行，不只依赖SOP标题。')
 add(rid,'V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',safe,'明确作业安全与人体工学操作。')
 add(rid,'V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL',incident,'当前采集运行中报告硬件或运行故障。')
 for e in EB[RID[rid]]:
  if e['code']=='V2_INCIDENT_SUPPORT' and e['metric']=='PREFERRED':
   if rid=='E0498':ov(rid,e['evidence_id'],'Bonus句有or，应保留任选。',branch='CHOICE')
   else:ov(rid,e['evidence_id'],'仅泛称hardware/software排障经验，无法确定是运行维护或研发调试，保留优先语境对象未知。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['PREFERRED'])
ov('E0498','E0498:O1','明示穿戴设备执行数据采集，不直接推定开发管线。',metric='DUTY_OWN_USE')
ov('E0499','E0499:3:0','葡语ou为明确任选，不是独立动捕要求。',branch='CHOICE')
add('E0497','V2_MOCAP','PREFERRED','CHOICE','Prior robotics or motion-capture exposure','优先段机器人或动捕经验，保留or任选。')
for rid in ['N0887','N0891']:
 R[rid]['judgment']='全文医院运行支持；领班新增排班培训不改变其医院运行任务。Unity为医院名称、can为普通助动词，目录外与否定均不补技术正例。补医院服务与作业安全。'
 add(rid,'V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Monitoring and safely assisting mobile service robots in a hospital environment','医院机器人安全操作。')
 add(rid,'V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','Communicating with hospital staff and, occasionally, the public regarding robot operation','直接面对医院用户提供运行服务。')
 add(rid,'V2_CUSTOMER_SERVICE','PREFERRED','UNCONDITIONAL','Formerly employed in the healthcare space: you have an insider understanding of the vernacular, organizational structure, and operational processes of hospitals','Ideal candidate段的医院流程经验。')
register(list(R.values()),'Astra_robotops_all22_completed')
