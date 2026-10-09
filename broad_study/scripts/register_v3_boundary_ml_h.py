from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0061':'参与后训练与本人设计优化、构建评测闭环分开；不因无工具名添加工具要求。',
'N0099':'算子自研、C/C++未知、CUDA任选；支持适配验证不等于独立验证执行。',
'N0097':'工业后训练本人设计与实施明确，压缩应用、协作反馈、目录LoRA边界逐项核对。',
'N0575':'实习VLA参与、仿真benchmark自建、世界建模探索和试验执行分别保留；兴趣不计要求。',
'N0573':'FluxVLA工程与明确模型开发，Python/PyTorch斜线未解；LoRA按冻结目录纳入。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
for e in ['O1','O4','1:0','1:1','3:0']:ov('N0061',e,'明确参与职责，仅保留参与承担；本人设计和构建另有证据。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0061','O2','RLHF-like位于如所引方法示例。',branch='EXAMPLE')
ov('N0099','O4','支持算子适配与验证，未断言本人独立测试。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0097','O2','PyTorch等框架为示例。',branch='EXAMPLE')
for e in ['O25','O26','O27']:ov('N0097',e,'仿真上位使用经验明确。',branch='UNCONDITIONAL')
ov('N0097','O29','SFT/RLHF跨方法关系未解，不能直接确定RL经验分支。',branch='UNRESOLVED')
ov('N0097','4:0','设计后训练数据集流程不直接证明该句本人后训练方法开发，另有直接SFT/RLHF职责。',metric='SEPARATE',branch='SUPPORTED_TRAINING_OBJECT')
ov('N0097','4:1','数据采集是包括清单中的具体方法，保留示例。',branch='EXAMPLE')
ov('N0097','5:0','与预训练工程师协作形成闭环不是新增本人后训练开发证据。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0097','5:1','通过已有蒸馏量化剪枝技术优化推理属于方法应用。',metric='DUTY_OWN_USE')
ov('N0097','6:0','微调、对齐或机器人策略学习的经验为任选，不能保证必有后训练。',branch='CHOICE')
ov('N0097','7:1','SFT、强化学习对齐等技术为示例。',branch='EXAMPLE')
ov('N0097','13:0','模型后训练经验或排行榜贡献是任选，SFT/RLHF同属后训练。',branch='CHOICE')
add('N0097','V2_MODEL_COMPRESSION','GENERAL','EXAMPLE',24,'冻结目录包含低秩适配LoRA/QLoRA，不能因其非量化而拒绝。')
for e in ['O6','O8','1:1']:ov('N0575',e,'参与模型/contact-rich研发或迁移工作流，仅保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
ov('N0575','1:0','开展系统辨识为应用该方法，及字并列无示例词。',metric='DUTY_OWN_USE',branch='UNCONDITIONAL')
ov('N0575','2:0','联合利用数据支持迁移，不等于本人迁移方法开发。',metric='SEPARATE',branch='SUPPORTED_MIGRATION_OBJECT')
for e in ['O21','O22','O23','O24','O25']:ov('N0575',e,'至少一种仿真平台保证上位经验，示例仅品牌。',branch='UNCONDITIONAL')
ov('N0575','7:0','浓厚兴趣不等于知识或经验要求。',metric='SEPARATE',branch='INTEREST')
add('N0575','V2_WORLD_MODEL','DUTY_OWN_DEVELOP','UNCONDITIONAL',4,'明确探索世界建模，不仅跟踪前沿。')
for e in ['O1','O2']:ov('N0573',e,'Python/PyTorch跨语言和框架的斜线未解，无任选词。',branch='UNRESOLVED')
ov('N0573','O8','参与codebase建设所包含评测工具，保留参与承担。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
add('N0573','V2_MODEL_COMPRESSION','PREFERRED','EXAMPLE',19,'LoRA等优先技术明确，冻结目录含低秩适配。')
register(list(R.values()),'Astra_v3_boundary_ml_h')
