from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0298':'轮式SLAM：激光或视觉框架都属SLAM上位，图优化库括号是例示而非任选；CUDA等例示。',
'N0293':'另一独立轮式SLAM广告正文语境一致，保留独立身份和排版；同工具框架边界同口径修正。',
'N0249':'导航感知：ROS/ROS2虽未解，但后半明确基于ROS开发经历可形成单独阳性；导航知识与规划接口理解保留。',
'E0150':'状态估计：输出标定报告不等于开发标定工具/数据管道；一般要求不误引职责，EKF/UKF上位仍受全句任选约束。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for r in ['N0298','N0293']:
 ov(r,'O6','CUDA、NEON等是例示。',branch='EXAMPLE')
 for e in ['O18','O19']:ov(r,e,'激光和视觉框架均属SLAM上位，不能标成上位任选。',branch='UNCONDITIONAL')
 for e in ['18:0','18:1','18:2']:ov(r,e,'括号列举图优化库，没有任选词。',branch='EXAMPLE')
add('N0249','SK_ROS','GENERAL','UNCONDITIONAL','有基于ROS的感知模块开发与调试经验','另句明确ROS经历，保留前面ROS/ROS2未知但正例可覆盖该格。')
ov('E0150','O9','输出数据质量评估属于评价使用而非开发评价方法。',metric='DUTY_OWN_USE')
ov('E0150','O10','输出文档与评估报告，不是数据管道开发。',metric='SEPARATE',branch='ASSESSMENT_REPORT_OBJECT')
ov('E0150','O17','原误引职责，改实际一般状态估计经验列表。',metric='GENERAL',branch='CHOICE',quote='熟悉EKF/UKF、惯性导航、SLAM或机器人状态估计。')
ov('E0150','4:0','输出标定文档不是开发标定工具，模块开发另有明确证据。',metric='SEPARATE',branch='CALIBRATION_REPORT_OBJECT')
ov('E0150','5:0','EKF/UKF虽同一上位，全句还有其他方法或状态估计经验。',branch='CHOICE')
register(list(R.values()),'Astra_v3_boundary_perception_d')
