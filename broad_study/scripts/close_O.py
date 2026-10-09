from common import *
import sys,random,sqlite3
sys.path.insert(0,str(ROOT/'configs'));from O_manual import D
ss=read(ROOT/'tables/O1_processing_status.csv');ee=read(ROOT/'tables/O2_evidence_long.csv');rr=read(ROOT/'tables/O4_company_role_object.csv');sens=read(ROOT/'tables/O4_sensitivity.csv')
# Literal year constraints are separate; branches and scope are never collapsed into one rank.
year=[]
for e in ee:
    if e['field_type']!='EXPERIENCE_RAW':continue
    text=e['quote'];norm=text.replace('五','5');amb='1-2+' in norm;constraints=[]
    if not amb:
        for m in re.finditer(r'(\d+)\s*(?:[-~—]\s*(\d+)\s*)?(\+|年及以上|年以上|年\s*以上|years?|年)',norm,re.I):
            constraints.append(dict(lower=int(m[1]),upper=int(m[2]) if m[2] else None,upper_open=not bool(m[2]),literal=m.group(),operator='RANGE' if m[2] else 'LOWER_BOUND',unit='years'))
    year.append(dict(identity_key=e['identity_key'],reading_id=e['reading_id'],raw=text,constraints_json=js(constraints),relation='ALTERNATIVE_EDUCATION_PATHS' if '或博士' in text else 'NESTED_TOTAL_AND_DOMAIN' if '其中' in text else 'MULTIPLE_RAW_CONSTRAINTS' if len(constraints)>1 else 'AMBIGUOUS_LITERAL' if amb else 'AS_WRITTEN',context=e['note'],interpretation='Not a standardized seniority rank; raw clause prevails',evidence_id=e['evidence_id']))
dump('tables/O2_experience_constraints.csv',year)
review=[];sample=json.loads((ROOT/'configs/O_secondary_review_sample.json').read_text(encoding='utf-8'))
for r in ss:
    review.append(dict(identity_key=r['identity_key'],reading_id=r['reading_id'],product_review='ALL84_SECOND_PASS',link_review='ALL84_SECOND_PASS; only evidenced links asserted',object_review='ALL84_EVIDENCE_SECOND_PASS',other_fields_random_review=int(r['seq']) in sample['seq'],reviewer='Astra',independence='Same researcher, separate pass; no external double coding',result='CORRECTED' if int(r['seq']) in [1,46,77] else 'RETAINED',detail=D[int(r['seq'])]['note']))
dump('tables/O_secondary_review.csv',review)
save_json('verification/O_semantic_review.json',{'reviewer':'Astra','all_product_decisions':84,'all_ads_for_link_decisions':84,'explicit_links_checked':47,'object_evidence_second_pass':84,'other_fields_seeded_sample':sample['seq'],'changes':{'N0384':'取消机器人应用运行系统对象；保留模型运行时与真机联调','N0099':'高性能算子从训练基础设施改其他；训练同事协作不等于对象归属','N0859':'取消训练基础设施对象；原引用仅属经历要求'},'method':'First pass read full ad fields; second pass inspect all object/link quotes and product decisions with source context, 20 random other-field checks. Not independent external review.'})
# Check aggregation using a separate SQL implementation of all 192 company-role-object cells.
db=sqlite3.connect(':memory:');db.execute('create table x(c text,f text,o text,r text,s text)');db.executemany('insert into x values(?,?,?,?,?)',[(r['company_id'],r['role'],r['object'],r['responsibility'],r['state']) for r in read(ROOT/'tables/O2_object_states.csv')]);ncheck=0
for c,f,o,r,n,p in db.execute("select c,f,o,r,count(*),sum(s='P') from x group by c,f,o,r"):
    z=next(x for x in rr if (x['company_id'],x['role'],x['object'],x['responsibility'])==(c,f,o,r));assert (p,n)==(int(z['P']),int(z['N']));ncheck+=1
save_json('verification/O_independent_arithmetic.json',{'checks':ncheck,'pass':True,'method':'Same researcher SQLite aggregation independent of main Python counting'})
def val(c,f,o,rel='ANY_RESPONSIBILITY',scenario=None):
    data=sens if scenario else rr
    z=next(r for r in data if (r['company_id'],r['role'],r['object'],r['responsibility'])==(c,f,o,rel) and (scenario is None or r['scenario']==scenario));return z['P']+'/'+z['N']
