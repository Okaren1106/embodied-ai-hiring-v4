# 公司分类与Q2分析规则 v1

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
