from bootstrap import *
def edit(name,old,new):
 p=RUN/'scripts'/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:70]);p.write_text(s.replace(old,new),encoding='utf-8')
edit('s03_build_tables.py','if claim_nature in ("MEDIA_STATEMENT",):','if claim_nature in ("MEDIA_STATEMENT", "MEDIA_REPORT"):')
edit('s13_semantic_checks.py',"  check('B5_SCOPE_REL','同字段多个产品或事件逐行绑定各自证据',not bad,bad)","""  check('B5_SCOPE_REL','同字段多个产品或事件逐行绑定各自证据',not bad,bad)
  media_bad=[]
  for f in facts:
   es=[ev[x] for x in f['time_basis_evidence_ids'].split('|') if x in ev]
   if es and all(e.get('claim_nature') in ['MEDIA_STATEMENT','MEDIA_REPORT'] for e in es) and f['value_status'] in ['SUPPORTED_EXTERNAL','COUNTERPARTY_CONFIRMATION']:media_bad.append(f['fact_id'])
  check('B5_MEDIA','仅有媒体报道支持的事实不升级为外部确认',not media_bad,media_bad)""")
edit('s11_release_gate.py','    "融资证据换成产品页且重建合法哈希",','    "融资证据换成产品页且重建合法哈希",\n    "媒体报道升级成外部确认",')
edit('s06_rebuild_and_fault.py','    # bind the fault report to this run\'s inputs and code, so a stale report cannot',"""    def upgrade_media(d):
        def mutate(rows):
            r = next(r for r in rows if r['fact_id'] == 'F_US_FIGURE__capital_event_figure_series_b')
            assert r['value_status'] == 'MEDIA_STATEMENT'
            r['value_status'] = 'SUPPORTED_EXTERNAL'
        mutate_csv(os.path.join(d, 'company_facts.csv'), mutate)
    probe('媒体报道升级成外部确认', '将仅有媒体来源的Figure B轮事实改为外部确认', upgrade_media)

    # bind the fault report to this run's inputs and code, so a stale report cannot""")
edit('s00_common.py','"s13_semantic_checks.py",','"s13_semantic_checks.py", "s14_reproduce.py",')
for name in ['s04_verify.py','s11_release_gate.py']:
 p=RUN/'scripts'/name;s=p.read_text(encoding='utf-8').replace('B-repair-r2','B-evidence-integrated').replace('stage_b_repair_r2_agent','stage_b_integrated_repair_agent').replace('定向补查完成，待独立验收','返修及证据接入完成，待独立验收');p.write_text(s,encoding='utf-8')
p=RUN/'scripts/s00_pipeline.py';s=p.read_text(encoding='utf-8');a=s.index('STEPS = [');b=s.index('\n]\n',a)+3;s=s[:a]+'''STEPS = [
    "s01_lock_inputs.py", "s02_build_facts.py", "s03_build_tables.py",
    "s05_grouping.py", "s03b_company_profile.py", "s09_search_log.py",
    "s04_verify.py", "s07_cards_and_html.py", "s06_rebuild_and_fault.py",
    "s11_release_gate.py",
]'''+s[b:];p.write_text(s,encoding='utf-8')
print('Media status normalization and reproducible entry finalized')
