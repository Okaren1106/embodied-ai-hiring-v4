# 当前进度：24家公司分类与Q2规则已固定，可进入正式结果分析

更新：2026-09-15。两份必读同步改写。用户要求亲自按顺序完成业务分类、覆盖诊断和Q2规则，本轮已完成，未委派代理。

## 最新分析规则与分类包

`reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/`

- [执行报告](<D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/REPORT.md>)；[分类总览](<D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/index.html>)。
- [24家公司逐项分类](<D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/COMPANY_CLASSIFICATION.md>)；[取舍讨论](<D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/DECISION_MEMO.md>)。
- [Q2规则正文](<D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/Q2_RULES.md>)；[比较许可](<D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/comparison_registry.json>)；[复算说明](<D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/analysis_rules_v1/run_20260915T085828Z/README.md>)。
- [公司事实与证据包](<D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/stage_b_supplemented/run_20260915T073556Z/README.md>)仍为证据底稿；本轮新增的是分析分类，不改写公司事实或广告。

## 已固定的分类

18家公司归为整机/机器人系统产品，3家跨本体模型/软件（Field AI、Physical Intelligence、Skild）；帕西尼触觉部件与系统组合、Nimble自营机器人履单服务分别单列，FAR按内部团队范围单列。供给形态不代表唯一收入主业或付费成熟度；系统组允许模型并行。

51条场景判断组成24×7状态矩阵，区分现行定位/提供、实际使用、捐赠、第三方科研使用、演示、未来目标和无日期背景。当前场景连接：制造10、物流11、商业服务4、巡检3、医疗照护3、家庭3、科研教育4；可以重叠，不是已交付公司数。制造/物流/商业服务为重叠描述分面，其他四类以任务案例展示；未知不当作反面组。

## Q2选择与分母

选定ML/AI工程与软件/平台：全样本159/181条，整公司主比较156/180条，FAR的3/1条保留团队点值。其他17类全量覆盖诊断保留；制造/质量/供应链和硬件也有可用数据，未入Q2是两职能研究范围取舍，不是数据不足。

主展示具体技能按整公司总体覆盖固定选择：ML/AI工程10项，软件/平台9项，各8项技术概念。泛称单列，不按国家/业务组差距选标签。UNMAPPED保留基础分母；逐标签×语境×分支判断PRESENT/UNKNOWN/NO_RECORDED_POSITIVE，UNKNOWN退出对应指标分母但保留广告其他可解释记录，不记为无要求。

模型组ML/AI仅17条，只作公司点值；软件/平台38条中Field AI占23条，可做附条件探索性汇总，必须披露集中和逐一剔除情况。模型组三家全为美国公司，禁止将供给组差异当国家效应。所有标签图格在未知排除后再核对≥3家公司且≥20条广告；每公司少于10条提示小样本。阈值是展示规则，不是统计充分性保证。

## 验证及接续

作者自验59/59，真实Chrome10/10且截图目视通过；隔离复算22份派生表/说明逐字节一致，4项发布保护故障通过。输入封存129文件（17份表/说明＋112份证据资产），设计锁9项；3309份保护原件哈希不变。原1654广告、研究库、r3、measurement规则与旧B包未改。

规则和分类已完成，不冒称独立验收或严格事前注册：编制时已知Q1总量和覆盖，尚未计算业务组技能率差。下一步直接按本版规则生成C阶段Q1—Q3正式结果、图表和分母表，随后做D阶段公司事实解释与敏感性检查；不再将“选择业务组/职能”列为待办，不凭结果大小更换组或技能。

## 前序B轮结果

`stage_b_evidence_integrated/run_20260915T064258Z`修复及16卡入表已独立验收通过（36项原条件＋20项数据审计）；随后按用户授权补入7家公司9证据并补傅利叶日期，接续事实包为`stage_b_supplemented/run_20260915T073556Z`，680事实、111证据（96个不同URL）、457关系、24资本事件、307原缺口。该包补充验证53/53、故障22/22、Chrome22/22、专项18/18、原条件36/36，旧包不回写。

无日期页、Moz1首发月份冲突、付款与融资非关键缺口仍保留原有限用途；阶段A、人工复核和技能用途专项继续沿用既定收口状态。

