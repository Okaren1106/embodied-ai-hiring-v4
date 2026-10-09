from bootstrap import *
import csv,collections
def rows(p):return list(csv.DictReader(Path(p).open(encoding='utf-8-sig',newline='')))
tables={n:rows(RUN/(n+'.csv')) for n in ['company_facts','company_evidence','evidence_links','capital_events','company_gaps','company_group_mapping','company_profile']}
old={f['fact_id']:f for f in rows(OLD/'company_facts.csv')};facts=tables['company_facts']
delta=[]
for f in facts:
 prior=old.get(f['fact_id']);diff=list(f) if prior is None else [k for k in f if f[k]!=prior.get(k)]
 if diff:delta.append({'fact_id':f['fact_id'],'company_id':f['company_id'],'changed_fields':diff,'old':prior,'new':f})
save(RUN/'repair_records/fact_delta.json',delta)
groups=tables['company_group_mapping'];dims=['product_lines','delivery_form','target_markets']
sets={d:{g['company_id'] for g in groups if g['dimension']==d and g['included_in_comparison']=='YES'} for d in dims}
cids={c['company_id'] for c in tables['company_profile']}
ing=read(RUN/'work/supplement_ingestion.json')
summary={'tables':{k:len(v) for k,v in tables.items()},'unique_source_urls':len({e['url'] for e in tables['company_evidence']}),'review_cards':len(ing['cards']),'new_evidence_vs_targeted':len(tables['company_evidence'])-len(rows(OLD/'company_evidence.csv')),'fact_rows_added':len(facts)-len(old),'existing_fact_rows_changed':sum(d['old'] is not None for d in delta),'changed_companies':sorted({d['company_id'] for d in delta}),'strict_coverage':{d:len(v) for d,v in sets.items()},'all_three':len(set.intersection(*sets.values())),'none_three':sorted(cids-set.union(*sets.values())),'excluded_per_dimension':{d:sorted(cids-v) for d,v in sets.items()},'gap_status':dict(collections.Counter(g['stage_b_status'] for g in tables['company_gaps'])),'web_extract_review_cards':[c['review_id'] for c in ing['cards'] if c['capture_medium']=='WEB_TOOL_EXTRACT'],'source_status_downgrade_only':[d['fact_id'] for d in delta if d['old'] and d['old']['value_status']=='SUPPORTED_EXTERNAL' and d['new']['value_status']=='MEDIA_STATEMENT' and d['old']['value']==d['new']['value']]}
save(RUN/'repair_records/data_summary.json',summary);print(json.dumps(summary,ensure_ascii=False,indent=2))
