"""Source identity and scoped-claim regression checks. Offline; no facts are altered."""
from pathlib import Path
import json,re
from s00_common import RUN,WORK,read_csv,read_json,sha256_file

def semantic_checks():
 out=[]
 def check(cid,name,ok,detail):out.append({'id':cid,'name':name,'passed':bool(ok),'detail':str(detail)})
 try:
  root=Path(RUN);work=Path(WORK)
  evs=read_csv(root/'company_evidence.csv');ev={e['evidence_id']:e for e in evs}
  facts=read_csv(root/'company_facts.csv');fs={f['fact_id']:f for f in facts}
  caps={c['capital_event_id']:c for c in read_csv(root/'capital_events.csv')}
  links=read_csv(root/'evidence_links.csv');snap=read_json(work/'snapshot_index.json')['snapshots']
  baseline=read_json(work/'evidence_identity_baseline.json')['entries']
  bad=[eid for eid,b in baseline.items() if eid not in ev or ev[eid]['url']!=b['url'] or ev[eid]['company_id']!=b['company_id']]
  check('B5_IDENTITY','同一证据ID保持同一公司与来源身份',not bad and len(ev)==len(evs),'mismatched IDs='+repr(bad))
  bindings=read_json(work/'capital_claim_bindings.json')['bindings'];bad=[]
  norm=lambda s:re.sub(r'\s+','',s).casefold()
  for b in bindings:
   c=caps.get(b['capital_event_id'],{});e=ev.get(b['evidence_id'],{});sp=snap.get(e.get('snapshot_id'),{})
   p=root/sp.get('snapshot_text_path','');text=p.read_text(encoding='utf-8') if p.is_file() else ''
   ok=(c.get('evidence_ids')==b['evidence_id'] and e.get('url')==b['source_url'] and e.get('snapshot_id')==b['snapshot_id'] and all(c.get(k)==b[k] for k in ['publication_date','event_date','amount_scope']) and e.get('publication_date')==b['publication_date'] and all(norm(q) in norm(text) for q in b['required_source_fragments']))
   if not ok:bad.append(b['capital_event_id'])
  c=caps.get('C_US_FIGURE__capital_event_figure_series_c',{})
  financing=[fs.get('F_US_FIGURE__'+f,{}) for f in ['capital_event_figure_series_c','latest_financing_disclosed','latest_financing_at_observation']]
  product=[fs.get('F_US_FIGURE__'+f,{}) for f in ['product_lines','delivery_form','target_markets']]
  ok=not bad and '承诺' in c.get('amount_original','') and all('B_US_FIGURE_004' in f.get('time_basis_evidence_ids','').split('|') and 'B_US_FIGURE_006' not in f.get('evidence_ids','') for f in financing) and all('B_US_FIGURE_006' in f.get('evidence_ids','') and 'B_US_FIGURE_004' not in f.get('evidence_ids','') for f in product)
  check('B5_CAPITAL','Figure C日期/承诺资本/估值直接来源与产品来源分离',ok,'unsupported capital bindings='+repr(bad))
  ingestion=read_json(work/'supplement_ingestion.json')['cards'];bad=[]
  linked={l['evidence_id'] for l in links}
  for card in ingestion:
   e=ev.get(card['evidence_id'],{});s=snap.get(e.get('snapshot_id'),{})
   if not e or e['evidence_id'] not in linked:bad.append(card['review_id']+':missing or unused');continue
   for pk,hk in [('snapshot_text_path','body_text_sha256'),('snapshot_raw_path','raw_sha256'),('capture_record_path','capture_record_sha256')]:
    if s.get(pk):
     p=root/s[pk]
     if not p.is_file() or sha256_file(p)!=s.get(hk):bad.append(card['review_id']+':'+pk)
   if e.get('capture_medium')=='WEB_TOOL_EXTRACT':
    if e.get('snapshot_raw_path') or e.get('snapshot_raw_sha256') or not e.get('capture_record_path'):bad.append(card['review_id']+':tool text mislabeled raw')
  check('B5_CAPTURE','16张审阅卡全部入表且保存媒介/哈希不混同',len(ingestion)==16 and not bad,bad)
  bad=[]
  for f in facts:
   actual={l['evidence_id'] for l in links if l['fact_id']==f['fact_id']}
   expected=set(f['evidence_ids'].split('|'))-{''}
   if actual!=expected:bad.append(f['fact_id'])
  check('B5_SCOPE_REL','同字段多个产品或事件逐行绑定各自证据',not bad,bad)
  media_bad=[]
  for f in facts:
   es=[ev[x] for x in f['time_basis_evidence_ids'].split('|') if x in ev]
   if es and all(e.get('claim_nature') in ['MEDIA_STATEMENT','MEDIA_REPORT'] for e in es) and f['value_status'] in ['SUPPORTED_EXTERNAL','COUNTERPARTY_CONFIRMATION']:media_bad.append(f['fact_id'])
  check('B5_MEDIA','仅有媒体报道支持的事实不升级为外部确认',not media_bad,media_bad)
  get=lambda cid,field:fs.get('F_'+cid+'__'+field,{})
  n=get('CN_NOETIX','evidence_customer_delivery');paid=get('CN_NOETIX','evidence_paid')
  sp=fs.get('F_CN_SPIRITAI__product_lines__2',{})
  far=get('US_AMAZON_FTR','product_lines');ags=get('US_AGILITY','evidence_paid')
  bd=get('US_BOSTON_DYNAMICS','deployment_status_actual');f02=get('US_FIGURE','deployment_status_actual');f03=fs.get('F_US_FIGURE__deployment_status_actual__2',{})
  check('B5_BOUNDARIES','捐赠/自述收入/研究本体/产品计划保持分离',
        n.get('assertion_kind')=='DONATION' and '两台' in n.get('value','') and paid.get('value_status')=='SEARCHED_NOT_FOUND' and sp.get('value_status')=='CONFLICT' and far.get('assertion_kind')=='RESEARCH_OUTPUT' and 'Unitree G1' in far.get('value','') and ags.get('value_status')=='COMPANY_SELF_REPORT' and 'IR_AGILITY_01' in ags.get('time_basis_evidence_ids','') and 'Stretch' in bd.get('product_or_business_scope','') and 'Atlas' not in bd.get('value','') and f02.get('value_status')=='COUNTERPARTY_CONFIRMATION' and f03.get('value_status')=='COMPANY_SELF_REPORT',
        'Noetix donation; Moz1 date conflict; FAR uses Unitree; GXO quotes supplier; F02/F03 and Stretch/Atlas separate')
  astro=ev.get('B_CN_ASTRIBOT_001',{});asp=root/astro.get('snapshot_text_path','')
  at=asp.read_text(encoding='utf-8') if asp.is_file() else ''
  check('B5_DATE','星尘发布日期来自原文日期行',astro.get('publication_date')=='2026-06-03' and '2026-06-03 12:06' in at and '原页无日期' not in astro.get('note',''),'evidence date='+astro.get('publication_date',''))
  groups=read_csv(root/'company_group_mapping.csv')
  bad=[g['basis_fact_ids'] for g in groups if g['included_in_comparison']=='YES' and fs.get(g['basis_fact_ids'],{}).get('assertion_kind') in ['RESEARCH_OUTPUT','LONG_TERM_GOAL','DATE_CONFLICT']]
  check('B5_GROUP','团队研究产物与长期目标不混入当前产品/场景业务组',not bad,bad)
 except Exception as exc:
  check('B5_ERROR','语义复核输入完整',False,repr(exc))
 return out

if __name__=='__main__':
 r=semantic_checks();print(json.dumps(r,ensure_ascii=False,indent=2));raise SystemExit(0 if all(x['passed'] for x in r) else 1)
