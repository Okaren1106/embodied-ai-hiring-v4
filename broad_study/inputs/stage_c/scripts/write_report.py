from analyze import ROOT,R,A,T,read,js,dump,table
from collections import Counter
import json
from html import escape
S=js(ROOT/'summary.json');F=js(ROOT/'figure_manifest.json')
q1=read(T/'T2_aggregates.csv');q2=read(T/'T3_aggregates.csv');qc=read(T/'T3_company_context.csv');act=read(T/'T4_activity_aggregates.csv');companies=read(T/'T1_company_sample.csv');cb={r['company_id']:r for r in companies}
roles={'RF_ML_AI_ENGINEERING':'ML/AI工程','RF_ROBOTICS_SOFTWARE':'软件与平台'}
metrics={'DUTY_OWN_USE':'职责中本人使用','DUTY_OWN_DEVELOP':'职责中本人开发','REQUIRED':'硬性要求','GENERAL':'一般要求','PREFERRED':'优先要求'}
branches={'UNCONDITIONAL':'独立条目','CHOICE':'任选','EXAMPLE':'示例','CHOICE_AND_EXAMPLE':'任选且示例'}
def pct(x):return f'{float(x)*100:.1f}%' if x!='' else 'NA'
def md(headers,rows):return '| '+' | '.join(headers)+' |\n|'+ '|'.join(['---']*len(headers))+'|\n'+'\n'.join('| '+' | '.join(str(x).replace('|','／').replace('\n',' ') for x in row)+' |' for row in rows)
top=[r for r in q1 if r['scope']=='ALL24' and r['denominator_basis']=='ALL'];top.sort(key=lambda r:-int(r['n_ads']))
q1table=md(['主职能/状态','广告数','全1,654条占比'],[[r['class_name'],r['n_ads'],pct(r['share_ad_weighted'])] for r in top])
def q2r(role,name,m='GENERAL',b='UNCONDITIONAL'):
 return next(r for r in q2 if r['group']=='WHOLE23' and r['role_code']==role and r['label_name']==name and r['metric_bucket']==m and r['branch_bucket']==b)
head=[]
for role,name,m,b in [('RF_ML_AI_ENGINEERING','Python','GENERAL','UNCONDITIONAL'),('RF_ML_AI_ENGINEERING','PyTorch','GENERAL','UNCONDITIONAL'),('RF_ML_AI_ENGINEERING','PyTorch','GENERAL','EXAMPLE'),('RF_ML_AI_ENGINEERING','训练推理系统','DUTY_OWN_DEVELOP','UNCONDITIONAL'),('RF_ML_AI_ENGINEERING','基础模型/VLA','DUTY_OWN_DEVELOP','UNCONDITIONAL'),('RF_ML_AI_ENGINEERING','数据管线与资产','DUTY_OWN_DEVELOP','UNCONDITIONAL'),('RF_ROBOTICS_SOFTWARE','Linux','GENERAL','UNCONDITIONAL'),('RF_ROBOTICS_SOFTWARE','C++','GENERAL','UNCONDITIONAL'),('RF_ROBOTICS_SOFTWARE','Python','GENERAL','UNCONDITIONAL'),('RF_ROBOTICS_SOFTWARE','可靠性','DUTY_OWN_DEVELOP','UNCONDITIONAL'),('RF_ROBOTICS_SOFTWARE','实时系统','DUTY_OWN_DEVELOP','UNCONDITIONAL')]:
 head.append(q2r(role,name,m,b))
