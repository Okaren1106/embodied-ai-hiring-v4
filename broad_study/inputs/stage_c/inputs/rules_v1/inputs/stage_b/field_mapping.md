# 本轮字段与口径补充

研究维度未新增。增加的是已有字段中的产品/事件分行与证据保存信息。

- 同字段以`fact_seq`指定关系目标；每行只引用自身直接支持或明确背景证据。
- `capture_medium`区分原HTTP字节、原PDF加视觉转录、web工具正文；`snapshot_raw_sha256`只用于真正原件；`capture_record_path/sha256`用于工具或读取记录。
- `WEB_TOOL_EXTRACT`允许审阅过的正文作为可追溯证据载体，但必须原样保留工具返回与媒介说明；不补造HTTP状态或原件哈希。
- BMW一份公告拆F02历史运行与F03计划：来源URL相同，不增加独立来源数；各自事件日与同一发布日期配对。
- `RESEARCH_OUTPUT`、`LONG_TERM_GOAL`与`DATE_CONFLICT`只作背景或退出商业产品/场景组。捐赠交付标签不等于付费交付。
- `MEDIA_REPORT`与`MEDIA_STATEMENT`属于同一媒体陈述层，不升级外部确认。

以下为沿用口径：

# 阶段 B 返修版字段与口径

一条广告计一次，广告不等于人数；金额保留原币种与原措辞，不做换算。本轮修复了事实粒度、
时间资格、未知状态、证据关系与资本事件五个方面的口径，下面按表说明。

## 一、表与粒度

| 文件 | 粒度 | 说明 |
|---|---|---|
| `company_facts.csv` | 公司 × 字段 × 主体/范围 × 事件/时期 | 允许同一公司同字段多行（`fact_seq` 区分）；混合断言必须拆开 |
| `company_evidence.csv` | 证据记录 | 新查与继承；`claim_nature` 区分自述、外部确认、媒体、母公司背景、访问记录 |
| `evidence_links.csv` | 事实 × 证据 | 每行一个声明关系；`qualifies_date` 标明该证据是否参与日期判定 |
| `capital_events.csv` | 实际资本事件 | 一个事件连接多条来源；金额、币种、单位、金额性质结构化；估值单列 |
| `company_gaps.csv` | 原 307 缺口逐项 | 每行对应一个继承 `gap_id`；未研究公司保留未查状态 |
| `company_group_mapping.csv` | 公司 × 维度取值 | `comparison_bucket` 决定是否进入严格比较 |
| `search_log.jsonl` | 逐次检索与访问 | 失败同样保留 |

## 二、事实表新增与关键字段

| 字段 | 含义 |
|---|---|
| `fact_seq` | 同公司同字段内的行序；`fact_id` 首行沿用 `F_<company_id>__<field>`，后续行加 `__<n>` |
| `assertion_kind` | 断言类型：披露/观测、招聘要求、母公司背景、边界说明、资本事件、产品线范围、市场范围 |
| `subject_entity` | 该断言的主体（法律实体或团队）；母公司材料的主体写母公司 |
| `subject_scope` | 研究主体范围（整公司 / 团队 / 收购后主体） |
| `product_or_business_scope` | 该断言涉及的产品或业务范围，与主体分开 |
| `event_or_period` | 事件或时期说明，用于表达历史时点与当前状态的差别 |
| `aggregation` | 单值或按范围拆分（多行） |
| `time_basis_evidence_ids` | 参与该断言日期判定的证据（只含 SUPPORTS/REFUTES） |
| `time_reason` | 时点判定的具体理由 |

## 三、`value_status` 枚举

