from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0446':'硬件实习：协助及在岗学习不记本人负责；接口认识或使用经验两者均是一般知识经验，非接口任选。',
'N0475':'线束：本人可靠性设计、测试方案开发与运行故障策略有明确证据；通用CAD能力成立。',
'N0465':'嵌入式校招：参与职责保留；分支全属于嵌入式，但具体系统和通信协议仍可任选；测试脚本要求无任选连接词。',
'N0649':'集成实习：明确移植RTOS与HAL设计独立成立，其他参与/协助不扩；C/C++关系未知保留。',
'N0639':'Layout：PCB和完整性设计方法使用明确；具名EDA工具至少一种；DFM知识及职责独立定位。',
'N0626':'嵌入式实习：明确仪器使用可保留，学习Git不作熟练要求；各RTOS选项同实时上位。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for i in range(6):ov('N0446','2:'+str(i),'认识或使用经验都是一般要求，无协议之间的任选关系。',branch='EXAMPLE')
for e in ['O16','O17','O18','O19']:ov('N0446',e,'原文列举相关经历，没有或/至少一类等任选标记。',branch='UNCONDITIONAL')
for e in ['O16','O18']:ov('N0465',e,'MCU平台、RTOS与嵌入式Linux实践均属于嵌入式上位。',branch='UNCONDITIONAL')
ov('N0465','O20','测试、分析、调试脚本并列，没有任选标记。',branch='UNCONDITIONAL')
for e in ['O12','O13','O14']:ov('N0626',e,'FreeRTOS、RT-Thread或其他RTOS全为实时系统。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_hw_g')
