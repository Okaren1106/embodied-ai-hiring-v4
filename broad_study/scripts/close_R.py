from common import *
from datetime import datetime,timezone
q1=read(ROOT/'tables/R_Q1_coverage_concentration.csv');q3=read(ROOT/'tables/R_Q3_activity_summary.csv');joint=read(ROOT/'tables/R_joint_summary.csv');cross=read(ROOT/'tables/R_cross_function.csv')
ledger=[]
def issue(i,kind,old,new,why,evidence):ledger.append(dict(issue_id=i,kind=kind,old_statement=old,adopted_statement=new,reason=why,evidence=evidence,status='RESOLVED_FOR_INTEGRATED_BASELINE',reviewer='Astra'))
issue('R01','SCOPE','研究活动外职能64.0%与72.7%','WHOLE23为48/66；ALL24为48/75','相同数据的范围差，不是计数冲突','R_cross_function.csv')
issue('R02','SEMANTIC_ADJUDICATION','工程质量300+U8；工程部署231+U12','ALL24:308/1623与243/1623，U均0；WHOLE23:301/1599与235/1599','15广告20格全文、要求与树复核；原始偏移恢复或唯一引文定位；同岗不同段落可共同适用','R2_adjudication.csv;R_joint_evidence_locations.csv')
issue('R03','DENOMINATOR','未知退出但报告P/B','P/N主率；N=B-U；P/B和(P+U)/B为赋值界限','历史DSV待裁决时工程质量300/1615、工程部署231/1611为主率；不是300/1623和231/1623。界限保留为历史场景','R_joint_summary.csv;inputs/prior_reports/dsv/tables/D9_sensitivity_ledger.csv')
issue('R04','PROGRAMMING_ERROR','各职能最大贡献公司均X Square','按正例计数重新取所有并列公司；制造Figure28、软件Galbot25、ML XSquare26、公司支持Paxini21、硬件Apptronik20','旧程序将最大分母公司写入最大正例公司列；Astra旧结果也未列全并列集合','R_max_contributor_correction.csv')
issue('R05','PROGRAMMING_ERROR','Q3 value_company_equal','逐公司P/N算术平均，N=0不进入均值','旧DSV函数的公司实参实际是剔除参数；本轮复现8活动和3活动对的旧误算','R_DSV_company_mean_correction.csv')
issue('R06','ANALYTIC_CHOICE','各稿统一称来源完整子集','S1=17公司968；S2=11公司576；S3=同11公司再限正文200字符557','筛选对象不同；比例变化不能单独归因正文长度或正文完整性，更不证明招聘板采全','R_source_membership.csv;R_source_scope_summary.csv;R_S3_removed_ads.csv')
issue('R07','EVIDENCE_UPDATE','智元制造场景只有供应方自述','龙旗使用方兼共同开发方2026年4月和7月确认G2在产线运行与验证','保留Grok旧候选时间记录，增加本轮补证后的资格；不改写为当初已知','R_T5_new_evidence_facts.csv;R_case_selection_update.csv')
issue('R08','OVERCLAIM','职能与活动相互独立','职能与活动是不同测量维度，不能互相替代','交叉表不构成统计独立性结论','R_role_activity_bidirectional.csv')
issue('R09','OVERCLAIM','来源筛选差异证明正文详略影响','所见结果对联合筛选方案敏感','同时改变公司组成、岗位构成、来源和长度，不能识别各自因果贡献','R_Q2_v1_scope_bridge.csv')
issue('R10','OVERCLAIM','低覆盖K解释全公司业务模式差异','AgiBot×Galbot限企业支持与ML两类，其中仅一个技术职能','低覆盖和不同分母不能称提纯或业务模式贡献率；留给D严格算术分解','inputs/protocol_v2/研究执行书_v2.md')
issue('R11','MEASUREMENT_BOUNDARY','ACT_DEPLOYMENT均是客户现场部署；ACT_QUALITY均是制造质量','部署与维护包含模型运行、训练环境和真机等对象；质量含安全合规','本轮原文复核发现原认可标签的实际范围更宽。保留标签，纠正Astra旧稿及研究书过窄措辞','notes/EXECUTION_AMENDMENTS.md;R2_adjudication.csv')
issue('R12','TREE_RULE','根ALL即可判所有两活动无条件','必须检查全部相关子分支；N0396唯一混合树没有原编码双本人承担，不影响当前三对数值','区分通用规则缺陷和当前样本数值影响','R_mixed_tree_audit.csv')
issue('R13','REPORTING_ERROR','DSV T6-03写300/None、231/None及20条去重广告','修订为明确P/U/B/N与15条广告20个格','None排版/字段错误；格数不等于唯一广告数','R2_adjudication.csv;R_joint_summary.csv')
issue('R14','OVERCLAIM','部分类别均值大于中位数，因此总体右偏','只报告具体职能的均值、中位数等分布描述；不保留总体右偏结论','本轮不新增总体分布形态假设','inputs/prior_reports/dsv/tables/D1_q1_coverage_concentration.csv')
issue('R15','ROLE_OF_EVIDENCE','进入产线等于付费、独立第三方验证或供应商承担全部维保','实际使用、共同开发、验证、付款与责任分别记录；未公布的合同分工仍未知','客户/使用方官方材料也可能为利益相关方自述','R_T5_new_evidence_facts.csv')
issue('R16','PROSE_COVERAGE_ERROR','Grok正文及v2研究书称Galbot与Figure共同K约48%/48%','Galbot 82/181=45.30%；Figure 60/126=47.62%','D逐职能复算发现规划性近似表述不准确；K不变，旧Grok活动率56.1%/45.0%与本轮一致，仅覆盖文字更正','D2_decomposition_role_parts.csv;D2_K_membership.csv')
dump('tables/R1_discrepancy_ledger.csv',ledger)
facts=[]
def fact(i,c,source,pub,event,product,stage,actor,text,state,lim):facts.append(dict(fact_id=i,company_id=c,source_url=source,publication_date=pub,event_date=event,product_scene=product,stage=stage,actor=actor,assertion=text,state=state,source_nature='使用方/合作方官方披露；利益相关方，非独立现场审计',read_date='2026-09-16',limits=lim,archive='evidence/R_external_retrieval_20260916.json',evidence_version='R_customer_v2',hiring_observation='2026-09-11',time_applicability='披露早于招聘观察；不直接证明状态持续到观察日'))
l1='https://us.longcheer.com/en/col76/260.html';l2='https://us.longcheer.com/en/col76/281.html';cat='https://www.catl.com/news/10053.html'
fact('R_E01','CN_AGIBOT',l1,'2026-04-15','2026-03-16（文内所述集成起始）；2026-04-14直播','G2/龙旗平板出货前测试','ACTUAL_USE','龙旗与智元','公告记录G2进入制造主线并执行测试上下料及分拣','SUPPORTED','时长和运行成绩为公司披露；无付款或全周期运维合同证明')
fact('R_E02','CN_AGIBOT',l1,'2026-04-15','2025-10合作起始；2026年初概念验证；具体日未披露','G2/龙旗产线','CO_DEVELOPMENT','龙旗+智元','龙旗提供制造工艺、节拍和异常约束，智元提供感知、规划与力控等能力，组建现场联合团队','SUPPORTED','共同开发不等于标准整机采购；不能把所有生产责任交给智元')
fact('R_E03','CN_AGIBOT',l2,'2026-07-11','2026-06-23至2026-06-28','8台G2/龙旗平板测试','ACTUAL_USE_VALIDATION','联合项目团队','龙旗报告六天64小时验证，任务包括测试上下料、转运和分拣','SUPPORTED','验证与真实订单场景有资料，99.99%等成绩为披露方指标，不作本研究独立测量')
fact('R_E04','CN_AGIBOT',l2,'2026-07-11','2026-06-23至2026-06-28','龙旗制造线','HUMAN_RESPONSIBILITY','龙旗现场人员','人员承担检查监督、协调和异常处置等工作；双方联合推进系统接入及节拍、异常、安全适配','SUPPORTED','未公布常态运维合同及员工归属完整清单')
fact('R_E05','CN_GALBOT',cat,'2026-06-24','截至2026-06-24已发生；投产具体日未知','Galbot S1/宁德时代模组及电池包产线','ACTUAL_USE','银河通用开发；宁德时代使用并提供电池','公告确认S1进入产线，涉及自主移动、搬运和取放工作','SUPPORTED','未公布付款、整线集成及持续运维责任分配')
fact('R_E06','CN_GALBOT',cat,'2026-06-24','未来安排，尚无履行日期','S1/售后服务协同','MAINTENANCE_PLAN','双方计划协作','服务体系延伸为未来合作安排','PLANNED','不能填成已经履行的维保事实')
for i,c,s,p in [('R_E07','CN_AGIBOT',l2,'G2/龙旗'),('R_E08','CN_GALBOT',cat,'S1/宁德时代')]:fact(i,c,s,'2026-07-11' if c=='CN_AGIBOT' else '2026-06-24','未披露',p,'PAYMENT_AND_FULL_MAINTENANCE','未知','本轮所读官方材料未确证付款条款及全部持续维保责任','UNKNOWN','未知不是免费或没有维护，不推断外包')
dump('tables/R_T5_new_evidence_facts.csv',facts)
dump('tables/R_case_selection_update.csv',[{'company_id':'CN_AGIBOT','old_selection_record':'Grok旧选择记录保留：当时供应方证据口径','new_evidence':'R_E01—R_E04','current_eligibility':'使用方兼共同开发方确认实际制造场景，可进入候选','selected_use':'O四公司完整框；D的AgiBot×Galbot为有限补充，Galbot×Figure为主分解','unchanged_limits':'低覆盖、一个技术共同职能；产品事实不能自动归属公司招聘'}, {'company_id':'CN_GALBOT','old_selection_record':'实际制造场景候选','new_evidence':'R_E05—R_E06','current_eligibility':'实际使用确认；运维计划独立列示','selected_use':'D主分解及O原文对象比较','unchanged_limits':'产品级事实，付款与持续运维仍未知'}])
# Preserve every inherited assertion as provenance; only new facts are marked re-read.
sources={'astra':'T5_responsibility_long.csv','grok':'T5_delivery_responsibility.csv','dsv':'D6_business_responsibility_long.csv'}
inherited=[]
for who,fn in sources.items():
    for n,r in enumerate(read(ROOT/f'inputs/prior_reports/{who}/tables/{fn}'),1):inherited.append({'integrated_id':f'{who.upper()}_{n:04}','source_report':who,'source_table':fn,'company_id':r.get('company_id',''),'verification_status':'INHERITED; original assertion retained, not all re-read in R','payload_json':js(r)})
