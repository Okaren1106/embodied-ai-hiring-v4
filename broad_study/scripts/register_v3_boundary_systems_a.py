from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0367':'声学系统独立设计与算法配合分开；音频仪为示例，供应商技术对接不是采购。逐项核对工具任选、例示和加分段。',
'E0567':'执行器集成岗：协作标定与本人测试开发分开；总线均在Bonus，Serial依冻结串口别名范围保留；修复误引职责的要求证据。',
'E0568':'灵巧手Own calibration不同于执行器岗Collaborate；本人开发测试工具明确，团队集成嵌入式为协作；修复Bonus总线和错引要求。',
'N0806':'整个人形系统集成岗位；校准工具链经历位于加分段任选列举，接口定义属于系统工程方法；不把纯仿真背景排除条件转成技术负值。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for e in ['O6','O7','20:0','20:1']:ov('N0367',e,'等与或/至少一种并存。',branch='CHOICE_AND_EXAMPLE')
for e in ['4:0','4:1','24:0','26:0','30:0']:ov('N0367',e,'明确等列举，没有任选连接词。',branch='EXAMPLE')
ov('N0367','8:0','配合算法团队完成标定。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0367','15:1','供应商技术对接未写采购、寻源或合同职责。',metric='SEPARATE',branch='TECHNICAL_VENDOR_INTERFACE')
for r in ['E0567','E0568']:
 ov(r,'O7','Collaborate明确协作，不能认作本人独立开发执行器。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
 ov(r,'O19','原引职责段，改实际一般要求。',metric='GENERAL',quote='mechanics, kinematics, controls, dynamics and sensor technologies')
 ov(r,'O11','本人开发故障回退诊断算法，重锚可靠性开发，而非由测试合格目标推出。',metric='DUTY_OWN_DEVELOP',quote='Develop real-time diagnostic algorithms to enable fall-back strategies.')
 prefix='6:' if r=='E0567' else '5:'
 for n in range(4):ov(r,prefix+str(n),'Bonus段like列举总线，不能作一般任选。',metric='PREFERRED',branch='EXAMPLE')
 add(r,'V2_RS485','PREFERRED','EXAMPLE','Working knowledge of communication buses and protocols like Ethernet, Ethercat, Serial, SPI and I2C.','Serial为串口的英文表达；冻结别名含串口与RS232，只能解释为该宽目录，不能推出特定RS-485物理协议。')
ov('E0567','2:0','Collaborate on calibration，明确协作。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0567','O22','原引职责，实际Bonus具备执行器建模能力。',metric='PREFERRED',quote='Numerical and first-principles modeling capabilities for actuators.')
add('E0567','TC_EVALUATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Build scripts, dashboards and automated test rigs to streamline repetitive testing, data collection and diagnostics','本人构建评测工具明确。')
ov('E0568','2:0','Own calibration strategies明确制定策略。',metric='DUTY_OWN_DEVELOP')
ov('E0568','O10','原引用标定而非评测开发，改明确测试工具开发句。',metric='DUTY_OWN_DEVELOP',quote='Build scripts, dashboards and automated test rigs to streamline repetitive testing, data collection and diagnostics')
ov('E0568','O12','Work with其他团队集成嵌入式，不能推出独立开发。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0568','O14','原引职责，改实际一般经验任选句。',metric='GENERAL',branch='CHOICE',quote='with a focus on actuation, manipulation or integration;')
ov('N0806','4:0','What Sets You Apart内工具列举有or。',metric='PREFERRED',branch='CHOICE_AND_EXAMPLE')
add('N0806','V2_REQUIREMENTS_ENGINEERING','DUTY_OWN_DEVELOP','UNCONDITIONAL','Define and maintain interfaces across autonomy, manipulation, locomotion, sensors, compute, controls, and field tools.','本人定义跨子系统接口，符合系统工程目录。')
register(list(R.values()),'Astra_v3_boundary_systems_a')
