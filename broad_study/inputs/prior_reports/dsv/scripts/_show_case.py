import csv
from pathlib import Path

d = Path(r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_d\run_20260915T175337Z")
r = list(csv.DictReader((d / "tables/D9b_case_deployment_sensitivity.csv").open(encoding="utf-8-sig")))
cases = ["CN_GALBOT", "CN_AGIBOT", "US_BOSTON_DYNAMICS", "US_PICKLE"]
for row in r:
    if row["subset"] != "BASE":
        continue
    parts = []
    for c in cases:
        parts.append(f"{c}: n={row[c+'_n']} all={row[c+'_share_all']} ML={row[c+'_share_ML']} SUP={row[c+'_share_SUP']}")
    print(row["scope"], "|", " | ".join(parts))
print()
f3 = list(csv.DictReader((d / "tables/D_fig3_plot_data.csv").open(encoding="utf-8-sig")))
for row in f3:
    print(row["company_id"], "deploy_all=", row["deployment_share_all"], "ML=", row["deployment_share_ML"])
