from bootstrap import *
import collections,csv,datetime
def rows(p):return list(csv.DictReader(Path(p).open(encoding='utf-8-sig',newline='')))
def md(n,s):(RUN/n).write_text(s.rstrip()+'\n',encoding='utf-8')
summary=read(RUN/'repair_records/data_summary.json');v=read(RUN/'verification.json');fault=read(RUN/'work/fault_probes.json');lock=read(RUN/'work/input_lock.json');rb=read(RUN/'work/rebuild_check.json');node=read(RUN/'work/html_runtime_checks.json');browser=read(REPO/'.b5repair/browser_check.json')
for n in ['browser_check.json','browser_noetix.png','browser_figure.png','prior_audit_regression.py','regression_context.py','browser_check.mjs']:
 if (REPO/'.b5repair'/n).exists():shutil.copy2(REPO/'.b5repair'/n,RUN/'repair_records'/n)
for n in ['bootstrap.py','patch_pipeline.py','ingest.py','finish_code.py','reconcile.py','refine_scopes.py','final_code_fix.py','summarize.py','finalize_docs.py']:
 shutil.copy2(REPO/'.b5repair'/n,RUN/'repair_records'/n)
before=read(RUN/'repair_records/protected_before.json');bad=[p for p,h in before.items() if not Path(p).is_file() or sha(p)!=h]
save(RUN/'repair_records/protected_final.json',{'n_files':len(before),'n_changed':len(bad),'changed':bad});assert not bad
priorfile=REPO/'.b5repair/audit_checks.json';prior=read(priorfile) if priorfile.exists() else None
if prior:shutil.copy2(priorfile,RUN/'repair_records/prior_audit_checks.json')
prior_text=f"原36项审计规则回归 {prior['n_pass']}/{prior['n_checks']}（本轮执行者参与修复，不冒称新的独立验收）" if prior else '原36项审计规则回归待执行'
archive=RUN/'repair_records/inherited_docs';archive.mkdir(exist_ok=True)
for p in RUN.glob('*.md'):
 if not (archive/p.name).exists():shutil.copy2(p,archive/p.name)
