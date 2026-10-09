"""Bounded admission-rule alternatives; never changes Q or source labels."""
from pathlib import Path
from collections import Counter, defaultdict
import csv, json, hashlib, unicodedata
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "analysis/example_increments"
def read(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))
def write(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)
def norm(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())
def main():
    scope_path = ROOT / "analysis/paired/qualification_scope_states.csv"
    paired_path = ROOT / "analysis/paired/paired_advertisements.csv"
    note_path = Path(__file__).with_name("review_annotations.json")
    ledger_path = OUT / "example_increment_ledger.csv"
    scope = [r for r in read(scope_path) if r["task"] == "ROBOT_MODEL"]
    pairs = [r for r in read(paired_path) if r["task"] == "ROBOT_MODEL"]
    notes = json.loads(note_path.read_text(encoding="utf-8"))
    increments = read(ledger_path)
    assert len(scope) == 210 and len(pairs) == 105 and len(increments) == 44
    explicit = {"EN_SUCH_AS", "EN_EG", "EXPLICIT_CHINESE_RU"}
    states = []
    for r in scope:
        nk = r["reading_id"] + "|" + r["label_code"]
        ann = notes.get(nk, {})
        family = ann.get("cue_family", "")
        q = r["Q"]
        all_example = r["Q_plus_example"]
        no_bare = q if family == "BARE_PARENTHETICAL_LIST" else all_example
        clear_only = "P" if q == "P" or family in explicit else q
        assert q != "U" or (no_bare == "U" and clear_only == "U")
        assert q != "P" or (no_bare == "P" and clear_only == "P")
        states.append({k: r[k] for k in ("identity_key","reading_id","label_code","M")} |
                      {"Q":q,"Q_plus_admitted_example_scope":all_example,
                       "Q_plus_examples_excluding_bare_parentheses":no_bare,
                       "Q_plus_explicit_nonexhaustive_cues":clear_only,
                       "reviewed_increment_cue_family":family})
    bykey = {(r["identity_key"],r["label_code"]):r for r in states}
    contrasts=[]
    for subset in ("all_ads","both_mentioned"):
        pp=[p for p in pairs if subset=="all_ads" or p["both_mentioned"]=="1"]
        for rule in ("Q","Q_plus_admitted_example_scope",
                     "Q_plus_examples_excluding_bare_parentheses","Q_plus_explicit_nonexhaustive_cues"):
            counts=Counter()
            for p in pp:
                for side in ("a","b"):
                    v=bykey[p["identity_key"],p["target_"+side]][rule]
                    counts[side,v]+=1
            n=len(pp); ap=counts["a","P"]; bp=counts["b","P"]; au=counts["a","U"]; bu=counts["b","U"]
            contrasts.append({"version":"v4_seven_corrections_relation_set_propagation","subset":subset,"admission_rule":rule,
                "ads":n,"python_P":ap,"python_U":au,"pytorch_P":bp,"pytorch_U":bu,
                "confirmed_gap_pp":100*(ap-bp)/n,
                "lower_pp":100*(ap-bp-bu)/n,"upper_pp":100*(ap+au-bp)/n})
    write(OUT/"admission_rule_states.csv",states)
    production=read(ROOT/"analysis/paired/qualification_scope_contrasts.csv")
    for c in contrasts:
        if c["admission_rule"] not in ("Q","Q_plus_admitted_example_scope"):
            continue
        measure="Q" if c["admission_rule"]=="Q" else "Q_plus_example"
        p=next(r for r in production if r["task"]=="ROBOT_MODEL" and
               r["subset"]==c["subset"] and r["measure"]==measure)
        for ours,theirs in (("python_P","a_P"),("python_U","a_U"),("pytorch_P","b_P"),("pytorch_U","b_U"),
                            ("lower_pp","difference_lo_pp"),("upper_pp","difference_hi_pp")):
            assert abs(float(c[ours])-float(p[theirs]))<1e-10,(c,p)
    write(OUT/"admission_rule_contrasts.csv",contrasts)
    grouped=defaultdict(list)
    for r in increments:
        parent=" | ".join(json.loads(r["parent_texts"]))
        grouped[r["company_id"],norm(parent)].append(r)
    repeated=[]
    for (company,parent),rows in grouped.items():
        if len({r["reading_id"] for r in rows})>1:
            repeated.append({"company_id":company,"normalized_parent_text":parent,
                "n_target_rows":len(rows),"n_ads":len({r["reading_id"] for r in rows}),
                "reading_ids":json.dumps(sorted({r["reading_id"] for r in rows})),
                "label_codes":json.dumps(sorted({r["label_code"] for r in rows}))})
    write(OUT/"repeated_parent_clauses.csv",repeated)
    summary={
        "version":"v4_seven_corrections_relation_set_propagation",
        "interpretation":"Admission-rule alternatives, not truth corrections; baseline Q unchanged. Narrower admission alternatives restore excluded increments to their current Q states.",
        "expanded_scope_definition":"Current production Q_plus_example includes known EXAMPLE qualifications plus UNCONDITIONAL_OR_EXAMPLE relation sets whose two readings both qualify under the expanded construct. The latter are not labelled known EXAMPLE.",
        "explicit_cues_admitted":["such as","e.g.","如"],
        "explicit_cues_not_observed_in_increment_set":["for example","例如","including"],
        "deng_only_is_separate":True,"n_reviewed_increments":44,
        "known_counterexample":"N0798 and N1044 bare parenthetical lists lack explicit example cues; current Q=U but both admitted relation readings enter expanded scope.",
        "classification_changes_made":False,
        "independent_human_validation":False,
        "by_company":dict(Counter(r["company"] for r in increments)),
        "by_cue":dict(Counter(r["cue_family"] for r in increments)),
        "repeated_parent_groups":len(repeated),
        "inputs":[{"path":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in (scope_path,paired_path,note_path,ledger_path)]
    }
    (OUT/"admission_rule_summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(contrasts,ensure_ascii=False,indent=2))
    print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
