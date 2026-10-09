from astra_review_tools import *
tx=transactions();full={t['identity_key'] for t in tx if t['review_mode']=='FULL_SOURCE_AND_CODING'}
anyq={t['identity_key'] for t in tx if t['review_mode'] in ['FULL_SOURCE_AND_CODING','BOUNDARY_CONTEXTS']}
pending=(SAMPLE-full)|(set(MAND)-anyq)
progress=dict(full=len(full),new_full=len(full)-181,seed_done=len(full&SAMPLE),seed_total=len(SAMPLE),mandatory_done=len(set(MAND)&anyq),mandatory_total=len(MAND),pending_union=len(pending),
 role_full=dict(Counter(AD[k]['role'] for k in full)),role_pending=dict(Counter(AD[k]['role'] for k in pending)))
save_json('verification/V3_review_progress.json',progress)
state=json.loads((ROOT/'RUN_STATE.json').read_text(encoding='utf-8'));state['review_progress']=progress;state['updated_utc']=datetime.now(timezone.utc).isoformat();save_json('RUN_STATE.json',state)
workspace=next(p for p in ROOT.parents if (p/'embodied-ai-hiring-research').is_dir())
p=workspace/'必读.md';old=p.read_text(encoding='utf-8');history=old[old.index('## 历史成果与当前边界'):]
top=f'''# 当前进度 Astra按六步顺序执行核心研究修订与Q2验收

更新：2026-09-17。用户授权按六步完成；全17职能验收范围保留，停止线已取消。当前目录：`{ROOT.relative_to(workspace).as_posix()}`。

## 当前步骤与结果

1. 活动边界裁决已写入规则—原文—旧结论链。部署与维护标签历史适用不一致，撤回依赖其一致性的实质主结论，历史数字不删除、不冒称修好了全部活动编码。质量规则原本包含合规。
2. Grok至Astra上一版修订影响基线完成：800项涉及161条独立广告，不能作错误率；25914个同口径整公司语境格中1556格的计数、分母或门槛变化。最终V3增量需在内容复核后更新。
3. 主/次任务方法明确：主统计只用一个主任务，基线167条带次任务。板级电路基线整公司56条，旧文51是误用生产工艺分母。
4. Q2复核正在执行：累计全文复核{len(full)}/1576条（上一版181＋本版新增{len(full)-181}）；预设抽样{len(full&SAMPLE)}/340，强制队列{len(set(MAND)&anyq)}/1208，待办去重{len(pending)}条。没有凭脚本或队列身份虚记内容通过。
5. 同任务技术出现与要求方式两层分析待复核后重算。
6. 综合核心研究稿待更新和验收；旧22页报告封存，不能作为本版最终结果。

## 当前入口

- [活动边界裁决]({ROOT.as_posix()}/reports/V3_01_活动边界裁决.md)
- [修订影响基线]({ROOT.as_posix()}/reports/V3_02_修订影响.md)
- [同任务比较方法]({ROOT.as_posix()}/reports/V3_03_同任务比较方法.md)
- [实际状态]({ROOT.as_posix()}/RUN_STATE.json)
- 旧交付：`run_20260916_astra_m5_m6_final`，保持封存字节；其数字会由V3另版更新。

## 保持的研究范围

冻结24主体1654条，整公司23家1630条，FAR24条单列；Q2为17具体职能1576条，整公司1552条。没有扩公司、恢复周采、重做冻结主分類、改研究库或封存A/B/C。

84条对象研究保留，81条不能归属命名产品；四共同职能内银河通用减Figure工程活动差+11.10个百分点=构成+19.45与职能内−8.35，限于描述分解。研究和宽质量活动比例可沿用，部署活动数字仅列历史测量附录，不解释为客户现场率。

'''
for dest in [workspace/'必读.md',workspace/'embodied-ai-hiring-research/必读.md']:dest.write_text(top+history,encoding='utf-8')
print(js(progress))
