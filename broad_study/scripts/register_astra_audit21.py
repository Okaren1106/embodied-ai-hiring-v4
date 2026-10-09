from astra_review_tools import *
AUDIT=ROOT.parent/'acceptance_astra_20260916'
audit=json.loads((AUDIT/'SEMANTIC_REVIEW_Astra.json').read_text(encoding='utf-8'))
records={x['reading_id']:dict(reading_id=x['reading_id'],review_mode='FULL_SOURCE_AND_CODING',
    judgment=x['supported_judgments']+'；边界与修订见本记录及Astra语义抽查台账。',
    evidence_overrides=[],additions=[]) for x in audit['reviews']}

def change(rid,eid,reason,**fields):
    records[rid]['evidence_overrides'].append(dict(evidence_id=eid,reason=reason,**fields))
def add(rid,code,metric,branch,quote,reason):
    records[rid]['additions'].append(dict(code=code,metric=metric,branch=branch,quote=quote,reason=reason))
def task(rid,code,quote,reason):
    records[rid]['task_override']=dict(task=code,quote=quote,reason=reason)

for eid in ['N0799:2:0','N0799:2:1']:
    change('N0799',eid,'such as及or同时支配具体控制方法。',branch='CHOICE_AND_EXAMPLE')
for eid in ['N0799:5:0','N0799:6:0','N0799:6:2','N0799:9:0']:
    change('N0799',eid,'Extras That Set You Apart优先段，不能记一般要求。',metric='PREFERRED')
change('N0799','N0799:6:1','原文命名ONNX Runtime，不以子串补ONNX格式能力。',metric='SEPARATE',branch='DIFFERENT_NAMED_TOOL')
change('N0547','N0547:5:0','AI Agent或企业知识库等存在明确任选；此处为安全治理经验，不能当本人开发Agent。',branch='CHOICE')
change('N0547','N0547:8:0','相关认证列举以等收尾，无明确任选，保存例示关系；不推断实际持证。',branch='EXAMPLE')
for eid in ['N0037:1:0','N0037:2:1']:
    change('N0037',eid,'开发、协议与整机联调调试，不符合运行排障窄定义。',metric='SEPARATE',branch='DEVELOPMENT_DEBUGGING')
