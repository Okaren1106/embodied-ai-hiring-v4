from common import *
from itertools import combinations,product
import math
lock_check()
TARGETS=[('D_MAIN','CN_GALBOT','US_FIGURE'),('D_LIMITED','CN_AGIBOT','CN_GALBOT'),('D_NA_1','US_NIMBLE','US_DEXTERITY'),('D_NA_2','US_AGILITY','US_NIMBLE')]
NR={(c,f):len({k for k in ids([c],True) if role(J[k])==f}) for c in WHOLE for f in CONCRETE}
qual=[]
for a,b in combinations(WHOLE,2):
    K=[f for f in CONCRETE if NR[a,f]>=10 and NR[b,f]>=10]
    qual.append(dict(company_a=a,company_b=b,K_json=js(K),n_K=len(K),eligible=len(K)>=2,technical_K=len([f for f in K if f!='RF_CORPORATE_SUPPORT']),A_K_N=sum(NR[a,f] for f in K),A_total_N=len(ids([a],True)),B_K_N=sum(NR[b,f] for f in K),B_total_N=len(ids([b],True)),note='Qualification only, not ranked by differences'))
assert len(qual)==253;dump('tables/D1_all_pair_qualification.csv',qual)
# Exact explicit-audience text filter, not latent seniority. Keep every trigger for review.
aud=[];dropaud=set();aud_rejected=[]
aud_config=json.loads((ROOT/'configs/audience_adjudication.json').read_text(encoding='utf-8'))
for k,j in J.items():
    title=j['title'];titlehit=re.search(r'实习|校招|\d{2,4}\s*届|\bintern(?:ship)?\b',title,re.I)
    evidence=[]
    if titlehit:evidence.append({'field':'title','quote':title,'reason':'EXPLICIT_TITLE'})
    for f in ['duties','requirements','full_description']:
        t=RAW[k].get(f,'') or ''
        for ln in t.splitlines():
            if re.search(r'应届|校招|\bnew graduate\b|\brecent graduate\b',ln,re.I):evidence.append({'field':f,'quote':ln,'reason':'EXPLICIT_ELIGIBILITY_NOT_EXCLUSIVITY'})
    if evidence:
        if j['reading_id'] in aud_config['false_positive_reading_ids']:
            aud_rejected.append(dict(identity_key=k,reading_id=j['reading_id'],reason=aud_config['false_positive_reading_ids'][j['reading_id']],evidence_json=js(evidence)))
            continue
        dropaud.add(k);aud.append(dict(identity_key=k,company_id=j['company_id'],reading_id=j['reading_id'],title=title,evidence_json=js(evidence),rule='Explicit text only; may include experienced candidates'))
dump('tables/D_explicit_audience_exclusions.csv',aud)
dump('tables/D_audience_false_positive_review.csv',aud_rejected)
clusters=defaultdict(list)
for k,j in J.items():
    t=re.sub(r'\s+',' ',RAW[k].get('duties') or RAW[k].get('full_description') or '').strip();clusters[j['company_id'],role(j),t if t else k].append(k)
keep={sorted(v)[0] for v in clusters.values()};dups=[dict(company_id=c,role=f,retained_id=sorted(kk)[0],all_ids_json=js(sorted(kk)),n=len(kk),duty_hash=hashlib.sha256(t.encode()).hexdigest()) for (c,f,t),kk in clusters.items() if len(kk)>1]
dump('tables/D_exact_duplicate_groups.csv',dups)
member=read(ROOT/'tables/R_source_membership.csv');SC={s:{r['identity_key'] for r in member if r['scope']==s} for s in ['S1_ACTIVITY_COMPLETE','S2_SOURCE_QUALITY','S3_SOURCE_QUALITY_LENGTH200']}
SC.update(MAIN=set(J),NO_EXPLICIT_CAMPUS_OR_INTERN=set(J)-dropaud,EXACT_DUTY_DEDUP=keep)
parts=[];results=[];outside=[];standard=[];bounds=[];membership=[];checks=[]
def calc(n1,n2,p1,p2):
    s1=[x/sum(n1) for x in n1];s2=[x/sum(n2) for x in n2];q1=[p/n for p,n in zip(p1,n1)];q2=[p/n for p,n in zip(p2,n2)]
    r1=sum(s*q for s,q in zip(s1,q1));r2=sum(s*q for s,q in zip(s2,q2));C=[(a-b)*(x+y)/2 for a,b,x,y in zip(s1,s2,q1,q2)];W=[(x-y)*(a+b)/2 for a,b,x,y in zip(s1,s2,q1,q2)]
    return r1,r2,C,W,s1,s2,q1,q2
