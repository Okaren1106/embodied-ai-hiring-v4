import json
from pathlib import Path

d = Path(r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_d\run_20260915T175337Z")
c = json.loads((d / "verification/step4_checks.json").read_text(encoding="utf-8"))
print("source-complete companies:", c["n_source_complete_companies"], "ads:", c["n_ads_source_complete"])
print()
hdr = ("metric", "P", "U", "interp", "adw", "eqw", "low(P/B)", "high((P+U)/B)", "srcSub", "LOOmin", "LOOmax")
print("{:<24}{:>5}{:>5}{:>7}{:>9}{:>9}{:>11}{:>14}{:>9}{:>9}{:>9}".format(*hdr))


def f(v):
    return "" if v is None else f"{v:.4f}"


for r in c["q2_ledger"]:
    print("{:<24}{:>5}{:>5}{:>7}{:>9}{:>9}{:>11}{:>14}{:>9}{:>9}{:>9}".format(
        r["metric_id"], r["n_positive"], r["n_unknown"], r["n_interpretable"],
        f(r["value_ad_weighted"]), f(r["value_company_equal"]),
        f(r["scenario_low_P_over_B"]), f(r["scenario_high_P_plus_U_over_B"]),
        f(r["s_source_complete_subset_ad_weighted"]), f(r["s_loo_min"]), f(r["s_loo_max"])))
print()
for r in c["unknown_scenarios"]:
    print(r["metric_id"], "book", r["book_reference_P_U_B"], "->", r["n_positive"], r["n_unknown"],
          r["n_base"], "match", r["matches_book_reference"],
          f(r["scenario_low_P_over_B"]), f(r["scenario_high_P_plus_U_over_B"]))
print()
for r in c["case_deployment"]:
    print(r["scope"], r["subset"],
          "| GALBOT all", r["CN_GALBOT_share_all"], "ML", r["CN_GALBOT_share_ML"], "SUP", r["CN_GALBOT_share_SUP"],
          "| AGIBOT all", r["CN_AGIBOT_share_all"], "ML", r["CN_AGIBOT_share_ML"], "SUP", r["CN_AGIBOT_share_SUP"])
