"""Apply Astra's explicit, source-reviewed boundary corrections once; retain before/after."""
from common import *
import copy, datetime

revision_id='Q-M5-INCIDENT-BOUNDARY-20260916-01'
history=ROOT/'configs/history'/f'{revision_id}.json'
assert not history.exists(), 'Revision already applied; refuse replay'
path=ROOT/'configs/Q_adjudications/RF_MANUFACTURING_QUALITY_SUPPLY.json'
data=json.loads(path.read_text(encoding='utf-8'))
before=hashlib.sha256(path.read_bytes()).hexdigest()
queue={r['review_id']:r for r in json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'))}
decisions={
 'N0888':['2'], 'N0678':['1'], 'N0786':['1','3','8'],
 'E0593':['1','2'], 'N0977':['4'], 'N0948':['2','6','12'],
 'E0038':['3'], 'E0367':['5'], 'E0331':['3'], 'E0330':['3'],
 'E0312':[],
}
reason='冻结V2_INCIDENT_SUPPORT限于运行中的排障、恢复、工单与升级；本提及为开发/原型/测试调试或未分对象的一般调试，未明示运行维护，不作为该窄类别正例。'
records=[]
for rid,indices in decisions.items():
 a=data['ads'][rid];old=copy.deepcopy(a);changes=[]
 for i in indices:
  actions=a['new'][i];assert isinstance(actions,list)
  removed=[x for x in actions if x[0]=='V2_INCIDENT_SUPPORT'];assert len(removed)==1
  remaining=[x for x in actions if x[0]!='V2_INCIDENT_SUPPORT']
  q=queue[rid+':'+i]
  a['new'][i]=remaining if remaining else 'OUTSIDE:'+reason
  if remaining:a.setdefault('outside_extra',[]).append(dict(quote=q['quote'],description=reason))
  changes.append(dict(review_id=rid+':'+i,removed=removed,remaining=remaining,quote=q['quote'],reason=reason))
 if rid=='E0312':
  matches=[x for x in a.get('additions',[]) if x['code']=='V2_INCIDENT_SUPPORT'];assert len(matches)==1
  a['additions']=[x for x in a['additions'] if x['code']!='V2_INCIDENT_SUPPORT']
  a.setdefault('outside_extra',[]).append(dict(quote=matches[0]['quote'],description=reason))
  changes.append(dict(removed_addition=matches[0],reason=reason))
 if rid=='N0948':
  extra=dict(code='V2_INCIDENT_SUPPORT',metric='PREFERRED',branch='UNCONDITIONAL',
    quote='Operational experience with robotic control systems, including performance monitoring, hardware health diagnostics, and data-driven analysis of robotic system behavior during testing and deployment',
    reason='另一个优先条件明确运行经验与硬件健康诊断；与设计集成调试句分开，具有运行对象证据。')
  assert locate(a['identity_key'],extra)['method']!='UNRESOLVED_LOCATION'
  a.setdefault('additions',[]).append(extra);changes.append(dict(added=extra))
 a.setdefault('revision_ids',[]).append(revision_id)
 a['notes']+=' 本轮运行排障边界定向复核：开发调试不直接纳入；见'+revision_id+'。'
 a['updated_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 records.append(dict(reading_id=rid,before=old,after=copy.deepcopy(a),changes=changes))
history.parent.mkdir(exist_ok=True)
encoded=json.dumps(data,ensure_ascii=False,indent=2).encode('utf-8')
payload=dict(revision_id=revision_id,reviewer='Astra',kind='TARGETED_FIRST_PASS_BOUNDARY_REVIEW_NOT_FULL_SECOND_PASS',
 frozen_definition_unchanged=True,source= 'configs/Q_catalog_v2_frozen.json#V2_INCIDENT_SUPPORT',
 before_config_sha256=before,after_config_sha256=hashlib.sha256(encoded).hexdigest(),records=records,
 retained_runtime_examples=['N0196:产线运行、升级回退和现场异常处理','E0038:终端现场故障定位职责补录','E0188:CNC日常维护排故','E0163:线上故障治理','E0332:现场升级与客户停机处置'],
 constraints='一般调试未分对象时不因岗位另含现场任务而回填为运行维护要求；未把研发调试改成客户现场维护。')
history.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
path.write_bytes(encoded)
print(revision_id,len(records),'ads revised;',sum(len(r['changes']) for r in records),'explicit changes; before/after retained')
