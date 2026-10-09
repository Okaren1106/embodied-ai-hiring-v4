from astra_review_tools import *
R={}
def rr(r):
 if r not in R:R[r]=dict(reading_id=r,review_mode='FOLLOWUP',judgment='已知规则跨批一致性回查；只修订下列有明确来源的判读，不增加全文阅读或独立编码声明。',evidence_overrides=[],additions=[])
 return R[r]
def ov(r,e,why,**f):rr(r)['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
for r,es in {'N0915':['O10'],'N0942':['O13'],'E0360':['O15','O16'],'E0476':['O7'],'N0977':['O9']}.items():
 for e in es:ov(r,e,'明确本人测试/仿真该技术对象，应计技术使用而非本体开发；纠正此前过窄排除。',metric='DUTY_OWN_USE',branch='UNCONDITIONAL')
ov('N0977','O9','设备及机械工装验证，恢复完整可定位句。',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote=ln('N0977',14))
ov('N0977','O8','本人制作工装并测试电机执行器，保留使用而非开发本体。',metric='DUTY_OWN_USE',branch='UNCONDITIONAL')
for e in ['O11','O12','O13']:ov('N0325',e,'同句不仅采购，还明确本人测试关键参数；等为示例。',metric='DUTY_OWN_USE',branch='EXAMPLE')
ov('N0325','ADD1','撰写设计/测试文档不等于开发评测方法。',metric='SEPARATE',branch='DOCUMENTATION_OBJECT')
for e in ['O17','O29']:ov('E0360',e,'台架可编程电源是仪器，未明示功率电路或供电工程能力。',metric='SEPARATE',branch='BENCH_INSTRUMENT')
ov('E0502','3:0','机械排障在Requirements，且可由机器人经历替代。',metric='GENERAL',branch='CHOICE')
rr('E0502')['additions'].append(dict(code='TC_MECHANICAL',metric='GENERAL',branch='CHOICE',quote=ln('E0502',14),reason='机械系统排障经验是一般资格的一种备选。'))
rr('N1029')['transaction_overrides']=[dict(target_batch='Astra_v3_boundary_deploy_c',target_addition_index=3,metric='SEPARATE',branch='GENERIC_VERSION_CONTROL_NOT_GIT',reason='冻结Git项要求命名工具或别名；泛version control不证明Git。')]
for e in ['1:0','8:0']:ov('N0063',e,'已有动捕数据的处理/格式知识不证明本人使用动作捕捉设备或执行采集。',metric='SEPARATE',branch='MOCAP_DATA_OBJECT')
ov('N0063','O13','如实时动作驱动是具体需求示例。',branch='EXAMPLE')
ov('N0405','O5','明确的是低延迟SFU架构，低延迟不自动等于实时约束。',metric='SEPARATE',branch='LATENCY_NOT_EXPLICIT_REALTIME')
rr('E0177')['additions'].append(dict(code='V2_TCPIP',metric='PREFERRED',branch='UNCONDITIONAL',quote=ln('E0177',30),reason='冻结别名明确包含UDP，旧拒绝理由与目录不符。'))
rr('N0942')['transaction_overrides']=[dict(target_batch='Astra_v3_boundary_sim_b',target_addition_index=1,metric='SEPARATE',branch='DEVELOPMENT_TEST_DEBUG',reason='冻结故障处理项限运行中恢复；此处明确台架和原型测试开发调试，不因root-cause字样扩大定义。')]
ov('N0693','O12','控制器与planner由本人编写，控制开发保持。',metric='DUTY_OWN_DEVELOP')
rr('N0693')['additions'].append(dict(code='TC_MOTION_PLANNING',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote=ln('N0693',8),reason='本人write planners；与N0692正文差异必须保留。'))
register(list(R.values()),'Astra_v3_final_rule_consistency')