for case,a,b in TARGETS:
    fixed=[f for f in CONCRETE if NR[a,f]>=10 and NR[b,f]>=10]
    for sn,allowed in SC.items():
        current=[f for f in CONCRETE if all(len({k for k in ids([c],True)&allowed if role(J[k])==f})>=10 for c in [a,b])]
        for mode,K in [('FIXED_K',fixed),('REBUILT_K_DIFFERENT_ESTIMAND',current)]:
            available={c:ids([c],True)&allowed for c in [a,b]};total={c:ids([c])&allowed for c in [a,b]};sets={c:{f:{k for k in available[c] if role(J[k])==f} for f in K} for c in [a,b]};full={c:{f:{k for k in total[c] if role(J[k])==f} for f in K} for c in [a,b]};n={c:[len(sets[c][f]) for f in K] for c in [a,b]}
            flag='NA_K_LESS_THAN_TWO' if len(K)<2 else 'NA_ZERO_CELL' if min(n[a]+n[b])==0 else 'DIAGNOSTIC_CELL_UNDER10' if min(n[a]+n[b])<10 else 'ELIGIBLE'
            for c in [a,b]:
                ins=set().union(*sets[c].values()) if K else set();outs=available[c]-ins
                for act in ACTS:outside.append(dict(case_id=case,scenario=sn,mode=mode,company_id=c,activity=act,K_json=js(K),K_N=len(ins),total_N=len(available[c]),coverage=ratio(len(ins),len(available[c])),outside_N=len(outs),outside_P=len(outs&OWN[act]),outside_rate=ratio(len(outs&OWN[act]),len(outs)),source_unassessable_total=len(total[c]-available[c]),source_unassessable_K=sum(len(full[c][f]-sets[c][f]) for f in K),primary_unassigned_source=sum(role(J[k]).startswith('STATUS_') for k in total[c]-available[c])))
            for act in ACTS:
                base=dict(case_id=case,company_a=a,company_b=b,scenario=sn,mode=mode,activity=act,K_json=js(K),K_added=js(sorted(set(K)-set(fixed))),K_removed=js(sorted(set(fixed)-set(K))),n_K=len(K),qualification=flag,A_K_N=sum(n[a]),B_K_N=sum(n[b]),A_total_N=len(available[a]),B_total_N=len(available[b]),A_coverage=ratio(sum(n[a]),len(available[a])),B_coverage=ratio(sum(n[b]),len(available[b])))
                if flag.startswith('NA'):
                    results.append({**base,'R_A':None,'R_B':None,'delta_pp':None,'composition_pp':None,'within_role_pp':None,'residual':None});continue
                p={c:[len(sets[c][f]&OWN[act]) for f in K] for c in [a,b]};z=calc(n[a],n[b],p[a],p[b]);ra,rb,cc,ww,sa,sb,qa,qb=z;delta=ra-rb;residual=delta-sum(cc)-sum(ww)
                assert abs(residual)<1e-10
                results.append({**base,'R_A':ra,'R_B':rb,'delta_pp':100*delta,'composition_pp':100*sum(cc),'within_role_pp':100*sum(ww),'residual':residual,'interpretation':'Arithmetic identity within K; not causal or business-model contributions'})
                for i,f in enumerate(K):
                    parts.append({**base,'role':f,'A_P':p[a][i],'A_N':n[a][i],'A_U_source':len(full[a][f]-sets[a][f]),'A_B_source_scenario':len(full[a][f]),'A_s':sa[i],'A_q':qa[i],'B_P':p[b][i],'B_N':n[b][i],'B_U_source':len(full[b][f]-sets[b][f]),'B_B_source_scenario':len(full[b][f]),'B_s':sb[i],'B_q':qb[i],'composition_pp':100*cc[i],'within_role_pp':100*ww[i]})
                for weight in ['OWN_K','EQUAL_K','POOLED_K']:
                    weights1=sa if weight=='OWN_K' else [1/len(K)]*len(K) if weight=='EQUAL_K' else [(x+y)/(sum(n[a])+sum(n[b])) for x,y in zip(n[a],n[b])];weights2=sb if weight=='OWN_K' else weights1
                    ar=sum(w*q for w,q in zip(weights1,qa));br=sum(w*q for w,q in zip(weights2,qb));standard.append({**base,'weight':weight,'A_rate':ar,'B_rate':br,'difference_pp':100*(ar-br)})
                # Validation with reversed labels, equal weights, identical rates and direct marginal sum.
                reverse=calc(n[b],n[a],p[b],p[a]);equal=calc([1]*len(K),[1]*len(K),qa,qb);samerate=calc(n[a],n[b],[x*y for x,y in zip(n[a],qa)],[x*y for x,y in zip(n[b],qa)])
                checks.append(dict(case_id=case,scenario=sn,mode=mode,activity=act,identity=abs(residual)<1e-10,swap=abs(sum(cc)+sum(reverse[2]))<1e-10 and abs(sum(ww)+sum(reverse[3]))<1e-10,equal_weights_C_zero=abs(sum(equal[2]))<1e-10,equal_rates_W_zero=abs(sum(samerate[3]))<1e-10,direct_total=abs(ra-sum(p[a])/sum(n[a]))<1e-10 and abs(rb-sum(p[b])/sum(n[b]))<1e-10))
                if mode=='FIXED_K' and sn=='MAIN':
                    for c in [a,b]:
                        for f in K:
                            membership.extend(dict(case_id=case,company_id=c,role=f,identity_key=k,reading_id=J[k]['reading_id']) for k in sorted(full[c][f])) if act==ACTS[0] else None
                    # Source-unknown assignment with fixed source bases and recomputed weights.
                    bn={c:[len(full[c][f]) for f in K] for c in [a,b]};u={c:[bn[c][i]-n[c][i] for i in range(len(K))] for c in [a,b]};saa=[v/sum(bn[a]) for v in bn[a]];sbb=[v/sum(bn[b]) for v in bn[b]]
                    baseline=calc(bn[a],bn[b],p[a],p[b]);basevals={'delta':baseline[0]-baseline[1],'composition':sum(baseline[2]),'within_role':sum(baseline[3])}
                    coefs={'delta':([1/sum(bn[a])]*len(K),[-1/sum(bn[b])]*len(K)),'composition':([(x-y)/2/v for x,y,v in zip(saa,sbb,bn[a])],[(x-y)/2/v for x,y,v in zip(saa,sbb,bn[b])]),'within_role':([(x+y)/2/v for x,y,v in zip(saa,sbb,bn[a])],[-(x+y)/2/v for x,y,v in zip(saa,sbb,bn[b])])}
                    for metric,(ca,cb) in coefs.items():
                        increments=[x*y for x,y in zip(ca+cb,u[a]+u[b])];lo=basevals[metric]+sum(min(0,x) for x in increments);hi=basevals[metric]+sum(max(0,x) for x in increments);bounds.append({**base,'metric':metric,'low_pp':100*lo,'high_pp':100*hi,'U_A_K':sum(u[a]),'U_B_K':sum(u[b]),'method':'Exact box extrema of linear q terms, weights based on B; all0/all1 are not presumed bounds','unknown_primary_note':'Unassigned primary roles are outside fixed K; cannot place them into K without new assumptions'})
dump('tables/D2_decomposition_role_parts.csv',parts);dump('tables/D2_decomposition_summary.csv',results);dump('tables/D2_K_membership.csv',membership);dump('tables/D2_K_outside_scope.csv',outside);dump('tables/D3_standardization_sensitivity.csv',standard);dump('tables/D3_unknown_assignment_bounds.csv',bounds)
assert all(all(r[k] for k in ['identity','swap','equal_weights_C_zero','equal_rates_W_zero','direct_total']) for r in checks);save_json('verification/D_algebra_checks.json',{'method':'Same researcher algebraic property checks','n_scenarios':len(checks),'checks':checks})
print('D main',js([r for r in results if r['scenario']=='MAIN' and r['mode']=='FIXED_K' and r['activity'] in ['ACT_ENGINEERING','ACT_DEPLOYMENT','ACT_QUALITY','ACT_RESEARCH']]));print('qualified pairs',sum(r['eligible'] for r in qual),'algebra scenarios',len(checks),'audience',len(aud))
