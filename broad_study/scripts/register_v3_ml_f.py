from astra_review_tools import *
JUD={
'N0923':'训练平台和CUDA内核本人职责明确。DDP/FSDP内部不同技术斜线未解；数据工程上位经验明确，不因Parquet/Arrow示例而丢掉上位类。补明确低时延推理建设。',
'E0384':'RL策略与真机迁移调优明确；e.g.框架列表没有or。动捕和遥操只是重定向管线的数据来源，不证明本人使用采集技术。',
'N0941':'抓取模型选择与策略、独立评测基础设施及仿真验证构成完整对象；GCP优先明确，AI coding assistant目录外保留。',
'E0588':'JAX优先标记直接明确，PyTorch与它的并列关系仍保留未知；平台支持新评估指标不自动等于本人开发评测框架。云环境e.g.没有or。',
'N0890':'操作模型与sim2real主责完整；职责已明确distill，不能漏掉压缩方法。优先and/or明确部分任选，transformer/diffusion内部仍未知，避免全部层级一律U。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[],additions=[]) for r,j in JUD.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**f))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
add('N0923','TC_REALTIME','DUTY_OWN_DEVELOP','UNCONDITIONAL','Build low-latency inference pipelines for production robotics workloads.','明确低时延推理管线本人建设。')
for e in ['O2','O3','O4','O5']:ov('E0384',f'E0384:{e}','e.g.列举没有or，不额外推定任选。',branch='EXAMPLE')
for e in ['E0384:1:0','E0384:1:1']:ov('E0384',e,'明确使用示教数据，不证明本人使用动捕或遥操采集方法；保留数据源提及。',metric='SEPARATE',branch='DATA_SOURCE')
add('E0384','V2_SIM2REAL','DUTY_OWN_DEVELOP','UNCONDITIONAL','Drive the entire development cycle, from prototyping in simulation to robustly transferring and fine-tuning policies on the robot.','本人负责从仿真原型到真机迁移。')
add('E0384','V2_POSTTRAINING','DUTY_OWN_USE','UNCONDITIONAL','robustly transferring and fine-tuning policies on the robot','明确对已有策略微调，按方法使用。')
ov('E0588','E0588:O1','原引文是协作研究者；岗位概述有明确本人构建JAX管线，重锚独立正例。',metric='DUTY_OWN_USE',quote='You’ll own critical infrastructure for large-scale training, from managing GPU/TPU compute and job orchestration to building reusable and efficient JAX training pipelines.')
ov('E0588','E0588:O2','JAX紧接preferred明确优先，逗号关系未解不推翻已明确优先语境。',branch='UNCONDITIONAL')
ov('E0588','E0588:O7','训练代码支持评估指标未表明开发评测方法框架，本句按应用已有指标。',metric='DUTY_OWN_USE')
ov('E0588','E0588:O11','一般要求原锚职责，改引真正familiarity资格段。',metric='GENERAL',quote='Familiarity with distributed training, multi-host setups, data loaders, and evaluation pipelines.')
for e in ['E0588:2:0','E0588:2:1','E0588:2:2']:ov('E0588',e,'e.g.平台列举无or，不虚构任选。',branch='EXAMPLE')
add('N0890','V2_MODEL_COMPRESSION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Optimize and distill models for edge deployment','蒸馏是明确本人模型优化方法。')
for e in ['O15','O16','O17']:ov('N0890',f'N0890:{e}','Partner with AI platform团队的协作集成验证不直接提升本人独立责任；其他独立验证与安全动作另保留。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in ['O20','O21']:ov('N0890',f'N0890:{e}','外层and/or明确允许选用VLA或行为克隆等；内部斜线只作用后面的模型子类。',branch='CHOICE')
ov('N0890','N0890:O22','transformer与diffusion均属机器学习模型，上位方法类出现可判，子类未解不外推为上位未知。',branch='UNCONDITIONAL')
ov('N0890','N0890:O26','synthetic data是including数据方法的例示。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_ml_f')
