"""Targeted definition-consistency review: FAI is explicitly inside frozen catalog."""
from common import *
import copy, datetime
path=ROOT/'configs/Q_adjudications/RF_MANUFACTURING_QUALITY_SUPPLY.json'
hid='Q-M5-FAI-DEFINITION-20260916-04'
hp=ROOT/'notes'/(hid+'.json')
assert not hp.exists(), 'One-time revision; inspect existing history'
data=json.loads(path.read_text(encoding='utf-8'))
before={r:copy.deepcopy(data['ads'][r]) for r in ['N1021','N0850','N0966','N1017']}
data['ads']['N1021']['new']['5']=[['V2_APQP_PPAP','DUTY_OWN_DEVELOP','EXAMPLE'],['V2_APQP_PPAP','DUTY_OWN_USE','EXAMPLE']]
data['ads']['N0850']['new']['3']=[['V2_APQP_PPAP','SEPARATE','COLLABORATION_OBJECT']]
def add(rid,metric,branch,quote,reason):
 x=dict(code='V2_APQP_PPAP',metric=metric,branch=branch,quote=quote,reason=reason)
 assert locate(data['ads'][rid]['identity_key'],x)['method']!='UNRESOLVED_LOCATION'
 data['ads'][rid].setdefault('additions',[]).append(x)
add('N0966','DUTY_OWN_USE','UNCONDITIONAL','Own first-article and process validation for critical purchased parts; qualify new and dual-source suppliers with capability evidence, not paperwork.','冻结目录明确包含首件检验；补入本人承担')
add('N0966','REQUIRED','UNCONDITIONAL','Deep working knowledge of GD&T, measurement systems analysis, process capability, first-article inspection, and process validation.','既读Required资格中的首件检验知识；与同句MSA保持要求语境一致')
add('N1017','SEPARATE','COLLABORATION_OBJECT','Uphold dimensional accuracy, surface finish, and part integrity standards for all machined hardware; partner with Quality Control on inspection protocols, first-article processes, and nonconformance disposition.','与质控合作首件流程，不升级独立承担')
for rid in before:
 data['ads'][rid]['notes']+=' 本轮FAI定义核对修订：冻结目录V2_APQP_PPAP明确含FAI/首件检验，早先不等同PPAP而排除的理由撤销；子型保持FAI，不称其为PPAP。见'+hid+'。'
 data['ads'][rid]['updated_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
after={r:copy.deepcopy(data['ads'][r]) for r in before}
save_json('notes/'+hid+'.json',dict(review='TARGETED_NOT_FULL_SECOND_PASS',scope_coded_ads=175,definition='明确质量策划、生产件批准或首件检验流程',reviewed_hits=['E0355','N0193','N0203','N0254','E0381','N0966','N1017','N1021','N0850'],unchanged_reason={'N0193':'推动首件/试装/试测问题闭环，未明确首件检验流程；不以首件词面自动补入','E0381':'斜杠分支未知保留','E0355':'已纳入','N0203':'已纳入','N0254':'已纳入'},before=before,after=after))
path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(hid,'4 ads revised')
