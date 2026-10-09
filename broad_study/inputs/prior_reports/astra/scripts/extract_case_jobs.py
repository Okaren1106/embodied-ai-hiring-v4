from common import *
import re
cs=[c for case in json.loads((ROOT/'evidence/case_selection.json').read_text(encoding='utf-8'))['cases'] for c in case['companies']]
rr=[]
for k in sorted(ids(cs)):
 j=J[k];s=RAW[k];d=s.get('duties') or s.get('full_description') or '';req=s.get('requirements') or '';full=s.get('full_description') or d+'\n'+req
 title=j['title'];years=[];degree=[]
 for field,txt in [('requirements',req),('full_description',full)]:
  for line in txt.splitlines():
   if re.search(r'\d+\s*(?:\+|[-–至到]\s*\d+)?\s*(?:年|years?)|[三五八十]年',line,re.I): years.append({'field':field,'quote':line,'start':txt.find(line)})
   if re.search(r'本科|硕士|博士|学士|\bbachelor\b|\bmaster\b|\bph\.?d\b|\bb\.?s\.?\b|\bm\.?s\.?\b',line,re.I): degree.append({'field':field,'quote':line,'start':txt.find(line)})
 emp='INTERNSHIP_EXPLICIT_TITLE' if re.search('实习|intern',title,re.I) else 'CAMPUS_EXPLICIT_TITLE' if re.search('校招|届',title) else 'UNSPECIFIED'
 fulltime=re.search(r'full[- ]time|全职',full,re.I)
 rr.append({'identity_key':k,'company_id':j['company_id'],'reading_id':j['reading_id'],'title':title,'role':role(j),'location':j['location'],'wave':j['observation_date'],'employment_title_status':emp,'fulltime_explicit_text':bool(fulltime),'seniority_title_raw':';'.join(re.findall(r'Senior|Staff|Principal|Head|Director|Lead|高级|资深|专家|总监|经理|初级',title,re.I)) or 'NOT_SPECIFIED','years_quotes_json':js(list({js(v):v for v in years}.values())),'education_quotes_json':js(list({js(v):v for v in degree}.values())),'duties_chars':len(d),'requirements_chars':len(req),'source_coverage':j['source_coverage'],'source_url':j['source_url'],'note':'资历摘录保留全部原句，可能包含可替代要求；不统一职级、不把未写等于零。英文缩写检索待上下文解读。'})
dump('case_ad_seniority_source.csv',rr)
selected=['N0413','N0401','N0384','N0406','N0390','N0038','N0098','N0100','N0162','N0111','N0009','N0050','N0874','N0878','N0882','N0923','N0925','N0918']
out=[]
for rid in selected:
 k=next(k for k,j in J.items() if j['reading_id']==rid);j=J[k];s=RAW[k]
 out.append('## '+rid+' '+j['company_id']+' '+j['title']+'\n\n'+(s.get('duties') or s.get('full_description') or '')+'\n\n要求\n'+s.get('requirements',''))
(ROOT/'evidence/case_jobs_reading.md').write_text('\n\n'.join(out),encoding='utf-8')
print('case_ads',len(rr),'explicit_title_types',collections.Counter(r['employment_title_status'] for r in rr))
for c in cs:
 print(c,collections.Counter(r['employment_title_status'] for r in rr if r['company_id']==c),len([r for r in rr if r['company_id']==c and r['years_quotes_json']!='[]']))
print('READ selected 1-9')
print('\n\n'.join(out[:9]))