q2table=md(['职能','技能/技术','明确语境','正向/可解释','关系未知','广告加权','公司等权'],[[roles[r['role_code']],r['label_name'],metrics[r['metric_bucket']]+'·'+branches[r['branch_bucket']],r['n_positive']+'/'+r['n_interpretable'],r['n_relation_unknown'],pct(r['share_ad_weighted']),pct(r['share_company_equal'])] for r in head])
activity=md(['活动','本人承担数/1,623','本人承担占比','参与协作数/1,623','参与协作占比'],[[r['label_name'],r['n_positive'],pct(r['share_ad_weighted']),next(x['n_positive'] for x in act if x['scope']=='ALL24' and x['label_code']==r['label_code'] and x['relation']=='PARTICIPATES'),pct(next(x['share_ad_weighted'] for x in act if x['scope']=='ALL24' and x['label_code']==r['label_code'] and x['relation']=='PARTICIPATES'))] for r in act if r['scope']=='ALL24' and r['relation']=='OWNED'])
# Sensitivity for every headline cell, with matching role/label/context/branch.
sr=read(T/'T3_scope_sensitivity.csv');lo=read(T/'T3_leave_one_company_out.csv');sens=[]
for h in head:
 match=lambda r:all(r[k]==h[k] for k in ['role_code','dimension','label_code','metric_bucket','branch_bucket'])
 subset=[r for r in sr if match(r)];leave=[r for r in lo if r['group']=='WHOLE23' and match(r) and r['gate']=='PASS'];v={r['variant']:r for r in subset}
 sens.append(dict(role=roles[h['role_code']],label=h['label_name'],context=metrics[h['metric_bucket']]+'·'+branches[h['branch_bucket']],company_equal_base=pct(h['share_company_equal']),ad_weighted_base=pct(h['share_ad_weighted']),catalog_direct_ad_weighted=pct(v['CATALOG_DIRECT']['share_ad_weighted']),exclude_multi_product_ad_weighted=pct(v['EXCLUDE_MULTI_PRODUCT']['share_ad_weighted']),exclude_media_only_ad_weighted=pct(v['EXCLUDE_MEDIA_ONLY']['share_ad_weighted']),leave_one_out_ad_weighted_min=min(float(r['share_ad_weighted']) for r in leave),leave_one_out_ad_weighted_max=max(float(r['share_ad_weighted']) for r in leave),n_leave_out_pass=len(leave)))
table('headline_sensitivity.csv',sens)
sensmd=md(['职能/指标','基础加权','排除技能UNMAPPED','排除已标多产品公司','逐一剔除公司范围'],[[r['role']+' '+r['label']+' '+r['context'],r['ad_weighted_base'],r['catalog_direct_ad_weighted'],r['exclude_multi_product_ad_weighted'],pct(r['leave_one_out_ad_weighted_min'])+'—'+pct(r['leave_one_out_ad_weighted_max'])] for r in sens])
maincompany=[]
q1c=read(T/'T2_company_primary_roles.csv')
for c in companies:
 rows=[r for r in q1c if r['company_id']==c['company_id']];mx=max(int(r['n_ads']) for r in rows);leaders=[r for r in rows if int(r['n_ads'])==mx]
 maincompany.append([c['company_name'],c['n_ads'],'、'.join(r['class_name'] for r in leaders),mx,pct(leaders[0]['share_all']),c['stratum_name']])
