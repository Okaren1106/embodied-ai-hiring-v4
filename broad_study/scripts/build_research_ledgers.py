from common import *
qc=json.loads((ROOT/'verification/astra_materialization.json').read_text(encoding='utf-8'))
t5=[
 dict(company_id='CN_AGIBOT',company='智元',scope='O固定框 ML12 软件7',evidence='O4_company_role_object.csv;O4_attribution_seniority_unknown.csv',judgment='ML模型策略12/12，软件机器人运行4/7；多模态模型和系统对象并存。',product_boundary='灵心有明确命名，其余不以G2补填。',delivery_boundary='客户/共研方资料是背景，不能分配每条广告的维护或付款责任。'),
 dict(company_id='CN_GALBOT',company='银河通用',scope='O固定框 ML24 软件25',evidence='O4_company_role_object.csv;D2_decomposition_summary.csv',judgment='ML模型策略22/24、数据12/24，软件机器人运行19/25；固定K工程分解+11.10=+19.45-8.35个百分点。',product_boundary='不能以S1客户材料归属全部广告。',delivery_boundary='实验室真机与客户生产现场不同；保留校招实习受众和参与型责任。'),
 dict(company_id='US_NIMBLE',company='Nimble',scope='O固定框 ML3 软件6',evidence='O4_company_role_object.csv;O2_evidence_long.csv',judgment='ML三条涉及数据；软件两条涉及履单业务，与机器人运行任务不同。',product_boundary='Cloud Logistics与Nimble Brain明确命名，其余保留未知。',delivery_boundary='自营履单责任不能推出所有软件广告都对应机器人部署。'),
 dict(company_id='US_DEXTERITY',company='Dexterity',scope='O固定框 ML5 软件2',evidence='O4_company_role_object.csv;O2_evidence_long.csv',judgment='模型全周期与基础设施、工程数据治理并存；软件仅两条，不作稳定公司均值判断。',product_boundary='不能以Mech公司介绍分配所有广告。',delivery_boundary='量小且对象异质，保持公司案例级解释。')]
dump('tables/T5_Astra_final.csv',t5)
claims=[
 ('A01','保留','跨职能活动','研究48/66、部署维护264/343、质量300/459位于同名职能之外。','WHOLE23 活动正例','R_cross_function.csv','活动不等于部门；部署包括模型与平台。'),
 ('A02','保留','共同承担','三组共同承担65、301、235/1599。','WHOLE23活动可判断范围','R_joint_summary.csv','共同岗位不证明流程因果。'),
 ('A03','保留','工作对象','84条中81条无命名产品归属。','固定四公司两职能','O4_attribution_seniority_unknown.csv','不以主打产品补未知。'),
 ('A04','保留','算术分解','工程总差+11.10，构成+19.45，职能内-8.35个百分点。','Galbot-Figure固定K','D2_decomposition_summary.csv','反向分量，不能发布因果贡献率。'),
 ('A05','条件保留','Q2扩展','17类1576条首轮编码；1552条为整公司主范围。','Q2-v2.1','Q4_role_coverage_final.csv','首轮覆盖不代表复核全部完成。'),
 ('A06','条件保留','同任务要求','机器人模型Python一般无条件40/90，U16；运行软件C++36/63，U24。','预设ROBOT_MODEL ROBOT_RUNTIME','Q5_prefixed_task_examples.csv','文本未知与内容误判是不同风险。'),
 ('A07','纠正','公司贡献','去掉Field AI后部署Python4/65，17有效公司仍通过组门槛。','WHOLE23 一般 无条件','Q4_leave_one_company_out_final.csv','广告加权敏感但不丧失许可。'),
 ('A08','纠正','比较资格','展示筛选和组比较资格逐格分开。','17职能22语境','Q4_display_selection.csv;Q4_task_strata_final.csv','不能笼统称小职能无组许可。'),
 ('A09','不接受','内容全部验收','实际全文复核'+str(qc['reviewed_full'])+'，种子'+str(qc['seeded_full_reviewed'])+'/340，强制'+str(qc['mandatory_reviewed'])+'/1208。','本轮Astra复核','Q3_review_receipts.csv','剩余复核不可冒充完成；队列互相重叠。'),
 ('A10','建议','扩样决策','先收口已有编码；新增公司应针对新研究问题和供给层不足。','研究设计判断','REPORT_Astra_final.md','20加20不是当前结论成立的必要条件。')]
dump('tables/T6_Astra_final.csv',[dict(conclusion_id=i,status=s,question=q,claim=c,scope=sc,evidence=e,limit=l) for i,s,q,c,sc,e,l in claims])
print('T5',len(t5),'T6',len(claims))
