from bootstrap import *
import csv,collections,re
NEW=Path(json.loads((SCRATCH/'new_run.json').read_text(encoding='utf-8'))['run']);NR=NEW/'supplement_records'
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
facts=rows(NEW/'company_facts.csv');fby={f['fact_id']:f for f in facts};evs=rows(NEW/'company_evidence.csv');eby={e['evidence_id']:e for e in evs};groups=rows(NEW/'company_group_mapping.csv');links=rows(NEW/'evidence_links.csv')
old={f['fact_id']:f for f in rows(RUN/'company_facts.csv')};added=[f for f in facts if f['fact_id'] not in old];changed=[f for f in facts if f['fact_id'] in old and f!=old[f['fact_id']]]
ing=json.loads((NR/'ingestion.json').read_text(encoding='utf-8'));checks=[]
def check(n,p,d=None):checks.append({'name':n,'passed':bool(p),'detail':d})
check('24_companies_1654_ads',len(rows(NEW/'company_profile.csv'))==24 and sum(int(r['n_ads_inherited']) for r in rows(NEW/'company_profile.csv'))==1654)
check('all_existing_fact_and_evidence_ids_retained',set(old)<=set(fby) and {r['evidence_id'] for r in rows(RUN/'company_evidence.csv')}<=set(eby))
check('capital_table_unchanged',sha(NEW/'capital_events.csv')==sha(RUN/'capital_events.csv'))
check('all_nine_new_sources_linked',len(ing['new_sources'])==9 and all(any(l['evidence_id']==r['evidence_id'] for l in links) for r in ing['new_sources']))
norm=lambda s:re.sub(r'\s+','',s).casefold()
bad=[]
for r in ing['new_sources']:
 e=eby[r['evidence_id']];p=NEW/e['snapshot_text_path'];capture=NEW/e['capture_record_path']
 if sha(p)!=e['snapshot_sha256'] or sha(capture)!=e['capture_record_sha256'] or norm(e['quote']) not in norm(p.read_text(encoding='utf-8')):bad.append(e['evidence_id'])
 if e['capture_medium']=='ORIGINAL_HTTP_BYTES':
  if sha(NEW/e['snapshot_raw_path'])!=e['snapshot_raw_sha256']:bad.append(e['evidence_id']+':raw')
 else:
  j=json.loads(capture.read_text(encoding='utf-8'))
  if not j.get('not_original_http_bytes') or e['snapshot_raw_path'] or p.read_text(encoding='utf-8')!=j['response']:bad.append(e['evidence_id']+':web')
check('new_source_quotes_capture_media_and_hashes_valid',not bad,bad)
check('7_http_originals_2_web_extracts',sum(r['capture_medium']=='ORIGINAL_HTTP_BYTES' for r in ing['new_sources'])==7 and sum(r['capture_medium']=='WEB_TOOL_EXTRACT' for r in ing['new_sources'])==2)
check('no_unclassified_group_values',not any(g['group_value']=='UNCLASSIFIED_VALUE' for g in groups))
strict={dim:{g['company_id'] for g in groups if g['dimension']==dim and g['included_in_comparison']=='YES'} for dim in ['product_lines','delivery_form','target_markets']}
check('strict_coverage_23_23_22',[len(v) for v in strict.values()]==[23,23,22],{k:len(v) for k,v in strict.items()})
check('galaxea_no_date_stays_background',fby['F_CN_GALAXEA__target_markets']['time_applicability']=='DATE_UNKNOWN' and 'CN_GALAXEA' not in strict['target_markets'])
check('unitree_current_industry_page_stays_background',fby['F_CN_UNITREE__target_markets__2']['time_applicability']=='DATE_UNKNOWN' and not any(g['basis_fact_ids']=='F_CN_UNITREE__target_markets__2' and g['included_in_comparison']=='YES' for g in groups))
check('unitree_actual_research_use_separate_from_far_outputs',fby['F_CN_UNITREE__target_markets']['assertion_kind']=='OBSERVED_APPLICATION' and eby['NEW_UNITREE_01']['url']==eby['IR_FAR_02']['url'] and 'US_AMAZON_FTR' not in strict['product_lines'])
check('no_new_paid_claim',all(f['field']!='evidence_paid' for f in added+changed))
spock=[f for f in facts if f['company_id']=='CN_DEEPROBOTICS' and '本篇未标厂商' in f['value']][0]
check('spock_customer_confirmed_scope_limited',spock['time_basis_evidence_ids']=='NEW_DEEP_02' and any(l['fact_id']==spock['fact_id'] and l['evidence_id']=='NEW_DEEP_01' and l['relation']=='CONTEXT_ONLY' for l in links))
check('limx_preorder_not_actual_delivery',fby['F_CN_LIMX__delivery_form__2']['assertion_kind']=='COMMERCIAL_OFFER' and '预订' in fby['F_CN_LIMX__delivery_form__2']['value'])
check('galbot_direct_customer_confirmation',fby['F_CN_GALBOT__evidence_customer_delivery']['value_status']=='COUNTERPARTY_CONFIRMATION' and eby['NEW_GALBOT_01']['url']=='https://www.catl.com/news/10053.html')
check('spirit_media_not_hardware_sales_inference',fby['F_CN_SPIRITAI__delivery_form__2']['value_status']=='MEDIA_STATEMENT' and {g['group_value'] for g in groups if g['basis_fact_ids']=='F_CN_SPIRITAI__delivery_form__2'}=={'HARDWARE_DEPLOYMENT'})
check('ces_publication_day_event_month_retained',eby['IR_FOURIER_01']['publication_date']=='2026-01-07' and eby['IR_FOURIER_01']['event_date']=='2026-01')
protected=json.loads((AUDIT/'protected_before.json').read_text(encoding='utf-8'));bad=[p for p,h in protected.items() if not Path(p).is_file() or sha(Path(p))!=h]
check('2615_originals_still_unchanged',not bad,bad)
data={'tables':{n:len(rows(NEW/(n+'.csv'))) for n in ['company_facts','company_evidence','evidence_links','capital_events','company_gaps','company_group_mapping','company_profile']},'unique_source_urls':len({e['url'] for e in evs}),'strict_coverage':{k:len(v) for k,v in strict.items()},'all_three':len(set.intersection(*strict.values())),'no_three':sorted({f['company_id'] for f in facts}-set.union(*strict.values())),'gap_status':dict(collections.Counter(r['stage_b_status'] for r in rows(NEW/'company_gaps.csv'))),'new_facts':len(added),'changed_existing_facts':len(changed),'changed_companies':sorted({f['company_id'] for f in added+changed}),'new_sources':9,'new_http_originals':7,'new_web_extracts':2}
save(NR/'data_summary.json',data);save(NR/'validation.json',{'n_checks':len(checks),'n_pass':sum(c['passed'] for c in checks),'n_fail':sum(not c['passed'] for c in checks),'checks':checks});save(NR/'fact_delta.json',{'added':added,'changed':[{'old':old[f['fact_id']],'new':f} for f in changed]})
print(json.dumps(data|{'checks':len(checks),'failed':[c for c in checks if not c['passed']]},ensure_ascii=False,indent=2))
raise SystemExit(1 if any(not c['passed'] for c in checks) else 0)
