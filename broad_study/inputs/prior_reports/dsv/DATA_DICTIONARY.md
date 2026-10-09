# 数据表目录

全部CSV为UTF-8 BOM，可用Excel导入。数值比例为0—1，NA在CSV中为空，计数为整数。

| 文件 | 行数 | 用途 |
|---|---|---|
| [D1_q1_coverage_concentration.csv](tables/D1_q1_coverage_concentration.csv) | 22 | Q1各主职能的公司覆盖、集中度、四分位与两种权重；含未明确状态单列行 |
| [D2_q2_coverage_concentration.csv](tables/D2_q2_coverage_concentration.csv) | 14490 | Q2全部标签×语境×分支的覆盖与集中度，分母贡献与正向贡献分列 |
| [D2_q3_coverage_concentration.csv](tables/D2_q3_coverage_concentration.csv) | 16 | Q3八类活动的公司覆盖、集中度与两种权重 |
| [D3_role_activity_bidirectional.csv](tables/D3_role_activity_bidirectional.csv) | 336 | 主职能×活动双向条件比例，含结构类与未明确状态 |
| [D4_activity_pair_cooccurrence.csv](tables/D4_activity_pair_cooccurrence.csv) | 6 | 三组活动配对的无条件/条件性/仅任选/未解决计数与主率 |
| [D4_activity_pair_lineage.csv](tables/D4_activity_pair_lineage.csv) | 622 | 每条共现判定的广告ID、分支定位、原文片段与理由 |
| [D5_activity_pair_structure.csv](tables/D5_activity_pair_structure.csv) | 95 | 各配对的所属职能与公司分布及集中度 |
| [D6_business_responsibility_long.csv](tables/D6_business_responsibility_long.csv) | 680 | 24主体业务环节与责任主体派生长表，保留fact_id与evidence_ids |
| [D6b_company_status_and_gaps.csv](tables/D6b_company_status_and_gaps.csv) | 24 | 24主体继承状态、关键缺口与业务责任行数 |
| [D7_case_candidates.csv](tables/D7_case_candidates.csv) | 10 | 案例候选表，含入选序位、资格判定与排除理由 |
| [D7a_pairwise_common_functions.csv](tables/D7a_pairwise_common_functions.csv) | 21 | 场景组内两两共同职能集合K，标注入选对与比较资格 |
| [D8a_company_points.csv](tables/D8a_company_points.csv) | 24 | 公司点值与活动可判读广告数 |
| [D8b_within_function_activity_rates.csv](tables/D8b_within_function_activity_rates.csv) | 336 | 公司具体职能内的活动率（每职能至少10条） |
| [D8c2_common_function_weighted_comparison_G2.csv](tables/D8c2_common_function_weighted_comparison_G2.csv) | 8 | G2物流组的同名比较，记录不适用 |
| [D8c_common_function_weighted_comparison.csv](tables/D8c_common_function_weighted_comparison.csv) | 8 | G1入选对的K内统一权重比较（自身/等权/合并三种权重） |
| [D8d_case_q2_context_points.csv](tables/D8d_case_q2_context_points.csv) | 44 | 四家案例公司的Q2固定展示项点值、未知数与样本提示 |
| [D8e_case_work_object_seniority.csv](tables/D8e_case_work_object_seniority.csv) | 82 | 案例公司两职能广告的工作对象与资历关键词派生附表 |
| [D9_sensitivity_ledger.csv](tables/D9_sensitivity_ledger.csv) | 22 | 核心指标的权重、范围、来源子集、逐一剔除与未知情景台账 |
| [D9b_case_deployment_sensitivity.csv](tables/D9b_case_deployment_sensitivity.csv) | 4 | 案例公司部署活动率在口径与子集下的敏感性 |
| [D9c_unknown_scenarios.csv](tables/D9c_unknown_scenarios.csv) | 4 | 未知情景P/B与(P+U)/B及其与执行书对照的核对结果 |
| [D_fig1_plot_data.csv](tables/D_fig1_plot_data.csv) | 80 | 图D1精确绘图数据 |
| [D_fig2_plot_data.csv](tables/D_fig2_plot_data.csv) | 10 | 图D2精确绘图数据 |
| [D_fig3_plot_data.csv](tables/D_fig3_plot_data.csv) | 4 | 图D3精确绘图数据 |
| [T5_company_hiring_correspondence.csv](tables/T5_company_hiring_correspondence.csv) | 1211 | T5公司背景、业务责任、招聘指标与案例资格长表 |
| [T6_conclusion_ledger.csv](tables/T6_conclusion_ledger.csv) | 7 | T6结论与敏感性台账 |

## 字段与连接

- `identity_key`：完整广告唯一身份；`record_id`、`reading_id`仅辅助定位。
- `n_positive`：经语境筛选后去重的正向广告数；`n_interpretable`：最终分母；`n_unknown`：该格未知数，只退出受影响格。
- `share_*`：0—1比例，空值表示无分母、不适用或不允许组汇总。
- 业务责任长表通过 `fact_id` 与 `evidence_ids` 连接阶段B补充包；派生规则ID在 `rule_id` 列。
- 共现判定通过 `identity_key` 回到 `D4_activity_pair_lineage.csv`，再连接原广告与 `T4_activity_lineage.csv`。
