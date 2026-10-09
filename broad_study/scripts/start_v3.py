from pathlib import Path
from datetime import datetime,timezone
import shutil,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
PREV=ROOT.parent/'run_20260916_astra_m5_m6_final'
REPO=ROOT.parents[3]
assert not (ROOT/'RUN_STATE.json').exists(),'Already started; do not reset.'
for folder in ['inputs','configs','notes','review','scripts']:
 shutil.copytree(PREV/folder,ROOT/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
for folder in ['tables','reports','verification','baseline_v2']:(ROOT/folder).mkdir(exist_ok=True)
for p in (PREV/'tables').glob('*.csv'):
 if p.name.startswith(('Q4_','Q5_')) or p.name in ['Q3_states_final.csv','Q3_states_partial.csv','Q3_ad_label_states_partial.csv']:continue
 if p.name in ['Q3_ads_final.csv','Q3_evidence_final.csv','Q3_review_receipts.csv','Q3_astra_changes.csv']:
  shutil.copy2(p,ROOT/'baseline_v2'/p.name)
 else:shutil.copy2(p,ROOT/'tables'/p.name)
for n in ['input_manifest.json']:shutil.copy2(PREV/n,ROOT/n)
for n in ['REPORT_Astra_final.md','FINAL_DELIVERY.json','publication_manifest.json']:shutil.copy2(PREV/n,ROOT/'baseline_v2'/n)
for n in ['measurement_rules_v0.7.4.yaml','measurement_rules_v0.7.5.yaml']:
 shutil.copy2(REPO/'configs'/n,ROOT/'inputs'/n)
userreview=Path(r'C:/Users/bestl/.codex/attachments/a9e2864b-ffea-44e6-9c74-7b03b69406ec/pasted-text.txt')
shutil.copy2(userreview,ROOT/'inputs/user_review_20260917.txt')
now=datetime.now(timezone.utc).isoformat()
state=dict(author='Astra',version='core-Q2-v3',started_utc=now,status='IN_PROGRESS',previous=str(PREV),authorization='用户同意按六步顺序完成；保留全17职能验收目标。',steps={str(i):'IN_PROGRESS' if i==1 else 'PENDING' for i in range(1,7)},baseline=dict(ads=1576,full_reviews=181,changes=800,pending_union=1047),constraints=['不改冻结主分类、研究库及A/B/C','不覆盖旧交付','不扩公司、不恢复采集','语义与数值验收分开','不凭队列成员身份登记复核完成'])
(ROOT/'RUN_STATE.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
for q in [REPO.parent/'必读.md',REPO/'必读.md']:
 s=q.read_text(encoding='utf-8');rest=s[s.index('## 最新结果入口'):]
 head='# 当前进度 Astra按六步顺序执行核心研究修订与Q2验收\n\n更新：2026-09-17。用户已同意依次完成概念与旧结论修订、修订影响表、同任务方法、Q2内容复核、要求方式深化及综合研究稿。当前执行目录：'+ROOT.relative_to(REPO).as_posix()+'。\n\n当前步骤1进行中；步骤2—6待执行。旧22页综合报告已封存，属于上一轮交付，Q2内容验收尚未全部完成。原17职能验收目标保留；当前待复核队列去重1,047条，其中含全部230条剩余预设抽样。停止线已取消。\n\n'
 q.write_text(head+rest,encoding='utf-8')
print(ROOT)
