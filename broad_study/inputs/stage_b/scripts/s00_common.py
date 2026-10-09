"""Stage B repair pass / shared helpers.

Design rules enforced here (these are the repair contracts, not conventions):

1. Two hashes per locked file: the byte hash of the file on disk, and the logical
   body hash computed with newlines normalized to \\n. The byte hash catches any
   change; the body hash lets a genuine, content-identical file compare equal even
   when a platform hands it different line endings. A snapshot is rejected only
   when the logical body hash differs as well.
2. Input lock and product manifest are separate documents. The input lock lists
   every file actually read to produce the release, with existence, byte hash and
   identity. The product manifest lists what this run produced. Neither trusts a
   previous run's success document.
3. Every locked document carries the run id, the code version and the hashes of
   the run's own scripts, so a success record can never be replayed against
   different inputs, different code or different outputs.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import unicodedata

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(RUN, "work")
SNAP = os.path.join(RUN, "evidence_snapshots")
R3 = r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_a_r3"
SUBMITTED = r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_b\run_20260914T142852Z"

CODE_VERSION = "stage-b-supplement-v2"
SOURCE_PACK = r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_b_repair_r2\run_20260915T020000Z"

# ---- observation dates ---------------------------------------------------
OBS = {"CN_XSQUARE": "2026-08-31", "US_AMAZON_FTR": "2026-09-11", "CN_FOURIER": "2026-09-11"}
PILOTS = ["CN_XSQUARE", "US_AMAZON_FTR", "CN_FOURIER"]

# ---- status vocabularies -------------------------------------------------
VALUE_STATUS = {
    "SUPPORTED_EXTERNAL",       # an opened outside-company source states it
    "COMPANY_SELF_REPORT",      # the company's own material states it
    "MEDIA_STATEMENT",          # third-party reporting; lead or noted supplement
    "COUNTERPARTY_CONFIRMATION",# customer / partner / regulator states it
    "PARENT_CONTEXT_ONLY",      # parent-company material, background for this subject
    "INHERITED_UNVERIFIED",
    "CONFLICT",
    "CONFLICT_RESOLVED_BY_SEPARATION",
    "MIXED_SEE_EVIDENCE",
    "ACCESS_BLOCKED",
    "SEARCHED_NOT_FOUND",
    "NOT_YET_SEARCHED",
    "NOT_APPLICABLE",
    "EXPLICITLY_NEGATED",
    "UNKNOWN",
}
RESEARCH_STATUS = {
    "SEARCHED_FOUND", "SEARCHED_NOT_FOUND", "NOT_YET_SEARCHED", "ACCESS_BLOCKED", "NOT_APPLICABLE",
}
TIME_APPLICABILITY = {
    "USABLE_AT_OBSERVATION",
    "RETROSPECTIVE_LATE_PUBLISH",
    "POST_OBSERVATION_EVENT",
    "DATE_IMPRECISE_SPANS_OBS",
    "DATE_UNKNOWN",
    "NOT_TIME_SENSITIVE",
}
# statuses that may take part in a strict time-point comparison
STRICT_COMPARABLE_TIME = {"USABLE_AT_OBSERVATION", "NOT_TIME_SENSITIVE"}
# value statuses that establish a value at all
ESTABLISHED_VALUE_STATUS = {
    "SUPPORTED_EXTERNAL", "COMPANY_SELF_REPORT", "MEDIA_STATEMENT", "COUNTERPARTY_CONFIRMATION",
    "CONFLICT_RESOLVED_BY_SEPARATION", "MIXED_SEE_EVIDENCE",
}
# value statuses that may never be turned into a definite negative group
NON_DEFINITE_STATUS = {
    "SEARCHED_NOT_FOUND", "NOT_YET_SEARCHED", "ACCESS_BLOCKED", "UNKNOWN", "CONFLICT",
    "INHERITED_UNVERIFIED",
}
RELATIONS = {"SUPPORTS", "CONTEXT_ONLY", "REPLACES", "REFUTES", "ACCESS_NOTE", "INHERITED_CONTEXT"}
# only these two relations give an assertion its date qualification
QUALIFYING_RELATIONS = {"SUPPORTS", "REFUTES"}
ACCESS_STATUS = {"OK", "OK_ARCHIVED", "HTTP_ERROR", "TLS_ERROR", "DNS_ERROR", "TIMEOUT", "BLOCKED", "NOT_ATTEMPTED"}
CLAIM_NATURE = {
    "COMPANY_SELF_REPORT", "EXTERNAL_CONFIRMATION", "MEDIA_REPORT", "REGULATORY_FILING",
    "PARENT_CONTEXT", "SEARCH_RECORD", "ACCESS_NOTE", "COUNTERPARTY_STATEMENT",
}
SOURCE_NATURE = {
    "OFFICIAL_COMPANY", "REGULATORY_OR_EXCHANGE", "COUNTERPARTY_CONFIRMATION",
    "GOVERNMENT_OR_STANDARDS", "MEDIA", "THIRD_PARTY_DATABASE", "ARCHIVE",
    "RESEARCH_INSTITUTION", "INHERITED_LOCAL_FILE",
}

# ---- inherited input inventory -------------------------------------------
# Key r3 tables are hashed against the r3 release manifest; the rest are hashed
# from disk with their identity recorded so a swap cannot go unnoticed.
R3_RELEASE_MANIFEST = "release_checksums.json"
R3_REQUIRED_TABLES = [
    "company_gaps.csv", "company_evidence.csv", "company_profile.csv",
    "T1_sample_company.csv", "jobs.csv", "company_inheritance_meta.json",
    "field_mapping.md", "analysis_manifest.json",
]
R3_LOCKED_DIR = "locked_inputs"
# every research source file this run reads (repair inputs live in work/)
RESEARCH_SOURCES = ["pilot_facts_CN_XSQUARE.json", "pilot_facts_US_AMAZON_FTR.json",
                    "pilot_facts_CN_FOURIER.json"]
# the config/rule documents that drive generation
RULE_DOCS = ["grouping_rules_source.json", "relation_policy.json", "evidence_identity_baseline.json", "capital_claim_bindings.json", "supplement_sources.json", "supplement_ingestion.json"]
# step entrypoints whose hash is part of every success record
CODE_FILES = [
    "s00_common.py", "s00_pipeline.py", "s01_lock_inputs.py", "s01b_rebuild_snapshots.py",
    "s02_build_facts.py", "s03_build_tables.py", "s03_fetch.py", "s03b_company_profile.py",
    "s04_verify.py", "s05_grouping.py", "s06_rebuild_and_fault.py", "s07_cards_and_html.py",
    "s08_docs.py", "s08_html_runtime_check.js", "s09_search_log.py", "s11b_search_log_ext.py",
    "s10_checksums.py",
    "s11_release_gate.py", "s12_repair_docs.py", "d01_diagnose.py", "d02_evidence_index.py",
    "d03_group_bindings.py", "_apply_targeted.py", "s13_semantic_checks.py", "s14_reproduce.py",
]


# fact fields every researched company must be assessed on (uniform core fields)
CORE_FIELDS = [
    "legal_entity_name",
    "research_subject",
    "parent_relationship",
    "hq_or_team_location",
    "founded_or_team_start_date",
    "hiring_board_channel",
    "observation_coverage",
    "product_lines",
    "delivery_form",
    "target_markets",
    "named_customers_or_partners",
    "deployment_status_actual",
    "evidence_demo",
    "evidence_loi_intent",
    "evidence_internal_test",
    "evidence_external_pilot",
    "evidence_production_shipment",
    "evidence_customer_delivery",
    "evidence_paid",
    "evidence_repeat_order",
    "evidence_sustained_use",
    "own_listing_status",
    "parent_listing_status",
    "latest_financing_disclosed",
    "latest_financing_at_observation",
    "ma_events",
]
# a core field may be satisfied by one of several scope-split rows
CORE_FIELD_SPLIT_CHILDREN = {
    "product_lines": ["product_lines_rehab", "product_lines_humanoid", "product_lines_companion"],
    "target_markets": ["target_markets_malaysia", "target_markets_singapore",
                       "target_markets_domestic_rehab"],
}


def read_csv(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: str, fieldnames: list[str], rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in fieldnames})


def write_json(path: str, obj) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def read_json(path: str):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def append_jsonl(path: str, obj) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(obj, ensure_ascii=False) + "\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def body_text_hash(path: str) -> str:
    """Byte hash of the normalized body text exactly as saved.

    This is the hash every snapshot declares, so comparing the declaration against
    this value detects a real content change in the saved body.
    """
    return sha256_file(path)


def normalized_newline_hash(path: str) -> str:
    """Same body with every newline normalized to \\n.

    Used as a secondary equality test so that a platform that rewrites line endings
    without changing content is not reported as tampering.
    """
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8", errors="replace")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def file_identity(path: str) -> dict:
    """Existence + byte hash + logical body hash + identity of one locked file."""
    if not os.path.exists(path):
        return {"path": path, "exists": False, "bytes": None, "sha256": None,
                "body_text_sha256": None, "normalized_newline_sha256": None, "is_text": None}
    size = os.path.getsize(path)
    is_text = path.lower().endswith((".txt", ".csv", ".json", ".md", ".jsonl", ".html", ".yaml", ".yml"))
    return {
        "path": path,
        "exists": True,
        "bytes": size,
        "sha256": sha256_file(path),
        "body_text_sha256": body_text_hash(path) if is_text else None,
        "normalized_newline_sha256": normalized_newline_hash(path) if is_text else None,
        "is_text": is_text,
    }


def resolve_locked_path(entry: dict) -> str:
    """Resolve a lock entry to a file in the current run or the sealed r3 tree.

    External r3 originals stay at the sealed r3 root. Everything this run owns
    (research sources, snapshots, search log, companies.json) resolves under RUN
    via the stable identity, never via a stale absolute path from another copy.
    """
    identity = (entry.get("identity") or "").replace("\\", "/")
    role = entry.get("role") or ""
    original = entry.get("path") or ""
    if role.startswith("r3_") or identity.startswith("stage_a_r3/"):
        rel = identity.split("stage_a_r3/", 1)[-1] if "stage_a_r3/" in identity else os.path.relpath(original, R3) if original else os.path.basename(original)
        return os.path.join(R3, rel.replace("/", os.sep))
    if identity:
        return os.path.join(RUN, identity.replace("/", os.sep))
    return original


def qualify_pairs(pairs: list[tuple[str, str]], obs: str, *, time_sensitive: bool = True) -> tuple[str, str, str, str]:
    """Qualify one assertion from per-evidence (event, publication) pairs.

    Event and publication of the same source stay together. Dates from different
    sources are never sorted independently and then recombined.
    """
    if not time_sensitive:
        evs = [e for e, _p in pairs if e]
        pubs = [p for _e, p in pairs if p]
        return ("NOT_TIME_SENSITIVE", "structural fact: no point-in-time judgement",
                evs[0] if evs else "", pubs[0] if pubs else "")
    if not pairs:
        return ("DATE_UNKNOWN", "no qualifying evidence pair", "", "")
    ranked = []
    for ev, pub in pairs:
        ta, reason = time_applicability(ev or "", pub or "", obs, time_sensitive=True)
        ranked.append((ta, reason, ev or "", pub or ""))
    usable = [r for r in ranked if r[0] == "USABLE_AT_OBSERVATION"]
    if usable:
        return usable[0]
    for code in ("POST_OBSERVATION_EVENT", "RETROSPECTIVE_LATE_PUBLISH", "DATE_IMPRECISE_SPANS_OBS"):
        hit = [r for r in ranked if r[0] == code]
        if hit:
            return hit[0]
    return ranked[0]


def norm_key(text: str) -> str:
    t = unicodedata.normalize("NFKC", text or "").strip().lower()
    return re.sub(r"\s+", " ", t)


def date_precision(value: str) -> str:
    v = (value or "").strip()
    if not v:
        return "NONE"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        return "DAY"
    if re.fullmatch(r"\d{4}-\d{2}", v):
        return "MONTH"
    if re.fullmatch(r"\d{4}", v):
        return "YEAR"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}/\d{4}-\d{2}-\d{2}", v):
        return "DAY_RANGE"
    if re.fullmatch(r"\d{4}-\d{2}/\d{4}-\d{2}", v):
        return "MONTH_RANGE"
    return "OTHER"


def compare_to_obs(value: str, obs: str) -> str:
    """Compare one date value against the observation date, never expanding precision.

    Returns BEFORE / SPANS / AFTER / UNKNOWN.
    """
    v = (value or "").strip()
    p = date_precision(v)
    if p == "NONE":
        return "UNKNOWN"
    if p == "DAY":
        return "BEFORE" if v <= obs else "AFTER"
    if p == "MONTH":
        if v[:7] == obs[:7]:
            return "SPANS"
        return "AFTER" if v[:7] > obs[:7] else "BEFORE"
    if p == "YEAR":
        if v == obs[:4]:
            return "SPANS"
        return "AFTER" if v > obs[:4] else "BEFORE"
    if p in ("DAY_RANGE", "MONTH_RANGE"):
        parts = v.split("/")
        p0, p1 = compare_to_obs(parts[0], obs), compare_to_obs(parts[1], obs)
        if p0 == p1:
            return p0
        if "SPANS" in (p0, p1) or {p0, p1} == {"BEFORE", "AFTER"}:
            return "SPANS"
        return "AFTER" if "AFTER" in (p0, p1) else ("BEFORE" if "BEFORE" in (p0, p1) else "UNKNOWN")
    return "UNKNOWN"


def time_applicability(event_date: str, publication_date: str, obs: str, *,
                       time_sensitive: bool = True) -> tuple[str, str]:
    """Time qualification of one assertion from its qualifying evidence only.

    The event and the publication are judged separately; an assertion is usable
    only when both are at or before the observation date. Returns
    (applicability, reason).
    """
    if not time_sensitive:
        return "NOT_TIME_SENSITIVE", "structural fact: no point-in-time judgement"
    ev, pub = (event_date or "").strip(), (publication_date or "").strip()
    if not ev and not pub:
        return "DATE_UNKNOWN", "qualifying evidence carries neither an event date nor a publication date"
    ev_rel = compare_to_obs(ev, obs) if ev else "UNKNOWN"
    pub_rel = compare_to_obs(pub, obs) if pub else "UNKNOWN"

    if ev_rel == "AFTER":
        return "POST_OBSERVATION_EVENT", f"event {ev} is after the observation date {obs}"
    if pub_rel == "AFTER":
        # event is at/before the observation date (or undated) but was published later
        return ("RETROSPECTIVE_LATE_PUBLISH",
                f"publication {pub} is after the observation date {obs}"
                + (f"; event {ev} is at or before it" if ev_rel == "BEFORE" else "; event date unknown"))
    if ev_rel == "SPANS" or pub_rel == "SPANS":
        return ("DATE_IMPRECISE_SPANS_OBS",
                f"imprecise date spans the observation date {obs} (event={ev or 'n/a'}, publication={pub or 'n/a'})")
    if ev_rel == "BEFORE" and pub_rel == "BEFORE":
        return ("USABLE_AT_OBSERVATION",
                f"event {ev} and publication {pub} are at or before the observation date {obs}")
    if not ev and pub_rel == "BEFORE":
        return ("USABLE_AT_OBSERVATION",
                f"no event date; publication {pub} is at or before the observation date {obs}")
    if ev_rel == "BEFORE" and pub_rel == "UNKNOWN":
        return ("DATE_UNKNOWN",
                f"event {ev} is dated but the same source has no publication date, so it cannot "
                f"be placed in the observation-day comparison")
    return "DATE_UNKNOWN", f"dates could not be placed relative to the observation date (event={ev or 'n/a'}, publication={pub or 'n/a'})"


def qualify_assertion(pairs: list[tuple[str, str]], obs: str, *,
                      time_sensitive: bool = True) -> tuple[str, str, str, str]:
    """Qualify one assertion from per-source (event, publication) pairs.

    Builder and verifier share this function. Dates from different sources are never
    sorted independently and then recombined into a pair that no single source states.
    """
    return qualify_pairs(pairs, obs, time_sensitive=time_sensitive)


def stable(rows: list[dict], keys: list[str]) -> list[dict]:
    return sorted(rows, key=lambda r: tuple(str(r.get(k, "")) for k in keys))


def load_companies(work: str | None = None) -> list[dict]:
    """The 24 inherited company_ids with their observation wave.

    Derived from the sealed r3 T1 sample and jobs table, never hard-coded.
    """
    work = work or WORK
    cached = os.path.join(work, "companies.json")
    if os.path.exists(cached):
        with open(cached, "r", encoding="utf-8") as fh:
            return json.load(fh)
    t1 = read_csv(os.path.join(R3, "T1_sample_company.csv"))
    jobs = read_csv(os.path.join(R3, "jobs.csv"))
    waves: dict[str, dict[str, int]] = {}
    wave_field = None
    if jobs:
        for cand in ("observation_date", "wave", "observation_dates", "obs_date"):
            if cand in jobs[0]:
                wave_field = cand
                break
    for j in jobs:
        cid = j.get("company_id", "")
        waves.setdefault(cid, {})
        key = str(j.get(wave_field, "")) if wave_field else ""
        waves[cid][key] = waves[cid].get(key, 0) + 1
    companies = []
    for row in t1:
        cid = row["company_id"]
        companies.append({
            "company_id": cid,
            "company_name": row.get("company_name", ""),
            "country": row.get("country", ""),
            "n_ads": int(row["n_ads"]) if row.get("n_ads", "").strip() else None,
            "observation_dates_t1": row.get("observation_dates", ""),
            "waves_from_jobs": dict(sorted(waves.get(cid, {}).items())),
            "entity_scope_inherited": row.get("entity_scope_inherited", ""),
            "hiring_scope_inherited": row.get("hiring_scope_inherited", ""),
        })
    write_json(cached, companies)
    return companies
