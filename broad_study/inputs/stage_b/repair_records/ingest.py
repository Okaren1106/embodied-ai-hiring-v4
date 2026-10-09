from bootstrap import *
import csv,sys,copy,datetime,re
sys.path.insert(0,str(RUN/'scripts'))
from s00_common import date_precision
SOURCES=read(RUN/'work/supplement_sources.json');SNAPS=read(RUN/'work/snapshot_index.json');ING=[];CHANGES=[]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def pathof(cid): return RUN/(f'work/pilot_facts_{cid}.json' if cid in ['CN_XSQUARE','US_AMAZON_FTR','CN_FOURIER'] else f'work/research/authored_{cid}.json')
DOCS={}
for s in SOURCES:
 cid=s['company_id']
 if cid in DOCS: continue
 envelope=read(pathof(cid));d=envelope.get('companies',[envelope])[0]
 if cid in ['US_AMAZON_FTR','CN_FOURIER']:
  # Materialize pre-existing product/region splits once; keep their fact identities.
  layer=read(RUN/f'work/pilot_facts_v2_{cid}.json')
  d['facts']=[f for f in layer['facts'] if f['assertion_kind']!='CAPITAL_EVENT']
  d['relations']=[{'fact':r['field'],'evidence':r['evidence_id'],'role':r['relation'],'review_note':r['review_note'],'fact_seq':next(f['fact_seq'] for f in layer['facts'] if f['fact_id']==r['fact_id'])} for r in layer['relations']]
  d['capital_events']=layer['capital_events'];d['scope_rows_materialized']=True
 DOCS[cid]=d
def fact(cid,field,value,status,eids,reason,*,append=False,kind='OBSERVATION_OR_DISCLOSURE',scope='',period='',labels=None,note='',roles=None):
 d=DOCS[cid];matches=[f for f in d['facts'] if f['field']==field]
 if append or not matches:
  seq=len(matches)+1;f={'field':field};d['facts'].append(f)
 else: seq=1;f=matches[0]
 old=copy.deepcopy(f)
 f.update(value=value,value_status=status,research_status=status if status in ['NOT_YET_SEARCHED','SEARCHED_NOT_FOUND','ACCESS_BLOCKED','NOT_APPLICABLE'] else 'SEARCHED_FOUND',evidence_ids=eids,decision_reason=reason,assertion_kind=kind,product_or_business_scope=scope,event_or_period=period,note=note)
 d['relations']=[r for r in d.get('relations',[]) if not(r['fact']==field and r.get('fact_seq',1)==seq)]
 for eid in eids:d['relations'].append({'fact':field,'fact_seq':seq,'evidence':eid,'role':(roles or {}).get(eid,'SUPPORTS'),'review_note':reason})
 if labels is not None:
  for dim in RULES['dimensions']:
   if dim['dimension']==field or field in {'product_lines_rehab','product_lines_humanoid','product_lines_companion'} and dim['dimension']=='product_lines':
    dim['group_bindings'].setdefault(cid,{})[value]=labels
 CHANGES.append({'company_id':cid,'field':field,'fact_seq':seq,'old':old,'new':copy.deepcopy(f)})
 return f
RULES=read(RUN/'work/grouping_rules_source.json')
RULES['rule_version']='stage-b-integrated-mapping-v1'
# Restore source identity before ingesting any supplements.
fig=DOCS['US_FIGURE'];r2fig=read(R2/'work/research/authored_US_FIGURE.json')
csource=next(e for e in r2fig['evidence'] if e['evidence_id']=='B_US_FIGURE_004')
product=next(e for e in fig['evidence'] if e['evidence_id']=='B_US_FIGURE_004')
assert not any(e['evidence_id']=='B_US_FIGURE_006' for e in fig['evidence'])
product['evidence_id']='B_US_FIGURE_006';fig['evidence'].append(copy.deepcopy(csource))
for f in fig['facts']:
 if f['field'] in ['product_lines','delivery_form','target_markets']:
  f['evidence_ids']=['B_US_FIGURE_006' if e=='B_US_FIGURE_004' else e for e in f.get('evidence_ids',[])]
for r in fig['relations']:
 if r['fact'] in ['product_lines','delivery_form','target_markets'] and r['evidence']=='B_US_FIGURE_004':r['evidence']='B_US_FIGURE_006'
