"""Record Astra's source-read boundary decisions and reproducible revision impact.
Frozen measurements remain untouched; withdrawal of a claim is not a recoding.
"""
from common import *
from datetime import datetime, timezone

PREV=ROOT.parent/'run_20260916_astra_m5_m6_final'
GROK=ROOT.parent/'run_20260916_astra_v2'
ad={a['identity_key']:a for a in read(ROOT/'baseline_v2/Q3_ads_final.csv')}
rids={j['reading_id']:k for k,j in J.items()}
decisions=[
 ('N0401','DIGITAL_MODEL_MAINTENANCE','部署并维护多模态感知算法/模型','明确模型维护；历史仅工程、没有部署维护。与N0312的宽对象处理不一致；不能据零值推出没有维护责任。'),
 ('N0384','RUNTIME_ENGINEERING_BOUNDARY','模型的统一接入与稳定运行','运行时开发与稳定性是交付目标；没有充分证据把它直接改判为持续运维，更不能解释为客户现场。'),
 ('E0248','MODEL_INTEGRATION_RELEASE','负责模型推理工程化集成与部署','历史部署正例实际指模型集成与发布更新；不能证明客户现场交付或持续生产运维。'),
 ('N0312','TRAINING_ENV_MAINTENANCE','负责训练环境的维护、Bug排查及日志分析','明确训练环境运维，历史计部署维护；与N0401对照说明对象范围和适用并不统一。'),
 ('N0867','SECURITY_COMPLIANCE','work with auditors, prospects and customers to demonstrate compliance with security policies.','原质量规则明确含合规，安全审计可纳入；应改写制造质量这一窄解释，无须据此改冻结标签。'),
 ('N0577','ROBOT_PROTOTYPE','负责强化学习算法在机器人物理样机上的部署落地','明确物理样机落地；不是客户现场证据。复合职能广告，保留在全样本活动分析，未强塞Q2单职能。'),
 ('N0611','ROBOT_PROTOTYPE','实现强化学习算法sim2real在机器人物理样机上的落地应用。','明确物理样机；与N0614职责模板相同但资格不同，不合并为同一招聘广告。'),
 ('N0614','ROBOT_PROTOTYPE','实现强化学习算法sim2real在机器人物理样机上的落地应用。','明确物理样机；不能改述为客户现场。'),
]
rows=[]
for rid,obj,quote,judgment in decisions:
 k=rids[rid];loc=locate(k,{'quote':quote});assert loc['method']!='UNRESOLVED_LOCATION',(rid,quote)
 rows.append(dict(reading_id=rid,identity_key=k,company_id=J[k]['company_id'],object_reading=obj,**loc,
  frozen_deployment_owned=k in OWN['ACT_DEPLOYMENT'],frozen_quality_owned=k in OWN['ACT_QUALITY'],
  decision=judgment,review_scope='FULL_SOURCE_ACTIVITY_BOUNDARY_ONLY',reviewer='Astra'))
dump('tables/V3_activity_rule_record_claim.csv',rows)
claims=[
 ('A_DEPLOY_ZERO','智元ML现场部署编码为零说明规则只测现场，因而不是编码错误','WITHDRAW','规则文字未将运行维护对象限定为客户现场，N0401/N0312又存在适用差异。零值解释没有得到证明。'),
 ('A_DEPLOY_OUTSIDE','264/343=76.97%的部署维护写在同名职能外','HISTORICAL_EXPLORATORY_ONLY','数值可复算，但混合数字系统与样机对象且边界适用不一致；撤出正式实质主结论，不改称客户现场比例。'),
 ('A_DEPLOY_DECOMP','银河通用减Figure部署维护差−0.81=+4.39−5.21个百分点','HISTORICAL_EXPLORATORY_ONLY','算术仍成立，活动测量不充分一致；不得作为可靠部署责任差异的主证据。工程活动分解不因此失效。'),
 ('A_QUALITY','质量验证相当于制造质量','REWRITE','原规则明确包含合规；N0867安全合规是有依据的正例。300/459只可解释为含验证、质量放行、合规和缺陷闭环的宽质量活动。'),
 ('A_OBJECT','模型部署、训练环境维护、机器人样机与客户现场应区分','RETAIN','八条回读支持区分对象；没有客户现场证据不得补出客户或产品归属。'),
 ('A_ENGINEERING_DECOMP','工程活动总差+11.10=构成+19.45与职能内−8.35','RETAIN_WITH_SCOPE','固定四共同职能、原工程编码下的描述分解；不作因果解释，不声称控制了其他岗位差异。'),
]
dump('tables/V3_claim_disposition.csv',[dict(claim_id=i,old_claim=o,disposition=d,reason=r) for i,o,d,r in claims])
text='''# 1. 活动规则—原文—旧结论裁决（Astra）

## 裁决
原 v0.7.4 与 v0.7.5 的部署定义都是“实际现场部署、验收、维修或运行维护。”它既没有清楚列举数字对象，也未明确说运行维护只限客户现场。八条原文回读显示：历史正例包括训练环境、模型工程集成和机器人物理样机；N0401的明确模型维护却没有同一活动标签。由此，旧窄解释错误，A01所谓“仅改名称、数据没有问题”的保证也缺乏依据。不能用一个更宽的新名称追认历史测量一致。

本版保留冻结编码及历史数字，撤回依赖部署标签一致性的实质主结论。264/343以及部署活动分解仅在历史测量附录保留，不作为客户现场、运维或交付责任差异的正式证据。没有用八条定向回读估计全体错误率，也没有只补N0401便声称343条全已修复。

若未来需要给出一致口径的部署率，须另立版本并对所有相关正例与潜在漏例按数字模型/训练环境、运行软件、物理样机、客户生产现场及持续维护责任区分后重算。本轮不声称已经做了这项全体新测量；现有主文通过撤回越界结论收口，不重开冻结主分类。

质量定义原文为“验证执行、质量放行、合规及缺陷闭环。”安全合规在定义中，不属于本轮新增范围。相应处理是改写“制造质量”的窄称，并保留宽质量结果及其限制。

## 可核查链条
- `tables/V3_activity_rule_record_claim.csv`：8条全文活动边界回读、精确原文位置及裁决。
- `review/activity_boundary_packet.md`：完整回读包。
- `tables/V3_claim_disposition.csv`：旧结论的保留、改写和撤回。
- `inputs/measurement_rules_v0.7.4.yaml`、`...v0.7.5.yaml`：两个原规则快照。

本记录的8条回读是活动专项，不自动计入Q2全目录二次复核。冻结A/B/C及1654认可参考均未改动。
'''
(ROOT/'reports').mkdir(exist_ok=True)
(ROOT/'reports/V3_01_活动边界裁决.md').write_text(text,encoding='utf-8')