dump('tables/R_T5_inherited_provenance.csv',inherited)
dump('tables/R_T5_company_status.csv',[{'company_id':c,'company_name':CO[c]['company_name'],'ads':CO[c]['n_ads'],'scope':CO[c]['entity_scope_inherited'],'stratum':CO[c]['stratum'],'fact_status':'CUSTOMER_EVIDENCE_UPDATED' if c in ['CN_AGIBOT','CN_GALBOT'] else 'INHERITED_NOT_REVERIFIED','new_fact_ids':js([r['fact_id'] for r in facts if r['company_id']==c]),'inherited_assertions':sum(r['company_id']==c for r in inherited),'limits':CO[c]['caveat'],'business_to_ad_attribution':'NOT_INFERRED_FROM_COMPANY_BRAND'} for c in ALL])
t6=[]
for who,fn in [('astra','T6_conclusions_sensitivity.csv'),('grok','T6_conclusions.csv'),('dsv','T6_conclusion_ledger.csv')]:
    for n,r in enumerate(read(ROOT/f'inputs/prior_reports/{who}/tables/{fn}'),1):
        ident=r.get('id',r.get('conclusion_id',str(n)));status='RETAIN_WITH_SCOPE_AND_NONCAUSAL_LIMITS';issues='R01;R06;R15'
        if who=='dsv':issues+=';R03;R04;R05;R08;R09;R10;R13;R14'
        if who=='astra':issues+=';R11'
        if who=='grok':issues+=';R07;R12'
        if who=='dsv' and ident=='T6-03':status='REPLACE_NUMBERS_AND_DENOMINATORS'
        if who=='dsv' and ident=='T6-05':status='RETAIN_DESCRIPTIVE_DIFFERENCE_WITHDRAW_BUSINESS_CAUSAL_READING'
        t6.append({'source_report':who,'old_id':ident,'status':status,'linked_issues':issues,'old_payload_json':js(r),'new_baseline':'R main text and R numeric tables; O/D/Q pending, do not claim new modules completed'})