scope='REPAIRED_AND_EVIDENCE_INTEGRATED_PENDING_INDEPENDENT_ACCEPTANCE'
status={'status':scope,'stage_b_complete':False,'stage_c_started':False,'run':str(RUN),'previous_candidate':str(OLD),'self_check':{'pass':v['n_pass'],'total':v['n_checks']},'fault_probes':{'pass':fault['n_pass'],'total':fault['n_probes'],'positive_control':fault['positive_control_ok']},'node':node['summary'],'browser':{'pass':browser['n_pass'],'total':browser['n_checks']},'prior_audit_regression':None if not prior else {k:prior[k] for k in ['n_checks','n_pass','n_fail']},'six_tables_identical':rb['identical'],'protected_originals_unchanged':len(before),'data':summary,'limitation':'9张审阅卡采用WEB_TOOL_EXTRACT归档，未冒称保存原网页HTTP字节；现有完整原件仍保留。'}
save(RUN/'repair_status.json',status)
save(RUN/'analysis_manifest.json',{'stage':'B-evidence-integrated','scope':scope,'run_id':RUN.name,'code_version':lock['code_version'],'input_root_digest':lock['input_root_digest'],'code_digest':lock['code_digest'],'counts':summary['tables'],'unique_source_urls':summary['unique_source_urls'],'gap_status':summary['gap_status'],'strict_coverage':summary['strict_coverage'],'verification':{k:v[k] for k in ['n_checks','n_pass','n_fail','verification_digest']},'fault_probes':{k:fault[k] for k in ['n_probes','n_pass','positive_control_ok']},'rebuild_identical':rb['identical'],'stage_b_complete':False,'capture_media_note':status['limitation']})
md('README.md',f'''# 阶段B修复及证据接入包

状态：**返修及证据入表完成，执行方验证通过，待独立验收**。未标阶段B完成，未开始业务组均值比较。

- [打开公司总览](index.html)：24家公司，可搜索切换，逐字段事实、证据、缺口、分组资格与资本事件。
- [修复报告](REPAIR_REPORT.md) / [新增证据入表对照](EVIDENCE_INGESTION.md) / [字段口径](field_mapping.md)。
- [公司主表](company_profile.csv)、[事实表](company_facts.csv)、[证据表](company_evidence.csv)、[关系表](evidence_links.csv)、[资本表](capital_events.csv)、[307项缺口](company_gaps.csv)、[分组映射](company_group_mapping.csv)。

本包667条事实、102条证据记录、88个不同来源URL、440条关系、24条资本事件。事实行包括未查/未知，证据行包括自述、媒体和背景，均不等于已独立确认外部事实。相对定向包增加15条证据记录、11条事实行；42条既有事实行发生取值、来源、日期或状态变化，仅涉及8家公司。

自检{v['n_pass']}/{v['n_checks']}，故障{fault['n_pass']}/{fault['n_probes']}，Node {node['summary']['n_pass']}/{node['summary']['n_checks']}，真实Chrome {browser['n_pass']}/{browser['n_checks']}；六表离线复算一致。{prior_text}。

## 复算

建议复制本目录后在副本运行（阶段A r3只读底稿仍需保留原路径）：

```text
python -B -X utf8 scripts/s14_reproduce.py
```

入口先核验输入锁，再重建事实、六表、公司主表、页面并复跑验收/故障/发布门禁。`s01_lock_inputs.py`默认仅核验；只有编制新版本时显式`--rebuild`才重建锁。本包已封定，不在原件上进行开发或补查。

`_apply_targeted.py`是历史导入器，已修正Figure编号并停用直接执行；不要重跑它覆盖本轮研究源。`s01b_rebuild_snapshots.py`等历史采集准备脚本不在复算路径。

## 保存方式与研究边界

9张审阅卡保存为`WEB_TOOL_EXTRACT`：有实际web读取返回、正文、定位、哈希与工具记录，**没有把工具返回冒充网站HTML原件**。其余使用既有HTTP/PDF原件。界面提供正文与读取记录链接，并明确显示是否有HTTP原件；完整原网页字节可后续另存补充。

产品、交付、目标场景的严格可用公司数分别23/24、19/24、20/24，三项都有17家。这里“严格”是本项目的时点/状态资格，包含明示的公司自述和媒体，不能理解成全部独立核验。FAR作为团队研究案例展示，未并入当前商业产品组。

旧定向包、r2、r3、研究库、规则与冻结参考保留；2003个保护文件哈希一致。1654条广告与分类没有修改。
''')
md('REPAIR_REPORT.md',f'''# 修复与证据接入结果

本轮完成用户授权的修复及新增证据入表。交付状态为`{scope}`；执行者参与修复，以下检查不冒称新的独立验收。

## 已修复

1. Figure：恢复`B_US_FIGURE_004`为2025-09-16 C轮公告；产品发布另用`B_US_FIGURE_006`。融资事实/资本事件引用004，产品引用006。研究源和历史导入脚本同时修正，避免重建回归。资本直接来源检查核对原文日期、C轮、承诺资本及390亿美元投后估值。
2. 同字段多行：按`fact_seq`声明关系，保留每行的产品/事件范围。BMW同稿F02的2025年运行与F03的2026年项目计划分为两条证据断言，共用原始来源，不算两份独立来源。
3. 星尘：证据发布日期填回原文明确的2026-06-03，撤销“无日期”说明；千寻名称修正，不动公司ID或广告数。
4. 媒体分级：统一识别`MEDIA_REPORT`与`MEDIA_STATEMENT`。Figure B轮聚合库事实保持原披露文字及未知时点，改为媒体陈述，不再显示外部确认。
5. 新增资料：16张审阅卡全部映射入表，8家公司；其中有新证据，也有旧来源复核。松延捐赠、千寻首发月份冲突、FAR研究本体、GXO供应方CEO收入陈述、Fourier概念演示均保留各自性质。
6. 页面：重建24张公司卡与总览，新增本地正文/读取记录链接及保存方式。原证据ID仍可在同页查阅。

## 实测

- 自检 {v['n_pass']}/{v['n_checks']}；故障 {fault['n_pass']}/{fault['n_probes']}，完整副本正对照可发布。
- 新故障：融资证据换成产品页且所有输入/表哈希合法重建，仍因来源身份及资本语义失败被拒；媒体事实升级为外部确认也被拒。
- 六表离线重建逐字节一致；Node {node['summary']['n_pass']}/{node['summary']['n_checks']}；localhost HTTP真实Chrome {browser['n_pass']}/{browser['n_checks']}，已目视截图。
- 输入锁{len(lock['entries'])}条、快照索引{len(read(RUN/'work/snapshot_index.json')['snapshots'])}条，0问题；保护文件{len(before)}个未变。
- {prior_text}。

第一轮故障回放发现母公司背景关系移位使旧负例未实际改动对象；已把来源接到专用背景行，并令找不到目标时直接报错，最终全套重新运行通过。没有把无效负例计为通过。

## 入表结果

| 项目 | 定向包 | 本包 |
|---|---:|---:|
| 事实行 | 656 | 667 |
| 证据记录 | 87 | 102 |
| 产品维度可用公司 | 21 | 23 |
| 交付维度可用公司 | 18 | 19 |
| 场景维度可用公司 | 18 | 20 |
| 三维均可用公司 | 16 | 17 |

分组映射301行，未声明取值0行。分组仍为多标签映射，尚未固定可用于业务比较的少数组定义，不能直接把所有细标签当互斥业务组。广告加权/公司等权的正式业务组比较尚未发布。

缺口307项原身份逐项保留：找到161、未查89、部分37、查后未找到14、不适用4、按分离规则1、沿用后续批次1。全部有记录并不等于每个字段已查完。

## 限制

9张审阅卡仅有web工具正文/读取记录归档，尚无原始HTML字节；所有保存类型和哈希均如实区分。Moz1首发月份冲突未强行裁决；FAR现行团队页/代码页无可靠页面发布日期；公司自述与媒体未升级。融资背景的继承待核条目仍保留，不宣称本轮重做了全部资本事件核验。

下一步对本包做独立复验，再固定少数有解释力的产品与场景组。无需继续泛搜所有融资或上市背景；未取得付费记录不能用于中美商业化高低判断。
''')
cards=read(RUN/'work/supplement_ingestion.json')['cards'];src={s['id']:s for s in read(RUN/'work/supplement_sources.json')}
lines=['# 16张审阅卡的证据入表对照','','证据记录不是独立来源数量。同一网址可按不同说话者、产品或事件拆成多条证据断言。','','| 审阅卡 | 公司 | 入表证据ID | 操作 | 保存方式 | 原文来源 |','|---|---|---|---|---|---|']
for c in cards:
 ids=[c['evidence_id']]+c.get('related_evidence_ids',[])
 lines.append('| '+ ' | '.join([c['review_id'],c['company_id'],'、'.join(ids),c['operation'],c['capture_medium'],f"[{src[c['review_id']]['title']}]({src[c['review_id']]['url']})"] )+' |')
