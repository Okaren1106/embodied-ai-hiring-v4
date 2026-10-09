"""Stage C. Frozen classifications, no recoding. Python stdlib only."""
from pathlib import Path
import csv,json,hashlib,sys,importlib.util
from collections import Counter,defaultdict
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'inputs/rules_v1'; A=R/'inputs/stage_a'; T=ROOT/'tables'
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def js(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def table(name,rows):
 rows=list(rows); assert rows,name
 p=T/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check_inputs():
 for rel,e in js(ROOT/'input_lock.json')['files'].items():
  p=ROOT/rel
  if not p.is_file() or sha(p)!=e['sha256'] or p.stat().st_size!=e['bytes']:raise ValueError('INPUT_DRIFT: '+rel)
def ratio(n,d):return round(n/d,10) if d else ''
def main():
 check_inputs();T.mkdir(exist_ok=True)
 spec=importlib.util.spec_from_file_location('fixed_rules',R/'scripts/build_rules.py');rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules)
 jobs=read(A/'jobs.csv');byid={j['identity_key']:j for j in jobs};assert len(byid)==1654
 cs=read(R/'company_classification.csv');cb={c['company_id']:c for c in cs};companies=sorted(cb)
 jc={c:[j for j in jobs if j['company_id']==c] for c in companies};whole={c for c in companies if cb[c]['scope_main_company']=='YES'}
 qrule=js(R/'decisions/q2_rules.json'); selected=read(R/'q2_display_selection.csv')
 # T1: inherited sampling fields + frozen factual classification. No new external claims.
 t1=[]
 for row in read(A/'T1_sample_company.csv'):
  c=cb[row['company_id']];r=dict(row)
  for k in ['stratum','stratum_name','scope_main_company','known_multi_product','media_only_basis','basis_fact_ids','basis_evidence_ids','caveat']:r[k]=c[k]
  r['current_scenes_json']=json.dumps([s['scene'] for s in read(R/'company_scene_matrix.csv') if s['company_id']==row['company_id'] and s['connection_status']=='CURRENT_CONNECTION'],ensure_ascii=False)
  t1.append(r)
 table('T1_company_sample.csv',t1)
 # Q1: all 22 categories, including three statuses. Recalculate from unique ads.
 prior=read(A/'T2_company_primary_roles.csv');cats={r['class_code']:(r['class_name'],r['class_kind']) for r in prior}
 classof=lambda j:j['primary_code'] if j['primary_status']=='CODED' else j['primary_status']
 q1=[]
 for c in companies:
  cnt=Counter(classof(j) for j in jc[c]);den=len(jc[c]);coded=sum(j['primary_status']=='CODED' for j in jc[c])
  for code,(name,kind) in cats.items():
   q1.append(dict(company_id=c,company_name=cb[c]['company_name'],country=cb[c]['country'],stratum=cb[c]['stratum'],class_code=code,class_name=name,class_kind=kind,n_ads=cnt[code],denominator_all=den,share_all=ratio(cnt[code],den),denominator_coded=coded,n_coded=cnt[code] if kind in ['concrete','structure'] else 0,share_coded=ratio(cnt[code],coded) if kind in ['concrete','structure'] else '',small_n_under10='YES' if den<10 else 'NO'))
 table('T2_company_primary_roles.csv',q1)
 table('T2_ad_lineage.csv',[{k:j[k] for k in ['identity_key','record_id','reading_id','company_id','title','source_url','observation_date','rule_version','text_version_hash','primary_status','primary_code']}|{'analysis_class':classof(j)} for j in jobs])
 q1groups={'ALL24':set(companies),'WHOLE23':whole}
 q1groups.update({g:{c for c in companies if cb[c]['stratum']==g} for g in sorted({r['stratum'] for r in cs})})
 qa=[]
 for group,members in q1groups.items():
  for denominator in ['ALL','CODED']:
   for code,(name,kind) in cats.items():
    rows=[r for r in q1 if r['company_id'] in members and r['class_code']==code]
    ds=[r['denominator_all' if denominator=='ALL' else 'denominator_coded'] for r in rows]; ns=[r['n_ads' if denominator=='ALL' else 'n_coded'] for r in rows]
    structural_available=denominator=='ALL' or kind in ['concrete','structure']
    eq=sum(n/d for n,d in zip(ns,ds) if d)/sum(d>0 for d in ds) if structural_available and any(ds) else ''
    qa.append(dict(scope=group,denominator_basis=denominator,class_code=code,class_name=name,class_kind=kind,n_ads=sum(ns),denominator=sum(ds),n_companies=sum(d>0 for d in ds),share_ad_weighted=ratio(sum(ns),sum(ds)) if structural_available else '',share_company_equal=round(eq,10) if eq!='' else '',note='FAR为团队单列；供给组为样本描述，不作国家效应推断'))
 table('T2_aggregates.csv',qa)
 # Q2: fixed semantic interpretation and display selection; retain every original item.
 items=read(R/'diagnostics/q2_item_interpretation.csv');bylabel=defaultdict(list)
 for r in items:bylabel[(r['identity_key'],r['dimension'],r['label_code'])].append(r)
 roles=qrule['primary_roles']; sj=[j for j in jobs if j['primary_status']=='CODED' and j['primary_code'] in roles]
 allow={'CODED','NOT_MENTIONED','UNMAPPED'};sf={'skills':'skills_status','technical_concepts':'technical_status'}
 base=[dict(identity_key=j['identity_key'],record_id=j['record_id'],reading_id=j['reading_id'],company_id=j['company_id'],role_code=j['primary_code'],dimension=d,dimension_status=j[sf[d]],base_eligible='YES' if j[sf[d]] in allow else 'NO',scope_main_company=cb[j['company_id']]['scope_main_company']) for j in sj for d in sf]
 assert {r['dimension_status'] for r in base}<=allow|{'SOURCE_UNASSESSABLE'}
 table('T3_base_admission.csv',base)
 labels={}
 for r in items:labels[(r['role_code'],r['dimension'],r['label_code'])]=r['label_name']
 mainset={(r['role_code'],r['dimension'],r['label_code']) for r in selected if r['main_display']=='YES'}
 slices=[(m,b) for m in qrule['positive_buckets'] for b in (['UNCONDITIONAL'] if m.startswith('DUTY_') else ['UNCONDITIONAL','CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE'])]
 qc=[];trace=[];states={};n_unknown_cells=0
 for (role,dim,label),name in sorted(labels.items()):
  eligible=[j for j in sj if j['primary_code']==role and j[sf[dim]] in allow]
  for metric,branch in slices:
   sk=(role,dim,label,metric,branch);ss={j['identity_key']:rules.label_state(bylabel[(j['identity_key'],dim,label)],metric,branch) for j in eligible};states[sk]=ss
   for ident,state in ss.items():
    if state=='NO_RECORDED_POSITIVE':continue
    j=byid[ident];trace.append(dict(identity_key=ident,record_id=j['record_id'],reading_id=j['reading_id'],company_id=j['company_id'],role_code=role,dimension=dim,label_code=label,metric_bucket=metric,branch_bucket=branch,state=state))
   for c in companies:
    cj=[j for j in eligible if j['company_id']==c];ct=Counter(ss[j['identity_key']] for j in cj);den=ct['PRESENT']+ct['NO_RECORDED_POSITIVE']
    qc.append(dict(company_id=c,company_name=cb[c]['company_name'],stratum=cb[c]['stratum'],role_code=role,dimension=dim,label_code=label,label_name=name,main_display='YES' if (role,dim,label) in mainset else 'NO',metric_bucket=metric,branch_bucket=branch,n_positive=ct['PRESENT'],n_base=len(cj),n_relation_unknown=ct['UNKNOWN'],n_interpretable=den,share=ratio(ct['PRESENT'],den),small_n_under10='YES' if 0<den<10 else 'NO',n_source_unassessable=sum(j['primary_code']==role and j[sf[dim]]=='SOURCE_UNASSESSABLE' for j in jc[c])))
 table('T3_company_context.csv',qc);table('T3_positive_unknown_lineage.csv',trace)
 # Zero cells are the base_admission complement of PRESENT/UNKNOWN; never split identity keys.
 table('T3_all_item_semantics.csv',items)
 groups={'WHOLE23':whole,'ALL24_TEAM_SENSITIVITY':set(companies)}
 groups.update({g:{c for c in companies if cb[c]['stratum']==g} for g in sorted({r['stratum'] for r in cs})})
 for country in sorted({r['country'] for r in cs}):groups['SYSTEM_PRODUCTS_'+country]={c for c in companies if cb[c]['stratum']=='SYSTEM_PRODUCTS' and cb[c]['country']==country}
 def aggregate(sk,members,variant='BASE'):
  role,dim,label,metric,branch=sk
  ids=[a for a in states[sk] if byid[a]['company_id'] in members and (variant!='CATALOG_DIRECT' or byid[a][sf[dim]]!='UNMAPPED')]
  if variant=='EXCLUDE_MULTI_PRODUCT':ids=[a for a in ids if cb[byid[a]['company_id']]['known_multi_product']!='YES']
  if variant=='EXCLUDE_MEDIA_ONLY':ids=[a for a in ids if cb[byid[a]['company_id']]['media_only_basis']!='YES']
  den=Counter(byid[a]['company_id'] for a in ids if states[sk][a]!='UNKNOWN');num=Counter(byid[a]['company_id'] for a in ids if states[sk][a]=='PRESENT');n=sum(den.values());nc=len(den)
  return dict(n_base=len(ids),n_relation_unknown=len(ids)-n,n_interpretable=n,n_positive=sum(num.values()),n_companies=nc,n_companies_ge10=sum(v>=10 for v in den.values()),largest_company_share=ratio(max(den.values(),default=0),n),share_ad_weighted=ratio(sum(num.values()),n),share_company_equal=round(sum(num[c]/d for c,d in den.items())/nc,10) if nc else '',gate='PASS' if nc>=3 and n>=20 else 'POINTS_ONLY',eligible_companies_json=json.dumps(sorted(den),ensure_ascii=False))
 ag=[];sens=[];loo=[]
 for sk in sorted(states):
  role,dim,label,metric,branch=sk
  key=dict(role_code=role,dimension=dim,label_code=label,label_name=labels[(role,dim,label)],main_display='YES' if (role,dim,label) in mainset else 'NO',metric_bucket=metric,branch_bucket=branch)
  for group,members in groups.items():
   out=aggregate(sk,members);case=group in ['TEAM_SEPARATE','COMPONENT_SYSTEM_PORTFOLIO','ROBOT_OPERATED_SERVICE']
   permitted=out['gate']=='PASS' and not case
   ag.append(key|dict(group=group,display_status='EXPLORATORY_SUMMARY' if permitted else 'CASE_POINTS_ONLY',dominance_warning='YES' if out['largest_company_share']!='' and out['largest_company_share']>.5 else 'NO')|out|dict(share_ad_weighted=out['share_ad_weighted'] if permitted else '',share_company_equal=out['share_company_equal'] if permitted else ''))
   if key['main_display']=='YES' and group in ['WHOLE23','SYSTEM_PRODUCTS','CROSS_BODY_MODELS']:
    for c in sorted(members):
     if not any(byid[a]['company_id']==c for a in states[sk]):continue
     s=aggregate(sk,members-{c});show=s['gate']=='PASS'
     loo.append(key|dict(group=group,removed_company=c)|s|dict(share_ad_weighted=s['share_ad_weighted'] if show else '',share_company_equal=s['share_company_equal'] if show else ''))
  if key['main_display']=='YES':
   for var in ['BASE','CATALOG_DIRECT','EXCLUDE_MULTI_PRODUCT','EXCLUDE_MEDIA_ONLY']:
    sens.append(key|dict(group='WHOLE23',variant=var)|aggregate(sk,whole,var))
 table('T3_aggregates.csv',ag);table('T3_scope_sensitivity.csv',sens);table('T3_leave_one_company_out.csv',loo)
 separate=defaultdict(set)
 for r in items:
  if r['metric_bucket']=='SEPARATE_NOT_POSITIVE':separate[(r['role_code'],r['dimension'],r['label_code'],r['label_name'],r['context'],r['use'],r['mention_relation'],r['branch_bucket'])].add(r['identity_key'])
 table('T3_separate_context_mentions.csv',[dict(role_code=k[0],dimension=k[1],label_code=k[2],label_name=k[3],context=k[4],use=k[5],mention_relation=k[6],branch_bucket=k[7],n_ads=len(ids),n_companies=len({byid[a]['company_id'] for a in ids}),ad_ids_json=json.dumps(sorted(ids),ensure_ascii=False),scope='ALL24',interpretation='已记录语境提及次数按广告去重，不是本人使用率或任职要求率') for k,ids in sorted(separate.items())])
 unmapped=[r for r in read(A/'unmapped_mentions.csv') if r['identity_key'] in {j['identity_key'] for j in sj}]
 table('T3_selected_role_unmapped_mentions.csv',unmapped)
 # Q3 activity relations are OWNED and PARTICIPATES; use dimension assessability, not primary class.
 acts=read(ROOT/'inputs/stage_a_extra/activities.csv');assert {r['relation'] for r in acts}=={'OWNED','PARTICIPATES'}
 anames={r['label_code']:r['label_name'] for r in acts};apairs=defaultdict(set)
 for r in acts:
  assert byid[r['identity_key']]['activities_status'] in allow
  apairs[(r['label_code'],r['relation'])].add(r['identity_key']);apairs[(r['label_code'],'ANY_RECORDED')].add(r['identity_key'])
 aq=[]
 for c in companies:
  eligible={j['identity_key'] for j in jc[c] if j['activities_status'] in allow}
  for label,name in anames.items():
   for rel in ['OWNED','PARTICIPATES','ANY_RECORDED']:
    positive=eligible&apairs[(label,rel)]
    aq.append(dict(company_id=c,company_name=cb[c]['company_name'],label_code=label,label_name=name,relation=rel,n_positive=len(positive),n_all_ads=len(jc[c]),n_source_unassessable=len(jc[c])-len(eligible),n_assessable=len(eligible),share=ratio(len(positive),len(eligible)),small_n_under10='YES' if len(eligible)<10 else 'NO'))
 table('T4_activity_company.csv',aq)
 activity_agg=[]
 for scope,members in [('ALL24',set(companies)),('WHOLE23',whole)]:
  for label,name in anames.items():
   for rel in ['OWNED','PARTICIPATES','ANY_RECORDED']:
    rows=[r for r in aq if r['company_id'] in members and r['label_code']==label and r['relation']==rel];n=sum(r['n_positive'] for r in rows);d=sum(r['n_assessable'] for r in rows)
    activity_agg.append(dict(scope=scope,label_code=label,label_name=name,relation=rel,n_positive=n,n_assessable=d,n_companies=sum(r['n_assessable']>0 for r in rows),share_ad_weighted=ratio(n,d),share_company_equal=round(sum(r['n_positive']/r['n_assessable'] for r in rows if r['n_assessable'])/sum(r['n_assessable']>0 for r in rows),10)))
 table('T4_activity_aggregates.csv',activity_agg)
 table('T4_activity_lineage.csv',[{k:r[k] for k in ['identity_key','record_id','reading_id','company_id','label_code','label_name','relation','quote','field','start','end']} for r in acts])
 table('T4_activity_admission.csv',[{k:j[k] for k in ['identity_key','record_id','reading_id','company_id','activities_status']}|{'base_eligible':'YES' if j['activities_status'] in allow else 'NO'} for j in jobs])
 cross=[]
 for code,(name,kind) in cats.items():
  ids={j['identity_key'] for j in jobs if classof(j)==code and j['activities_status'] in allow}
  for label,an in anames.items():
   for rel in ['OWNED','PARTICIPATES']:
    pos=ids&apairs[(label,rel)];cross.append(dict(primary_code=code,primary_name=name,activity_code=label,activity_name=an,relation=rel,n_positive=len(pos),n_assessable=len(ids),share=ratio(len(pos),len(ids))))
 table('T4_primary_activity_cross.csv',cross)
 structures=[json.loads(x) for x in (A/'relations.jsonl').read_text(encoding='utf-8').splitlines() if json.loads(x)['kind']=='role_structure']
 st=[];nodes=[]
 def traverse(node,parent,anc,out):
  rel=node['relation']; nid=node['node_id'];path=anc+[rel]
  out.append(dict(node_id=nid,parent_id=parent,relation=rel,ancestor_relations_json=json.dumps(anc),function_code=node.get('function',''),duties_status=node.get('duties_status',node.get('duty_status','')),raw_node_json=json.dumps(node,ensure_ascii=False)))
  for child in node.get('children',[]):traverse(child,nid,path,out)
 for r in structures:
  j=byid[r['identity_key']];tree=r['tree_json'];tree=json.loads(tree) if isinstance(tree,str) else tree
  # Original nodes and full expression are kept verbatim. No flattening of choice branches.
  ns=r['nodes']; roles_ns=[n for n in ns if n['relation']=='ROLE'];mixed=any(n['relation'] in ['ALL','OR'] and n['relation']!=r['root_relation'] for n in ns)
  st.append(dict(identity_key=r['identity_key'],record_id=j['record_id'],reading_id=j['reading_id'],company_id=j['company_id'],company_name=cb[j['company_id']]['company_name'],title=j['title'],root_relation=r['root_relation'],n_role_nodes=len(roles_ns),has_mixed_branch='YES' if mixed else 'NO',primary_code=j['primary_code'],tree_json=json.dumps(tree,ensure_ascii=False)))
  for n in ns:nodes.append(dict(identity_key=r['identity_key'],reading_id=j['reading_id'],company_id=j['company_id'],root_relation=r['root_relation'],**{k:n.get(k,'') for k in ['node_id','parent_id','relation','function','duties_status','duty_status','quote','raw_json']}))
 table('T4_role_structures.csv',st);table('T4_role_structure_nodes.csv',nodes)
 structures_company=[]
 for c in companies:
  rows=[r for r in st if r['company_id']==c]
  structures_company.append(dict(company_id=c,company_name=cb[c]['company_name'],n_all_ads=len(jc[c]),n_compound=sum(r['root_relation']=='ALL' for r in rows),n_alternative=sum(r['root_relation']=='OR' for r in rows),n_mixed=sum(r['has_mixed_branch']=='YES' for r in rows)))
 table('T4_role_structure_company.csv',structures_company)
 # Direction appearances: an ad may appear in multiple functions, with no headcount meaning.
 appearances=defaultdict(set)
 for r in nodes:
  if r['relation']=='ROLE':appearances[(r['root_relation'],r['function'])].add(r['identity_key'])
 table('T4_structure_function_appearances.csv',[dict(root_relation=rt,function_code=fn,n_ads=len(ids),ad_ids_json=json.dumps(sorted(ids),ensure_ascii=False)) for (rt,fn),ids in sorted(appearances.items())])
 summary=dict(n_ads=len(jobs),n_companies=len(cs),n_whole_company_ads=sum(len(jc[c]) for c in whole),primary_counts=dict(Counter(classof(j) for j in jobs)),activity_status=dict(Counter(j['activities_status'] for j in jobs)),activity_items=len(acts),activity_relations=dict(Counter(r['relation'] for r in acts)),structures=len(st),structure_roots=dict(Counter(r['root_relation'] for r in st)),mixed_structures=sum(r['has_mixed_branch']=='YES' for r in st),structure_nodes=len(nodes),structure_role_nodes=sum(r['relation']=='ROLE' for r in nodes),q2_roles=dict(Counter(j['primary_code'] for j in sj)),q2_label_pairs=len(labels),q2_main_label_pairs=len(mainset),q2_item_rows=len(items),q2_positive_unknown_rows=len(trace),q2_company_cells=len(qc),q2_aggregate_cells=len(ag),q2_loo_rows=len(loo),table_rows={p.name:len(read(p)) for p in T.glob('*.csv')})
 dump(ROOT/'summary.json',summary);print(json.dumps(summary,ensure_ascii=False))
if __name__=='__main__':main()
