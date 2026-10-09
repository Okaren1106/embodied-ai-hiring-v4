from common import *
import random
lock_check()
selected={k for k,j in J.items() if role(j) in CONCRETE}
coverage=[];pool=[];raw_items=read(A/'skills.csv')+read(A/'technical_concepts.csv');unmapped=read(A/'unmapped_mentions.csv')
for n,r in enumerate(raw_items):
    if r['identity_key'] in selected:pool.append(dict(candidate_id=f'Q_OLD_{n:05}',origin='ACCEPTED_TAG',identity_key=r['identity_key'],company_id=r['company_id'],role=role(J[r['identity_key']]),dimension=r['dimension'],label_code=r['label_code'],surface=r['quote'],context=r['context'],use=r['use'],mention_relation=r['mention_relation'],requirement_node_id=r['requirement_node_id'],raw_json=r['raw_json']))
for n,r in enumerate(unmapped):
    if r['identity_key'] in selected:pool.append(dict(candidate_id=f'Q_UNM_{n:05}',origin='DIRECTORY_UNMAPPED_MENTION',identity_key=r['identity_key'],company_id=r['company_id'],role=role(J[r['identity_key']]),dimension=r['dimension'],label_code='',surface=r['surface'],context=r['context'],use=r['use'],mention_relation=r['mention_relation'],requirement_node_id=r['requirement_node_id'],raw_json=r['raw_json']))
dump('tables/Q_candidate_mention_pool.csv',pool)
idx=defaultdict(list)
for r in unmapped:
    if r['identity_key'] in selected:idx[role(J[r['identity_key']]),r['surface']].append(r)
surface=[]
for (f,s),v in sorted(idx.items()):surface.append(dict(role=f,surface=s,n_ads=len({r['identity_key'] for r in v}),n_companies=len({r['company_id'] for r in v}),dimensions=js(sorted({r['dimension'] for r in v})),candidate_ids=js([f'Q_UNM_{unmapped.index(r):05}' for r in v]),ad_ids=js(sorted({r['identity_key'] for r in v}))))
dump('tables/Q_unmapped_surface_survey.csv',surface)
pilot=[];rng=random.Random(20260916)
priority=['RF_MANUFACTURING_QUALITY_SUPPLY','RF_HARDWARE_ELECTRICAL','RF_ML_AI_ENGINEERING','RF_ROBOTICS_SOFTWARE']+[f for f in CONCRETE if f not in ['RF_MANUFACTURING_QUALITY_SUPPLY','RF_HARDWARE_ELECTRICAL','RF_ML_AI_ENGINEERING','RF_ROBOTICS_SOFTWARE']]
for fi,f in enumerate(priority,1):
    kk=sorted(k for k in selected if role(J[k])==f);byc=defaultdict(list)
    for k in kk:byc[J[k]['company_id']].append(k)
    for c in sorted(byc):rng.shuffle(byc[c])
    cc=sorted(byc);rng.shuffle(cc);chosen=[];roundn=0
    while len(chosen)<min(20,len(kk)):
        for c in cc:
            if roundn<len(byc[c]):chosen.append(byc[c][roundn])
            if len(chosen)>=min(20,len(kk)):break
        roundn+=1
    for i,k in enumerate(chosen,1):pilot.append(dict(role=f,role_order=fi,pilot_order=i,identity_key=k,reading_id=J[k]['reading_id'],company_id=J[k]['company_id'],title=J[k]['title']))
    coverage.append(dict(role=f,role_name=RN[f],all24_ads=len(kk),all24_companies=len(byc),whole23_ads=sum(J[k]['company_id'] in WHOLE for k in kk),whole23_companies=len(set(byc)&set(WHOLE)),skills_source_eligible=sum(J[k]['skills_status']!='SOURCE_UNASSESSABLE' for k in kk),technical_source_eligible=sum(J[k]['technical_status']!='SOURCE_UNASSESSABLE' for k in kk),unmapped_mentions=sum(r['role']==f and r['origin']=='DIRECTORY_UNMAPPED_MENTION' for r in pool),pilot_ads=len(chosen),L0_status='COMPLETE',L1_status='PENDING_CATALOG_AND_CONTENT',L2_status='PENDING_TASK_COMPARABILITY',L3_status='CELL_SPECIFIC_PENDING'))
    out=['# '+f+' '+RN[f]]
    for i,k in enumerate(chosen,1):
        r=J[k];out.append(f"## {i} {r['reading_id']} {r['company_id']} {r['title']}\nidentity {k}")
        texts=[]
        for field in ['duties','requirements','full_description']:
            t=RAW[k].get(field,'') or ''
            if t and not any(t==old or t in old for old in texts):out.append('['+field+']\n'+t);texts.append(t)
    (ROOT/f'notes/Q_pilot_{fi:02d}.md').write_text('\n\n'.join(out),encoding='utf-8')
dump('tables/Q1_role_coverage.csv',coverage);dump('tables/Q_calibration_sample.csv',pilot)
# Raw ad frame is separate from mention pool, ensuring NOT_MENTIONED and no-hit ads remain in scope.
dump('tables/Q_full_ad_frame.csv',[{key:J[k][key] for key in ['identity_key','reading_id','company_id','title','primary_code','skills_status','technical_status','observation_date']} for k in sorted(selected)])
save_json('notes/Q_preparation_summary.json',{'all_concrete_ads':len(selected),'candidate_mentions':len(pool),'unique_unmapped_role_surfaces':len(surface),'pilot_ads':len(pilot),'raw_unmapped_ads':len({r['identity_key'] for r in unmapped}),'unmapped_ads_with_CODED_skills':len({r['identity_key'] for r in unmapped if J[r['identity_key']]['skills_status']=='CODED'}),'method':'Candidate pool is an inventory, not completed coding. All raw full texts retained; no keyword-positive inference.'})
print('Q prepare',len(selected),'ads',len(pool),'candidate mentions',len(pilot),'calibration sample');print('pilot files',[(p.name,p.stat().st_size) for p in sorted((ROOT/'notes').glob('Q_pilot_*.md'))])
