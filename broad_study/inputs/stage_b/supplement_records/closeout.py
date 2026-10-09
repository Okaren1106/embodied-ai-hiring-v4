from bootstrap import *
NEW=Path(json.loads((SCRATCH/'new_run.json').read_text(encoding='utf-8'))['run'])
NR=NEW/'supplement_records'
checks=json.loads((NR/'audit_checks.json').read_text(encoding='utf-8'))
assert checks['n_pass']==36 and checks['n_fail']==0
for name in ['REPAIR_REPORT.md','quality_report.md']:
 p=NEW/name
 t=p.read_text(encoding='utf-8').replace('新增专项验证18/18。','新增专项验证18/18；原36项审计条件回归36/36。')
 p.write_text(t,encoding='utf-8')
p=NEW/'REPAIR_SELFCHECK.md'
p.write_text(p.read_text(encoding='utf-8').replace('18项新增专项均通过。','18项新增专项及原36项审计条件回归均通过。'),encoding='utf-8')
status=json.loads((NEW/'repair_status.json').read_text(encoding='utf-8'))
status['original_audit_conditions_regression']={'pass':36,'total':36}
save(NEW/'repair_status.json',status)
baseurl=NEW.as_posix()
auditurl=AUDIT.as_posix()
current=f'''# 当前进度：B轮修复已独立验收通过，追加补查已入新包并验证

更新：2026-09-15。两份必读同步维护。原修复包的独立验收和本轮追加资料的验证分开记录；阶段B的有限业务组尚未固定，不声明整个B阶段完成，未发布业务组均值。

## 最新接续包

`reports/2026-09-14_company_data_analysis/stage_b_supplemented/run_20260915T073556Z/`

- [公司资料总览](<{baseurl}/index.html>)
- [入口与复算说明](<{baseurl}/README.md>)
- [验收及本轮补充说明](<{baseurl}/REPAIR_REPORT.md>)
- [新增9条证据对照](<{baseurl}/SUPPLEMENT_INGESTION.md>)
- [原修复包独立验收报告](<{auditurl}/REPORT.md>)

## 已完成的验收与补查

原送审包`stage_b_evidence_integrated/run_20260915T064258Z`通过独立验收（ACCEPTED_WITH_LIMITATIONS）：原36项条件与新增20项数据审计全部通过；副本完整复跑自检53/53、故障22/22、Node23/23、真实Chrome16/16。六表、公司主表和HTML逐字节一致，输入锁570条/快照143条无问题。Figure融资与产品证据分离、星尘发布日期、千寻名称及媒体来源性质修复均成立，16张审阅卡全部入表。旧包保留原状，验收结论位于独立报告目录。

按用户“有新增信息直接加入”追加补查：智元、云深处、逐际动力、千寻智能、星海图、宇树、银河通用共7家公司新增9条证据；另补傅利叶CES稿的2026-01-07发布日期精度。新证据中7份保存HTTP原始字节、2份保存实际web工具正文。新增13条事实，调整5条既有事实（含日期），共涉及8家公司。本轮自行编制的新增内容已验证，不冒称新的独立验收。

有业务解释价值的新增包括：智元工业线应用自述、云深处X30与SPock隧道巡检的分层来源、逐际TRON1发售及科研教育定位、千寻小墨PACK产线媒体报道、星海图R1科研/数据采集背景、宇树G1论文中的实际使用及官网工业场景、宁德时代对银河通用S1上岗的直接客户确认。预订不当交付，产量不当交付量，供应方转述不升格客户原文，无日期页面只作背景。

## 当前数据与资格

24家公司；680条事实、111条证据记录（96个不同URL）、457条关系、24条资本事件、307项原缺口、320条分组映射。证据记录不等于独立来源数，事实行包含未知/背景。资本事件表与原送审包逐字节一致，没有泛搜全部融资。

按现行时点和状态规则，产品/交付形态/场景资格覆盖23/23/22家公司，三项都有22家。该资格包含自述、媒体、可提供形态与实际应用，不等于23家已有付费交付；FAR三项均不并入当前商业比较，星海图场景仍缺观察时点日期。缺口状态：找到162、未查88、部分37、查后未找到14、不适用4、按分离规则1、继承后续批次1。

补充后验证：自检53/53、完整正对照及故障22/22、Node23/23、真实Chrome22/22、新增专项18/18、原36项审计条件回归36/36；六表离线重建一致，最终发布门禁通过。输入锁595条、快照152条均无问题。2615份保护原件哈希一致，包括旧包和本次送审包；研究库、r3、measurement规则及1654条广告未修改。

继承的9张审阅卡仍只有实际web工具正文、读取记录和哈希，未冒称网站原始HTML；本轮2份工具归档也明确标注。Moz1首发月份冲突继续保留，付款或融资细节未全面查明不等于无客户或无融资。

下一步：固定少数有业务解释力的产品/场景组及Q2选职能规则，再进行Q1—Q3比较；不以24/24字段完整率为目标，不凭付费证据缺失判断中美商业化高低。阶段A、人工复核和技能用途收口沿用用户既定决定。历史定向包仍保留原CHANGES_REQUIRED记录，不在旧原件回写修复。

'''
before=(REPO/'必读.md').read_text(encoding='utf-8')
tail=before[before.index('2026-09-14 阶段A已完成二次独立验收'):]
for p in [REPO/'必读.md',REPO.parent/'必读.md']:p.write_text(current+tail,encoding='utf-8')
p=BASE/'EXECUTION_PLAN.md';t=p.read_text(encoding='utf-8')
header='''# 公司背景与招聘数据正式研究：执行安排

状态更新：2026-09-15。阶段A已收口。B轮修复及16卡入表原包已通过[独立验收](stage_b_evidence_integrated_acceptance/run_20260915T064258Z/REPORT.md)：原36项条件＋新增20项数据审计通过，完整复跑及真实浏览器通过，未发现阻塞该轮修复的问题。

按用户追加授权，7家公司新增9条证据，另补傅利叶CES发布日期精度；已直接入[最新接续包](stage_b_supplemented/run_20260915T073556Z/README.md)。当前680事实、111证据记录（96个不同URL）、457关系、24资本事件、307缺口。产品/交付形态/场景时点资格23/23/22，三项都有22家；资格不等于付费交付确认。

新增包为本轮编制后的验证：自检53/53、故障22/22、Node23/23、Chrome22/22、专项18/18、原审计条件回归36/36，六表重建一致；与原包独立验收分别记录。新增7份HTTP原件＋2份工具正文，继承9卡工具正文限制保留。2615份原件哈希未变，研究库、r3、规则及1654分母不变。

下一步固定有限业务组及Q2选职能规则，再开展Q1—Q3比较。FAR研究产物不并入当前商业产品组，星海图无日期场景只作背景；捐赠、自述、媒体、预订和计划保留各自性质。尚不声明整个B阶段完成，不发布业务组均值；融资非关键缺口不阻塞研究。

'''
t=header+t[t.index('依据：'):]
old='上述四项是原定首批成果。A阶段前三项已交付并通过独立验收；B阶段定向补查已写入 `stage_b_targeted/run_20260915T030000Z`，待独立验收。'
new='上述四项是原定首批成果。A阶段前三项已交付并通过独立验收；B轮修复及16卡入表已独立验收通过，追加补查已入 `stage_b_supplemented/run_20260915T073556Z` 并验证。'
assert old in t
p.write_text(t.replace(old,new),encoding='utf-8')
protected=json.loads((AUDIT/'protected_before.json').read_text(encoding='utf-8'))
changed=[p for p,h in protected.items() if not Path(p).is_file() or sha(Path(p))!=h]
assert not changed,changed
result={'n_protected':len(protected),'n_changed':len(changed),'changed':changed,'current_progress_copies_equal':(REPO/'必读.md').read_bytes()==(REPO.parent/'必读.md').read_bytes(),'note':'两份当前必读及执行安排按本轮结论同步改写，不属于历史原件保护集合。'}
for p in [AUDIT/'protected_final.json',NR/'protected_final.json']:save(p,result)
for source,dest in [(REPO/'必读.md','current_progress_after.md'),(BASE/'EXECUTION_PLAN.md','EXECUTION_PLAN_after.md')]:shutil.copy2(source,AUDIT/dest)
save(NR/'visual_review.json',{'reviewed':['browser_galbot.png'],'result':'PASS','observation':'公司筛选、字段表、证据引用及页面状态可读；页面标明原包已独立验收及补充验证区别。'})
shutil.copy2(Path(__file__),NR/'closeout.py')
print(json.dumps(result,ensure_ascii=False))