# Step 2 compares like keys rather than mixing the 14-slice and 22-slice totals.
fields=['role','label_code','metric','branch']
def aggregate_rows(p):
 with p.open(encoding='utf-8-sig',newline='') as f:
  return {tuple(r[z] for z in fields):r for r in csv.DictReader(f) if r['scope']=='WHOLE23'}
old=aggregate_rows(GROK/'tables/Q4_aggregates.csv');new=aggregate_rows(PREV/'tables/Q4_aggregates_final.csv')
imp=[]
for key,o in old.items():
 n=new[key]
 if any(o[z]!=n[z] for z in ['P','U','Z','N','B','gate']):
  imp.append(dict(zip(fields,key),label_name=n['label_name'],**{'old_'+z:o.get(z,'') for z in ['P','U','Z','N','B','gate','share_ad_weighted']},
   **{'v2_'+z:n.get(z,'') for z in ['P','U','Z','N','B','SOURCE_EXCLUDED','gate','share_ad_weighted']},
   delta_P=int(n['P'])-int(o['P']),delta_U=int(n['U'])-int(o['U']),
   rate_change_pp=(float(n['share_ad_weighted'])-float(o['share_ad_weighted']))*100 if n['share_ad_weighted'] and o['share_ad_weighted'] else '',
   interpretation='同一冻结文本的测量或计算修订；不是时间变化'))
dump('tables/V3_revision_impact_grok_to_astra_v2.csv',imp)
changes=read(ROOT/'baseline_v2/Q3_astra_changes.csv');groups=defaultdict(list)
for c in changes:
 try:b=json.loads(c['before']);a=json.loads(c['after'])
 except json.JSONDecodeError:groups['TASK_ASSIGNMENT'].append(c);continue
 if not b:groups['EVIDENCE_ADDITION'].append(c)
 else:
  for f in ['code','metric','branch','affected_metrics','excluded_from_catalog']:
   if a.get(f)!=b.get(f):groups[f.upper()].append(c)
  if any(a.get(f)!=b.get(f) for f in ['quote','field','start','end']):groups['QUOTE_LOCATION'].append(c)
dump('tables/V3_revision_change_axes.csv',[dict(axis=g,change_rows=len(cc),unique_ads=len({c['identity_key'] for c in cc}),count_note='按实际字段变化归类；各轴可重叠，不相加为广告数') for g,cc in sorted(groups.items())])
overview=dict(baseline_change_rows=len(changes),baseline_changed_ads=len({c['identity_key'] for c in changes}),comparable_cells=len(old),changed_aggregate_cells=len(imp),
 added_duty_branch_cells=len(set(new)-set(old)),change_axes={g:dict(rows=len(cc),ads=len({c['identity_key'] for c in cc})) for g,cc in groups.items()})
