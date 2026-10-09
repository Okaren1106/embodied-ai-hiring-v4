# 阶段 E 计算协议与真实字段映射

协议版本：E-G0-v1，2026-09-18。方法负责人：Astra。仅当同目录 G0_status.json 为 APPROVED 时，本协议用于执行。适用本项目书 v1.1，不新增编码或改动冻结输入。

## 路径和范围

- PROJECT：`D:/Embod AI analysis/embodied-ai-hiring-research`
- V3：`${PROJECT}/reports/2026-09-14_company_data_analysis/stage_d_integrated_v2/run_20260917_astra_core_q2_v3`
- B：`${PROJECT}/reports/2026-09-14_company_data_analysis/stage_b_supplemented/run_20260915T073556Z`
- E：`${PROJECT}/analysis_E_v1_1`
- 稳定身份：`identity_key`。`reading_id` 只作查找，不作主键；E0107的不同岗位身份不得合并。
- 全体1654、整公司1630、Q2全体1576、Q2整公司1552；FAR团队24条单列。Q3_ads_final仅含Q2具体职能，不是1654条全体主分类表。

## 固定任务与标签

| role | task | label_code | 名称 |
|---|---|---|---|
| RF_ML_AI_ENGINEERING | ROBOT_MODEL | SK_PYTHON | Python |
| RF_ML_AI_ENGINEERING | ROBOT_MODEL | SK_PYTORCH | PyTorch |
| RF_ROBOTICS_SOFTWARE | ROBOT_RUNTIME | SK_CPP | C++ |
| RF_ROBOTICS_SOFTWARE | ROBOT_RUNTIME | SK_LINUX | Linux |
| RF_HARDWARE_ELECTRICAL | BOARD_CIRCUIT | SK_ALTIUM | Altium |
| RF_HARDWARE_ELECTRICAL | BOARD_CIRCUIT | V2_EMC_SIPI | 电磁兼容与信号电源完整性 |

这六个组合是全文展示范围；固定公司对为CN_GALBOT与CN_XSQUARE的ROBOT_MODEL/SK_PYTHON及ROBOT_RUNTIME/SK_CPP，US_APPTRONIK的BOARD_CIRCUIT/SK_ALTIUM为例证。不得为提高差异重选公司。

## M 相关技术提及

源：V3/tables/V3_two_layer_company_points.csv；全任务汇总为V3_two_layer_aggregates.csv。

- 逻辑 `m_pos=P`，`m_den_v3=N`，`m_share=share`；汇总使用已有`share_ad_weighted`和`share_company_equal`。
- 本表的N=P+Z，B=N+U。必须使用本表自己定义的P/Z/U，不得借用严格语境的状态。
- `U`表示第一层未知状态；`has_unresolved_branch`表示提及正例中存在未解分支的诊断。二者不可互换；有未解分支仍可为M正例。
- 保留`SOURCE_EXCLUDED`、`NA`、`total_ads`、`small_n`。`N`不自动等于任务广告总数。
- 直接提取既有四情景值，不用证据长表重做第一层语义解析。

## W 提及后的要求方式

仍用两层表：职责=`DUTY_ANY`，明确必备=`REQUIRED`，一般=`GENERAL`，优先=`PREFERRED`。比例各自除以该行M的P；P=0记NA。四列可重叠，不能加成100%。

`DUTY_ANY`是广告去重后的职责联合，不把`DUTY_OWN_USE + DUTY_OWN_DEVELOP`直接相加。`GENERAL_UNCONDITIONAL`只提供该严格格的正例计数，不提供其完整N或U。宽联系`DUTY_PLUS_COLLAB_CONTACT`不是本人能力。

## G 原22格严格语境

主任务已有源：`Q4_task_company_points_final.csv`（公司），`Q4_task_strata_final.csv`（任务汇总）。筛选WHOLE23及上述role/task/label_code。指标由`metric,branch`共同确定，不按名称相似连接。

新情景仅补固定五个公司—任务—条目组合的`metric=GENERAL, branch=UNCONDITIONAL`。五组合为两个公司各两任务加Apptronik一项。其他新增格不在当前任务中。

唯一允许的明细状态源：`Q3_states_final.csv`。它已经解析最终P/Z/U/NA/SOURCE_EXCLUDED；直接按状态计数，不重新解析原文或改优先级。

`P_g=count(P)`，`Z_g=count(Z)`，`U_g=count(U)`；`N_g=P_g+Z_g`，`B_g=N_g+U_g`。NA、SOURCE_EXCLUDED另列；主率P_g/N_g；已识别未知界限P_g/B_g至(P_g+U_g)/B_g，分母为零记NA。小样本为0<N_g<10。未知界限不是置信区间。