companymd=md(['公司/团队','广告总数','最高主职能（含并列）','该类广告数','公司内占比','固定供给形态'],maincompany)
report=f'''# Q1—Q3 正式描述结果 v1

2026-09-15。按已固定分析规则 v1 完成阶段 C。Q2 暂保留 **ML/AI工程、软件与平台两个代表职能**。本轮由主助手完成整理、分析与作者验证；独立验收尚未进行。

入口：[图表总览与公司查询](index.html) · [结果工作簿](outputs/01a0a3f0/Q1-Q3_results.xlsx) · [计数与分母说明](METHODS.md) · [全部表格目录](DATA_DICTIONARY.md)。

## 1. 这批结果回答了什么

1. **Q1：样本招聘包含完整的产品工程与运营分工。** 制造、质量与供应链215条（13.0%），软件与平台181条（10.9%），ML/AI工程159条（9.6%）。这些是本批广告构成，不是员工结构或实际招聘人数。
2. **Q2：同类职能的技术内容必须连同语境读。** ML/AI工程中，训练推理系统开发为81/156（51.9%）；软件与平台中，可靠性开发为107/180（59.4%）。PyTorch等工具大量处于示例或任选结构，不能全部读作独立硬性要求。
3. **Q3：研究科学职能与研究探索活动有交集，也有不同范围。** 32条以研究科学为主职能；75条明确本人承担研究探索，其中36条主职能是ML/AI工程，27条是研究科学。工程实现活动覆盖957/1,623条（59.0%）。
4. **职责结构保留原关系。** 19条复合承担、11条多方向任选，其中1条在任选分支内嵌套复合职责；30棵树和87个职能节点完整保留。

以上是描述结果。阶段 D 再将业务事实、反例和招聘范围逐项连接，形成解释与结论台账；本报告未把供给形态或国家当作这些差别的原因。

## 2. 样本和分母

- 全部24个主体、1,654条认可广告，中国12家963条，美国12家691条。原8家610条观察日为2026-08-31，新增16家1,044条为2026-09-11，属于两个观察批次。
- Q1保留全部广告；1,606条明确主类由1,576条具体职能和30条结构类组成，另15歧义、2目录未覆盖、31来源不足。
- 整公司主汇总为23家公司1,630条，Amazon FAR的24条作为团队点值。傅利叶、Boston Dynamics保留原全公司多产品边界；Diligent保留组织归属边界。
- Q2两职能全范围159/181条，整公司范围156/180条。该两职能技能维度各有2条UNMAPPED；目录外事实未因此变成“未提及”。来源可读不代表每项关系可解释，逐格未知另减。
- Q3活动可判读1,623条，其中1,618条CODED和5条NOT_MENTIONED；31条来源不足退出活动分母。

## 3. Q1：公司招什么工作

### 3.1 全样本构成

{q1table}

![公司主职能组合](charts/F1_q1_company_roles.png)

### 3.2 公司等权与广告加权

在23家整公司范围内，制造/质量/供应链等权13.0%、加权13.1%；软件与平台10.8%/11.0%；ML/AI工程9.7%/9.6%。三个职能在两种权重下均居前三。公司等权回答“样本公司平均怎样组合”，广告加权回答“这批广告怎样组成”。

权重对较小类别更敏感：机器人操作的公司等权2.7%、广告加权1.3%；控制与规划6.2%/4.6%；公司支持6.7%/8.1%。因此不能只用广告池总量概括典型公司。FAR单列后，研究科学由全范围32条变为整公司23条；FAR自身9/24为研究科学，团队范围对研究类结果有明显影响。

![两种权重](charts/F2_q1_weighting.png)

### 3.3 逐公司结果

下表只用于读图导航，“最高”保留并列且不自动代表业务主业。例如星尘智能的制造/质量/供应链与商务/客户均为14条，不能只挑其中一项叙述。

{companymd}

来源不足31条中Field AI占23条。它的软件与平台23/131与来源不足23/131并列；保留分母和状态可避免把有限正文误当成确定职能分布。

## 4. Q2：两个代表职能中的技术与技能

### 4.1 固定展示标签和语境

ML/AI具体技能10项，软件与平台9项，各8项技术概念，共35个“职能×标签”展示项；全部115个已记录“职能×标签”组合仍输出附表。泛称工具、背景、否定和未解决关系单列。

每项标签保留14种语境分支：本人使用、本人开发；硬性/一般/优先要求各拆为独立、任选、示例、任选且示例。一般要求不会自动升级为硬性；任选表示处于选择关系，示例表示举例，均不是单项无条件要求。

### 4.2 主要读数（整公司范围）

{q2table}

ML/AI工程的结果既包含模型，也包含训练推理、数据管线和评测。训练推理系统开发81/156、基础模型/VLA开发72/156、数据管线开发67/156；这些标签会共现，不相加为岗位数。公司等权下训练推理系统为60.8%，而基础模型/VLA为37.4%，反映各公司样本大小和内容组成不同。

软件与平台的Linux独立一般要求为70/177（39.5%），C++为42/150（28.0%），Python为35/165（21.2%）。这些分母不同：Linux有3条、C++有30条、Python有15条关系未知，被排除的仅是相应指标。不能把未知当成否定，也不能直接把70、42、35除以全部180来替代已固定口径。

PyTorch的一般要求中，独立条目31/144，示例41/144，另有任选及交叉分支。两格可能包含同一广告，不能相加。具体工具的职责开发列较少，表示原有广告证据和目录判读较少明确“开发该工具本身”，不能据此推断工程师不开发软件。

![ML技能语境](charts/F3_q2_ml_skills.png)

![软件技能语境](charts/F4_q2_software_skills.png)

技术概念全图见[ML/AI技术](charts/A1_q2_ml_technical.png)、[软件与平台技术](charts/A2_q2_software_technical.png)。逐公司一般要求见[ML公司点值](charts/A3_q2_ml_company_general.png)、[软件公司点值](charts/A4_q2_software_company_general.png)；其他13种语境通过总览查询和完整T3读取。

### 4.3 公司、业务组和国家比较的许可

全部公司格保留分子、基础范围、关系未知、可解释分母与少于10条提示。业务组在每个最终标签格重新核对至少3家有分母公司且合计至少20条可解释广告，未通过者不发布组平均。

跨本体模型组的ML/AI仅17条，保留公司点值。该组软件与平台38条中Field AI贡献23条；逐一排除Field AI后仅2家15条，组平均失去展示资格。即便完整组某格通过门槛，其平均也只能探索性使用。本轮保留全部逐格门槛及逐一剔除记录，未选取组间最大差距作结论。

国家辅助格只在整机/机器人系统组内计算；3家跨本体模型公司均来自美国，不能据组差解释国家差异。场景是重叠且成熟度不同的连接，本轮保留分类供后续解释，没有把场景当独立实验组。

### 4.4 已完成的基础敏感性

除公司等权/广告加权及FAR范围外，已计算固定展示项的目录直接子集、排除已标多产品公司、排除仅媒体依据公司，以及整公司/系统组/模型组逐一剔除公司。以下为正文读数的对应检查，范围是同一指标的逐一剔除最小/最大值，不是置信区间。

{sensmd}

这些是阶段C结果的基础核对，尚不等于完成阶段D的来源完整子集、商业化证据、场景实际使用子集、反例和最终结论台账。

## 5. Q3：活动与职责如何组合

### 5.1 活动的承担关系

{activity}

同一广告可同时出现本人承担与参与同类活动。例如工程实现：本人承担957、参与205，并集1,034，二者不能直接相加；交集为128条。多种活动也能共存，总比例不要求为100%。

研究探索本人承担75条中，研究科学主职能27条、ML/AI工程36条，其余分布于软件、控制、感知、数据和评测类。研究科学主职能32条也不自动全记为研究探索活动：活动按原文独立判读。这说明Q1职能与Q3活动测量不同内容，不能互相替代。

![公司活动](charts/F5_q3_activity_company.png)

### 5.2 复合与任选结构

19条复合职能（1.15%）、11条多方向招聘（0.67%），合计30/1,654（1.81%）。结构节点87个，只作为分支/组成提及，不能解释为87个岗位或人数，也不拆入Q2具体主职能分母。

智元N0396“具身大模型AI Infra工程师/专家”的原文为“可选择以下一个或多个方向深入参与”。根节点是OR；五个方向中的第四个同时包含模型推理与跨版本自动化评测，内部为ALL。本轮保留“方向1 或 方向2 或 方向3 或（模型推理 × 评测）或 方向5”，不会把整条改成同时承担六项职责。

87个职能节点中，75个为DESCRIBED、12个为NOT_EXPANDED（以原始节点状态为准）。只列出可见职责，不把分类目录的定义补成广告原文。完整30棵原树、118个全部节点、87个职能节点以及原文定位分别见T4。

![职责结构](charts/F6_q3_role_structures.png)

## 6. 本轮完成边界和下一步

**阶段C的T1整合、T2正式表、T3语境结果、T4活动与结构表、6张主图和4张附图已产出。** 每幅图另有精确绘图数据表，PNG适合阅读，SVG适合排版导出。

数据整理沿用A阶段认可快照和已固定规则，保留广告身份、文本哈希、观察日期、原规则版本；未重分类、未回填技能目录、未新采集广告。当前人工复核完成状态沿用用户确认，不额外声称独立双重编码。

下一步进入阶段D：从本批描述结果提炼待检验解释，联系供给形态、实际交付与招聘范围，选择有证据支持的少量可比案例，完成T5公司背景对应表和T6结论/敏感性台账。随后阶段E写研究初稿。Q2继续两个代表职能，扩展其他职能不列为当前前置工作。

验证方法与结果见[验证说明](verification/REPORT.md)。
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
methods='''# 计数、分母与追溯

