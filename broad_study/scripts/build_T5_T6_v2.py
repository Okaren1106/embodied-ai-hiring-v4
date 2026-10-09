"""Build integrated T5/T6 after Q2 completion."""
from common import *
from datetime import datetime, timezone
ads=read(ROOT/'tables/Q3_adjudicated_ads_partial.csv')
disp=read(ROOT/'tables/Q4_display_items.csv')
cov=read(ROOT/'tables/Q1_role_coverage.csv')
t5=[]
t5.append(dict(item_id='T5_Q2_SCOPE',topic='Q2范围',scope='17 concrete roles, 1576 ads',evidence='Q3_adjudicated_ads_partial.csv',finding='全部17类完成首轮全文编码与分层比较资格判定',limit='复合/任选/歧义/来源不足不拆入单职能分母',sensitivity='FAR单列；S1–S3为不同范围'))
t5.append(dict(item_id='T5_O_PRODUCT_UNKNOWN',topic='产品归属',scope='84 ML+software ads in 4 companies',evidence='O4_attribution_seniority_unknown.csv',finding='81/84条产品未知，3条能直接连到命名产品',limit='不以公司品牌补产品',sensitivity='对象多值不可相加'))
t5.append(dict(item_id='T5_D_GALBOT_FIGURE',topic='构成分解',scope='Galbot×Figure K=4',evidence='D2_decomposition_summary.csv MAIN FIXED_K ACT_ENGINEERING',finding='工程Δ=+11.10pp，构成+19.45，职能内−8.35',limit='算术分量非因果',sensitivity='S1–S3因Galbot退出为NA；等权可反向'))
t5.append(dict(item_id='T5_DEPLOYMENT_OBJECT',topic='部署活动对象',scope='ACT_DEPLOYMENT',evidence='R A01; O reports',finding='部署与维护含模型/平台对象',limit='不能整体改称客户现场',sensitivity='客户现场须另用对象证据'))
t5.append(dict(item_id='T5_Q2_RESEARCH_OPS',topic='稀疏职能',scope='research science; robot ops',evidence='Q1_role_coverage.csv',finding='无L3组汇总格',limit='POINTS_ONLY',sensitivity='加公司也不保证任务可比'))
for r in disp:
    if r['role'] in ('RF_ML_AI_ENGINEERING','RF_ROBOTICS_SOFTWARE','RF_DEPLOYMENT_FIELD_SERVICE') and r['label_code'] in ('SK_PYTHON','SK_LINUX','SK_CPP','V2_INCIDENT_SUPPORT'):
        t5.append(dict(item_id='T5_Q2_'+r['role']+'_'+r['label_code'],topic='主图项',scope='WHOLE23 GENERAL UNCONDITIONAL',evidence='Q4_display_items.csv',finding=f"{r['label_name']} P/N={r['P']}/{r['N']} ad={r['share_ad_weighted']} eq={r['share_company_equal']} dominance={r['dominance_warning']}",limit='探索性；C/C++未知另见Q4_unknown_bounds',sensitivity='leave-one-out; S1–S3'))
dump('tables/T5_integrated_v2.csv', t5)
t6=[
 dict(conclusion_id='R_T6_01',question='Q1',status='SUPPORTED_DESCRIPTIVE',wording='制造、软件、ML是本目录下样本广告总量前三；不能推断行业总体人才结构',sensitivity='等权/加权接近',counterexample='机器人操作等权高于加权'),
 dict(conclusion_id='R_T6_02',question='Q3',status='SUPPORTED_DESCRIPTIVE',wording='整公司研究/部署与维护/质量活动位于专门职能之外分别48/66、264/343、300/459',sensitivity='ALL24与S1方向一致',counterexample='同名职能不是空集'),
 dict(conclusion_id='R_T6_03',question='Q3',status='ADJUDICATED',wording='争议格复核后共同承担成立，整公司三对65、301、235/1599',sensitivity='关系未知0',counterexample='共现不是流程依赖'),
 dict(conclusion_id='R_T6_04',question='Q2v1',status='SUPPORTED_WITH_CATALOG_LIMITS',wording='原两职能v1读数保留；来源筛选改变组成',sensitivity='v1固定35项',counterexample='v2新口径不是v1纠错'),
 dict(conclusion_id='R_T6_05',question='BUSINESS',status='SUPPORTED_FACTS_WITH_UNKNOWN_RESPONSIBILITIES',wording='龙旗支持智元G2使用与共同开发；宁德时代支持银河通用S1产线使用；付款与全部运维未知',sensitivity='材料早于招聘观察日',counterexample='招聘缺失不反推外包'),
 dict(conclusion_id='R_T6_06',question='EXPLANATION',status='SUPPORTED_WITH_COMPLETED_O_D_Q',wording='对象、受众及构成分析已完成：84条多数产品未知；Galbot×Figure工程分解+11.10/+19.45/−8.35；Q2十七类均有L0及可行层级结果',sensitivity='S1–S3、等权/加权、未知边界、精确重复职责',counterexample='研究科学与机器人操作无L3'),
 dict(conclusion_id='Q_T6_01',question='Q2',status='SUPPORTED_DESCRIPTIVE',wording='17类1,576条完成编码；目录保持Q2-v2.1；研究科学与机器人操作无组汇总主图',sensitivity='L0全覆盖不等于L3',counterexample='硬件覆盖21家但广告分散'),
 dict(conclusion_id='Q_T6_02',question='Q2',status='EXPLORATORY_CELL_SPECIFIC',wording='整公司一般要求下ML Python 60/135、软件Linux 70/177、控制闭环52/75；C++未知宽',sensitivity='未知赋值、逐一剔除、S1 29/71',counterexample='部署Python被Field AI主导'),
 dict(conclusion_id='Q_T6_03',question='Q2',status='NOT_A_TASK_EQUIVALENCE',wording='同主职能不同任务子类不可解释为同一任务的技术选择',sensitivity='Q4_task_strata.csv',counterexample='制造测试88 vs 采购29；软件运行时87 vs 开发基础设施44'),
 dict(conclusion_id='Q_T6_04',question='Q2',status='CATALOG_LIMIT',wording='目录外2329条，本轮不发布v2.2',sensitivity='缺口审计',counterexample='FPGA任务存在但工具未入目录'),
]
dump('tables/T6_integrated_v2.csv', t6)
# refresh R_T6_06
rows=read(ROOT/'tables/R_T6_integrated_claims.csv')
for r in rows:
    if r['conclusion_id']=='R_T6_06':
        r['status']='SUPPORTED_WITH_COMPLETED_O_D_Q'
        r['wording']='工作对象、构成分解与Q2十七类可行比较已完成；多数广告产品未知；部署活动不能整体改称客户现场'
        r['tables']='O4_attribution_seniority_unknown.csv;D2_decomposition_summary.csv;Q4_display_items.csv;T6_integrated_v2.csv'
dump('tables/R_T6_integrated_claims.csv', rows)
save_json('verification/T5_T6_v2_receipt.json', dict(t5=len(t5),t6=len(t6),updated_utc=datetime.now(timezone.utc).isoformat()))
print('T5',len(t5),'T6',len(t6))