2026-09-14 阶段A已完成二次独立验收，正式接续包为 `reports/2026-09-14_company_data_analysis/stage_a_r3/`。r2的五项数据返修均已核实；本轮又复现并修复封存元数据哈希未校验、复算入口依赖现场文件、manifest记录自身旧大小的问题，并加入全部验证通过才发布新目录、拒绝覆盖已有目录的保护。r3内置检查1349通过、独立数据核验32通过、完整入口隔离与故障测试23通过，均0失败。独立核验逐对象比较1654条研究库快照，重算528格T2和88行聚合；禁止读取现场项目文件后，整包仍可复算。7类锁故障全部拒绝；验证失败不发布，历史目录不覆盖。1349与r2原1353的差异来自5项现场检查改由独立原件保护、入口增加1项封存一致性检查，不是统计检查回退。

原 `stage_a/`、送审 `stage_a_r2/`、研究库、measurement规则和冻结包共139个受保护文件哈希未变；本轮没有重分类、回填目录或联网补查。r3的快照、岗位表、全部CSV、关系和追溯数据与r2逐字节一致，T2原哈希仍为 `231179cb…` / `04590caf…`。公司表仍为24行主表、214条台账/状态/边界记录、307条待查项；214不等于已确认外部事实，307不等于查后未找到。职责节点87个已映射，T1保留继承主体与来源范围；要求强度/承担关系先筛选再作广告—标签去重，长表未删行。完整证据及复验方法见 `reports/2026-09-14_company_data_analysis/stage_a_r2_acceptance/REPORT.md`。阶段A已经收口；阶段B的启动范围和当前执行状态以上述最新安排为准。

技能用途专项已按用户决定收口。已有118条技能UNMAPPED广告的276种原始写法、59组用途说明与证据保留，详见 `reports/2026-09-14_unmapped_skill_research/REPORT.md`。既有“能确定是工具就可以直接加入”的授权保持原意，85项不是固定上限；本次收口不代表已发布扩充目录或回填标签。目录外提及、来源不足以及背景、任选、示例、一般要求、硬性要求的区别写入分析口径。另662条CODED广告的目录外提及未被118条专项覆盖，不宣称已全部处理；这些目录工作不再作为当前正式分析的开工前置事项。

2026-09-14 用户已明确要求“人工复核标记完成”，当前24家公司1654条认可研究的人工复核状态为完成，依据记录见 `research/human_review_completion_2026-09-14.json`。人工复核不再列为正式分析的前置待办，不新建抽检或重分类任务。历史冻结包与研究库导入记录的 `human_validated=false` 保留原始版本含义；当前完成状态以用户确认及记录为准，不补造逐条审核提交或独立双盲程序。后续执行书已完成评估并由本轮阶段切换承接，按修订后的“公司背景补缺＋正式结果分析”推进；评估依据见 `reports/2026-09-14_analysis_plan_assessment/REPORT.md`，当前执行顺序以上述新阶段安排为准。

2026-09-14 已按用户要求启动最新工作台（8502研究端、8503人工端，进程36428，使用--no-seed）。启动前两端均无运行服务、没有活动分类批次。实测1654条认可参考查询与CSV导出、E0107双岗位、详情修订版本令牌、1648条分类输入及旧引擎不兼容保护，8503拒绝研究管理API。研究库哈希和0条主线修订保持不变，未重跑自动分类、未新建审核任务、周采关闭。项目研究进度报告已完成：reports/2026-09-14_project_progress_report.md，重点说明研究目的、公司工作与技术组合主线、24家数据/1654条参考/四维规则成果、初步描述统计及尚待完成的正式分析。支持统计与运行证据位于reports/2026-09-14_project_progress/。此前研究库迁移修复已验收通过，默认481项工程测试全部通过；自动分类器仍未适配v0.7.5新结构类。