## Q1

单位为认可广告身份identity_key。CODED使用已有primary_code，其他状态分别作为歧义、目录未覆盖、来源不足类。每公司22格合计该公司全部广告。明确子集为CODED的1,606条，包含两个结构类，未明确类在该子集比例为NA。公司等权为有分母公司的各自比例算术平均；广告加权为分子合计/分母合计。

## Q2

仅primary_status=CODED且主类为固定两具体职能。skills/technical_concepts各自使用CODED、NOT_MENTIONED、UNMAPPED基础范围；SOURCE_UNASSESSABLE退出该维度。目录外原词单存，并未加入正式标签。

要求分支沿requirement_group的所有祖先和根关系判定，OR/OR_EQUIVALENT/SOME_OF保留为CHOICE，EXAMPLE保留为EXAMPLE，二者同时存在为CHOICE_AND_EXAMPLE，未解决关系为UNRESOLVED。使用固定v1的label_state：精确语境分支有正向记录为PRESENT；无明确正向但存在可影响该格的关系/用途/语境未知为UNKNOWN；其他为NO_RECORDED_POSITIVE。明确正向优先于同一广告其他未知提及。

分子=PRESENT；分母=PRESENT+NO_RECORDED_POSITIVE。UNKNOWN只退出相应标签语境格。这个比例衡量已记录目录标签的明确语境覆盖，0不证明真实岗位没有要求。一个广告可以进入不同语境格，禁止横向相加。硬性REQUIRED、一般GENERAL、优先PREFERRED独立编码；背景与否定不并入正向。

