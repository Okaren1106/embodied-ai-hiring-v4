from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0206':'PCB布局：DFM/DFA同属目录上位；SI/PI及EMC也属同一方法上位，不因具体名斜杠将上位能力未知；CIS仍元件数据非学习数据。',
'E0430':'FPGA桥接板：PCB标签是工程方法，设计板卡属于使用该方法；安全功能来自与感知团队合作，未证明本人安全技术开发。保留RTL/FPGA工具目录缺口。',
'N0666':'固件与电机控制：全部资格为Preferred；不同应用领域均要求固件开发，上位嵌入式不受应用任选影响；C/C++保留未解。',
'N0339':'硬件研究：明确完整PCB设计及EDA软件使用，工具例示、至少一种和热设计等分支有依据；参与可靠性试验不作独立执行。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('N0206','6:0','DFM/DFA均在V2_DFM定义和别名内。',branch='UNCONDITIONAL')
ov('N0206','19:0','SI/PI/EMC均为同一目录条目，知识或仿真皆体现该方法能力。',branch='UNCONDITIONAL')
ov('E0430','O1','SK_PCB定义为PCB设计工程方法；本人设计板卡是使用该方法，未说发明设计方法。',metric='DUTY_OWN_USE')
ov('E0430','O7','works closely with perception team to enable safety，属于协作目标。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('E0430','3:1','DFM/DFA同一上位方法，斜杠不影响该目录格。',branch='UNCONDITIONAL')
for e in ['O12','O15']:ov('N0666',e,'firmware development各应用领域都支持嵌入式上位。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_hw_a')
