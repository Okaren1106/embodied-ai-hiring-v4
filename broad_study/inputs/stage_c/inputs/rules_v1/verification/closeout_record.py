from pathlib import Path
import json,hashlib,subprocess,sys,shutil
REPO=Path(r'D:\Embod AI analysis\embodied-ai-hiring-research');BASE=REPO/'reports/2026-09-14_company_data_analysis';RUN=BASE/'analysis_rules_v1/run_20260915T085828Z';SCRATCH=REPO/'.b5accept'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def seal(root):
 files={p.relative_to(root).as_posix():{'bytes':p.stat().st_size,'sha256':sha(p)} for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='release_checksums.json'}
 dump(root/'release_checksums.json',{'version':'1.0','n_files':len(files),'files':files,'excludes':['release_checksums.json (self)','__pycache__/']})
def invoke(source,dest):
 return subprocess.run([sys.executable,'-B','-X','utf8',str(source/'scripts/reproduce.py'),'--output',str(dest)],cwd=source,capture_output=True,text=True,encoding='utf-8')
assert read(RUN/'verification/result.json')['n_fail']==0
assert read(RUN/'verification/browser_check.json')['n_fail']==0
dump(RUN/'verification/visual_review.json',{'reviewed':['overview.png','nimble_pi.png'],'result':'PASS','notes':'24家公司目录、分类与边界、场景状态及本地证据链接可读；1500px无横向溢出。'})
seal(RUN)
copy=SCRATCH/'rules_reproduced_final'
cp=invoke(RUN,copy)
assert cp.returncode==0,(cp.stdout,cp.stderr)
reproduction=json.loads(cp.stdout.strip());assert reproduction['identical_derived_files']==22 and reproduction['verification']==59
probes=[]
def record(name,result,ok):probes.append({'name':name,'passed':bool(ok),'exit_code':result.returncode,'output':(result.stdout+result.stderr)[-1600:]})
existing=invoke(RUN,copy);record('existing_destination_refused',existing,existing.returncode!=0 and 'Refusing to overwrite' in existing.stdout+existing.stderr)
target=copy/'inputs/stage_a/jobs.csv';original=target.read_bytes();target.write_bytes(original+b'\n')
out=SCRATCH/'rules_should_not_publish_input_drift';bad=invoke(copy,out);record('input_tamper_no_publication',bad,bad.returncode!=0 and not out.exists());target.write_bytes(original)
marker=copy/'unlisted_probe.txt';marker.write_text('unlisted',encoding='utf-8');out=SCRATCH/'rules_should_not_publish_inventory';bad=invoke(copy,out);record('unlisted_file_no_publication',bad,bad.returncode!=0 and not out.exists());marker.unlink()
target=copy/'company_classification.csv';original=target.read_bytes();release_original=(copy/'release_checksums.json').read_bytes();target.write_bytes(original+b'\n');seal(copy)
out=SCRATCH/'rules_should_not_publish_different_rebuild';bad=invoke(copy,out);record('rehashed_derived_table_must_reproduce_or_not_publish',bad,bad.returncode!=0 and not out.exists() and 'Rebuild differs' in bad.stdout+bad.stderr)
target.write_bytes(original);(copy/'release_checksums.json').write_bytes(release_original)
assert all(p['passed'] for p in probes),probes
dump(RUN/'verification/reproduction.json',reproduction)
dump(RUN/'verification/publication_probes.json',{'n_checks':len(probes),'n_pass':sum(p['passed'] for p in probes),'n_fail':sum(not p['passed'] for p in probes),'checks':probes})
(RUN/'verification/development_notes.md').write_text('''# 编制期验证记录

首轮语义验证发现未知身份列表用竖线连接会与identity_key内竖线冲突，59项最终检查中的身份可逆性检查已覆盖该问题。现改为CSV字段内JSON数组，不截断广告身份。未改任何原广告、原分类或原关系，未放宽测试条件。

最终59项语义/身份/输入验证、10项真实Chrome检查、22项派生文件隔离重建逐字节一致，以及4项发布入口故障检查均通过。复制件上的故障注入后恢复原复制件；正式旧包始终只读。
''',encoding='utf-8')
url=RUN.as_posix();facturl=(BASE/'stage_b_supplemented/run_20260915T073556Z').as_posix()
newbrief=f'''# 当前进度：24家公司分类与Q2规则已固定，可进入正式结果分析

更新：2026-09-15。两份必读同步改写。用户要求亲自按顺序完成业务分类、覆盖诊断和Q2规则，本轮已完成，未委派代理。

## 最新分析规则与分类包

`reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/`

- [执行报告](<{url}/REPORT.md>)；[分类总览](<{url}/index.html>)。
- [24家公司逐项分类](<{url}/COMPANY_CLASSIFICATION.md>)；[取舍讨论](<{url}/DECISION_MEMO.md>)。
- [Q2规则正文](<{url}/Q2_RULES.md>)；[比较许可](<{url}/comparison_registry.json>)；[复算说明](<{url}/README.md>)。
- [公司事实与证据包](<{facturl}/README.md>)仍为证据底稿；本轮新增的是分析分类，不改写公司事实或广告。

## 已固定的分类

18家公司归为整机/机器人系统产品，3家跨本体模型/软件（Field AI、Physical Intelligence、Skild）；帕西尼触觉部件与系统组合、Nimble自营机器人履单服务分别单列，FAR按内部团队范围单列。供给形态不代表唯一收入主业或付费成熟度；系统组允许模型并行。

51条场景判断组成24×7状态矩阵，区分现行定位/提供、实际使用、捐赠、第三方科研使用、演示、未来目标和无日期背景。当前场景连接：制造10、物流11、商业服务4、巡检3、医疗照护3、家庭3、科研教育4；可以重叠，不是已交付公司数。制造/物流/商业服务为重叠描述分面，其他四类以任务案例展示；未知不当作反面组。

## Q2选择与分母

选定ML/AI工程与软件/平台：全样本159/181条，整公司主比较156/180条，FAR的3/1条保留团队点值。其他17类全量覆盖诊断保留；制造/质量/供应链和硬件也有可用数据，未入Q2是两职能研究范围取舍，不是数据不足。

主展示具体技能按整公司总体覆盖固定选择：ML/AI工程10项，软件/平台9项，各8项技术概念。泛称单列，不按国家/业务组差距选标签。UNMAPPED保留基础分母；逐标签×语境×分支判断PRESENT/UNKNOWN/NO_RECORDED_POSITIVE，UNKNOWN退出对应指标分母但保留广告其他可解释记录，不记为无要求。

模型组ML/AI仅17条，只作公司点值；软件/平台38条中Field AI占23条，可做附条件探索性汇总，必须披露集中和逐一剔除情况。模型组三家全为美国公司，禁止将供给组差异当国家效应。所有标签图格在未知排除后再核对≥3家公司且≥20条广告；每公司少于10条提示小样本。阈值是展示规则，不是统计充分性保证。

## 验证及接续

作者自验59/59，真实Chrome10/10且截图目视通过；隔离复算22份派生表/说明逐字节一致，4项发布保护故障通过。输入封存129文件（17份表/说明＋112份证据资产），设计锁9项；3309份保护原件哈希不变。原1654广告、研究库、r3、measurement规则与旧B包未改。

规则和分类已完成，不冒称独立验收或严格事前注册：编制时已知Q1总量和覆盖，尚未计算业务组技能率差。下一步直接按本版规则生成C阶段Q1—Q3正式结果、图表和分母表，随后做D阶段公司事实解释与敏感性检查；不再将“选择业务组/职能”列为待办，不凭结果大小更换组或技能。

## 前序B轮结果

`stage_b_evidence_integrated/run_20260915T064258Z`修复及16卡入表已独立验收通过（36项原条件＋20项数据审计）；随后按用户授权补入7家公司9证据并补傅利叶日期，接续事实包为`stage_b_supplemented/run_20260915T073556Z`，680事实、111证据（96个不同URL）、457关系、24资本事件、307原缺口。该包补充验证53/53、故障22/22、Chrome22/22、专项18/18、原条件36/36，旧包不回写。

无日期页、Moz1首发月份冲突、付款与融资非关键缺口仍保留原有限用途；阶段A、人工复核和技能用途专项继续沿用既定收口状态。

'''
before=(REPO/'必读.md').read_text(encoding='utf-8');tail=before[before.index('2026-09-14 阶段A已完成二次独立验收'):]
for p in [REPO/'必读.md',REPO.parent/'必读.md']:p.write_text(newbrief+tail,encoding='utf-8')
p=BASE/'EXECUTION_PLAN.md';t=p.read_text(encoding='utf-8')
header='''# 公司背景与招聘数据正式研究：执行安排

状态更新：2026-09-15。阶段A已收口；B轮修复已独立验收，追加公司事实包已验证。当前已完成24家公司业务分类、全17职能覆盖诊断和Q2规则固定，接续[分析规则v1](analysis_rules_v1/run_20260915T085828Z/REPORT.md)。公司事实底稿仍为[补充证据包](stage_b_supplemented/run_20260915T073556Z/README.md)。

分类为18家整机/机器人系统、3家跨本体模型/软件；帕西尼部件与系统组合、Nimble履单运营、FAR内部团队单列。51条场景判断、24×7状态矩阵保留多重归属、目标/使用/演示/计划/无日期区别，不以未知生成否定组。

Q2固定ML/AI工程及软件/平台，全样本159/181条，整公司范围156/180条；分别选10/9项具体技能、各8项技术概念。按逐标签×语境×分支解释资格计算分母，关系UNKNOWN不算0；UNMAPPED保留基础范围。模型组ML仅17条点值展示；软件38条由Field AI贡献23条，须披露集中。国家辅助比较须在同一供给形态内满足覆盖，不从供给组差异推国家差异。

本轮作者验证59/59、Chrome10/10、隔离重建22文件一致、4项发布故障通过；3309份旧原件哈希未变。下一步按已固定规则执行C阶段Q1—Q3正式结果，再做D阶段解释与敏感性。规则与分类不再待定；全阶段结果和论文尚未生成。

'''
t=header+t[t.index('依据：'):]
old='**Q2：** 根据跨公司覆盖、可用广告数与研究意义选择两个主职能，覆盖不足时减少；每个先展示约8—10项有足够覆盖的技能及适量技术概念，完整标签明细保留附表。选择不得按组间差距最大进行。职责使用、硬性要求、一般要求、优先条件、背景，以及任选和示例关系分别保留。'
new='**Q2：** 按[已固定规则v1](analysis_rules_v1/run_20260915T085828Z/Q2_RULES.md)采用ML/AI工程与软件/平台，分别展示10/9项具体技能及各8项技术概念，完整标签和泛称保留附表。选择基于研究问题与总体覆盖，不按组间差距；逐标签、语境和关系分支处理未知分母，职责、硬性/一般/优先要求及任选/示例分别保留。'
assert old in t;t=t.replace(old,new)
old='可准备不依赖业务分组的C阶段描述统计；公司分组及对应Q2纳入规则应在组间比较前固定，当前不发布业务组或商业化比较结论。'
new='公司分类及Q2规则现已固定于`analysis_rules_v1/run_20260915T085828Z`，直接按比较许可表进入C阶段；尚未发布正式业务组结果或商业化比较结论。'
assert old in t;t=t.replace(old,new)
t=t.replace('公司某职能少于10条时提示样本小；业务组少于3家公司时以案例展示为主。这些是展示规则，不能证明统计充分性。','公司某指标分母少于10条提示样本小；业务组每个标签/语境图格少于3家或20条最终可解释广告时以公司点值为主；具体单列场景依规则v1。阈值是展示规则，不能证明统计充分性。')
p.write_text(t,encoding='utf-8')
protected=read(RUN/'verification/protected_before.json');bad=[p for p,h in protected.items() if not Path(p).is_file() or sha(Path(p))!=h]
assert not bad,bad
dump(RUN/'verification/protected_final.json',{'n_files':len(protected),'n_changed':len(bad),'changed':bad,'progress_copies_equal':(REPO/'必读.md').read_bytes()==(REPO.parent/'必读.md').read_bytes()})
dump(RUN/'RULES_FIXED.json',{'status':'RULES_FIXED_AND_CLASSIFIED','version':'1.0','stage_c_results_computed':False,'independent_acceptance_claimed':False,'validation':'59/59','browser':'10/10','reproduction_identical_files':22,'publication_probes':'4/4','protected_files_unchanged':len(protected),'current_scope':'Company classification and executable Q2 design; main research outcome analysis is next.'})
for src,name in [(REPO/'必读.md','current_progress_after.md'),(BASE/'EXECUTION_PLAN.md','execution_plan_after.md')]:shutil.copy2(src,RUN/'verification'/name)
shutil.copy2(Path(__file__),RUN/'verification/closeout_record.py')
seal(RUN)
release=read(RUN/'release_checksums.json');bad=[rel for rel,e in release['files'].items() if sha(RUN/rel)!=e['sha256'] or (RUN/rel).stat().st_size!=e['bytes']]
assert not bad,bad
print(json.dumps({'status':'RULES_FIXED_AND_CLASSIFIED','validation':'59/59','browser':'10/10','reproduction_identical_files':22,'publication_probes':'4/4','protected_unchanged':len(protected),'release_files':release['n_files'],'progress_copies_equal':True},ensure_ascii=False))