T3_base_admission保留全部680个广告×维度资格。T3_positive_unknown_lineage保留所有PRESENT/UNKNOWN；未列出的基础资格广告在相应标签格为NO_RECORDED_POSITIVE，免去重复存储数十万零行。用identity_key、role_code、dimension、label_code、metric_bucket、branch_bucket连接。identity_key含竖线，是完整不透明标识，不能按竖线拆分。所有ID集合用JSON数组。

T3_all_item_semantics保留5,547条原始标签提及和语义判断，含未作为正向的记录。原始技能/技术长表有field/start/end、quote、text_version_hash，位于inputs/rules_v1/inputs/stage_a。requirements关系原树在relations.jsonl。T3_separate_context_mentions按广告去重列背景、否定、协作或未解决语境计数，属于记录数清点，不声称正向率。

组均值要求本格≥3家非零分母公司且≥20条可解释广告；门槛中的公司数不是正向提及公司数。单公司、团队、单独案例均只展示点值；零分母NA；0<n<10标小样本；最大公司分母贡献>50%标集中。阈值是展示约定，不是统计充分性保证。单列案例及失败格保留分子分母但组均值留空。

## Q3

活动维度独立于主职能，CODED+NOT_MENTIONED共1,623条可判读。按广告×活动×relation去重，OWNED=本人承担、PARTICIPATES=参与协作；ANY_RECORDED为并集。现有数据没有其他关系枚举，新出现未知关系时脚本拒绝运行，不能默认本人承担。所有源标签行保留追溯。

结构广告总计30；根ALL为复合19，根OR为任选11，含一棵混合树。T4_role_structures保存完整树JSON，T4_role_structure_nodes保存原节点，function_appearances仅统计广告中的职能组成/分支出现，不作人数。每条结构广告在Q1计1，不拆到Q2。

## 来源与适用范围

唯一数据集为REFERENCE1654_USER_ACCEPTED_2026_09_14_V1，不混入1648开发基线。两批观察日期分别2026-08-31和2026-09-11。原始规则版本保留，分析代码复用固定v1解释规则，不宣称已重分类为同一规则版本。业务分类事实来自已封存B补充包；其证据、状态、时间适用性和原始用途保留。未知场景不是无场景，公开目标不是实际付费交付。

