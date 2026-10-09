from pathlib import Path
from datetime import datetime, timezone
import json, re, hashlib, sys, platform, sqlite3, zipfile
from importlib.metadata import version
ROOT=Path(__file__).resolve().parents[1]
WORK=Path('D:/Embod AI analysis')
REPO=WORK/'embodied-ai-hiring-research'
NOW=datetime.now(timezone.utc).isoformat()
def readj(rel): return json.loads((ROOT/rel).read_text(encoding='utf-8'))
def write(rel,text): (ROOT/rel).write_text(text,encoding='utf-8')
def save(rel,obj): write(rel,json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
receipts=['V3_independent_state_resolution.json','astra_independent_numeric.json',
 'V3_two_layer_independent_sql.json','astra_isolated_reproduction.json',
 'V3_protected_inputs.json','query_v3.json']
for x in receipts: assert readj('verification/'+x)['status']=='PASS',x
progress=readj('verification/V3_review_progress.json')
assert progress['seed_done']==progress['seed_total']==340
assert progress['mandatory_done']==progress['mandatory_total']==1208
assert progress['pending_union']==0 and progress['full']==469
impact=readj('verification/V3_revision_impact_final.json')
assert (impact['boundary_only'],impact['unselected'])==(760,347)
doc=ROOT/'document/具身智能公开招聘研究_最终综合报告_Astra.docx'
with zipfile.ZipFile(doc) as z: assert z.testzip() is None
pages=readj('document_qa/page_text.json')
assert len(pages)==17 and [x['page'] for x in pages]==list(range(1,18))
for n in range(1,18):assert (ROOT/f'document_qa/page-{n}.png').exists()
# Markdown path quoting only. The Word manuscript text and image are unchanged.
for f in ['REPORT_Astra_final.md','REPORT.md']:
 s=(ROOT/f).read_text(encoding='utf-8')
 s=re.sub(r'(!\[[^\]]*\]\()([^<][^)]*)(\))',r'\1<\2>\3',s)
 write(f,s)
assert (ROOT/'REPORT.md').read_bytes()==(ROOT/'REPORT_Astra_final.md').read_bytes()
comp=readj('verification/astra_comparison.json')
comp['coding']='Astra-Q2-v2.1-review3'
comp['metadata_corrected_utc']=NOW
comp['metadata_note']='Corrected stale hardcoded version label only; numeric outputs unchanged.'
save('verification/astra_comparison.json',comp)
write('reports/V3_02_修订影响.md',"""# 2. 修订对结论的影响（Astra，最终 V3）

更新：2026-09-18。当前结果以最终 V3 表和报告为准。

## 版本与分母

Grok首轮至上一版Astra的800项事务涉及161条独立广告。原14语境可对齐25,914格，其中1,556格的计数、分母或门槛变化。该段是历史基线，不是当前工作量。

本版新增4,548项事务，涉及900条广告；累计5,348项。与上一版相比，最终证据新增或改变4,394条，涉及895条广告。事务数、证据数和广告数不同，也都不能解释为总体错误率。修订含要求语境、责任关系、分支、未知范围、任务判断、补充提及和规则适用变化。

相同22语境下，40,722个整公司汇总格中4,609格变化，4格改变组门槛。扩表本身不等于需求增长；两个版本均描述同一冻结样本。

## 结论如何变化

- ML训练推理系统无条件开发：阶段C 81/156，Grok及上一版80/156，本版76/156。
- ML基础模型/VLA无条件开发：阶段C 72/156，Grok及上一版67/156，本版49/154，U=2。18个旧正例退出严格格，主要改为参与协作、示例、未知或基础设施支持关系，不能说18条广告完全没有模型工作。正文同时列宽联系情景。
- ML Python一般无条件：上一版60/135、U=21，本版60/133、U=23；未知增加不自动说明质量提高。
- 软件Linux一般无条件：70/177改为69/177；C++ 42/150改为44/150，U=30仍在。
- 控制闭环一般无条件：Grok 52/75，上一版51/75，本版52/75。回到旧数值是逐证据再裁决的结果。
- 部署与现场服务Python：11/78、U=6；去Field AI后4/65、17家有效公司，仍过当前门槛，但比例对该公司的广告贡献敏感。撤回“去Field后不能比较”的旧说法。
- 部署活动旧标签口径不一致，相关活动比例和分解撤出实质主结论。这与“部署与现场服务职能”不同。

完整链见 tables/V3_key_results_version_chain.csv；同口径格变动见 tables/V3_revision_impact_v2_to_v3.csv；事务轴与有效证据变动分别见 tables/V3_incremental_change_axes.csv、tables/V3_effective_evidence_changes.csv。最终主报告解释公司差异、未知界限和敏感性，不根据修改次数评价模型优劣。
""")
write('reports/V3_03_同任务比较方法.md',"""# 3. 同任务比较方法（Astra，最终 V3）

更新：2026-09-18。

## 任务从职责和工作对象划分

保持冻结主职能；Python、Linux、C++或某工具不能单独作为任务纳入条件。任务赋值是文本判断，不是关键词分类。任务定义延续Q2-v2.1，不能根据公司工具差异大小更换比较组。

机器人模型：本人训练或优化机器人策略/具身模型；仅提供训练基础设施不进入主层。机器人运行软件：本人交付运行时、中间件、机器人应用或遥操软件；普通业务后台、内部IT和云端界面不因使用C++进入。板级电路：本人交付板卡、PCB、电源或驱动电路；仅固件或线束不因出现PCB进入。

## 主任务与次任务

主分析每条广告只计一个主任务。上一版三层整公司样本为106、87、56条，167条广告有次任务。本版最终为105、87、56条，166条有次任务。N0353主要交付是业务场景模型，机器人仅出现在优先背景，因此移出机器人模型主层；保留原文与事务理由。

主次共同纳入只用于敏感性，按广告去重，不能与主任务计数相加。主任务不明确保留UNRESOLVED/OTHER。看到工具结果后的回看不称盲法验证。旧文板级电路51条误用了生产工艺分母，实际56条。

## 两层指标

第一层：可辨识技术在本人职责或资格要求中出现，按广告去重；明确任选、示例和术语明确但分支未解可计提及；对象本身未解不计正例。背景和协作联系另列。

第二层：在上述提及广告内，分别统计职责、明确必备、一般、优先；同一广告可进入多列，不能相加成100%。原22个无条件/任选/示例等语境格继续单独呈现。

未知赋值上下界只针对已识别未知。责任宽情景包含参与、协作和支持联系，是联系上界，不等于本人能力；不能替代严格职责层。去模板、去实习校招、纳入次任务、逐家公司剔除分别处理不同风险。

三任务仍存在细对象、资历、语言和模板差异；同任务提高可比性，不保证工作完全相同。结果与成员清单见 tables/V3_two_layer_aggregates.csv、tables/V3_two_layer_membership.csv、tables/V3_two_layer_evidence.csv，正文第七至八节给出研究判断。
""")
write('reports/V3_04_内容验收.md',"""# 4. 全17职能规定范围验收（Astra）

2026-09-18。本轮规定范围已完成：预设340条全文抽样全部复核；强制1,208条队列全部完成相应边界或全文复核，两者有重叠。累计469条全文（上一版181＋本版288）、760条仅边界、347条未选二次，合计1,576条。没有把边界复核写成全文复核，也没有因未选中就批量改为未知。

边界复核读候选或已有证据的相关段落、邻接语境与标题；全文复核读完整可用文本。已对无关键词记录、已知语义规则问题和局部来源问题定向回查。不能把定向样本当随机准确率样本，Astra复读自身旧判读不是独立双编码。

所有规定待办为0，最终表保留证据位置、理由、作者、事务顺序和不同深度的复核状态。三个来源受限广告按真实限制物化SOURCE_EXCLUDED；未知语义与来源排除分开。E0107两条不同广告以完整identity_key区分。

内容研究完成不等于全部证据逐项双重验证。17职能按探索性统计发布；国家因果、行业总体招聘需求、人数、公司能力和业务模式贡献率不在证据支持范围。

数据：tables/V3_review_coverage_final.csv、tables/Q3_review_receipts.csv、verification/V3_review_progress.json。
""")
state=readj('RUN_STATE.json')
state.update(status='COMPLETE',updated_utc=NOW,
 steps={str(i):'COMPLETE' for i in range(1,7)},
 step_notes={'1':'Deployment activity substantive claims withdrawn; historical measurements retained.',
 '2':'Final C/Grok/Astra-v2/Astra-v3 comparable revision chain completed.',
 '3':'Final primary/secondary task definitions and membership documented.',
 '4':'Specified seed and mandatory semantic review scope completed; not all-ad independent double coding.',
 '5':'Three fixed tasks, two-layer comparison and sensitivity completed.',
 '6':'Independent and isolated computation passed; 17-page report visually inspected and delivered.'},
 review_progress={**progress,'boundary_only':760,'unselected_second_pass':347},
 final_report='REPORT_Astra_final.md',publication_manifest='publication_manifest.json')
save('RUN_STATE.json',state)
lim=['固定样本探索研究，不是行业普查或因果研究。',
 '469全文、760仅边界、347继承首轮；不是全样本二次全文或独立双编码。',
 '部署活动历史测量口径不一致，相关实质主结论已撤回。',
 'P/Z/U及来源排除保证状态表达；数值复算不证明语义准确率。']
save('FINAL_DELIVERY.json',dict(status='COMPLETE',author='Astra',version='core-Q2-v3',
 completed_utc=NOW,M5='COMPLETE_SPECIFIED_REVIEW_SCOPE',M6='COMPLETE',
 report_markdown='REPORT_Astra_final.md',report_word=doc.relative_to(ROOT).as_posix(),
 query_index='index.html',two_layer_query='two_layers.html',word_pages=17,
 review_scope=state['review_progress'],state_counts=comp['state_counts'],
 verification_receipts=receipts,limitations=lim,remaining_required_work=[]))
save('verification/document_qa_v3.json',dict(status='PASS',pages=17,
 inspected_pages=list(range(1,18)),inspector='Astra',
 method='Hidden Microsoft Word opened DOCX read-only and exported PDF; PyMuPDF rendered all pages; every page visually inspected.',
 fallback_reason='Default renderer unavailable because LibreOffice not installed; Word export used.',
 checks=['No clipped or overlapping text','Tables readable and repeated header rows present',
 'Figure legible','No orphan final page','Author Astra and current scope explicit'],
 docx_sha256=sha(doc),pdf_sha256=sha(ROOT/'document_qa/Astra_final_report.pdf'),
 page_png_sha256={str(n):sha(ROOT/f'document_qa/page-{n}.png') for n in range(1,18)},
 metadata='Markdown image target was subsequently angle-quoted only; manuscript content and Word image unchanged.',
 created_utc=NOW))
libs={}
for n in ['numpy','python-docx']:
 try:libs[n]=version(n)
 except Exception:libs[n]='not available'
sys.path.insert(0,str(ROOT/'runtime'))
for n in ['matplotlib','PyMuPDF','Pillow']:
 try:libs[n]=version(n)
 except Exception:libs[n]='not available'
save('verification/environment_v3.json',dict(python=sys.version,python_executable=sys.executable,
 platform=platform.platform(),sqlite=sqlite3.sqlite_version,packages=libs,
 local_runtime=str(ROOT/'runtime'),document_export='Microsoft Word COM, hidden read-only',
 time_utc=NOW))
old=(WORK/'必读.md').read_text(encoding='utf-8')
history='## 历史成果与当前边界'+old.split('## 历史成果与当前边界',1)[1]
history=history.replace('不表示Q2新增字段的内容验收已经完成','不表示所有Q2新增字段均已独立双重验证')
base=ROOT.as_posix()
header=f"""# 当前进度：Astra 六步研究修订与 Q2 拓展已完成

更新：2026-09-18。用户授权的六步工作、M5规定范围内容复核、M6计算及最终报告交付均已完成。当前版为 run_20260917_astra_core_q2_v3，报告署名 Astra。

## 当前交付

- [最终综合报告 Markdown](<{base}/REPORT_Astra_final.md>)
- [最终综合报告 Word（17页）](<{base}/document/具身智能公开招聘研究_最终综合报告_Astra.docx>)
- [17职能查询](<{base}/index.html>)；[三任务两层比较](<{base}/two_layers.html>)
- [状态与范围](<{base}/FINAL_DELIVERY.json>)；[复算说明](<{base}/README_REPRODUCE.md>)
- [交付哈希清单](<{base}/publication_manifest.json>)

## 六步结果

1. 活动规则—原文—结论核对完成。部署与维护标签历史口径不一致，依赖该口径的实质结论已撤回；研究和宽质量活动、工程活动算术分解保留。
2. 阶段C→Grok→Astra上一版→本版修订链完成。本版新增4,548项事务、900条广告；有效证据变动4,394条、895条广告；40,722个同口径汇总格中4,609格变化、4格改变门槛。都不是总体错误率。
3. 主次任务定义与最终成员完成。机器人模型、运行软件、板级电路整公司主任务为105、87、56条；166条广告有次任务，另列敏感性。
4. 17职能规定复核范围完成：340/340预设全文，1,208/1,208强制队列，去重待办0。累计469全文、760仅边界、347继承首轮。不是1,576条全部二次全文或独立双编码。
5. 三任务技术提及与职责/必备/一般/优先的两层比较完成，并列未知界限、去模板、去校招实习、次任务和去公司敏感性。
6. 4,402,134状态格独立重建、独立矩阵和SQL检验通过；隔离复算21份输出逐字节一致。Word17页逐页检查通过，查询页功能与112条链接检查通过。

## 主要研究判断

84条对象研究中81条不能归属命名产品；四共同职能内银河通用减Figure工程活动差+11.10个百分点=构成+19.45与职能内−8.35，仅为描述性算术分解。

机器人模型Python提及在银河通用与自变量之间仍有样本差异；运行软件C++在两者中都常见，未知界限重叠，不支持需求排序。板级电路应同时看EDA工具和验证方法。部署现场职能Python去Field AI后仍通过当前组门槛，但比例对该公司广告贡献敏感。

## 范围、保护及后续

冻结24主体1,654条；整公司23家1,630条，FAR24条单列；Q2为17具体职能1,576条、整公司1,552条。冻结输入909文件、原Grok1,742文件及旧Astra封存1,835文件哈希未变。未扩公司、恢复周采、改冻结主分类或研究库。

本轮授权必需工作已无待办。若启动下一轮，优先另版重建部署活动的对象边界；其次在固定任务内研究资历、模板与要求方式。扩公司应服务具体比较，优先补稀缺供给类型并统一团队切分；20+20不是证明研究有效的条件。独立双编码、行业总体推断、国家或业务模式因果效应仍未建立。

旧22页 run_20260916_astra_m5_m6_final 保持封存；当前数字使用本版。旧Astra347条及grok接续署名不改。包内未带V3前缀的旧T5/T6用于历史追溯，当前结论以V3_T5/V3_T6及主报告为准。

"""
for f in [WORK/'必读.md',REPO/'必读.md']:f.write_text(header+history,encoding='utf-8')
assert (WORK/'必读.md').read_bytes()==(REPO/'必读.md').read_bytes()
link_count=0
for f in [ROOT/'REPORT.md',ROOT/'REPORT_Astra_final.md']:
 for target in re.findall(r'\]\(<([^>]+)>\)',f.read_text(encoding='utf-8')):
  p=Path(target)
  if p.name!='publication_manifest.json':assert p.exists(),target
  link_count+=1
save('verification/final_links_v3.json',dict(status='PASS',markdown_links_checked=link_count,
 workspace_readme_copies_identical=True,created_utc=NOW))
files=[]
for p in sorted(ROOT.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(ROOT)
 if rel.as_posix()=='publication_manifest.json':continue
 if any(x in {'runtime','document_qa','__pycache__','.git'} for x in rel.parts):continue
 if p.suffix=='.pyc':continue
 files.append(dict(path=rel.as_posix(),bytes=p.stat().st_size,sha256=sha(p)))
save('publication_manifest.json',dict(status='COMPLETE',author='Astra',created_utc=NOW,
 scope='Current V3 delivery including retained historical inputs; current claims use REPORT_Astra_final.md and V3_T5/V3_T6.',
 exclusions=['publication_manifest.json','runtime/','document_qa/','__pycache__/','*.pyc','.git/'],
 workspace_status_sha256=sha(WORK/'必读.md'),files=files))
assert not any(x['path']=='publication_manifest.json' for x in files)
print(json.dumps(dict(status='COMPLETE',publication_files=len(files),bytes=sum(x['bytes'] for x in files),
 word_pages=17,required_pending=0,markdown_links=link_count),ensure_ascii=False))

