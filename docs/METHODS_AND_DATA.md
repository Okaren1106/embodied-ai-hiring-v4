# 方法与数据 / Methods and data

## 观测结构

|层|规模|内容|
|---|---:|---|
|全部语料|1,654 条／24 主体|主职能、活动、广告身份、企业范围与源文|
|整公司范围|1,630 条／23 公司|Amazon FAR 团队单列 24 条|
|具体职能资格目录|1,576 条／17 职能|354 个条目、22 个语境格；整公司子集为 1,552 条|
|工作对象研究|84 条／4 公司|ML 与软件广告的工作对象、产品联系与经验原句|
|V4 配对研究|248 条／496 目标行|105 机器人学习、87 机器人相关软件、56 板级电路|
|同类框架扩展|105 条，26 条共同提及|PyTorch—TensorFlow，在原任务样本上新增关系判读|

源文记录的复合身份包含数据集、公司、招聘来源、岗位 ID 和文本版本哈希。`reading_id`是便于阅读的编号，连接数据时使用 `identity_key`。企业总部、岗位地点和广告语言分别记录。

## 文件地图

### 全样本研究 `broad_study/`

|路径|用途|
|---|---|
|`inputs/accepted_jobs.jsonl.gz`|1,654 条广告的保留正文与字段，恢复后为 JSONL|
|`inputs/stage_c/inputs/rules_v1/inputs/stage_a/jobs.csv`|广告身份和主分类；源文本连接键|
|`inputs/stage_c/tables/T1_company_sample.csv`|主体名单、比较范围与公司分组|
|`inputs/stage_c/tables/T2_company_primary_roles.csv`|公司主职能结构|
|`inputs/stage_c/tables/T4_activity_lineage.csv`|活动证据与 OWNED／PARTICIPATES 关系|
|`configs/Q_catalog_v2_frozen.json`|资格目录、适用职能和条目类型|
|`configs/Q_coding_rules_v2.json`|22 个语境格及展示规则|
|`configs/Q_adjudications/`|逐职能的语义裁决记录|
|`notes/`|源文阅读材料、候选证据与语义审阅队列|
|`review/astra_reviews.jsonl`|有原文定位、旧值、新值、原因和署名的修订事务|
|`tables/Q3_ads_final.csv`|资格目录分析广告与任务归属|
|`tables/Q3_evidence_final.csv`|最终证据的条目、语境、关系、原句及位置|
|`tables/Q3_states_final.csv.gz`|全部 4,402,134 个广告—条目—语境状态格|
|`tables/Q4_*.csv` / `.csv.gz`|各范围、公司、任务、未知界限、模板与剔除公司结果|
|`tables/V3_two_layer_*.csv`|三个任务层的提及与表达方式|
|`tables/D2_decomposition_*.csv`|Galbot—Figure 工程活动的职能构成分解|
|`tables/V3_T6_claims.csv`|综合报告结论与证据的连接|
|`query/`、`index.html`|离线查询与结果浏览页面|
|`scripts/`|构造统计、复核、文档生成及历史研究事务脚本|
|`verification/`|原数值核验与环境记录|

工作对象研究和企业解释表也保留在 `tables/` 与冻结阶段输入中。查询页保存原始版本；下载后可在本地浏览。

### 技术资格研究 `paper_v4/`

|路径|用途|
|---|---|
|`RESEARCH_PROTOCOL.md`|V4 研究问题、比较规则和资格构造|
|`source_snapshot/`|V3 接受输入与哈希清单，包含广告、证据和任务样本|
|`data/`|V4 原文修订覆盖层与判读记录|
|`analysis/paired/`|广告—技术状态、配对、共同提及与权重结果|
|`analysis/empirical/`|公司比较、局部模板、关系诊断和反转距离|
|`extensions/framework_control/`|PyTorch—TensorFlow 的协议、判读、代码与输出|
|`audit/`|独立实现检查结果|
|`literature/`|论文文献与新颖性核查材料|
|`stages/`|各项研究提升完成后的阶段回顾|
|`work/`|主分析、独立核验、证据审阅与文档构建脚本|
|`release/`|主文、表格、补充材料、PDF、Word、Markdown 和图|

## 主要编码字段

|字段或状态|解释|
|---|---|
|`identity_key`|完整广告身份，连接表的唯一键|
|`source_version` / `text_version_hash`|保留广告文本的版本|
|`role` / `primary_code`|主要交付所对应的主职能|
|`task`|职责所对应的主任务；次任务另列|
|`label_code` / `code`|资格目录的条目代码|
|`metric`|本人职责使用／开发、一般、明确必备、优先等语境|
|`branch`|UNCONDITIONAL、CHOICE、EXAMPLE、CONDITIONAL 或 UNRESOLVED 等关系|
|`quote`, `field`, `start`, `end`|证据原句及其原字段位置|
|P|该构造下的确认正例|
|Z|已判断且在该构造下没有正例|
|U|该构造下关系或对象仍未解|
|NA|条目在该广告的目录规则下不适用|
|SOURCE_EXCLUDED|相应来源不足，退出受影响的比较分母|

## 分母和权重

全样本资格目录中，可判断分母 N=P+Z，含未知基数 B=P+Z+U；NA 与 SOURCE_EXCLUDED 独立记录。广告加权与公司等权分别回答广告组成与公司平均表达。探索性组展示通常要求至少 3 家有效公司、N≥20；公司 N<10 带小样本标记。

V4 同任务技术比较采用相同广告基数 B，每条广告有两条目标记录。M 和 H 是已保存表达的出现指标；Q 及其扩展使用 P/Z/U。资格确认正例满足 `Q^P ⊆ H ⊆ M`。PREFERRED 独立于 H、Q 和扩展。

共同提及子样本要求同一广告同时命名两个目标。公司等权、完整资格文本等权与局部父句等权分别检查公司广告贡献和重复表达的影响。未知范围使用构造特定的 U，扩展计数可能使一条 Q 未知转为正例。

## 判读与计算

研究先通过模型辅助原文阅读保存语义证据与裁决，再以确定性程序计算状态和比例。综合研究的二次复核覆盖 469 条全文、760 条边界语境、347 条保留首轮；这三类互斥。V4 对七项源文决策进行覆盖修订，最终 496 行中 Q 为 169 正例、284 无正例、43 未解。

独立数值实现、NumPy 矩阵复算、SQL 去重与源文位置校验分别验证不同计算环节。语义验证和计算一致性在记录中保留各自含义。详见原协议、最终报告与补充材料。

## 版本读取规则

全样本报告保留广泛的职能与活动研究；V4 修订的是技术配对分析。因而引用最新技术资格结论时使用 `paper_v4`；引用工作组织、84 条对象研究与构成分解时使用 `broad_study`。`history/` 与 `archives/` 中较早论文包含当时结论与修订状态。

English: the broad study and V4 paired study have distinct units and denominators. The broad study preserves functions, activities, responsibilities and qualification relations. V4 places two fixed technology targets in each of 248 advertisements and changes only the admitted qualification relation. Evidence spans and composite advertisement identities connect the released tables to captured source text.
