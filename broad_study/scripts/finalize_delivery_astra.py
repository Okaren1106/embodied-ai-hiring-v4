"""Record the actual deliverable and its limits; never convert numeric PASS into content acceptance."""
from pathlib import Path
import json,hashlib,csv,sys,platform,importlib.metadata as meta,re
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[3]
WORK=REPO.parent
AUDIT=ROOT.parent/'acceptance_astra_20260916'
now=datetime.now(timezone.utc).isoformat()
def readj(p):return json.loads(p.read_text(encoding='utf-8'))
def write(p,t):p.parent.mkdir(exist_ok=True,parents=True);p.write_text(t,encoding='utf-8')
def save(p,a):write(p,json.dumps(a,ensure_ascii=False,indent=2)+'\n')
qc=readj(ROOT/'verification/astra_materialization.json')
numeric=readj(ROOT/'verification/astra_independent_numeric.json')
repro=readj(ROOT/'verification/astra_isolated_reproduction.json')
browser=readj(ROOT/'verification/query_browser.json')
assert numeric['status']==repro['status']==browser['status']=='PASS'
assert qc['reviewed_full']==181 and qc['changes']==800

write(ROOT/'README.md',r'''# Astra 综合研究与Q2拓展交付包

2026年9月17日。作者 Astra。报告已交付；**Q2全部内容验收尚未完成**，不能登记 M5/M6 全部 COMPLETE。

## 阅读入口

- [综合报告](REPORT_Astra_final.md)：整合合并裁决、84条对象研究、公司差异分解、17职能Q2、敏感性、验收判断和后续方向。
- [Word报告](document/具身智能公开招聘研究_最终综合报告_Astra.docx)：22页，四张图，逐页目视检查。
- [17职能查询](index.html)：每类所有适用条目、22种语境；整公司范围及预设同任务公司点值。
- [方法](METHODS.md)、[数据字典](DATA_DICTIONARY.md)、[核验说明](verification/REPORT.md)、[当前状态](RUN_STATE.json)。

“最终”指本轮综合研究交付版本，不表示完成研究书规定的所有内容质量验收。当前首轮覆盖1,576条；实际全文复核181条，修订800项。种子抽样110/340、强制队列161/1,208；两个队列有重叠。未复核广告仍保留首轮判读，并明确标为 REVIEW_PENDING，不能用队列成员身份自动证明已经复读。

## 可复算范围

全部Q3状态与Q4数字按修订台账重建。独立数值检查覆盖4,402,134个状态格和六张统计表；物理隔离复算16个输出逐字节一致。R/O/D是前序完成模块，本包继承其数据与报告；本次16文件复算不冒称从零重做R/O/D语义研究。

用下列命令建立新隔离目录。后缀必须为未用过的字母、数字或下划线；脚本拒绝覆盖已存在目录。它物理复制输入、规则、判读及必要种子表，再执行物化与统计。不会执行 register 草稿。

```powershell
$astraPython = 'C:/Users/bestl/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
& $astraPython -B -X utf8 './scripts/reproduce_astra_isolated.py' '_new_check'
```

在新目录运行 `scripts/verify_astra_numeric.py` 可执行不导入生产聚合函数的NumPy数值核对。当前隔离目录登记在 `verification/astra_isolated_reproduction.json`。

报告维护顺序为 `prepare_report_data.py`、`prepare_report_comparisons.py`、`build_final_research_report.py`、`build_research_ledgers.py`、`build_query_astra.py`、`build_word_astra.py`；它们会写派生交付文件，后续修订请先另建版本。图表依赖Matplotlib；Word依赖python-docx。环境见 `verification/environment.json`。此版已完成生成，无须为了阅读再次运行。

## 文件与版本

`inputs/`保存固定数据；`configs/`保留Q2-v2.1的354项及职能适用范围；`notes/`保留前序语义记录。`review/astra_reviews.jsonl`是本轮实际复核与修订，包含判读理由、证据和源文本哈希。`tables/Q3_*final.csv`及`Q4_*final.csv`是本轮结果；同名partial或旧编码表仅作来源，不能代替final表。

`T5_Astra_final.csv`、`T6_Astra_final.csv`分别提供公司解释摘要和最终结论台账，细粒度原证据继续由R/O/D长表承担。`figures/`的四幅图分别附同名CSV。`publication_manifest.json`锁定本版文件，`input_manifest.json`保留909份冻结输入来源记录。

原grok送审包 `../run_20260916_astra_v2/`没有改动，1,742个原文件哈希保持一致。347条旧Astra与grok首轮署名保留。本轮复读不能回称人工独立双盲编码。

## 待完成的验收

完成剩余230条预设抽样、1,047条强制复核队列及系统性规则影响回查；两个数量不可相加为不同广告数。重点包括要求标题强度、任选与示例、协作对象与本人责任、运行期排障与开发调试、供应商技术评审与采购方法。新发现须另版记录，统一重算并重新评估解释。未完成事项属于本轮Q2新增研究字段；不重新开启已认可1654条主分类审核。

原始采集、研究库和封存A/B/C不改；没有扩公司、恢复周采或把供给形态差异解释为国家效应。
''')