非概率样本、公开招聘渠道范围、广告正文的详略和职能目录覆盖共同限制外推。未做显著性检验或因果估计。UNMAPPED敏感性仅检查已有目录直接子集，不能证明目录外技能不存在。
'''
(ROOT/'METHODS.md').write_text(methods,encoding='utf-8')
descs={'T1_company_sample.csv':'24行样本、四维状态、供给分类与证据ID','T2_company_primary_roles.csv':'24×22公司主职能格','T2_aggregates.csv':'全24、整公司23及供给形态描述；全部/明确分母','T2_ad_lineage.csv':'1654条主职能计数的广告、原URL及文本版本','T3_company_context.csv':'全部已记录标签的公司×语境×分支结果','T3_aggregates.csv':'组汇总与每格门槛；不允许汇总的率留空','T3_base_admission.csv':'两职能广告×维度基础资格','T3_positive_unknown_lineage.csv':'逐标签语境的正向与未知广告清单','T3_all_item_semantics.csv':'全部原标签提及、原文和固定语义判读','T3_scope_sensitivity.csv':'固定展示项的范围与目录子集检查','T3_leave_one_company_out.csv':'逐一剔除公司；不足门槛时不发布均值','T3_separate_context_mentions.csv':'非正向语境按广告去重清点','T3_selected_role_unmapped_mentions.csv':'两职能已有目录外提及，含多个维度','T4_activity_company.csv':'公司×8活动×本人/参与/并集，576格','T4_activity_aggregates.csv':'全24与整公司23活动汇总','T4_activity_lineage.csv':'全部3236原活动提及，分析中按广告去重','T4_activity_admission.csv':'1654广告活动维度资格','T4_primary_activity_cross.csv':'主职能×活动关系交叉，不互相代替分类','T4_role_structures.csv':'30条结构广告及原始完整树JSON','T4_role_structure_nodes.csv':'118原节点，其中87职能节点','T4_role_structure_company.csv':'逐公司复合/任选/混合广告数','T4_structure_function_appearances.csv':'结构中的职能提及，以广告去重，不是人数','headline_sensitivity.csv':'正文具体读数的对应敏感性摘要'}
dictionary='# 数据表目录\n\n全部CSV为UTF-8 BOM，可用Excel导入。数值比例为0—1，NA在CSV中为空，计数为整数。\n\n'+md(['文件','行数','用途'],[[f'[{p.name}](tables/{p.name})',len(read(p)),descs.get(p.name,'图表精确绘图数据；源表和图注见figure_manifest.json')] for p in sorted(T.glob('*.csv'))])+'''\n\n## 字段与连接\n\n- identity_key：完整广告唯一身份；record_id、reading_id仅辅助定位，不替代唯一身份。\n- n_positive：经语境筛选后去重的正向广告数；n_base：该职能该维度基础广告数；n_relation_unknown：该指标关系未知；n_interpretable：最终分母。\n- share、share_all、share_ad_weighted、share_company_equal：0—1比例。空值为无分母、明确子集不适用或不允许组汇总，结合对应状态字段解释。\n- n_companies：本格非零分母公司数；eligible_companies_json：相应公司列表。\n- *_json：JSON文本，使用JSON解析，不按分隔符拆分。\n- primary_code、label_code、metric_bucket、branch_bucket、relation为原有或已固定v1枚举。字段含义补充见METHODS。\n- 业务分类证据通过company_id→basis_fact_ids/basis_evidence_ids连接inputs/rules_v1内的decision_provenance、evidence_index和封存证据。\n\nExcel提供主要结果：Q1完整528格、Q2整公司490语境格、Q2公司一般独立要求840格、Q3完整576格及30条结构概览。其他语境的公司格、业务组与全部追溯放在CSV和HTML查询中，工作簿并非全量长表的重复备份。\n'''
(ROOT/'DATA_DICTIONARY.md').write_text(dictionary,encoding='utf-8')
# Workbook clean intermediates: source-derived counts stay typed; displayed rates use transparent formulas.
def num(v):return int(v)
books=[]
books.append(dict(name='Q1职能',source='T2_company_primary_roles.csv',headers=['公司','主职能或状态','广告数','全部分母','全部占比','明确子集数','明确分母','明确占比','类别','供给形态'],rows=[[r['company_name'],r['class_name'],num(r['n_ads']),num(r['denominator_all']),None,num(r['n_coded']),num(r['denominator_coded']),None,r['class_kind'],r['stratum']] for r in q1c],formulas={4:'=IF(D{r}=0,"n.a.",C{r}/D{r})',7:'=IF(I{r}="unspecified","n.a.",IF(G{r}=0,"n.a.",F{r}/G{r}))'},rates=[4,7]))
qr=[r for r in q2 if r['group']=='WHOLE23' and r['main_display']=='YES']
books.append(dict(name='Q2语境',source='T3_aggregates.csv：WHOLE23且固定展示项',headers=['职能','技能或技术','语境','关系分支','正向数','基础数','关系未知','可解释分母','广告加权','公司等权','公司数','维度'],rows=[[roles[r['role_code']],r['label_name'],metrics[r['metric_bucket']],branches[r['branch_bucket']],num(r['n_positive']),num(r['n_base']),num(r['n_relation_unknown']),num(r['n_interpretable']),None,float(r['share_company_equal']),num(r['n_companies']),r['dimension']] for r in qr],formulas={8:'=IF(H{r}=0,"n.a.",E{r}/H{r})'},rates=[8,9]))
qr=[r for r in qc if r['main_display']=='YES' and r['metric_bucket']=='GENERAL' and r['branch_bucket']=='UNCONDITIONAL']
books.append(dict(name='Q2公司一般要求',source='T3_company_context.csv：一般要求、独立条目、固定展示项',headers=['公司','职能','技能或技术','正向数','基础数','关系未知','可解释分母','占比','小样本','维度'],rows=[[r['company_name'],roles[r['role_code']],r['label_name'],num(r['n_positive']),num(r['n_base']),num(r['n_relation_unknown']),num(r['n_interpretable']),None,r['small_n_under10'],r['dimension']] for r in qr],formulas={7:'=IF(G{r}=0,"n.a.",D{r}/G{r})'},rates=[7]))
books.append(dict(name='Q3活动',source='T4_activity_company.csv',headers=['公司','活动','承担关系','正向广告数','公司广告数','来源不足','可判读分母','占比'],rows=[[r['company_name'],r['label_name'],{'OWNED':'本人承担','PARTICIPATES':'参与协作','ANY_RECORDED':'任一提及并集'}[r['relation']],num(r['n_positive']),num(r['n_all_ads']),num(r['n_source_unassessable']),num(r['n_assessable']),None] for r in read(T/'T4_activity_company.csv')],formulas={7:'=IF(G{r}=0,"n.a.",D{r}/G{r})'},rates=[7]))
names={r['class_code']:r['class_name'] for r in q1c}
def expr(n):
 if n['relation']=='ROLE':return names[n['value']]
 return '('+(' × ' if n['relation']=='ALL' else ' 或 ').join(expr(ch) for ch in n['children'])+')'