lines+=['','Figure03产品证据006属于修复旧编号冲突，另计新增记录。详见`work/supplement_ingestion.json`和`repair_records/fact_delta.json`；后者列出重建后的最终变更。','','9条web读取记录以`.web.json`保存，JSON内`not_original_http_bytes=true`；其哈希不是网站原件哈希。论文PDF宣传册保留原件，图像PDF说明采用人工视觉转录。']
md('EVIDENCE_INGESTION.md','\n'.join(lines))
md('CHANGE_LOG.md','# 本轮变更\n\n详见[修复报告](REPAIR_REPORT.md)及[证据对照](EVIDENCE_INGESTION.md)。\n\n相对前一定向包：新增15条证据记录、11条事实行，42条既有事实行改动；仅8家公司事实变化。其余16家公司事实记录未改。\n\n历史文档备份在`repair_records/inherited_docs/`，前轮原件不改。')
md('quality_report.md','# 本轮质量报告\n\n'+f'自检{v["n_pass"]}/{v["n_checks"]}，故障{fault["n_pass"]}/{fault["n_probes"]}，Node23/23，Chrome16/16，六表离线一致，保护原件{len(before)}文件未变。\n\n'+prior_text+'。\n\n'+status['limitation']+'\n\n严格资格为时间和状态门槛，不是独立真实性认证。当前状态、完整边界及复算入口见[README](README.md)。')
md('REPAIR_SELFCHECK.md','# 执行方返修检查\n\n本轮由Codex执行修复与证据接入，自检53/53、故障22/22、Node23/23、真实浏览器16/16，六表离线一致。\n\n'+prior_text+'。未把执行方自检改称独立验收。详细结果见`verification.json`、`work/fault_probes.json`、`work/rebuild_check.json`和`repair_records/browser_check.json`。')
md('problem_register.md','''# 当前问题台账

| 问题 | 本轮结果 |
|---|---|
| Figure004来源冲突 | 已修复，产品006独立；新负例已验证 |
| 星尘证据日期缺失 | 已按原文补2026-06-03 |
| 千寻名称写成灵初 | 已修正当前说明，ID与65条广告不改 |
| 事实多行关系绑定 | 已按fact_seq处理，F02/F03、捐赠/销售分别保留 |
| 媒体状态名称漏归一 | 已修复Figure B轮事实的外部确认误标 |
| 原网页HTTP字节未保存 | 9张卡采用web工具正文归档并明确标媒介，原始HTML待补 |
| Moz1首发月份 | 5月/6月并存，保留冲突 |
| FAR历史业务可比性 | 研究案例单列，不据研究项目推断公司销售/部署 |
| 独立验收与组定义 | 尚待独立复验及固定业务组，未开始业务组比较 |
''')
for n in ['TARGETED_TASK_STATUS.md','SEARCH_TRAIL.md','WITHDRAWN_FACTS.md']:
 text=(archive/n).read_text(encoding='utf-8')
 md(n,'> 此文是前轮历史记录。当前修复结果与新证据入表以[修复报告](REPAIR_REPORT.md)和[证据对照](EVIDENCE_INGESTION.md)为准。前轮“未取得”不代表本轮仍未取得。\n\n'+text)
