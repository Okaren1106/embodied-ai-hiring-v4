from common import *
import re
lock_check()
PAIRS=[('RESEARCH_ENGINEERING','ACT_RESEARCH','ACT_ENGINEERING'),('ENGINEERING_QUALITY','ACT_ENGINEERING','ACT_QUALITY'),('ENGINEERING_DEPLOYMENT','ACT_ENGINEERING','ACT_DEPLOYMENT')]
STATES=['UNCONDITIONAL','CONDITIONAL_ONLY','CHOICE_ONLY','UNRESOLVED','NO_RECORDED_JOINT']
def locate(k,r):
 q=r.get('quote','');field=r.get('field','');text=RAW[k].get(field,'') or '';start=r.get('start','')
 if q and str(start).isdigit() and text[int(start):int(start)+len(q)]==q:return {'field':field,'start':int(start),'end':int(start)+len(q),'status':'EXACT_OFFSET','quote':q}
 if q and q in text:return {'field':field,'start':text.find(q),'end':text.find(q)+len(q),'status':'EXACT_QUOTE_RELOCATED','quote':q}
 for f in ['duties','requirements','full_description']:
  txt=RAW[k].get(f,'') or ''
  if q and q in txt:return {'field':f,'start':txt.find(q),'end':txt.find(q)+len(q),'status':'EXACT_QUOTE_OTHER_FROZEN_FIELD','quote':q}
 # Some accepted quotes join wrapped lines with spaces. Preserve original and relocated raw text.
 if q:
  pattern=r'\s+'.join(re.escape(s) for s in q.split())
  for f in ['duties','requirements','full_description']:
   txt=RAW[k].get(f,'') or '';m=re.search(pattern,txt)
   if m:return {'field':f,'start':m.start(),'end':m.end(),'status':'WHITESPACE_ONLY_RELOCATED','quote':q,'frozen_exact_quote':m.group()}
 return {'field':field,'start':start,'end':r.get('end',''),'status':'NOT_LOCATED','quote':q}
def joint_judge(k,ev1,ev2):
 # Existing primary role tree and exact evidence, plus a conservative lexical screen for unbound directions.
 es1=[locate(k,x) for x in ev1];es2=[locate(k,x) for x in ev2]
 if not any(e['status']!='NOT_LOCATED' for e in es1) or not any(e['status']!='NOT_LOCATED' for e in es2):return 'UNRESOLVED','至少一个活动缺少可在冻结正文定位的引文',es1,es2
 s=ST.get(k)
 if s and (s['root_relation']!='ALL' or s['has_mixed_branch']=='YES'):return 'UNRESOLVED','可选职责方向存在，联合证据未绑定无条件分支',es1,es2
 txt='\n'.join(e['quote'] for e in es1+es2)
 if re.search(r'以下.{0,6}(?:一个|一项|方向)|任一方向|depending on (?:your|the) (?:interest|background)|one or more (?:of the following|areas)|either.{0,100}\bor\b',txt,re.I):return 'UNRESOLVED','活动引文存在可选提示，未建立无条件连接',es1,es2
 return 'UNCONDITIONAL','两项原OWNED引文可定位，职责树无互斥分支；同广告直接责任列表可共同成立',es1,es2
line=[];coll=[]
for name,a,b in PAIRS:
 for k in sorted(admitted):
  double=k in OWN[a] and k in OWN[b];state='NO_RECORDED_JOINT';reason='无原编码双本人承担';e1=[];e2=[]
  if double:state,reason,e1,e2=joint_judge(k,AE[(k,a,'OWNED')],AE[(k,b,'OWNED')])
  line.append({'pair':name,'activity1':a,'activity2':b,'identity_key':k,'reading_id':J[k]['reading_id'],'company_id':J[k]['company_id'],'role':role(J[k]),'raw_double_positive':double,'joint_state':state,'reason':reason,'tree':ST.get(k,{}).get('tree_json',''),'evidence1_json':js(e1),'evidence2_json':js(e2),'source_url':J[k]['source_url']})
  if k in (OWN[a]|PART[a]) and k in (OWN[b]|PART[b]) and (k in PART[a] or k in PART[b]):coll.append({'pair':name,'identity_key':k,'company_id':J[k]['company_id'],'activity1_owned':k in OWN[a],'activity2_owned':k in OWN[b],'activity1_participates':k in PART[a],'activity2_participates':k in PART[b],'note':'参与协作另表，可能同时有本人承担；不得加入主联合分子'})