ML='RF_ML_AI_ENGINEERING';SW='RF_ROBOTICS_SOFTWARE'
out=['# 方向一：完整84条工作对象研究｜Astra','## 1. 本轮回答了什么','在固定四公司、两职能的84条广告中，模型/策略、模型训练系统、机器人运行软件、工具和履单业务系统经常出现在同一主职能内。原文可以支持工作对象的区别，但大部分广告仍不能归属具体产品、客户项目或明确命名业务线。该缺口限制了从公司业务到岗位比例的解释。','## 2. 方法与范围','固定框为智元19、银河通用49、Dexterity7、Nimble9条，其中ML44、软件40。未用关键词筛选广告。先按8个公司职能格抽取16条试读，种子20260916；冻结8类对象定义后逐条阅读全文。对象多值，承担与参与分列，比例不可相加。原认可主职能不改。','所有84条均有可读对象判定。新字段在派生层保存；440条证据涵盖对象、原始资历、受众、命名产品/单元及技能用途。O3记录47条明确语义连接，保留职责、能力要求、经历要求与优先项的不同性质；不将其当作全部技能出现量或员工实际使用率。','## 3. ML职能内的工作对象','|公司|模型/策略|训练/推理基础设施|数据资产|真机/物理现场系统|','|---|---:|---:|---:|---:|']
for c in ['CN_AGIBOT','CN_GALBOT','US_DEXTERITY','US_NIMBLE']:out.append('|'+CO[c]['company_name']+'|'+'|'.join(val(c,ML,o) for o in ['MODEL','TRAINING_INFRA','DATA','FIELD_SYSTEM'])+'|')
out+=['','这里“真机/物理现场系统”包含实验室或样机测试、迁移和现场问题，不能统一叫客户生产交付。对象统计包含明确参与，主表之外另列OWNED与PARTICIPATES。','智元ML12条均以模型/策略或模型运行时为对象，部分直接面向语音、交互、推理延迟和端侧资源。银河通用除模型研发，还有更常见的数据闭环及真机工作；但其ML中6条明确面向校招/实习，职责表述的参与责任与招聘受众均需保留。两边并非“纯研究对纯交付”的二分。','Nimble三条ML均明确建设或组织数据，样本很小。Dexterity的模型岗位包含带队监督、视觉和规划等任务，不能把全公司Mech产品简介自动连接到每个岗位。','## 4. 软件职能内的异质性','|公司|机器人运行软件|工具链|履单业务软件|其他对象|','|---|---:|---:|---:|---:|']
for c in ['CN_AGIBOT','CN_GALBOT','US_DEXTERITY','US_NIMBLE']:out.append('|'+CO[c]['company_name']+'|'+'|'.join(val(c,SW,o) for o in ['ROBOT_RUNTIME','TOOLCHAIN','FULFILMENT_IT','OTHER'])+'|')
out+=['','智元软件7条中既有交互控制面、整机架构，也有通用后端、开放网关和实时音视频。银河通用25条中19条连接机器人运行软件，10条涉及开发测试工具；工业工具、存储和检索等对象另外保留。','Nimble软件6条中2条涉及履单业务软件或WMS接口。Cloud Logistics广告明确无需机器人或物流经验，因此不能把机器人企业的全部软件招聘视为机器人算法开发。Dexterity仅两条软件主类广告，分别涉及裸机/混合云基础设施及PLM/BOM/ECO文控。后者是原主类内部的内容异质性，本轮不改分类，也不据此计算两个公司“相同软件任务”的技术优劣。','## 5. 产品归属与资历的真实边界','仅3/84条能直接定位到本轮记录的命名产品、平台或业务线：智元灵心、Nimble Cloud Logistics、Nimble Brain。其余81条保持具体产品/项目归属未知。通用功能团队名（如ML Infrastructure team）不等于单一商业产品；没有把G2、S1或Mech分配给所有相关公司广告。也没有找到可把未知广告唯一连接至这些产品的直接证据链。','经验年限明示39条，未明示45条；有学历表达76条，其中既有学位替代，也有“或同等经历”及未指定层级的Degree。N0386保留3年以上或博士毕业后2年以上路径；N0418保留总8年以上且其中行业5年以上，不能加成13年；N0925的1–2+原样保留，N0913年限位于优先条件。没有生成统一初级/资深等级。','## 6. 敏感性与可比较程度','完整结果、剔除明确校招实习、完全一致非空duties字段保留一条、仅明示产品及仅明示年限分别计算。完全一致字段检查移除2条；这比只取职责段落更严格，不是模糊去重，也不把多地广告视为错误。仅明示产品时大多数格N=0，记NA，不赋给主产品。','同对象活动点值另表列示，但同对象仍不等于相同任务：模型开发、模型推理和训练平台维护也可能不同。任何少于10条的格标小样本；四家公司不能合并成国家或业务模式因果比较。','## 7. 四家公司解释稿','**智元：**所见ML广告更多展示多模态模型与运行系统，软件涉及机器人整机与平台。与龙旗共同开发的客户资料可作背景，但无法把这些广告归给G2项目。','**银河通用：**模型、数据、真机任务及机器人软件工具有较多同时出现；工业、交互、人形等对象并存。客户S1资料不能覆盖全部招聘，校招/实习以及参与型措辞也影响表述。','**Nimble：**招聘同时涉及机器人模型、训练数据、机器人平台和自营履单IT。持续服务的业务责任可提出多种软件需求，而不是单一部署指标的必然提高。','**Dexterity：**有限样本出现模型全周期、基础设施和工程数据治理。既定软件主类中的文控对象提醒我们先核查任务可比性；两条软件广告不具备稳健公司均值解释条件。','## 8. 验证和交付','Astra完成全文首轮及第二遍证据核对；84条产品判断和技能连接状态均检查，所有对象证据复查，另抽20条资历/受众等字段。复查纠正3处对象范围。不存在外部独立双人编码。192个公司×职能×对象×责任统计格由第二套SQLite汇总检查。','O1处理清单、O2证据和逐对象P/Z表、O3用途连接、O4所有点值/未知/敏感性以及本O5报告共同构成交付。脚本analyze_O.py与close_O.py从冻结输入和具名人工判读配置重建结果。']
# Derive prose counts rather than trust hand-written expectations.
years=sum(r['years_state']=='STATED' for r in ss);degree=sum(r['degree_state']=='STATED' for r in ss)
out=[x.replace('经验年限明示39条，未明示45条；有学历表达76条',f'经验年限明示{years}条，未明示{84-years}条；有学历表达{degree}条') for x in out]
(ROOT/'reports/O_工作对象研究报告_Astra.md').write_text('\n\n'.join(out),encoding='utf-8')
print('O close',ncheck,'years',years,'degree',degree)
