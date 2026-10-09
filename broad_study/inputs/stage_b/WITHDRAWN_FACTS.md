> 此文是前轮历史记录。当前修复结果与新证据入表以[修复报告](REPAIR_REPORT.md)和[证据对照](EVIDENCE_INGESTION.md)为准。前轮“未取得”不代表本轮仍未取得。

# 撤回与替换清单（B2-01）

| 原错误 | 撤回原因 | 替代 |
|---|---|---|
| `B_CN_NOETIX_001` 非夕 Flexiv 王世全访谈 | r3 样本 CN_NOETIX 为松延动力 Noetix，招聘域 noetixrobotics.com | 新 `B_CN_NOETIX_001` 松延官网 Organization schema |
| 8 条事实（主体、产品、交付、场景、演示、融资等）写非夕 | 错绑主体 | 按松延官网重写；无依据字段降为未查或查后未找到 |
| 7 条 STRICT_COMPARABLE 使用 Flexiv 产品/场景标签 | 分组绑定了错误取值 | 更新 grouping_rules_source 中 CN_NOETIX 取值键 |
| 资本/融资把非夕「本月融资」与 Noetix 1B 标题混写 | 主体不一致 | 只保留 Noetix 标题线索，不建观察日可用资本行 |

样本 ID、13 条广告、r3 招聘范围未改。