write(ROOT/'METHODS.md',r'''# 本轮研究计数与解释方法

作者 Astra　2026年9月17日

## 范围与单位

固定24主体、1,654条公开广告。整公司主范围23家、1,630条；Amazon FAR团队24条独列。Q2只对17个具体职能1,576条编码，整公司Q2为1,552条。复合、任选、歧义、未映射及来源不足主类不强拆入单职能。观察批次不同，广告数不等于人数。

唯一主键identity_key含冻结数据集及来源身份，reading_id仅用于展示；不能按阅读编号或标题连接。分类沿用认可参考，新任务、技术语境和修订在独立分析层。

## 状态和语境

逐广告、职能适用标签、语境与分支物化状态。P明确正例；U局部关系未解；Z来源可读而该格未记录正例；NA不适用；SOURCE_EXCLUDED为来源不能支持该格。N=P+Z，B=P+Z+U。广告加权P/N；未知赋值界限P/B到(P+U)/B。B为零时比例留空，不能填零。未知界限不是置信区间，也不包含漏标和误标风险。

22个格含原14语境和新增8个职责分支格。本人职责分使用与开发；要求分GENERAL、REQUIRED、PREFERRED。无条件、任选、示例、任选且示例分别保留；职责另保留CONDITIONAL。明确必备标题优先于宽泛要求判断；优先标题按优先处理。裸括号和斜线关系不能凭惯例全部当必备。同一广告同格证据去重，多语境比例不相加成100%。

N0528优先要求段在可用原文内截尾，本轮按受影响语境物化712个SOURCE_EXCLUDED；已可确认的正例保留。该路径证明排除机制已实现，不代表全库截尾普查已完成。证据表有一条目录外定性保留记录，不进入适用目录统计。

## 公司比较

先算各公司P/N，再对N大于零公司求平均，称公司等权。广告加权用合计P除以合计N。每个职能、标签、任务与语境重新检查至少3家N大于零公司及合计N至少20的门槛；小样本标记为0<N<10。零分母公司点保留缺失。

主图选择要求明确正例并集覆盖至少5家公司、10条广告；按覆盖排序，每种测量类型最多8项。这是图面选择，不等于上述探索性组比较许可。所有并列最大正例贡献公司保留；最大分母公司另列。P总数为零时不存在最大正例贡献者。

同任务比较从逐格状态重新聚合，不能沿用原先未扣除未知的任务广告总数。预设任务外仍保留各任务统计，以免只展示选中任务。公司选择沿用冻结覆盖顺序，没有按已见到的最大差异选案例。

## 敏感性

保留30个范围定义和广告成员清单，包括整公司/全体/FAR、三种来源方案、明确受众剔除、完全一致职责模板、既定多产品与媒体依据排除、供给类型、七种场景的当前联系与已有使用、旧目录直接覆盖。新增v2条目没有旧目录CODED状态时，不伪造DIRECT对应。

模板筛查仅同公司同主职能、职责去空白标准化后完全一致且至少80字符；要求段可能不同，因此作为模板权重敏感性，不宣称发现重复招聘职位。场景可重叠，观察使用含研究使用与捐赠，不自动等于商业销售。空范围为NA。组门槛须在每个子集重查。

展示条目在22种语境逐一剔除每家公司，共99,792行；未知赋值界限另列，不将删除结果平均当作公司等权。

## 两项深化及其边界

方向一固定四公司两职能84条，ML44、软件40；对象可以多值，命名产品明示、直接连接和未知分开。81条不能归属命名产品，不按公司品牌推填。明示经验年限39条，不明示45条。

方向二在固定共同职能K内，用对称两因素恒等式分解。对公司A减B，构成分量为Σ(sA−sB)(qA+qB)/2，职能内分量为Σ(qA−qB)(sA+sB)/2。两项加总等于总差；不是因果贡献率。每方每职能至少10条活动可判断广告，K至少两个职能。报告K覆盖与技术职能构成；来源筛选使一方缺失时为NA。

## 内容质量与计算质量

首轮1,576条由既有Astra/grok形成。本轮181条全文复读、800项修订；种子样本110/340、强制队列161/1,208。当前复核并非独立概率样本，不估计准确率或kappa。机器人操作22条和工业体验设计23条全部复读；其他职能覆盖不均。

NumPy数值实现未调用生产聚合函数，核对所有状态及六张Q4表。隔离物理复制重建16个Q3/Q4文件并比较完整SHA256。以上证明计算与给定编码一致，不证明未复核的编码正确。Q2内容验收保持未完成。
''')