sts=read(T/'T4_role_structures.csv')
books.append(dict(name='Q3职责结构',source='T4_role_structures.csv：完整原树另存CSV',headers=['公司','阅读编号','岗位标题','根关系','职能节点数','有嵌套混合','结构表达','广告ID'],rows=[[r['company_name'],r['reading_id'],r['title'],'复合承担' if r['root_relation']=='ALL' else '多方向任选',num(r['n_role_nodes']),r['has_mixed_branch'],expr(json.loads(r['tree_json'])['expression']),r['record_id']] for r in sts],formulas={},rates=[]))
books.append(dict(name='样本与来源',source='T1_company_sample.csv；固定规则v1',headers=['公司','国家','广告数','观察日期','供给形态','主体范围','技能UNMAPPED','活动来源不足','招聘来源URL','分类证据ID'],rows=[[r['company_name'],r['country'],num(r['n_ads']),r['observation_dates'],r['stratum_name'],r['entity_scope_inherited'],num(r['skills_UNMAPPED']),num(r['activities_SOURCE_UNASSESSABLE']),r['hiring_source_url'],r['basis_evidence_ids']] for r in companies],formulas={},rates=[]))
dump(ROOT/'workbook_data.json',books)
# HTML is self-contained for querying all 11,760 fixed-display company cells, including zero/NA.
lookup_rows=[[r[k] for k in ['company_id','role_code','dimension','label_code','label_name','metric_bucket','branch_bucket','n_positive','n_base','n_relation_unknown','n_interpretable','share','small_n_under10']] for r in qc if r['main_display']=='YES']
querydata={'rows':lookup_rows,'companies':{r['company_id']:r['company_name'] for r in companies},'roles':roles,'metrics':metrics,'branches':branches}
gallery=''.join(f'<section id="{f["id"]}"><h2>{f["id"].split("_")[0]} {escape(f["title"])}</h2><p>{escape(f["caption"])}</p><a href="{f["png"]}"><img src="{f["png"]}" alt="{escape(f["title"])}"></a><p><a href="{f["svg"]}">SVG</a> · <a href="{f["plot_data"]}">绘图数据 CSV</a></p></section>' for f in sorted(F,key=lambda f:(f['id'][0]!='F',f['id'])))
html='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Q1—Q3 正式结果</title><style>
body{margin:0;background:#f3f6f8;color:#213247;font:16px/1.7 "Microsoft YaHei",sans-serif}main{max-width:1420px;margin:auto;padding:35px 25px}h1{font-size:32px;margin-bottom:10px}h2{font-size:23px}h3{font-size:18px}p{max-width:1050px}nav{display:flex;flex-wrap:wrap;gap:10px 22px;margin:25px 0}a{color:#1e6596}section{background:white;padding:26px;margin:25px 0;border-radius:10px;border:1px solid #dfe6ec}img{display:block;width:100%;height:auto}.summary{border-left:5px solid #286793;padding:10px 22px;background:white}select{font:inherit;padding:8px;margin:5px;max-width:100%}.scroll{overflow:auto}table{border-collapse:collapse;font-size:14px;min-width:820px;width:100%}th,td{padding:9px 12px;border-bottom:1px solid #dfe6ec;text-align:left}th{background:#eaf0f5}td.num{text-align:right}.small{color:#855821}.controls{display:flex;flex-wrap:wrap;gap:5px}.muted{color:#536475;font-size:14px}footer{padding:30px 0} @media(max-width:700px){main{padding:18px 12px}section{padding:16px}h1{font-size:25px}}
</style><main><h1>Q1—Q3 正式结果 v1</h1><p>24 个主体，1,654 条认可招聘广告。阶段 C 描述分析，Q2 保留 ML/AI 工程与软件/平台两个代表。</p><nav><a href="REPORT.md">完整结果报告</a><a href="outputs/01a0a3f0/Q1-Q3_results.xlsx">结果工作簿</a><a href="METHODS.md">计数与分母</a><a href="DATA_DICTIONARY.md">全部数据表</a><a href="verification/REPORT.md">验证记录</a><a href="#query">Q2 公司查询</a></nav><div class="summary"><p><b>Q1：</b>制造/质量/供应链 215 条，软件/平台 181 条，ML/AI 工程 159 条。</p><p><b>Q2：</b>ML/AI 训练推理系统开发 81/156；软件/平台可靠性开发 107/180。每格按原语境计算分母。</p><p><b>Q3：</b>本人承担工程实现 957/1,623。复合 19 条，任选 11 条，保留嵌套关系。</p></div>
<section id="query"><h2>Q2：查询同一职能、同一语境的公司点值</h2><p>包括零值与零分母。0 表示未记录到这一明确正向语境；NA 表示该格没有可解释分母。FAR 为团队点值，* 表示分母少于 10 条。</p><div class="controls"><select id="role" aria-label="职能"></select><select id="dim" aria-label="维度"><option value="skills">具体技能</option><option value="technical_concepts">技术概念</option></select><select id="label" aria-label="标签"></select><select id="metric" aria-label="语境"></select><select id="branch" aria-label="分支"></select></div><p id="querycount" class="muted"></p><div class="scroll"><table><thead><tr><th>公司/团队</th><th>正向数</th><th>基础数</th><th>关系未知</th><th>最终分母</th><th>比例</th><th>样本提示</th></tr></thead><tbody id="result"></tbody></table></div><p><a href="tables/T3_company_context.csv">全部标签与语境公司表</a> · <a href="tables/T3_positive_unknown_lineage.csv">正向/未知广告追溯</a> · <a href="tables/T3_aggregates.csv">逐格业务组许可与汇总</a></p></section>
'''+gallery+'''<footer>当前为作者完成并验证的阶段 C 结果。阶段 D 公司事实解释与完整结论台账、阶段 E 论文初稿尚待推进。招聘广告不等于人数，样本不代表行业总体。</footer></main><script>
const data=QUERY_DATA;const $=id=>document.getElementById(id);function opts(el,obj){el.replaceChildren(...Object.entries(obj).map(([v,t])=>{let o=document.createElement('option');o.value=v;o.textContent=t;return o}));}
opts($('role'),data.roles);opts($('metric'),data.metrics);$('metric').value='GENERAL';opts($('branch'),data.branches);
function labels(){const obj={};for(const r of data.rows)if(r[1]==$('role').value&&r[2]==$('dim').value)obj[r[3]]=r[4];opts($('label'),obj);render();}
function render(){const duty=$('metric').value.startsWith('DUTY_');$('branch').disabled=duty;if(duty)$('branch').value='UNCONDITIONAL';const rows=data.rows.filter(r=>r[1]==$('role').value&&r[2]==$('dim').value&&r[3]==$('label').value&&r[5]==$('metric').value&&r[6]==$('branch').value);$('result').replaceChildren(...rows.map(r=>{let tr=document.createElement('tr');let values=[data.companies[r[0]]+(r[0]=='US_AMAZON_FTR'?'（团队）':''),r[7],r[8],r[9],r[10],r[11]==''?'NA':(Number(r[11])*100).toFixed(1)+'%',r[12]=='YES'?'* 少于10条':r[10]=='0'?'无分母':''];for(let i=0;i<values.length;i++){let td=document.createElement('td');td.textContent=values[i];if(i>0&&i<6)td.className='num';if(i==6)td.className='small';tr.append(td)}return tr}));$('querycount').textContent=rows.length+' 个公司/团队点值。筛选仅改变视图，标签与分类规则保持固定。';}
$('role').onchange=labels;$('dim').onchange=labels;for(const id of ['label','metric','branch'])$(id).onchange=render;labels();
</script>'''
def wrap_json(text, width=480):
    """Insert newlines after commas outside strings; retain all original bytes."""
    out = []
    quoted = escaped = False
    column = 0
    for char in text:
        out.append(char)
        column = 0 if char == '\n' else column + len(char.encode('utf-8'))
        if quoted:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == '"':
                quoted = False
        elif char == '"':
            quoted = True
        elif char == ',' and column >= width:
            out.append('\n')
            column = 0
    return ''.join(out)

html=html.replace('QUERY_DATA',wrap_json(json.dumps(querydata,ensure_ascii=False).replace('</','<\\/')))
(ROOT/'index.html').write_text(html,encoding='utf-8')
print('Report, methods, dictionary, HTML and workbook inputs generated')
