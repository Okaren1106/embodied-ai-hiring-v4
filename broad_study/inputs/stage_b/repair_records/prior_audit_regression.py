"""Independent audit of delivered tables and evidence. Does not import producer code."""
from regression_context import HERE,RUN,BASE,rows,sha,save
from collections import Counter
from pathlib import Path
import json,re
facts=rows(RUN/'company_facts.csv');evs=rows(RUN/'company_evidence.csv');links=rows(RUN/'evidence_links.csv');groups=rows(RUN/'company_group_mapping.csv');caps=rows(RUN/'capital_events.csv');gaps=rows(RUN/'company_gaps.csv');profile=rows(RUN/'company_profile.csv')
fby={f['fact_id']:f for f in facts};eby={e['evidence_id']:e for e in evs};t1=rows(BASE/'stage_a_r3/T1_sample_company.csv');tby={r['company_id']:r for r in t1};strict=[g for g in groups if g['comparison_bucket']=='STRICT_COMPARABLE']
checks=[]
def check(name,passed,detail=None):checks.append({'name':name,'passed':bool(passed),'detail':detail})
check('24_company_ids_and_ads_match_r3',len(profile)==24 and set(p['company_id'] for p in profile)==set(tby) and all(p['n_ads_inherited']==tby[p['company_id']]['n_ads'] for p in profile))
check('1654_ads_preserved',sum(int(p['n_ads_inherited']) for p in profile)==1654)
check('fact_observation_dates_match_r3',all(f['observation_date']==tby[f['company_id']]['observation_dates'] for f in facts))
check('fact_evidence_link_ids_unique',len(fby)==len(facts) and len(eby)==len(evs) and len({l['link_id'] for l in links})==len(links))
check('all_link_ids_resolve',all(l['fact_id'] in fby and l['evidence_id'] in eby for l in links))
check('link_company_ids_match',all(l['company_id']==fby[l['fact_id']]['company_id']==eby[l['evidence_id']]['company_id'] for l in links))
check('fact_evidence_lists_match_edges',Counter((f['fact_id'],e) for f in facts for e in f['evidence_ids'].split('|') if e)==Counter((l['fact_id'],l['evidence_id']) for l in links))
og=rows(BASE/'stage_a_r3/company_gaps.csv');ogby={g['gap_id']:g for g in og}
check('307_original_gap_ids_preserved',len(gaps)==307 and Counter(g['orig_gap_id'] for g in gaps)==Counter(g['gap_id'] for g in og))
check('gap_inherited_values_preserved',all(g['inherited_value']==ogby[g['orig_gap_id']]['inherited_value'] and g['inherited_evidence_ids']==ogby[g['orig_gap_id']]['existing_evidence_ids'] for g in gaps))
check('gap_fact_references_resolve',all(i in fby for g in gaps for i in g['new_fact_ids'].split('|') if i))
unknown={'NOT_YET_SEARCHED','SEARCHED_NOT_FOUND','UNKNOWN','ACCESS_BLOCKED'}
check('unknown_values_not_zero_or_negative',all(not f['value'].strip() for f in facts if f['value_status'] in unknown))
unsearched=[f for f in facts if f['research_status']=='NOT_YET_SEARCHED']
check('unsearched_is_unchecked',all(f['checked_in_stage_b']=='NO' for f in unsearched),len(unsearched))
check('unsearched_not_in_strict_groups',not any(g['basis_fact_ids'] in {f['fact_id'] for f in unsearched} for g in strict))
check('strict_groups_resolve_facts',all(g['basis_fact_ids'] in fby for g in strict))
check('strict_groups_have_eligible_recorded_states',all(g['time_applicability'] in {'USABLE_AT_OBSERVATION','NOT_TIME_SENSITIVE'} and g['value_status'] in {'SUPPORTED_EXTERNAL','COMPANY_SELF_REPORT','MEDIA_STATEMENT','COUNTERPARTY_CONFIRMATION','MIXED_SEE_EVIDENCE','CONFLICT_RESOLVED_BY_SEPARATION'} for g in strict))
check('non_strict_not_included',all(g['included_in_comparison']=='NO' for g in groups if g['comparison_bucket']!='STRICT_COMPARABLE'))
snapshot_bad=[]
for e in evs:
    p=RUN/e['snapshot_text_path']
    if not p.is_file() or sha(p)!=e['snapshot_sha256']:snapshot_bad.append(e['evidence_id'])
check('all_evidence_snapshot_hashes_match',not snapshot_bad,snapshot_bad)
checksum_bad=[]
for n in ['release_checksums.json','output_checksums.json']:
    doc=json.loads((RUN/n).read_text(encoding='utf-8'))
    for rel,meta in doc['files'].items():
        p=RUN/rel
        if not p.is_file() or sha(p)!=meta['sha256'] or p.stat().st_size!=meta['bytes']:checksum_bad.append([n,rel])
