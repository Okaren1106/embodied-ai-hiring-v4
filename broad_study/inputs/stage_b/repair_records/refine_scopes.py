from bootstrap import *
import copy
baseline=read(RUN/'work/evidence_identity_baseline.json');ing=read(RUN/'work/supplement_ingestion.json')
# Restore the parent-background provenance at its own row. The fault test must mutate an existing edge.
p=RUN/'work/pilot_facts_US_AMAZON_FTR.json';d=read(p)
f=next(f for f in d['facts'] if f['field']=='parent_robotics_scale_context');f['evidence_ids']=['B_US_AMAZON_FTR_007']
d['relations'].append({'fact':'parent_robotics_scale_context','evidence':'B_US_AMAZON_FTR_007','role':'CONTEXT_ONLY','review_note':'仅母公司背景，无FAR断言日期资格','fact_seq':1});save(p,d)
p=RUN/'scripts/s06_rebuild_and_fault.py';s=p.read_text(encoding='utf-8');old='''                if r["evidence_id"] == "B_US_AMAZON_FTR_007":
                    r["relation"] = "SUPPORTS"
                    return
        mutate_csv(os.path.join(d, "evidence_links.csv"), fn)''';new=old.replace('        mutate_csv','            raise RuntimeError("Fault injection did not find a parent-context edge")\n        mutate_csv');assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf-8')
# A single press release can contain a historical deployment and a future project.
# Separate evidence assertions to retain one event/publication pair per fact.
p=RUN/'work/research/authored_US_FIGURE.json';d=read(p)
e=copy.deepcopy(next(e for e in d['evidence'] if e['evidence_id']=='IR_FIGURE_02'))
e.update(evidence_id='IR_FIGURE_02_F02',field='deployment_status_actual / evidence_external_pilot / evidence_sustained_use',event_date='2025',event_date_precision='YEAR',date_precision='YEAR',quote='more than 30,000 BMW X3 vehicles over ten months',quote_locator='BMW原文2025年Figure 02回顾段；web记录L105；供应方引语L104',claim='BMW回顾2025年Figure 02在车身车间实际运行，10个月协助超过30000辆X3生产；供应方CEO同稿说11个月。',note='本条事件年2025指F02运行；发布日期仍为2026-06-25。IR_FIGURE_02另支持2026年F03项目计划。同URL的两条证据是不同断言，不是两份独立来源。')
d['evidence'].append(e)
fields=['deployment_status_actual','evidence_external_pilot','evidence_sustained_use']
for f in d['facts']:
 if f['field'] in fields and 'IR_FIGURE_02' in f['evidence_ids']:f['evidence_ids']=['IR_FIGURE_02_F02' if x=='IR_FIGURE_02' else x for x in f['evidence_ids']]
for r in d['relations']:
 if r['fact'] in fields and r['evidence']=='IR_FIGURE_02':r['evidence']='IR_FIGURE_02_F02'
save(p,d);baseline['entries'][e['evidence_id']]={'company_id':'US_FIGURE','url':e['url']}
next(c for c in ing['cards'] if c['review_id']=='IR_FIGURE_02')['related_evidence_ids']=['IR_FIGURE_02_F02']
ing['post_ingestion_refinements']=[{'reason':'同一BMW来源内F02历史运行与F03未来项目的事件日期分别建证据断言','evidence_id':'IR_FIGURE_02_F02','source_count_increment':0},{'reason':'FAR母公司背景来源接回独立背景行；故障实验必须找到并改变真实边','evidence_id':'B_US_AMAZON_FTR_007'}]
save(RUN/'work/supplement_ingestion.json',ing);save(RUN/'work/evidence_identity_baseline.json',baseline)
print('Historical F02 event date and parent background relation corrected')
