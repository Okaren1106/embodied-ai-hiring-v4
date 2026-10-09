from astra_review_tools import *
ids=['N0696','N0697','E0500','E0502','N0892','N0894','N0863','E0580','N0914','N0866']
R={rid:dict(reading_id=rid,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for rid in ids}
R['E0505']=dict(reading_id='E0505',review_mode='FOLLOWUP',judgment='依冻结操作方法定义补查已全文读过的SOP与作业安全，不改变客户现场任务。',evidence_overrides=[],additions=[])
def ov(rid,eid,reason,**fields):R[rid]['evidence_overrides'].append(dict(evidence_id=eid,reason=reason,**fields))
def add(rid,c,m,b,q,reason):R[rid]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=reason))
for rid in ['N0696','N0697']:
 R[rid]['judgment']='全文为遥操示范数据采集，任务正确；公司模型愿景不计本人模型开发，未写具名编程工具不补值。补回操作规程及作业安全。'
 add(rid,'V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Follow established procedures for teleoperation and data collection.','明示执行遥操与采集操作规程。')
 add(rid,'V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Maintain efficiency, safety, and instructional accuracy in robotic operations.','明示机器人操作安全。')
add('N0697','TC_DATA_PIPELINE','DUTY_OWN_USE','UNCONDITIONAL','You will be expected to meet a bar of performance on both the quality and quantity of the data you collect.','数据质量与资产定义，与同文N0696保持一致；不推断数据工程开发。')
for rid in ['E0500','E0502','E0505']:
 if rid!='E0505':
  R[rid]['judgment']='客户现场运行任务有据；一般要求错放优先及任选丢失已修复；遥操安全句保留本人遥操使用未知，补运行工单、SOP和作业安全。'
  for e in EB[RID[rid]]:
   if e['code']=='V2_INCIDENT_SUPPORT':ov(rid,e['evidence_id'],'Requirements中的or是一般要求任选。',metric='GENERAL',branch='CHOICE')
   if e['code']=='V2_TELEOP':ov(rid,e['evidence_id'],'遵守遥操设备安全规程不直接确证本人遥操；仅职责使用未知。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
  add(rid,'V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Track, document, and escalate issues to the appropriate engineering teams using Jira.','运行中的工单记录与升级符合冻结定义。')
 add(rid,'V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Follow proper equipment and robot maintenance procedures, including bring-up and shutdown.','明确遵循设备与机器人维护规程。')
 q=next(e['quote'] for e in EB[RID[rid]] if e['code']=='TC_SAFETY')
 add(rid,'V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',q,'明确本人遵守机器人作业安全规程，不推定已取得证书。')
for rid in ['N0892','N0894']:
 R[rid]['judgment']='全文医院服务任务、运行排障及客户服务语境有据；普通can不是总线；无源外工具推断。补医院服务与作业安全的漏读。'
 q='Monitoring and safely assisting mobile service robots in a hospital environment' if rid=='N0892' else 'you will uphold the highest standards for safe clinical use of robots in real-world hospital environments.'
 add(rid,'V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL',q,'医院环境安全使用与操作职责。')
 q='Communicating with hospital staff and, occasionally, the public regarding robot operation' if rid=='N0892' else 'Prioritizing the customer experience by communicating with them when needed'
 add(rid,'V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL',q,'职责直接服务医院用户，不是内部一般跨团队沟通。')
 q='Formerly employed in the healthcare space: you have an insider understanding of the vernacular, organizational structure, and operational processes of hospitals' if rid=='N0892' else 'Formerly employed or shadowed in the healthcare space: you have an insider understanding of the vernacular, organizational structure, and operational processes of hospitals'
 add(rid,'V2_CUSTOMER_SERVICE','PREFERRED','UNCONDITIONAL',q,'The ideal candidate would be标题下的医院流程经验；不自动硬化成一般要求。')
for rid in ['N0863','N0866']:
 R[rid]['judgment']='客户现场运行与维护有据；Python/SQL斜线继续未知，EtherCAT保留明确or任选；like和e.g.的工具改为示例，ArgoCD/Beckhoff/Elmo保留目录外。补明示规程开发、安全与客户培训。'
 for e in EB[RID[rid]]:
  if e['code'] in ['V2_JIRA','V2_ZENDESK','V2_GRAFANA','V2_KIBANA','V2_FOXGLOVE']:ov(rid,e['evidence_id'],'like/e.g.是示例，没有or；不把并列工具当任选。',branch='EXAMPLE')
  if e['code']=='V2_CALIBRATION':ov(rid,e['evidence_id'],'including下列出服务任务的例子，保留示例。',branch='EXAMPLE')
  if e['code']=='V2_INCIDENT_SUPPORT' and e['quote'].startswith('Build knowledge base'):ov(rid,e['evidence_id'],'交付排障知识库方法，不是该句亲自执行运行排障。',metric='DUTY_OWN_DEVELOP')
 add(rid,'V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Reduce repeat incidents by authoring runbooks, knowledge base articles, and automated diagnostics.','本人编制运行规程。')
 add(rid,'V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Safely operate Mech and materials handling systems.','本人安全操作设备。')
 add(rid,'V2_CUSTOMER_SERVICE','DUTY_OWN_USE','UNCONDITIONAL','Support customer training sessions and act as a trainer for new users.','本人作为培训者服务客户使用流程。')
R['E0580']['judgment']='全文主任务为示范数据采集；不从演示操作推出本人掌握操作算法或闭环控制；遥操与数据质量职责有据。AI/ML斜线保留未知；gaming或simulation的仿真对象不明确，保留优先未知。'
ov('E0580','E0580:O3','提供示范数据的对象，不证明操作算法的本人使用；冻结定义不把亲自操作设备自动归算法。',metric='SEPARATE',branch='DEMONSTRATION_OBJECT')
ov('E0580','E0580:O4','直观控制界面不证明动力学闭环、运动控制方法或控制器技能。',metric='SEPARATE',branch='CONTROL_INTERFACE')
ov('E0580','E0580:O7','Gaming or simulation experience with controllers未明确机器人/物理仿真对象。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['PREFERRED'])
add('E0580','V2_SOP_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Maintain high standards for data quality and consistency across all demonstrations','执行明确示范数据质量标准，非仅性格细心。')
add('E0580','V2_MOCAP','DUTY_OWN_USE','CHOICE','Either lead robot movements with your arms (the robot mirrors your actions) or guide robots using specialized controllers','明示身体动作映射或控制器示范数据采集；保留方法任选，不推断具体传感服。')
R['N0914']['judgment']='履单运行监控和故障恢复成立，软件与OSHA要求有据；RCA参与和协助验证与本人拥有任务分开，补作业安全方法。'
for eid in ['N0914:O4','N0914:O5','N0914:3:0']:ov('N0914',eid,'Participate in RCA and assist in testing属于协作责任；本人独立运行排障另有明确证据。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0914','V2_SAFETY_OPERATION','DUTY_OWN_USE','UNCONDITIONAL','Enforce safety protocols when operating on the grid and the control mezzanine.','本人执行作业安全规程。')
add('N0914','V2_SAFETY_OPERATION','REQUIRED','UNCONDITIONAL','Required to work and walk at elevated heights, using fall protection equipment.','明确Required及高处作业防坠装备，不推定实际持证。')
register(list(R.values()),'Astra_robotops_seeded_fullread')