**当前唯一认可参考仍为24家公司1654条**。冻结包 `outputs/reference-expansion-2026-09-11/accepted-reference1654-v1-2026-09-14/`，指针 `outputs/reference-expansion-2026-09-11/current_reference.json`。当前可编辑研究状态以 `data/research/research.sqlite3` 为准；指针同时标明冻结包职责与研究库职责，不是两套可独立改写的当前答案。1606明确（1576原17类＋11多方向＋19复合）、15歧义、2未映射、31来源不足。历史导入数据全部 USER_ACCEPTED_REFERENCE、user_accepted=true、human_validated=false，保留原始AI判读与认可来源；当前人工复核已由用户本轮确认为完成，另存项目状态记录，不把历史整包认可追认成当时已有逐条审核提交。

1654 认可参考与 1648 采集基线是不同观察范围，已分别保存数据集身份、观察时间和来源关系。工作台正式分类页仍以 1648 冻结基线为自动分类输入；同岗位但正文版本不同时只提示、不对齐删改。E0107 阅读编号对应两条不同广告身份，研究库同时保存，不以 E/N/标题作唯一键。

主库与工作台库分开写入。清理或重建 `data/interim/workbench/` 不影响研究库。开发测试使用隔离临时库。主线修改必须走研究修订接口并记录版本与原因。自动分类器仍绑定 v0.7.4，存储升级不等于已支持 v0.7.5 新结构类。

导入核验：1654条完整；状态/主职能/公司汇总与冻结包一致；CSV 逐行与冻结 `reference1654.csv` 一致；重复导入不增记录；冻结包 manifest/jsonl/csv 与 1648 基线 manifest 哈希未变。用法：`data/research/README.md`。实施报告：`reports/2026-09-14_research_store/REPORT.md`。

此前同日已验收结构迁移修复并发布1654统一包；旧610/1044分包入口仍为 SUPERSEDED_BY_UNIFIED_REFERENCE，只作追溯。该合包事实未因本次存储升级而改判。

2026-09-14 完成40家池外待选扫描，并按用户点名补核大厂具身团队。随后把40池剩余16家与这些待选公司/团队统一做了接入可能性核验：现在可接入者以美国 Ashby 独立板（Cobot、Standard Bots、Persona、Sunday、Dyna、Weave）和优必选自有北森站为主；星动纪元飞书板用历史独立浏览器直连打开，当前 19 岗且详情 ID 可核；Tesla / NVIDIA / OpenAI / 小米 / 小鹏须先冻结切开规则；魔法原子今日仍为追觅租户；Covariant 不宜再当在营公司接入。完整判断见 `reports/2026-09-14_onboarding_feasibility/REPORT.md`。正式24家1648条基线、周采关闭、1044条AI参考冻结均未改。没有写入 `company_landscape.csv`，没有采集广告。

用户点名核验：北京人形、Tesla Optimus、NVIDIA Robotics 已在40家未接入；章鱼动力、黎曼动力为池外新独立 CORE；小鹏/小米/理想/字节 Seed、OpenAI Robotics、DeepMind、Meta、腾讯 Robotics X 按可切团队口径待选。完整名单见 `reports/2026-09-14_new_company_candidates/REPORT.md`。未授权接入或采集。

同日另完成10家美国具身/人形公司官方招聘源实测核验（1X、Sanctuary AI、Neura Robotics、Figure、Apptronik、Agility Robotics、Boston Dynamics、K-Scale Labs、Foundation、Dexterity），含 ATS 类型、岗位数、稳定ID与发布日期可达性、采集难度分级。要点：K-Scale 实体已死（域名不可解析）；1X 站点实为 San Carlos 且走 Ashby(87)；Boston Dynamics 用 Workday 但列表 API 实测 500，官方岗位总数 unverified；Neura 用 Talent's Connect + Ashby 跳转，sitemap 247 条。完整表见 `reports/official-careers-board-verification-2026-09-14.md`。未写入基线、未采集广告。

