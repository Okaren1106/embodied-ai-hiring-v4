from common import *
from datetime import datetime,timezone
import sys
milestone,status,note=sys.argv[1:4]
state=json.loads((ROOT/'RUN_STATE.json').read_text(encoding='utf-8'));state['milestones'][milestone]=status;state['updated_utc']=datetime.now(timezone.utc).isoformat();state['note']=note;save_json('RUN_STATE.json',state)
repo=ROOT.parents[3];workspace=repo.parent
done='、'.join(k for k,v in state['milestones'].items() if v=='COMPLETE');active='、'.join(k for k,v in state['milestones'].items() if v=='IN_PROGRESS') or '待接续'
for p in [workspace/'必读.md',repo/'必读.md']:
    old=p.read_text(encoding='utf-8');rest=old[old.index('## 最新结果入口'):]
    rest=rest.replace('尚未进行正式合并裁决。','三稿合并裁决已完成，见本轮R报告。') if state['milestones']['M1']=='COMPLETE' else rest
    head=f'# 当前进度 研究书v2执行中｜已完成{done}｜当前{active}\n\n更新：2026-09-16。用户已授权按研究书v2逐步执行全部工作。执行包为`reports/2026-09-14_company_data_analysis/stage_d_integrated_v2/run_20260916_astra_v2`。{note}\n\n里程碑：'+ '；'.join(k+'='+v for k,v in state['milestones'].items())+'。进度以RUN_STATE.json与各模块验收记录为准。原认可分类、研究库和A/B/C历史包不改，不增加公司或广告，周采关闭。\n\n'
    p.write_text(head+rest,encoding='utf-8')
assert (workspace/'必读.md').read_bytes()==(repo/'必读.md').read_bytes()
print(state['milestones'])
