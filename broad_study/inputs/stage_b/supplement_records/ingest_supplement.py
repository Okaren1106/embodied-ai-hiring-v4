from bootstrap import *
import copy,datetime,csv,re
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
NEW=BASE/('stage_b_supplemented/run_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
assert not NEW.exists()
shutil.copytree(RUN,NEW,ignore=shutil.ignore_patterns('__pycache__'))
save(SCRATCH/'new_run.json',{'run':str(NEW),'created_at':NOW})
NR=NEW/'supplement_records';NR.mkdir()
save(NR/'protected_before.json',json.loads((AUDIT/'protected_before.json').read_text(encoding='utf-8')))
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
snaps=read(NEW/'work/snapshot_index.json');rules=read(NEW/'work/grouping_rules_source.json');identity=read(NEW/'work/evidence_identity_baseline.json')
DOCS={};DELTAS=[];ADDED=[]
def pathof(cid):return NEW/(f'work/pilot_facts_{cid}.json' if cid in ['CN_FOURIER','CN_XSQUARE','US_AMAZON_FTR'] else f'work/research/authored_{cid}.json')
def doc(cid):
 if cid not in DOCS:
  d=read(pathof(cid));DOCS[cid]=d.get('companies',[d])[0]
 return DOCS[cid]
def evidence(eid,cid,title,publisher,pub,event,quote,locator,claim,source='OFFICIAL_COMPANY',nature='COMPANY_SELF_REPORT',note=''):
 src=SCRATCH/'new_sources';web=read(src/(eid+'.web.json'));fetch=read(src/(eid+'.fetch.json'))
 raw=src/(eid+'.html');rp='';rh='';medium='WEB_TOOL_EXTRACT'
 if fetch['http_code']==200 and fetch['exit_code']==0 and raw.is_file():
  medium='ORIGINAL_HTTP_BYTES';dest=NEW/'evidence_snapshots'/raw.name;shutil.copy2(raw,dest);rp='evidence_snapshots/'+raw.name;rh=sha(dest)
  body=(src/(eid+'.raw.txt')).read_text(encoding='utf-8')
  record=fetch|{'capture_medium':medium,'normalizer':'stdlib-html-parser-skip-script-style-v1'}
  recordname=eid+'.fetch.json';retrieved=fetch['started_at']
 else:
  body=web['response'];record=web;recordname=eid+'.web.json';retrieved=web['retrieved_at']
  assert 'Failed to fetch' not in body and 'Internal Error' not in body
  note+=' 原HTTP字节本次未取得；保存实际web工具返回。'
 recordpath=NEW/'evidence_snapshots'/recordname;save(recordpath,record)
 textpath=NEW/'evidence_snapshots'/(eid+'.txt');textpath.write_text(body,encoding='utf-8')
 norm=lambda s:re.sub(r'\s+','',s).casefold()
 assert norm(quote) in norm(body),(eid,'quote absent')
 for suff in ['.web.json','.fetch.json']:
  shutil.copy2(src/(eid+suff),NR/(eid+suff))
 snap={'snapshot_id':eid,'company_id':cid,'question':claim,'requested_url':web['url'],'effective_url':fetch.get('effective_url') or web['url'],'access_status':'OK','http_code':200 if rp else None,'retrieved_at_utc':retrieved,'snapshot_raw_path':rp,'raw_sha256':rh,'snapshot_text_path':'evidence_snapshots/'+textpath.name,'body_text_sha256':sha(textpath),'capture_medium':medium,'capture_record_path':'evidence_snapshots/'+recordname,'capture_record_sha256':sha(recordpath),'normalizer':'stdlib-html-parser-skip-script-style-v1' if rp else 'web-tool-returned-text-v1','note':note}
 snaps['snapshots'][eid]=snap
 e={'evidence_id':eid,'record_kind':'STAGE_B_NEW','field':'见逐条事实关系','claim':claim,'quote':quote,'quote_locator':locator,'source_title':title,'publisher':publisher,'source_nature':source,'url':web['url'],'publication_date':pub,'event_date':event,'event_date_precision':{0:'UNKNOWN',4:'YEAR',7:'MONTH',10:'DAY'}.get(len(event),'UNKNOWN'),'date_precision':{0:'UNKNOWN',4:'YEAR',7:'MONTH',10:'DAY'}.get(len(event or pub),'UNKNOWN'),'retrieved_at':retrieved,'claim_nature':nature,'access_status':'OK','snapshot_id':eid,'linked_inherited_evidence':[],'relation_to_inherited':'INDEPENDENT_SUPPLEMENT','note':note}
 doc(cid)['evidence'].append(e);identity['entries'][eid]={'company_id':cid,'url':web['url']};ADDED.append({'evidence_id':eid,'company_id':cid,'url':web['url'],'capture_medium':medium,'publication_date':pub})
 return eid
def fact(cid,field,value,eids,status='COMPANY_SELF_REPORT',*,append=False,kind='OBSERVATION_OR_DISCLOSURE',scope='',period='',labels=None,note='',roles=None):
 d=doc(cid);matches=[f for f in d['facts'] if f['field']==field]
 if append or not matches:seq=len(matches)+1;f={'field':field};d['facts'].append(f)
 else:seq=1;f=matches[0]
 old=copy.deepcopy(f)
 f.update(value=value,value_status=status,research_status='SEARCHED_FOUND',evidence_ids=eids,decision_reason=note,assertion_kind=kind,product_or_business_scope=scope,event_or_period=period,note=note)
 d['relations']=[r for r in d['relations'] if not(r['fact']==field and r.get('fact_seq',1)==seq)]
 for eid in eids:d['relations'].append({'fact':field,'fact_seq':seq,'evidence':eid,'role':(roles or {}).get(eid,'SUPPORTS'),'review_note':note})
 if labels is not None:
  for dim in rules['dimensions']:
   if dim['dimension']==field:dim['group_bindings'].setdefault(cid,{})[value]=labels
 DELTAS.append({'company_id':cid,'field':field,'fact_seq':seq,'old':old,'new':copy.deepcopy(f)})

evidence('NEW_AGIBOT_01','CN_AGIBOT','智元第10000台通用具身机器人正式下线','智元','2026-03-31','',
 '收到越来越多来自汽车制造、3C电子、物流仓储等行业的刚需采购订单','正文02节、龙旗与均胜应用段及标题日期',
 '智元带日期公告介绍采购订单与G2产线应用。10000台是下线产量，不是累计交付；龙旗和均胜情况属于公司公告，未经本轮直接回访客户确认。')
fact('CN_AGIBOT','delivery_form','按采购订单提供具身机器人整机及产线应用；公司公告列龙旗、均胜的G2应用',['NEW_AGIBOT_01'],append=True,scope='G2 / 制造业产线',labels=['HARDWARE_SALES','SYSTEM_INTEGRATION'],note='采购与产线应用支持提供形态；10000台下线不能换成10000台已交付。')
fact('CN_AGIBOT','target_markets','汽车制造、3C电子与物流仓储；具体列举龙旗平板产线和均胜汽车零部件装配',['NEW_AGIBOT_01'],append=True,scope='G2及公告覆盖业务',labels=['AUTOMOTIVE_MANUFACTURING','ELECTRONICS_MANUFACTURING','WAREHOUSE_LOGISTICS'],note='带日期公司自述；目标场景与客户确认层级分开。')
fact('CN_AGIBOT','deployment_status_actual','公司2026-03-31公告称G2已在龙旗平板产线投产并线，并用于均胜汽车零部件装配',['NEW_AGIBOT_01'],append=True,scope='G2 / 龙旗、均胜',note='只确立供应方应用自述，未取得付款与独立客户验收。')

evidence('NEW_DEEP_01','CN_DEEPROBOTICS','X30 robot dog pioneers smart inspection in Singapore power cable tunnel','DEEP Robotics','2025-03-04','',
 'SPock, adapted from the X30 model','日期行；Transforming power cable inspection及Overcoming localization challenges',
 '云深处称X30改装为SPock，在SP Group电缆隧道试点巡检，并调整传感器、软件和导航以适配当地环境；拓展规模为后续计划。')
evidence('NEW_DEEP_02','CN_DEEPROBOTICS','How this technical officer and robot SPock hunt hazards to protect Singapore power tunnels','SP Group','2024-11-27','',
 'trained robotic dog SPock to conduct independent tunnel inspections','正文SPock段与页末27 Nov 2024',
 'SP Group确认SPock隧道巡检项目及设备功能，本文未写X30或厂商名；供应方身份必须另据云深处来源，不能将整条身份链升级为客户确认。',source='COUNTERPARTY_CONFIRMATION',nature='COUNTERPARTY_STATEMENT')
fact('CN_DEEPROBOTICS','delivery_form','X30机器人本体配合面向新加坡电缆隧道的传感器、软件及导航定制，用于SP Group巡检试点',['NEW_DEEP_01'],append=True,scope='X30 / SPock / 新加坡隧道',labels=['HARDWARE_PRODUCT','SYSTEM_INTEGRATION'],note='公司自述的本体与定制解决方案；不推断销售金额、合同形式或扩大试点已完成。')
fact('CN_DEEPROBOTICS','deployment_status_actual','云深处称X30改装的SPock已在SP Group地下电缆隧道巡检试点运行',['NEW_DEEP_01'],append=True,scope='X30 / SPock',note='型号和供应商身份来自供应方自述；客户SPock项目另行记录。')
fact('CN_DEEPROBOTICS','evidence_external_pilot','SP Group确认SPock自主隧道巡检项目；本篇未标厂商或型号',['NEW_DEEP_02','NEW_DEEP_01'],status='COUNTERPARTY_CONFIRMATION',append=True,scope='SPock项目；厂商归属另据供应方',roles={'NEW_DEEP_01':'CONTEXT_ONLY'},note='客户确认限SPock巡检命题；将其关联X30依据供应方说明，不虚构客户直接确认X30型号。')

evidence('NEW_LIMX_01','CN_LIMX','新品上市：逐际动力发售多形态双足机器人TRON 1','逐际动力','2024-10-16','2024-10-16',
 '预订正式开启','标题日期及开头、科研用户与预购段',
 'TRON 1于2024-10-16公开发售/开放预订，是软硬件科研平台；支持算法验证、学术研究和教学培训，不证明预购已经履约交付。')
fact('CN_LIMX','delivery_form','TRON 1以机器人硬件科研平台对外发售并接受预订，提供SDK和底层硬件接口',['NEW_LIMX_01'],append=True,kind='COMMERCIAL_OFFER',scope='TRON 1',period='2024-10-16发售/预订',labels=['HARDWARE_SALES','DEVELOPER_PLATFORM'],note='支持硬件销售提供形态；早鸟预订不计实际交付，不回填其他型号。')
fact('CN_LIMX','target_markets','TRON 1面向运动控制、具身智能算法研究、验证和教学培训',['NEW_LIMX_01'],append=True,scope='TRON 1',labels=['RESEARCH_EDUCATION'],note='公司发售公告明确目标用户；属于出售的科研平台，不是将研究论文当商业商品。')

evidence('NEW_SPIRIT_01','CN_SPIRITAI','宁德时代落地人形机器人动力电池PACK生产线','财联社/科创板日报','2025-12-17','',
 '“小墨”由宁德时代生态企业千寻智能机器人公司研发','2025年12月17日22:25:17及电报正文',
 '记者报道千寻研发的小墨在宁德时代中州PACK产线已投入运行；缺少直接客户原件，保留媒体陈述，不核定首次运行精确日期。',source='MEDIA',nature='MEDIA_REPORT')
fact('CN_SPIRITAI','delivery_form','实体机器人“小墨”投入宁德时代中州电池PACK生产线承担接插件插接作业',['NEW_SPIRIT_01'],status='MEDIA_STATEMENT',append=True,scope='小墨 / 宁德时代中州PACK产线',labels=['HARDWARE_DEPLOYMENT'],note='报道支持实体本体产线提供/应用形态；未给交易模式，不标硬件销售、租赁或RaaS。')
fact('CN_SPIRITAI','deployment_status_actual','2025-12-17报道千寻研发的小墨已在宁德时代中州电池PACK产线运行',['NEW_SPIRIT_01'],status='MEDIA_STATEMENT',append=True,scope='小墨 / 宁德时代中州',note='报道日为确定时间；投运实际日未给，事件日留空，不把报道日当投运日。')

evidence('NEW_GALAXEA_01','CN_GALAXEA','星海图R1产品页','星海图','','',
 'R1全面高效，科研利器','产品型号对比：R1、R1 Lite',
 '现行产品页将R1定位为科研平台，R1 Lite定位数据采集；无发布日期，不推定观察时点已公开。')
fact('CN_GALAXEA','target_markets','R1面向科研开发，R1 Lite面向机器人数据采集（现行产品定位）',['NEW_GALAXEA_01'],scope='R1 / R1 Lite；现行页面',labels=['RESEARCH_EDUCATION','ROBOT_DATA_COLLECTION'],note='找到明确定位；无发布日期，仅背景展示，不将页脚年份或下载日当发布日。')

evidence('NEW_UNITREE_01','CN_UNITREE','TWIST2固定v1论文：实验本体为Unitree G1','TWIST2作者/研究机构','2025-11','2025-11',
 'We use Unitree G1 with 29 DoF','固定v1，III-B Humanoid Robot with Active Vision',
 '研究使用方明确实际采用Unitree G1进行人形遥操作、数据采集与策略实验；支持科研应用场景，不证明对外付费、销售规模或宇树目标市场整体占比。',source='RESEARCH_INSTITUTION',nature='EXTERNAL_CONFIRMATION',note='与FAR的IR_FAR_02为同一论文URL；主体为机器人使用方和宇树产品的关系，不增加独立来源数。年月精度沿用固定v1。')
fact('CN_UNITREE','target_markets','G1已有科研应用：TWIST2研究团队使用G1进行人形遥操作与数据采集实验',['NEW_UNITREE_01'],status='SUPPORTED_EXTERNAL',kind='OBSERVED_APPLICATION',scope='G1 / TWIST2研究实际使用',period='2025-11固定v1',labels=['RESEARCH_EDUCATION'],note='这是产品实际应用场景，不等于宇树整体市场定位；不得将FAR研究成果归为宇树自研模型。')
evidence('NEW_UNITREE_02','CN_UNITREE','Advanced Quadruped Inspection Solutions','Unitree','','',
 'Power substation inspections, refinery pipeline checks, and mine tunnel monitoring','Industrial Energy、Intelligent City及Transportation & Water Utilities',
 '现行工业巡检方案覆盖电力、管道、矿山与城市基础设施等目标场景；无发布日期，不能据此补观察日前业务。')
fact('CN_UNITREE','target_markets','现行四足巡检方案面向变电站、炼化管线、矿井隧道及城市基础设施',['NEW_UNITREE_02'],append=True,scope='四足机器人巡检方案；现行页面',labels=['ENERGY_INSPECTION','INFRASTRUCTURE_INSPECTION'],note='官方目标场景；无日期，仅背景展示，未取得本条具名客户交付。')

evidence('NEW_GALBOT_01','CN_GALBOT','首款搭载宁德时代电池的重载人形机器人上岗','宁德时代','2026-06-24','',
 'Galbot S1已正式进入宁德时代智慧产线','2026-06-24日期及应用工序段',
 '宁德时代直接确认银河通用Galbot S1进入其智慧产线，在模组与电池包生产环节作业；全球拓展和后市场服务标准属于双方协议计划。',source='COUNTERPARTY_CONFIRMATION',nature='COUNTERPARTY_STATEMENT')
fact('CN_GALBOT','evidence_customer_delivery','宁德时代确认Galbot S1已进入其智慧产线，在模组与电池包环节承担长程自主作业',['NEW_GALBOT_01'],status='COUNTERPARTY_CONFIRMATION',kind='CUSTOMER_CONFIRMED_USE',scope='Galbot S1 / 宁德时代智慧产线',labels=['CUSTOMER_CONFIRMED_USE'],note='具名客户直接确认实际入线；无台数、付款和首次投运日，不据此确认收入或大规模交付。')
fact('CN_GALBOT','deployment_status_actual','宁德时代2026-06-24公告称Galbot S1已进入智慧产线，在模组与电池包生产环节作业',['NEW_GALBOT_01'],status='COUNTERPARTY_CONFIRMATION',append=True,kind='CUSTOMER_CONFIRMED_USE',scope='Galbot S1 / 宁德时代',note='入线为已发生状态；全球市场拓展与服务标准不当成已完成。')
fact('CN_GALBOT','target_markets','动力电池模组及电池包制造，面向物料搬运、拣选等高负载工序',['NEW_GALBOT_01'],status='COUNTERPARTY_CONFIRMATION',append=True,scope='Galbot S1 / 宁德时代',labels=['INDUSTRIAL_MANUFACTURING'],note='具名用户确认的产线场景；本条不推算部署量或付款。')

# Minor precision improvement found during acceptance: the existing preserved source explicitly dates the CES release Jan 7.
fourier=doc('CN_FOURIER')
ef=next(e for e in fourier['evidence'] if e['evidence_id']=='IR_FOURIER_01')
assert ef['publication_date']=='2026-01'
ef['publication_date']='2026-01-07';ef['note']+=' 本轮目视正文首行Jan. 7, 2026，发布日期由月精度补为日；CES展示事件仍仅月精度。'
for cid,d in DOCS.items():save(pathof(cid),d)
rules['rule_version']='stage-b-supplement-mapping-v2'
save(NEW/'work/grouping_rules_source.json',rules);save(NEW/'work/snapshot_index.json',snaps);save(NEW/'work/evidence_identity_baseline.json',identity)
save(NR/'ingestion.json',{'created_at':NOW,'source_candidate':str(RUN),'original_candidate_verdict':'ACCEPTED_WITH_LIMITATIONS','new_sources':ADDED,'changes':DELTAS,'ces_publication_precision_corrected':True,'independent_acceptance_of_supplement':False})
with (NEW/'search_log.jsonl').open('a',encoding='utf-8') as fh:
 for a in ADDED:fh.write(json.dumps({'ts_utc':NOW,'action':'PAGE_REVIEW','company_id':a['company_id'],'evidence_id':a['evidence_id'],'url':a['url'],'question':'用户追加授权：补查核心缺口；逐来源见supplement_records/ingestion.json','snapshot_id':a['evidence_id'],'capture_medium':a['capture_medium']},ensure_ascii=False)+'\n')
code=NEW/'scripts/s00_common.py';code.write_text(code.read_text(encoding='utf-8').replace('CODE_VERSION = "stage-b-evidence-integrated-v1"','CODE_VERSION = "stage-b-supplement-v2"'),encoding='utf-8')
save(NR/'source_preservation_summary.json',{'new_sources':len(ADDED),'raw_originals':sum(a['capture_medium']=='ORIGINAL_HTTP_BYTES' for a in ADDED),'web_extracts':sum(a['capture_medium']=='WEB_TOOL_EXTRACT' for a in ADDED),'initial_sandbox_fetch_attempts':{'count':9,'exit_code':7,'result':'connection denied; retried with approved public-source network access'},'limitation':'本次新增以实际下载或工具返回保存；日志不冒充搜索引擎原始请求记录。'})
print(json.dumps({'run':str(NEW),'sources':len(ADDED),'fact_changes':len(DELTAS),'companies':sorted(DOCS)},ensure_ascii=False))