r2snaps=read(R2/'work/snapshot_index.json')['snapshots'];sid=csource['snapshot_id'];SNAPS['snapshots'][sid]=copy.deepcopy(r2snaps[sid])
for key in ['snapshot_raw_path','snapshot_text_path']:
 rel=SNAPS['snapshots'][sid].get(key)
 if rel: shutil.copy2(R2/rel,RUN/rel)
# Existing ID -> same publisher/source. Distinct claim by quoted supplier gets its own evidence row.
reuse={'IR_FIGURE_01':'B_US_FIGURE_004','IR_ASTRIBOT_01':'B_CN_ASTRIBOT_001','IR_BD_01':'B_US_BOSTON_DYNAMICS_003'}
nature={
 'INVESTOR_DISCLOSURE':('REGULATORY_OR_EXCHANGE','REGULATORY_FILING'),
 'PARTICIPATING_PUBLIC_AUTHORITY':('GOVERNMENT_OR_STANDARDS','COUNTERPARTY_STATEMENT'),
 'UNIVERSITY_INTERVIEW':('RESEARCH_INSTITUTION','COMPANY_SELF_REPORT'),
 'COMPANY_BROCHURE':('OFFICIAL_COMPANY','COMPANY_SELF_REPORT'),
 'PUBLIC_AUTHORITY_FEATURE':('GOVERNMENT_OR_STANDARDS','MEDIA_REPORT'),
 'PUBLIC_AUTHORITY_REPORT_REPUBLICATION':('GOVERNMENT_OR_STANDARDS','MEDIA_REPORT'),
 'OFFICIAL_COMPANY':('OFFICIAL_COMPANY','COMPANY_SELF_REPORT'),
 'PRIMARY_RESEARCH':('RESEARCH_INSTITUTION','COMPANY_SELF_REPORT'),
 'OFFICIAL_RESEARCH_REPOSITORY':('OFFICIAL_COMPANY','COMPANY_SELF_REPORT'),
 'COUNTERPARTY_CONFIRMATION':('COUNTERPARTY_CONFIRMATION','COUNTERPARTY_STATEMENT'),
 'COMPANY_PRESS_RELEASE':('OFFICIAL_COMPANY','COMPANY_SELF_REPORT'),
}
def imported_snapshot(s):
 sid=s['id'];web=RUN/f'evidence_snapshots/{sid}.web.json';raw_path='';raw_sha='';record='';recordsha=''
 if web.exists():
  j=read(web);text=j['response'];medium='WEB_TOOL_EXTRACT';record=str(web.relative_to(RUN)).replace('\\','/');recordsha=sha(web);retrieved=j['started_at']
 elif s.get('raw_key'):
  m=read(AUDIT/f"independent_research/{s['raw_key']}.json");src=AUDIT/m['raw_path'];assert sha(src)==m['raw_sha256']
  ext='.pdf' if src.read_bytes().startswith(b'%PDF') else '.html';dest=RUN/f'evidence_snapshots/{sid}{ext}';shutil.copy2(src,dest)
  raw_path=str(dest.relative_to(RUN)).replace('\\','/');raw_sha=sha(dest);text=(AUDIT/m['text_path']).read_text(encoding='utf-8');medium='ORIGINAL_HTTP_BYTES';retrieved=m['retrieved_at']
  if sid=='IR_SPIRITAI_01':text='[VISUAL_TRANSCRIPTION_OF_IMAGE_PDF]\n'+s['quote']+'\n审计已目视第2、3页；本段不是PDF机器提取。原件见同编号PDF。\n'+s['summary'];medium='ORIGINAL_PDF_WITH_VISUAL_TRANSCRIPTION'
  recordpath=RUN/f'evidence_snapshots/{sid}.fetch.json';save(recordpath,m|{'imported_from_audit':str(AUDIT),'imported_at':NOW});record=str(recordpath.relative_to(RUN)).replace('\\','/');recordsha=sha(recordpath)
 else:
  raise ValueError('No capture for '+sid)
 textpath=RUN/f'evidence_snapshots/{sid}.txt';textpath.write_text(text,encoding='utf-8')
 meta={'snapshot_id':sid,'company_id':s['company_id'],'question':s['summary'],'requested_url':s['url'],'effective_url':s['url'],'access_status':'OK','http_code':None if medium=='WEB_TOOL_EXTRACT' else m.get('http_status'),'retrieved_at_utc':retrieved,'snapshot_raw_path':raw_path,'raw_sha256':raw_sha,'snapshot_text_path':str(textpath.relative_to(RUN)).replace('\\','/'),'body_text_sha256':sha(textpath),'capture_medium':medium,'capture_record_path':record,'capture_record_sha256':recordsha,'normalizer':'web-tool-returned-text-v1' if medium=='WEB_TOOL_EXTRACT' else 'audit-extraction-preserved-v1','note':'WEB_TOOL_EXTRACT 的正文/工具记录哈希不代表原网页字节；原始 HTTP 字节未取得。' if medium=='WEB_TOOL_EXTRACT' else '原件从上轮独立补查归档复制并复核哈希。'}
 SNAPS['snapshots'][sid]=meta;return sid,meta
