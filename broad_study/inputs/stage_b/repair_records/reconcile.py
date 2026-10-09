from bootstrap import *
import csv
def rows(p):return list(csv.DictReader(Path(p).open(encoding='utf-8-sig',newline='')))
baseline=read(RUN/'work/evidence_identity_baseline.json')
for e in rows(OLD/'company_evidence.csv'):
 if e['evidence_id']=='B_US_FIGURE_004':continue
 baseline['entries'][e['evidence_id']]={'company_id':e['company_id'],'url':e['url']}
for cid,eid in [('CN_XSQUARE','B_CN_XSQUARE_006'),('US_AMAZON_FTR','B_US_AMAZON_FTR_004')]:
 p=RUN/f'work/pilot_facts_{cid}.json';obj=read(p);d=obj.get('companies',[obj])[0]
 e=next(e for e in d['evidence'] if e['evidence_id']==eid);e['url']=baseline['entries'][eid]['url'];save(p,obj)
save(RUN/'work/evidence_identity_baseline.json',baseline)
rules=read(RUN/'work/grouping_rules_source.json')
labels={'CN_NOETIX':'DONATION_DELIVERY','US_FIGURE':'CUSTOMER_CONFIRMED_F02_USE','US_BOSTON_DYNAMICS':'CUSTOMER_CONFIRMED_STRETCH_USE'}
for f in rows(RUN/'company_facts.csv'):
 label=None
 if f['field']=='deployment_status_actual' and f['company_id'] in labels:label='F03_ARRIVAL_SELF_REPORT' if f['fact_seq']=='2' else labels[f['company_id']]
 if f['field']=='product_lines' and f['company_id']=='CN_SPIRITAI' and f['fact_seq']=='2':label='MOZ1_LAUNCH_DATE_CONFLICT'
 if label:
  for dim in rules['dimensions']:
   if dim['dimension']==f['field']:dim['group_bindings'].setdefault(f['company_id'],{})[f['value']]=[label]
save(RUN/'work/grouping_rules_source.json',rules)
print('Pinned identities reconciled to prior published evidence, new scoped group labels declared')