按`identity_key,label_code,metric,branch`检查唯一状态；若出现多行，先比较所有定位列包括slice_family并报告，不擅自择一。同一目标成员每个适用格必须有且仅有一个最终状态；缺行不得补Z。新增情景的目标task来自成员表，不能再按状态表原主task过滤，否则会丢失次任务成员。

## 情景成员与连接

源：`V3_two_layer_membership.csv`，键=`scenario,role,task,identity_key`。

| scenario | 含义 | 对应Q4范围 |
|---|---|---|
| PRIMARY | 原主任务 | WHOLE23与固定任务 |
| PLUS_SECONDARY | 已登记主/次任务并集 | 直接用两层成员，不重建任务 |
| DEDUP_PRIMARY | 原主任务职责模板敏感性 | DEDUPE_EXACT_DUTIES |
| NO_CAMPUS_PRIMARY | 去明示校招/实习 | EXCLUDE_EXPLICIT_CAMPUS_INTERN |

成员记录数分别248、259、236、224，用作接入锚点，不是新增独立招聘人数。主任务数105/87/56。对PLUS_SECONDARY按广告×目标任务去重，不把跨任务重复计成独立广告。

模板方案直接继承成员；历史实现另有限定职责文本>=80字符及固定代表选择，不重选代表、不重定义模板。

## 复核状态

连接PRIMARY成员到`Q3_review_receipts.csv`的identity_key。`ASTRA_FULL_SOURCE_REVIEWED`→全文；`ASTRA_BOUNDARY_REVIEWED`→边界。`REVIEW_PENDING`仅在seeded=NO且mandatory=NO、并符合V3已完成范围时展示为继承首轮；其他组合报告，不批量改成继承或待办。

锚点：模型24/63/18，运行软件19/58/10，板级13/43/0；总计56/164/28。保留原状态列和展示列，不回写原件。不把本轮连接检查说成语义复核或独立人工编码。

## 公司、整体职能和分解

- 公司范围：`V3/inputs/stage_c/tables/T1_company_sample.csv`。一公司一行，保留单位、日期、来源及范围警示。
- 公司职能：同目录`T2_company_primary_roles.csv`，展示`n_ads/denominator_all,share_all`。不得替换为`share_coded`；structural与未明确类别不偷偷删除。
- 整体职能分布：`V3/tables/R_Q1_coverage_concentration.csv`，按scope读取WHOLE23；Q1分母不要换成1552。
- B背景分别读取company_profile、company_facts、company_evidence、evidence_links，先保存一公司一行概览及独立证据长表；不能多对多连接广告后数行。
- 公司案例解释：`V3_T5_company_interpretation.csv`，有效结论：`V3_T6_claims.csv`和`V3_claim_disposition.csv`。
- 工程分解：`D2_decomposition_summary.csv`筛选case_id=D_MAIN、company_a=CN_GALBOT、company_b=US_FIGURE、mode=FIXED_K、activity=ACT_ENGINEERING。保留MAIN、NO_EXPLICIT_CAMPUS_OR_INTERN、EXACT_DUTY_DEDUP及三个来源方案NA行。各情景用自己的覆盖分母，不把主范围82/181、60/126复制给其他情景。

## 权重与检查

公司等权只在同一指标N_c>0的公司求平均(P_c/N_c)，包含P_c=0；广告加权为sum(P)/sum(N)。W层采用各公司M正例数作为自己的分母。留一公司结果单列，不能把其平均称公司等权。

G的公司未知界限平均遵循V3/astra_stats.py：B_c>0的公司参与界限均值，可能与N_c>0的点值公司集合不同；必须明确两种集合。当前新增任务只要求公司点值及广告权重并列，不自行扩组。

组展示门槛沿V3：至少3家公司、合计N>=20；两公司比较仍作为公司点值/固定案例，不借组门槛获得显著性。已有主图筛选与组展示门槛不是一回事。

使用未舍入值。演示甲1/2、乙8/10、丙0/4：等权43.333333%，加权56.25%，留一合并率均值49.603175%。加P=N=0公司不改主值但保留缺失记录。不得对研究数据人为加入演示记录。

## 操作范围和写入

文件定位、表头、哈希和原始行数检查不需要等待G0；解释性连接和正式计算需G0通过。V3、B、A/C、研究库均只读。禁止在V3原目录运行任何会写表的compute/materialize/register脚本；复用纯函数须核对导入副作用，优先在个人工作目录写只读提取脚本。

Q3_states_final约1.49GB：用标准CSV流式读取，先用小成员表构建目标集合，只保留五个固定组合和严格格。不要整表读入模型上下文或复制给多个模型反复解析。

输出携带input/source路径及哈希、协议版本、scenario、role、task、label、metric、单位和检查状态。任何真实矛盾先记录影响范围，不改原标签。可选词面基线本轮默认不做，待主稿就绪再决定。
