from bootstrap import *
import datetime
NEW=Path(json.loads((SCRATCH/'new_run.json').read_text(encoding='utf-8'))['run']);NR=NEW/'supplement_records'
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
d=read(NR/'data_summary.json');v=read(NEW/'verification.json');fault=read(NEW/'work/fault_probes.json');browser=read(NR/'browser_check.json');lock=read(NEW/'work/input_lock.json')
assert v['n_pass']==53 and v['n_fail']==0 and fault['n_pass']==22 and browser['n_pass']==22
archive=NR/'prior_package_docs';archive.mkdir(exist_ok=True)
names=['README.md','REPAIR_REPORT.md','REPAIR_SELFCHECK.md','repair_status.json','analysis_manifest.json','quality_report.md','problem_register.md','CHANGE_LOG.md','TARGETED_TASK_STATUS.md','SEARCH_TRAIL.md','TARGETED_COLLECTION_PENDING_ACCEPTANCE']
for n in names:
 if not (archive/n).exists():shutil.copy2(NEW/n,archive/n)
def write(n,t):(NEW/n).write_text(t.strip()+'\n',encoding='utf-8')
readme='''# B轮验收后公司证据补充包

**原修复及16卡入表包已通过独立验收；本版按用户追加授权补查并直接入表，补充后验证通过。** 原件独立验收与本轮自行补充验证分别记录。阶段B的有限业务组尚未固定，不声明整个B阶段完成。

- [公司资料总览](index.html)：24家公司，逐字段事实、证据原文、保存方式、缺口与资格。
- [验收及本轮新增说明](REPAIR_REPORT.md)；[原送审包独立验收](../../stage_b_evidence_integrated_acceptance/run_20260915T064258Z/REPORT.md)。
- [9条新增证据对照](SUPPLEMENT_INGESTION.md)；[原16卡对照](EVIDENCE_INGESTION.md)。
- [公司主表](company_profile.csv)、[事实](company_facts.csv)、[证据](company_evidence.csv)、[关系](evidence_links.csv)、[资本事件](capital_events.csv)、[缺口](company_gaps.csv)、[分组映射](company_group_mapping.csv)。

680条事实、111条证据记录、96个不同URL、457条关系、24条资本事件、307项原缺口、320条分组映射。证据记录数不是独立来源数；事实含未知和背景，不能当作全量外部确认。

产品/交付/场景时点资格覆盖23/23/22家公司，三项都有22家。FAR三项均不并入当前商业比较；星海图场景只作无日期背景。资格包含自述、媒体、提供形态及实际应用，不等于已售商品或付费证据齐全。业务组定义和Q2职能选择仍应在比较前固定。

## 复算

复制本目录至新的空目录，在副本执行：

```text
python -B -X utf8 scripts/s14_reproduce.py
```

入口先核验已封定输入锁，再重建并复跑故障与发布门禁。阶段A r3等既有只读底稿须保留脚本声明的本机原路径。`s01_lock_inputs.py`默认只核验；`--rebuild`仅供编制新版本，不用于掩盖审计时的输入漂移。

本轮9份新来源中7份保存HTTP原始字节、2份保存实际web工具返回，均有正文、记录与哈希。继承9张卡仅有工具正文的限制继续保留。旧包、研究库、measurement规则和1654条广告未修改。
'''
write('README.md',readme)
report='''# B轮验收结果与追加补证

## 结论

原送审包`stage_b_evidence_integrated/run_20260915T064258Z`的修复与16卡入表通过独立验收：36项原审计条件＋20项新增数据核验全部通过，完整副本53项自检、22项故障、23项Node和16项真实Chrome均通过，六表/主表/HTML逐字节一致。详见[独立验收报告](../../stage_b_evidence_integrated_acceptance/run_20260915T064258Z/REPORT.md)。

本轮随后按用户“有新增信息直接加入”的指令另建本包。新增资料由审计者编制，因此以下是补充后验证，不冒称对自身补充的独立验收。

## 实际新增

| 公司 | 找到并写入的内容 | 保留边界 |
|---|---|---|
| 智元 | 带日期的官方订单与G2制造产线应用 | 下线量不是交付量；供应方公告不升级直接客户验收 |
| 云深处 | X30/SPock隧道试点及软硬件定制；SP Group项目确认 | 客户文未点名X30，型号归属仍据供应方；扩展规模是计划 |
| 逐际动力 | 2024-10-16 TRON1发售、开放预订、科研教学定位 | 预订不当作已交付；只限定TRON1 |
| 千寻智能 | 2025-12-17小墨进入宁德时代中州PACK产线的记者报道 | 媒体性质；实体部署不推断销售/RaaS模式或付款 |
| 星海图 | R1科研、R1 Lite数据采集的现行官方定位 | 没有发布日期，背景展示 |
| 宇树 | 使用方论文确认G1科研应用；官方工业巡检方案 | 论文不证明付款；现行工业页无日期，背景展示 |
| 银河通用 | 宁德时代直接确认Galbot S1进入其智慧产线 | 未披露台数、付款与首次投运日；协议计划另看 |

另将傅利叶CES稿已明示的发布日期由2026-01补为2026-01-07，展示事件仍按2026-01保留。未改发布日期未知的其他来源。

与送审包相比：新增9条证据记录、13条事实行，5条既有事实行变化（3条未知字段补值、2条CES事实日期更新）；事实变化涉及8家公司，其中7家有新来源。资本表逐字节未改。新来源7份HTTP原件、2份web工具正文；星海图web读取失败后通过直接HTTP成功取回正文，未因单一路径失败判为不可查。

## 补充后的数据与验证

- 680事实、111证据记录、96不同URL、457关系、24资本事件、307缺口、320映射。
- 产品/交付/场景资格23/23/22，三项都有22家；FAR全无，星海图场景仍缺观察时点日期。
- 缺口：找到162、未查88、部分37、查后未找到14、不适用4、按分离规则1、继承后续批次1。307项是沿用的缺口身份，新增字段事实数量不等于关闭缺口数量。
- 自检53/53；完整正对照与故障22/22；Node23/23；真实Chrome22/22；新增专项验证18/18。六表离线重建一致。
- 第一轮编制核验因中间事实源哈希尚未更新而正确拒绝；先生成新中间源、封定新版本输入后完整重跑通过。未放宽检查条件。
- 2615份保护原件哈希未变，包括旧版及当前送审包；研究库、冻结1654、规则与广告分类均未改。

## 当前可用范围

公司事实已足以支持有限探索，但本包的细标签仍为多标签映射。硬件销售、预订、系统集成、实际应用、捐赠、研究发布和概念展示的含义不同。下一步先固定少数有研究意义的业务/场景组，以及Q2职能选择规则，再计算比较结果。无需为追求全部完整继续泛搜所有融资背景。未知付费不能用于判断中美商业化高低。

本轮没有获取所有继承来源的原始HTML，也没有重新联网验证全部680行事实。完整新增来源和断言见[对照表](SUPPLEMENT_INGESTION.md)；脚本、差异、检验与浏览器证据见`supplement_records/`。
'''
write('REPAIR_REPORT.md',report)
sources=read(NR/'ingestion.json')['new_sources'];titles={x['evidence_id']:x for x in __import__('csv').DictReader((NEW/'company_evidence.csv').open(encoding='utf-8-sig'))}
table=['# 本轮9条新增证据入表','', '逐条来源均已打开正文；同一TWIST2论文同时解释FAR研究产物和宇树G1实际使用，只增加证据记录，不增加独立来源数量。','', '| 证据ID | 公司 | 发布日 | 保存方式 | 原文 |','|---|---|---|---|---|']
for s in sources:
 e=titles[s['evidence_id']];table.append(f"| {s['evidence_id']} | {s['company_id']} | {s['publication_date'] or '未知'} | {s['capture_medium']} | [{e['source_title']}]({s['url']}) |")
