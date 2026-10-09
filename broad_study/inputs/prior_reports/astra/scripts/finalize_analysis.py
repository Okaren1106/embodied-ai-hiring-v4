from common import *
lock_check()

# Directory coverage is a different uncertainty from requirement relation.
s=read(C/'tables/T3_scope_sensitivity.csv')
core={'SK_PYTHON','SK_PYTORCH','SK_CPP','SK_LINUX','TC_ML_SYSTEMS','TC_FOUNDATION_MODEL','TC_DATA_PIPELINE','TC_RELIABILITY','TC_REALTIME'}
dump('Q2_inherited_directory_product_sensitivity.csv',[r for r in s if r['group']=='WHOLE23' and r['label_code'] in core and r['main_display']=='YES'])

h=read(ROOT/'tables/H1_cross_function_sensitivity.csv')
summary=[]
for a in ['ACT_RESEARCH','ACT_DEPLOYMENT','ACT_QUALITY']:
 for d in ['ALL_ACTIVITY_POSITIVE','CONCRETE_PRIMARY_ONLY']:
  rows=[r for r in h if r['activity']==a and r['denominator']==d]
  for stat in ['company_equal','ad_weighted']:
   for family,rr in [('ALL_SPECIFIED',rows),('WHOLE_COMPANY_LOO',[r for r in rows if r['scope'].startswith('LOO_')])]:
    lo=min(rr,key=lambda r:float(r[stat]));hi=max(rr,key=lambda r:float(r[stat]))
    summary.append({'activity':a,'denominator':d,'statistic':stat,'sensitivity_family':family,'min':lo[stat],'min_scope':lo['scope'],'max':hi[stat],'max_scope':hi['scope'],'n_variants':len(rr)})
dump('H1_sensitivity_envelope.csv',summary)

