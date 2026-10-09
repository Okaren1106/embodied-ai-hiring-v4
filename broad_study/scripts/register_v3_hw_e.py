from astra_review_tools import *
JUD={
'E0374':'真实设计验证夹具开发与测试执行并存。PCB/PCBA同属板设计方法，上位项经验可以判断；Altium可替代、LTspice例示和职责装配指南各自保留。',
'N0740':'个人嵌入式工作与宽团队介绍分开；Yocto和通讯协议列表为具体例示。诊断watchdog工具开发明确，优先标题空白没有截断证据，不凭相邻广告补要求。',
'E0465':'多板卡对象以like/or任选示例，未当每岗全覆盖；USB3/4都是USB版本，族存在可判，所在高速板卡括号仍例示。',
'E0533':'充电功率电路任务、PFC must与普通经验分开。EMI/EMC属于同一冻结方法族，可判一般要求；safety/compliance跨不同含义仍U，不外推。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[]) for r,j in JUD.items()}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
ov('E0374','E0374:O4','PCB与PCBA均属该板设计方法概念，designing/prototyping经验明确；不把同族斜线当上位未知。',branch='UNCONDITIONAL')
for eid in ['N0740:1:0','N0740:5:0','N0740:5:1','N0740:5:2','N0740:5:3','N0740:5:4','N0740:5:5']:
 ov('N0740',eid,'具体环境或协议位于上位对象后的括号列表，保留例示，不默认全部无条件。',branch='EXAMPLE')
for eid in ['E0465:1:0','E0465:1:1','E0465:ADD1']:
 ov('E0465',eid,'高速板对象后括号为具体协议例示；USB3/4两版本同属USB族，本项不再未知。',branch='EXAMPLE')
ov('E0533','E0533:2:0','EMI与EMC均在同一冻结电磁兼容方法族内，不因同族斜线使类别存在未知。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_hw_e')
