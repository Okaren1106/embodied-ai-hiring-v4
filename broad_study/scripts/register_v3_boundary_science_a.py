from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0414':'核对世界模型/C语言和要求分支：C/C++仍未解；世界模型项目与具身领域项目明确任选。',
'E0176':'核对后训练边界与要求错位：公司我们段不是本人职责/优先要求，重锚实际工作及要求；真机验证是执行。',
'N0351':'核对工具斜杠及至少一项研究经历，Python/C++/MATLAB和TF/PyTorch关系未知；ROS为工具清单例示。',
'N0411':'补读省略标题确认必备技术背景；参与或主导造成承担关系未解，VLA/多模态及工具斜杠保留真实分支。',
'N0374':'核对世界模型/重建及资格语境：一般/优先多处错引职责，改实际要求；编程与框架斜杠不能凭等字视作确定例示。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
ov('N0414','9:0','世界模型或具身领域主导项目，世界模型为任选。',branch='CHOICE')
ov('N0414','O10','CV、AIGC、NLP、RL等是一般认知例示。',branch='EXAMPLE')
ov('E0176','1:0','我们在做什么介绍团队方向，不转写本人独立职责。',metric='SEPARATE',branch='TEAM_BACKGROUND')
ov('E0176','O9','负责实验并真机验证是研究实验执行，没有开发测评工具/框架的具体证据。',metric='DUTY_OWN_USE')
ov('E0176','O19','原引团队评测资源，改实际优先闭环验证经历。',metric='PREFERRED',quote='有机器人真机部署与调试经验，有完整的训练→真机验证闭环经历')
ov('E0176','O25','原引团队介绍，改实际推理优化优先经历。',metric='PREFERRED',quote='有推理优化相关经验（异步推理、RTC、Test Time Compute等）')
ov('N0351','O4','等开发工具为清单例示，ROS不在斜杠内部。',branch='EXAMPLE')
for e in ['O1','O2','O15','1:0']:ov('N0411',e,'斜杠未给定并用或任选。',branch='UNRESOLVED')
ov('N0411','O16','VLA或多模态模型，后者不必为基础模型。',branch='CHOICE')
for e in ['O18','O21']:ov('N0411',e,'参与或主导以下一个或多个方向，不能确定独立开发承担。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP'])
ov('N0411','O22','原真机句仅参与；仿真实验验证是本人直接职责，重锚。',metric='DUTY_OWN_USE',quote='在高保真仿真环境（如 Isaac Sim / Mujoco）中设计实验并验证算法')
for e in ['O31','O32']:ov('N0411',e,'VLM与LLM均为基础模型上位，但该项属于以下之一的外层任选。',branch='CHOICE')
for e in ['O1','O2','O3','O4']:ov('N0374',e,'C++/Python及pytorch/tensorflow斜杠未解，不直接视作确定例示。',branch='UNRESOLVED')
ov('N0374','O5','了解ROS等框架为例示。',branch='EXAMPLE')
ov('N0374','O17','原引用职责，改实际一般模型认知要求。',metric='GENERAL',quote='对生成模型、视频生成、多模态时序建模或世界模型等至少一个方向有较深入理解')
for e in ['O19','O21','O22']:ov('N0374',e,'原引用职责，改实际优先经验句。',metric='PREFERRED',quote='有视频生成、世界模型、机器人学习、仿真或强化学习经验者优先')
ov('N0374','11:0','至少一个方向且等列举。',branch='CHOICE_AND_EXAMPLE')
ov('N0374','12:0','世界模型与其他方向或，明确任选。',branch='CHOICE')
add('N0374','V2_3D_RECONSTRUCTION','GENERAL','UNCONDITIONAL','熟悉基于神经网络的三维重建','一般三维重建知识明确，不只优先项目经历。')
register(list(R.values()),'Astra_v3_boundary_science_a')
