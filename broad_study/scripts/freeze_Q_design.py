from common import *
import math,datetime
# Coarse task strata are descriptive. The raw fine task is retained alongside them.
task_defs={
'RF_MANUFACTURING_QUALITY_SUPPLY':[
('PROCESS_BUILD','生产工艺、装配和原型制造','本人交付制造工艺、实物装配或试制；供应商采购、检验结论和软件测试分列。'),
('HARDWARE_TEST_QUALITY','硬件与整机测试质量','本人交付硬件/整机验证、检验或质量闭环；可复用工具链仍保留原主职能。'),
('SOFTWARE_DATA_TEST','软件和数据测试','软件接口、性能、数据平台测试与质量；不与硬件良率直接比较。'),
('PROCUREMENT_SUPPLY','采购与供应链','寻源、供应商、采购、交付或物流流程；库存实操另列。'),
('MATERIAL_INVENTORY','物料与库存操作','物料准备、库存、搬运及内部交付；不推断采购决策。')],
'RF_HARDWARE_ELECTRICAL':[
('BOARD_CIRCUIT','电路板与器件设计','板卡、PCB、电源和驱动电路；保留具体板卡对象。'),
('FIRMWARE','嵌入式固件与驱动','底层驱动、MCU、RTOS、ISP或电机固件；不等同电路设计。'),
('HARNESS_SYSTEM','电气互连与系统架构','线束、连接器、电气系统架构与接口。'),
('FPGA','FPGA与数字逻辑','可编程逻辑设计、验证及与板卡集成。')],
'RF_ML_AI_ENGINEERING':[
('ROBOT_MODEL','机器人模型与策略','直接训练/优化机器人策略或具身基础模型；保留预训练/后训练等细项。'),
('TRAIN_INFER_INFRA','训练推理基础设施','训练编排、算力性能、部署推理服务；不把所有软件平台算模型研究。'),
('DATA_EVAL_FOR_ML','学习数据与评测管线','服务模型研发的数据/评测工程；按主交付保持既有分类。'),
('OTHER_MODEL','其他模型应用','语音、业务分析等明确模型任务，与机器人动作策略区分。')],
'RF_ROBOTICS_SOFTWARE':[
('ROBOT_RUNTIME','机器人运行软件','中间件、运行时、嵌入式上层、机器人应用与遥操软件；保留子对象。'),
('ROBOT_CLOUD_UI','机器人云端与交互','机器人云平台、控制界面、移动终端与车队服务。'),
('DEV_INFRA','开发与数据平台','通用开发、测试、运维、数据及工程管理系统。'),
('BUSINESS_APP','业务应用系统','支付、身份、履单、CRM等业务系统；不解释为机器人控制栈。'),
('CUSTOMER_INTEGRATION','客户软件集成','客户系统接口与软件集成应用；与内部运行平台分列。')],
'RF_COMMERCIAL_CUSTOMER':[
('SALES','销售与渠道经营','企业/区域/渠道销售、商务拓展及销售支持。'),
('CUSTOMER_SUCCESS','客户成功与用户支持','客户体验、续约、服务运营与用户问题闭环。'),
('MARKETING','品牌营销与传播','市场活动、内容、视频、公关与技术传播。'),
('ECOSYSTEM','开发者与合作生态','开发者社区、伙伴计划和生态经营。'),
('STRATEGY','商业战略分析','市场、竞争、金融与商业策略分析。')],
'RF_CONTROL_PLANNING':[
('LOCOMOTION_WBC','运动与全身控制','腿足运动、平衡和全身控制；不与车队调度合并。'),
('MANIPULATION','机械臂与灵巧手控制','手臂、末端、双臂操作与力控。'),
('NAV_PLANNING','导航与运动规划','单机路径、轨迹或移动操作规划。'),
('FLEET_PLANNING','多机与车队规划','多机器人协调、调度和车队路径。'),
('CONTROL_RUNTIME','控制运行实现','电机固件、嵌入式安全与控制运行基础设施。')],
'RF_CORPORATE_SUPPORT':[
('HR','招聘与人力','人才获取、人员运营、薪酬与组织流程。'),
('FINANCE','财务与资本沟通','会计财税、审计、预算、资本与投资者沟通，保留子类。'),
('LEGAL','法务与治理','合同、公司治理、知识产权与合规。'),
('ADMIN_FACILITIES','行政与设施','办公室、前台、高管支持、物业与楼宇维护。'),
('IT_SECURITY','内部IT与安全','公司信息系统、安全和信息治理。'),
('EDUCATION_POLICY','教育或政策支持','课程教育、政策分析、政府项目及其他专业支持。')],
'RF_DATA_INFRA_OPERATIONS':[
('DATA_PIPELINE','数据平台与管线','数据基础设施、处理、存储和数据集/模型管线。'),
('DATA_OPERATIONS','采集与标注运营','采集场地、班组、质量、流程或自动标注运营。'),
('DATA_PRODUCT','数据产品与策略','数据需求、策略、产品和数据生产规划。'),
('ANALYTICS','统计与业务分析','统计建模、分析服务与业务决策支持。')],
'RF_DEPLOYMENT_FIELD_SERVICE':[
('CUSTOMER_INTEGRATION','客户安装与集成','客户现场安装、调试、集成与技术应用。'),
('ROBOT_SERVICE','机器人维修与服务','机器人故障诊断、修复、保养和客户技术支持。'),
('LAB_DEMO','实验室与演示服务','内部试验设备、研究车队、演示或数据场地保障。'),
('FACILITY','设施维护','仓储或楼宇设施维修；不能算全部机器人维修。'),
('SERVICE_LEADERSHIP','服务运营管理','区域、全球服务及现场运营团队管理。')],
'RF_INDUSTRIAL_EXPERIENCE_DESIGN':[
('INDUSTRIAL_CMF','工业外观与CMF','外观形态、色彩材料、可穿戴工业设计。'),
('DIGITAL_UX','数字界面与交互','机器人/软件界面、设计系统、数字体验原型。'),
('SERVICE_HUMAN_FACTORS','服务体验与人因','服务流程、用户研究、人因与使用概念。'),
('HRI_HARDWARE','人机交互硬件','声音灯光等交互硬件方案与体验。')],
'RF_MECHANICAL_MECHATRONICS':[
('ROBOT_STRUCTURE','机器人结构与机构','机体、底盘、传动与机械架构设计。'),
('ACTUATOR_GEAR','关节与传动部件','关节、减速器、电机机电集成和传动。'),
('COMPONENT_PROCESS','部件设计与制造转化','机械零件、连接器、工艺适配、原型及量产设计。'),
('THERMAL','机械热管理','热结构、载荷与散热设计。'),
('SOFT_GOODS','柔性材料与纺织部件','织物、弹性材料、抓取接触材料设计。')],
'RF_PERCEPTION':[
('OBJECT_VISION','物体与场景视觉','物体识别跟踪、场景理解和学习感知。'),
('LOCALIZATION','定位建图与融合','SLAM、定位、导航状态估计与多传感融合。'),
('RECONSTRUCTION','三维重建表示','几何、点云、神经重建与空间表示。'),
('TACTILE_AUDIO','触觉与音视频交互感知','触觉、力觉、音频或多模态交互感知。')],
'RF_PRODUCT_PROGRAM':[
('ROBOT_PRODUCT','机器人产品定义','本体、导航、自主能力、交互或遥操产品路线图与需求。'),
('SOFTWARE_DATA_PRODUCT','软件与数据产品','内部平台、数据/研究运营、客户体验软件产品。'),
('RND_PROGRAM','研发与量产项目','研发、新品导入、生产运营项目及里程碑。'),
('CUSTOMER_PROGRAM','客户项目交付','客户计划、交付、技术运营与项目协调。'),
('OTHER_DOMAIN','设施或教育等专项产品','设施施工、课程教育等不同工作对象。')],
'RF_RESEARCH_SCIENCE':[
('ROBOT_LEARNING','机器人学习研究','模型/策略、灵巧操作、全身控制、基础模型或世界模型研究。'),
('HARDWARE_NUMERICAL','硬件与数值方法研究','结构拓扑、材料、传感器、数值算法等研究。'),
('MULTIAREA','多方向研究','原文允许多个研究方向或对象无法进一步确定；不强分单一方向。')],
'RF_ROBOT_OPERATIONS':[
('DATA_DEMONSTRATION','示范与动作数据采集','本人遥操、穿戴动捕或示教采集。'),
('CUSTOMER_OPERATION','客户现场机器人运行','本人运行机器人、异常处理及服务支持。'),
('HOSPITAL_OPERATION','医院机器人服务','临床环境机器人监控、服务沟通与支持。'),
('FULFILMENT_OPERATION','履单机器人运行','仓内车队监控、故障恢复及吞吐保障。'),
('MIXED_DATA_CUSTOMER','采集和客户运行双任务','原文明示两者均承担；不强行归入单一比较层。')],
'RF_SIMULATION_EVALUATION':[
('SIM_PLATFORM','仿真环境与平台','物理引擎、场景、资产、导航仿真与平台研发。'),
('MODEL_EVAL','模型评测','算法复现、模型基准与真机验证方法。'),
('HARDWARE_TEST_INFRA','硬件产测与表征工具链','电路/执行器/整机测试工具、测量设备和产测平台。'),
('CALIBRATION','标定与系统辨识工具链','标定、辨识、HIL及校准平台；具体对象保留。'),
('SOFTWARE_TEST_INFRA','软件测试与诊断基础设施','测试框架、自动化、CI、故障诊断与回归工具。'),
('SYSTEM_EVAL','整机评价体系','整机性能、竞品及用户场景评价方法。')],
'RF_SYSTEMS_ENGINEERING_INTEGRATION':[
('WHOLE_ROBOT','整机架构与集成','跨机械、电气、软件的整机系统架构和集成。'),
('SUBSYSTEM','子系统跨域集成','关节、传感、计算、电源、声学或灵巧手系统集成。'),
('FUNCTIONAL_SAFETY','安全架构与验证','产品安全/功能安全要求、架构和验证。'),
('DIAGNOSTICS','系统诊断与持续运行','跨域故障定位、可靠性与运行诊断体系。'),
('TECHNICAL_LEADERSHIP','跨产品研发统筹','多产品、多专业技术决策与研发规范。')]}
assert set(task_defs)==set(CONCRETE)
save_json('configs/Q_task_strata_v2.json',dict(version='Q2-v2.1',assignment='研究者全文判断；可多值，主任务无法确定记UNRESOLVED。不可由关键词或原主职能自动赋任务。',comparison='主结果按职能描述组合；同任务子层另算，不把宽泛子层等同完全相同工作，细任务和对象均保留。',new_tasks='目录未覆盖记OTHER并留证；统一变更后回看受影响全部广告。',roles={f:[dict(task_code=c,name=n,definition=d) for c,n,d in rows] for f,rows in task_defs.items()}))
# Fixed focus is the within-role task contrast across all observed companies.
# Company points are never selected because of the size or direction of a skill gap.
focus=[]
for f,defs in task_defs.items():
 kk=[k for k,j in J.items() if role(j)==f and j['company_id'] in WHOLE];counts=Counter(J[k]['company_id'] for k in kk)
 focus.append(dict(role=f,role_name=RN[f],focus_task=defs[0][0],comparison_design='所有观察公司在该职能与预设任务层的点值；组汇总逐格3家公司/20条。任务资格不满足时保留NA，不替换为结果更大的任务。',context_display='14格拆分；职责示例/条件与背景另列',prominent_companies_by_coverage=js(sorted(counts,key=lambda c:(-counts[c],c))[:3]),selection_basis='仅全职能广告覆盖排序，未查看新技能公司差异',role_ads=len(kk),qc_minimum=max(10,math.ceil(sum(role(j)==f for j in jobs)*.2))))
