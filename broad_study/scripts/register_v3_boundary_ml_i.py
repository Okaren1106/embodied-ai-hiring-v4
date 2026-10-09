from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0572':'本人推理引擎二次开发与量化应用明确；跨工具斜线未知，等框架为示例。',
'N0313':'后训练与真机迁移为直接职责，RL或IL明确任选；上位操作经验类内替代不使整类任选。',
'N0337':'VLA自研、数据管线与性能评测体系明确；操作数据不直接证明操作策略开发。',
'N0353':'补读全文核对任务边界：实际业务RL未限定机器人，机器人控制仅优先应用示例。',
'E0075':'基础模型预训练与下游目标区分；DeepSpeed与FSDP同在等列表。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
for e in ['O1','O2','O3','3:0']:ov('N0572',e,'不同语言/框架或CUDA/Triton/cuBLAS斜线关系未明。',branch='UNRESOLVED')
for e in ['6:0','6:1']:ov('N0572',e,'TensorRT、vLLM等无任选词，保留示例。',branch='EXAMPLE')
ov('N0572','O11','改用本人负责仿真环境推理链路优化句，旧句仅参与真机调试。',metric='DUTY_OWN_USE',quote=ln('N0572',2))
R['N0572']['additions'].append(dict(code='V2_MODEL_COMPRESSION',metric='PREFERRED',branch='EXAMPLE',quote=ln('N0572',19),reason='LoRA属于冻结低秩适配目录。'))
for e in ['O2','O3']:ov('N0313',e,'Isaac Gym/Sim同一冻结工具类，等为示例。',branch='EXAMPLE')
ov('N0313','O8','负责采集标准制定与分析不是本人执行采集，属于数据流程开发。',metric='DUTY_OWN_DEVELOP')
for e in ['O9','O10']:ov('N0313',e,'RL或IL明确任选。',branch='CHOICE')
ov('N0313','O11','操作和抓取在如所引具体场景中。',branch='EXAMPLE')
for e in ['O15','O16','O17']:ov('N0313',e,'三个替代经验均属机器人操作类别。',branch='UNCONDITIONAL')
ov('N0313','2:0','主导部署验证解决虚实差异，未明确研发迁移技术本身。',metric='DUTY_OWN_USE')
ov('N0337','O10','采集处理机器人操作数据不证明本人操作算法开发，保留工作对象。',metric='SEPARATE',branch='DATA_OBJECT')
for e in ['O2','O3']:ov('N0353',e,'至少一种编程语言加如和等，同时任选和示例。',branch='CHOICE_AND_EXAMPLE')
R['N0353']['task_override']=dict(task='OTHER_MODEL',quote=ln('N0353',2),reason='全部核心职责为一般业务RL研究，机器人只出现在与自动驾驶、金融交易并列的优先经历，不能因雇主推成机器人模型任务。')
ov('E0075','1:0','DeepSpeed和FSDP同属等训练框架列表，均为示例。',branch='EXAMPLE')
register(list(R.values()),'Astra_v3_boundary_ml_i')
