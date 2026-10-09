from astra_review_tools import *
ids=['E0103','N0471','N0512','N0059','N0299','E0488']
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ids}
for r in ['N0822','N0528']:R[r]=dict(reading_id=r,review_mode='FOLLOWUP',judgment='',evidence_overrides=[],additions=[])
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['E0103']['judgment']='明确多传感融合、标定、定位建图与规划；传感器组合不推具体未出现软件。交付效率稳定性是交付过程目标，不等于机器人系统可靠性开发。'
ov('E0103','E0103:O5','此处稳定性修饰项目交付，与系统可靠性/寿命/故障目标不同。',metric='SEPARATE',branch='DELIVERY_PROCESS_GOAL')
R['N0471']['judgment']='VLIO与重定位研发明确，感知学历不计方法要求。跟进验证不能直接认定执行测试。Ceres/g2o为普通并列，不能凭括号推or；视觉/LiDAR/IMU标定对象斜线保持未知。'
ov('N0471','N0471:O7','硕士的专业研究方向是学历背景。',metric='SEPARATE',branch='EDUCATION_FIELD')
ov('N0471','N0471:O6','跟进技术指标验证未明确本人执行测试，责任保留未知。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
for eid in ['N0471:11:0','N0471:11:1']:ov('N0471',eid,'Ceres、G2O普通并列，无or、如或等；括号本身不等于任选。',branch='UNCONDITIONAL')
for eid in ['N0471:O9','N0471:9:0']:ov('N0471',eid,'视觉/LiDAR/IMU标定对象关系未解，限定此普通要求语境。',branch='UNRESOLVED')
R['N0512']['judgment']='空间智能岗位明确算法研发；世界模型首段本人负责，参与清单不升级承担。特定方法至少一项、等、或及斜线逐条区分。模型轻量化未写压缩具体方法，维持排除；算法鲁棒性作为系统技术目标保留原概念。'
ov('N0512','N0512:1:0','首段负责世界模型相关算法研发，属于开发而非使用。',metric='DUTY_OWN_DEVELOP')
for eid in ['N0512:2:0','N0512:2:1']:ov('N0512',eid,'参与方向清单未明确本人承担该方法。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0512','N0512:3:0','优化3DGS/神经渲染算法属于开发，斜线方法关系未解。',metric='DUTY_OWN_DEVELOP',branch='UNRESOLVED')
ov('N0512','N0512:4:0','至少一个方向，保留任选。',branch='CHOICE')
for eid in ['N0512:7:0','N0512:15:0']:ov('N0512',eid,'经验清单含明确或。',branch='CHOICE')
for eid in ['N0512:8:0','N0512:19:0']:ov('N0512',eid,'等引出的具体方法/技术示例。',branch='EXAMPLE')
for eid in ['N0512:O44','N0512:O45']:ov('N0512',eid,'高精定位或高精地图等经验清单含or。',branch='CHOICE')
add('N0512','V2_3D_RECONSTRUCTION','DUTY_OWN_DEVELOP','UNCONDITIONAL','负责三维重建、生成式场景建模、世界模型与空间表征相关算法研发','明确本人研发重建算法，区别一般三维资产建模。')
R['N0059']['judgment']='本人视觉算法开发成立；少样本/零样本方法位于包括但不限于清单且内部斜线未解，不可记ML无条件开发。Python与C++是and不是C/C++。'
ov('N0059','N0059:O5','少样本/零样本学习的具体方法分支未解决。',branch='UNRESOLVED')
R['N0299']['judgment']='轮式SLAM、状态估计和实机验证明确；现场调试属于研发迭代，未当在役服务。CUDA等是例子，图优化库普通并列不是任选；Kalman上位因子图知识另有无条件支持。'
ov('N0299','N0299:O6','CUDA、NEON等是优先经验示例。',branch='EXAMPLE')
for eid in ['N0299:18:0','N0299:18:1','N0299:18:2']:ov('N0299',eid,'括号列g2o、Ceres、GTSAM普通并列，无or或例示词，不假定任选。',branch='UNCONDITIONAL')
add('N0299','V2_KALMAN_FACTOR','GENERAL','EXAMPLE','精通EKF、UKF、ESKF等滤波算法','滤波具体子型为等示例，与因子图优化上位明确知识并存。')
R['E0488']['judgment']='定位、标定与评测开发明确，普通/硬性标题不可混用。动捕估计问题是已捕获数据/算法对象，不证明操作采集。SLAM优先证据改到正确条款，补深度学习重建经验路径。'
ov('E0488','E0488:4:0','Required Qualifications支配传感器标定经验。',metric='REQUIRED')
ov('E0488','E0488:5:0','human motion capture or AR/VR estimation是估计问题研究对象，未明确本人动作采集。',metric='SEPARATE',branch='MOCAP_DATA_PROCESSING')
ov('E0488','E0488:O11','原引用误指职责标定开发，改为Required段实际标定能力句。',metric='REQUIRED',quote='Hands-on experience with sensor calibration (e.g., multi-camera and IMU intrinsics/extrinsics).')
ov('E0488','E0488:O14','原引用误指Required段；实际优先SLAM任选来自Bonus段应用对象。',metric='PREFERRED',quote='Experience applying state-of-the-art Deep Learning approaches to SLAM, 3D reconstruction, or human pose estimation.')
add('E0488','V2_3D_RECONSTRUCTION','PREFERRED','CHOICE','Experience applying state-of-the-art Deep Learning approaches to SLAM, 3D reconstruction, or human pose estimation.','明确深度学习三维重建方法经验，任务对象以or任选。')
R['N0822']['judgment']='按冻结TC_RELIABILITY定义回改：技术概念包含明示系统可靠性目标，不强制出现可靠性测试方法；本人把算法变成可靠机器人能力有据。'
ov('N0822','N0822:O17','冻结定义包含系统可靠性目标，不能用V2专业方法的更窄标准删除机器人可靠能力的明确工作目标。',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL')
R['N0528']['judgment']='进一步区分三维资产制作与特定重建方法；照片与尺寸建模可能为手工资产还原，不能确定3DGS/辐射场等方法本人使用。相应新增使用/一般能力改未知；明确3DGS/NeRF优先经验另保留。'
R['N0528']['transaction_overrides']=[dict(target_batch='Astra_audit_open_items_closed',target_addition_index=i,metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=[m],reason='一般照片/尺寸资产还原不能确定冻结三维重建方法，保留对象未知。') for i,m in [(5,'DUTY_OWN_USE'),(6,'GENERAL')]]
register(list(R.values()),'Astra_perception_fullread_a_and_consistency')
