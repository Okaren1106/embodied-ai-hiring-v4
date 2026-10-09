"""Correct a homonymous course-project/curriculum label found in targeted review."""
from common import *
from copy import deepcopy
from datetime import datetime,timezone
rid='N0446';revision_id='Q-M5-CURRICULUM-HOMONYM-20260916-07'
hp=ROOT/'notes'/f'{revision_id}.json'
assert not hp.exists()
p=ROOT/'configs/Q_adjudications/RF_HARDWARE_ELECTRICAL.json'
d=json.loads(p.read_text(encoding='utf-8'));a=d['ads'][rid]
removed=[x for x in a['additions'] if x['code']=='SK_CURRICULUM']
assert len(removed)==1
quote=removed[0]['quote'];assert locate(a['identity_key'],dict(quote=quote))['method']!='UNRESOLVED_LOCATION'
a['additions']=[x for x in a['additions'] if x['code']!='SK_CURRICULUM']
a.setdefault('outside_extra',[]).append(dict(quote=quote,description='课程设计此处指学生工程课程项目经历，不是设计课程体系/课程开发能力；按冻结SK_CURRICULUM的培训课程用途示例排除同形异义。'))
a['notes']+=' 定向回查：学生课程项目经历不能按同词面标SK_CURRICULUM课程体系设计。'
a['updated_utc']=datetime.now(timezone.utc).isoformat()
history=dict(revision_id=revision_id,reviewer='Astra',created_utc=a['updated_utc'],coded_ads_at_review=251,scope='All coded ads with 课程设计 text or SK_CURRICULUM evidence; targeted homonym check, not full QC',reviewed_ids=['N0444','N0446','N0468'],removed_addition=removed,changed_ids=['N0446'],keep_decisions={'N0444':'项目开发经历中的课程设计，不补课程开发专业能力','N0468':'课程设计/电子竞赛经历，不补课程开发专业能力'},original_and_frozen_catalog_unchanged=True)
hp.write_text(json.dumps(history,ensure_ascii=False,indent=2),encoding='utf-8')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(revision_id,'1 homonym correction; 3 ads reviewed; full QC pending')

