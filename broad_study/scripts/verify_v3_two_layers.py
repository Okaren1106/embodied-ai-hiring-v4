from common import *
import sqlite3
db=sqlite3.connect(':memory:')
db.executescript('CREATE TABLE ev(k TEXT, code TEXT, metric TEXT, branch TEXT); CREATE TABLE members(scenario TEXT,role TEXT,task TEXT,k TEXT,co TEXT);')
ev=[(e['identity_key'],e['code'],e['metric'],e['branch']) for e in read(ROOT/'tables/Q3_evidence_final.csv') if e.get('excluded_from_catalog')!='True']
db.executemany('INSERT INTO ev VALUES (?,?,?,?)',ev)
mm=read(ROOT/'tables/V3_two_layer_membership.csv')
db.executemany('INSERT INTO members VALUES (?,?,?,?,?)',[(x['scenario'],x['role'],x['task'],x['identity_key'],x['company_id']) for x in mm])
db.executescript('CREATE INDEX ix_ev ON ev(k,code); CREATE INDEX ix_mem ON members(k);')
qual="('DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED')"
selects={'P':f'metric IN {qual}','DUTY_ANY':"metric IN ('DUTY_OWN_USE','DUTY_OWN_DEVELOP')",'clear_relation_mention':f"metric IN {qual} AND branch!='UNRESOLVED'",'has_unresolved_branch':f"metric IN {qual} AND branch='UNRESOLVED'"}
for m in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED']:
 selects[m]=f"metric='{m}'";selects[m+'_UNCONDITIONAL']=f"metric='{m}' AND branch='UNCONDITIONAL'"
for b in ['CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','CONDITIONAL']:selects[b]=f"metric IN {qual} AND branch='{b}'"
sql='SELECT m.scenario,m.role,m.task,e.code,m.co,'+','.join(f'COUNT(DISTINCT CASE WHEN {v} THEN m.k END)' for v in selects.values())+' FROM members m JOIN ev e ON e.k=m.k GROUP BY m.scenario,m.role,m.task,e.code,m.co'
want={tuple(x[:5]):dict(zip(selects,x[5:])) for x in db.execute(sql)}
n=0
for r in read(ROOT/'tables/V3_two_layer_company_points.csv'):
 key=(r['scenario'],r['role'],r['task'],r['label_code'],r['company_id']);w=want.get(key,{})
 for c in selects:assert int(r[c])==w.get(c,0),(key,c,r[c],w.get(c,0));n+=1
 assert int(r['total_ads'])==sum(int(r[x]) for x in ['P','U','Z','NA','SOURCE_EXCLUDED'])
 assert int(r['P'])==int(r['N'])-int(r['Z'])
 assert int(r['DUTY_ANY'])<=int(r['DUTY_PLUS_COLLAB_CONTACT'])<=int(r['total_ads'])
ad={r['identity_key']:r for r in read(ROOT/'tables/Q3_ads_final.csv')}
for x in mm:
 a=ad[x['identity_key']];assert x['role']==a['role'] and a['company_id'] in WHOLE
 assert a['task']==x['task'] or (x['scenario']=='PLUS_SECONDARY' and a['secondary_task']==x['task'])
save_json('verification/V3_two_layer_independent_sql.json',dict(status='PASS',method='Independent SQLite DISTINCT ad counts for term mentions, five contexts and branch forms; membership and denominator invariants',scalar_checks=n,membership_rows=len(mm)))
print('PASS',n,'SQL counts')