units={
'Q3_ads_final.csv':'一条Q2广告及其任务和实际复核状态',
'Q3_evidence_final.csv':'一条可定位语义证据；统计前按广告和格去重',
'Q3_states_final.csv':'一条广告×适用标签×语境×分支的状态',
'Q3_astra_changes.csv':'一项本轮显式修订',
'Q3_review_receipts.csv':'一条广告的实际复核收据与队列覆盖',
'Q4_aggregates_final.csv':'一个范围×职能×标签×语境×分支的组格',
'Q4_company_points_final.csv':'整公司范围下一个职能×标签×语境×分支×公司的点',
'Q4_task_strata_final.csv':'一个职能×任务×标签×语境×分支的组格',
'Q4_task_company_points_final.csv':'任务格中的公司点；预设任务全点及其他任务有P或U的格',
'Q4_leave_one_company_out_final.csv':'一个展示格删除一家公司的重算',
'Q4_display_cells_final.csv':'通过主图展示筛选的独立语境格',
'Q4_role_coverage_final.csv':'一个职能的广告覆盖与当前复核规模',
'Q4_scope_definitions.csv':'一个分析范围定义',
'Q4_scope_membership.csv':'一个范围与一条广告的成员关系',
'Q4_dedup_membership.csv':'一个相同职责模板簇内的广告与保留决定',
'Q4_display_selection.csv':'一个职能内通过展示条件的标签',
'Q5_prefixed_company_examples.csv':'正文固定同任务公司展示点',
'T5_Astra_final.csv':'一家公司解释摘要；原始责任证据在继承长表',
'T6_Astra_final.csv':'一条最终研究结论及其限制'
}
dd=[]
for name,unit in units.items():
 p=ROOT/'tables'/name
 with p.open(encoding='utf-8-sig',newline='') as f:fields=next(csv.reader(f))
 dd.append(dict(file='tables/'+name,row_unit=unit,fields=fields))
