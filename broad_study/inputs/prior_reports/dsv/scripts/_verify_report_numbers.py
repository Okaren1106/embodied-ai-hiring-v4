import csv
from pathlib import Path

d = Path(r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_d\run_20260915T175337Z")


def read(p):
    return list(csv.DictReader((d / p).open(encoding="utf-8-sig", newline="")))


print("=== D1 机器人操作 / 控制与规划 ===")
for r in read("tables/D1_q1_coverage_concentration.csv"):
    if r["class_code"] in ("RF_ROBOT_OPERATION", "RF_CONTROL_PLANNING"):
        print(r["class_name"], "adw", r["share_ad_weighted_all"], "eqw", r["share_company_equal_all"])

print("\n=== D8b GALBOT/AGIBOT within ML function ===")
for r in read("tables/D8b_within_function_activity_rates.csv"):
    if r["company_id"] in ("CN_GALBOT", "CN_AGIBOT") and r["primary_code"] == "RF_ML_AI_ENGINEERING":
        print(f'{r["company_id"]:<12} {r["activity_name"]:<12} n={r["n_assessable_in_function"]:>3} pos={r["n_positive"]:>3} share={float(r["share_within_function"])*100:5.1f}%')

print("\n=== D8b GALBOT/AGIBOT within 公司支持 ===")
for r in read("tables/D8b_within_function_activity_rates.csv"):
    if r["company_id"] in ("CN_GALBOT", "CN_AGIBOT") and r["primary_code"] == "RF_CORPORATE_SUPPORT":
        print(f'{r["company_id"]:<12} {r["activity_name"]:<12} n={r["n_assessable_in_function"]:>3} pos={r["n_positive"]:>3} share={float(r["share_within_function"])*100:5.1f}%')

print("\n=== D8c full K rows for G1 (all three weightings) ===")
for r in read("tables/D8c_common_function_weighted_comparison.csv"):
    if r["activity_code"] in ("ACT_ENGINEERING", "ACT_QUALITY", "ACT_DEPLOYMENT", "ACT_BUSINESS", "ACT_RESEARCH"):
        g = lambda k: "NA" if r[k] in ("", None) else f"{float(r[k])*100:.1f}%"
        print(f'{r["activity_name"]:<10} GALBOT all={g("CN_GALBOT_share_all")} self={g("CN_GALBOT_share_self_weighted")} '
              f'eq={g("CN_GALBOT_share_equal_weighted")} pool={g("CN_GALBOT_share_pooled_weighted")} | '
              f'AGIBOT all={g("CN_AGIBOT_share_all")} self={g("CN_AGIBOT_share_self_weighted")} '
              f'eq={g("CN_AGIBOT_share_equal_weighted")} pool={g("CN_AGIBOT_share_pooled_weighted")}')

print("\n=== D7 exclusions wording ===")
for r in read("tables/D7_case_candidates.csv"):
    if r["selected"] == "NO":
        print(r["company_id"], "|", r["decision_reason"][:130])