table+=['','- 全量变更：`supplement_records/ingestion.json`（研究源变更）及`fact_delta.json`（最终表变更）。','- 原始字节、正文、读取记录：`evidence_snapshots/NEW_*`。','- 首次受限环境直连失败，随后经网络权限审核执行公开来源下载；7成功、2 TLS失败，后者使用已实际读取的web工具正文。没有自动审批拒绝导致的未完成事项。','- 搜索结果与失败导航保留在原验收目录`web_records/`，新增HTTP请求结果保存于`supplement_records/NEW_*.fetch.json`。']
write('SUPPLEMENT_INGESTION.md','\n'.join(table))
write('quality_report.md','# 本版质量与状态\n\n'+ '\n'.join(report.split('## 补充后的数据与验证')[1].split('## 当前可用范围')[0].splitlines()))
write('REPAIR_SELFCHECK.md','# 本版验证\n\n53项自检、22项故障（含完整正对照）、23项Node、22项真实Chrome、18项新增专项均通过。详细结果见verification.json、work/fault_probes.json、supplement_records/validation.json和browser_check.json。原包独立验收56项通过，不与本版自行验证混称。')
write('problem_register.md','# 当前问题与限制\n\n本轮修复包的原阻塞项已通过独立验收。新增来源已按授权入表并验证。待固定业务组和Q2选择规则；Moz1首发月份冲突仍退出对应比较；FAR研究不并入商业产品；星海图场景与宇树工业方案无日期；付款未知不等于无客户。既有工具正文归档限制保留。')
write('CHANGE_LOG.md','# 本轮变化\n\n原包独立验收通过后按用户追加授权补9证据、13事实；5既有事实更新。7公司新增来源，傅利叶另补CES发布日期精度。原包及研究库不改写。详见REPAIR_REPORT.md。')
write('TARGETED_TASK_STATUS.md','# 本轮状态\n\n原修复包独立验收通过；本版按用户授权补查并入表，补充后验证通过。阶段B业务组尚待固定。旧定向任务的历史记录见supplement_records/prior_package_docs/。')
write('SEARCH_TRAIL.md','# 检索与归档范围\n\n用户追加要求补查原缺失信息。本次针对交付形态、目标场景和具名客户使用核查，新增9证据，涉及7公司。搜索工具返回见原验收目录web_records；新增页面/HTTP访问记录见supplement_records/NEW_*。原search_log中的192项派生摘要仍标DERIVED_STATUS_SUMMARY，不当作真实搜索。新增9条PAGE_REVIEW对应实际读取，原43条SEARCH计数不冒充包含本轮全部外部搜索。')
write('TARGETED_COLLECTION_PENDING_ACCEPTANCE',f'stage: B\nscope: SUPPLEMENT_VALIDATED_NOT_INDEPENDENTLY_ACCEPTED\nrun: {NEW.name}\ncode_version: stage-b-supplement-v2\noriginal_candidate: INDEPENDENT_ACCEPTANCE_PASSED\nstage_b_complete: false')
status={'status':'SUPPLEMENT_VALIDATED_NOT_INDEPENDENTLY_ACCEPTED','original_candidate_status':'ACCEPTED_WITH_LIMITATIONS','run':str(NEW),'previous_candidate':str(RUN),'stage_b_complete':False,'stage_c_started':False,'data':d,'self_check':{'pass':53,'total':53},'fault_probes':{'pass':22,'total':22},'node':{'pass':23,'total':23},'browser':{'pass':22,'total':22},'supplement_checks':{'pass':18,'total':18},'protected_original_files':2615}
save(NEW/'repair_status.json',status)
manifest={'stage':'B-supplemented','scope':status['status'],'run_id':NEW.name,'code_version':'stage-b-supplement-v2','input_root_digest':lock['input_root_digest'],'code_digest':lock['code_digest'],'counts':d['tables'],'unique_source_urls':d['unique_source_urls'],'strict_coverage':d['strict_coverage'],'gap_status':d['gap_status'],'verification':{k:v[k] for k in ['n_checks','n_pass','n_fail','verification_digest']},'fault_probes':{'n_probes':22,'n_pass':22,'positive_control_ok':True},'rebuild_identical':True,'stage_b_complete':False,'original_candidate_independent_acceptance':'../../stage_b_evidence_integrated_acceptance/run_20260915T064258Z/REPORT.md','capture_media_note':'本轮新证据7份HTTP原件＋2份工具正文；继承9张卡工具归档限制保留。'}
save(NEW/'analysis_manifest.json',manifest)
for n in ['bootstrap.py','audit_extra.py']:
 shutil.copy2(SCRATCH/n,AUDIT/n)