dump('tables/R_T6_claim_mapping.csv',t6)
newclaims=[('R_T6_01','Q1','制造、软件、ML是本目录下样本广告总量前三；公司覆盖广泛，但不能推断行业总体人才结构','R_Q1_coverage_concentration.csv','SUPPORTED_DESCRIPTIVE'),('R_T6_02','Q3','整公司研究/部署与维护/质量活动位于专门职能之外分别48/66、264/343、300/459；不是统计独立或部门协同证明','R_cross_function.csv','SUPPORTED_DESCRIPTIVE'),('R_T6_03','Q3','20个争议格复核后共同承担成立，整公司三对65、301、235/1599；仅描述同广告本人责任','R2_adjudication.csv;R_joint_summary.csv','ADJUDICATED'),('R_T6_04','Q2 v1','原两职能技术及要求语境读数保留；来源筛选改变多项组成，不能只解释为文本长度效应','R_Q2_v1_scope_bridge.csv','SUPPORTED_WITH_CATALOG_LIMITS'),('R_T6_05','BUSINESS','龙旗资料支持智元G2实际使用与共同开发；宁德时代资料支持S1实际使用，尚不足以确定付款及全部运维','R_T5_new_evidence_facts.csv','SUPPORTED_FACTS_WITH_UNKNOWN_RESPONSIBILITIES'),('R_T6_06','EXPLANATION','工作对象、受众及构成值得继续分析；旧标准化未完成严格分解，公司品牌未证明产品归属','notes/EXECUTION_AMENDMENTS.md','O_D_Q_PENDING')]
dump('tables/R_T6_integrated_claims.csv',[dict(conclusion_id=i,question=q,wording=w,tables=t,status=s) for i,q,w,t,s in newclaims])
def pct(x):return f'{float(x)*100:.2f}%'
text=['# 三份阶段D报告合并验收｜Astra','日期：2026-09-16。R模块完成；本报告不表示O、D、Q及E已完成。','## 1. 验收结论','三份分析共享一个冻结样本，不能视为三倍样本或用多数投票裁决。现已统一到23家整公司主口径、24主体补充口径；15项分歧完成登记。原认可分类和三个旧报告均未改写。','## 2. 计数结果','|活动对|整公司 P/U/N|全24 P/U/N|','|---|---:|---:|']
for pid in ['RESEARCH_ENGINEERING','ENGINEERING_QUALITY','ENGINEERING_DEPLOYMENT']:
    a=next(r for r in joint if r['scope']=='WHOLE23' and r['pair']==pid);b=next(r for r in joint if r['scope']=='ALL24' and r['pair']==pid);text.append(f"|{pid}|{a['P']}/{a['U']}/{a['N']}|{b['P']}/{b['U']}/{b['N']}|")