同日完成国内接入通道实测复核，**推翻三条此前的"无公开源"判定**：(1) 北森 `zhiye.com` 公开 API `POST https://<sub>.zhiye.com/api/JobAd/GetJobAdPageList` 直接返回完整 JD，实测 10 个租户可用（ubtrobot 117、dobot 164、paxini 124、unitree 83、magiclab 73、galaxea 44、roborock 43、siasun 37、jaka 22），字段含稳定 `JobAdId`、`Duty`、`Require`、`Count`；**注意 `PostDate` 实测恒为 `0001-01-01T00:00:00`，日期不可用，纵向须用 `first_seen`**；租户不存在时响应恒为 159 字节，可作判定规则。据此优必选（过去判 POOR）、越疆、魔法原子从"不可采"变为可接入。(2) 众擎 EngineAI 找到官方飞书板 `dx3a2bminsq.jobs.feishu.cn`（由官网 career.html 提取），过去"ERR_CONNECTION_CLOSED 无 JD 层"的判定作废。(3) 加速进化 Booster 官网静态 HTML 直接嵌入飞书板 `booster.jobs.feishu.cn`。另有新发现：小米 `xiaomi.jobs.f.mioffice.cn`、理想 `li.jobs.feishu.cn` 均为飞书板，列表页 curl 实测 200，且都支持 `?keywords=` 过滤——理想该过滤实测 45 条且职位名带【人形机器人】前缀，是边界隔离最干净的大厂样本。**方法教训：直连失败不等于站点不可采。** 飞书板与小米站用 .NET `Invoke-WebRequest` 全部报"基础连接已经关闭"，换 `curl.exe` 全部 200（本机 TLS 指纹差异，非站点封锁）；对理想/小米/智元/众擎四家实测静态 HTML 中详情 ID 均为 0，即飞书板职位完全依赖前端渲染，任何基于静态抓取的判定都会误判为"零岗位"。本轮 `agent-browser` 渲染通道连续三次超时，未能在本环境复现渲染级证据（项目有 5 家飞书板成功采集的历史证据，属本环境异常）。交付见 `交付/具身智能公司接入调研-2026-09-14.md` 与 `交付/具身智能接入候选清单-2026-09-14.csv`。未改基线、未采集广告、未写 `company_landscape.csv`。

同日再完成美国具身公司**候选池扩展**：8家未接入公司逐一核验，并新增约45家候选（人形、机器人基础模型、仓储物流、垂直部署、国防、大厂团队各路）。结论：8家中仅 Cobot（Ashby `cobot`）、Standard Bots（Ashby `standardbots`）、Ambi（Ashby `ambirobotics`，posting-api 401 需前端渲染）可机器采集；Chef 已迁 Gem（无公开API）；Tesla 全路径 Akamai 403、NVIDIA 为 Workday SPA，二者均为 HARD 且团队边界风险极高；Covariant 站点已无任何 career 路径（2024 Amazon 人才+授权交易后的结构性断点）；Robust AI 无任何可达 ATS 板。已确认不可作在营公司采样：Bossa Nova、Rapid Robotics（2026-02 英国实体解散）、FarmWise、Monarch Tractor（2026-04 被 Caterpillar 收购）、Fox Robotics（2026-02 被 Symbotic 收购）、K-Scale、Kindred（并入 Ocado）；Diligent 已为 Serve Robotics 子公司。采集规范更正：`jobs.ashbyhq.com/<任意串>` 恒返回 200，板存在性只能用 `api.ashbyhq.com/posting-api/job-board/<slug>` 判定；`boards-api.eu.greenhouse.io` 无 DNS 记录，EU 板只能抓前端 HTML；Greenhouse API 仍输出旧域 deep link，应以 `gh_jid` 归一；日期字段为 Greenhouse `first_published`、Ashby `publishedAt`、Lever `createdAt`（epoch ms）。完整表、A/B 分组与逐条验证记录见 `reports/2026_us_embodied_ai_candidate_expansion.md`。未改基线、未采集广告、未写 `company_landscape.csv`。

## 当前工作边界

公司接入阶段已完成，24家公司1648条基线冻结，周采保持关闭。用户2026-09-12已授权对新增16家公司1044条进行四维AI参考分类，并明确只使用Astra子代理。六名gpt-6-astra代理依据冻结v0.7.4逐条判读，主助手统一复核；该参考分类阶段未运行现行自动分类器。2026-09-14用户另授权发布职责结构规则及契约校验，随后完成结构适用性审核并授权应用。早先16条Sol试判因技术要求系统性漏标未达完整性门槛，已由Astra逐条重审并经主助手裁决；Sol原稿仅留作试判质量证据。