mapping=(archive/'field_mapping.md').read_text(encoding='utf-8')
mapping=mapping.replace('尚未查、受阻、冲突的行不携带确定值，也不生成确定否定组。','尚未查、受阻的行不携带确定值；冲突可保留并列说明，但不生成确定否定组。')
md('field_mapping.md','''# 本轮字段与口径补充

研究维度未新增。增加的是已有字段中的产品/事件分行与证据保存信息。

- 同字段以`fact_seq`指定关系目标；每行只引用自身直接支持或明确背景证据。
- `capture_medium`区分原HTTP字节、原PDF加视觉转录、web工具正文；`snapshot_raw_sha256`只用于真正原件；`capture_record_path/sha256`用于工具或读取记录。
- `WEB_TOOL_EXTRACT`允许审阅过的正文作为可追溯证据载体，但必须原样保留工具返回与媒介说明；不补造HTTP状态或原件哈希。
- BMW一份公告拆F02历史运行与F03计划：来源URL相同，不增加独立来源数；各自事件日与同一发布日期配对。
- `RESEARCH_OUTPUT`、`LONG_TERM_GOAL`与`DATE_CONFLICT`只作背景或退出商业产品/场景组。捐赠交付标签不等于付费交付。
- `MEDIA_REPORT`与`MEDIA_STATEMENT`属于同一媒体陈述层，不升级外部确认。

以下为沿用口径：

'''+mapping)
print(json.dumps({'status':scope,'prior_regression':prior_text,'protected':len(before)},ensure_ascii=False))
