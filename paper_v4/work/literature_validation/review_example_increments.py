"""Review packet and provenance ledger for all robot-model Q -> Q+E increments.

Read-only with respect to source_snapshot and analysis/paired.
Semantic review notes are entered separately in review_annotations.json after
model reading. This script verifies source spans, not human semantic validity.
"""
from pathlib import Path
from collections import defaultdict, Counter
import csv, json, hashlib, re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "analysis/example_increments"
NOTES = Path(__file__).with_name("review_annotations.json")

def readcsv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def writecsv(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    paths = {
        "scope": ROOT / "analysis/paired/qualification_scope_states.csv",
        "evidence": ROOT / "source_snapshot/source_v2/data/inputs/context_evidence.csv",
        "records": ROOT / "source_snapshot/source_v2/data/inputs/records.json",
        "revisions": ROOT / "source_snapshot/data/analysis_revision_ledger.json",
        "v4_revisions": ROOT / "data/v4_source_corrections.json",
    }
    scope = readcsv(paths["scope"])
    evidences = readcsv(paths["evidence"])
    records = json.loads(paths["records"].read_text(encoding="utf-8"))
    revisions = json.loads(paths["revisions"].read_text(encoding="utf-8"))["changes"]
    v4_revisions = json.loads(paths["v4_revisions"].read_text(encoding="utf-8"))["changes"]
    bysource = {r["identity_key"]: r for r in records}
    byev = defaultdict(list)
    for e in evidences:
        byev[e["identity_key"], e["code"]].append(e)
    byrev = {(r["identity_key"], r["label_code"]): r for r in revisions}
    byrev4 = {(r["identity_key"], r["label_code"]): r for r in v4_revisions}
    chosen = sorted((r for r in scope if r["task"] == "ROBOT_MODEL" and
                     r["Q"] != "P" and r["Q_plus_example"] == "P"),
                    key=lambda r: (r["reading_id"], r["label_code"]))
    assert len(chosen) == 44, "Run after coordinated v4 scope refresh including both bare-parenthesis relation sets."
    assert Counter(r["label_code"] for r in chosen) == {"SK_PYTHON": 1, "SK_PYTORCH": 43}
    assert Counter(r["Q"] for r in chosen) == {"Z":42,"U":2}
    notes = json.loads(NOTES.read_text(encoding="utf-8")) if NOTES.exists() else {}
    packet, span_checks, ledger = [], [], []
    unique = {}
    for r in chosen:
        k = r["identity_key"], r["label_code"]
        src = bysource[k[0]]
        ev = byev[k]
        gm = [e for e in ev if e["metric"] in ("GENERAL", "REQUIRED")]
        inherited = [e for e in gm if e["branch"] == "EXAMPLE"]
        revision3 = byrev.get(k)
        revision4 = byrev4.get(k)
        revision = revision4 or revision3
        assert inherited or revision
        assert bool(revision3) == bool(int(r["v3_example_clarification_applied"]))
        selected = inherited if inherited else gm
        evidence_packet = []
        for e in ev:
            field = src["fields"][e["field"]]
            a, b = int(e["verified_start"]), int(e["verified_end"])
            pa, pb = int(e["parent_start"]), int(e["parent_end"])
            ha, hb = int(e["heading_context_start"]), int(e["heading_context_end"])
            checks = {
                "span_exact": field[a:b] == e["quote"],
                "hash_exact": hashlib.sha256(field.encode()).hexdigest() == e["source_field_sha256"],
                "parent_exact": field[pa:pb] == e["parent_text"],
                "parent_contains_target": pa <= a < b <= pb,
                "heading_context_exact": field[ha:hb] == e["heading_to_evidence_context"],
            }
            assert all(checks.values()), (r["reading_id"], e["evidence_id"], checks)
            span_checks.append({"reading_id": r["reading_id"], "label_code": r["label_code"],
                                "evidence_id": e["evidence_id"], **checks})
            paths_to_target = json.loads(e["historical_tree_paths_json"])
            example_nodes = [n["quote"] for p in paths_to_target for n in p if n.get("relation") == "EXAMPLE"]
            ep = {n: e[n] for n in ("evidence_id", "field", "metric", "branch", "quote",
                                  "verified_start", "verified_end", "parent_start", "parent_end",
                                  "parent_text", "nearest_heading_text", "heading_to_evidence_context")}
            ep["example_ancestor_quotes"] = list(dict.fromkeys(example_nodes))
            evidence_packet.append(ep)
        revision_quote_present = not revision or revision["source_quote"] in src["fields"]["full_description"]
        assert revision_quote_present, r["reading_id"]
        if revision4:
            field = src["fields"][revision4["source_field"]]
            assert field[revision4["source_start"]:revision4["source_end"]] == revision4["source_quote"]
            assert hashlib.sha256(field.encode()).hexdigest() == revision4["source_field_sha256"]
            if "identical_full_source_to" in revision4:
                twin = next(s for s in records if s["reading_id"] == revision4["identical_full_source_to"])
                assert field == twin["fields"]["full_description"]
        nk = r["reading_id"] + "|" + r["label_code"]
        ann = notes.get(nk, {})
        entry = {
            "identity_key": k[0], "reading_id": r["reading_id"], "label_code": r["label_code"],
            "company_id": src["company_id"], "company": src["company"], "title": src["title"],
            "source_url": src["source_url"], "Q_before": r["Q"], "Q_plus_example": r["Q_plus_example"],
            "increment_origin": ("v4_consistency_clarification" if revision4 else
                                 "v3_example_clarification" if revision3 else "historical_EXAMPLE_branch"),
            "revision_audit_id": revision["audit_id"] if revision else "",
            "prior_v3_Q": revision4["Q_before"] if revision4 else r["Q"],
            "v3_clarification_flag": bool(revision3),
            "v4_clarification_flag": bool(revision4),
            "historical_qualification_branches": r["qualification_branches"],
            "source_field_sha256": hashlib.sha256(src["fields"]["full_description"].encode()).hexdigest(),
            "all_source_span_parent_heading_checks_pass": True,
            "current_metric_codes": json.dumps(sorted({e["metric"] for e in gm})),
            "increment_evidence_ids": json.dumps([e["evidence_id"] for e in selected]),
            "parent_texts": json.dumps(list(dict.fromkeys(e["parent_text"] for e in selected)), ensure_ascii=False),
            "review_status": "MODEL_FULL_SOURCE_REVIEWED" if ann else "PENDING_MODEL_SOURCE_REVIEW",
            "cue_family": ann.get("cue_family", ""),
            "governing_expression": ann.get("governing_expression", ""),
            "qualification_scope_review": ann.get("qualification_scope_review", ""),
            "counterexample_or_ambiguity": ann.get("counterexample_or_ambiguity", ""),
            "review_conclusion": ann.get("review_conclusion", ""),
            "independent_human_validation": False,
        }
        ledger.append(entry)
        packet.append({"ledger": entry, "evidence": evidence_packet, "revision": revision,
                       "fields": src["fields"]})
        unique.setdefault(r["reading_id"], {"source": src, "targets": []})["targets"].append(r["label_code"])
    assert not (set(notes) - {r["reading_id"] + "|" + r["label_code"] for r in chosen})
    writecsv(OUT / "example_increment_ledger.csv", ledger)
    writecsv(OUT / "source_integrity_checks.csv", span_checks)
    (OUT / "example_increment_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    full = ["# Full captured sources for model review", "", "Local research packet; not an independent human gold standard.", ""]
    for rid, item in unique.items():
        src = item["source"]
        full += ["## " + rid + " | " + src["company"] + " | " + src["title"],
                 "Targets: " + ", ".join(item["targets"]), "", src["fields"]["full_description"], ""]
        for key, value in src["fields"].items():
            if key != "full_description" and value and value not in src["fields"]["full_description"]:
                full += ["Additional captured field: " + key, value, ""]
    (OUT / "full_source_review_packet.md").write_text("\n".join(full), encoding="utf-8")
    summary = {
        "scope": "All ROBOT_MODEL current-Q-non-P to Q_plus_example-positive transitions, including admitted UNCONDITIONAL_OR_EXAMPLE relation sets",
        "n_pairs": len(ledger), "n_advertisements": len(unique),
        "by_technology": dict(Counter(r["label_code"] for r in ledger)),
        "by_origin": dict(Counter(r["increment_origin"] for r in ledger)),
        "by_cue_family": dict(Counter(r["cue_family"] for r in ledger)),
        "review_status": dict(Counter(r["review_status"] for r in ledger)),
        "source_evidence_occurrences_checked": len(span_checks),
        "checks_per_evidence": 5, "all_integrity_checks_pass": True,
        "all_before_states": dict(Counter(r["Q_before"] for r in ledger)),
        "independent_human_validation": False, "blind_review": False,
        "classification_changes_made": False,
        "full_captured_sources_saved": True,
        "source_inputs": [{"path": str(p.relative_to(ROOT)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths.values()],
    }
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
if __name__ == "__main__":
    main()
