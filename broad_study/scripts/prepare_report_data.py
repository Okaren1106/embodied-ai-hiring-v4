from common import *
def stream(n):
 with (ROOT/'tables'/n).open(encoding='utf-8-sig',newline='') as f:
  yield from csv.DictReader(f)
core=list(stream('Q4_display_cells_final.csv'))
def short(a):return {k:a[k] for k in ['label_code','label_name','metric','branch','P','U','N','share_ad_weighted','share_company_equal','unknown_low_ad','unknown_high_ad','gate','n_companies','max_positive_companies','max_positive_contribution']}
tops={}
for r in sorted({a['role'] for a in core}):
 d=[a for a in core if a['role']==r and a['branch']=='UNCONDITIONAL' and a['metric'] in ['GENERAL','DUTY_OWN_USE','DUTY_OWN_DEVELOP'] and int(a['P'])]
 tops[r]=[short(a) for a in sorted(d,key=lambda a:(-int(a['P']),a['label_code']))[:6]]
focus={}
for a in stream('Q4_task_strata_final.csv'):
 if a['prefixed_focus']=='YES' and a['metric']=='GENERAL' and a['branch']=='UNCONDITIONAL' and int(a['P']):
  focus.setdefault(a['role'],[]).append(dict(task=a['task'],**short(a)))
for r in focus:focus[r]=sorted(focus[r],key=lambda a:-int(a['P']))[:3]
keys={
 ('RF_ML_AI_ENGINEERING','SK_PYTHON'),('RF_ML_AI_ENGINEERING','SK_CPP'),
 ('RF_ROBOTICS_SOFTWARE','SK_LINUX'),('RF_ROBOTICS_SOFTWARE','SK_CPP'),
 ('RF_CONTROL_PLANNING','TC_CONTROL'),('RF_CONTROL_PLANNING','SK_CPP'),
 ('RF_DEPLOYMENT_FIELD_SERVICE','SK_PYTHON'),
 ('RF_MANUFACTURING_QUALITY_SUPPLY','V2_PROCUREMENT'),
 ('RF_HARDWARE_ELECTRICAL','TC_EMBEDDED')}
sens=[a for a in stream('Q4_aggregates_final.csv') if (a['role'],a['label_code']) in keys and a['metric']=='GENERAL' and a['branch']=='UNCONDITIONAL']
loo=[a for a in stream('Q4_leave_one_company_out_final.csv') if (a['role'],a['label_code']) in keys and a['metric']=='GENERAL' and a['branch']=='UNCONDITIONAL']
data=dict(tops=tops,focus=focus,sensitivity=sens,loo=loo,coverage=list(stream('Q4_role_coverage_final.csv')),scopes=list(stream('Q4_scope_definitions.csv')),qc=json.loads((ROOT/'verification/astra_materialization.json').read_text(encoding='utf-8')))
save_json('reports/final_report_data.json',data)
for r,v in tops.items():
 print(RN[r],js(v))
 print('FOCUS',js(focus.get(r,[])))
print('KEY SENS',js([dict(scope=a['scope'],role=a['role'],**short(a)) for a in sens if a['scope'] in ['WHOLE23','ALL24','DEDUPE_EXACT_DUTIES','EXCLUDE_EXPLICIT_CAMPUS_INTERN','S2_SOURCE_QUALITY']]))
print('FIELD LOO',js([short(a) for a in loo if a['role']=='RF_DEPLOYMENT_FIELD_SERVICE' and a['removed_company']=='US_FIELD_AI']))
