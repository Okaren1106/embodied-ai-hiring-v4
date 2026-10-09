"""First-pass adjudication for ML coding_order 7-9. Reader: grok4.6."""
from common import *
from register_Q_decisions import register

def duty_line(rid, needle):
 k=next(j['identity_key'] for j in jobs if j['reading_id']==rid)
 for field in ['duties','requirements','full_description']:
  t=RAW[k].get(field) or ''
  for ln in t.splitlines():
   if needle in ln:
    return ln.split('.',1)[-1] if ln[:1].isdigit() else ln
 raise SystemExit('missing '+rid+' '+needle)

n0619_task=duty_line('N0619','全身动作模型')
n0619_post=duty_line('N0619','指令微调')

decisions={
"N1001":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"COLLECT_TRAIN_EVAL_TOOLING",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"Your scope will span data pipelines, training infrastructure, evaluation systems, and the tooling that connects them",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "2":"REJECT:C++不是C语言；无独立C证据。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[
  {"quote":"Experience building internal tools, dashboards, or GUI applications.","description":"内部工具/仪表盘/GUI任选经验，冻结ML目录无对应GUI项。"},
  {"quote":"Experience with cloud infrastructure, databases, Docker, and job orchestration.","description":"泛称cloud infrastructure与job orchestration，不映射GCP；Docker已由继承SK_DOCKER覆盖。"}
 ],
 "notes":"标题含Large Scale Behavior Cloning，正文主责是采集-训练-评测循环的工具与基础设施，不是本人训练行为克隆策略。Nice to have中behavior cloning/diffusion/VLA/VLM为优先任选，VLA/VLM斜线保持未解。与研究科学家协作为协作，不升为本人模型研发。"
},
"N0674":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_ALGORITHMS_FOR_ROBOTS",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"Develop and implement state-of-the-art reinforcement learning algorithms for robotic applications.",
 "new":{
  "1":"REJECT:C++不是C语言；Python, C++, or similar为语言任选。",
  "2":"REJECT:薪资USD不是Universal Scene Description。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[
  {"quote":"various reinforcement learning algorithms and techniques (model-free, model-based, multi-task, hierarchical, multi-agent, etc.)","description":"RL子型示例保留原文，不另建未冻结细目录。"},
  {"quote":"Communicate effectively with inference, application, and deployment engineers to integrate RL models into robotic systems","description":"与推理/部署工程师协作集成，不是本人拥有部署职能。"}
 ],
 "notes":"Preferred Qualifications为该广告唯一资格栏，继承项按PREFERRED保留。公司简介中的robust/data-driven ML记背景。扩大训练规模为与研究员协作，不单独记训练基础设施主责。"
},
"N0619":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"WAM_VLA_ARCHITECTURE_AND_TRAINING",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":n0619_task,
 "new":{
  "1":"REJECT:GitHub Stars是开源论文影响力门槛，不是Git技能要求。",
  "2":"OUTSIDE:RT系列为VLA架构示例家族，未单列冻结项。",
  "3":"OUTSIDE:OpenVLA为具身模型架构示例；不把名称写成训练框架。",
  "4":"OUTSIDE:π0为具身模型架构示例；不把π0等同OpenPi。",
  "5":[["V2_WORLD_MODEL","GENERAL","EXAMPLE"]],
  "6":[["V2_MODEL_COMPRESSION","PREFERRED","UNRESOLVED"]]
 },
 "old_overrides":{
  "O5":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"Isaac Gym / MuJoCo / PyBullet等同时任选与示例。"},
  "O6":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一仿真平台斜线加等。"},
  "O7":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一仿真平台斜线加等。"},
  "O9":{"metric":"DUTY_OWN_DEVELOP","branch":"EXAMPLE","relation":"OWN_DEVELOP","reason":"扩散策略、自回归动作生成、时序建模等为前沿方法示例。"},
  "O13":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"推理优化支撑真机实时控制需求，不是开发实时操作系统。"},
  "O26":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"量化/蒸馏/推理加速斜线未解；推理加速不单独构成压缩。"},
  "O27":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"同一斜线组。"},
  "O28":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"同一斜线组。"},
  "O29":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"仿真平台斜线加等。"},
  "O30":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"仿真平台斜线加等。"},
  "O31":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"仿真平台斜线加等。"}
 },
 "additions":[
  {"code":"V2_POSTTRAINING","metric":"GENERAL","branch":"EXAMPLE","quote":n0619_post,"reason":"指令微调与对齐为所列技术之一；预训练不写成后训练主责。"}
 ],
 "outside_extra":[
  {"quote":"有真机部署经验者优先","description":"真机部署优先经验保留；不自动升为客户现场部署职责。"},
  {"quote":"WAM（全身动作模型）","description":"本条WAM是全身动作模型，不能按另一广告的世界模型WAM别名处理。"}
 ],
 "notes":"主导或参与不影响架构设计与训练优化这一本人任务。Python/C++斜线保持未解。RLHF/PPO/DPO写在强化学习示例括号内，后训练另以指令微调/对齐句登记。同一句C++不记C语言。"
}
}

if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
