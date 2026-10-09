import csv
import json
from pathlib import Path

d = Path(r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_d\run_20260915T175337Z")


def read(p):
    return list(csv.DictReader((d / p).open(encoding="utf-8-sig", newline="")))


print("=== D1 (WHOLE23, top by ad-weighted) ===")
d1 = [r for r in read("tables/D1_q1_coverage_concentration.csv") if r["class_kind"] != "status"]
for r in sorted(d1, key=lambda x: -int(x["n_ads_ad_weighted"]))[:8]:
    print(f'{r["class_name"]:<18} n={r["n_ads_ad_weighted"]:>4} adw={float(r["share_ad_weighted_all"])*100:5.1f}% '
          f'eqw={float(r["share_company_equal_all"])*100:5.1f}% med={float(r["company_share_median"])*100:5.1f}% '
          f'p25={float(r["company_share_p25"])*100:5.1f}% p75={float(r["company_share_p75"])*100:5.1f}% '
          f'posComp={r["n_companies_positive"]} largestPos={float(r["largest_company_positive_contribution"])*100:4.1f}% ({r["largest_company_id"]})')
print()
for r in read("tables/D1_q1_coverage_concentration.csv"):
    if r["class_kind"] == "status":
        print(f'{r["class_code"]:<32} n={r["n_ads_ad_weighted"]:>3} adw={float(r["share_ad_weighted_all"])*100:.2f}% eqw={float(r["share_company_equal_all"])*100:.2f}%')

print("\n=== D3 headline cross (ALL24) ===")
for act in ("ACT_RESEARCH", "ACT_QUALITY", "ACT_DEPLOYMENT", "ACT_ENGINEERING", "ACT_BUSINESS"):
    rows = [r for r in read("tables/D3_role_activity_bidirectional.csv") if r["scope"] == "ALL24" and r["activity_code"] == act]
    rows = [r for r in rows if int(r["n_positive_in_primary"]) > 0]
    rows.sort(key=lambda x: -int(x["n_positive_in_primary"]))
    tot = rows[0]["n_activity_positive_total"]
    print(act, "total", tot, "|", ", ".join(f'{r["primary_name"]}={r["n_positive_in_primary"]}({float(r["share_of_activity"])*100:.1f}%)' for r in rows[:5]))

print("\n=== D8c G1 weighted comparison (selected rows) ===")
for r in read("tables/D8c_common_function_weighted_comparison.csv"):
    if r["activity_code"] in ("ACT_DEPLOYMENT", "ACT_ENGINEERING", "ACT_QUALITY", "ACT_RESEARCH", "ACT_BUSINESS"):
        f = lambda v: "NA" if v in ("", None) else f"{float(v)*100:.1f}%"
        print(f'{r["activity_name"]:<10} GALBOT all={f(r["CN_GALBOT_share_all"])} self={f(r["CN_GALBOT_share_self_weighted"])} '
              f'eq={f(r["CN_GALBOT_share_equal_weighted"])} | AGIBOT all={f(r["CN_AGIBOT_share_all"])} '
              f'self={f(r["CN_AGIBOT_share_self_weighted"])} eq={f(r["CN_AGIBOT_share_equal_weighted"])}')

print("\n=== D4 pairs ===")
for r in read("tables/D4_activity_pair_cooccurrence.csv"):
    if r["scope"] == "ALL24":
        print(f'{r["pair_name"]:<18} both={r["n_both_owned_raw"]:>4} uncond={r["n_unconditional"]:>4} cond={r["n_conditional"]} '
              f'alt={r["n_alternative_only"]} unres={r["n_unresolved"]:>3} share={float(r["share_unconditional_of_assessable"])*100:5.2f}% companies={r["n_companies_in_both"]}')

print("\n=== D6/D6b ===")
d6b = read("tables/D6b_company_status_and_gaps.csv")
print("companies", len(d6b), "open gaps total", sum(int(r["n_gaps_open"]) for r in d6b),
      "business rows", sum(int(r["n_responsibility_rows"]) for r in d6b),
      "delivery rows", sum(int(r["n_delivery_rows"]) for r in d6b))

print("\n=== T5/T6 ===")
t5 = read("tables/T5_company_hiring_correspondence.csv")
t6 = read("tables/T6_conclusion_ledger.csv")
print("T5", len(t5), "T6", len(t6))
for r in t6:
    print(r["conclusion_id"], r["status"], "|", r["final_wording"][:80])
