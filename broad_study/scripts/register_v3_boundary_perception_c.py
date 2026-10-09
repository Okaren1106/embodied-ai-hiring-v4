from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0516':'轻图算法：所有斜杠经验选项都是定位建图，上位SLAM可确认；多传感器融合下位仍不可替所有选项。',
'N0522':'里程计：RNN/Transformer属ML上位，g2o/GTSAM及TensorRT/ONNX斜杠保留未知；量化是括号例示。',
'N0066':'激光SLAM：Ceres/GTSAM斜杠不能肯定任选；基础滤波因子图等方法与一般数学理论例示分别处理。',
'N0068':'视觉研发：支持RL及协同闭环不能记独立开发；一般要求的Sim2Real/域随机化误入Preferred，ONNX Runtime不推出格式。',
'N0615':'定位算法原文图优化方法可计现目录；滤波泛称本身不补成具体卡尔曼方法。',
'N0529':'正式感知岗本人评测体系和执行均有依据，开头参与传感器测试不独立；一般工具与加分工具错段已修。',
'N0527':'感知实习职责全部参与/协助，独立职责阳性撤回；Eigen/PCL在一般任选例示，滤波/标定加分皆有备选。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O4','O5','O7']:ov('N0516',e,'SLAM/融合建图/融合定位均属于上位定位建图经验。',branch='UNCONDITIONAL')
for e in ['O31','O32']:ov('N0522',e,'RNN/Transformer均为ML模型；如例示保持。',branch='EXAMPLE')
for e in ['5:0','5:1','13:0','13:1']:ov('N0522',e,'工具所在斜杠关系未解。',branch='UNRESOLVED')
ov('N0522','13:4','NEON、量化、TensorRT/ONNX为优化经验括号例示。',branch='EXAMPLE')
for e in ['5:1','5:2']:ov('N0066',e,'Ceres/GTSAM关系未解。',branch='UNRESOLVED')
for e in ['1:0','4:0']:ov('N0066',e,'等核心模块/基础理论例示方法。',branch='EXAMPLE')
for e in ['O13','O14','O15','O16']:ov('N0068',e,'支持技术研发并协同搭建，非独立本人开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0068','2:0','支持Sim2Real研发属于协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O32','O33','O34','O35']:ov('N0068',e,'与相关团队高效协作，技术为团队对象，不是本人技术知识要求。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['3:0','3:1','4:0']:ov('N0068',e,'等方法/工具是例示。',branch='EXAMPLE')
for e in ['6:0','6:1']:ov('N0068',e,'技能要求段具体开发经验，不是加分段。',metric='GENERAL')
ov('N0068','7:0','工作经验要求段有或。',metric='GENERAL',branch='CHOICE')
for e in ['8:0','8:2']:ov('N0068',e,'加分满足其一为任选祖先，工具等例示。',branch='CHOICE_AND_EXAMPLE')
ov('N0068','8:1','Runtime产品不能推出ONNX格式能力。',metric='SEPARATE',branch='RUNTIME_NOT_FORMAT')
add('N0615','V2_KALMAN_FACTOR','GENERAL','CHOICE','熟悉图优化或者滤波算法','图优化为明确备选方法；不假定泛称滤波必为卡尔曼。')
ov('N0529','O7','原参与测试，独立评测执行另句明确，重锚。',metric='DUTY_OWN_USE',quote='建立算法评测体系，完成数据采集、问题分析、精度评估和版本迭代；')
ov('N0529','O22','标定或嵌入式/深度学习经验的本句实际是标定或时间同步，不能无条件评价。',branch='CHOICE')
ov('N0529','O26','ARM、Jetson或其他嵌入式平台全属于嵌入式上位。',branch='UNCONDITIONAL')
for e in ['8:0','8:1']:ov('N0529',e,'等常用开发工具例示。',branch='EXAMPLE')
for e in ['11:0','11:1','11:2']:ov('N0529',e,'一般要求等至少一种工具，非Preferred。',metric='GENERAL',branch='CHOICE_AND_EXAMPLE')
ov('N0529','11:3','一般要求非线性优化或因子图工具，上位方法确定。',metric='GENERAL')
ov('N0529','20:0','内外参/在线标定或时间同步算法，是任选。',branch='CHOICE')
ov('N0529','23:0','NeRF/3DGS与其他视觉技术或模型是任选列举。',branch='CHOICE')
for e in ['O7','O8','O9','O10','O11','1:0']:ov('N0527',e,'职责明确参与或协助。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['3:0','3:1']:ov('N0527',e,'一般要求中或和等，非加分。',metric='GENERAL',branch='CHOICE_AND_EXAMPLE')
for e in ['11:0','14:0']:ov('N0527',e,'明确或备选。',branch='CHOICE')
ov('N0527','15:0','等或其他视觉基础模型，任选加例示。',branch='CHOICE_AND_EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_perception_c')