save_json('verification/V3_revision_impact_baseline.json',overview)
(ROOT/'reports/V3_02_修订影响.md').write_text('# 2. 修订对结论的影响（Astra，基线核对）\n\n'+
 f'Grok首轮到上一版Astra的{len(changes)}项修订涉及{overview["baseline_changed_ads"]}条独立广告，不能当作800条错误广告或总体错误率。原14语境中可对齐{len(old):,}格，有{len(imp):,}格的计数、分母或门槛变化；新增职责分支另列，不能把扩表带来的格数当成新增招聘需求。\n\n'+
 '完整同口径变化见`tables/V3_revision_impact_grok_to_astra_v2.csv`，字段修订分布见`tables/V3_revision_change_axes.csv`。旧阶段C只能在词条与语境含义一致时比较，不能直接把不同目录合计相减。\n\n'+
 '已落实的结论修订：控制闭环一般要求52改51；部署现场Python去Field后仍有17家公司、4/65，失去门槛的说法撤回，改为对该公司广告贡献敏感；C++大量C/C++关系未知仍保留；研究科学与机器人操作的组门槛与主图筛选分开；板级电路任务整公司分母应为56，旧文51是生产工艺任务的分母。\n\n'+
 '后续V3复核产生的影响将在本表之后单列，逐项检查公司差异缩小、消失或反转；当前文件不冒充最终V3结果。\n',encoding='utf-8')

# Step 3 materializes task membership explicitly; primary remains the main design.
definitions=json.loads((ROOT/'configs/Q_task_strata_v2.json').read_text(encoding='utf-8'))
taskrows=[]
for r,defs in definitions['roles'].items():
 for d in defs:
  aa=[a for a in ad.values() if a['role']==r and a['company_id'] in WHOLE and a['task']==d['task_code']]
  taskrows.append(dict(role=r,**d,primary_whole23_ads=len(aa),primary_whole23_companies=len({a['company_id'] for a in aa}),
   decision_basis='职责、工作对象及本人交付；工具/技术词条出现本身不决定任务',primary_policy='主分析每条广告一个主任务；次任务只在独立敏感性中使用'))
dump('tables/V3_task_definitions_and_size.csv',taskrows)
members=[dict(identity_key=k,reading_id=a['reading_id'],company_id=a['company_id'],role=a['role'],primary_task=a['task'],secondary_task=a['secondary_task'],
 task_quote=a['task_quote'],task_field=a['task_field'],task_start=a['task_start'],task_end=a['task_end'],scope='WHOLE23' if a['company_id'] in WHOLE else 'FAR') for k,a in ad.items()]
dump('tables/V3_task_membership_baseline.csv',members)
sec=Counter(a['secondary_task'] for a in ad.values() if a['secondary_task'])
save_json('verification/V3_task_method_baseline.json',dict(primary_ads=len(ad),secondary_ads=sum(sec.values()),secondary_values=dict(sec)))
(ROOT/'reports/V3_03_同任务比较方法.md').write_text('''# 3. 同任务比较方法（Astra）

## 任务划分与技术结果分开
任务由岗位职责的主要交付与工作对象划定，保持冻结主职能；Python、Linux、C++或HR流程等技术要求不能单独作为任务纳入条件。任务赋值是研究者的文本判断，不是关键词分类。定义在Q2-v2.1时已冻结；本版展示原定义及逐条职责依据，不按公司工具差异的大小更换比较组。

机器人模型：本人训练或优化机器人策略/具身模型；仅提供训练基础设施不进入主层。机器人运行软件：本人交付中间件、运行时、机器人应用或遥操软件；普通履单后台、内部IT或云端界面不因使用C++就进入。板级电路：本人交付板卡/PCB/电源驱动电路；仅嵌入式固件或线束设计不因出现PCB进入。HR：本人招聘、人力流程与组织服务交付；法务、财税和IT不会因要求沟通协作进入。

主分析每条广告只有一个主任务。secondary_task保留了次任务，基线167条非空；此前代码只使用主任务，故不能宣称多任务已进入主结果。主任务模糊保留UNRESOLVED/OTHER，不从所比较的技术反推填入。受过工具结果影响的回看属于修订与敏感性，不能称盲法验证。

深化分析固定为机器人模型、运行软件、板级电路三个既有任务，主任务基线分别106、87、56条整公司广告。任务仍有细对象、资历、语言与模板差异，只提高可比程度，不等于工作完全相同。对主次任务共同纳入的结果另列并按广告去重，不能与主任务层相加。主任务与原职能相关的高比例用于描述范围；主文重点解释相近任务内的具体工具与表达方式。

附表给出全目录定义、各任务规模和逐条职责位置。Q2复核如修订任务，必须写明原文与理由，并重新生成规模；旧文板级电路51修正为56，不把生产工艺分母误用为板级电路。
''',encoding='utf-8')
state=json.loads((ROOT/'RUN_STATE.json').read_text(encoding='utf-8'))
state['steps'].update({'1':'COMPLETE_WITH_DEPLOYMENT_CLAIMS_WITHDRAWN','2':'BASELINE_COMPLETE_FINAL_V3_DELTA_PENDING','3':'COMPLETE_BASELINE_MEMBERSHIP_FROZEN','4':'IN_PROGRESS'})
state['updated_utc']=datetime.now(timezone.utc).isoformat();save_json('RUN_STATE.json',state)
print(js(dict(boundary_reads=len(rows),revision=overview,secondary_ads=sum(sec.values()))))
