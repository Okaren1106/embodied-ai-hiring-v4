# 数据表目录

全部CSV为UTF-8 BOM，可用Excel导入。数值比例为0—1，NA在CSV中为空，计数为整数。

| 文件 | 行数 | 用途 |
|---|---|---|
| [A1_q2_ml_technical_plot_data.csv](tables/A1_q2_ml_technical_plot_data.csv) | 112 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [A2_q2_software_technical_plot_data.csv](tables/A2_q2_software_technical_plot_data.csv) | 112 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [A3_q2_ml_company_general_plot_data.csv](tables/A3_q2_ml_company_general_plot_data.csv) | 240 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [A4_q2_software_company_general_plot_data.csv](tables/A4_q2_software_company_general_plot_data.csv) | 216 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [F1_q1_company_roles_plot_data.csv](tables/F1_q1_company_roles_plot_data.csv) | 528 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [F2_q1_weighting_plot_data.csv](tables/F2_q1_weighting_plot_data.csv) | 22 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [F3_q2_ml_skills_plot_data.csv](tables/F3_q2_ml_skills_plot_data.csv) | 140 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [F4_q2_software_skills_plot_data.csv](tables/F4_q2_software_skills_plot_data.csv) | 126 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [F5_q3_activity_company_plot_data.csv](tables/F5_q3_activity_company_plot_data.csv) | 576 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [F6_q3_role_structures_plot_data.csv](tables/F6_q3_role_structures_plot_data.csv) | 24 | 图表精确绘图数据；源表和图注见figure_manifest.json |
| [headline_sensitivity.csv](tables/headline_sensitivity.csv) | 11 | 正文具体读数的对应敏感性摘要 |
| [T1_company_sample.csv](tables/T1_company_sample.csv) | 24 | 24行样本、四维状态、供给分类与证据ID |
| [T2_ad_lineage.csv](tables/T2_ad_lineage.csv) | 1654 | 1654条主职能计数的广告、原URL及文本版本 |
| [T2_aggregates.csv](tables/T2_aggregates.csv) | 308 | 全24、整公司23及供给形态描述；全部/明确分母 |
| [T2_company_primary_roles.csv](tables/T2_company_primary_roles.csv) | 528 | 24×22公司主职能格 |
| [T3_aggregates.csv](tables/T3_aggregates.csv) | 14490 | 组汇总与每格门槛；不允许汇总的率留空 |
| [T3_all_item_semantics.csv](tables/T3_all_item_semantics.csv) | 5547 | 全部原标签提及、原文和固定语义判读 |
| [T3_base_admission.csv](tables/T3_base_admission.csv) | 680 | 两职能广告×维度基础资格 |
| [T3_company_context.csv](tables/T3_company_context.csv) | 38640 | 全部已记录标签的公司×语境×分支结果 |
| [T3_leave_one_company_out.csv](tables/T3_leave_one_company_out.csv) | 21084 | 逐一剔除公司；不足门槛时不发布均值 |
| [T3_positive_unknown_lineage.csv](tables/T3_positive_unknown_lineage.csv) | 5466 | 逐标签语境的正向与未知广告清单 |
| [T3_scope_sensitivity.csv](tables/T3_scope_sensitivity.csv) | 1960 | 固定展示项的范围与目录子集检查 |
| [T3_selected_role_unmapped_mentions.csv](tables/T3_selected_role_unmapped_mentions.csv) | 1424 | 两职能已有目录外提及，含多个维度 |
| [T3_separate_context_mentions.csv](tables/T3_separate_context_mentions.csv) | 155 | 非正向语境按广告去重清点 |
| [T4_activity_admission.csv](tables/T4_activity_admission.csv) | 1654 | 1654广告活动维度资格 |
| [T4_activity_aggregates.csv](tables/T4_activity_aggregates.csv) | 48 | 全24与整公司23活动汇总 |
| [T4_activity_company.csv](tables/T4_activity_company.csv) | 576 | 公司×8活动×本人/参与/并集，576格 |
| [T4_activity_lineage.csv](tables/T4_activity_lineage.csv) | 3236 | 全部3236原活动提及，分析中按广告去重 |
| [T4_primary_activity_cross.csv](tables/T4_primary_activity_cross.csv) | 352 | 主职能×活动关系交叉，不互相代替分类 |
| [T4_role_structure_company.csv](tables/T4_role_structure_company.csv) | 24 | 逐公司复合/任选/混合广告数 |
| [T4_role_structure_nodes.csv](tables/T4_role_structure_nodes.csv) | 118 | 118原节点，其中87职能节点 |
| [T4_role_structures.csv](tables/T4_role_structures.csv) | 30 | 30条结构广告及原始完整树JSON |
| [T4_structure_function_appearances.csv](tables/T4_structure_function_appearances.csv) | 18 | 结构中的职能提及，以广告去重，不是人数 |

## 字段与连接

- identity_key：完整广告唯一身份；record_id、reading_id仅辅助定位，不替代唯一身份。
- n_positive：经语境筛选后去重的正向广告数；n_base：该职能该维度基础广告数；n_relation_unknown：该指标关系未知；n_interpretable：最终分母。
- share、share_all、share_ad_weighted、share_company_equal：0—1比例。空值为无分母、明确子集不适用或不允许组汇总，结合对应状态字段解释。
- n_companies：本格非零分母公司数；eligible_companies_json：相应公司列表。
- *_json：JSON文本，使用JSON解析，不按分隔符拆分。
- primary_code、label_code、metric_bucket、branch_bucket、relation为原有或已固定v1枚举。字段含义补充见METHODS。
- 业务分类证据通过company_id→basis_fact_ids/basis_evidence_ids连接inputs/rules_v1内的decision_provenance、evidence_index和封存证据。

Excel提供主要结果：Q1完整528格、Q2整公司490语境格、Q2公司一般独立要求840格、Q3完整576格及30条结构概览。其他语境的公司格、业务组与全部追溯放在CSV和HTML查询中，工作簿并非全量长表的重复备份。
