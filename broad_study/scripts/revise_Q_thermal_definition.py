"""Targeted re-review of all inherited thermal labels in currently coded ads.
Researcher decisions below; not automatic semantic classification or full QC.
"""
from common import *
from datetime import datetime, timezone
from copy import deepcopy

revision_id='Q-M5-THERMAL-DEFINITION-20260916-06'
history_path=ROOT/'notes'/f'{revision_id}.json'
assert not history_path.exists(), 'Do not repeat a historical revision'
paths=sorted((ROOT/'configs/Q_adjudications').glob('*.json'))
docs={p:json.loads(p.read_text(encoding='utf-8')) for p in paths}
where={rid:p for p,d in docs.items() for rid in d['ads']}
ads={rid:d['ads'][rid] for p,d in docs.items() for rid in d['ads']}
old=json.loads((ROOT/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
by=defaultdict(list)
for r in old:by[r['reading_id']].append(r)
decisions={
('E0430','O9'):('SEPARATE','BACKGROUND','BACKGROUND','仅提出thermal constraints，未明确散热、热仿真、热路径或热布局；不足冻结定义，不由硬件架构职能补值。'),
('N0339','O12'):('DUTY_OWN_DEVELOP','EXAMPLE','OWN_DEVELOP','明确热设计；电气性能、尺寸、热设计等受等示例列表支配，不列无条件职责。'),
('E0124','O4'):('DUTY_OWN_USE','UNCONDITIONAL','OWN_USE','明确散热接口对接支持热管理概念；本人承担接口集成，未明确设计散热接口。'),
('N0792','O11'):('SEPARATE','BACKGROUND','BACKGROUND','thermal components安装对象未明示散热/热仿真/热路径/热布局；不将泛称温度相关部件自动等同热管理。'),
('N0784','O13'):('SEPARATE','BACKGROUND','BACKGROUND','thermal components安装对象不足冻结热管理定义；本广告另有明确thermal management优先要求，独立保留。'),
('E0467','O9'):('SEPARATE','BACKGROUND','BACKGROUND','thermals性能验证与温度测量不明确热管理/热设计；仅保留既有评测职责，不推热设计概念。'),
}
keep={
('N0951','O8'):'优化逆变器热行为并用仿真指导设计，结合紧凑板级布局与热要求，明确热设计工作。',
('N0951','O23'):'明确thermal management知识，局部including示例分支已修订。',
('E0464','O7'):'首轮已排除泛称thermal considerations，本次核对维持。',
('E0014','O8'):'液冷基础设施是采购对象，维持分离语境，不计本人热设计。',
('E0151','O8'):'热管理团队为协作对象，维持分离语境。',
('E0148','O9'):'配合研发定位热管理问题，维持协作语境。',
('N0784','O23'):'明确Understanding of thermal management，保持优先知识要求，不由安装部件推出。',
('E0479','O6'):'thermal subassemblies属于采购对象，维持分离语境。',
}
observed={(rid,f'O{i}') for rid in ads for i,r in enumerate(by[rid],1) if r['code']=='TC_THERMAL_MANAGEMENT'}
assert observed==set(decisions)|set(keep),(observed,set(decisions)|set(keep))
ledger=[];changes=[]
for rid,key in sorted(observed):
 a=ads[rid];orig=by[rid][int(key[1:])-1];before=deepcopy(a.get('old_overrides',{}).get(key))
 if (rid,key) in decisions:
  m,b,rel,reason=decisions[rid,key]
  override=dict(metric=m,branch=b,relation=rel,reason=reason)
  a.setdefault('old_overrides',{})[key]=override
  a['notes']+=f' 定向复核{revision_id}：'+reason
  a['updated_utc']=datetime.now(timezone.utc).isoformat()
  changes.append(dict(reading_id=rid,evidence_id=key,before=before,after=deepcopy(override),original=orig))
 else:reason=keep[rid,key]
 raw=RAW[a['identity_key']]
 local=[]
 for f in ['duties','requirements','full_description']:
  for line in (raw.get(f) or '').splitlines():
   if re.search(r'thermal|heat|热|cool|液冷',line,re.I) and line not in [v['quote'] for v in local]:
    local.append(dict(field=f,quote=line))
 ledger.append(dict(reading_id=rid,evidence_id=key,code='TC_THERMAL_MANAGEMENT',source_version=a['source_version'],original_quote=orig['quote'],decision='REVISED' if (rid,key) in decisions else 'REVIEWED_KEEP',reason=reason,effective_override=a.get('old_overrides',{}).get(key),reviewed_context=local,full_qc_completed=False))
history=dict(revision_id=revision_id,reviewer='Astra',created_utc=datetime.now(timezone.utc).isoformat(),scope='All inherited thermal-management occurrences in currently first-pass-coded ads; targeted definition review, not full second-pass QC',coded_ads_at_review=len(ads),reviewed_ads=len({x[0] for x in observed}),reviewed_occurrences=len(observed),changes=changes,ledger=ledger,frozen_definition='明确散热、热仿真、热路径或热布局设计。',protected_original_reference_unchanged=True)
for p,d in docs.items():p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
history_path.write_text(json.dumps(history,ensure_ascii=False,indent=2),encoding='utf-8')
print('Thermal targeted review:',len(observed),'occurrences;',len(changes),'derived revisions;',len({x[0] for x in observed}),'ads; full QC remains pending')

