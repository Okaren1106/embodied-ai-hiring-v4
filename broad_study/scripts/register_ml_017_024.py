"""First-pass adjudication for ML coding_order 17-24. Reader: grok4.6."""
from register_Q_decisions import register

decisions={
"N0315":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"EMBODIED_PRETRAIN_ARCHITECTURE",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"负责大规模具身智能模型的预训练架构设计、数据配比及Scaling Law验证，确保模型具备基础的通识操作能力。",
 "new":{"1":"REJECT:C++不是C语言；Python/C++斜线保持未解。"},
 "old_overrides":{
  "O4":{"metric":"DUTY_OWN_DEVELOP","branch":"EXAMPLE","relation":"OWN_DEVELOP","reason":"如VLA、Diffusion Policy等为预训练架构示例。"},
  "O5":{"metric":"DUTY_OWN_DEVELOP","branch":"EXAMPLE","relation":"OWN_DEVELOP","reason":"同一如列表中的Diffusion Policy。"},
  "O7":{"metric":"SEPARATE","branch":"BACKGROUND","relation":"BACKGROUND","reason":"通识操作能力是预训练目标，不是操作控制开发职责。"}
 },
 "additions":[
  {"code":"V2_POSTTRAINING","metric":"PREFERRED","branch":"CHOICE","quote":"有大模型（LLM/VLM）全参数微调或预训练实战经验者优先。","reason":"全参数微调与预训练为优先任选；微调不升为无条件后训练主责。"}
 ],
 "outside_extra":[
  {"quote":"针对冰箱整理、传送带分拣等复杂场景，设计预训练阶段的能力储备方案。","description":"场景是预训练能力储备对象，不是本人产线部署。"}
 ],
 "notes":"主责具身预训练架构与分布式训练稳定性。跟踪复现前沿架构记开发示例，不等于已选定单一VLA路线。"
},
"N0890":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"LEARNING_BASED_MANIPULATION",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"Develop learning-based manipulation models for end to end sensor-driven interaction (e.g., reaching, motion generation, and execution in dynamic environments).",
 "new":{
  "1":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_DOMAIN_RANDOMIZATION","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "2":[["V2_SIM2REAL","PREFERRED","UNCONDITIONAL"],["V2_DOMAIN_RANDOMIZATION","PREFERRED","EXAMPLE"]],
  "3":[["V2_ONNX","PREFERRED","UNRESOLVED"],["V2_TENSORRT","PREFERRED","UNRESOLVED"],["V2_MODEL_COMPRESSION","PREFERRED","EXAMPLE"]],
  "4":"DUPLICATE:N0890:3",
  "5":"DUPLICATE:N0890:3"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[
  {"quote":"dataset creation from robot logs/teleop","description":"遥操日志是训练数据来源，不把本岗位记为遥操作系统开发。"}
 ],
 "notes":"主责学习型操作模型及训练/评测/边缘部署。Isaac Sim/Mujoco斜线保持未解。量化仅为边缘部署优先示例，不扩到未写明的蒸馏裁剪。"
},
"E0078":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"MULTIMODAL_TRAINING_INFRA",
 "secondary_task":"",
 "task_evidence":"参与大规模具身智能模型的训练Infra建设。",
 "new":{
  "1":[["V2_TRITON_COMPILER","GENERAL","UNRESOLVED"]],
  "2":[["V2_DEEPSPEED","PREFERRED","EXAMPLE"]]
 },
 "old_overrides":{
  "O12":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原短词大模型定位字段为空，改为完整并行架构句。","quote":"深入理解大模型训练多维并行架构，如Tensor并行、流水线并行、序列并行等。"},
  "O16":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原短词定位字段为空，改为优先句。","quote":"有大规模多模态大模型训练系统研发经历者优先。"}
 },
 "additions":[],
 "outside_extra":[
  {"quote":"了解开源多模态大模型结构，如qwen-vl、llama等。","description":"开源模型家族示例保留目录外，不把名称写成必须框架。"},
  {"quote":"有Megatron-LM、DeepSpeed等大模型训练框架的优化经验优先。","description":"Megatron-LM未单列冻结项；DeepSpeed已编码。"}
 ],
 "notes":"主责训练Infra。CUDA/triton中的triton按编译器而非Inference Server。C++或Python为语言任选，不记C语言。同一句C++不写入候选正例。"
},
"N0509":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VLM_FOR_HUMANOID_MANIPULATION",
 "secondary_task":"",
 "task_evidence":"探索视觉大模型在机器人上的应用，以支持机器人的空间感知、导航、操作、交互等功能；",
 "new":{"1":"REJECT:C++不是C语言；Python / C++斜线保持未解。"},
 "old_overrides":{
  "O5":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"如Pytorch, TensorFlow同时任选示例。"},
  "O6":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一框架如列表。"}
 },
 "additions":[
  {"code":"V2_POSTTRAINING","metric":"GENERAL","branch":"EXAMPLE","quote":"如监督微调、编排、数据生成、带人类反馈的强化学习等。","reason":"监督微调与RLHF为多模态大模型经验示例；编排不单列。"}
 ],
 "outside_extra":[],
 "notes":"职责以应用视觉大模型与学习算法支持感知/导航/操作为主；L4为交互中学习的算法开发。等功能列表不拆成独立导航岗位。"
},
"N0440":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"IL_RL_MULTIMODAL_HUMANOID",
 "secondary_task":"",
 "task_evidence":"设计和开发创新性的模仿学习和强化学习算法，应用于人形机器人场景任务，具备泛化能力",
 "new":{"1":"REJECT:HIL-SERL是算法名，不是硬件在环仿真。"},
 "old_overrides":{
  "O4":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"PyTorch、JAX、TensorFlow等同时任选示例。"},
  "O5":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一框架等列表。"},
  "O6":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一框架等列表。"}
 },
 "additions":[],
 "outside_extra":[
  {"quote":"有ACT、MT-ACT、RT系列、Diffusion Policy，GO/GE World系列，PI系列，GR00T系列，HIL-SERL等算法相关研究背景经验者优先","description":"GO/GE World、PI、GR00T等家族名保留目录外示例，不映射为未冻结训练框架。"}
 ],
 "notes":"主责人形场景IL/RL与多模态大模型。HIL不按硬件在环处理。"
},
"N0421":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"RL_POSTTRAIN_FRAMEWORK",
 "secondary_task":"",
 "task_evidence":"负责强化学习、模型精调、知识蒸馏等核心模块的设计与开发；",
 "new":{
  "1":[["V2_MODEL_COMPRESSION","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "2":"DUPLICATE:N0421:1",
  "3":"REJECT:轻量化训练框架与微调部署不是量化/蒸馏/裁剪的充分证据。",
  "4":[["V2_DEEPSPEED","GENERAL","EXAMPLE"]],
  "5":"OUTSIDE:Megatron-LM未在冻结ML细目录中。",
  "6":"DUPLICATE:N0421:4",
  "7":[["V2_POSTTRAINING","PREFERRED","EXAMPLE"]],
  "8":"DUPLICATE:N0421:7",
  "9":"OUTSIDE:PPO作为RL算法示例，不单列冻结项。",
  "10":"OUTSIDE:veRL强化学习框架未单列冻结项。",
  "11":"OUTSIDE:Slime强化学习框架未单列冻结项。",
  "12":"OUTSIDE:AReaL强化学习框架未单列冻结项。",
  "13":[["V2_HUGGINGFACE","PREFERRED","EXAMPLE"]],
  "14":"DUPLICATE:N0421:13",
  "15":[["V2_POSTTRAINING","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},
 "additions":[
  {"code":"V2_POSTTRAINING","metric":"DUTY_OWN_DEVELOP","branch":"EXAMPLE","quote":"负责强化学习、模型精调、知识蒸馏等核心模块的设计与开发；","reason":"模型精调与RL并列为核心模块；不把蒸馏句重复记后训练。"}
 ],
 "outside_extra":[],
 "notes":"主责RL/精调/蒸馏训练框架，而非直接训练某一机器人策略。L15 RLHF全流程为优先后训练经验。"
},
"N0413":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VLA_PRETRAIN_FOR_MANIPULATION",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"聚焦机器人具身操纵场景，负责VLA相关算法的设计与研发；",
 "new":{"1":"OUTSIDE:数据配比已由继承数据管线覆盖，不另建目录外正例。"},
 "old_overrides":{},
 "additions":[
  {"code":"V2_POSTTRAINING","metric":"GENERAL","branch":"UNCONDITIONAL","quote":"具备数据构建、指令微调及模型开发经验；","reason":"指令微调为明确要求经验，不是预训练主责本身。"}
 ],
 "outside_extra":[],
 "notes":"主责操纵场景VLA设计与预训练。任职要求中的指令微调/RL记经验，不把岗位改成后训练专岗。"
},
"N0412":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"WHOLE_BODY_VLA",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"参与设计和实现面向人形机器人的 Vision-Language-Action 统一模型架构",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","DUTY_OWN_USE","EXAMPLE"]],
  "2":"DUPLICATE:N0412:1",
  "3":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "4":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "5":"DUPLICATE:N0412:4",
  "6":[["V2_WORLD_MODEL","PREFERRED","UNRESOLVED"]],
  "7":"DUPLICATE:N0412:6",
  "8":[["V2_WORLD_MODEL","GENERAL","EXAMPLE"]],
  "9":"OUTSIDE:Transformer已由继承TC_ML_MODELS覆盖。",
  "10":"DUPLICATE:N0412:8",
  "11":[["V2_POSTTRAINING","GENERAL","EXAMPLE"]],
  "12":[["V2_CLASSICAL_CONTROL","GENERAL","EXAMPLE"]],
  "13":"REJECT:薪酬与发展空间不是人力资源岗位技能。"
 },
 "old_overrides":{
  "O18":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"处理稳定性/安全性/实时性是控制接口约束，不是功能安全完整性开发。"},
  "O19":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"实时性为对接约束，不是实时操作系统开发。"}
 },
 "additions":[
  {"code":"V2_MODEL_COMPRESSION","metric":"GENERAL","branch":"EXAMPLE","quote":"部署：WBC、阻抗控制、策略蒸馏、模型压缩","reason":"技术栈示例中的蒸馏与压缩；示例栏非限制。"}
 ],
 "outside_extra":[
  {"quote":"技术栈示例（非限制）","description":"技术栈示例不得升为硬性必备。"}
 ],
 "notes":"岗位背景段的VLA目标保持背景；正式职责从模型设计句起。跟踪世界模型记背景，技术栈/加分项中的世界模型另记。"
}
}

if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
