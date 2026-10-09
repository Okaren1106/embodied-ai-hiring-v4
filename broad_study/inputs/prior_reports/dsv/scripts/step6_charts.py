#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage D step 6: three main figures.

Figure purposes fixed by the research book: cross-function activity
distribution, within-function company differences, and business
responsibility against hiring combination. Exact plot data is written next to
each figure; PNG for reading, SVG for typesetting. Figure metadata is stripped
of dates so the outputs are byte-reproducible.
"""
from __future__ import annotations

import csv
import json
import os
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

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

TAB = RUN / "tables"
CH = RUN / "charts"
CH.mkdir(parents=True, exist_ok=True)

FONT = "C:/Windows/Fonts/msyh.ttc"
if Path(FONT).exists():
    font_manager.fontManager.addfont(FONT)
    plt.rcParams["font.family"] = font_manager.FontProperties(fname=FONT).get_name()
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["svg.hashsalt"] = "stage-d-v1"
META = {"Date": None}


def read(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(name, rows, fields):
    with (TAB / name).open("w", encoding="utf-8-sig", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        wr.writeheader()
        for row in rows:
            wr.writerow(row)


t2 = read(C / "tables/T2_company_primary_roles.csv")
t1 = read(C / "tables/T1_company_sample.csv")
d3 = read(RUN / "tables/D3_role_activity_bidirectional.csv")
d8b = read(RUN / "tables/D8b_within_function_activity_rates.csv")
d6 = read(RUN / "tables/D6_business_responsibility_long.csv")
d8a = read(RUN / "tables/D8a_company_points.csv")
d8c = read(RUN / "tables/D8c_common_function_weighted_comparison.csv")
d9b = read(RUN / "tables/D9b_case_deployment_sensitivity.csv")
selection = json.loads((RUN / "cases/case_selection.json").read_text(encoding="utf-8"))
companies = {r["company_id"]: r for r in t1}
fname = {r["class_code"]: r["class_name"] for r in t2}

ACT_ORDER = ["ACT_ENGINEERING", "ACT_QUALITY", "ACT_DEPLOYMENT", "ACT_BUSINESS",
             "ACT_MANUFACTURING", "ACT_DATA_OPERATIONS", "ACT_RESEARCH",
             "ACT_ROBOT_OPERATION"]
ANAME = {}
for r in d3:
    ANAME[r["activity_code"]] = r["activity_name"]

# ------------------------------------------------- figure 1: cross function
rows = [r for r in d3 if r["scope"] == "ALL24"]
agg24 = [x for x in read(C / "tables/T2_aggregates.csv")
         if x["scope"] == "ALL24" and x["denominator_basis"] == "ALL" and x["class_kind"] == "concrete"]
top_functions = [r["class_code"] for r in sorted(agg24, key=lambda x: -int(x["n_ads"]))][:10]
data = []
for act in ACT_ORDER:
    for code in top_functions:
        r = next((x for x in rows if x["activity_code"] == act and x["primary_code"] == code), None)
        if not r:
            continue
        data.append({"activity_code": act, "activity_name": ANAME.get(act, act),
                     "primary_code": code, "primary_name": fname.get(code, code),
                     "n_positive_in_primary": r["n_positive_in_primary"],
                     "share_of_activity": r["share_of_activity"]})
write_csv("D_fig1_plot_data.csv", data,
          ["activity_code", "activity_name", "primary_code", "primary_name",
           "n_positive_in_primary", "share_of_activity"])

fig, ax = plt.subplots(figsize=(11, 6.2))
colors = plt.get_cmap("tab20").colors
left = [0.0] * len(ACT_ORDER)
ys = list(range(len(ACT_ORDER)))
for i, code in enumerate(top_functions):
    vals = []
    for act in ACT_ORDER:
        r = next((x for x in data if x["activity_code"] == act and x["primary_code"] == code), None)
        vals.append(float(r["share_of_activity"]) if r else 0.0)
    ax.barh(ys, vals, left=left, color=colors[i % len(colors)], label=fname.get(code, code),
            edgecolor="white", linewidth=0.6)
    left = [l + v for l, v in zip(left, vals)]
ax.set_yticks(ys)
ax.set_yticklabels([ANAME.get(a, a) for a in ACT_ORDER])
ax.invert_yaxis()
ax.set_xlim(0, 1)
ax.set_xlabel("该活动本人承担广告在各主职能中的占比（后向分布）")
ax.set_title("图D1 八类活动的主职能分布（全24主体，活动可判读1623条）")
ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=8, title="主职能")
ax.grid(axis="x", linestyle=":", alpha=0.4)
fig.savefig(CH / "D1_cross_function_activity.png", metadata=META)
fig.savefig(CH / "D1_cross_function_activity.svg", metadata=META)
plt.close(fig)

# -------------------------------------------- figure 2: within function diff
G1 = selection["selected_groups"]["G1_MANUFACTURING_LINE"]
a, b = G1[0], G1[1]
acts = ["ACT_ENGINEERING", "ACT_QUALITY", "ACT_DEPLOYMENT", "ACT_BUSINESS", "ACT_RESEARCH"]
fig2 = []
for act in acts:
    for cid in G1:
        r = next((x for x in d8b if x["company_id"] == cid
                  and x["primary_code"] == "RF_ML_AI_ENGINEERING" and x["activity_code"] == act), None)
        k_row = next((x for x in d8c if x["activity_code"] == act), {})
        fig2.append({
            "company_id": cid, "company_name": companies[cid]["company_name"],
            "activity_code": act, "activity_name": ANAME.get(act, act),
            "n_ML_assessable": r["n_assessable_in_function"] if r else "",
            "n_ML_positive": r["n_positive"] if r else "",
            "share_ML": r["share_within_function"] if r else "",
            "share_all_company": k_row.get(f"{cid}_share_all", ""),
            "share_K_self_weighted": k_row.get(f"{cid}_share_self_weighted", ""),
        })
write_csv("D_fig2_plot_data.csv", fig2, list(fig2[0].keys()))

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.6), sharey=True)
panels = [("share_all_company", "全公司口径"),
          ("share_K_self_weighted", "共同职能K内自我权重"),
          ("share_ML", "ML/AI工程职能内")]
x = np.arange(len(acts))
w = 0.38
for ax, (field, title) in zip(axes, panels):
    va, vb = [], []
    for act in acts:
        ra = next((r for r in fig2 if r["company_id"] == a and r["activity_code"] == act), {})
        rb = next((r for r in fig2 if r["company_id"] == b and r["activity_code"] == act), {})
        va.append(float(ra.get(field) or 0))
        vb.append(float(rb.get(field) or 0))
    ax.bar(x - w / 2, va, w, label=companies[a]["company_name"], color="#3d6fb4")
    ax.bar(x + w / 2, vb, w, label=companies[b]["company_name"], color="#c85a3a")
    ax.set_xticks(x)
    ax.set_xticklabels([ANAME.get(t, t) for t in acts], rotation=30, ha="right", fontsize=8)
    ax.set_title(title, fontsize=10)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
axes[0].set_ylabel("本人承担该活动的广告占比")
axes[0].legend(fontsize=8)
fig.suptitle("图D2 同一职能内部的活动承担差异（制造产线案例组，2026-09-11同批）", fontsize=11)
fig.savefig(CH / "D2_same_function_company_diff.png", metadata=META)
fig.savefig(CH / "D2_same_function_company_diff.svg", metadata=META)
plt.close(fig)

# --------------------------- figure 3: responsibility vs hiring combination
CASES = selection["selected"]
STAGES = ["PRODUCT_MODEL_DEV", "SYSTEM_INTEGRATION", "CUSTOMER_SITE_DEPLOYMENT",
          "CONTINUOUS_OPERATION", "PRODUCT_DELIVERY"]
SNAME = {"PRODUCT_MODEL_DEV": "产品或模型开发", "SYSTEM_INTEGRATION": "系统集成",
         "CUSTOMER_SITE_DEPLOYMENT": "客户现场部署", "CONTINUOUS_OPERATION": "持续运行",
         "PRODUCT_DELIVERY": "产品交付"}
base_dep = next((r for r in d9b if r["scope"] == "ALL24" and r["subset"] == "BASE"), {})
fig3 = []
for cid in CASES:
    cnt = Counter(r["business_stage"] for r in d6 if r["company_id"] == cid)
    dep = next((r for r in d8b if r["company_id"] == cid and r["activity_code"] == "ACT_DEPLOYMENT"
                and r["primary_code"] == "RF_ML_AI_ENGINEERING"), {})
    denom = next((r["n_ads_activity_assessable"] for r in d8a if r["company_id"] == cid), 0)
    fig3.append({
        "company_id": cid, "company_name": companies[cid]["company_name"],
        **{f"n_{s}": cnt.get(s, 0) for s in STAGES},
        "n_activity_assessable": denom,
        "deployment_share_all": base_dep.get(f"{cid}_share_all", ""),
        "deployment_share_ML": base_dep.get(f"{cid}_share_ML", ""),
        "ML_function_n": base_dep.get(f"{cid}_ML_n", ""),
    })
write_csv("D_fig3_plot_data.csv", fig3, list(fig3[0].keys()))

fig, ax = plt.subplots(figsize=(11, 5))
ys = np.arange(len(CASES))
left = np.zeros(len(CASES))
cmap = plt.get_cmap("YlGnBu")
for i, s in enumerate(STAGES):
    vals = np.array([float(r[f"n_{s}"]) for r in fig3])
    ax.barh(ys, vals, left=left, label=SNAME[s], color=cmap(0.25 + 0.15 * i), edgecolor="white")
    left = left + vals
ax.set_yticks(ys)
labels = []
for r in fig3:
    share = r["deployment_share_all"]
    share_txt = f"{float(share)*100:.1f}%" if share not in ("", None) else "NA"
    ml_n = r["ML_function_n"]
    ml_txt = f"{float(r['deployment_share_ML'])*100:.0f}%({ml_n}条)" if r["deployment_share_ML"] not in ("", None) else "NA"
    labels.append(f'{r["company_name"]}\n全公司部署活动率 {share_txt}｜ML职能内 {ml_txt}')
ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel("继承的业务责任事实条数（按业务环节）")
ax.set_title("图D3 业务责任环节与招聘活动率的对应（四家案例公司）")
ax.legend(fontsize=8, title="业务环节")
ax.grid(axis="x", linestyle=":", alpha=0.4)
fig.savefig(CH / "D3_responsibility_vs_hiring.png", metadata=META)
fig.savefig(CH / "D3_responsibility_vs_hiring.svg", metadata=META)
plt.close(fig)

manifest = {
    "figures": [
        {"id": "D1", "file_png": "charts/D1_cross_function_activity.png",
         "file_svg": "charts/D1_cross_function_activity.svg",
         "plot_data": "tables/D_fig1_plot_data.csv",
         "purpose": "跨职能活动分布", "source": "tables/D3_role_activity_bidirectional.csv"},
        {"id": "D2", "file_png": "charts/D2_same_function_company_diff.png",
         "file_svg": "charts/D2_same_function_company_diff.svg",
         "plot_data": "tables/D_fig2_plot_data.csv",
         "purpose": "同职能公司差异",
         "source": "tables/D8b_within_function_activity_rates.csv + tables/D8c_common_function_weighted_comparison.csv"},
        {"id": "D3", "file_png": "charts/D3_responsibility_vs_hiring.png",
         "file_svg": "charts/D3_responsibility_vs_hiring.svg",
         "plot_data": "tables/D_fig3_plot_data.csv",
         "purpose": "业务责任与招聘组合对应",
         "source": "tables/D6_business_responsibility_long.csv + tables/D9b_case_deployment_sensitivity.csv"},
    ],
    "font": FONT,
    "figure1_note": "后向分布按活动，各主职能占比之和为100%；同一广告可同时计入多个活动，禁止跨活动相加",
    "figure2_note": "K内自我权重仅覆盖共同职能，覆盖率有限，见D8c",
    "figure3_note": "业务环节事实条数不是人数或订单数；招聘活动率为广告占比；ML职能内n为该职能活动可判读广告数",
}
(RUN / "figure_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                          encoding="utf-8")
print("figures written:", [f["id"] for f in manifest["figures"]])
