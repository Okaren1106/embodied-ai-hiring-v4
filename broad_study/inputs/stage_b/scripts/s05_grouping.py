"""Stage B repair / step 5: grouping rules, group mapping and the comparison bucket.

What changed against the submitted package:

  * the per-company label table no longer decides anything on its own: a group label
    is declared per (company, dimension, fact value) in the locked rule document, and
    a value that is not declared is reported as UNCLASSIFIED_VALUE and excluded
    rather than silently labelled;
  * a dimension enters the strict comparison only when the fact carries an
    established value and its time qualification is usable at the observation date;
  * SEARCHED_NOT_FOUND / NOT_YET_SEARCHED / ACCESS_BLOCKED / UNKNOWN / CONFLICT /
    INHERITED_UNVERIFIED can never produce a definite negative group, so an unknown
    listing status cannot become NOT_LISTED;
  * background and unusable-time values are shown in their own bucket and are never
    counted together with comparable companies.

Outputs: company_group_mapping.csv, grouping_rules.md, work/grouping_summary.json
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import (  # noqa: E402
    ESTABLISHED_VALUE_STATUS, NON_DEFINITE_STATUS, RUN, STRICT_COMPARABLE_TIME, WORK,
    load_companies, read_csv, write_csv, write_json,
)

RULE_FILE = os.path.join(WORK, "grouping_rules_source.json")

# scope-split child field -> the merged field it refines
CHILD_FIELDS: dict[str, list[str]] = {
    "product_lines_rehab": ["product_lines"],
    "product_lines_humanoid": ["product_lines"],
    "product_lines_companion": ["product_lines"],
    "target_markets_malaysia": ["target_markets"],
    "target_markets_singapore": ["target_markets"],
    "target_markets_domestic_rehab": ["target_markets"],
}

GROUP_FIELDS = [
    "company_id", "dimension", "group_value", "basis_fact_ids", "evidence_strength",
    "value_status", "time_applicability", "comparison_bucket",
    "included_in_comparison", "exclusion_reason", "multiple_allowed", "rule_version",
]

BUCKETS = ("STRICT_COMPARABLE", "BACKGROUND_DISPLAY_ONLY", "EXCLUDED_UNKNOWN", "NOT_RESEARCHED")


def bucket_for(fact: dict) -> tuple[str, str]:
    """Return (bucket, reason) for one fact row."""
    status = fact["value_status"]
    if status in NON_DEFINITE_STATUS:
        return "EXCLUDED_UNKNOWN", f"value status {status} does not establish a value"
    if status == "NOT_APPLICABLE":
        return "EXCLUDED_UNKNOWN", "the proposition does not apply to this subject"
    if status not in ESTABLISHED_VALUE_STATUS and status != "PARENT_CONTEXT_ONLY":
        return "EXCLUDED_UNKNOWN", f"value status {status} is not an established value"
    if status == "PARENT_CONTEXT_ONLY":
        return "BACKGROUND_DISPLAY_ONLY", "parent-company material: background only"
    if fact.get("assertion_kind") in ("RESEARCH_OUTPUT", "LONG_TERM_GOAL", "DATE_CONFLICT"):
        return "BACKGROUND_DISPLAY_ONLY", "研究产物、长期目标或首发日期冲突不作当前商业产品/场景分组"
    if fact["time_applicability"] in STRICT_COMPARABLE_TIME:
        return "STRICT_COMPARABLE", ""
    return "BACKGROUND_DISPLAY_ONLY", f"time applicability {fact['time_applicability']}: {fact['time_reason']}"


def main() -> int:
    rules = json.load(open(RULE_FILE, encoding="utf-8"))
    rule_version = rules["rule_version"]
    companies = load_companies()
    facts = read_csv(os.path.join(RUN, "company_facts.csv"))
    links = read_csv(os.path.join(RUN, "evidence_links.csv"))

    by_company_field: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    for f in facts:
        by_company_field[f["company_id"]][f["field"]].append(f)

    rows = []
    unclassified = []
    for dim in rules["dimensions"]:
        dimension = dim["dimension"]
        declared: dict[str, list[dict]] = dim.get("group_bindings", {})
        for c in companies:
            cid = c["company_id"]
            # a scope-split child (product_lines_rehab, target_markets_malaysia, …)
            # is its own dimension with its own bindings, so its time qualification
            # governs only its own region or product line
            field_facts = list(by_company_field.get(cid, {}).get(dimension, []))
            for child, parents in CHILD_FIELDS.items():
                if dimension in parents:
                    field_facts.extend(by_company_field.get(cid, {}).get(child, []))
            if not field_facts:
                rows.append({
                    "company_id": cid, "dimension": dimension, "group_value": "NOT_RESEARCHED",
                    "basis_fact_ids": "", "evidence_strength": "", "value_status": "",
                    "time_applicability": "", "comparison_bucket": "NOT_RESEARCHED",
                    "included_in_comparison": "NO",
                    "exclusion_reason": "no fact row for this dimension (including split child fields)",
                    "multiple_allowed": "YES" if dim["multiple_allowed"] else "NO",
                    "rule_version": rule_version,
                })
                continue
            for fact in field_facts:
                bucket, reason = bucket_for(fact)
                value = (fact["value"] or "").strip()
                per_company = declared.get(cid, {}) if isinstance(declared, dict) else {}
                if value in per_company:
                    labels = per_company[value]
                elif bucket == "EXCLUDED_UNKNOWN" and not value:
                    labels = [f"UNKNOWN_NOT_COMPARABLE:{fact['value_status']}"]
                else:
                    labels = ["UNCLASSIFIED_VALUE"]
                    unclassified.append({"company_id": cid, "dimension": dimension,
                                         "fact_id": fact["fact_id"], "value": value[:80],
                                         "fact_ids": [fact["fact_id"]]})
                if bucket == "EXCLUDED_UNKNOWN" and value:
                    labels = [f"UNKNOWN_NOT_COMPARABLE:{fact['value_status']}"]
                for label in labels:
                    if label == "UNCLASSIFIED_VALUE":
                        # a value the locked rule document does not declare leaves the
                        # comparison entirely, so its bucket never claims comparability
                        bucket = "EXCLUDED_UNKNOWN"
                        include, why = "NO", "value not declared in the locked rule document"
                    elif bucket == "STRICT_COMPARABLE":
                        include, why = "YES", ""
                    elif bucket == "BACKGROUND_DISPLAY_ONLY":
                        include, why = "NO", reason or "background only"
                    else:
                        include, why = "NO", reason
                    rows.append({
                        "company_id": cid, "dimension": dimension, "group_value": label,
                        "basis_fact_ids": fact["fact_id"],
                        "evidence_strength": fact["value_status"],
                        "value_status": fact["value_status"],
                        "time_applicability": fact["time_applicability"],
                        "comparison_bucket": bucket,
                        "included_in_comparison": include,
                        "exclusion_reason": why,
                        "multiple_allowed": "YES" if dim["multiple_allowed"] else "NO",
                        "rule_version": rule_version,
                    })

    write_csv(os.path.join(RUN, "company_group_mapping.csv"), GROUP_FIELDS,
              sorted(rows, key=lambda r: (r["dimension"], r["company_id"], r["group_value"])))

    strict = defaultdict(Counter)
    display_only = defaultdict(Counter)
    excluded = defaultdict(Counter)
    for r in rows:
        if r["comparison_bucket"] == "STRICT_COMPARABLE":
            strict[r["dimension"]][r["group_value"]] += 1
        elif r["comparison_bucket"] == "BACKGROUND_DISPLAY_ONLY":
            display_only[r["dimension"]][r["group_value"]] += 1
        elif r["comparison_bucket"] == "EXCLUDED_UNKNOWN":
            excluded[r["dimension"]][r["group_value"]] += 1

    lines = [
        "# 阶段 B 返修版分组规则与结果",
        "",
        f"- 规则版本：`{rule_version}`",
        "- 规则来源：`work/grouping_rules_source.json`，属被锁定输入，随输入摘要一起校验；改动标签表必须改变输入摘要。",
        "- 取值到组标签的对应关系在规则文件里逐条声明，程序不做关键词归类；未声明的取值标为 `UNCLASSIFIED_VALUE` 并退出比较。",
        "",
        "## 严格比较许可（STRICT_COMPARABLE）",
        "",
        "进入严格比较必须同时满足：取值已确立（SUPPORTED_EXTERNAL / COMPANY_SELF_REPORT / MEDIA_STATEMENT /",
        "COUNTERPARTY_CONFIRMATION / CONFLICT_RESOLVED_BY_SEPARATION / MIXED_SEE_EVIDENCE），且时点适用性为",
        "`USABLE_AT_OBSERVATION` 或 `NOT_TIME_SENSITIVE`。",
        "",
        "未查、查后未找到、访问受阻、未知、冲突、继承未核实一律不生成确定否定组；",
        "只有 `EXPLICITLY_NEGATED`（来源明确否定）与 `NOT_APPLICABLE`（命题不适用于该主体）才可能形成否定取值。",
        "",
    ]
    for dim in rules["dimensions"]:
        dimension = dim["dimension"]
        lines.append(f"### {dim['label']}（`{dimension}`）")
        lines.append("")
        if strict[dimension]:
            lines.append("| 可比较组 | 取值行数 | 公司 | 是否满足 3 家规则 |")
            lines.append("|---|---|---|---|")
            for label, n in strict[dimension].most_common():
                members = sorted({r["company_id"] for r in rows
                                  if r["dimension"] == dimension and r["group_value"] == label
                                  and r["comparison_bucket"] == "STRICT_COMPARABLE"})
                note = "达到展示门槛；待业务组定义与口径确认" if len(members) >= 3 else "不足 3 家，仅作案例展示"
                lines.append(f"| {label} | {n} | {', '.join(members)} | {note} |")
        else:
            lines.append("（本轮无已查公司在该维度形成可比较取值）")
        lines.append("")
        if display_only[dimension]:
            lines.append("仅背景展示（不进入比较）：" + "、".join(f"`{k}`×{v}" for k, v in display_only[dimension].most_common()))
            lines.append("")
        if excluded[dimension]:
            lines.append("退出该维度（未确立取值或不适用）：" + "、".join(f"`{k}`×{v}" for k, v in excluded[dimension].most_common()))
            lines.append("")
        if unclassified:
            pending = [u for u in unclassified if u["dimension"] == dimension]
            if pending:
                lines.append(f"未声明取值（已退出比较）：{len(pending)} 项 — " +
                             "；".join(f"{u['company_id']}「{u['value'][:30]}」" for u in pending[:4]))
                lines.append("")
    lines += [
        "## 使用限制",
        "",
        "1. 本轮 24 家均有公司记录，但字段级未查仍然存在；任何分组都不得当作已完成的 24 家组间统计。",
        "2. 公司业务形态不同，目标场景维度互不重叠时不构成互斥业务组。",
        "3. 商业化证据按演示、意向、内部测试、外部试点、交付、付费、重复订单、持续使用分开记录，未推导成成熟度阶梯；未披露不等于 0。",
        "4. 母公司能力、伙伴 logo、订单额、出货量均不得作为分组或成熟度依据。",
        "",
        "## 追溯",
        "",
        "每个取值可回溯 `basis_fact_ids` → `company_facts.csv` → `evidence_links.csv` 中声明的关系 → 本地快照路径与哈希。",
        "",
    ]
    with open(os.path.join(RUN, "grouping_rules.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    summary = {
        "rule_version": rule_version,
        "n_rows": len(rows),
        "by_bucket": dict(Counter(r["comparison_bucket"] for r in rows).most_common()),
        "strict_by_dimension": {k: dict(v.most_common()) for k, v in strict.items()},
        "background_by_dimension": {k: dict(v.most_common()) for k, v in display_only.items()},
        "excluded_by_dimension": {k: dict(v.most_common()) for k, v in excluded.items()},
        "unclassified_values": unclassified,
        "unknown_negative_guard": {
            "note": "no definite negative group is produced for a non-definite status",
            "non_definite_statuses": sorted(NON_DEFINITE_STATUS),
        },
    }
    write_json(os.path.join(WORK, "grouping_summary.json"), summary)
    print(json.dumps({
        "n_rows": summary["n_rows"],
        "by_bucket": summary["by_bucket"],
        "strict": {k: dict(v) for k, v in strict.items()},
        "unclassified": len(unclassified),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