for s in SOURCES:
 cid=s['company_id'];d=DOCS[cid];eid=reuse.get(s['id'],s['id'])
 if s['id'] in ['IR_FIGURE_01','IR_BD_01','IR_AGILITY_01']:
  oldid=reuse.get(s['id'],'B_US_AGILITY_005');old=next(e for e in d['evidence'] if e['evidence_id']==oldid);sid=old['snapshot_id'];meta=SNAPS['snapshots'][sid]
 else: sid,meta=imported_snapshot(s)
 if s['id'] in reuse:
  e=next(e for e in d['evidence'] if e['evidence_id']==eid)
  if s['id']=='IR_ASTRIBOT_01':
   e.update(publication_date='2026-06-03',snapshot_id=sid,quote_locator='证券时报原文标题下来源/作者/日期行：2026-06-03 12:06；正文首段6月3日',note='已核到明确发布日期2026-06-03；撤销此前“无日期”注释。媒体陈述，非付款凭证。')
 else:
  sn,cn=nature.get(s['source_nature'],('MEDIA','MEDIA_REPORT'))
  if s['id']=='IR_AGILITY_01':sn='COUNTERPARTY_CONFIRMATION';cn='COMPANY_SELF_REPORT'
  e={'evidence_id':eid,'record_kind':'STAGE_B_NEW','field':'见逐条事实—证据关系','claim':s['summary'],'quote':s['quote'],'quote_locator':s['locator'],'source_title':s['title'],'publisher':s['publisher'],'source_nature':sn,'url':s['url'],'publication_date':s['publication_date'],'event_date':s['event_date'],'event_date_precision':date_precision(s['event_date']),'date_precision':date_precision(s['event_date'] or s['publication_date']),'retrieved_at':meta.get('retrieved_at_utc',''),'claim_nature':cn,'access_status':'OK','snapshot_id':sid,'linked_inherited_evidence':[],'relation_to_inherited':'INDEPENDENT_SUPPLEMENT','note':s.get('publication_date_note','')+' '+s.get('event_date_note','')+' '+s['summary']+' '+meta.get('note','')}
  if s['id']=='IR_FAR_03':e['publication_date']='';e['note']+=' README中11月5日是研究发布、12月2日是代码开源；当前页面无发布日期，不拿研究发布日期代替代码公开日。'
  d['evidence'].append(e)
 ING.append({'review_id':s['id'],'company_id':cid,'evidence_id':eid,'operation':'REVIEW_EXISTING_AND_REBIND' if s['id'] in reuse else 'NEW_EVIDENCE','snapshot_id':sid,'capture_medium':meta.get('capture_medium','ORIGINAL_HTTP_BYTES'),'raw_http_bytes_present':bool(meta.get('snapshot_raw_path')),'limitation':s['summary']})
 # This is an actual page re-review/import, never a fabricated search query.
 with (RUN/'search_log.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps({'ts_utc':NOW,'action':'PAGE_REVIEW','company_id':cid,'evidence_id':eid,'url':s['url'],'question':s['summary'],'snapshot_id':sid,'capture_medium':meta.get('capture_medium','ORIGINAL_HTTP_BYTES'),'imported_from_review_card':s['id']},ensure_ascii=False)+'\n')

# Scope-bounded facts; existing unknown/background rows are replaced only for the exact proposition investigated.
fact('CN_NOETIX','product_lines','人形机器人本体与仿生人脸产品；BUMI 人形机器人已用于学校捐赠','COUNTERPARTY_CONFIRMATION',['IR_NOETIX_01','IR_NOETIX_02'],'投资方披露支持产品大类；捐赠组织方确认 BUMI 型号。',scope='松延整公司产品；BUMI单独交付',labels=['HUMANOID','BIONIC_FACE'])
fact('CN_NOETIX','product_lines','E1、N2、Hobbs 产品介绍（清华校友采访中的公司陈述）','COMPANY_SELF_REPORT',['IR_NOETIX_03'],'受访者产品介绍，不将订单和租赁回本说法当成交验收。',append=True,scope='E1/N2/Hobbs',labels=['HUMANOID','BIONIC_FACE'])
fact('CN_NOETIX','delivery_form','机器人硬件制造与销售业务（投资方披露，未给某笔销售合同）','COUNTERPARTY_CONFIRMATION',['IR_NOETIX_01'],'投资方明确制造与销售业务；不证明收入金额或具体订单。',labels=['HARDWARE_PRODUCT'])
fact('CN_NOETIX','delivery_form','向琉璃庙镇中心小学无偿捐赠交付两台 BUMI','COUNTERPARTY_CONFIRMATION',['IR_NOETIX_02'],'捐赠，不是销售或付费客户。',append=True,kind='DONATION',scope='BUMI / 琉璃庙镇中心小学',period='2026-06-30',labels=['DONATION'])
fact('CN_NOETIX','target_markets','中小学教育与 AI 教学（具名学校 BUMI 捐赠场景）','COUNTERPARTY_CONFIRMATION',['IR_NOETIX_02'],'教育场景有具名接收方；不外推市场规模。',scope='BUMI',labels=['EDUCATION'])
for field in ['deployment_status_actual','evidence_customer_delivery']:
 fact('CN_NOETIX',field,'2026-06-30 无偿交付两台 BUMI 至北京市怀柔区琉璃庙镇中心小学；未取得后续持续运行资料','COUNTERPARTY_CONFIRMATION',['IR_NOETIX_02'],'活动组织方确认交付；接收方不是由此确立的付费客户。',kind='DONATION',scope='BUMI / 琉璃庙镇中心小学',period='2026-06-30',labels=['DONATION_DELIVERY'] if field=='evidence_customer_delivery' else None)
fact('CN_NOETIX','evidence_paid','','SEARCHED_NOT_FOUND',[],'本次证据仅确立捐赠与销售业务介绍，未取得对应付款确认；未知不等于未付费。')
fact('CN_NOETIX','legal_entity_name','2025-09-02 投资公告记为松延动力（北京）科技有限公司；与当前官网股份公司名称分期保留','COUNTERPARTY_CONFIRMATION',['IR_NOETIX_01'],'只说明公告当时所称法律实体，不推断后续改制日期。',append=True,scope='投资公告历史主体',period='2025-09-02')

fact('CN_SPIRITAI','product_lines','Moz1 人形机器人、Moz2 商服机器人、Spirit v1.6 具身基座模型','MEDIA_STATEMENT',['IR_SPIRITAI_02'],'带日期的机构报道支持观察日前产品与模型存在；部署绩效不升级为客户确认。',scope='Moz1/Moz2/Spirit v1.6',labels=['HUMANOID','FOUNDATION_MODEL'])
fact('CN_SPIRITAI','product_lines','Moz1 首次发布日期有月份冲突：宣传册写2025年5月，官方 news/11 写2025年6月','CONFLICT',['IR_SPIRITAI_01','B_CN_SPIRITAI_002'],'保留两处公司材料冲突，不取其中一月；宣传册上传路径不是发布日期。',append=True,kind='DATE_CONFLICT',scope='Moz1 首发日期')
fact('CN_SPIRITAI','target_markets','工业制造、零售门店，以及 Moz2 面向的商超、酒旅和办公楼宇','MEDIA_STATEMENT',['IR_SPIRITAI_02'],'目标方向与实际使用分开；家庭仍是长期目标。',scope='Moz1/Moz2',labels=['INDUSTRIAL_MANUFACTURING','RETAIL','HOSPITALITY','OFFICE_SERVICES'])
fact('CN_SPIRITAI','target_markets','家庭服务为长期目标，现阶段不宣称大规模 C 端普及','COMPANY_SELF_REPORT',['IR_SPIRITAI_02'],'保留负责人引述的长期目标，不纳入现有商业场景组。',append=True,kind='LONG_TERM_GOAL',scope='家庭',labels=['HOME_LONG_TERM_GOAL'])
fact('CN_SPIRITAI','evidence_demo','2026年6月中关村现场 Moz1 自主收纳演示','MEDIA_STATEMENT',['IR_SPIRITAI_03'],'机构报道的演示，不证明客户交付。',kind='DEMONSTRATION',scope='Moz1 / 中关村展厅',period='2026-06')
# Delivery mode requires a separate commercial-mode source: do not infer one from demonstrations.

fact('US_AMAZON_FTR','product_lines','TWIST2 人形遥操作与全身数据采集研究系统（FAR参与；实验本体是 Unitree G1）','COMPANY_SELF_REPORT',['IR_FAR_02'],'固定v1论文明确作者机构及FAR实习；研究产物不代表FAR自产人形机器人。',kind='RESEARCH_OUTPUT',scope='TWIST2 / FAR参与研究',period='2025-11',labels=['RESEARCH_SYSTEM'])
fact('US_AMAZON_FTR','delivery_form','TWIST2 研究代码公开：README记2025-12-02开源；不据此判断对外产品销售模式','COMPANY_SELF_REPORT',['IR_FAR_03'],'研究发布与代码开源日期分开；当前README无页面发布日期。',kind='RESEARCH_OUTPUT',scope='TWIST2 开源代码',period='2025-12-02',labels=['RESEARCH_CODE_RELEASE'])
fact('US_AMAZON_FTR','target_markets','现行团队页自述面向 Amazon 内部运营的基础模型与机器人研究','COMPANY_SELF_REPORT',['IR_FAR_01'],'现行页面无日期，不回填观察日组织与业务结构；并列导航不代表正式汇报关系。',scope='FAR；当前团队页',labels=['INTERNAL_OPERATIONS_RESEARCH'])
fact('US_AMAZON_FTR','evidence_demo','TWIST2 固定v1报告人形遥操作、数据采集与策略实验；使用 Unitree G1','COMPANY_SELF_REPORT',['IR_FAR_02'],'科研实验，不是客户交付、FAR本体产品或母公司部署量。',kind='RESEARCH_OUTPUT',scope='TWIST2',period='2025-11')
for field in ['evidence_paid','evidence_sustained_use']:
 fact('US_AMAZON_FTR',field,'','SEARCHED_NOT_FOUND',[],'本次团队页、论文与代码材料不提供对外付费/持续使用确认，撤销从内部团队身份推定不适用；保留未知。')
fact('US_AMAZON_FTR','boundary_far_vs_ftr','当前可达路径为 amazon.jobs/content/en/teams/ftr，列出 AFT、Amazon Robotics 与 FAR；旧路径404仅是访问记录','COMPANY_SELF_REPORT',['IR_FAR_01'],'记录可达入口；无发布日期，不能据页面导航断言历史正式汇报关系。',kind='BOUNDARY_NOTE',scope='FAR/FTR现行入口')

fact('US_FIGURE','deployment_status_actual','BMW确认2025年 Figure 02 在 Spartanburg 车身车间运行，协助超过30000辆 X3 生产，正文记10个月','COUNTERPARTY_CONFIRMATION',['IR_FIGURE_02'],'F02客户确认；同稿Figure CEO引语记11个月，两处口径保留，不套给F03。',kind='CUSTOMER_CONFIRMED_USE',scope='Figure 02 / BMW Spartanburg',period='2025（2026-06-25回顾）',note='BMW正文10个月；供应方CEO引语11个月。')
fact('US_FIGURE','deployment_status_actual','Figure 2026-06-30 自述 Figure 03 已到达 BMW Spartanburg Hall 52','COMPANY_SELF_REPORT',['B_US_FIGURE_005'],'保持公司到场自述；BMW6月25日公告是后续项目，不能确认6月30日已完成。',append=True,kind='ARRIVAL_SELF_REPORT',scope='Figure 03 / BMW Hall 52',period='2026-06-30')
fact('US_FIGURE','evidence_loi_intent','BMW于2026-06-25宣布 Figure 03 后续物流排序项目，将开始部署','COUNTERPARTY_CONFIRMATION',['IR_FIGURE_02'],'未来式项目公告按计划记录。',kind='PLAN',scope='Figure 03 / BMW物流排序',period='2026-06-25')
fact('US_FIGURE','evidence_external_pilot','BMW确认 Figure 02 已完成车身车间试点','COUNTERPARTY_CONFIRMATION',['IR_FIGURE_02'],'客户确认F02；不把F03项目计划算成已完成试点。',kind='CUSTOMER_CONFIRMED_USE',scope='Figure 02 / BMW',period='2025')
fact('US_FIGURE','evidence_sustained_use','BMW正文记 Figure 02 于2025年运行10个月；同稿供应方CEO说11个月','COUNTERPARTY_CONFIRMATION',['IR_FIGURE_02'],'只采用BMW正文作为客户口径，同时显式保留供应方引语差异。',scope='Figure 02 / BMW',period='2025')
fact('US_FIGURE','named_customers_or_partners','BMW：Figure 02 已完成试点；Figure 03 另有后续项目公告','COUNTERPARTY_CONFIRMATION',['IR_FIGURE_02'],'具名交易对方；两个产品进度分开。',scope='F02/F03分别')

fact('CN_FOURIER','product_lines_companion','CES 2026展示 GR-3 Care-bot，并展示仍在开发的小型陪伴概念机','COMPANY_SELF_REPORT',['IR_FOURIER_01'],'公司经PRNewswire发布；概念机尚在开发，不倒填后续GR Nano型号。',kind='PRODUCT_DEMONSTRATION',scope='GR-3 / 未命名小型概念机',period='2026-01',labels=['HUMANOID','COMPANION_CONCEPT'])
fact('CN_FOURIER','product_lines_companion','WAIC 2026：GRW轮式双臂机器人发布，GR Mini与GR Nano陪伴系列展示','MEDIA_STATEMENT',['IR_FOURIER_02'],'投资界完整正文；媒体性质，不升级为官方交付或家庭客户事实。',append=True,kind='PRODUCT_RELEASE',scope='GRW / GR Mini / GR Nano',period='2026-07-17',labels=['WHEELED_DUAL_ARM','COMPANION_ROBOT'])
fact('CN_FOURIER','target_markets','GR-3/陪伴系列面向照护、交互陪伴；GRW面向仓储物流、制造与康养重载辅助','MEDIA_STATEMENT',['IR_FOURIER_02'],'产品目标场景，展台家庭Demo不是家庭交付。',append=True,scope='GR-3/GRW/陪伴系列',period='2026-07-17',labels=['HEALTHCARE_REHABILITATION','WAREHOUSE_LOGISTICS','INDUSTRIAL_MANUFACTURING','COMPANIONSHIP'])
fact('CN_FOURIER','evidence_demo','公司稿记CES 2026 GR-3互动演示与小型陪伴概念机展示','COMPANY_SELF_REPORT',['IR_FOURIER_01'],'只记公司演示陈述，不记外部验收。',append=True,kind='DEMONSTRATION',scope='GR-3 / 小型概念机',period='2026-01')
fact('CN_FOURIER','evidence_demo','WAIC 2026展台居家Demo、GRW发布与GR Mini/GR Nano展示','MEDIA_STATEMENT',['IR_FOURIER_02'],'完整媒体正文支持演示，未取得家庭交付证据。',append=True,kind='DEMONSTRATION',scope='WAIC 2026',period='2026-07-17')

fact('US_AGILITY','evidence_paid','GXO 2024-06-27公告引用Agility CEO称 Digit 已为公司产生收入；金额未知','COMPANY_SELF_REPORT',['IR_AGILITY_01'],'说话者是供应方CEO；位于客户网站仍是供应方收入自述。此日期不支持2026年新合同金额和运行小时数。',scope='Digit / GXO-SPANX案例',period='2024-06-27',labels=['REVENUE_SELF_REPORT'])

bd='US_BOSTON_DYNAMICS';bid='B_US_BOSTON_DYNAMICS_003'
oldbd=next(f for f in DOCS[bd]['facts'] if f['field']=='deployment_status_actual').copy()
fact(bd,'deployment_status_actual','DHL称Stretch自2023年在北美投入商业使用，随后扩展至英国和欧洲','COUNTERPARTY_CONFIRMATION',[bid],'既有Stretch使用；另外1000台为MOU，Atlas交付是计划。',kind='CUSTOMER_CONFIRMED_USE',scope='Stretch / DHL',period='2023起（2025-05-13公告）')
fact(bd,'evidence_loi_intent',oldbd['value'],'MEDIA_STATEMENT',oldbd['evidence_ids'],'Atlas生产/预订与未来交付计划单列；不写入实际部署。',append=True,kind='PLAN',scope='Atlas / 现代与Google',period='2026计划')
fact(bd,'evidence_customer_delivery','DHL确认Stretch自2023年起投入商业使用，后扩展到英国和欧洲；未给本条已交付台数','COUNTERPARTY_CONFIRMATION',[bid],'产品限定Stretch；不把1000台意向算为交付。',kind='CUSTOMER_CONFIRMED_USE',scope='Stretch / DHL',period='2023起',labels=['CUSTOMER_CONFIRMED_USE'])
fact(bd,'evidence_sustained_use','DHL公告回顾Stretch从2023年北美使用到英国和欧洲扩展','COUNTERPARTY_CONFIRMATION',[bid],'具名客户持续采用，不推断每一台连续运行时长。',scope='Stretch / DHL',period='2023至2025公告')

for cid,d in DOCS.items():
 # Remove exact duplicate relations; differing evidence scopes remain distinct.
 unique={}
 for r in d.get('relations',[]):unique[(r['fact'],r.get('fact_seq',1),r['evidence'])]=r
 d['relations']=list(unique.values());save(pathof(cid),d)
save(RUN/'work/snapshot_index.json',SNAPS);save(RUN/'work/grouping_rules_source.json',RULES)
save(RUN/'work/supplement_ingestion.json',{'created_at':NOW,'n_review_cards':len(ING),'cards':ING,'claim_changes':CHANGES,'note':'原候选未改；WEB_TOOL_EXTRACT独立标注，不冒充HTTP原件。'})
before=read(RUN/'repair_records/protected_before.json');before.update(read(AUDIT/'protected_before.json'));save(RUN/'repair_records/protected_before.json',before)
# Baseline is from the prior accepted source identities, plus new IDs. Only Figure004 is restored, never replaced.
identity={}
for p in (RUN/'work/research').glob('authored_*.json'):
 for e in read(p).get('evidence',[]):identity[e['evidence_id']]={'company_id':read(p)['company_id'],'url':e['url']}
for cid in ['CN_XSQUARE','CN_FOURIER','US_AMAZON_FTR']:
 d=read(pathof(cid));d=d.get('companies',[d])[0]
 for e in d['evidence']:identity[e['evidence_id']]={'company_id':cid,'url':e['url']}
save(RUN/'work/evidence_identity_baseline.json',{'source':'r2 accepted identities; targeted new identities; Figure004 restored to r2; new supplement IDs','entries':identity})
save(RUN/'work/capital_claim_bindings.json',{'bindings':[{'capital_event_id':'C_US_FIGURE__capital_event_figure_series_c','evidence_id':'B_US_FIGURE_004','source_url':csource['url'],'snapshot_id':csource['snapshot_id'],'locator':'官方标题日期行及第一段','publication_date':'2025-09-16','event_date':'2025-09-16','amount_scope':'COMMITTED_CAPITAL','required_source_fragments':['September 16, 2025','committed capital','Series C','39 billion'],'note':'日期、轮次、承诺资本和估值必须在同一直接来源中成立；其他多事件公告不强制全等主事件日期。'}]})
print(json.dumps({'review_cards':len(ING),'new_evidence':sum(x['operation']=='NEW_EVIDENCE' for x in ING),'fact_changes':len(CHANGES),'source_identities':len(identity),'protected':len(before)},ensure_ascii=False))
