from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0104':'整机测试：感知导航规划机械性能为被测对象；可靠性老化有明确测试方法，不把AI编程工具理解为模型训练。',
'N0128':'招标采购：法规为广告中实际流程知识，不解释法律现行效力；SRM/ERP跨类别斜线未知。',
'N0105':'硬件和数据采购：数据资产为采购对象，安全合规与法律审查是本人责任；没有推成模型训练或集群运维。',
'N0005':'传感器验收：独立执行和独立编写计划清楚，协助设计另列；ROS/ROS2未知，点云与融合均属感知上位。',
'N0069':'发布测试：RTOS或裸机均为嵌入式上位；实时子项任选仍保留，通信裸斜线未知。',
'N0116':'软件研发质量：阶段评审风险管理有据，ISO9001优先；CMMI未合并进入ISO类别。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O4','O5','O6','O7']:ov('N0104',e,'对应算法和机械性能明确为被测对象，不证明本人使用相应算法或机械设计方法。',metric='SEPARATE',branch='TEST_OBJECT')
for e in ['O4','O5']:ov('N0005',e,'ROS与ROS2单独建类，裸斜线没有解除内层关系不清。',branch='UNRESOLVED')
for e in ['O12','O13']:ov('N0005',e,'点云处理与IMU融合均为感知概念，上位无任选。',branch='UNCONDITIONAL')
R['N0005']['additions'].append(dict(code='TC_EVALUATION',metric='DUTY_OWN_DEVELOP',branch='EXAMPLE',quote=RAW[RID['N0005']]['full_description'].splitlines()[7],reason='本人编写测试计划等文档，测试计划为开放文档列表的一项。'))
for e in ['O7','O9','O10']:ov('N0069',e,'实时系统与裸机均为嵌入式系统上位。',branch='UNCONDITIONAL')
for e in ['8:0','8:1','8:2','8:3']:ov('N0069',e,'UART/I2C/SPI/CAN跨协议裸斜线关系不清。',branch='UNRESOLVED')
register(list(R.values()),'Astra_v3_boundary_mfg_f')
