"""Read-only source inventory for the frozen framework-control extension."""
from pathlib import Path
from collections import Counter
import csv,json,re,hashlib
EXT=Path(__file__).resolve().parents[1]
ROOT=EXT.parents[1]
OUT=EXT/"outputs"
PAT=re.compile(r"(?<![A-Za-z0-9_])tensorflow(?![A-Za-z0-9_])",re.I)
SHORT=re.compile(r"(?<![A-Za-z0-9_])tf(?![A-Za-z0-9_])",re.I)
def read(path):
    with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def write(path,rows):
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def treepaths(node,path=()):
    if isinstance(node,list):
        for n in node:yield from treepaths(n,path)
    elif isinstance(node,dict):
        current={k:node[k] for k in ("id","relation","use","field","start","quote","surface") if k in node}
        here=path+(current,) if current else path
        if PAT.fullmatch(str(node.get("surface",""))) or PAT.fullmatch(str(node.get("quote",""))):
            yield list(here)
        for key in ("expression","children"):
            if key in node:yield from treepaths(node[key],here)
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    paths={"pairs":ROOT/"analysis/paired/paired_advertisements.csv",
           "records":ROOT/"source_snapshot/source_v2/data/inputs/records.json",
           "pytorch_scope":ROOT/"analysis/paired/qualification_scope_states.csv"}
    pairs=[r for r in read(paths["pairs"]) if r["task"]=="ROBOT_MODEL"]
    records=json.loads(paths["records"].read_text(encoding="utf-8"))
    by={r["identity_key"]:r for r in records}
    pyt={(r["identity_key"],r["label_code"]):r for r in read(paths["pytorch_scope"])}
    fields,packet,inventory=[],[],[]
    for p in sorted(pairs,key=lambda p:p["reading_id"]):
        src=by[p["identity_key"]];occ=[];short=[]
        for name,text in src["fields"].items():
            if not isinstance(text,str):continue
            matches=list(PAT.finditer(text));shortmatches=list(SHORT.finditer(text))
            fields.append({"identity_key":src["identity_key"],"reading_id":src["reading_id"],
                "field":name,"characters":len(text),"field_sha256":hashlib.sha256(text.encode()).hexdigest(),
                "literal_tensorflow_count":len(matches),"literal_TF_abbreviation_count":len(shortmatches),
                "all_field_text_scanned":True})
            for m in matches:
                start=text.rfind("\n",0,m.start())+1
                end=text.find("\n",m.end());end=len(text) if end<0 else end
                occ.append({"field":name,"start":m.start(),"end":m.end(),"surface":m.group(),
                            "parent_start":start,"parent_end":end,"parent_text":text[start:end]})
            short.extend({"field":name,"start":m.start(),"end":m.end(),"surface":m.group()} for m in shortmatches)
        py=pyt[src["identity_key"],"SK_PYTORCH"]
        inventory.append({"identity_key":src["identity_key"],"reading_id":src["reading_id"],
            "company_id":src["company_id"],"title":src["title"],"literal_TensorFlow_M":int(bool(occ)),
            "pytorch_M":int(py["M"]),"all_fields_checked":len(src["fields"]),
            "literal_occurrences_across_fields":len(occ),"TF_abbreviation_occurrences":len(short)})
        if occ or short:
            packet.append({"identity_key":src["identity_key"],"reading_id":src["reading_id"],
                "company":src["company"],"title":src["title"],"source_url":src["source_url"],
                "fields":src["fields"],"occurrences":occ,"short_abbreviation_occurrences":short,
                "historical_target_paths":list(treepaths(src.get("historical_requirement_groups",[]))),
                "existing_pytorch_scope":py})
    assert len(inventory)==105 and sum(r["literal_TensorFlow_M"] for r in inventory)==26
    assert sum(r["literal_TensorFlow_M"] and r["pytorch_M"] for r in inventory)==26
    assert not any(r["TF_abbreviation_occurrences"] for r in inventory),"Inspect explicit definitions before proceeding."
    write(OUT/"all_field_literal_checks.csv",fields)
    write(OUT/"literal_inventory_105.csv",inventory)
    (OUT/"matched_source_packet.json").write_text(json.dumps(packet,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    full=[]
    for r in packet:
        full += ["# "+r["reading_id"]+" | "+r["company"]+" | "+r["title"],"",r["fields"]["full_description"],""]
        for name,text in r["fields"].items():
            if name!="full_description" and text and text not in r["fields"]["full_description"]:
                full += ["Additional captured field: "+name,text,""]
    (OUT/"matched_full_sources.md").write_text("\n".join(full),encoding="utf-8")
    manifest={"n_ads":105,"literal_target_hit_ads":26,"literal_cohit_ads":26,"literal_nonhit_ads":79,
              "fields_scanned":len(fields),"nonempty_fields_scanned":sum(r["characters"]>0 for r in fields),
              "TF_abbreviation_occurrences":0,"independent_human_validation":False,
              "inputs":[{"path":str(p.relative_to(ROOT)),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths.values()]}
    (OUT/"source_inventory_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,indent=2))
if __name__=="__main__":main()