text+=['','P为明确正例，U为该格关系未知，B为基础范围，N=B−U。报告P/N，并列P/B与(P+U)/B的未知赋值界限。活动来源不足31条不进入活动基础范围。','## 3. 修正不是只改数字','20个争议格来自15条广告。逐条复核职责、要求和职责树后，均支持两活动由同一岗位共同承担。不同职责段落不必重叠才共同适用；任职知识任选也不能自动变成工作方向任选。完整理由、唯一身份与证据位置见R2_adjudication.csv。','DSV的8项活动和3组共同承担均值误算已通过重建旧程序逻辑复现并更正。最大正例贡献公司与最大分母公司分别列示，所有并列保留。公司等权为有分母公司的P/N算术平均。','一个额外的实质修正：原ACT_DEPLOYMENT实际也编码模型部署、训练环境维护；ACT_QUALITY也包含安全合规。综合版使用“部署与维护”“质量验证”，不把全部活动解释为客户现场或制造质量。旧Astra及研究书的部分窄化表述由本轮A01修订替代。','## 4. 来源子集是三种不同筛选','S1为17家968条，仅要求公司内活动来源不足为零；S2为11家576条，加官方来源、质量等级及主职能可读；S3在S2上再限正文至少200字符，剩557条。19条移除广告逐条保留。各方案都不等于招聘板全量采集，也不能把变化归因单一文本长度。','## 5. 案例证据更新','[龙旗4月披露](https://us.longcheer.com/en/col76/260.html)与[7月披露](https://us.longcheer.com/en/col76/281.html)支持使用方兼共同开发方确认G2产线任务及联合开发。后一材料描述6月23—28日八台机器人的验证。它们不证明付费采购、独立审计或智元承担全部维护。','[宁德时代披露](https://www.catl.com/news/10053.html)支持银河通用S1进入模组及电池包产线；服务延伸安排仍以未来计划记录。上述材料早于9月招聘观察，但不能据此断言每项状态持续至观察日。','保留旧候选选择的时间记录，新增补证后的资格状态。O继续四公司原文框；D以银河通用×Figure为主分解，智元×银河通用为有限补充。Nimble×Dexterity与Agility×Nimble不满足共同职能门槛时保留NA。','## 6. 保留与退出','保留跨职能活动、同职能技术/要求语境与有限案例差异；撤回统计独立、纯文本详略因果解释及公司业务模式贡献率等过强用词。未知的付款、持续维护和广告产品归属不填零。业务背景用于限制解释，不能由招聘缺失反推外包。','## 7. 验证与界限','55项独立SQL算术检查通过；这是同一研究者的第二套计算实现，不是外部同行复核。R2新增语义判读由Astra完成；其余活动语义继承原认可结果，并检查证据定位，未声称重新阅读1654条全文。输入909文件锁保持有效。','R_T5_inherited_provenance.csv完整保留旧断言出处，R_T5_company_status.csv区分本轮补证与继承；R_T6_claim_mapping.csv逐条连接三稿结论与15项裁决。可重复运行scripts/reconcile_R.py与scripts/close_R.py。后续O/D/Q可在本综合基线上推进。']
text=[x.replace('15项分歧','16项分歧').replace('15项裁决','16项裁决') for x in text]
text.append('方向二接续复算又核定一处正文近似错误（R16）：银河通用×Figure共同K覆盖实际为45.30%/47.62%，替代旧Grok及研究书的约48%/48%。K与此前对应活动率未变。原稿不倒改，综合版采用精确值。')
(ROOT/'reports/R_合并验收报告_Astra.md').write_text('\n\n'.join(text),encoding='utf-8')
print('R interpretation outputs written',len(ledger),len(facts),len(inherited),len(t6))