新增1044条四维参考已完成、冻结并经用户2026-09-14认可。52批全部收齐、复核完毕，子代理均已结束。该来源组在已合入统一包的修订快照中为1001条CODED、13条AMBIGUOUS、2条UNMAPPED、28条SOURCE_UNASSESSABLE，今后使用1654统一入口。主助手对全部1044条逐条检查过主次职能核心证据和四维标签；按问题深入阅读，不声称全文深读每一条全部证据。初始复核含113条全文四维细读（其中12条亲自判读）、304条全文主职能重点复核及四维筛查，其余详见qa/final_parent_review_scope.json；68条跨批修订由主助手亲自裁决，已计入上述1044条。

中间复审应用（2026-09-14 v2）：用户当时要求“应用”，将傅利叶N0459/N0474、逐际N0577的主职能改为歧义；该授权当时不将1044条全部标成用户认可。v2现为历史快照。随后v0.7.5规则发布及结构审核建议30条迁移；现已按Astra结果应用，N0577改复合职能，N0459/N0474仍歧义。原final/、final-v2-2026-09-14/与reassessment-2026-09-14/保留历史证据。

当前职责结构规则（measurement-v0.7.5，2026-09-14）：保留原17类作为具体职能组成；分别表达单一主导职能、复合职能（本人明确同时承担多项独立交付且无法确定单一主导）、多方向招聘（招聘方向或对应职责明确可任选）。复合展示为“A × B”，任选展示为“A 或 B”；各组成/分支保存职能、可见的具体职责和原文证据，不把目录定义补写成广告职责。仅知识技能或工具任选不能证明岗位方向任选；只有标题或关系不清仍保留歧义。共同职责与任选分支并存时保留“A ×（B 或 C）”等原文关系，不强行扁平化。每条广告总量仍计1，方向提及可另统计但不可相加当人数，也不推断各方向均实际招聘。本版主类为17个具体职能＋2个结构类别，次职能仍为原17类；两个新类必须提供role_structure关系树。正式规则见docs/MEASUREMENT_RULES_V0.7.5.md。

研究参考现统一使用`outputs/reference-expansion-2026-09-11/accepted-reference1654-v1-2026-09-14/`。原新增1044目录中的v2/v3/v4及current_reference.json保留来源链，旧入口已标为被统一包替代。当前统一包48条关注记录由15歧义＋2未覆盖＋31来源不足组成；不能把原1044的43条关注当作全项目总数。

用户认可610条参考并另授权过工作台升级；v0.7.9是上次已完成验收的发布，当前源码有未完成验收的v0.7.10修改。新增岗位参考分类已结束；职责结构规则、校验和30条参考迁移已应用，未升级自动识别算法。此前测试精简和15个GitHub工程Skills选型均已完成，历史报告分别见reports/test-suite-cleanup-2026-09-12/REPORT.md、reports/2026-09-12_coding_skills_project_selection.md。未安装Skill或第三方工具。

测试由521项精简为500项，最终完整运行500通过、0失败/错误/跳过，27.329秒。默认455项，另45项旧研究/原型用--include-legacy选入；67项早期测试整理为54项，其中9项数据保护继续默认运行。删除4项低价值检查、合并17次重复执行；35条结构复核的身份/哈希与真实提交保护保留。报告：reports/test-suite-cleanup-2026-09-12/REPORT.md；逐条去向：legacy-decisions.csv。114份生产源码/配置和30份保护资料哈希未变。

v0.7.10既有610回放主类一致354条，但相对v0.7.9有8条退步，且E0051歧义被赋类；本轮未修复这些分类问题。下一步如继续分类器开发，须加入逐条回归门槛，不能把500项测试通过当作分类质量已验收。

本次规则发布验证（2026-09-14）：默认测试471通过、0失败/错误/跳过，29.890秒，含16个新结构契约用例；旧引擎功能检查绑定其v0.7.4规则，另测当前规则下阻止未适配引擎启动。37份旧规则、冻结参考、基线与配置保护文件哈希一致。未整体复核或重新分类610/1044，未修改正式数据库；测试通过只证明本轮工程契约检查，不代表分类准确率。验证记录：reports/2026-09-14_role_structure_rules/verification.json。

## 当前研究数据

