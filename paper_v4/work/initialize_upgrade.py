"""Record intake state and protect immutable sources; no historical writes."""
from pathlib import Path
import json, hashlib, csv, collections, platform

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT.parent / 'analysis_E_english_v3_0'
REVIEW = ROOT / 'review' / 'supporting'
REVIEW.mkdir(parents=True, exist_ok=True)

def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

manifest=[]
for p in sorted(OLD.rglob('*')):
    if p.is_file():
        manifest.append({'path':p.relative_to(OLD).as_posix(), 'bytes':p.stat().st_size,
                         'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
save(ROOT/'verification'/'v3_protection_baseline.json', manifest)
sources=[]
for i,name in enumerate(['English_Manuscript_IJM.md','Supplementary_Material.md'],1):
    p=OLD/'release'/name
    sources.append({'source_id':f'SRC-{i:02}', 'path':str(p), 'status':'fully_read',
                    'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                    'notes':'Source Markdown read; visual delivery not yet rechecked in this upgrade.'})
stages={k:'pending' for k in ['intake','reconstruction','frontier','audit','counterargument','synthesis','verification','delivery']}
stages.update(intake='passed',reconstruction='in_progress',frontier='in_progress',audit='in_progress')
run={'schema_version':'0.4','review_id':'ijm-upgrade-intake-20260926','paper_title':'Technology Mentions and Direct Qualification Expressions in Embodied AI Recruitment',
     'assessment_date':'2026-09-26','status':'draft','mode':'quick','requested_mode':'quick','delivered_mode':'quick','mode_transition':'none',
     'target':{'venue':'International Journal of Manpower','tier':'standard-field'},'paper_family':'descriptive-measurement',
     'designs':['purposive-cross-section','partial-identification','relational-text-coding'],'requested_addons':['journal_fit'],
     'identity_handling':'identity_minimized','assessment_boundary':{'sources':sources,'figures':'captions_only',
       'equations':'source_preserved','appendix':'fully_read','notes':'Initial contribution/design audit; not an exhaustive final referee report. New analyses run separately from immutable v3 sources.'},
     'capabilities':{'live_literature_search':True,'replication_code':'static_only'},
     'comment_policy':{'minimum_target':0,'maximum':None,'substance_maximum':100,'writing_maximum':30,'exhaustive':False},
     'stage_status':stages,'gates_loaded':[],'counts':{k:0 for k in ['critical','major','minor','info','essential']},'verification_passed':False}
save(REVIEW/'run.json',run)
source_inventory=[]
for source in sources:
    lines=Path(source['path']).read_text(encoding='utf-8').splitlines()
    headings=[(n,s) for n,s in enumerate(lines,1) if s.startswith('#')]
    for j,(start,title) in enumerate(headings):
        end=headings[j+1][0]-1 if j+1<len(headings) else len(lines)
        source_inventory.append({'source_id':source['source_id'],'anchor_id':f"{source['source_id']}-S{j+1:02}",'start_line':start,'end_line':end,'heading':title,'state':'read'})
save(REVIEW/'intake_source_inventory.json',source_inventory)
print(json.dumps({'protected_files':len(manifest),'sources':len(sources),'section_units':len(source_inventory),'python':platform.python_version()}))
