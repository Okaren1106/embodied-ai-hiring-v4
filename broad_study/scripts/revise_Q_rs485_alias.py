"""Second-pass RS485 alias back-check. Frozen aliases include 串口/RS232; do not narrow by protocol name."""
from common import *
from copy import deepcopy
from datetime import datetime, timezone
revision_id='Q-M5-RS485-ALIAS-20260916-11'
hp=ROOT/'notes'/f'{revision_id}.json'
assert not hp.exists()
changes=[]
edits={
 'N0498':[('2',[['V2_RS485','PREFERRED','UNRESOLVED']], '串口/网口斜线未决，按冻结宽串口组别名计入PREFERRED UNRESOLVED。'),
          ('3','DUPLICATE:N0498:2','同句串口短词。')],
 'E0076':[('3', None, 'comma列举含串口，补V2_RS485 GENERAL CHOICE。')],
 'N0643':[('2',[['V2_RS485','DUTY_OWN_USE','CHOICE']], '职责列举串口、网口等，按冻结宽串口组计入。'),
          ('6',[['V2_RS485','PREFERRED','UNCONDITIONAL']], '优先项串口通信，按冻结别名计入。')],
 'N0633':[('4', None, '职责列举含串口，补V2_RS485 DUTY_OWN_USE CHOICE。'),
          ('13', None, '斜线总线列举含串口，补V2_RS485 GENERAL UNRESOLVED。')],
 'E0031':[('5', None, '任选接口含串口，补V2_RS485 GENERAL CHOICE。')],
 'N0078':[('1', None, '列举含串口，补V2_RS485 GENERAL CHOICE。')],
}
docs={p:json.loads(p.read_text(encoding='utf-8')) for p in sorted((ROOT/'configs/Q_adjudications').glob('*.json'))}
where={}
for p,d in docs.items():
    for store,a in d['ads'].items():
        where[store]=p
        where[a.get('reading_id') or store]=p
        where[a['identity_key']]=p
def ad_of(rid):
    p=where[rid]
    d=docs[p]
    if rid in d['ads']: return d['ads'][rid], p
    for k,a in d['ads'].items():
        if a.get('reading_id')==rid or a['identity_key']==rid: return a,p
    raise KeyError(rid)
for rid, items in edits.items():
    a,p=ad_of(rid)
    before=deepcopy(a)
    for ni, action, reason in items:
        old=a['new'][ni]
        if action is None:
            assert isinstance(old,list), (rid,ni,old)
            if not any(x[0]=='V2_RS485' for x in old):
                if rid=='N0633' and ni=='4':
                    old.append(['V2_RS485','DUTY_OWN_USE','CHOICE'])
                elif rid=='N0633' and ni=='13':
                    old.append(['V2_RS485','GENERAL','UNRESOLVED'])
                elif rid in ('E0076','N0078'):
                    old.append(['V2_RS485','GENERAL','CHOICE'])
                elif rid=='E0031':
                    old.append(['V2_RS485','GENERAL','CHOICE'])
            a['new'][ni]=old
        else:
            a['new'][ni]=action
        changes.append(dict(reading_id=rid,cand=ni,before=old if action is not None else 'append',after=a['new'][ni],reason=reason))
    a.setdefault('revision_ids',[]).append(revision_id)
    a['notes']=(a.get('notes') or '')+' 二次复核'+revision_id+'：冻结V2_RS485别名含串口/RS232。'
    a['updated_utc']=datetime.now(timezone.utc).isoformat()
    a['qc_status']='SECOND_PASS_REVISED'
hp.write_text(json.dumps(dict(revision_id=revision_id,reviewer='grok4.6',kind='SYSTEMATIC_SECOND_PASS_FROZEN_ALIAS',frozen_catalog_changed=False,created_utc=datetime.now(timezone.utc).isoformat(),records=changes),ensure_ascii=False,indent=2),encoding='utf-8')
for p,d in docs.items():
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(revision_id, len(changes), 'candidate edits')