正式基线 MERGED_24_COMPANIES_2026-09-11：24家公司，中国12家964条、美国12家684条，共1648条广告。原八家最近成功观察604条（2026-09-07）＋新增十六家1044条（2026-09-11）；保留各自真实日期，不当作同一时刻普查。1642条正文非空、6条为空；另有云深处WM正文疑似截尾待查。

基线文件 outputs/reference-expansion-2026-09-11/merged-baseline-2026-09-11/records.jsonl；jobs.csv可直接查看；manifest.json记录哈希。工作台 configs/workbench.yaml 的 baseline_snapshot 指向此冻结基线。latest视图不再重复列出同一批资料。旧candidate_path和configs/baseline_freeze.yaml仍描述历史610条，保留用于旧任务与研究追溯，不是当前基线入口。

主线认可参考的当前可编辑状态在 `data/research/research.sqlite3`。冻结包与指针见上文；Excel/CSV 仍作查看导出。DuckDB 采集观察与历史研究复核库未搬迁，仍按原路径关联使用。工作台 `classification.sqlite3` / `reviews.sqlite3` 只保存自动预测、实验批次和人工审核任务，不是1654认可答案的写入入口。

新增中国八家：银河通用184、星尘智能51、帕西尼125、智元83、傅利叶42、云深处38、逐际动力92、星海图44。美国八家：Skild62、Field AI131、Dexterity31、Diligent11、Nimble34、Pickle13、Amazon FAR24、Boston Dynamics79。魔法原子、优必选材料仅备选，未混入正式基线。乐聚未取得可核验当前母公司广告，不当作零招聘。

原八家为CN_UNITREE、CN_SPIRITAI、CN_XSQUARE、CN_NOETIX、US_FIGURE、US_AGILITY、US_APPTRONIK、US_PHYSICAL_INTELLIGENCE。CN_XSQUARE是自变量X Square；本轮新增CN_GALAXEA才是星海图，不得混同。1X／NEURA仍只是历史诊断材料。

## 分类状态与报告

当前项目统一认可参考：研究库 `data/research/research.sqlite3` 为当前可编辑入口；冻结包 `outputs/reference-expansion-2026-09-11/accepted-reference1654-v1-2026-09-14/` 为归档。工作台「认可参考」页走研究库；「正式分类」页对 1648 基线跑自动预测并只读对比认可参考。原610的认可及修订身份可从origin_reference追溯；原1044的整包认可也保留，不声称用户逐条人工复核。

两项已确认修订：自变量“信息化与安全总监”、Figure“Technical Program Manager, Security & Privacy”主职能均改公司支持；Agility Robot Operator II维持制造质量供应。仿真评测在参考表展示为“仿真、评测与测量工具链”。参考包保持不变；在用户随后授权下，安全治理边界、测试执行说明及展示名称已另版发布为measurement-v0.7.4，不覆盖第一轮冻结参考或旧规则。

统一参考中原610来源的千寻导航算法工程师（VLN/规划/SLAM，E0051）已为多方向招聘；宇树机电全栈工程师（E0104）、自变量机器人全栈工程师（E0144）仍为AMBIGUOUS。来源不足为自变量两条数据采集员、PI Research Internships，需要补正文；当前无阻塞参考发布的额外人工裁决。

整体报告 reports/2026-09-11_merged_baseline_and_classification_report.md。原1214条观察（610＋604）已完成AI四维参考及第一轮工作台比较；参考先冻结，之后运行代码。689份全文阅读包保留1195个精确版本及全部观察身份。第一轮为AI_REFERENCE；本次用户抽查认可另存为当前参考，不把一致率解释为准确率。

第一轮历史610条比较（尚未采用本次两项修订）：AI参考604明确、3歧义、3来源不足；代码385 CODED、132 FAILED（130规则未覆盖＋2解析异常）、91 UNKNOWN、2 SKIPPED。282条双方同主类、103条已有类但不同、225条代码未给类。主次/技术/技能/活动及完整属性差异见phase2-onboarding/baseline610_all.csv和baseline610_followup.csv。