save(ROOT/'data_dictionary.json',dd)
md=['# 本轮数据字典','','所有CSV为UTF-8；空比例表示无分母或未获组汇总许可，不能替换为0。完整字段清单见[data_dictionary.json](data_dictionary.json)。','','|文件|一行单位|','|---|---|']
md += ['|['+a['file'].split('/')[-1]+']('+a['file']+')|'+a['row_unit']+'|' for a in dd]
md += ['','## 共用字段','',
'`identity_key`为唯一广告身份；`reading_id`用于展示；`company_id`为主体身份；`role`为冻结具体主职能；`task`为新分析层主任务；`label_code`及证据中的`code`均连接冻结Q2-v2.1目录。',
'', '`P/U/Z/NA/SOURCE_EXCLUDED`为广告计数；`N=P+Z`，`B=P+Z+U`。`share`、`share_ad_weighted`、`share_company_equal`以及未知上下界以0到1储存，正文乘100。`gate`为EXPLORATORY_SUMMARY或POINTS_ONLY；不代表内容准确性验收。',
'', '`metric`区分职责使用、职责开发、一般、必备、优先；`branch`保留任选、示例等语境。`field/start/end/quote`给出Python字符串偏移及原文定位，偏移不是UTF-8字节。`qc_status`只有实际本轮全文复读才标ASTRA_FULL_SOURCE_REVIEWED；`REVIEW_PENDING`继续保留首轮状态，不删除数据。',
'','## 继承证据与历史表','',
'R表记录三稿裁决、活动与范围；O表记录84广告工作对象、产品、资历和用途连接；D表记录共同覆盖、分解与敏感性。这些表沿用原完成研究，解释见reports内相应Astra模块报告。原partial表与旧Q2结果属于来源和历史，不是当前统计入口。统一结论采用T6_Astra_final，原三稿结论映射仍由R_T6_claim_mapping承载。',
'','四张图在figures目录各有同名CSV。SOURCE_EXCLUDED从状态层单独汇总，未并入U。Q3_evidence_final有一条excluded_from_catalog=True的定性保留证据，不进入Q3统计格。']
write(ROOT/'DATA_DICTIONARY.md','\n'.join(md)+'\n')

for name in ['阶段E初稿.md','Q_M5_全职能编码与比较报告.md']:
 write(ROOT/'reports'/name,'# 当前正文入口\n\n本目录当前综合正文为[最终综合报告 Astra](../REPORT_Astra_final.md)。原grok同名报告保存在[原送审包](../../run_20260916_astra_v2/reports/'+name+')。\n\nQ2全范围计算已形成；内容验收未完成，不能沿用原全部COMPLETE声明。研究发现、修订与实际复核覆盖以新正文和Q3复核收据为准。\n')
write(ROOT/'REPORT.md','# 综合报告入口\n\n请阅读[最终综合报告 Astra](REPORT_Astra_final.md)。Q2内容验收仍未完成；实际工作范围与限制见正文。\n')

state=readj(ROOT/'RUN_STATE.json');state.update(status='REPORT_DELIVERED_CONTENT_ACCEPTANCE_PENDING',phase='M5_M6_RESEARCH_DELIVERY',updated_utc=now)
state['milestones'].update(M5='FULL_SCOPE_COMPUTED_CONTENT_QC_INCOMPLETE',M6='REPORT_REPRODUCTION_DELIVERED_CONDITIONAL')
state['completed']=['17职能1576条首轮基础完整接续','181条实际全文复核及800项修订','任务分母及公司小样本标记修复','SOURCE_EXCLUDED已物化','30范围22语境与完整公司任务表','独立数值核验及16输出隔离逐字节复算','Astra综合报告和17职能查询交付']
state['pending']=['剩余230条预设抽样与1047条强制队列内容核对（相互重叠）','系统性语义规则影响范围完整回查','上述修订后的再统计与M5/M6正式内容验收']
state['review_progress']=qc
save(ROOT/'RUN_STATE.json',state)

audit=readj(AUDIT/'AUDIT_STATUS.json');audit.update(updated_utc=now,status='CONTENT_NOT_ACCEPTED_NUMERIC_REPAIRS_VERIFIED',execution_status='ASTRA_RESEARCH_REPORT_DELIVERED',repair_package=str(ROOT),next_actions=state['pending'])
audit['acceptance_milestones'].update(M5=state['milestones']['M5'],M6=state['milestones']['M6'])
audit['quota_stop_active']=False
save(AUDIT/'AUDIT_STATUS.json',audit)
ap=AUDIT/'REPORT_Astra.md';old=ap.read_text(encoding='utf-8')
old=old.split('## 八、本轮停止记录')[0]+'## 八、后续返修交付状态\n\n用户已取消原额度停止线。Astra继续完成了分母、资格、来源排除、敏感性、数值核验与隔离复算，并交付[综合研究报告](../run_20260916_astra_m5_m6_final/REPORT_Astra_final.md)。本验收报告前文保留原送审问题的历史判断；哪些问题已经修复以新报告第八节为准。\n\n本轮实际全文复核181条、800项修订；预设样本110/340、强制队列161/1208。内容质量尚未达到研究书全部核对要求，不能因计算通过而追认原M5/M6全部COMPLETE。\n'
write(ap,old)

