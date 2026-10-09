from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0658':'生产运维云平台职责斜线未解，任职至少一种则明确任选；监控工具无示例词。',
'N0654':'灵巧手应用含控制/示教功能；参与联调测试与直接开发区分，上层仿真要求明确。',
'N0021':'后台语言数据库至少一种，Redis由和连接；Kafka斜线未解。',
'N0095':'C与C++均明确；Linux/Unix未知保留，网络协议以等列举。',
'N0173':'中间件参与工作与本人数据闭环/HIL建设分开，工具链目标不等于控制方法。',
'N0009':'校招参与系统研发；测试和仿真均是协作支持表述。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['3:0','3:1','11:0']:ov('N0658',e,'不同云平台或Shell/Python之间裸斜线未解。',branch='UNRESOLVED')
for e in ['7:0','7:1']:ov('N0658',e,'括号明确并列，无示例词。',branch='UNCONDITIONAL')
for e in ['O1','O2','2:0','2:1','2:2']:ov('N0654',e,'多个通信协议裸斜线未解。',branch='UNRESOLVED')
for e in ['O12','O13','1:0']:ov('N0654',e,'应用功能包括且以等列举。',branch='EXAMPLE')
for e in ['O16','O19','O32']:ov('N0654',e,'联合团队/参与测试平台保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O27','O28','O29']:ov('N0654',e,'具体仿真工具未解不影响明确的上层仿真经验。',branch='UNCONDITIONAL')
for e in ['7:0','7:1','7:2','7:3']:ov('N0654',e,'至少一种和等共同修饰总线协议。',branch='CHOICE_AND_EXAMPLE')
ov('N0021','2:3','Redis由和缓存单列，不属于数据库任选。',branch='UNCONDITIONAL')
ov('N0021','7:0','Kafka/RabbitMQ/RocketMQ裸斜线未解。',branch='UNRESOLVED')
ov('N0095','4:0','协议列表以等结尾。',branch='EXAMPLE')
for e in ['O1','O2','O6','O7']:ov('N0173',e,'参与/支持开发保留协作承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0173','O8','控制是工具链所支持模块，未明本人控制方法使用。',metric='SEPARATE',branch='TOOLCHAIN_TARGET')
for e in ['O3','O4']:ov('N0009',e,'协助测试、协作支持仿真不升级独立直接承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
register(list(R.values()),'Astra_v3_boundary_sw_d')