统一认可包中的新增来源1044条：1001明确、13歧义、2目录未覆盖、28来源不足；28条中只有4条全文为空，其余24条文字不足以确定主职能，Field AI合计占23条。13条歧义按现有正文保留，不因有新结构类而批量改判。正式工作台仍全部NOT_CODED，本轮未运行自动分类或写入正式分类库。新基线中的原604条保留已有373 CODED、137 FAILED、92 UNKNOWN、2 SKIPPED。分类库10批1304条结果、7物化快照；人工3任务2修订0最终提交，未变化。规则升级后原604条在当前分类页显示STALE，旧结果仍在历史；新1044条NOT_CODED。610回放另存开发目录，不写正式库。

## 当前规则与运行入口

当前研究规则measurement-v0.7.5：19个主类展示值（17具体职能＋复合职能／多方向招聘），次职能17类、7可选子类、25技术、85技能、8活动。规则包哈希acf40442760b06231a282064c9059edfe5ec7a46ac59a02692c9d89edc3a7920。旧v0.7.4及更早规则、对应主词表均保留原字节；v0.7.4包哈希仍为c6f5ee6916c8b37afaa1f98b47eaebd850748ffe57c0b62544283da3d0d31cc9。上次验收引擎为local-multidim-v0.7.9。当前目录由measurement_current.yaml统一指向；seed_codebook_path仅核验历史v0.4校准包，保留原路径及任务版本。

研究工作台 http://127.0.0.1:8502/#reference 为认可参考；#classification 为自动分类。人工端8503。自动分类预测写入工作台库，认可参考只读自研究库指定版本。上次v0.7.9发布验收时服务以--no-seed重启。工作区自动分类算法当前为local-multidim-v0.7.10，仍绑定measurement-v0.7.4，尚未完成分类质量验收。当前研究规则已为v0.7.5，旧引擎compatible=false，现有前后端版本检查会暂停新自动分类；既有结果保留。界面尚无关系树编辑器，新结构仅完成规则、结构化导入与研究库保存，不能宣称按钮已支持新类自动识别。

最终回放 outputs/classifier-v079/final/：411 CODED、98 UNKNOWN、99 FAILED、2 SKIPPED，程序异常0；FAILED包含77映射/责任未覆盖、8主责未覆盖、14不支持的语言。44条改善、4条转复核，净增40条主类一致。四维不是全面解决：技术标签集合一致77→156，但加语境/关系后66→65；技能基本持平；活动有所提升；次职能提出100个岗位—标签组合仅9个与参考相同，自动建议统一需复核，不标为可直接统计。610条是已曝光开发参考，不是独立准确率验证。 before/为升级前，final/为最终版本，调试中间副本已移除，仅保留升级前和最终快照及验收证据。

## 周采已关闭

configs/weekly_schedule.yaml：enabled=false、status=DISABLED_BY_USER；pilot_collection.yaml：recurring_collection_enabled=false。Windows任务EmbodiedAIHiring-4plus4-Weekly已Disabled，原9月13日计划不再执行。此次正式入库是带原采集时间的公开证据导入，不宣称后台实时爬取。

智元与逐际动力通过项目已验证的独立浏览器直连方法恢复，分别83/83及92/92条详情；普通浏览器ERR_CONNECTION_CLOSED不能直接判不可采。恢复证据位于phase2-onboarding/direct_browser_recovery/20260911T063916Z/。仅实例直连，没有改系统代理。

## 历史保护与研究边界

旧610条原始文件SHA256 ebe2f5e520c9247ef51fcc95dd906f6877a00dae307a63075bf51be67e8f8bb7；旧候选文件SHA256 5c0847c982359cfc538beae66f586bbf25dcbaaab8526069dc05a0132b661502，均保留。第一轮比较快照phase1-existing/comparison/不改写。此前v0.7.8实施与文件清理报告继续作为历史证据保存。

研究观察公开广告中的工作分工、技术、技能与活动。公司归属、岗位地点与语言分开；广告不等于人数，缺采是未知，案例不代表国家总体。Amazon仅FAR团队；Diligent保留收购边界；傅利叶和Boston Dynamics为全公司多产品范围。当前1654条人工复核已由用户本轮确认为完成；统一包保留AI生成身份及原观察/判读版本，没有据此新增独立双重编码金标准或虚构逐条审核提交。
