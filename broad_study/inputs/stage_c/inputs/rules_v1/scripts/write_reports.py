from pathlib import Path
import csv,json,html
from collections import Counter
R=Path(__file__).resolve().parents[1]
read=lambda n:json.loads((R/n).read_text(encoding='utf-8'))
rows=lambda n:list(csv.DictReader((R/n).open(encoding='utf-8-sig',newline='')))
def write(n,t):(R/n).write_text(t.strip()+'\n',encoding='utf-8')
def mdtable(headers,data):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(str(x).replace('|','／').replace('\n',' ') for x in row)+' |' for row in data])
def main():
 s=read('diagnostics/summary.json');supply=read('decisions/supply_classification.json');q=read('decisions/q2_rules.json');sc=read('decisions/scene_classification.json')
 cc=rows('company_classification.csv');scene=rows('company_scene_assertions.csv');rd=rows('diagnostics/role_coverage.csv');gd=rows('diagnostics/group_role_coverage.csv');dis=rows('q2_display_selection.csv');ev=rows('evidence_index.csv');ip=rows('diagnostics/q2_item_interpretation.csv')
 names={r['company_id']:r['company_name'] for r in cc};roles={r['role_code']:r['role_name'] for r in rd}
 group_table=mdtable(['归类','公司数','广告数','公司'],[(supply['groups'][g]['name'],s['strata_counts'][g],s['strata_ads'][g],'、'.join(r['company_name'] for r in cc if r['stratum']==g)) for g in supply['groups']])
 scene_table=mdtable(['场景连接','当前连接公司数','有实际使用/捐赠/科研使用记录','解释范围'],[(sc['scenes'][g],n,s['scene_observed_use_donation_research'].get(g,0),'定位与使用分列；可多属') for g,n in s['scene_connections'].items()])
 role_table=mdtable(['职能','全部广告','全部公司','整公司广告/公司','技能CODED/未提/目录外','选定'],[(r['role_name'],r['n_ads_all'],r['n_companies_all'],r['n_ads_main_companies']+'/'+r['n_main_companies'],r['skills_CODED']+'/'+r['skills_NOT_MENTIONED']+'/'+r['skills_UNMAPPED'],r['selected']) for r in rd])
 rule_support=mdtable(['供给范围','职能','有该职能公司数','基础可评价广告','最大公司占比','允许展示'],[(supply['groups'][r['group']]['name'],roles[r['role_code']],r['companies_with_denominator'],r['n_assessable_ads'],f"{float(r['largest_company_share'])*100:.1f}%",'有条件汇总' if r['display_status']=='EXPLORATORY_SUMMARY_ELIGIBLE' else '公司点值/单列') for r in gd if r['dimension']=='skills' and r['group'] in ['SYSTEM_PRODUCTS','CROSS_BODY_MODELS']])
 write('REPORT.md',f'''# 公司分类与Q2分析规则 v1：执行结果

日期：2026-09-15。执行者按用户要求亲自逐公司判断，未委派代理。本版为分析规则与分类交付；公司事实沿用已验收后补充包，广告沿用阶段A r3，不重分类招聘数据。

## 结论

1. 24家公司已逐一归类：18家整机/机器人系统、3家跨本体模型/软件；帕西尼的部件与系统组合、Nimble的机器人履单运营、FAR内部团队分别单列。
2. 产品供给、应用连接和主体范围分开。51条场景判断组成24×7场景状态表；无证据不记为否定，未来/演示/无日期材料不记当前实际使用。
3. Q2固定ML/AI工程与软件/平台两个职能：全样本159/181条，整公司主比较156/180条；FAR的3/1条保留团队点值。
4. 具体工具按全体整公司广告中的覆盖排序：ML/AI工程10项，软件/平台9项；各8项技术概念。泛称单列，不凑满数量，不按业务组或国家差距选标签。
5. 已落实逐标签×要求语境×分支的三态解释：明确记录、关系未知、未记录正向。未知退出对应指标分母，不能记成没有要求。

## 1. 公司供给归类

{group_table}

这是观察时点已确立的公开供给形态，不是按营收给公司判定唯一主业。整机组允许自研模型；跨本体模型组包括研究型模型发布，不宣称已许可或付费。帕西尼、Nimble不被丢出研究，仍完整参加公司层面的Q1—Q3；FAR按团队范围保留。

详细逐家公司理由、事实ID和场景见[分类说明](COMPANY_CLASSIFICATION.md)及[分类表](company_classification.csv)。

## 2. 场景分类

{scene_table}

“连接”指明确现行定位、当前提供或实际应用之一。它不是已交付公司数，也不是市场份额。三个例子：逐际科研平台预订属于当前提供；松延学校捐赠属于已观察教育用途；宇树G1被研究使用属于第三方科研应用。三者不合并成付费教育市场。

制造、物流和商业服务可作重叠分面的探索性描述；巡检、医疗/照护、家庭、科研教育本版以公司/任务案例为主。后四类数量少或任务、来源状态差别大，达到公司数门槛也不自动授权业务组均值。

公司可属于多个场景，必须显示交集。[场景矩阵](company_scene_matrix.csv)区分当前连接、仅背景/计划和未确立；未确立不等于不存在。具体状态和所选事实片段见[51条判断](company_scene_assertions.csv)。

## 3. Q2职能选择

{role_table}

选取学习/模型工程和运行软件/平台两个可解释锚点，覆盖足够且有互补性。制造/质量/供应链与硬件/电气也有可用数据，未选不是因为无数据：本版两题预算优先软件技术组合，它们保留在Q1/Q3与完整覆盖附表；Q2不能外推为全部技术岗位要求。完整取舍见[决策讨论](DECISION_MEMO.md)。

职能门槛按整公司主体检查：至少100条广告、18家公司、5家公司各有5条广告，目标维度来源可评价比例≥80%。门槛只是实施标准，不能证明估计精度；研究价值仍由明确问题决定。此规则是在已知覆盖情况下制定，不冒称盲选或事前注册。

## 4. 哪些比较目前能做

{rule_support}

跨本体模型组的ML/AI工程只有17条，低于本版20条汇总展示门槛，保留3家公司点值，不给跨供给组均值差。软件/平台38条达到基础门槛，但Field AI占23/38；必须并列公司等权/广告加权并剔除Field AI检查，剔除后只剩2家公司，不能宣称跨公司稳定。

跨本体模型3家公司全部来自美国，所以供给组差异不能解释为国家差异。仅在同一供给形态、两国各≥3家且≥20条，并满足范围限制时，才允许辅助国家描述。

上述数量都是基础范围。每一个标签×语境×分支图格，还必须排除关系UNKNOWN后重新核对公司数、广告数和缺失；基础门槛通过不等于所有技能图格都可汇总。

## 5. 固定的分析边界

- 一个广告身份和正文版本只计一次；原1654基准、17具体职能和2结构类不改。1576条具体主职能广告用于全职能覆盖诊断，复合/多方向保留Q3原结构。
- 同标签可同时有职责使用和一般要求；各自去重，不把不同语境或任选分支相加为同时必须掌握。
- UNMAPPED保留在基础分母，另报目录外状态及原词。指标是已有目录标签的记录覆盖，不声称完整真实能力需求；目录可直接评价子集并列作敏感性。
- 模型发布、产品提供、部署、付款、持续运行各保留性质；不制作商业化成熟度排名，不做国家产业优劣判断。
- 正式Q1—Q3结果表、组内比例、图表和解释性结论尚未在本包计算。接续时执行已固定规则，不再按结果大小换组或换技能。

## 交付与复算

[规则正文](Q2_RULES.md) · [分类与取舍讨论](DECISION_MEMO.md) · [后续比较登记](comparison_registry.json) · [数据及证据索引](evidence_index.csv) · [验证结果](verification/result.json)

本包封存17份A/B输入表及112份实际证据文件，来源清单逐文件记录原路径和哈希。脚本不联网，不改旧包；`scripts/reproduce.py --output <新的空目录>`核验输入与设计锁后重建本包派生表和说明。完整说明见[README](README.md)。
''')
 company_lines=['# 24家公司分类及逐项理由','',group_table,'','## 逐公司说明','']
 for c in cc:
  sr=[r for r in scene if r['company_id']==c['company_id']]
  company_lines += [f"### {c['company_name']}（{c['company_id']}）",'',f"**{c['stratum_name']}**；范围：{c['scope']}；广告：{c['n_ads']}；观察日：{c['observation_date']}。",'',c['decision_reason'],'',f"边界：{c['caveat']}",'',f"事实依据：`{c['basis_fact_ids']}`。证据：`{c['basis_evidence_ids']}`。",'',mdtable(['场景','状态','采用的事实片段','限制'],[(r['scene_name'],r['state'],r['selected_claim'],r['decision_reason']) for r in sr]),'']
 company_lines += ['原文URL及本地正文路径见[evidence_index.csv](evidence_index.csv)；事实全文见[company_facts.csv](inputs/stage_b/company_facts.csv)。分类是分析者判断，不能将分类说明冒充来源原话。']
 write('COMPANY_CLASSIFICATION.md','\n'.join(company_lines))
 write('DECISION_MEMO.md','''# 分类与Q2选择：决策讨论

## 一、采用什么归类方式

本次目标是解释招聘组合与公开产品/业务的对应关系。归类先依据B轮事实，不查看业务组技能差距。已知Q1和覆盖诊断不隐藏，因此这是有记录的探索性研究设计，而不是事前注册。

### 方案A：按人形、四足、模型给每家公司唯一分类

不采用作主分组。机器人外形与模型是不同维度；Boston Dynamics、智元和宇树有多种形态，Figure等整机公司也开发模型。按单一标签容易把同类公司拆开或丢失业务组合，且全公司招聘不能自动分给某一产品。

### 方案B：按“通用/专用”二分

不采用。通用可指身体形态、跨任务能力、平台宣传或计划市场；Agility的通用人形本体与具体仓库作业不能仅凭一个通用标签与家庭机器人等同。现有证据不足以统一衡量通用程度。

### 方案C：按商业化成熟程度高低排序

不采用。现有材料有公司自述、媒体、客户确认、捐赠、试点、订单和长期目标。不同事件不是固定的顺序量表，缺少付款记录不是未商业化。资本金额、母公司规模、logo也不作为代理分数。

### 采用：公开供给形态归类＋场景多重连接＋主体边界

整机/系统产品与跨本体模型/软件是当前能够用事实定义且有多家公司支持的两个主要供给范围。其余明确的不同模式单列，不为凑组挤入：帕西尼有明确触觉部件供给与系统组合；Nimble公开交付3PL履单服务；FAR为内部团队。

独立部件供给不同于整机企业自研核心零部件。因此自变量的全栈自研记录不自动与帕西尼触觉芯片量产供应等同。Nimble使用自有机器人不等于向客户卖机器人。FAR使用G1不等于研发/销售G1。以上是可检验的具体边界，不是认为这些公司与其他业务绝无重叠。

主表的互斥归类是本版组织比较的约定，不是唯一真实产业分类。18家系统组本身仍有异质性：保留多产品、仅媒体依据及收购边界标记，结果阶段须检查这些公司是否主导差异。系统组里的模型能力不被删去，跨本体模型组也不称纯软件企业。

## 二、为何没有把所有场景都变成正式业务组

本版逐条选取事实中的具体子句，将现行定位、实际使用、预订提供、捐赠、科研使用、演示、未来及无日期记录分开。某篇报道同时说“初期制造、以后家庭”，不能把两个场景同样计为当前业务。

制造产线10家与物流11家、商业服务4家可以作为公司分面描述，但相互重叠，不能把每组当成独立样本，更不能把其余企业当作确定的反面组。公司数只对唯一company_id计数，事实多条不增加公司权重。

医疗/照护有3家，但分别包括康复治疗、院内物流和养老操作；把它们混成一类技术任务会损害解释。家庭3家主要是现行定位，不证明家用交付。科研教育4家包含平台发售、捐赠及第三方实验使用；它们说明不同应用联系。巡检只有3家且任务及实用证据不同。这些在v1以任务案例呈现，避免以数值门槛替代实质可比性。

## 三、Q2为何选择ML/AI工程和软件/平台

研究要连接公司产品、技术能力与工作分工。本版选取两个互补锚点：学习/模型开发工程，以及部署这些能力所需的运行软件/平台。它们并非全部技术岗位，但职能边界可解释，跨公司覆盖高，已有技能和技术记录充分。

制造/质量/供应链215条、硬件/电气126条同样有可用数据；不选择它们不是数据失败。制造主类横跨制造、质量与供应链工作，如果本次作为核心Q2需要更细任务解释；本版两职能范围优先软件技术。该选择有研究者判断，报告明确记录，不能称客观唯一最优选择。其余17类均保留诊断，Q1/Q3仍完整。

控制/规划有75条、感知47条、研究科学32条，进一步分公司和业务后有限。不会为扩充这些职能而把结构类分支展开成多个同岗，或降低阈值直到得到预期结果。

## 四、覆盖足够与可解释不是一回事

两个所选职能的基础来源可评价率均为100%，但并非每个关系都已解决。选定职能中技能记录涉及53条ML/AI广告、76条软件广告含至少一个未解决关系；技术记录对应21条和7条。这是“至少一项不明”，不表示这些广告所有标签都不可用。

所以采用标签×语境×分支三态：同指标已有明确正向记录→PRESENT；否则有可能影响判断的未解决项→UNKNOWN；其余→NO_RECORDED_POSITIVE。UNKNOWN不算0，退出对应指标分母；广告的其他可解释标签继续保留。否定、背景和协作对象仍分别保存。这是分析层的保守使用规则，不改变用户认可的原编码或人工复核状态。

目录外词同样不能凭状态改成无技能。主结果解释为“既有目录已记录覆盖”，并列目录状态、原词和目录可直接评价子集；不假装完成了未实施的扩充目录。

## 五、哪些预期比较需要降级

跨本体模型组ML/AI仅17条，3家公司都不足10条；本版不发布该组均值差，只展示公司点值。软件/平台有38条，但Field AI占23条。去掉Field AI后仅2家公司，已经不满足组级汇总门槛；因此该比较最多是小样本、来源范围受限的探索性描述。

跨本体模型组的3家公司都是美国主体，供给类型与国家没有充分交叉。它与系统组的差异无法用于识别国家影响。国家辅助描述只在同一供给形态有实际两侧覆盖时做，仍不能代表全国行业。

## 六、冻结与后续修订

本版固定后，Q1—Q3正式结果按相同输入、成员、分母和标签选择生成。新增证据、明确程序错误可以建立新版本修订，但须列出理由、成员/结果变动，并保留v1对照。不能因结果不显著或不符合预期而改分组、丢公司、替换技能。

本轮完成规则与分类，未计算组间技能率差，未开始因果解释或商业化高低判断。使用前核验design_lock和source_lock；原阶段A/B、研究库与1654认可参考均保持只读。
''')
 tool_lists=[]
 for code in q['primary_roles']:
  tool_lists += [f"### {roles[code]}",'']
  for dim,title in [('skills','具体工具'),('technical_concepts','技术概念')]:tool_lists += [f"**{title}**："+'、'.join(r['label_name'] for r in dis if r['role_code']==code and r['dimension']==dim and r['main_display']=='YES')+'。','']
 write('Q2_RULES.md','''# Q2规则 v1（已固定）

## 1. 研究对象与职能

选定`RF_ML_AI_ENGINEERING`和`RF_ROBOTICS_SOFTWARE`，要求主职能CODED且直接为该具体代码。全样本159/181条；FAR团队3/1条单列；整公司主比较156/180条。所有原1654广告保持原状，其他职能由Q1/Q3覆盖。

## 2. 先确定基础范围，再逐指标确定分母

1. 基础来源可评价状态为CODED、NOT_MENTIONED、UNMAPPED。来源不足退出该维度，未知状态使脚本停止。技能不明不自动连带退出技术维度。
2. 对某个标签、语境和分支，按原始要求树追踪所有祖先。不能只读叶子或把OR、SOME_OF、EXAMPLE展平成ALL。
3. 同指标有明确正向记录，广告记PRESENT；否则有可能影响该指标的未解决关系/语境，记UNKNOWN；其余记NO_RECORDED_POSITIVE。
4. 指标分母为基础范围中PRESENT和NO_RECORDED_POSITIVE的广告数；UNKNOWN单列。分子只计PRESENT。NO_RECORDED_POSITIVE表示未记录到此类正向标签，不证明真实能力需求不存在。
5. 基础总量、UNMAPPED、来源不足、该指标关系UNKNOWN、最终分母都须列出。目录可直接评价子集仅CODED+NOT_MENTIONED，作为并列敏感性，不能声称已完全覆盖目录外词。

代码实现为`build_rules.label_state`；逐广告基础资格在`diagnostics/admission.csv`，原条目的语境解释在`q2_item_interpretation.csv`；主展示标签的未知身份清单在`q2_label_interpretability.csv`。诊断文件均位于diagnostics目录。

## 3. 语境与计数

- 职责本人使用与本人开发分别统计；协作、采购、招聘、教学或产品定义对象不计成本人使用。
- 硬性要求、一般要求、优先分别统计；要求分支分为无条件、任选、示例、任选且示例、未解决。
- “A或B”可以支持明确的任选提及，不能支持A和B分别都是无条件要求。否定和背景不进正向要求。
- 先筛语境/关系，再按广告身份×标签×语境×分支去重；同一广告两次提及不计两份。不同语境率可重叠，不相加解释为100%构成。
- 泛称保留独立说明，不推断任一具体工具；目录外原词不自动新建标签。

## 4. 主图标签选择

仅按所选职能的整公司可评价广告，合并明确正向本人职责与要求提及；允许任选/示例参与“已提及”覆盖排序，最终图中仍拆语境。按覆盖公司数降序、广告数降序、标签代码升序固定；至少5家公司且10条广告。具体技能最多10项，技术概念最多8项，不足不补凑；泛称SK_GENERIC_ML_FRAMEWORK、SK_GENERIC_LANGUAGE、SK_CAD单列。完整排名和未选项目见`q2_display_selection.csv`。

'''+'\n'.join(tool_lists)+'''
## 5. 汇总和比较许可

先展示公司点值和分母。业务组必须有至少3家该指标分母大于0的公司、至少20条最终可解释广告，才可给探索性均值；每公司不足10条提示小样本。这里门槛不是显著性检验或充分精度保证。

公司等权：先求每家公司PRESENT/最终分母，再对有效公司取算术平均。广告加权：合并PRESENT数除以合并最终分母。没有该职能或最终分母为0的公司记NA，不放入平均当作0。

最大公司广告占比超过50%时提示集中；逐一剔除时同时记录剩余公司数、广告数和门槛是否失效。FAR团队、帕西尼产品组合、Nimble运营服务单列，不为凑公司数合并。

场景可多重归属，制造/物流/商业服务以重叠分面描述，显示交集，不做独立互斥样本的均值差推断。巡检、医疗照护、家庭、科研教育v1按案例展示，原因见决策备忘录。未确立不是“无此业务”。

国家只作同供给范围内的辅助描述，两国各至少3家、20条，且需重新核对每一指标最终覆盖。跨本体模型全为美国公司，不能从跨供给组差异推断国家影响。

## 6. 必做敏感性与结论范围

公司等权/广告加权；逐一剔除公司；整公司/团队单列；剔除已明确多产品范围的Fourier和Boston Dynamics；排除归组仅依赖媒体者；主分母/目录可直接评价子集；场景全部连接/实际使用子集。每个子集也重查展示门槛。

“仅媒体”敏感性针对归组依据的性质，不等于对整个公司的所有事实作信誉打分；原media_only_basis派生列可复算。实际使用子集包括捐赠与第三方研究，若讨论商业交付，必须再排除这些类型并核查具体供给/付款事实。

结论只限当前样本公开广告与已保存业务证据的对应关系。不能推出员工人数、实际技能水平、因果关系、市场份额或国家产业优劣。
''')
 registry={'version':'1.0','no_outcome_contrasts_computed':True,'comparisons':[
 {'id':'SUPPLY_SOFTWARE','role':'RF_ROBOTICS_SOFTWARE','groups':['SYSTEM_PRODUCTS','CROSS_BODY_MODELS'],'status':'CONDITIONAL_EXPLORATORY','base_ads':[124,38],'conditions':['每一标签语境重算未知排除后的分母和3家/20条门槛','Field AI集中23/38须披露及剔除','不作国家解释']},
 {'id':'SUPPLY_ML','role':'RF_ML_AI_ENGINEERING','groups':['SYSTEM_PRODUCTS','CROSS_BODY_MODELS'],'status':'COMPANY_POINTS_ONLY','reason':'模型组仅17条，不作组均值差'},
 {'id':'SCENE_FACETS','roles':q['primary_roles'],'scenes':['MANUFACTURING','LOGISTICS','RETAIL_SERVICE'],'status':'OVERLAPPING_DESCRIPTIVE_FACETS','conditions':['明示交集','目标/使用状态并列','不作独立样本或反面组差异推断','逐指标门槛重查']},
 {'id':'SCENE_CASES','scenes':['FIELD_INSPECTION','HEALTHCARE_CARE','HOME','RESEARCH_EDUCATION'],'status':'CASE_ONLY','reason':'少量公司、不同任务或目标/实用证据异质，不自动以3家门槛授权均值'},
 {'id':'COUNTRY_WITHIN_SYSTEMS','roles':q['primary_roles'],'status':'AUXILIARY_CONDITIONAL','conditions':['仅SYSTEM_PRODUCTS范围','两侧各3家20条最终可解释广告','范围/渠道/时点限制及敏感性','不代表国家产业']},
 {'id':'SPECIAL_CASES','companies':['CN_PAXINI','US_NIMBLE','US_AMAZON_FTR'],'status':'SEPARATE_POINTS_AND_CASES','reason':'不删除广告，不为组均值凑数'}]}
 (R/'comparison_registry.json').write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 write('README.md','''# 公司分类与Q2分析规则 v1

**规则与24家公司分类已完成；验证结果见verification/result.json。** 本版为作者自行验证，不冒称独立验收。正式Q1—Q3结果和业务差异解释尚待下一步执行。

- [执行报告](REPORT.md)：分类、覆盖与本轮结论。
- [逐公司分类](COMPANY_CLASSIFICATION.md)、[分类CSV](company_classification.csv)。
- [取舍讨论](DECISION_MEMO.md)、[Q2规则](Q2_RULES.md)、[正式比较许可](comparison_registry.json)。
- [场景状态矩阵](company_scene_matrix.csv)、[事实片段判断](company_scene_assertions.csv)、[证据索引](evidence_index.csv)。
- [职能覆盖](diagnostics/role_coverage.csv)、[公司职能覆盖](diagnostics/company_role_coverage.csv)、[业务组覆盖](diagnostics/group_role_coverage.csv)、[显示标签选择](q2_display_selection.csv)。
- [标签解释资格](diagnostics/q2_label_interpretability.csv)：未知关系不计0。
- [可读HTML](index.html)。

## 封存与复算

inputs/source_lock.json锁定输入表与实际证据文件；design_lock.json锁定人工判断及执行脚本；release_checksums.json覆盖完整交付包。校验采用SHA-256。

使用Python标准库，无网络或第三方库依赖。执行：

```text
python -B -X utf8 scripts/verify_rules.py
python -B -X utf8 scripts/reproduce.py --output <新的不存在的目录>
```

复算入口核验封存与设计，不读取现场研究库；在隔离临时目录构建并验证，通过后发布到新的空目录，拒绝覆盖。旧阶段A/B包、研究库、冻结1654与规则文件保持原样。author_decisions.py为人工决定的编制记录，不是重新自动分类入口。

## 状态

RULES_FIXED_AND_CLASSIFIED。完成本轮归类和分析设计；已知事实缺口仍按背景、未知和案例范围保留。规则固定不意味着全部公司业务已查明，也不意味着Q1—Q3正式比较已完成。
''')
 # Static reader: all facts remain readable without JavaScript or external assets.
 esc=html.escape
 def htable(headers,data):return '<table><thead><tr>'+''.join('<th>'+esc(str(x))+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(str(x))+'</td>' for x in row)+'</tr>' for row in data)+'</tbody></table>'
 cards=[];evby={e['evidence_id']:e for e in ev}
 for c in cc:
  sr=[r for r in scene if r['company_id']==c['company_id']];eids=c['basis_evidence_ids'].split('|')
  evidence_links=' · '.join('<a href="'+esc(evby[e]['local_text_path'])+'">'+esc(e)+'</a>' for e in eids)
  cards.append('<section id="'+c['company_id']+'"><h2>'+esc(c['company_name'])+' <small>'+esc(c['company_id'])+'</small></h2><p class="tag">'+esc(c['stratum_name'])+' · '+c['n_ads']+' 条广告</p><p>'+esc(c['decision_reason'])+'</p><p class="caveat">'+esc(c['caveat'])+'</p>'+htable(['场景','状态','采用的事实片段','限制'],[(r['scene_name'],r['state'],r['selected_claim'],r['decision_reason']) for r in sr])+'<p>本地证据：'+evidence_links+'</p></section>')
 nav=' · '.join('<a href="#'+r['company_id']+'">'+esc(r['company_name'])+'</a>' for r in cc)
 write('index.html','''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>公司分类与Q2规则 v1</title><style>body{margin:0;background:#f4f6f8;color:#172635;font:16px/1.7 "Microsoft YaHei",sans-serif}main{max-width:1280px;margin:auto;padding:32px}h1{font-size:30px}h2{font-size:22px;margin-top:0}small{font-size:13px;color:#657386}a{color:#126395;text-decoration:none}nav{line-height:2.2}section,.summary{background:white;padding:26px;margin:24px 0;border:1px solid #dce3eb;border-radius:10px;scroll-margin:20px}.tag{font-weight:bold;color:#126395}.caveat{border-left:3px solid #ddac54;padding-left:12px;color:#536273}table{border-collapse:collapse;width:100%;font-size:14px;margin:14px 0}th,td{border-bottom:1px solid #dce3eb;padding:10px;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:#edf2f7}td:nth-child(2){max-width:210px}@media print{body{background:white}main{padding:0}section{break-inside:avoid}nav{display:none}}</style><main><h1>公司分类与 Q2 分析规则 v1</h1><p>24家公司 · 1654条广告 · 规则已固定 · 正式组间结果尚未计算</p><div class="summary"><h2>本轮决定</h2><p>18家整机/系统、3家跨本体模型；帕西尼、Nimble与FAR分别单列。Q2采用ML/AI工程和软件/平台；未知要求关系逐标签处理，不记成0。</p><p>分类依据为已封存公司事实；不推断唯一收入主业。场景可重叠，定位、使用、捐赠、演示和计划分别记录。</p><p><a href="REPORT.md">执行报告</a> · <a href="DECISION_MEMO.md">取舍讨论</a> · <a href="Q2_RULES.md">Q2规则</a> · <a href="q2_display_selection.csv">标签选择</a> · <a href="verification/result.json">验证</a></p></div><nav>'''+nav+'</nav>'+''.join(cards)+'</main></html>')
 print('Reports, comparison registry and static overview written.')
if __name__=='__main__':main()