check('release_and_output_checksums_current',not checksum_bad,checksum_bad)
lock=json.loads((RUN/'work/input_lock.json').read_text(encoding='utf-8'))
identities={e['identity'] for e in lock['entries']}
check('company_cache_locked','work/companies.json' in identities)
check('identity_map_locked','work/identity_map.json' in identities)
noetix=[f for f in facts if f['company_id']=='CN_NOETIX']
check('noetix_facts_no_flexiv',not any(re.search('非夕|flexiv',f['value']+' '+f['subject_entity'],re.I) for f in noetix))
check('noetix_positive_identity',any('松延' in f['value'] for f in noetix if f['field']=='legal_entity_name'))
check('noetix_wrong_evidence_withdrawn',not any('B_CN_NOETIX_001' in f['evidence_ids'].split('|') and '非夕' in eby.get('B_CN_NOETIX_001',{}).get('claim','') for f in noetix))
check('far_parent_context_only',all(l['relation']=='CONTEXT_ONLY' and l['qualifies_date']=='NO' for l in links if l['evidence_id']=='B_US_AMAZON_FTR_007'))
check('far_old_quote_binding_fixed','10426076' in eby['B_US_AMAZON_FTR_004']['url'])
publess=[c['capital_event_id'] for c in caps if c['time_applicability']=='USABLE_AT_OBSERVATION' and not c['publication_date']]
check('capital_asof_no_missing_publication',not publess,publess)
check('facts_asof_no_missing_publication',all(f['publication_date'] for f in facts if f['time_applicability']=='USABLE_AT_OBSERVATION'))
date_unpaired=[]
for f in facts:
    if f['time_applicability']=='NOT_TIME_SENSITIVE' or not (f['event_date'] or f['publication_date']):continue
    es=[eby[i] for i in f['time_basis_evidence_ids'].split('|') if i in eby]
    if (f['event_date'],f['publication_date']) not in {(e['event_date'],e['publication_date']) for e in es}:date_unpaired.append(f['fact_id'])
check('fact_dates_match_one_supporting_pair',not date_unpaired,date_unpaired)
check('limx_saved_publication_fixed',eby['B_CN_LIMX_002']['publication_date']=='2026-07-14' and '2026年07月14日' in (RUN/eby['B_CN_LIMX_002']['snapshot_text_path']).read_text(encoding='utf-8'))
fc=next(c for c in caps if c['capital_event_id']=='C_US_FIGURE__capital_event_figure_series_c')
check('figure_c_date_and_committed_capital',fc['event_date']==fc['publication_date']=='2025-09-16' and fc['amount_scope']=='COMMITTED_CAPITAL' and 'figure.ai/news/series-c' in eby[fc['evidence_ids']]['url'])
dc=next(c for c in caps if c['company_id']=='US_DILIGENT')
check('diligent_includes_contingent_and_closing_dates',dc['event_date']=='2026-01-27' and dc['publication_date']=='2026-01-29' and '含最高530' in dc['amount_original'] and 'sec.gov/' in eby[dc['evidence_ids']]['url'])
log=[json.loads(l) for l in (RUN/'search_log.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
derived=[l for l in log if l.get('tool')=='stage_b_repair_extension' and l.get('action')=='SEARCH']
check('192_generated_searches_marked_derived',len(derived)==192 and all(l.get('record_kind')=='DERIVED_STATUS_SUMMARY' for l in derived))
check('derived_search_not_reported_as_real',json.loads((RUN/'work/search_log_summary.json').read_text(encoding='utf-8'))['n_derived_search']==192)
gen=(RUN/'scripts/s11b_search_log_ext.py').read_text(encoding='utf-8')
check('status_based_search_generation_disabled','append_jsonl' not in gen)
check('browser_page_scope_updated','其余 21 家仍未查' not in (RUN/'index.html').read_text(encoding='utf-8'))
guard=json.loads((HERE/'protected_before.json').read_text(encoding='utf-8'))
changes=[p for p,h in guard.items() if not Path(p).is_file() or sha(Path(p))!=h]
check('all_protected_files_unchanged',not changes,{'n':len(guard),'changed':changes})
out={'n_checks':len(checks),'n_pass':sum(c['passed'] for c in checks),'n_fail':sum(not c['passed'] for c in checks),'checks':checks}
save('audit_checks.json',out)
print(json.dumps({k:v for k,v in out.items() if k!='checks'}|{'failed':[c for c in checks if not c['passed']]},ensure_ascii=False,indent=2))
raise SystemExit(1 if out['n_fail'] else 0)
