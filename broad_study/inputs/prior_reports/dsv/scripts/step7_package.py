#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage D step 7: package metadata.

Writes DATA_DICTIONARY.md, input_lock.json and release_checksums.json.
The checksum file covers every published file of this run directory and is
written last so a later reproduce run can verify the package and refuse to
overwrite an existing output directory.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent


def _resolve_base(run: Path) -> Path:
    """Input root: explicit env wins, then the run's own input_lock.json."""
    env = os.environ.get("STAGE_D_BASE")
    if env:
        return Path(env)
    lock = run / "input_lock.json"
    if lock.is_file():
        try:
            recorded = json.loads(lock.read_text(encoding="utf-8")).get("base_dir")
        except (OSError, json.JSONDecodeError):
            recorded = None
        if recorded:
            return Path(recorded)
    return run.parents[1]


BASE = _resolve_base(RUN)
C = BASE / "stage_c/run_20260915T105656Z"
B = BASE / "stage_b_supplemented/run_20260915T073556Z"
R = BASE / "analysis_rules_v1/run_20260915T085828Z"


def sha256(path: Path, chunk=1 << 20):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            block = fh.read(chunk)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def rows_of(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return sum(1 for _ in csv.reader(fh)) - 1


PURPOSE = {
    "D1_q1_coverage_concentration.csv": "Q1各主职能的公司覆盖、集中度、四分位与两种权重；含未明确状态单列行",
    "D2_q2_coverage_concentration.csv": "Q2全部标签×语境×分支的覆盖与集中度，分母贡献与正向贡献分列",
    "D2_q3_coverage_concentration.csv": "Q3八类活动的公司覆盖、集中度与两种权重",
    "D3_role_activity_bidirectional.csv": "主职能×活动双向条件比例，含结构类与未明确状态",
    "D4_activity_pair_cooccurrence.csv": "三组活动配对的无条件/条件性/仅任选/未解决计数与主率",
    "D4_activity_pair_lineage.csv": "每条共现判定的广告ID、分支定位、原文片段与理由",
    "D5_activity_pair_structure.csv": "各配对的所属职能与公司分布及集中度",
    "D6_business_responsibility_long.csv": "24主体业务环节与责任主体派生长表，保留fact_id与evidence_ids",
    "D6b_company_status_and_gaps.csv": "24主体继承状态、关键缺口与业务责任行数",
    "D7a_pairwise_common_functions.csv": "场景组内两两共同职能集合K，标注入选对与比较资格",
    "D7_case_candidates.csv": "案例候选表，含入选序位、资格判定与排除理由",
    "D8a_company_points.csv": "公司点值与活动可判读广告数",
    "D8b_within_function_activity_rates.csv": "公司具体职能内的活动率（每职能至少10条）",
    "D8c_common_function_weighted_comparison.csv": "G1入选对的K内统一权重比较（自身/等权/合并三种权重）",
    "D8c2_common_function_weighted_comparison_G2.csv": "G2物流组的同名比较，记录不适用",
    "D8d_case_q2_context_points.csv": "四家案例公司的Q2固定展示项点值、未知数与样本提示",
    "D8e_case_work_object_seniority.csv": "案例公司两职能广告的工作对象与资历关键词派生附表",
    "D9_sensitivity_ledger.csv": "核心指标的权重、范围、来源子集、逐一剔除与未知情景台账",
    "D9b_case_deployment_sensitivity.csv": "案例公司部署活动率在口径与子集下的敏感性",
    "D9c_unknown_scenarios.csv": "未知情景P/B与(P+U)/B及其与执行书对照的核对结果",
    "D_fig1_plot_data.csv": "图D1精确绘图数据",
    "D_fig2_plot_data.csv": "图D2精确绘图数据",
    "D_fig3_plot_data.csv": "图D3精确绘图数据",
    "T5_company_hiring_correspondence.csv": "T5公司背景、业务责任、招聘指标与案例资格长表",
    "T6_conclusion_ledger.csv": "T6结论与敏感性台账",
}

lines = ["# 数据表目录", "", "全部CSV为UTF-8 BOM，可用Excel导入。数值比例为0—1，NA在CSV中为空，计数为整数。", "",
         "| 文件 | 行数 | 用途 |", "|---|---|---|"]
for path in sorted((RUN / "tables").glob("*.csv")):
    lines.append(f"| [{path.name}](tables/{path.name}) | {rows_of(path)} | "
                 f"{PURPOSE.get(path.name, '阶段D派生表')} |")
lines += ["", "## 字段与连接", "",
          "- `identity_key`：完整广告唯一身份；`record_id`、`reading_id`仅辅助定位。",
          "- `n_positive`：经语境筛选后去重的正向广告数；`n_interpretable`：最终分母；`n_unknown`：该格未知数，只退出受影响格。",
          "- `share_*`：0—1比例，空值表示无分母、不适用或不允许组汇总。",
          "- 业务责任长表通过 `fact_id` 与 `evidence_ids` 连接阶段B补充包；派生规则ID在 `rule_id` 列。",
          "- 共现判定通过 `identity_key` 回到 `D4_activity_pair_lineage.csv`，再连接原广告与 `T4_activity_lineage.csv`。",
          ""]
(RUN / "DATA_DICTIONARY.md").write_text("\n".join(lines), encoding="utf-8")

inputs = {}
for name, path in (
    ("stage_c_package", C),
    ("stage_c_input_lock", C / "input_lock.json"),
    ("stage_c_tables_T1", C / "tables/T1_company_sample.csv"),
    ("stage_c_tables_T2", C / "tables/T2_company_primary_roles.csv"),
    ("stage_c_tables_T2_aggregates", C / "tables/T2_aggregates.csv"),
    ("stage_c_tables_T3_aggregates", C / "tables/T3_aggregates.csv"),
    ("stage_c_tables_T3_base_admission", C / "tables/T3_base_admission.csv"),
    ("stage_c_tables_T3_positive_unknown_lineage", C / "tables/T3_positive_unknown_lineage.csv"),
    ("stage_c_tables_T4_activity_admission", C / "tables/T4_activity_admission.csv"),
    ("stage_c_tables_T4_activity_lineage", C / "tables/T4_activity_lineage.csv"),
    ("stage_c_tables_T4_activity_company", C / "tables/T4_activity_company.csv"),
    ("stage_c_tables_T4_activity_aggregates", C / "tables/T4_activity_aggregates.csv"),
    ("stage_c_tables_T4_primary_activity_cross", C / "tables/T4_primary_activity_cross.csv"),
    ("stage_c_tables_T4_role_structures", C / "tables/T4_role_structures.csv"),
    ("stage_c_jobs", C / "inputs/rules_v1/inputs/stage_a/jobs.csv"),
    ("stage_b_company_facts", B / "company_facts.csv"),
    ("stage_b_company_gaps", B / "company_gaps.csv"),
    ("stage_b_company_profile", B / "company_profile.csv"),
    ("rules_company_classification", R / "company_classification.csv"),
    ("rules_company_scene_assertions", R / "company_scene_assertions.csv"),
    ("rules_q2_display_selection", R / "q2_display_selection.csv"),
):
    if path.is_file():
        inputs[name] = {"path": str(path).replace("\\", "/"), "sha256": sha256(path),
                        "bytes": path.stat().st_size}
    else:
        inputs[name] = {"path": str(path).replace("\\", "/"), "status": "DIRECTORY_OR_MISSING"}
(RUN / "input_lock.json").write_text(json.dumps({
    "run_id": RUN.name,
    "base_dir": str(BASE).replace("\\", "/"),
    "reference_set": "REFERENCE1654_USER_ACCEPTED_2026_09_14_V1",
    "stage_c_package_files": sum(1 for _ in C.rglob("*") if _.is_file()),
    "inputs": inputs,
    "note": "阶段C原封存包只读；本清单登记阶段D读取的输入文件哈希",
}, ensure_ascii=False, indent=2), encoding="utf-8")

files = []
for path in sorted(p for p in RUN.rglob("*") if p.is_file()):
    rel = path.relative_to(RUN).as_posix()
    if rel in ("release_checksums.json",):
        continue
    files.append({"path": rel, "sha256": sha256(path), "bytes": path.stat().st_size})
(RUN / "release_checksums.json").write_text(json.dumps({
    "run_id": RUN.name,
    "packaging": "STAGE_D_V1",
    "n_files": len(files),
    "algorithm": "sha256",
    "files": files,
}, ensure_ascii=False, indent=2), encoding="utf-8")

print(json.dumps({"tables": len(list((RUN / 'tables').glob('*.csv'))),
                  "n_charts": len(list((RUN / 'charts').glob('*'))),
                  "n_published_files": len(files)}, ensure_ascii=False))