dump('tables/Q1_prefixed_comparison_plan.csv',focus)
# Snapshot the initial candidate version; changes after this point require an amendment.
p=ROOT/'configs/Q_catalog_v2_candidate.json';cat=json.loads(p.read_text(encoding='utf-8'))
assert len(cat['labels'])==354 and len({d['code'] for d in cat['labels']})==354
notes=json.loads((ROOT/'configs/Q_calibration_notes.json').read_text(encoding='utf-8'))
assert set(notes['roles'])==set(CONCRETE)
assert all(len(v['task_assignments'])==20 for v in notes['roles'].values())
bridge=json.loads((ROOT/'verification/Q_v1_bridge.json').read_text(encoding='utf-8'));assert bridge['status']=='PASS'
cat['status']='FROZEN_CANDIDATE_BEFORE_FULL_CODING'
cat['frozen_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
cat['selection_disclosure']='已知旧Q1/Q2结果、全部候选原词和340条校准原文；不是盲选或事前注册。尚未计算v2公司技能差异。'
cat['coverage_limitation']='有限目录；目录外候选保留并逐全文判定影响，不能宣称覆盖全部技能。'
save_json('configs/Q_catalog_v2_frozen.json',cat)
files=['configs/Q_catalog_v2_frozen.json','configs/Q_coding_rules_v2.json','configs/Q_task_strata_v2.json','configs/Q_baseline_catalog_reference.json','tables/Q1_prefixed_comparison_plan.csv','tables/Q2_catalog_bridge.csv','tables/Q2_role_catalog.csv','tables/Q_v1_fixed_display_items.csv']
save_json('configs/Q_design_lock_v2.json',dict(version='Q2-v2.1',files=[dict(path=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()) for p in files]))
report="""# Q2全17职能目录与桥接：M4规则固定
署名：Astra。2026-09-16。状态：候选目录已冻结；全量编码与结果尚未完成。

## 已实际执行

- 全17职能每类20条、共340条公司轮转校准；完整职责和要求已读。另核对full_description，53组独有补充段落已读，其他相同段落以原文引用。重复显示压缩不参与语义判断。
- 固定17类任务分层、354项有限测量目录、ROLE_LABEL_COUNT个职能与条目组合。旧85技能和25技术概念定义参考保留，其中3个旧技能在当前具体职能没有候选，不强行配给职能。
- 新增244项，分为工具/仪器/协议、工程方法、技术概念、工程标准、专业能力、专业资格和操作方法；泛称另列。复合方法类别保留具体原词，不能解释为掌握其中所有方法。
- 全部原词候选池23,426条，其中认可标签18,496条、目录外候选4,930条。1,922种目录外原词完成词面普查；MATCH_COUNT条有候选目录匹配、OUTSIDE_COUNT条仍在初版目录之外。这只是词面库存，不是语义编码或正例。
- 研究书所称662条指skills维度目录外提及且原技能CODED的广告；任意维度目录外提及交集为828条，二者口径不同。
- 从锁定标签与要求树单独重算5,547条旧Q2语义记录和38,640个公司语境格，全部一致。固定ML的10技能/8技术、软件的9技能/8技术，共35个职能标签对照项。

## 执行规则

14种原语境分支逐值继承。新职责中的示例、任选及条件执行单列，不能冒充无条件职责；新旧差异由完整桥接解释。新增条目在全文审读后才能判P/Z/U/NA。词面命中、候选映射和继承标签均不是本轮语义复核完成证明。

同一主职能内部先展示任务组合；相同任务层另算，保留对象与细任务。每类的首个预设任务层作为固定重点，所有公司均保留点值；突出显示公司仅按全职能覆盖排序，不能按差异大小挑选。无法满足任务比较条件时保留NA，不临时替换出“好看”差异。

每个公司与标签语境格保留P/U/B/N、Z、NA、来源排除。公司N少于10提示小样本；每组至少3家N>0公司、20条可解释广告才许可探索性汇总。新主图每类型至多8项，至少5家阳性公司与10条阳性广告，按公司覆盖、广告覆盖、代码固定排序；示例/任选仅可进入选项覆盖，图内继续拆分。

## 下一步与限制

M5须对1,576条具体职能广告完成全部适用内容编码、目录外影响审查、分层比较、敏感性与第二遍核对。340条校准可复用已阅读的原文，但仍须逐提及审查新标签与语境，不能直接声称340条正式编码已完成。研究者第二遍核对署名Astra，不称外部独立双盲复核。

原认可主职能、历史标签、原研究库均不改。当前冻结文件及哈希见configs/Q_design_lock_v2.json。若发现目录边界系统性问题，先登记修订与受影响范围，再统一复查，不静默修改已冻结版本。
"""
lex=read(ROOT/'tables/Q_lexical_catalog_candidates.csv')
report=report.replace('ROLE_LABEL_COUNT',str(len(read(ROOT/'tables/Q2_role_catalog.csv')))).replace('MATCH_COUNT',str(sum(r['status']=='LEXICAL_CANDIDATES_ONLY' for r in lex))).replace('OUTSIDE_COUNT',str(sum(r['status']=='OUTSIDE_INITIAL_CATALOG_REQUIRES_CONTEXT_REVIEW' for r in lex)))
report+='\n版本v2.1澄清：对全部原文另做词面覆盖检查，并使用空surface历史记录的quote建立候选；避免已有提及池缺字段导致整职能漏纳条目。该步骤不自动生成正例。v2.0封存在configs/history/Q2_v2.0。\n'
(ROOT/'reports/Q_M4_目录与桥接报告_Astra.md').write_text(report,encoding='utf-8')
print('M4 design frozen:',len(cat['labels']),'labels;',sum(len(x) for x in task_defs.values()),'task strata;',sum(r['qc_minimum'] for r in focus),'minimum second-pass ads')