task('E0598','CUSTOMER_INTEGRATION','Deploy and debug learned policies on physical robots, diagnosing failures across the full stack (perception, policy, control, hardware).','全文客户流程、伙伴场景与真实机器人部署；改出内部实验/演示服务，保留研究型部署细任务。')
add('E0598','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Deploy and debug learned policies on physical robots, diagnosing failures across the full stack (perception, policy, control, hardware).','结合全文现场可靠性与真实部署，明示本人实际机器人全栈故障诊断。')
change('E0402','E0402:O7','Perform or support使本人执行与协作责任未解决，且thermal为including下的例子。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP'])
change('E0402','E0402:O8','Plan and execute testing为测试计划及执行，不直接证明开发可复用评测工具方法。',metric='DUTY_OWN_USE')
change('N0949','N0949:O7','such as列举，没有明确任选祖先。',branch='EXAMPLE')
change('N0949','N0949:10:0','括号etc为示例，没有or。',branch='EXAMPLE')
change('N0949','N0949:O11','按冻结TC_SAFETY的系统安全目标定义；本人建立系统安全标准，不限于功能安全完整性。',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL')
change('N0560','N0560:5:0','等局部地图框架是明确示例。',branch='EXAMPLE')
change('N0560','N0560:10:0','TensorRT、CUDA或端侧模型部署经验，保留任选。',branch='CHOICE')
change('N0245','N0245:5:0','Jira/禅道的斜线关系未解决，不能直接任选；保留未知。',branch='UNRESOLVED')
change('N0245','N0245:5:1','Microsoft Project等研发管理工具，明确示例。',branch='EXAMPLE')
add('N0245','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','制定项目计划、预算及关键里程碑','本人项目计划和风险管理符合冻结专业方法定义，不能因无别名关键词而漏编。')
add('N0245','V2_PROJECT_METHOD','GENERAL','UNCONDITIONAL','精通硬件/软件协同开发流程及项目管理方法论','要求明示项目管理方法，属专业方法项。')
add('N0944','V2_SIM2REAL','DUTY_OWN_DEVELOP','EXAMPLE',"You'll drive independent research initiatives in areas such as perception, manipulation, science understanding, locomotion, manipulation, sim2real transfer",'本人drive independent research initiatives的such as列举；不是公司宣传，原拒收理由与原文矛盾。')
change('N0944','N0944:O12','研究方向中的sim2real/real2sim是示例对象，开发/使用的责任未明，不强推本人无条件使用。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP'])
change('N0944','N0944:O13','efficient model inference位于for example列举。',branch='EXAMPLE')
change('N1042','N1042:9:0','该句位于Preferred；Typescript独立并列，and/or局部连接Python和C++。',metric='PREFERRED',branch='UNCONDITIONAL')
change('N1042','N1042:5:0','LLM-driven or agentic systems明示任选；另外一条独立Agent性能经验仍支持GENERAL正例。',branch='CHOICE')
change('N1042','N1042:7:0','被举例的是Agent架构内部种类，Agent工作流上位对象本身明确要求；不把子例子关系错误外推到上位类。',branch='UNCONDITIONAL')
task('N1042','ROBOT_RUNTIME','System 2 – the planning and reasoning layer that sits above robotic control','正文为机器人运行中的规划推理层，没有云平台/界面证据；保留细任务AGENTIC_SYSTEMS。')
change('E0505','E0505:4:0','位于Requirements且有or；一般要求任选。',metric='GENERAL',branch='CHOICE')
change('E0505','E0505:3:0','遵守遥操设备安全规程不足以确定本人执行遥操；未知仅限职责使用。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
add('E0505','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','Track, document, and escalate issues to the appropriate engineering teams using Jira.','全文客户运行中工单记录、故障升级，明确符合冻结运行排障项。')
for eid in ['E0407:15:0','E0407:15:1','E0407:15:2']:
    change('E0407',eid,'具体库在类名后括号列举；Ceres/g2o有e.g.，没有or，不推任选。',branch='EXAMPLE')
for eid in ['N0871:28:0','N0871:28:1','N0871:28:2']:
    change('N0871',eid,'语言名在such as列表中，无明确任选。',branch='EXAMPLE')
for e in EB[RID['N0871']]:
    if e['metric']=='GENERAL' and e['branch']=='CHOICE' and 'such as PROFINET' in e['quote']:
        change('N0871',e['evidence_id'],'通信协议在such as示例中；含斜线的局部对象保持未知。',branch='UNRESOLVED' if e['code'] in ['V2_ETHERCAT','V2_FSOE'] else 'EXAMPLE')
    if e['metric'].startswith('DUTY') and 'Collaborate with Hardware, System, and Software teams on safety analyses' in e['quote']:
        change('N0871',e['evidence_id'],'仅此出现明确为与跨职能团队协作开展安全分析，未明确本人独立拥有所列每项方法。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
change('N0619','N0619:ADD1','预训练、指令微调、对齐是普通并列，不凭列举数量降为示例。',branch='UNCONDITIONAL')
for e in EB[RID['N0619']]:
    if e['metric'].startswith('DUTY') and '主导或参与' in e['quote']:
        change('N0619',e['evidence_id'],'主导或参与的本人开发责任未解决，不强推无条件。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP'])
    if e['branch']=='CHOICE_AND_EXAMPLE' and e['code'] in ['SK_ISAAC_SIM','SK_MUJOCO','SK_PYBULLET']:
        change('N0619',e['evidence_id'],'平台斜线未能明确是任选；与同文本语言斜线规则一致保留未知。',branch='UNRESOLVED')
change('N0528','N0528:6:0','Blender等DCC工具为明确示例。',branch='EXAMPLE')
for e in EB[RID['N0528']]:
    if 'Codex 等' in e['quote'] and e['branch']=='CHOICE':
        change('N0528',e['evidence_id'],'Codex等是示例，非明确任选。',branch='EXAMPLE')
records['N0528']['source_limits']=[dict(metrics=['PREFERRED'],codes='ALL_APPLICABLE',reason='三个冻结字段都在加分项末尾“资产自动化工具链开”截断；优先语境的未观察格不能一概记Z。可见正例保留；职责与完整一般要求段仍可判断。')]
# Requirements were wrongly removed as duplicates of a duty occurrence.
for q in QB[RID['N0528']]:
    if q['review_id'].split(':')[-1] in ['14','16','17']:
        records['N0528'].setdefault('candidate_reconsiderations',[]).append(dict(review_id=q['review_id'],quote=q['quote'],reason='不同职责/要求语境不能相互去重；待补充对应命名标签。'))

register(list(records.values()),'Astra_audit21_repairs')