rootread=WORK/'必读.md';old=rootread.read_text(encoding='utf-8');rest=old[old.index('## 前序B轮结果'):]
prefix=f'''# 当前进度 Astra综合研究报告已交付 Q2内容验收尚未完成

更新：2026-09-17。当前研究入口为 `{ROOT.relative_to(REPO).as_posix()}`。用户要求基于已有数据完成Q2拓展并整合最终研究报告，停止线已取消。

本轮已形成22页Astra综合报告、17职能查询、完整修订数据与复算包。M0—M4保留完成。M5已完成全范围统计，但内容质量核对未达到研究书全部要求；M6报告和复算已交付，正式整包验收仍待M5内容收口。不得把原grok全部COMPLETE当成独立验收结论。

## 最新结果入口

- [Astra综合报告]({ROOT.as_posix()}/REPORT_Astra_final.md)
- [Word报告]({ROOT.as_posix()}/document/具身智能公开招聘研究_最终综合报告_Astra.docx)
- [17职能全项查询]({ROOT.as_posix()}/index.html)
- [复算入口与限制]({ROOT.as_posix()}/README.md)
- [实际状态]({ROOT.as_posix()}/RUN_STATE.json)、[核验说明]({ROOT.as_posix()}/verification/REPORT.md)
- [研究书v2]({REPO.as_posix()}/reports/2026-09-14_company_data_analysis/research_protocol_v2_20260916/研究执行书_v2.md)

## 当前研究事实和进度

冻结24主体1,654条，整公司23家1,630条，FAR24条单列；Q2为17具体职能1,576条，整公司1,552条。没有扩公司、恢复周采、重做主分类或修改研究库与封存A/B/C。原grok送审目录 `stage_d_integrated_v2/run_20260916_astra_v2` 保留历史状态，1,742个文件哈希未变。

三稿合并裁决R、84条对象研究O、固定共同职能分解D沿用完成。研究/部署维护/质量活动位于对应专门职能之外为48/66、264/343、300/459。84条对象研究81条不能归属命名产品；银河通用减Figure四共同职能内工程差+11.10个百分点=构成+19.45与职能内−8.35，不作因果贡献解释。

Q2首轮1,576条完整接续；本轮181条实际全文复核、800项显式修订。预设抽样110/340、强制队列161/1,208；仍余230和1,047条，两队列有重叠不能相加。机器人操作22条与工业体验设计23条均已全文复读，其余职能覆盖不均；当前全样本比例为修订编码条件下的探索性结果。

任务分母、零分母、小样本标记、组门槛与主图筛选已修复。SOURCE_EXCLUDED对截尾要求按格物化。已重算30范围、22种语境、公司点值、任务比较和99,792行逐一删公司结果。独立数值实现核对4,402,134状态格及六张统计表通过；隔离物理复制复算16个输出逐字节一致。17页查询通过真实Chrome 656组筛选，Word22页已逐页检查。程序通过不能替代语义核对。

## 还剩什么

完成剩余预设抽样与强制队列的真实核对，并对要求强度、括号/斜线关系、本人责任、事故排障、供应商采购等系统性边界进行全影响范围回查；随后另版修订、重算与正式内容验收。现阶段优先提高现有数据质量，不为补齐20+20而扩样。未来如转向供给形态比较，再按缺少的有效公司与任务设计新样本。

## 历史成果与当前边界

原Astra、grok4.6、dsv4.1flash三份D研究各自保留；原首轮347条Astra和grok署名不变。本轮Astra回读自身旧判读不是独立双编码。历史A/B/C、认可参考和人工主分类完成状态保持，下文为其历史记录，不表示Q2新增字段的内容验收已经完成。

'''
write(rootread,prefix+rest);write(REPO/'必读.md',prefix+rest)

