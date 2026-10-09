"""Analyst-authored decisions. No job proportions, skill rates or country contrasts determine membership."""
from pathlib import Path
import json
RUN=Path(__file__).resolve().parents[1]
def dump(name,obj):(RUN/'decisions'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def fid(c,s):return 'F_'+c+'__'+s
groups={
 'SYSTEM_PRODUCTS':{'name':'整机与机器人系统产品','definition':'在观察日前已有具名自主机器人整机/系统产品，或针对该系统的发布、提供或外部使用证据。允许自研模型并行，不推断收入主业、已付费或自主制造所有部件。','use':'PRIMARY_DESCRIPTIVE'},
 'CROSS_BODY_MODELS':{'name':'跨本体模型与软件','definition':'公开供给对象明确为可用于多种机器人本体的模型/软件能力；本包足以支持该供给形态，但不足以支持本公司的自有整机产品入SYSTEM_PRODUCTS。不得简称纯软件或已商业许可。','use':'PRIMARY_DESCRIPTIVE'},
 'COMPONENT_SYSTEM_PORTFOLIO':{'name':'触觉部件与机器人产品组合','definition':'可核实的触觉芯片/传感器量产供给和机器人产品并行；保留部件供给边界，不依据未披露收入给出主业占比。','use':'CASE_ONLY'},
 'ROBOT_OPERATED_SERVICE':{'name':'自营机器人履单服务','definition':'公开交付对象为依托自营机器人履单网络提供的3PL服务，不由部署机器人推断其对外出售机器人。','use':'CASE_ONLY'},
 'TEAM_SEPARATE':{'name':'大公司内部研究团队（范围单列）','definition':'招聘主体为具名内部团队；该项是主体范围隔离，不作为与整公司并列的商业类别。','use':'SCOPE_SEPARATE'}
}
# company_id, presentation stratum, fact fields, decision, scope caveat
manual=[
 ('CN_AGIBOT','SYSTEM_PRODUCTS',['product_lines','delivery_form__2'],'A3/X2产品发布及G2产线提供支持整机系统形态；四足、手和清洁等业务并行。','不能把全公司83条广告归给G2或工业产线。'),
 ('CN_ASTRIBOT','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'S/T本体与Lumo/DuoCore/OS一体；模型能力不使其退出机器人系统组。','入组主要依赖有日期媒体，媒体排除敏感性中退出。'),
 ('CN_DEEPROBOTICS','SYSTEM_PRODUCTS',['product_lines','delivery_form__2'],'四足本体及X30/SPock改装系统支持机器人产品形态。','客户SPock公告未直接点名X30，厂家/型号归属仍是供应方自述。'),
 ('CN_FOURIER','SYSTEM_PRODUCTS',['product_lines_rehab','product_lines_humanoid','delivery_form'],'康复设备和GR系列都是实体机器人产品；按整家公司组合保留。','康复/人形多产品；不能将康复交付外推为GR系列付费交付。'),
 ('CN_GALAXEA','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'有日期资料同时明确本体、开发平台、数据与模型，采用系统产品归属并保留模型并行说明。','R1无日期页面不用于观察时点场景入组；不把模型研发等同跨本体软件商业许可。'),
 ('CN_GALBOT','SYSTEM_PRODUCTS',['delivery_form','product_lines','deployment_status_actual__2'],'机器人系统与模型一体，零售门店和客户产线分别有依据。','零售自营与工业客户作业是两种模式，不从任一模式推断全公司收入重心。'),
 ('CN_LIMX','SYSTEM_PRODUCTS',['product_lines','delivery_form__2'],'机器人本体及已发售的TRON1平台足以确认系统产品；OS/FluxVLA为并行能力。','预订、订单量与履约交付分开。'),
 ('CN_NOETIX','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'投资方披露机器人产品及制造销售形态，BUMI学校交付另有证据。','学校交付为捐赠，既不计收入也不推断主要市场份额。'),
 ('CN_PAXINI','COMPONENT_SYSTEM_PORTFOLIO',['product_lines','delivery_form'],'触觉芯片/传感器量产供应与手、机器人同时明确，单列产品组合以免将125条广告都解释为整机业务。','没有可核实收入占比；不能称纯部件公司，也不以标题中的客户名称建立终端行业组。'),
 ('CN_SPIRITAI','SYSTEM_PRODUCTS',['product_lines','delivery_form__2'],'Moz系列及小墨产线作业支持实体系统；Spirit模型作为并行供给记录。','首发月份冲突不影响已有产品存在，但冲突条目不作日期支持；家庭是长期目标。'),
 ('CN_UNITREE','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'四足及人形整机产品与销售形态有有日期资料。','G1科研使用是观察到的应用，不证明科研是收入主业；工业官网页无日期。'),
 ('CN_XSQUARE','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'0755养老机器人和自研本体/部件/数采系统支持实体系统，模型开源并行。','广告覆盖整家公司；具名养老部署与物流未具名运行分开。'),
 ('US_AGILITY','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'Digit与Arc组合通过RaaS提供给客户；仍属于机器人系统产品。','RaaS合同与客户现场不代表已披露机器人数量或合同金额。'),
 ('US_AMAZON_FTR','TEAM_SEPARATE',['research_subject','product_lines'],'以输入公司主表的内部团队边界单列；TWIST2为研究系统，Unitree G1不是FAR自产本体。','参加Q1/Q2/Q3团队点值，退出整公司业务组均值及国家组均值。'),
 ('US_APPTRONIK','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'Apollo及配套部署工具支持机器人系统产品。','当前定位制造/仓储物流；后续零售、医疗及家庭计划不作当前场景。'),
 ('US_BOSTON_DYNAMICS','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'Atlas/Spot/Stretch与软件平台为多产品系统组合。','Stretch既有使用与Atlas产品发布分开；整公司招聘不分配到某一产品。'),
 ('US_DEXTERITY','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'Mech移动双臂及卡车装载软件应用属于具名机器人系统产品。','无日期全轮班运营规模不进入当前实际部署证据组。'),
 ('US_DILIGENT','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'Moxi院内服务机器人为主体产品，被收购后仍保留该公司招聘主体。','收购前后及渠道边界保留；收购方整体业务不合并进来。'),
 ('US_FIELD_AI','CROSS_BODY_MODELS',['product_lines','delivery_form'],'FFM是可驱动多种形态的风险感知模型/软件大脑；软件在工作流部署的表述有日期。','客户运行规模为自述，不据此确认客户付款或销售合同。'),
 ('US_FIGURE','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'Figure03整机与Helix一体供给；具名本体使其归入系统产品组。','Figure02在BMW运行与Figure03到厂/后续安排分开。'),
 ('US_NIMBLE','ROBOT_OPERATED_SERVICE',['product_lines','delivery_form'],'自有机器人履单中心与robotic 3PL是已披露供给形态，单列服务运营。','不用机器人中心推断对外售卖机器人，也不将中心启用视为所有节点成熟运行。'),
 ('US_PHYSICAL_INTELLIGENCE','CROSS_BODY_MODELS',['product_lines','delivery_form'],'π0明确跨多种本体控制，公开发布的是模型与研究演示。','是独立公司，非FAR式内部团队；未披露商业合同，家务演示不是家庭市场交付。'),
 ('US_PICKLE','SYSTEM_PRODUCTS',['product_lines','delivery_form'],'Unload System是明确的机器人卸货系统及部署供给。','具体吞吐与已运行规模按公司自述保留。'),
 ('US_SKILD','CROSS_BODY_MODELS',['product_lines','delivery_form'],'Skild Brain/S1公开供给为跨本体基础模型，已有日期明确发布。','无日期ARR/客户数不作当前商业化分组依据；跨本体不等于具体行业。')
]
primary=[]
for c,g,fields,why,caveat in manual:
 primary.append({'company_id':c,'stratum':g,'basis_fact_ids':[fid(c,f) for f in fields if f!='research_subject'],'scope_basis':'inputs/stage_b/company_profile.csv','decision_reason':why,'caveat':caveat,'judgement_kind':'ANALYST_CLASSIFICATION_FROM_FROZEN_FACTS'})
dump('supply_classification.json',{'version':'1.0','groups':groups,'precedence':['TEAM_SCOPE_SEPARATE','EXPLICIT_ROBOT_OPERATED_3PL','EXPLICIT_COMPONENT_AND_SYSTEM_PORTFOLIO','NAMED_OWN_ROBOT_SYSTEM','EXPLICIT_CROSS_BODY_MODEL'],'rationale':'当前24家上的公开供给形态归类；顺序处理已识别混合边界，不推断收入主业或不存在其他业务。新增公司/证据须复核规则而非强行落入旧类。','companies':primary})
scenes={'MANUFACTURING':'制造产线','LOGISTICS':'仓储与物流','FIELD_INSPECTION':'基础设施/野外巡检','HEALTHCARE_CARE':'医疗与照护','RETAIL_SERVICE':'零售及商业服务','HOME':'家庭使用','RESEARCH_EDUCATION':'科研与教育','UNSPECIFIED':'终端场景未确立'}
rows=[]
def scene(c,group,state,field,claim,why=''):
 rows.append({'company_id':c,'scene':group,'state':state,'basis_fact_ids':[fid(c,x) for x in field.split('|')] if field else [],'selected_claim':claim,'decision_reason':why,'judgement_kind':'ANALYST_CLASSIFICATION_FROM_FROZEN_FACTS'})
scene('CN_AGIBOT','MANUFACTURING','OBSERVED_USE','deployment_status_actual__2','G2在龙旗平板产线并线及均胜零部件装配','公司自述，非客户原文确认。')
scene('CN_AGIBOT','LOGISTICS','CURRENT_TARGET','target_markets__2','物流仓储为公告列举的应用范围','不将产量改写成交付量。')
scene('CN_ASTRIBOT','RETAIL_SERVICE','OBSERVED_USE','deployment_status_actual|target_markets','报道列机器人MART零售商业落地','限报道所述零售，不外推其他服务行业。')
scene('CN_DEEPROBOTICS','FIELD_INSPECTION','OBSERVED_USE','deployment_status_actual__2','X30/SPock新加坡电缆隧道巡检试点','具体型号来自供应方。')
scene('CN_DEEPROBOTICS','RESEARCH_EDUCATION','CURRENT_TARGET','target_markets','列举教育科研为应用场景')
scene('CN_DEEPROBOTICS','LOGISTICS','CURRENT_TARGET','target_markets','列举物流运输为场景','宽泛定位，没有对应客户现场。')
scene('CN_FOURIER','HEALTHCARE_CARE','OBSERVED_USE','deployment_status_actual|product_lines_rehab','康复中心与医院的康复设备部署','不能与院内物流或养老照护当成同一任务。')
scene('CN_FOURIER','MANUFACTURING','CURRENT_TARGET','target_markets','GRW面向制造重载辅助','产品定位，不是已运行工厂。')
scene('CN_FOURIER','LOGISTICS','CURRENT_TARGET','target_markets','GRW面向仓储物流','产品定位。')
scene('CN_FOURIER','HOME','CURRENT_TARGET','target_markets_domestic_rehab','国内康复及居家场景定位','主体是康复产品；不得扩展成GR系列已进入家庭。')
scene('CN_FOURIER','HOME','DEMONSTRATED_TASK','evidence_demo__3','WAIC展台居家Demo','演示单列，不作居家部署。')
scene('CN_GALAXEA','RESEARCH_EDUCATION','BACKGROUND_DATE_UNKNOWN','target_markets','R1科研与R1 Lite数据采集定位','产品页无日期，退出观察时点场景统计。')
scene('CN_GALBOT','RETAIL_SERVICE','OBSERVED_USE','deployment_status_actual','香港自营机器人零售门店营业')
scene('CN_GALBOT','MANUFACTURING','OBSERVED_USE','deployment_status_actual__2','宁德时代模组和电池包生产作业','直接客户确认。')
scene('CN_GALBOT','RETAIL_SERVICE','FUTURE_PLAN','target_markets','旅游区扩展及图书馆/博物馆讲解','计划部分不计已发生业务。')
scene('CN_LIMX','RESEARCH_EDUCATION','CURRENT_OFFER','delivery_form__2|target_markets__2','TRON1科研/教学平台发售和预订','未由预订推断履约。')
for group,claim in [('RETAIL_SERVICE','商业服务'),('FIELD_INSPECTION','全地形巡检'),('MANUFACTURING','工业应用')]:scene('CN_LIMX',group,'CURRENT_TARGET','target_markets',claim,'宽泛现行定位；当前具体落地未据此确立。')
scene('CN_NOETIX','RESEARCH_EDUCATION','OBSERVED_DONATION','deployment_status_actual|target_markets','两台BUMI捐赠学校用于AI教学','教育应用连接可成立，付费市场不能据此成立。')
scene('CN_PAXINI','UNSPECIFIED','END_USE_UNSPECIFIED','target_markets','触觉部件为具身产业基础配置','缺少清楚终端任务；不从比亚迪标题归汽车产线。')
scene('CN_SPIRITAI','MANUFACTURING','OBSERVED_USE','deployment_status_actual__2','小墨在宁德时代中州电池PACK产线插接','媒体陈述。')
scene('CN_SPIRITAI','RETAIL_SERVICE','CURRENT_TARGET','target_markets','零售门店及Moz2的商超、酒旅、办公楼宇','产品面向领域，不等于全部部署。')
scene('CN_SPIRITAI','HOME','LONG_TERM_GOAL','target_markets__2','家庭服务长期目标','退出当前家庭业务组。')
scene('CN_UNITREE','RESEARCH_EDUCATION','OBSERVED_RESEARCH_USE','target_markets','TWIST2实际使用Unitree G1开展遥操作和数据采集研究','第三方科研使用；不推断厂商主要目标市场或收入。')
scene('CN_UNITREE','FIELD_INSPECTION','BACKGROUND_DATE_UNKNOWN','target_markets__2','现行变电站、矿井、炼化与城市基础设施巡检页','无日期，不用于观察时点主比较。')
scene('CN_XSQUARE','HEALTHCARE_CARE','OBSERVED_USE','product_lines|deployment_status_actual','0755在深圳具名养老机构上岗','该场景具名，其他场景分别处理。')
scene('CN_XSQUARE','LOGISTICS','OBSERVED_USE','deployment_status_actual','物流真实场景运行数月','客户未具名，公司运行陈述；不记外部具名客户确认。')
scene('CN_XSQUARE','MANUFACTURING','CURRENT_TARGET','target_markets','自述逐步进入工业制造','没有据此确认具名工厂。')
scene('CN_XSQUARE','HOME','CURRENT_TARGET','target_markets','自述逐步进入家居','无具名家庭现场，不作已交付家庭。')
scene('US_AGILITY','LOGISTICS','OBSERVED_USE','deployment_status_actual','GXO SPANX仓库料箱搬运','客户商业部署确认。')
scene('US_AMAZON_FTR','UNSPECIFIED','TEAM_BACKGROUND','target_markets','现行团队页面向Amazon内部运营研究','页面无日期，且不映射成对外商业行业。')
for group,claim in [('MANUFACTURING','初始制造业'),('LOGISTICS','初始仓储物流')]:scene('US_APPTRONIK',group,'CURRENT_TARGET','target_markets',claim,'后续计划在同一条事实中另行分离。')
for group in ['RETAIL_SERVICE','HEALTHCARE_CARE','HOME']:scene('US_APPTRONIK',group,'FUTURE_PLAN','target_markets','后续扩展至零售、医疗并最终家庭','不能加入当前相应场景。')
scene('US_BOSTON_DYNAMICS','LOGISTICS','OBSERVED_USE','deployment_status_actual','DHL Stretch商业使用','限Stretch，不外推Atlas。')
scene('US_BOSTON_DYNAMICS','MANUFACTURING','CURRENT_TARGET','target_markets|product_lines','Atlas工业物料搬运与企业工作流','当前产品定位，不以Stretch运行替代Atlas运行。')
scene('US_DEXTERITY','LOGISTICS','CURRENT_OFFER','product_lines|delivery_form|target_markets','Mech卡车装载、码垛、拣选产品应用','工业场地中的物流任务，不据工业一词加入制造工艺组。')
scene('US_DILIGENT','HEALTHCARE_CARE','OBSERVED_USE','deployment_status_actual|target_markets','Moxi院内样本等物资运送','医疗场所物流任务，与康复治疗/养老不同。')
scene('US_FIELD_AI','FIELD_INSPECTION','CURRENT_TARGET','target_markets','建筑、能源与巡检','公司自述定位。')
scene('US_FIELD_AI','MANUFACTURING','CURRENT_TARGET','target_markets','制造','未据总体部署自述确立具体制造工序。')
scene('US_FIELD_AI','LOGISTICS','CURRENT_TARGET','target_markets','城市配送','与仓库作业的任务差别在窄口径中保留。')
scene('US_FIGURE','MANUFACTURING','OBSERVED_USE','deployment_status_actual','BMW Figure02车身车间运行','限历史F02，F03到厂不是已运行。')
scene('US_FIGURE','HOME','CURRENT_TARGET','product_lines|target_markets','Figure03设计面向家庭使用','非家庭交付确认。')
scene('US_NIMBLE','LOGISTICS','OBSERVED_USE','deployment_status_actual|delivery_form','自有机器人履单中心启用并提供3PL','运营服务，非外售机器人。')
scene('US_PHYSICAL_INTELLIGENCE','HOME','DEMONSTRATED_TASK','target_markets','洗衣、叠衣、做咖啡、装袋研究演示','任务环境不能当商业家庭定位或付费客户。')
scene('US_PHYSICAL_INTELLIGENCE','UNSPECIFIED','END_USE_UNSPECIFIED','target_markets','未给商业行业清单')
scene('US_PICKLE','LOGISTICS','OBSERVED_USE','deployment_status_actual|target_markets','分拨中心/仓库卡车卸货系统运行','公司运行自述。')
scene('US_SKILD','UNSPECIFIED','END_USE_UNSPECIFIED','target_markets','跨形态控制，没有已确立终端行业清单','机器人形态不是行业。')
dump('scene_classification.json',{'version':'1.0','scenes':scenes,'membership_positive_states':['OBSERVED_USE','OBSERVED_DONATION','OBSERVED_RESEARCH_USE','CURRENT_OFFER','CURRENT_TARGET'],'interpretation':'公司在观察时点与该应用存在明确连接，可来自现行定位或使用；不等于全部已部署或商业主业。不同状态不得合并解释为已交付。','assignments':rows})
q2={
 'version':'1.0','status':'DESIGN_FIXED_BEFORE_GROUP_SKILL_RATE_COMPARISONS','selection_disclosure':'已知Q1职能总量和公司覆盖；已做资料可用性诊断。不是事前注册或盲选；未以业务组/国家技能差距选择。',
 'primary_roles':['RF_ML_AI_ENGINEERING','RF_ROBOTICS_SOFTWARE'],
 'selection_logic':'各取一个学习/模型工程与运行软件/平台锚点，以解释具身系统的软件技术工作组合。二者分别有159/181条、24/23家公司覆盖；优先两个边界可解释且可用资料充分的职能。所有17类均列诊断，其他类不因未入Q2而从Q1/Q3删除。',
 'role_feasibility_gates':{'min_ads':100,'min_companies':18,'min_dimension_source_assessable_share':0.8,'min_companies_with_5_ads':5},
 'gate_note':'本样本的可操作筛选门槛，不是显著性/精度证明，也不唯一决定研究价值。未过时不扩大或混并职能；按锚点减少本轮主题。',
 'primary_ad_rule':'primary_status=CODED，且primary_code为所选具体职能；不展开复合/多方向主类，不重分类。',
 'denominator':{'main':'基础范围为该具体职能中目标维度状态CODED/NOT_MENTIONED/UNMAPPED的广告，保留UNMAPPED；随后逐标签×语境×分支判断解释资格。指标为既有目录标签已记录明示覆盖率，不声称完整能力需求率。','relation_uncertainty':'同广告同标签同指标已有明确正向记录时为PRESENT；否则存在可能影响该指标的未解决关系/语境时为UNKNOWN并退出该指标分母；其余为NO_RECORDED_POSITIVE，不称真实能力需求不存在。不得把关系不明算0，也不整条广告退出所有指标。','source_unassessable':'退出该维度分母，单列；不因技能不足退出技术维度。','unknown_dimension_status':'拒绝未知状态，停止构建。','catalog_sensitivity':'并列仅CODED+NOT_MENTIONED的目录可直接评价子集；不得当作主结果或声称此子集全无目录外内容。','scope':'24家均保留公司点值；主业务比较仅23个整公司主体，FAR单列。'},
 'deduplication_key':['identity_key','dimension','label_code','use','mention_relation','branch_bucket'],
 'branch_buckets':['UNCONDITIONAL','CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','UNRESOLVED'],
 'branch_logic':{'choice_relations':['OR','OR_EQUIVALENT','SOME_OF'],'example_relations':['EXAMPLE'],'unresolved_relations':['UNRESOLVED'],'unconditional_relations':['ITEM','ALL'],'missing_requirement_node':'UNRESOLVED, never unconditional','priority':'任何未解决节点/未知关系优先UNRESOLVED；否则按所有祖先同时判断任选和示例；不限于叶子节点。'},
 'positive_buckets':{'DUTY_OWN_USE':['DUTY_USE','OWN_USE'],'DUTY_OWN_DEVELOP':['DUTY_USE','OWN_DEVELOP'],'REQUIRED':['REQUIRED','EXPERIENCE_REQUIREMENT'],'GENERAL':['GENERAL_REQUIREMENT','EXPERIENCE_REQUIREMENT'],'PREFERRED':['PREFERRED','EXPERIENCE_REQUIREMENT']},
 'separate_not_positive':['BACKGROUND','NEGATED','UNRESOLVED','COLLABORATION_OBJECT','PRODUCT_DEFINITION_OBJECT','PROCUREMENT_OBJECT','RECRUITMENT_OBJECT','TEACHING_OBJECT'],
 'main_plot':'按职责本人使用/本人开发、硬性/一般/优先要求分别展示；要求的UNCONDITIONAL、CHOICE、EXAMPLE、CHOICE_AND_EXAMPLE分开。无条件与任选不能加成同时必须掌握。',
 'display_selection':{'skill_limit':10,'technical_limit':8,'min_distinct_companies':5,'min_distinct_ads':10,'generic_skill_codes_separate':['SK_GENERIC_ML_FRAMEWORK','SK_GENERIC_LANGUAGE','SK_CAD'],'generic_rule':'泛称保留附表与覆盖说明，主技能图使用具体命名工具；不由泛称推断任何具体工具。','rank':['distinct_companies_desc','distinct_ads_desc','label_code_asc'],'rank_scope':'每个已选职能的全部可评价整公司广告合并；使用正向本人职责与要求的标签并集去重，任选/示例可作为明确提及但不当作无条件要求；不读业务组/国家差距。','insufficient':'够条件的标签不足上限时全部展示，不补凑数量；其余完整附表。'},
 'group_display':{'min_positive_companies':3,'min_assessable_role_ads_for_summary':20,'company_small_n':10,'dominant_company_share_warning':0.5,'meaning':'此处positive_companies指分母大于0的公司，不是技能阳性的公司。基础覆盖达门槛仅有条件允许汇总；每个标签×语境×分支须在排除UNKNOWN后再次检查3家公司/20条。任一不足仅公司点值/案例；不构成统计充分性证明。','weighting':['company_equal','ad_weighted'],'zero_role_company':'角色分母为0显示NA，不以0率进入平均','overlap':'场景可多属；重叠公司必须列出，不将场景视为独立互斥样本。'},
 'country_comparison':{'scope':'仅相同供给形态内；每国至少3家该职能可评价公司且20条广告，再标范围/渠道限制。','prohibited':'跨本体模型组全为美国公司，不能据模型组与系统组差异推断国家差异。'},
 'sensitivity_checks':['公司等权/广告加权','逐一剔除公司并记录阈值跌破','剔除内部团队（主比较默认）','剔除已明确多产品公司Fourier/Boston Dynamics','排除归组仅由媒体支持的公司','主分母/目录可直接评价子集','全部场景连接/具名或明确实际使用子集','不将重叠场景当互斥组'],
 'stop_conditions':['输入哈希不匹配','身份重复或孤立标签/关系','不认识的状态或关系类型','归组缺少事实依据','不合时点证据进入当前场景','所选职能不满足已定可行门槛'],
 'stage_c_status':'Rules and diagnostics only; full outcome tables/figures and substantive contrasts are next stage.'
}
dump('q2_rules.json',q2)
print('Authored',len(primary),'company classifications and',len(rows),'scene assertions; Q2 rules recorded.')
