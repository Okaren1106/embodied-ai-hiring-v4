from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0950':'核对FAR科学相似广告实际差异：基础模型或LLM上位明确；sim2real在本人研究句实际出现，不接受候选器旧拒绝理由。',
'N0945':'逐项核对与N0950相同证据及本广告身份；语言任选不取消上位编程，PyTorch/JAX和Unix/Linux仍未解，FAR保持单列。',
'E0357':'Staff研究岗要求错引职责需修；IL、RL与操作优先改实际语句，Sim2Real在Bonus段，团队方法标准可独立开发。',
'N0961':'FAR硬件科学：系统辨识与Sim2Real研究明示，旧候选误拒；HIL只是帮助技术方向，不能记独立执行。',
'N0958':'FAR另一硬件科学广告，保留独立身份和协议要求差异；CAN/EtherCAT/RS485为Preferred括号例示，不是一般任选。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
for r in ['N0950','N0945']:
 ov(r,'O4','任何选项都为编程语言，上位明确。',branch='UNCONDITIONAL')
 for e in ['O18','O19']:ov(r,e,'foundation models或LLM均为上位基础模型。',branch='UNCONDITIONAL')
 ov(r,'O13','efficient model inference在for example清单中。',branch='EXAMPLE')
 add(r,'V2_SIM2REAL','DUTY_OWN_DEVELOP','EXAMPLE','for example open-vocabulary panoptic scene understanding, scaling up multi-modal LLMs, sim2real/real2sim techniques, end-to-end vision-language-action models, efficient model inference, video tokenization','本人独立研究明确包含仿真现实迁移；旧拒绝理由与原文冲突。')
for e in ['O16','O17']:ov('E0357',e,'原误引职责，改实际一般经验任选句。',metric='GENERAL',branch='CHOICE',quote='3+ years of hands-on experience developing and deploying learning-from-demonstration, reinforcement learning, imitation learning, foundation models, or related robot learning systems in real-world or simulated robotics environments')
ov('E0357','O20','原任选经历不足以支持无条件IL；另句明确LFD工具，重锚。',metric='GENERAL',quote='Experience with modern learning-from-demonstration tools such as DiffusionPolicy.')
for e in ['O26','O27']:ov('E0357',e,'原误引职责，改Bonus中RL和操作经验。',metric='PREFERRED',quote='Experience with modern reinforcement learning techniques for locomotion, manipulation, and whole-body control')
ov('E0357','4:0','Bonus段仿真现实迁移。',metric='PREFERRED')
for r in ['N0961','N0958']:
 ov(r,'3:0','Contribute to strategy and help shape包括HIL，属于协作方向，不是独立测试执行。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
 ov(r,'O18','HIL句协作；本人其他实验评价在day in life有明确责任，重锚该句。',metric='DUTY_OWN_USE',quote='Design and implement innovative systems and algorithms, leveraging our extensive computational and robotics hardware infrastructure to prototype and evaluate at scale')
 add(r,'V2_SYSID','DUTY_OWN_DEVELOP','EXAMPLE','including robot co-design, manipulation mechanisms, innovative actuation and motor control strategies, state estimation, low-level control, system identification, reinforcement learning, and sim-to-real transfer','独立研究列表实际明示系统辨识。')
 add(r,'V2_SIM2REAL','DUTY_OWN_DEVELOP','EXAMPLE','including robot co-design, manipulation mechanisms, innovative actuation and motor control strategies, state estimation, low-level control, system identification, reinforcement learning, and sim-to-real transfer','独立研究列表实际明示仿真现实迁移。')
ov('N0961','9:0','Basic Qualifications段，不是Preferred。',metric='GENERAL')
for e in ['O2','O3']:ov('N0961',e,'such as与or并存。',branch='CHOICE_AND_EXAMPLE')
ov('N0958','7:0','Basic Qualifications段。',metric='GENERAL')
ov('N0958','O4','所有选项都是编程语言，上位无条件。',branch='UNCONDITIONAL')
for e in ['9:0','9:1','9:2']:ov('N0958',e,'Preferred段括号列举协议，无or。',metric='PREFERRED',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_science_b')