ledger=[
 dict(id='H1a',hypothesis='研究、部署与质量活动分散到同名专门职能之外',scope='WHOLE23；广告承担活动，并非员工分工',companies='研究13；部署22；质量23家有正例',ads='研究66；部署343；质量459',P='48；264；300',N='66；343；459',U='主职能不明0；3；4；另31条活动来源不可判读退出活动范围',metric='活动正例中专门职能之外占比；公司等权与广告加权',result='72.73%；76.97%；65.36%（广告加权）',status='SUPPORTED_DESCRIPTIVE',sensitivity='全部24、整公司23、正文活动完整17、逐公司剔除、具体主职能、排除既知多产品均保持过半',counterexample='质量活动仍有159/459在制造质量供应链职能；科研活动全样本加入FAR后专门职能比例提高',alternative='分类粒度、招聘写法、活动可同时出现；不能证明部门协作或行业独有',limits='可读广告中的分布；来源完整不等于招聘板全量',tables='H1_cross_function_sensitivity.csv;H1_sensitivity_envelope.csv;role_activity_bidirectional.csv',figures='F1_activity_roles.png',sources='inputs/stage_c/tables/T4_activity_lineage.csv'),
 dict(id='H1b',hypothesis='科研广告常同时要求工程实现；工程与质量、部署也有共同承担',scope='WHOLE23活动可判读1599；原文证据及分支核对',companies='23',ads='1599',P='研究工程65；工程质量301；工程部署235',N='1599（联合率）；66（研究正例条件率）',U='所选活动对关系未知0；来源不足31单列',metric='无条件共同承担；五状态互斥',result='65/66=98.48%的研究正例也承担工程；联合率65/1599=4.07%',status='SUPPORTED_DESCRIPTIVE',sensitivity='全部24为71/75；正文活动完整17为33/33；分职能及公司点值另表',counterexample='存在研究未与工程共同承担的广告；不把参与当本人承担',alternative='招聘职责多项并列，不等于生产过程中的先后依赖或效率互补',limits='未抽取普遍任务网络；仅三组预设活动对',tables='activity_joint_ad_status.csv;activity_joint_summary.csv;activity_joint_role.csv',figures='',sources='原广告职责原文及T4证据偏移'),
 dict(id='H2a',hypothesis='智元与银河通用制造应用下存在不同的招聘任务组合',scope='同波次整公司；案例产品背景与全公司招聘分开',companies='CN_AGIBOT;CN_GALBOT',ads='83;184',P='部署3;25',N='活动可读82;181；共同K23;37',U='来源1;3',metric='总体、同K自有权重、等权K、合并K权重',result='总体部署3.66%/13.81%；等权K 0%/16.67%',status='PARTIALLY_SUPPORTED_EXPLANATION',sensitivity='去明确校招/实习/接受应届者及重复职责后方向保持；来源极端界限不重叠；工程与科研部分比较换权重后反向',counterexample='智元有模型部署和端侧运行岗位；活动现场部署为零不代表没有部署相关工作',alternative='产品工作对象、渠道受众、资历与招聘时点可能共同作用',limits='K只有企业支持与ML两个职能；仅覆盖28.05%/20.44%，技术职能仅一个；非业务因果分解',tables='case_standardization_sensitivity.csv;case_common_role_coverage_sensitivity.csv;T5_case_work_object_evidence.csv',figures='F2_case1_weights.png',sources='ASTRA_E01;ASTRA_E02;NEW_GALBOT_01;N0401;N0384;N0098'),
 dict(id='H2b',hypothesis='自行持续运营履单服务应有更高部署活动占比',scope='Nimble履单网络与Dexterity装载系统有限对照',companies='US_NIMBLE;US_DEXTERITY',ads='34;31',P='部署13;15',N='34;30',U='来源0;1',metric='公司点值；共同K门槛',result='38.24%/50.00%；K=0，统一权重不适用',status='NOT_SUPPORTED_BY_THIS_PAIR',sensitivity='去同职责重复后35.48%/50.00%；Dexterity来源界限48.39%—51.61%',counterexample='自营履单的Nimble没有更高部署广告占比',alternative='履单IT对接、机器人现场运行与卡车装载产品不是同一对象；软件/ML分母均小于10',limits='反例只否定本样本的简单单调解释；不证明相反因果',tables='case_activity_sensitivity.csv;case_common_role_coverage_sensitivity.csv;T5_responsibility_long.csv',figures='F4_responsibility.png',sources='B_US_NIMBLE_002;ASTRA_E03;ASTRA_E04;B_US_DEXTERITY_002;B_US_DEXTERITY_003;N0925;N0918;N0882'),
 dict(id='H3a',hypothesis='同一ML/软件职能下技术、工具与任务对象组合各异',scope='固定35个职能标签组合×14语境；整公司ML156、软件180',companies='23（各格可解释公司另列）',ads='336',P='ML训练81；软件可靠性107；ML Python一般要求60',N='156；180；Python133',U='Python关系未知23；各格独立处理',metric='技术OWN_DEVELOP与技能GENERAL分开；UNCONDITIONAL分支',result='训练51.92%；可靠性59.44%；Python主率45.11%，极端界限38.46%—53.21%',status='SUPPORTED_WITH_SEMANTIC_LIMITS',sensitivity='公司等权、逐公司剔除、目录直接映射、来源完整、排除多产品、标签未知界限均列；不作总工具指数',counterexample='相同Python/PyTorch写法可用于训练、平台或推理；示例不是硬要求',alternative='原目录覆盖与要求语法影响可见频率；原文点读不能替代全量技能用途编码',limits='两个代表职能及固定目录；工作对象解读限18条案例证据',tables='Q2_fixed_coverage_unknown.csv;Q2_inherited_directory_product_sensitivity.csv;case_Q2_audience_template_unknown.csv;T5_case_work_object_evidence.csv',figures='F3_case1_q2.png',sources='原Q2语境与逐广告谱系；18条原文定位'),
 dict(id='H3b',hypothesis='跨本体模型公司有稳定的不同技术组合，可以作业务类型排名',scope='既定3家公司模型/软件组',companies='3；逐一剔除后2',ads='ML17；软件38（Field AI23）',P='ML训练14；软件可靠性27',N='17；38',U='格内未知和门槛逐次重算',metric='至少3家公司且20条可解释广告',result='ML组均值不许可；软件组主表许可但所有单公司剔除失去公司数门槛',status='INSUFFICIENT_EVIDENCE',sensitivity='剔除Field AI后软件2家15条；主分母集中60.53%',counterexample='不是所有有业务标签的公司组都支持汇总',alternative='单家公司贡献、样本规模、范围与产品形态混杂',limits='保留公司点值，不发布稳健组排名、不解释国家效应',tables='Q2_core_scope_leave_one_unknown.csv;Q2_fixed_coverage_unknown.csv',figures='',sources='固定分组与Q2门槛')
]
dump('T6_conclusions_sensitivity.csv',ledger)
print('T6',len(ledger),'envelopes',len(summary))
