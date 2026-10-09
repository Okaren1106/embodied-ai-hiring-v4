from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0578':'培训COE本人设计培训体系与课程方案，课程开发为开发关系，不是仅执行既定课程；ADDIE保持目录外。',
'N0569':'机器人课程本人设计课程，不是操作课程所讲机器人；任职要求可有机器人知识，开发目录与教学对象不混淆。',
'N0556':'研发财务BP：成本测算不是明示财务建模，协同完善ERP不是本人用ERP；会计准则和核算主责另有证据。',
'N0258':'资料脱敏为信息保护非技术安全；Git/SVN斜杠仍未解，配置与资料操作规范可单记SOP。',
'N0302':'科技视觉PPT/Keynote斜杠关系未解，不能从PPT美化标题反推唯一工具；Python是加分例示。',
'N0246':'战略方法BLM/BSC/OKR/KPI未单列；战略校准不当系统标定，保留PPT呈现要求。',
'N0244':'费用会计明确核算主责与准则要求，学历字段不代替能力；费控系统维护对象明确。',
'N0319':'财务BP工具例示与ERP泛称斜杠分开；证书上位确定但CPA未知，学历和证书不能直接替会计核算方法。',
'N0276':'投资者关系估值营收预测知识未明示建模方法，不依据职位补值，记录目录覆盖有限。',
'E0290':'政府事务政策法规知识明确，可计法律专业要求；一般办公软件不可补成Microsoft Office。',
'E0243':'专利职责和知识要求明确；代理资格或司法考试均属法律资格上位，保持通过考试与持证原文区别。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0578','O1','提供定制化培训方案属于本人课程设计。',metric='DUTY_OWN_DEVELOP')
ov('N0569','O1','负责课程内容设计，明确开发课程。',metric='DUTY_OWN_DEVELOP')
ov('N0556','O2','费用测算与财务评估未明示建立财务模型。',metric='SEPARATE',branch='FINANCIAL_ASSESSMENT_NOT_MODELING')
ov('N0556','O3','协同完善ERP核算维度，不等于本人独立使用系统。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0556','2:0','财会经济学历专业不是核算技能证据。',metric='SEPARATE',branch='FIELD_OF_STUDY')
ov('N0556','2:1','各证书均属财会资格，上位明确。',branch='UNCONDITIONAL')
for e in ['7:0','7:1']:ov('N0556',e,'Tableau/Power BI/SQL斜杠未解，与SQL同口径。',branch='UNRESOLVED')
add('N0556','V2_ACCOUNTING','DUTY_OWN_USE','UNCONDITIONAL','落实研发费用加计扣除、高企申报、政府项目申报等财税合规工作','财税实际职责明确。')
ov('N0258','O1','客户信息与技术参数脱敏属信息治理，不是目录安全工程主题。',metric='SEPARATE',branch='INFORMATION_GOVERNANCE')
ov('N0258','2:0','Git/SVN关系未解。',branch='UNRESOLVED')
add('N0258','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','搭建并运维研发配置管理规范（版本控制规则、命名规范、存取权限等），从源头防止新增资料混乱','明示资料配置操作规范建设。')
ov('N0302','O1','PPT/Keynote斜杠未解。',branch='UNRESOLVED')
ov('N0244','3:0','学历专业非核算方法能力。',metric='SEPARATE',branch='FIELD_OF_STUDY')
ov('N0319','2:0','学历专业非核算方法能力。',metric='SEPARATE',branch='FIELD_OF_STUDY')
ov('N0319','3:0','单有证书不转记核算方法知识。',metric='SEPARATE',branch='CREDENTIAL_OBJECT')
ov('N0319','3:1','斜杠全部选项均属财会资格，上位明确。',branch='UNCONDITIONAL')
for e in ['6:0','6:1','6:2']:ov('N0319',e,'如和等明示例示，无或任选。',branch='EXAMPLE')
add('E0290','V2_LEGAL','GENERAL','UNCONDITIONAL','熟悉政府运作流程和相关政策法规，具备一定的政策分析能力','岗位明示相关法规专业理解；不推断任何具体法律。')
ov('E0243','2:1','两个选项均属法律资格，细节保留原文。',branch='UNCONDITIONAL')
R['N0246']['catalog_gap_notes']=['公司战略解码BLM/BSC/OKR/KPI未在冻结目录单列；不能把工具少解释为方法弱。']
R['N0276']['catalog_gap_notes']=['基本估值、营收预测和投资者关系活动目录覆盖有限；不得据少量或零工具得出技能需求弱。']
register(list(R.values()),'Astra_v3_boundary_corporate_b')
register([dict(reading_id='N1007',review_mode='FOLLOWUP',judgment='更正上一条解释措辞：V2_CALIBRATION适用于公司支持职能，但此广告仅写楼宇设备校准，未确定为目录列出的传感器、关节、运动学或测试仪器；所以保留不补标。')],'Astra_v3_facilities_calibration_scope_note')
