"""Fixed-sample exploratory framework control. Python standard library only."""
from pathlib import Path
from collections import Counter
import csv,json,re,hashlib,itertools
import prepare_sources
EXT=Path(__file__).resolve().parents[1]
ROOT=EXT.parents[1]
OUT=EXT/"outputs"
MEASURES=("M","H","Q","Q_plus_example","Q_plus_choice_example")
TFPAT=prepare_sources.PAT
PTPAT=re.compile(r"(?<![A-Za-z0-9_])pytorch(?![A-Za-z0-9_])",re.I)
def read(path):return prepare_sources.read(path)
def write(path,rows):
    if rows:prepare_sources.write(path,rows)
    else:path.write_text("reading_id,differences_from_inherited_PyTorch\n",encoding="utf-8")
def jsonout(name,data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def narrow(ann):
    if ann["metric"] not in ("GENERAL","REQUIRED"):
        return {"H":0,"Q":"Z","Q_plus_example":"Z","Q_plus_choice_example":"Z"}
    branch=ann["branch"]
    q="P" if branch=="UNCONDITIONAL" else "U" if branch in ("UNRESOLVED","UNCONDITIONAL_OR_EXAMPLE") else "Z"
    return {"H":1,"Q":q,
            "Q_plus_example":"P" if q=="P" or branch in ("EXAMPLE","UNCONDITIONAL_OR_EXAMPLE") else q,
            "Q_plus_choice_example":"P" if q=="P" or branch in ("EXAMPLE","CHOICE","CHOICE_AND_EXAMPLE","UNCONDITIONAL_OR_EXAMPLE") else q}
def inherited(row):
    return {"M":int(row["M"]),"H":int(row["H_qualification_context"]),
            **{k:row[k] for k in MEASURES[2:]}}
def asstate(value):return ("P" if value else "Z") if isinstance(value,int) else value
def aggregate(pairs,version,subset):
    results=[]
    for measure in MEASURES:
        c=Counter()
        for p in pairs:
            c["a",asstate(p["a"][measure])]+=1
            c["b",asstate(p["b"][measure])]+=1
        n=len(pairs);ap=c["a","P"];au=c["a","U"];bp=c["b","P"];bu=c["b","U"]
        results.append({"version":version,"subset":subset,"measure":measure,"ads":n,
            "a_P":ap,"a_U":au,"b_P":bp,"b_U":bu,"confirmed_gap_pp":100*(ap-bp)/n,
            "difference_lo_pp":100*(ap-bp-bu)/n,"difference_hi_pp":100*(ap+au-bp)/n})
    return results
def possibilities(value):
    return (1,) if value=="P" else (0,) if value=="Z" else (0,1)
def main():
    prepare_sources.main()
    source_path=ROOT/"source_snapshot/source_v2/data/inputs/records.json"
    assert hashlib.sha256(source_path.read_bytes()).hexdigest()=="c3bf940e3cf39fabeea2d3ae25684577f8cd6fc1e71450b9a5a60a19ab743acb"
    records=json.loads(source_path.read_text(encoding="utf-8"));by={r["identity_key"]:r for r in records}
    packet=json.loads((OUT/"matched_source_packet.json").read_text(encoding="utf-8"))
    inventory=read(OUT/"literal_inventory_105.csv")
    notes_path=EXT/"data/source_review_annotations.json"
    notes=json.loads(notes_path.read_text(encoding="utf-8"))
    assert len(notes)==26 and set(notes)=={r["reading_id"] for r in packet}
    assert len({r["reading_id"] for r in inventory})==105
    scope=read(ROOT/"analysis/paired/qualification_scope_states.csv")
    smap={(r["identity_key"],r["label_code"]):r for r in scope}
    reviews=[];byreview={};integrity=[]
    for r in packet:
        ann=notes[r["reading_id"]];full=r["fields"]["full_description"]
        assert ann["full_captured_source_model_read"]
        assert any(ann["governing_expression"] in field for field in r["fields"].values())
        tfm=list(TFPAT.finditer(full));ptm=list(PTPAT.finditer(full))
        assert len(tfm)==1,("additional TensorFlow occurrence requires review",r["reading_id"])
        start=full.rfind("\n",0,tfm[0].start())+1
        end=full.find("\n",tfm[0].end());end=len(full) if end<0 else end
        same=all(start<=m.start()<m.end()<=end for m in ptm) and bool(ptm)
        assert same and ann["same_predicate_and_operator_as_pytorch"]
        for occ in r["occurrences"]:
            text=r["fields"][occ["field"]]
            exact=text[occ["start"]:occ["end"]]==occ["surface"]
            parent=text[occ["parent_start"]:occ["parent_end"]]==occ["parent_text"]
            assert exact and parent
            integrity.append({"reading_id":r["reading_id"],"field":occ["field"],
                "start":occ["start"],"end":occ["end"],"target_exact":exact,"parent_exact":parent,
                "field_sha256":hashlib.sha256(text.encode()).hexdigest()})
        new=narrow(ann);old=inherited(r["existing_pytorch_scope"])
        differences=[m for m in MEASURES[1:] if old[m]!=new[m]]
        review={"identity_key":r["identity_key"],"reading_id":r["reading_id"],"company":r["company"],
            "title":r["title"],"source_url":r["source_url"],"source_field":"full_description",
            "source_field_sha256":hashlib.sha256(full.encode()).hexdigest(),
            "parent_start":start,"parent_end":end,"parent_text":full[start:end],
            "TF_full_source_occurrences":len(tfm),"PyTorch_full_source_occurrences":len(ptm),
            "all_pytorch_occurrences_in_same_parent":same,
            "same_predicate_and_operator":True,"separate_TF_qualification_found":False,
            "separate_PyTorch_qualification_found":False,**ann,
            "TF_H":new["H"],"TF_Q":new["Q"],"TF_Q_plus_example":new["Q_plus_example"],
            "TF_Q_plus_choice_example":new["Q_plus_choice_example"],
            "inherited_PyTorch_H":old["H"],"inherited_PyTorch_Q":old["Q"],
            "inherited_PyTorch_Q_plus_example":old["Q_plus_example"],
            "inherited_PyTorch_Q_plus_choice_example":old["Q_plus_choice_example"],
            "harmonized_PyTorch_H":new["H"],"harmonized_PyTorch_Q":new["Q"],
            "harmonized_PyTorch_Q_plus_example":new["Q_plus_example"],
            "harmonized_PyTorch_Q_plus_choice_example":new["Q_plus_choice_example"],
            "differences_from_inherited_PyTorch":json.dumps(differences),
            "historical_target_paths":json.dumps(r["historical_target_paths"],ensure_ascii=False),
            "review_status":"MODEL_FULL_SOURCE_REVIEW_NOT_BLIND"}
        reviews.append(review);byreview[r["identity_key"]]=review
    difference_ids=[r["reading_id"] for r in reviews if json.loads(r["differences_from_inherited_PyTorch"])]
    assert difference_ids==[],("Run after coordinated main-layer bare-parenthesis consistency update.",difference_ids)
    write(OUT/"source_review_26.csv",reviews)
    write(OUT/"source_integrity_checks.csv",integrity)
    write(OUT/"pytorch_harmonization_differences.csv",[r for r in reviews if json.loads(r["differences_from_inherited_PyTorch"])])
    tfledger=[];paired=[];models={"inherited_PyTorch_vs_new_TF":[],"harmonized_framework_control":[]}
    for inv in inventory:
        key=inv["identity_key"];src=by[key];rr=byreview.get(key)
        tf={"M":int(inv["literal_TensorFlow_M"]),**narrow(notes[inv["reading_id"]])} if rr else {"M":0,"H":0,"Q":"Z","Q_plus_example":"Z","Q_plus_choice_example":"Z"}
        oldpt=inherited(smap[key,"SK_PYTORCH"])
        harmpt={"M":oldpt["M"],**narrow(notes[inv["reading_id"]])} if rr else dict(oldpt)
        tfledger.append({"identity_key":key,"reading_id":inv["reading_id"],"company_id":inv["company_id"],
            "title":inv["title"],"source_url":src["source_url"],**tf,
            "classification_basis":"MODEL_FULL_SOURCE_REVIEW" if rr else "ALL_CAPTURED_FIELDS_LITERAL_TARGET_ABSENT",
            "metric":rr["metric"] if rr else "NONE","branch":rr["branch"] if rr else "ABSENT",
            "cue_family":rr["cue_family"] if rr else "NONE",
            "all_fields_checked":inv["all_fields_checked"],"source_review_reading_id":inv["reading_id"] if rr else "",
            "independent_human_validation":False})
        for name,pt in (("inherited_PyTorch_vs_new_TF",oldpt),("harmonized_framework_control",harmpt)):
            models[name].append({"identity_key":key,"reading_id":inv["reading_id"],"a":pt,"b":tf,"both":bool(pt["M"] and tf["M"])})
        flat={"identity_key":key,"reading_id":inv["reading_id"],"both_mentioned":int(bool(oldpt["M"] and tf["M"]))}
        for prefix,state in (("inherited_pytorch",oldpt),("harmonized_pytorch",harmpt),("tensorflow",tf)):
            flat.update({prefix+"_"+m:state[m] for m in MEASURES})
        paired.append(flat)
    write(OUT/"tensorflow_states_105.csv",tfledger)
    write(OUT/"paired_states_105.csv",paired)
    contrasts=[]
    for name,pp in models.items():
        for subset in ("all_ads","both_mentioned"):
            selected=[p for p in pp if subset=="all_ads" or p["both"]]
            assert len(selected)==(105 if subset=="all_ads" else 26)
            contrasts+=aggregate(selected,name,subset)
    write(OUT/"framework_contrasts.csv",contrasts)
    # Additional equality assumption only for individually documented same-predicate U-U sources.
    coupled=[]
    for subset in ("all_ads","both_mentioned"):
        pp=[p for p in models["harmonized_framework_control"] if subset=="all_ads" or p["both"]]
        for measure in MEASURES[2:]:
            lo=hi=0;coupled_ids=[]
            for p in pp:
                av=p["a"][measure];bv=p["b"][measure]
                choices=list(itertools.product(possibilities(av),possibilities(bv)))
                if p["reading_id"] in ("N0149","N0798") and av==bv=="U":
                    assert av==bv=="U"
                    choices=[(0,0),(1,1)];coupled_ids.append(p["reading_id"])
                differences=[a-b for a,b in choices];lo+=min(differences);hi+=max(differences)
            coupled.append({"version":"harmonized_framework_control","subset":subset,"measure":measure,"ads":len(pp),
                "coupled_reading_ids":json.dumps(sorted(coupled_ids)),
                "lower_pp_under_shared_completion":100*lo/len(pp),
                "upper_pp_under_shared_completion":100*hi/len(pp),
                "assumption":"Only N0149 and N0798 U indicators share a binary completion within each named construct; other U assignments remain free."})
    write(OUT/"coupled_reading_diagnostic.csv",coupled)
    summary={"n_ads":105,"n_joint_mentions":26,"n_literal_absent_ads_checked":79,
        "n_reviewed_full_sources":26,"full_source_same_predicate_count":26,
        "separate_target_qualification_occurrences_found":0,
        "tensorflow_Q_states":dict(Counter(r["Q"] for r in tfledger)),
        "tensorflow_H":sum(r["H"] for r in tfledger),
        "tensorflow_example_P":sum(r["Q_plus_example"]=="P" for r in tfledger),
        "tensorflow_choice_example_P":sum(r["Q_plus_choice_example"]=="P" for r in tfledger),
        "reviewed_branch_counts":dict(Counter(r["branch"] for r in reviews)),
        "reviewed_metric_counts":dict(Counter(r["metric"] for r in reviews)),
        "pytorch_harmonization_differences":difference_ids,
        "original_496_state_rows_modified":False,"independent_human_validation":False,
        "inherited_comparison_is_diagnostic_only":True,
        "harmonized_primary_scope":"Both frameworks reviewed in 26 co-mention ads; PyTorch in other 79 remains inherited.",
        "source_occurrence_checks":len(integrity),"all_target_and_parent_span_checks_pass":True,
        "annotation_sha256":hashlib.sha256(notes_path.read_bytes()).hexdigest(),
        "inputs":[{"path":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in (source_path,ROOT/"analysis/paired/qualification_scope_states.csv",
                            ROOT/"data/v4_source_corrections.json",notes_path)]}
    jsonout("summary.json",summary)
    print(json.dumps(summary,indent=2))
    print(json.dumps([r for r in contrasts if r["version"]=="harmonized_framework_control"],indent=2))
if __name__=="__main__":main()

