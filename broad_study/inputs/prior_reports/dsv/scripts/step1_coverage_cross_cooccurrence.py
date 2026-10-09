#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage D step 1.

Coverage and concentration (D1), Q2/Q3 coverage (D2), role-activity
bidirectional cross (D3), three activity-pair co-occurrence groups with
relation adjudication (D4/D5).

Reads fixed Stage C / Stage B / rules-v1 published inputs read-only and
writes only derived Stage D tables. No reclassification, no new collection.
"""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
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

TAB = RUN / "tables"
VER = RUN / "verification"
TAB.mkdir(parents=True, exist_ok=True)
VER.mkdir(parents=True, exist_ok=True)


def read(path: Path):
    with Path(path).open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write(name: str, rows, fields):
    path = TAB / name
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        wr.writeheader()
        for row in rows:
            wr.writerow(row)
    return path


def jdump(obj, name: str):
    path = VER / name
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def num(v, default=0):
    return int(v) if v not in (None, "", "NA") else default


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def ratio(a, b):
    if not b:
        return None
    return round(a / b, 10)


def quantile(values, p):
    vals = sorted(values)
    if not vals:
        return None
    k = (len(vals) - 1) * p
    lo = int(k)
    hi = min(lo + 1, len(vals) - 1)
    return round(vals[lo] + (vals[hi] - vals[lo]) * (k - lo), 10)


# ----------------------------------------------------------------- inputs
jobs = read(C / "inputs/rules_v1/inputs/stage_a/jobs.csv")
t1 = read(C / "tables/T1_company_sample.csv")
t2 = read(C / "tables/T2_company_primary_roles.csv")
t2agg = read(C / "tables/T2_aggregates.csv")
t3adm = read(C / "tables/T3_base_admission.csv")
t3lin = read(C / "tables/T3_positive_unknown_lineage.csv")
t3agg = read(C / "tables/T3_aggregates.csv")
t4cross = read(C / "tables/T4_primary_activity_cross.csv")
t4co = read(C / "tables/T4_activity_company.csv")
t4agg = read(C / "tables/T4_activity_aggregates.csv")
t4adm = read(C / "tables/T4_activity_admission.csv")
t4lin = read(C / "tables/T4_activity_lineage.csv")
t4struct = read(C / "tables/T4_role_structures.csv")

company = {r["company_id"]: r for r in t1}
WHOLE = sorted(c for c, r in company.items() if r["scope_main_company"] == "YES")
FAR = sorted(c for c, r in company.items() if r["scope_main_company"] != "YES")
jobs_by_id = {j["identity_key"]: j for j in jobs}
assert len(jobs_by_id) == len(jobs) == 1654, len(jobs)

ACTIVITY_NAMES = {}
for r in t4agg:
    ACTIVITY_NAMES[r["label_code"]] = r["label_name"]

eligible = {r["identity_key"] for r in t4adm if r["base_eligible"] == "YES"}
n_assess_all24 = len(eligible)

owned = defaultdict(set)
part = defaultdict(set)
for r in t4lin:
    if r["identity_key"] not in eligible:
        continue
    if r["relation"] == "OWNED":
        owned[r["label_code"]].add(r["identity_key"])
    elif r["relation"] == "PARTICIPATES":
        part[r["label_code"]].add(r["identity_key"])


def company_of(ik):
    return jobs_by_id[ik]["company_id"]


def in_scope(ik, scope):
    return True if scope == "ALL24" else company_of(ik) in set(WHOLE)


ASSESS_BY_SCOPE = {
    "ALL24": n_assess_all24,
    "WHOLE23": sum(1 for i in eligible if company_of(i) in set(WHOLE)),
}

checks = {"n_ads": len(jobs), "n_assessable_all24": n_assess_all24,
          "n_assessable_whole23": ASSESS_BY_SCOPE["WHOLE23"],
          "n_whole_companies": len(WHOLE), "far": FAR}

# ------------------------------------------------- D1 coverage & concentration
CLASS_META = {}
for r in t2:
    CLASS_META[r["class_code"]] = (r["class_name"], r["class_kind"])
order = [r["class_code"] for r in t2agg
         if r["scope"] == "ALL24" and r["denominator_basis"] == "ALL"
         and r["class_kind"] != "unspecified"]

per_company = defaultdict(dict)
for r in t2:
    per_company[r["company_id"]][r["class_code"]] = r

d1_rows = []
for code in order:
    name, kind = CLASS_META.get(code, ("", ""))
    denom_all = sum(num(per_company[c].get(code, {}).get("denominator_all")) for c in WHOLE)
    pos_all = sum(num(per_company[c].get(code, {}).get("n_coded")) for c in WHOLE)
    denom_coded = sum(num(per_company[c].get(code, {}).get("denominator_coded")) for c in WHOLE)
    shares_all = [fnum(per_company[c][code]["share_all"]) for c in WHOLE
                  if code in per_company[c] and num(per_company[c][code]["denominator_all"]) > 0]
    shares_all = [s for s in shares_all if s is not None]
    shares_coded = [fnum(per_company[c][code]["share_coded"]) for c in WHOLE
                    if code in per_company[c] and num(per_company[c][code]["denominator_coded"]) > 0]
    shares_coded = [s for s in shares_coded if s is not None]
    n_pos_companies = sum(1 for c in WHOLE if num(per_company[c].get(code, {}).get("n_coded")) > 0)
    largest_den_c = max(WHOLE, key=lambda c: num(per_company[c].get(code, {}).get("denominator_all")), default=None)
    largest_pos_c = max(WHOLE, key=lambda c: num(per_company[c].get(code, {}).get("n_coded")), default=None)
    largest_den = num(per_company[largest_den_c].get(code, {}).get("denominator_all")) if largest_den_c else 0
    largest_pos = num(per_company[largest_pos_c].get(code, {}).get("n_coded")) if largest_pos_c else 0
    d1_rows.append({
        "scope": "WHOLE23",
        "class_code": code,
        "class_name": name,
        "class_kind": kind,
        "n_ads_ad_weighted": pos_all,
        "denominator_all_ads": denom_all,
        "denominator_coded_ads": denom_coded,
        "n_companies_with_denominator": len(shares_all),
        "n_companies_positive": n_pos_companies,
        "share_ad_weighted_all": ratio(pos_all, denom_all),
        "share_company_equal_all": round(sum(shares_all) / len(shares_all), 10) if shares_all else None,
        "share_ad_weighted_coded": ratio(pos_all, denom_coded),
        "share_company_equal_coded": round(sum(shares_coded) / len(shares_coded), 10) if shares_coded else None,
        "company_share_p25": quantile(shares_all, 0.25),
        "company_share_median": quantile(shares_all, 0.50),
        "company_share_p75": quantile(shares_all, 0.75),
        "company_share_min": round(min(shares_all), 10) if shares_all else None,
        "company_share_max": round(max(shares_all), 10) if shares_all else None,
        "largest_company_id": largest_den_c,
        "largest_company_denominator_contribution": ratio(largest_den, denom_all),
        "largest_company_positive_contribution": ratio(largest_pos, pos_all) if pos_all else None,
        "n_companies_zero_observed": len(shares_all) - n_pos_companies,
        "note": "WHOLE23=整公司23家；分母为公司全部认可广告；观测零公司进入分布",
    })

# unspecified (ambiguous + unmapped + source unassessable) coverage
UNSPEC = ["primary_AMBIGUOUS", "primary_UNMAPPED", "primary_SOURCE_UNASSESSABLE"]
unspec_rows = []
for tag in UNSPEC:
    tot = sum(num(company[c][tag]) for c in WHOLE)
    den = sum(num(company[c]["n_ads"]) for c in WHOLE)
    shares = [num(company[c][tag]) / num(company[c]["n_ads"]) for c in WHOLE if num(company[c]["n_ads"])]
    unspec_rows.append({
        "scope": "WHOLE23", "class_code": tag, "class_name": tag, "class_kind": "status",
        "n_ads_ad_weighted": tot, "denominator_all_ads": den, "denominator_coded_ads": "",
        "n_companies_with_denominator": len(shares), "n_companies_positive": sum(1 for c in WHOLE if num(company[c][tag]) > 0),
        "share_ad_weighted_all": ratio(tot, den),
        "share_company_equal_all": round(sum(shares) / len(shares), 10) if shares else None,
        "share_ad_weighted_coded": "", "share_company_equal_coded": "",
        "company_share_p25": quantile(shares, 0.25), "company_share_median": quantile(shares, 0.50),
        "company_share_p75": quantile(shares, 0.75),
        "company_share_min": round(min(shares), 10) if shares else None,
        "company_share_max": round(max(shares), 10) if shares else None,
        "largest_company_id": "", "largest_company_denominator_contribution": "",
        "largest_company_positive_contribution": "", "n_companies_zero_observed": "",
        "note": "未明确主类比例；不解释为公司不需要该工作",
    })

D1_FIELDS = list(d1_rows[0].keys())
write("D1_q1_coverage_concentration.csv", d1_rows + unspec_rows, D1_FIELDS)

# ------------------------------------------------- D2 Q2/Q3 coverage
base_by_id = defaultdict(set)   # identity -> {(role,dimension)}
for r in t3adm:
    if r["base_eligible"] == "YES":
        base_by_id[r["identity_key"]].add((r["role_code"], r["dimension"]))

cell_present = defaultdict(set)
cell_unknown = defaultdict(set)
for r in t3lin:
    key = (r["role_code"], r["dimension"], r["label_code"], r["metric_bucket"], r["branch_bucket"])
    if r["state"] == "PRESENT":
        cell_present[key].add(r["identity_key"])
    elif r["state"] == "UNKNOWN":
        cell_unknown[key].add(r["identity_key"])

def base_ids(role, dim):
    return {ik for ik, keys in base_by_id.items() if (role, dim) in keys}

d2_rows = []
for r in t3agg:
    role, dim = r["role_code"], r["dimension"]
    lab, mb, bb = r["label_code"], r["metric_bucket"], r["branch_bucket"]
    key = (role, dim, lab, mb, bb)
    scope = r["group"] if r["group"] in ("WHOLE23", "ALL24") else "WHOLE23"
    b_all = base_ids(role, dim)
    b = {i for i in b_all if in_scope(i, scope) and (r["group"] != "WHOLE23" or True)}
    if scope == "WHOLE23":
        b = {i for i in b if company_of(i) in set(WHOLE)}
    pres = {i for i in cell_present.get(key, set()) if i in b}
    unk = {i for i in cell_unknown.get(key, set()) if i in b}
    interp = b - unk
    by_company_interp = Counter(company_of(i) for i in interp)
    by_company_pres = Counter(company_of(i) for i in pres)
    ordered_interp = sorted(by_company_interp.items())
    ordered_pres = sorted(by_company_pres.items())
    largest_den_c = max(ordered_interp, key=lambda kv: kv[1])[0] if ordered_interp else ""
    largest_pos_c = max(ordered_pres, key=lambda kv: kv[1])[0] if ordered_pres else ""
    eq_shares = [by_company_pres.get(c, 0) / n for c, n in ordered_interp if n]
    share_equal = round(sum(eq_shares) / len(eq_shares), 10) if eq_shares else None
    d2_rows.append({
        "q": "Q2", "scope": scope, "role_code": role, "dimension": dim,
        "label_code": lab, "label_name": r["label_name"],
        "metric_bucket": mb, "branch_bucket": bb,
        "main_display": r["main_display"], "display_status": r["display_status"],
        "n_base": len(b), "n_union_unknown": len(unk), "n_interpretable": len(interp),
        "n_positive": len(pres),
        "n_companies_base": len({company_of(i) for i in b}),
        "n_companies_interpretable": len(by_company_interp),
        "n_companies_positive": len(by_company_pres),
        "share_ad_weighted": ratio(len(pres), len(interp)),
        "share_company_equal": share_equal,
        "largest_company_id_by_denominator": largest_den_c,
        "largest_company_denominator_contribution": ratio(by_company_interp[largest_den_c], len(interp)) if largest_den_c else None,
        "largest_company_id_by_positive": largest_pos_c,
        "largest_company_positive_contribution": ratio(by_company_pres[largest_pos_c], len(pres)) if largest_pos_c else None,
        "gate_3companies_20ads": "PASS" if (len(by_company_interp) >= 3 and len(interp) >= 20) else "FAIL",
    })

# Q3 coverage per activity (company table already satisfies fixed denominators)
q3_rows = []
for lab, lname in ACTIVITY_NAMES.items():
    rows = [r for r in t4co if r["label_code"] == lab]
    for scope in ("ALL24", "WHOLE23"):
        if scope == "WHOLE23":
            rows_s = [r for r in rows if r["company_id"] in set(WHOLE)]
        else:
            rows_s = rows
        den = sum(num(r["n_assessable"]) for r in rows_s)
        pos = sum(num(r["n_positive"]) for r in rows_s)
        interp_c = Counter({r["company_id"]: num(r["n_assessable"]) for r in rows_s if num(r["n_assessable"]) > 0})
        pres_c = Counter({r["company_id"]: num(r["n_positive"]) for r in rows_s if num(r["n_positive"]) > 0})
        lden = max(interp_c, key=interp_c.get) if interp_c else ""
        lpos = max(pres_c, key=pres_c.get) if pres_c else ""
        q3_rows.append({
            "q": "Q3", "scope": scope, "label_code": lab, "label_name": lname,
            "relation": "OWNED",
            "n_companies_base": len({r["company_id"] for r in rows_s if num(r["n_all_ads"]) > 0}),
            "n_companies_interpretable": len(interp_c),
            "n_companies_positive": len(pres_c),
            "n_assessable": den, "n_positive": pos,
            "share_ad_weighted": ratio(pos, den),
            "share_company_equal": round(sum(num(r["n_positive"]) / num(r["n_assessable"]) for r in rows_s if num(r["n_assessable"])) / max(1, len(interp_c)), 10),
            "largest_company_id_by_denominator": lden,
            "largest_company_denominator_contribution": ratio(interp_c[lden], den) if lden else None,
            "largest_company_id_by_positive": lpos,
            "largest_company_positive_contribution": ratio(pres_c[lpos], pos) if lpos else None,
            "gate_3companies_20ads": "PASS" if (len(interp_c) >= 3 and den >= 20) else "FAIL",
        })

D2_FIELDS = ["q", "scope", "role_code", "dimension", "label_code", "label_name",
             "metric_bucket", "branch_bucket", "main_display", "display_status",
             "n_base", "n_union_unknown", "n_interpretable", "n_positive",
             "n_companies_base", "n_companies_interpretable", "n_companies_positive",
             "share_ad_weighted", "share_company_equal",
             "largest_company_id_by_denominator", "largest_company_denominator_contribution",
             "largest_company_id_by_positive", "largest_company_positive_contribution",
             "gate_3companies_20ads"]
for row in d2_rows:
    row.setdefault("main_display", "")
for row in q3_rows:
    row.setdefault("role_code", "")
    row.setdefault("dimension", "")
    row.setdefault("metric_bucket", "")
    row.setdefault("branch_bucket", "")
    row.setdefault("main_display", "")
    row.setdefault("display_status", "")
    row.setdefault("n_base", "")
    row.setdefault("n_union_unknown", "")
d2_rows_sorted = sorted(d2_rows, key=lambda r: (r["role_code"], r["dimension"], r["label_code"], r["metric_bucket"], r["branch_bucket"]))
write("D2_q2_coverage_concentration.csv", d2_rows_sorted, D2_FIELDS)
write("D2_q3_coverage_concentration.csv", q3_rows, D2_FIELDS)

# ------------------------------------------------- D3 role x activity cross
primary_of = {}
for j in jobs:
    primary_of[j["identity_key"]] = j["primary_code"] if j["primary_status"] == "CODED" else j["primary_status"]

d3_classes = order + sorted({c for c in set(primary_of.values()) if c not in order})
d3_rows = []
for scope in ("ALL24", "WHOLE23"):
    ids = {i for i in eligible if in_scope(i, scope)}
    for lab, lname in ACTIVITY_NAMES.items():
        pos_all = owned[lab] & ids
        for code in d3_classes:
            sel = {i for i in ids if primary_of[i] == code}
            pos = sel & pos_all
            if not sel and not pos:
                continue
            d3_rows.append({
                "scope": scope, "primary_code": code, "primary_name": CLASS_META.get(code, ("", ""))[0],
                "primary_kind": CLASS_META.get(code, ("", ""))[1],
                "activity_code": lab, "activity_name": lname, "relation": "OWNED",
                "n_primary_assessable": len(sel), "n_positive_in_primary": len(pos),
                "share_within_primary": ratio(len(pos), len(sel)),
                "n_activity_positive_total": len(pos_all),
                "share_of_activity": ratio(len(pos), len(pos_all)),
            })
D3_FIELDS = list(d3_rows[0].keys())
write("D3_role_activity_bidirectional.csv", d3_rows, D3_FIELDS)

# headline cross-check against the three fixed readings
def headline(act, scope="ALL24"):
    ids = {i for i in eligible if in_scope(i, scope)}
    pos = owned[act] & ids
    rows = [r for r in d3_rows if r["scope"] == scope and r["activity_code"] == act]
    return pos, rows

hcheck = {}
for act, expect in (("ACT_RESEARCH", 75), ("ACT_DEPLOYMENT", 351), ("ACT_QUALITY", 466)):
    pos, rows = headline(act)
    cnt = Counter(primary_of[i] for i in pos)
    hcheck[act] = {"owned_all24": len(pos), "expected": expect,
                   "matches": len(pos) == expect,
                   "top": sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[:6],
                   "sum_of_primary_rows": sum(r["n_positive_in_primary"] for r in rows),
                   "ambiguous_in_pos": cnt.get("RF_AMBIGUOUS", 0),
                   "source_unassessable_in_pos": cnt.get("SOURCE_UNASSESSABLE", 0)}
checks["headline_cross"] = hcheck

# ------------------------------------------------- D4/D5 activity pair co-occurrence
PAIRS = [
    ("P1_RESEARCH_ENGINEERING", "ACT_RESEARCH", "ACT_ENGINEERING",
     "研究探索与工程实现"),
    ("P2_ENGINEERING_QUALITY", "ACT_ENGINEERING", "ACT_QUALITY",
     "工程实现与质量验证"),
    ("P3_ENGINEERING_DEPLOYMENT", "ACT_ENGINEERING", "ACT_DEPLOYMENT",
     "工程实现与部署维护"),
]

# --- structure adjudication helpers
def collect_nodes(tree):
    """Return list of (node_id, kind, path_top_branch, depth, evidence_ranges)."""
    out = []

    def walk(node, branch, depth):
        nid = node.get("id", "")
        ranges = []
        for ev in node.get("evidence", []) or []:
            if isinstance(ev, dict) and ev.get("field"):
                try:
                    ranges.append((ev["field"], int(ev["start"]), int(ev["end"]), ev.get("quote", "")))
                except (TypeError, ValueError):
                    pass
        out.append({"node_id": nid, "relation": node.get("relation", ""),
                    "depth": depth, "branch": branch, "ranges": ranges})
        for child in node.get("children", []) or []:
            walk(child, branch if depth > 0 else child.get("id", ""), depth + 1)

    walk(tree.get("expression", tree), "", 0)
    return out


def ranges_overlap(a, b):
    return a[0] == b[0] and not (a[2] <= b[1] or b[2] <= a[1])


struct_by_id = {}
for r in t4struct:
    try:
        tree = json.loads(r["tree_json"])
    except json.JSONDecodeError:
        continue
    struct_by_id[r["identity_key"]] = {
        "root_relation": r["root_relation"],
        "has_mixed_branch": r["has_mixed_branch"],
        "nodes": collect_nodes(tree),
    }

mentions = defaultdict(list)
for r in t4lin:
    try:
        s, e = int(r["start"]), int(r["end"])
    except (TypeError, ValueError):
        continue
    mentions[(r["identity_key"], r["label_code"])].append((r["field"], s, e, r["quote"], r["relation"]))


def locate(ik, lab):
    """Deepest structure node covering a mention, by span overlap then text containment."""
    st = struct_by_id.get(ik)
    if not st:
        return None
    best = None
    for (field, s, e, quote, rel) in mentions.get((ik, lab), []):
        qn = "".join(quote.split())
        for node in st["nodes"]:
            hit = False
            for rng in node["ranges"]:
                if ranges_overlap((field, s, e), rng):
                    hit = True
                    break
            if not hit:
                for rng in node["ranges"]:
                    if rng[0] != field:
                        continue
                    nq = "".join(str(rng[3]).split())
                    if len(nq) >= 6 and (nq in qn or qn in nq):
                        hit = True
                        break
            if hit:
                cand = (node["depth"], node["branch"], node["node_id"])
                if best is None or cand[0] > best[0]:
                    best = cand
    if best is None:
        return None
    return {"branch": best[1], "node_id": best[2], "depth": best[0]}


pair_rows = []
pair_lineage = []
for pair_id, act_a, act_b, pair_name in PAIRS:
    both = (owned[act_a] & owned[act_b]) & eligible
    status = Counter()
    for ik in sorted(both):
        st = struct_by_id.get(ik)
        if not st:
            status["UNCONDITIONAL"] += 1
            pair_lineage.append({
                "pair_id": pair_id, "activity_a": act_a, "activity_b": act_b,
                "identity_key": ik, "record_id": jobs_by_id[ik]["record_id"],
                "reading_id": jobs_by_id[ik]["reading_id"], "company_id": company_of(ik),
                "primary_code": primary_of[ik], "root_relation": "", "branch_a": "", "branch_b": "",
                "status": "UNCONDITIONAL", "quote_a": "", "quote_b": "",
                "reason": "无职责关系树；两活动均由原文明确本人承担且无任选/互斥限定",
            })
            continue
        la, lb = locate(ik, act_a), locate(ik, act_b)
        root_rel = st["root_relation"]
        qa = " || ".join(m[3] for m in mentions.get((ik, act_a), []))[:160]
        qb = " || ".join(m[3] for m in mentions.get((ik, act_b), []))[:160]
        if la is None or lb is None:
            stt = "UNRESOLVED"
            reason = "结构树存在但活动文本未落到任何节点区间，无法定位所属性分支"
        elif root_rel == "ALL":
            stt = "UNCONDITIONAL"
            reason = "根关系为复合承担(ALL)，两活动同在一条复合职责内"
        elif la["branch"] and lb["branch"] and la["branch"] == lb["branch"]:
            stt = "CONDITIONAL"
            reason = "根关系为任选(OR)，两活动落在同一可选方向内；仅在该方向被选中时同时承担"
        elif la["branch"] and lb["branch"] and la["branch"] != lb["branch"]:
            stt = "ALTERNATIVE_ONLY"
            reason = "两活动分属不同可选方向，原文为互斥的任选关系"
        else:
            stt = "CONDITIONAL" if (la["branch"] or lb["branch"]) else "UNRESOLVED"
            reason = "一项落在可选方向、另一项未落入具体方向，按条件性共同承担处理"
        status[stt] += 1
        pair_lineage.append({
            "pair_id": pair_id, "activity_a": act_a, "activity_b": act_b,
            "identity_key": ik, "record_id": jobs_by_id[ik]["record_id"],
            "reading_id": jobs_by_id[ik]["reading_id"], "company_id": company_of(ik),
            "primary_code": primary_of[ik], "root_relation": root_rel,
            "branch_a": (la or {}).get("branch", ""), "branch_b": (lb or {}).get("branch", ""),
            "status": stt, "quote_a": qa, "quote_b": qb, "reason": reason,
        })

    for scope in ("ALL24", "WHOLE23"):
        ids = {i for i in eligible if in_scope(i, scope)}
        den = len(ids)
        n_both = len(both & ids)
        st_scoped = Counter(r["status"] for r in pair_lineage
                            if r["pair_id"] == pair_id and r["identity_key"] in ids)
        unresolved = st_scoped.get("UNRESOLVED", 0)
        pair_rows.append({
            "scope": scope, "pair_id": pair_id, "pair_name": pair_name,
            "activity_a": act_a, "activity_a_name": ACTIVITY_NAMES[act_a],
            "activity_b": act_b, "activity_b_name": ACTIVITY_NAMES[act_b],
            "n_assessable": den,
            "n_owned_a": len(owned[act_a] & ids), "n_owned_b": len(owned[act_b] & ids),
            "n_both_owned_raw": n_both,
            "n_unconditional": st_scoped.get("UNCONDITIONAL", 0),
            "n_conditional": st_scoped.get("CONDITIONAL", 0),
            "n_alternative_only": st_scoped.get("ALTERNATIVE_ONLY", 0),
            "n_unresolved": unresolved,
            "n_not_cooccurring": den - n_both,
            "n_denominator_excl_unresolved": den - unresolved,
            "share_unconditional_of_assessable": ratio(st_scoped.get("UNCONDITIONAL", 0), den),
            "share_unconditional_excl_unresolved": ratio(st_scoped.get("UNCONDITIONAL", 0), den - unresolved),
            "n_companies_in_both": len({company_of(i) for i in both & ids}),
        })

D4_FIELDS = ["scope", "pair_id", "pair_name", "activity_a", "activity_a_name",
             "activity_b", "activity_b_name", "n_assessable", "n_owned_a", "n_owned_b",
             "n_both_owned_raw", "n_unconditional", "n_conditional", "n_alternative_only",
             "n_unresolved", "n_not_cooccurring", "n_denominator_excl_unresolved",
             "share_unconditional_of_assessable", "share_unconditional_excl_unresolved",
             "n_companies_in_both"]
write("D4_activity_pair_cooccurrence.csv", pair_rows, D4_FIELDS)

DL_FIELDS = ["pair_id", "activity_a", "activity_b", "identity_key", "record_id", "reading_id",
             "company_id", "primary_code", "root_relation", "branch_a", "branch_b",
             "status", "quote_a", "quote_b", "reason"]
write("D4_activity_pair_lineage.csv", pair_lineage, DL_FIELDS)

# D5 function / company distribution for each pair
d5_rows = []
for pair_id, act_a, act_b, pair_name in PAIRS:
    both = (owned[act_a] & owned[act_b]) & eligible
    by_primary = Counter(primary_of[i] for i in both)
    by_company = Counter(company_of(i) for i in both)
    uncond = {r["identity_key"] for r in pair_lineage
              if r["pair_id"] == pair_id and r["status"] == "UNCONDITIONAL"}
    uncond_primary = Counter(primary_of[i] for i in uncond)
    uncond_company = Counter(company_of(i) for i in uncond)
    for code, n in sorted(by_primary.items(), key=lambda kv: (-kv[1], kv[0])):
        d5_rows.append({
            "pair_id": pair_id, "pair_name": pair_name, "dimension": "primary_function",
            "key": code, "key_name": CLASS_META.get(code, (code, ""))[0],
            "n_both_owned": n, "share_of_both_owned": ratio(n, len(both)),
            "n_unconditional": uncond_primary.get(code, 0),
            "share_of_unconditional": ratio(uncond_primary.get(code, 0), len(uncond)) if uncond else None,
        })
    for cid, n in sorted(by_company.items(), key=lambda kv: (-kv[1], kv[0])):
        d5_rows.append({
            "pair_id": pair_id, "pair_name": pair_name, "dimension": "company",
            "key": cid, "key_name": company[cid]["company_name"],
            "n_both_owned": n, "share_of_both_owned": ratio(n, len(both)),
            "n_unconditional": uncond_company.get(cid, 0),
            "share_of_unconditional": ratio(uncond_company.get(cid, 0), len(uncond)) if uncond else None,
        })
D5_FIELDS = ["pair_id", "pair_name", "dimension", "key", "key_name",
             "n_both_owned", "share_of_both_owned", "n_unconditional", "share_of_unconditional"]
write("D5_activity_pair_structure.csv", d5_rows, D5_FIELDS)

checks["pair_summary"] = [
    {k: r[k] for k in ("scope", "pair_id", "n_assessable", "n_both_owned_raw", "n_unconditional",
                       "n_conditional", "n_alternative_only", "n_unresolved",
                       "share_unconditional_of_assessable", "n_companies_in_both")}
    for r in pair_rows if r["scope"] == "ALL24"
]
checks["n_structured_ads"] = len(struct_by_id)

# cross-check D3 against published T4 cross table (ALL24, OWNED)
mismatch = []
publish = {(r["primary_code"], r["activity_code"]): r for r in t4cross if r["relation"] == "OWNED"}
for r in d3_rows:
    if r["scope"] != "ALL24":
        continue
    p = publish.get((r["primary_code"], r["activity_code"]))
    if p is None:
        continue
    if int(p["n_positive"]) != r["n_positive_in_primary"] or int(p["n_assessable"]) != r["n_primary_assessable"]:
        mismatch.append({"primary": r["primary_code"], "activity": r["activity_code"],
                         "published": (p["n_positive"], p["n_assessable"]),
                         "recomputed": (r["n_positive_in_primary"], r["n_primary_assessable"])})
checks["d3_vs_published_t4_mismatches"] = mismatch
checks["d3_cells_compared"] = sum(1 for r in d3_rows if r["scope"] == "ALL24" and (r["primary_code"], r["activity_code"]) in publish)

jdump(checks, "step1_checks.json")
print(json.dumps(checks, ensure_ascii=False, indent=2)[:4000])
print("D1 rows", len(d1_rows) + len(unspec_rows), "D2 rows", len(d2_rows), "+", len(q3_rows),
      "D3 rows", len(d3_rows), "D4 rows", len(pair_rows), "lineage", len(pair_lineage),
      "D5 rows", len(d5_rows))
