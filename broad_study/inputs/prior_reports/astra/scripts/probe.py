from pathlib import Path
import csv,json,collections
R=Path(__file__).resolve().parents[1]; C=R/'inputs/stage_c'; A=C/'inputs/rules_v1/inputs/stage_a'
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
for p in [A/'jobs.csv',A/'primary_roles.csv',A/'technical_concepts.csv',A/'dimension_status.csv',C/'tables/T1_company_sample.csv',C/'tables/T4_activity_lineage.csv',C/'tables/T4_role_structures.csv',C/'tables/T3_company_context.csv',C/'tables/T3_all_item_semantics.csv',R/'inputs/stage_b/company_facts.csv',R/'inputs/stage_b/company_evidence.csv',C/'inputs/rules_v1/company_scene_matrix.csv']:
 rr=rows(p);print('\nFILE',p.name,len(rr));print('FIELDS',list(rr[0]));print('EXAMPLE',str(rr[0])[:3200])
print('\nCOMPANIES');print(json.dumps(rows(C/'tables/T1_company_sample.csv'),ensure_ascii=False,indent=1))
