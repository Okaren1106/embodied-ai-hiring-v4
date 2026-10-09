> 此文是前轮历史记录。当前修复结果与新证据入表以[修复报告](REPAIR_REPORT.md)和[证据对照](EVIDENCE_INGESTION.md)为准。前轮“未取得”不代表本轮仍未取得。

# 17 项定向补查任务结果

对照 [targeted_collection_queue.csv](../stage_b_repair_r2_acceptance/run_20260915T020000Z/targeted_collection_queue.csv)。只处理列明字段；不扩公司、不追全部未查背景字段。

| 任务 | 结果 | 严格比较 | 说明 |
|---|---|---|---|
| B_TARGET_01 傅利叶映射 | 已执行 | 产品／场景父维度现有严格组 | `s05` 将拆分子事实并入父维度；陪伴线仍无合格发布日 |
| B_TARGET_02 Agility RaaS | 已执行 | 交付形态 `RAAS` | GXO 2024-06-27 客户公告；日期与断言一并补入 |
| B_TARGET_03 PI | 已执行 | 产品／交付／场景可用；部署退出 | π0 2024-10-31；部署查后未找到 |
| B_TARGET_04 Field AI | 已执行 | 三业务维可用 | 2025-08-20 官方页；部署量为自述 |
| B_TARGET_05 Skild | 已执行 | 三业务维可用 | Brain 与 S1 两条带日期发布 |
| B_TARGET_06 千寻智能 | 部分完成 | **仍退出产品严格组** | 官方 Moz1 正文无发布日 |
| B_TARGET_07 Agility 业务 | 已执行 | 产品／场景／部署可用 | 与 B_TARGET_02 同一客户页 |
| B_TARGET_08 Dexterity | 已执行 | 三业务维可用 | Mech 发布 + Sagawa 验证／试点 |
| B_TARGET_09 Nimble | 已执行 | 三业务维可用 | 2024-09-26 新泽西履单节点 |
| B_TARGET_10 Stretch | 已执行 | 产品含 Stretch，与 Atlas／Spot 分开 | DHL 存档稿；1000 台记意向 |
| B_TARGET_11 FAR | 已记录 | 继续退出相应业务组 | FTR 团队页仍 404 |
| B_TARGET_12 智元 | 已执行 | 产品可用 | 2026-09-08 新闻室 A3／X2 |
| B_TARGET_13 Figure | 已执行 | 三业务维可用 | Figure 03 发布；BMW 为公司自述 |
| B_TARGET_14 松延 | 未解决 | 仍退出 | 新闻页正文为空 |
| B_TARGET_15 自变量 | 已执行 | 产品收窄为有日期的 0755 | 复用 `B_CN_XSQUARE_006` |
| B_TARGET_16 银河通用 | 已执行 | 产品收窄为带日期零售报道 | 复用 `B_CN_GALBOT_001` |
| B_TARGET_17 云深处 | 已执行 | 产品收窄为带日期四足类别 | 复用 `B_CN_DEEPROBOTICS_001` |