| 值 | 含义 |
|---|---|
| `SUPPORTED_EXTERNAL` | 由公司之外的来源（政府、交易对方、监管、独立渠道）陈述 |
| `COUNTERPARTY_CONFIRMATION` | 交易对方或合作方官方确认 |
| `COMPANY_SELF_REPORT` | 公司自身材料陈述；不升级为独立确认 |
| `MEDIA_STATEMENT` | 媒体报道陈述 |
| `MIXED_SEE_EVIDENCE` | 同一字段内不同项证据强度不同，逐项见证据 |
| `CONFLICT_RESOLVED_BY_SEPARATION` | 存在冲突，按分离规则处理 |
| `PARENT_CONTEXT_ONLY` | 母公司材料，对本主体只作背景 |
| `INHERITED_UNVERIFIED` | 继承值，本轮未复核 |
| `SEARCHED_NOT_FOUND` | 实际查过但未找到（须有检索记录） |
| `NOT_YET_SEARCHED` | 尚未查 |
| `NOT_APPLICABLE` | 命题不适用于该主体 |
| `ACCESS_BLOCKED` | 访问受阻 |
| `CONFLICT` | 来源冲突未解决 |
| `UNKNOWN` | 未确立值；不得写成 NO 或 0 |
| `EXPLICITLY_NEGATED` | 有直接证据明确否定，须限定主体与时间 |

修复要点：**只有公司自述材料支持的断言不再标为 `SUPPORTED_EXTERNAL`**；查后未找到、
尚未查、受阻的行不携带确定值；冲突可保留并列说明，但不生成确定否定组。

## 四、`time_applicability` 判定

事件日与发布日期**分别**与该公司的招聘观察日比较，且只使用该断言的直接支持证据：

| 值 | 判据 |
|---|---|
| `USABLE_AT_OBSERVATION` | 事件日在观察日或之前，且证据在观察日或之前已公开 |
| `RETROSPECTIVE_LATE_PUBLISH` | 事件在观察日或之前，发布晚于观察日（只作背景） |
| `POST_OBSERVATION_EVENT` | 事件本身发生在观察日之后 |
| `DATE_IMPRECISE_SPANS_OBS` | 月/年精度跨过观察日，无法判定先后 |
| `DATE_UNKNOWN` | 没有可用于判定的日期 |
| `NOT_TIME_SENSITIVE` | 结构性事实（如主体归属），不作时点判定 |

月精度一律不补成某月 1 日；HTTP 更新时间、页脚年份与本项目首次看到的时间都不作为发布日期。
母公司背景、其他产品与其他事件的日期不参与该断言的资格计算。不取多条日期中的最早值代替规则。

## 五、关系枚举（`evidence_links.csv`）

| 关系 | 含义 |
|---|---|
| `SUPPORTS` | 该证据直接陈述该断言（主体与范围匹配）；参与成立与日期判定 |
| `REFUTES` | 该证据反驳该断言；可参与日期判定但不成立值 |
| `CONTEXT_ONLY` | 背景材料（母公司、未具名对方、其他范围、弱线索）；不成立值、不定日期 |
| `REPLACES` | 该证据替代另一来源的同一事项，冲突保留 |
| `ACCESS_NOTE` | 访问结果记录（404、正文不可取、检索无结果） |
| `INHERITED_CONTEXT` | 继承材料，仅作追溯 |

关系逐条声明，不由证据 ID 前缀推断；一条被引用但没有声明关系的证据会让构建直接失败。

## 六、比较资格（`company_group_mapping.csv`）

`comparison_bucket` 取 `STRICT_COMPARABLE` / `BACKGROUND_DISPLAY_ONLY` / `EXCLUDED_UNKNOWN` /
`NOT_RESEARCHED`。进入严格比较需同时满足：取值已确立，且时点适用性为 `USABLE_AT_OBSERVATION`
或 `NOT_TIME_SENSITIVE`。背景展示与未确立取值分别单列，不与合格公司混计。

## 七、缺口状态

`stage_b_status` 取值：`RESOLVED_FOUND`、`RESOLVED_NOT_APPLICABLE`、`RESOLVED_PARTIAL`、
`RESOLVED_BY_SEPARATION_RULE`、`NOT_FOUND_NOT_DEFINITE`、`NOT_YET_SEARCHED`、`ACCESS_BLOCKED`、
`NOT_YET_MAPPED_THIS_RUN`、`DEFERRED_TO_STAGE_B_BATCH_2`、`UNRESOLVED_MAPPING`。
本轮未研究的公司，其全部继承缺口（含 `inherited_open_question`）保持
`NOT_YET_MAPPED_THIS_RUN`，通用规则不代替公司专属问题的查证。