dump('activity_joint_ad_status.csv',line);dump('activity_joint_participation.csv',coll)
def summary_joint(rr,scope,cs):
 records=[]
 for pair in sorted({r['pair'] for r in rr}):
  rs=[r for r in rr if r['pair']==pair and r['company_id'] in cs];ct=collections.Counter(r['joint_state'] for r in rs);base=len(rs);u=ct['UNRESOLVED'];p=ct['UNCONDITIONAL'];n=base-u
  pts=[(c,len([r for r in rs if r['company_id']==c and r['joint_state']=='UNCONDITIONAL']),len([r for r in rs if r['company_id']==c and r['joint_state']!='UNRESOLVED'])) for c in cs if any(r['company_id']==c for r in rs)]
  records.append({'scope':scope,'pair':pair,'raw_double_P':sum(r['raw_double_positive'] for r in rs),'B':base,'U':u,'Z':n-p,'unknown_low':ratio(p,base),'unknown_high':ratio(p+u,base),**{s:ct[s] for s in STATES},**distribution(pts)})
 return records
summ=[]
for scope,cs in {'ALL24':ALL,'WHOLE23':WHOLE,'ACTIVITY_COMPLETE_COMPANIES':FULL}.items():summ+=summary_joint(line,scope,cs)
dump('activity_joint_summary.csv',summ)
dump('activity_joint_company.csv',[r|{'company_id':c} for c in ALL for r in summary_joint(line,'COMPANY',[c])])
dump('activity_joint_role.csv',[{'pair':p,'role':r,'role_name':RN[r],'B':len(sub),'P':sum(x['joint_state']=='UNCONDITIONAL' for x in sub),'U':sum(x['joint_state']=='UNRESOLVED' for x in sub),'n_positive_companies':len({x['company_id'] for x in sub if x['joint_state']=='UNCONDITIONAL'})} for p in [x[0] for x in PAIRS] for r in ROLES if (sub:=[x for x in line if x['pair']==p and x['role']==r])])
# ML technical pairs use inherited per-label PRESENT / UNKNOWN; an unknown is pair-relevant only if the other label is not known Z.
sem=read(C/'tables/T3_all_item_semantics.csv');tech=read(A/'technical_concepts.csv');ti={(r['identity_key'],r['item_index']):r for r in tech}
ml={k for k,j in J.items() if j['primary_code']=='RF_ML_AI_ENGINEERING' and j['primary_status']=='CODED' and j['company_id'] in WHOLE and j['technical_status']!='SOURCE_UNASSESSABLE'}
labels=['TC_ML_SYSTEMS','TC_FOUNDATION_MODELS_VLA','TC_DATA_PIPELINES']
all_labels={x['label_code']:x['label_name'] for x in tech};print('TECH LABELS',[(k,v) for k,v in all_labels.items() if any(s in v for s in ['基础模型','数据管','资产'])])
labels=['TC_ML_SYSTEMS']+[k for k,v in all_labels.items() if ('基础模型' in v or 'VLA' in v)]+[k for k,v in all_labels.items() if '数据管线' in v]
assert len(labels)==3,labels
ll=read(C/'tables/T3_positive_unknown_lineage.csv');ls={(r['identity_key'],r['label_code']):r['state'] for r in ll if r['role_code']=='RF_ML_AI_ENGINEERING' and r['dimension']=='technical_concepts' and r['metric_bucket']=='DUTY_OWN_DEVELOP' and r['branch_bucket']=='UNCONDITIONAL'}
te=collections.defaultdict(list)
for r in sem:
 if r['dimension']=='technical_concepts' and r['metric_bucket']=='DUTY_OWN_DEVELOP' and r['branch_bucket']=='UNCONDITIONAL' and r['positive_recorded_mention']=='YES':te[(r['identity_key'],r['label_code'])].append(ti[(r['identity_key'],r['item_index'])])
tline=[]
for a,b in itertools.combinations(labels,2):
 for k in sorted(ml):
  s1=ls.get((k,a),'NO_RECORDED_POSITIVE');s2=ls.get((k,b),'NO_RECORDED_POSITIVE');double=s1==s2=='PRESENT';state='NO_RECORDED_JOINT';reason='至少一项已知未记录正向';e1=[];e2=[]
  if double:state,reason,e1,e2=joint_judge(k,te[(k,a)],te[(k,b)])
  elif 'UNKNOWN' in [s1,s2] and 'NO_RECORDED_POSITIVE' not in [s1,s2]:state='UNRESOLVED';reason='单标签未知会改变该联合指标'
  tline.append({'pair':a+'__'+b,'identity_key':k,'company_id':J[k]['company_id'],'reading_id':J[k]['reading_id'],'state1':s1,'state2':s2,'raw_double_positive':double,'joint_state':state,'reason':reason,'evidence1_json':js(e1),'evidence2_json':js(e2)})
dump('ML_technical_joint_ad_status.csv',tline);dump('ML_technical_joint_summary.csv',summary_joint(tline,'WHOLE_ML',WHOLE))
print('ACTIVITY JOINT',[(r['scope'],r['pair'],r['raw_double_P'],r['P'],r['U'],r['N']) for r in summ]);print('UNRESOLVED',[(r['reading_id'],r['pair'],r['reason']) for r in line if r['joint_state']=='UNRESOLVED'])
