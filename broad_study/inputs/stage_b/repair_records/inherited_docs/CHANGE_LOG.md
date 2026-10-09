# 定向补查变更清单

对照对象：已通过独立复验的 r2 返修底稿
`D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_b_repair_r2\run_20260915T020000Z`

本轮目录：
`D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_b_targeted\run_20260915T030000Z`

代码版本：`stage-b-targeted-v1`。r2 原件、送审包、`stage_a_r3`、研究库、规则、冻结参考未改写。标记：`TARGETED_COLLECTION_PENDING_ACCEPTANCE`。不写 `STAGE_B_COMPLETE`。

任务来源：[17 项定向补查任务](../stage_b_repair_r2_acceptance/run_20260915T020000Z/targeted_collection_queue.csv)。逐项结果见 `TARGETED_TASK_STATUS.md`。

## 一、规模对比

| 表 | r2 底稿 | 本轮 | 说明 |
|---|---:|---:|---|
| 事实行 | 656 | 656 | 行数不变；改的是已有字段取值、证据与时点 |
| 证据行 | 75 | 87 | 新增带日期官方／客户页；未删原证据 ID |
| 关系行 | 425 | 424 | 旧无日期页改为 `CONTEXT_ONLY`，新页 `SUPPORTS` |
| 资本事件 | 24 | 24 | 本轮不追融资金额 |
| 缺口行 | 307 | 307 | 307 项原缺口仍逐项保留 |
| 分组映射 | 300 | 287 | 傅利叶子事实并入父维度后不再出现 `NOT_RESEARCHED` 空行 |

## 二、程序

- `s05_grouping.py`：康复／人形／场景拆分子事实并入 `product_lines`、`target_markets` 父维度；取值仍精确字符串匹配。
- 分组规则版本：`stage-b-targeted-grouping-v1-2026-09-15`。
- 门禁标记改为定向补查待验收；禁止 `STAGE_B_COMPLETE`。

## 三、已写入的业务事实（诚实边界）

| 公司 | 写入 | 不做的升级 |
|---|---|---|
| 傅利叶 | 子事实映射到产品／场景父维度 | 陪伴线仍无合格发布日，不并入康复或人形 |
| Agility | GXO 2024-06-27 客户公告：Digit、Arc、SPANX、多年 RaaS | 媒体 1000 台秋季计划不记已部署 |
| PI | 2024-10-31 π0 研究模型发布 | 演示不是付费；部署为查后未找到 |
| Field AI | 2025-08-20 FFM／跨形态与行业清单 | 「数百现场」保持公司自述 |
| Skild | Brain 2025-07-29；S1 2026-08-18 | ARR／许可博客无日期，仅背景 |
| Dexterity | Mech 2025-03-17；Sagawa 现场验证自 2025-05 | 1000 台是计划；Sagawa 是验证／试点 |
| Nimble | 2024-09-26 新泽西 3PL 节点 | 处理量自述首页无日期，仅背景 |
| 千寻智能 | 官方 Moz1／Spirit v1 正文 | **无发布日**，仍不能进严格比较 |
| Boston Dynamics | DHL 存档稿：Stretch 既有卸货与 1000 台 MOU 分开 | 1000 台是意向，不是已交付 |
| Figure | 2025-10-09 Figure 03；2026-06-30 公司称到达 BMW | BMW 现场为公司公告，不是客户本站 |
| 智元 | 2026-09-08 新闻室 A3／X2 | 15000 台下线是自述，不等于客户交付 |
| 自变量／银河通用／云深处 | 复用已有带日期原文，收窄产品取值 | 不用成立或融资日替代产品日 |
| Amazon FAR | 复核 FTR 团队页仍 404 | 继续退出相应业务组，保留案例 |
| 松延 | 打开新闻中心，正文为空 | 产品日期仍不足，保持背景 |

## 四、比较覆盖（执行方读回，待独立验收）

按公司去重、严格桶（确立取值且观察日可用／非时点敏感）：

| 维度 | r2 严格可用 | 本轮 |
|---|---:|---:|
| 产品形态 | 9/24 | **21/24**（中 10／美 11） |
| 交付形态 | 11/24 | **18/24**（中 7／美 11） |
| 目标场景 | 10/24 | **18/24**（中 7／美 11） |

三项都有：16 家。三项都无：松延、千寻智能、Amazon FAR。

仍不够单独做的比较：付费证据仍只有少数中国公司；`RESEARCH_MODEL_RELEASE` 只有 PI 与 Skild 两家，不能当「软件组」互斥样本。混合业务可多选，组定义需在看岗位差异前固定。

## 五、检索与门禁

- 本轮真实 SEARCH／PAGE_REVIEW 写入 `search_log.jsonl`；历史 192 条派生 SEARCH 仍标 `DERIVED_STATUS_SUMMARY`。
- 自检 45/45、故障 20/20、Node 23/23、离线重建一致、门禁 PASSED。
- 输入锁 536 条目、130 条快照哈希可复算；`input_root_digest` 见 `work/input_lock.json`。
- 未做独立复验、未做真实浏览器验收；不得把本包自检写成独立背书。