ep=REPO/'reports/2026-09-14_company_data_analysis/EXECUTION_PLAN.md';txt=ep.read_text(encoding='utf-8');start=txt.index('## 当前执行依据')
txt='# 公司背景与招聘数据正式研究执行安排\n\n更新：2026-09-17。A、B、C和M0—M4沿用完成记录。Astra已交付综合报告、全17职能统计与查询及复算包；Q2内容复核尚未全部完成，M5/M6正式内容验收保持待完成。当前入口：[Astra综合报告](stage_d_integrated_v2/run_20260916_astra_m5_m6_final/REPORT_Astra_final.md)。原grok包保留。\n\n'+txt[start:]
txt=txt.replace('全量结果尚未发布。','全量修订统计与报告已交付，内容验收未完成。')
txt=txt.replace('| Q Q2全17类拓展 | M4完成，M5执行中 | 1,576条全量编码、比较及第二遍核对 |','| Q Q2全17类拓展 | 首轮及全量统计形成，内容验收未完成 | 剩余230抽样及1047强制队列（重叠），系统性回查 |')
txt=txt.replace('| E 初稿与整包交付 | 尚未开始 | 整合验收后的全部成果 |','| E 初稿与整包交付 | Astra综合报告和复算已交付 | 内容修订后最终验收 |')
last=txt.index('两份必读.md同步维护')
txt=txt[:last]+'两份必读.md同步维护当前状态。计划、程序、研究和内容验收分开登记。当前首轮1576条已接续，本轮181条全文复核、800项修订；不能将340条校准或1208条队列成员身份充当已完成第二遍核对。\n'
write(ep,txt)

packages={}
for name in ['numpy','python-docx']:
 try:packages[name]=meta.version(name)
 except meta.PackageNotFoundError:packages[name]='unavailable'
save(ROOT/'verification/environment.json',dict(python=sys.executable,python_version=sys.version,platform=platform.platform(),packages=packages,additional_runtime=str(ROOT/'runtime'),render='Native installed Microsoft Word, hidden COM export, then PyMuPDF page render; bundled render_docx unavailable because soffice.exe absent',browser='Installed Google Chrome via bundled Playwright',created_utc=now))

write(ROOT/'verification/REPORT.md',f'''# Astra本轮验证范围

2026年9月17日。数值计算和交付检查通过；**Q2完整内容验收未完成**。

|检查|实际结果|不能据此推断|
|---|---|---|
|固定输入|909份核对通过|不代表文本全无截尾|
|内容复核|181条实际全文阅读、800项修订|不代表所有1576条已二次复读|
|预设抽样|110/340|不能用首轮或校准代替剩余核对|
|强制队列|161/1208|成员身份不等于已复核|
|独立数值实现|{numeric['state_rows']:,}状态格、{numeric['scalar_checks']:,}项数值比较，六张结果表0差异|不代表给定语义编码全部正确|
|物理隔离复算|{len(repro['files'])}文件完整SHA256一致，无链接代替输入|仅此次Q3/Q4重算，非重新判读R/O/D|
|原grok保护|{repro['original_submission_files_checked']}文件SHA256不变|保留原稿不代表采纳其全部结论|
|查询页|Chrome {browser['pages']}页、{browser['states']}筛选状态通过|未遍历每一可选组合|
|Word|22页原生Word渲染后逐页目视核对|不同用户字体环境仍可能重新分页|

独立数值实现为Astra编写的NumPy矩阵核对，不导入生产聚合函数；不是另一位独立研究者的语义复审。已检查各公司与组的P/U/Z、分母、均值、未知界限、所有最大并列、门槛、删除公司与同任务范围。

明确未完成：剩余抽样、强制语义队列及系统性影响回查；没有发布准确率、人工双盲一致性或全部内容PASS。核验原始记录见本目录各JSON；隔离目录见astra_isolated_reproduction.json；原文定位和实际判读见review/astra_reviews.jsonl。
''')
print('Delivery documentation and synchronized status written; content acceptance stays pending.')