for n in ['bootstrap.py','ingest_supplement.py','prepare_supplement.py','verify_supplement.py','fetch_sources.py','finalize_docs.py']:
 shutil.copy2(SCRATCH/n,NR/n)
shutil.copy2(SCRATCH/'supplement_reproduction.log',NR/'final_pipeline.log')
# Same 36 assertions, new target context: this is a regression run by the supplement author.
shutil.copy2(AUDIT/'prior_audit_regression.py',NR/'prior_audit_regression.py')
context=(AUDIT/'regression_context.py').read_text(encoding='utf-8').replace('HERE.parent.parent','HERE.parent.parent.parent').replace('RUN=BASE/"stage_b_evidence_integrated/run_20260915T064258Z"','RUN=HERE.parent')
(NR/'regression_context.py').write_text(context,encoding='utf-8')
save(AUDIT/'acceptance_verdict.json',{'verdict':'ACCEPTED_WITH_LIMITATIONS','candidate':str(RUN),'independent_checks':56,'n_fail':0,'selfcheck_replayed':'53/53','faults_replayed':'22/22','chrome':'16/16','protected_originals':2615,'stage_b_complete':False,'user_requested_supplement':str(NEW)})
print(json.dumps({'finalized':str(NEW),'report':str(AUDIT/'REPORT.md')},ensure_ascii=False))
