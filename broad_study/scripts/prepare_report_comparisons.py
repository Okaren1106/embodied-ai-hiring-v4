from common import *
def stream(n):
 with (ROOT/'tables'/n).open(encoding='utf-8-sig',newline='') as f:yield from csv.DictReader(f)
design=[
 ('RF_ML_AI_ENGINEERING','ROBOT_MODEL','SK_PYTHON'),
 ('RF_ROBOTICS_SOFTWARE','ROBOT_RUNTIME','SK_LINUX'),
 ('RF_ROBOTICS_SOFTWARE','ROBOT_RUNTIME','SK_CPP'),
 ('RF_HARDWARE_ELECTRICAL','BOARD_CIRCUIT','SK_PCB_DESIGN'),
 ('RF_MANUFACTURING_QUALITY_SUPPLY','PROCESS_BUILD','TC_MECHANICAL'),
 ('RF_CORPORATE_SUPPORT','HR','V2_HR')]
plans={a['role']:json.loads(a['prominent_companies_by_coverage']) for a in read(ROOT/'tables/Q1_prefixed_comparison_plan.csv')}
res=[]
for a in stream('Q4_task_company_points_final.csv'):
 if (a['role'],a['task'],a['label_code']) in design and a['metric']=='GENERAL' and a['branch']=='UNCONDITIONAL' and a['company_id'] in plans[a['role']]:
  a['company_name']=CO[a['company_id']]['company_name'];res.append(a)
dump('tables/Q5_prefixed_company_examples.csv',res)
for a in res:print(a['role'],a['task'],a['label_name'],a['company_name'],a['P']+'/'+a['N'],'U='+a['U'],'B='+a['B'])
ts=[]
for a in stream('Q4_task_strata_final.csv'):
 if (a['role'],a['task'],a['label_code']) in design and a['metric']=='GENERAL' and a['branch']=='UNCONDITIONAL':ts.append(a)
dump('tables/Q5_prefixed_task_examples.csv',ts)
print('TASK',js([{k:a[k] for k in ['role','task','label_code','P','U','N','gate']} for a in ts]))
