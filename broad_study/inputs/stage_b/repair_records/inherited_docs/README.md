# 阶段 B 定向补查包（TARGETED_COLLECTION_PENDING_ACCEPTANCE）

运行目录：`run_20260915T030000Z`；代码版本：`stage-b-targeted-v1`；
输入摘要：`9c5867b195b2b7c6af9ff44eef16f0d8b50bab01c39b1d5dc4d807af859cab67`。

本包在已通过的 r2 返修底稿上做定向业务补查，未重做岗位分类，未改写阶段 A、研究库与规则。
24 家均有公司记录，不等于每字段已查完。逐字段未查/查后未找到仍展示。不得当作阶段 B 完成，也不得进入阶段 C。

## 入口

| 文件 | 用途 |
|---|---|
| `index.html` | 总览页：公司切换、搜索、逐字段事实、证据原文与快照、分组资格、缺口逐项、资本事件 |
| `company_cards/*.md` | 24 家公司卡（含未查公司的待查清单） |
| `company_facts.csv` | 事实表（公司 × 字段 × 主体/范围 × 事件/时期） |
| `company_evidence.csv` | 证据记录与原文定位 |
| `evidence_links.csv` | 事实—证据关系（逐条声明） |
| `capital_events.csv` | 资本事件（金额结构化、估值分离） |
| `company_gaps.csv` | 307 项继承缺口逐项结果 |
| `company_group_mapping.csv` | 分组与比较资格 |
| `verification.json` | 验收自检，绑定本次输入、代码与产物哈希 |
| `field_mapping.md` / `quality_report.md` | 字段口径与质量报告 |
| `release_gate_status.json` | 发布门禁结果（失败时只有失败报告） |
| `CHANGE_LOG.md` | 相对 r2 底稿的定向补查变更 |
| `TARGETED_TASK_STATUS.md` | 17 项补查任务逐项结果 |
| `REPAIR_SELFCHECK.md` | 返修自检与独立验收的区别说明 |

## 复算与复验

```text
python scripts/s01_lock_inputs.py      # 重建输入锁，核验所有输入与快照哈希
python scripts/s02_build_facts.py      # 从研究源重建事实层（含逐条关系声明）
python scripts/s03_build_tables.py     # 生成事实/证据/关系/资本/缺口表
python scripts/s05_grouping.py         # 生成分组映射与规则说明
python scripts/s04_verify.py           # 验收自检（绑定输入与产物哈希）
python scripts/s06_rebuild_and_fault.py# 离线复算 + 完整副本正对照 + 单点故障注入
python scripts/s07_cards_and_html.py   # 公司卡与总览页
node scripts/s08_html_runtime_check.js .  # 页面脚本实际执行检查
python scripts/s09_search_log.py       # 检索日志：区分真实 SEARCH / FETCH / PAGE_REVIEW / 派生总结
python scripts/s11b_search_log_ext.py  # 只标明历史派生行，不再补写 SEARCH
python scripts/s11_release_gate.py     # 发布门禁（通过后再写清单）
```

## 已知边界

- 融资金额未知不作为失败条件；未披露即保留未知。
- 傅利叶人形机器人在新加坡的临床部署证据不足，冲突未关闭。
- 自变量上市状态为查后未找到，保持未知并退出该比较维度。
