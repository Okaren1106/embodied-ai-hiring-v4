# 阶段 B 返修版质量报告

本报告数字全部由生成的表读回；不是独立验收结论，也不声称用户已逐条复核。

## 一、范围

- 运行目录：`run_20260915T030000Z`；标记：`TARGETED_COLLECTION_PENDING_ACCEPTANCE`（未写 `STAGE_B_COMPLETE`）。
- 本轮 24 家均有公司记录（CN_AGIBOT, CN_ASTRIBOT, CN_DEEPROBOTICS, CN_FOURIER, CN_GALAXEA, CN_GALBOT, CN_LIMX, CN_NOETIX, CN_PAXINI, CN_SPIRITAI, CN_UNITREE, CN_XSQUARE, US_AGILITY, US_AMAZON_FTR, US_APPTRONIK, US_BOSTON_DYNAMICS, US_DEXTERITY, US_DILIGENT, US_FIELD_AI, US_FIGURE, US_NIMBLE, US_PHYSICAL_INTELLIGENCE, US_PICKLE, US_SKILD）。
- 字段级未查/查后未找到仍单独展示；不得把 24 家有记录写成每字段已查完。
- 招聘分类、研究库、r3 底稿与冻结参考未改写（见输入锁与验收自检 L5、D7）。

## 二、产出

- 事实行：656（只由 60 个字段承载；同字段多行用于主体/范围/事件拆分）
- 证据行：87（其中 STAGE_B_NEW 87）
- 关系行：424；关系分布：`SUPPORTS`×395、`CONTEXT_ONLY`×26、`ACCESS_NOTE`×3
- 资本事件：24 行
- 缺口行：307（原 307 项逐项保留）
- 分组映射行：287

## 三、证据性质分布（事实行）

| 证据性质 | 行数 |
|---|---|
| `NOT_YET_SEARCHED` | 209 |
| `COMPANY_SELF_REPORT` | 132 |
| `MEDIA_STATEMENT` | 130 |
| `NOT_APPLICABLE` | 53 |
| `INHERITED_UNVERIFIED` | 49 |
| `SUPPORTED_EXTERNAL` | 34 |
| `SEARCHED_NOT_FOUND` | 20 |
| `COUNTERPARTY_CONFIRMATION` | 16 |
| `MIXED_SEE_EVIDENCE` | 5 |
| `DATE_UNKNOWN` | 3 |
| `DATE_IMPRECISE_SPANS_OBS` | 1 |
| `MEDIA_AND_THIRD_PARTY_RECORD` | 1 |
| `CONFLICT_RESOLVED_BY_SEPARATION` | 1 |
| `ACCESS_BLOCKED` | 1 |
| `PARENT_CONTEXT_ONLY` | 1 |

## 四、时点适用性分布（事实行）

| 时点 | 行数 |
|---|---|
| `DATE_UNKNOWN` | 407 |
| `USABLE_AT_OBSERVATION` | 192 |
| `NOT_TIME_SENSITIVE` | 53 |
| `DATE_IMPRECISE_SPANS_OBS` | 4 |

## 五、缺口状态分布（307 项）

| 状态 | 行数 |
|---|---|
| `RESOLVED_FOUND` | 158 |
| `NOT_YET_SEARCHED` | 89 |
| `RESOLVED_PARTIAL` | 37 |
| `NOT_FOUND_NOT_DEFINITE` | 17 |
| `RESOLVED_NOT_APPLICABLE` | 4 |
| `RESOLVED_BY_SEPARATION_RULE` | 1 |
| `DEFERRED_TO_STAGE_B_BATCH_2` | 1 |

## 六、比较资格分布

| 桶 | 行数 |
|---|---|
| `STRICT_COMPARABLE` | 170 |
| `EXCLUDED_UNKNOWN` | 72 |
| `BACKGROUND_DISPLAY_ONLY` | 45 |

## 七、验证结果（执行方自检）

- 验收自检：45/45 通过，失败 0。
- 受控故障实验：20/20 探针按预期被拒绝，正对照 通过。
- 离线复算：五张核心表与发布版本逐字节一致。
- 输入锁：包含 536 个文件，输入摘要 `9c5867b195b2b7c6…`，代码摘要 `c4ca5882eea56fed…`；快照声明哈希全部可复算。

## 八、本轮明确未做的事情

1. 未对 24 家穷尽检索；未补造任何金额、日期或客户。
2. 未把未查、查后未找到、访问受阻写成否定结论。
3. 未用母公司材料支撑 FAR 团队断言；未把招聘职责当作公司已开展的事实。
4. 未把媒体口径升级为独立确认；未把估计或冲突值合并成单一数字。
5. 未修改阶段 A 交付、研究库、规则与冻结参考；未进入阶段 C。

