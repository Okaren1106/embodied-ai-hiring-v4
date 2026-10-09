from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0330':'灵巧手嵌入式：正文通用模块开发，不能仅按标题推抓取；本人验证与协助测试分别明确。',
'N0328':'传感器嵌入式：协议斜线保留未知，标题不自动补感知；模块功能验证本人承担。',
'E0069':'中央域控：Linux内核和ROS知识是一般要求，端云存储加密明确；通用AI工具不强推具名模型。',
'E0099':'硬件电路：PCB是应用设计方法，不能因开发电路判为开发PCB方法；EMC方法与测试执行有直接证据。',
'E0302':'MCU：软件设计与仪器调优分列；调优电机启停不等同开发执行器本体。',
'E0298':'SoC Linux：明确内核/驱动及系统开发，视频采集不自动推视觉算法；正文尾优先稳定性要求可用。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('E0099','O1','PCB为工程设计方法，设计实体电路板是方法使用。',metric='DUTY_OWN_USE')
ov('E0302','O6','利用仪器解决电机抖动为调试使用，未说明开发执行器本体。',metric='DUTY_OWN_USE')
register(list(R.values()),'Astra_v3_boundary_hw_j')
