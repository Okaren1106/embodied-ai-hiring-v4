# 计数、分母与追溯

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
