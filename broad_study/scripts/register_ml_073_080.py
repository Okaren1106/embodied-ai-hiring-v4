"""First-pass adjudication for ML coding_order 73-80. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"N0097":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"INDUSTRIAL_SFT_RLHF_POSTTRAIN",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"设计并实施具身大模型的监督微调（SFT）流程，基于工业场景的半结构化任务数据，提升模型在特定机器人任务中的指令遵循、操作精度和任务完成度",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":R+"置信度校准不是传感器/系统标定。",
  "4":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_MODEL_COMPRESSION","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "6":[["V2_POSTTRAINING","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_HUGGINGFACE","GENERAL","UNCONDITIONAL"],["V2_POSTTRAINING","GENERAL","UNCONDITIONAL"]],
  "8":O+"LlaMA-Factory微调框架未单列冻结项。",
  "9":"DUPLICATE:N0097:7",
  "10":R+"LoRA/QLoRA/Adapter是参数高效微调，不是量化蒸馏裁剪的充分证据。",
  "11":[["V2_SAPIEN","PREFERRED","EXAMPLE"],["V2_POSTTRAINING","PREFERRED","EXAMPLE"]],
  "12":"DUPLICATE:N0097:11",
  "13":[["V2_POSTTRAINING","PREFERRED","EXAMPLE"]],
  "14":[["V2_ONNX","PREFERRED","UNRESOLVED"],["V2_TENSORRT","PREFERRED","UNRESOLVED"],["V2_POSTTRAINING","PREFERRED","UNCONDITIONAL"],["V2_MODEL_COMPRESSION","PREFERRED","EXAMPLE"]],
  "15":"DUPLICATE:N0097:14","16":"DUPLICATE:N0097:14",
  "17":[["V2_POSTTRAINING","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"探索PEFT（参数高效微调）方案设计与落地验证。","description":"PEFT/LoRA不自动记模型压缩。Pi系列不写成OpenPi。"}],
 "notes":"主责工业后训练SFT/RLHF。知识蒸馏/量化/剪枝才记压缩。L4置信度校准已拒绝标定目录。"
},
"N0057":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"HRI_INTERACTION_POLICY_INTERN",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责人机交互场景下的具身智能算法研究，包括交互策略建模、多模态感知与动作生成。",
 "new":{},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"候选队列为空。主责人机交互策略，强化学习或模仿学习任选。"
},
"N0588":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"HUMANOID_FOUNDATION_MOTION_TRACKING",
 "secondary_task":"",
 "task_evidence":"构建、训练和部署人形机器人基础模型（Humanoid Foundation Model），应用于全身运动跟踪及移动操作。",
 "new":{"1":O+"BFM运动基础模型缩写未单列冻结项。","2":O+"WBT未单列冻结项。"},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"探索前沿运动基础模型（BFM / WBT）、动作跟踪（Motion Tracking）算法、模仿学习以及VLA模型","description":"WBT不能按WAM或世界模型改写。"}],
 "notes":"主责人形基础模型用于运动跟踪与移动操作。BFM/WBT保留目录外。"
},
"N0575":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"HUMANOID_VLA_WORLD_SIM2REAL_INTERN",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"参与人形机器人 VLA 模型的设计、训练与评测；",
 "new":{
  "1":[["V2_SYSID","DUTY_OWN_DEVELOP","EXAMPLE"],["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_WORLD_MODEL","DUTY_OWN_USE","EXAMPLE"]],
  "4":[["V2_SAPIEN","GENERAL","CHOICE_AND_EXAMPLE"],["V2_GENESIS","GENERAL","CHOICE_AND_EXAMPLE"]],
  "5":"DUPLICATE:N0575:4","6":"DUPLICATE:N0575:4",
  "7":[["V2_WORLD_MODEL","GENERAL","EXAMPLE"]],
  "8":[["V2_WORLD_MODEL","PREFERRED","CHOICE"]],
  "9":[["V2_SIM2REAL","PREFERRED","CHOICE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"开展数字孪生、系统辨识及仿真参数校准","description":"仿真参数校准不是传感器标定，未写入V2_CALIBRATION。真机微调泛称不自动升后训练。"}],
 "notes":"VLA实习覆盖世界建模与Sim2Real。L7校准已排除传感器标定。仿真平台斜线加等。"
},
"N0573":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"FLUXVLA_TRAIN_DEPLOY_ENGINEERING",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"负责 VLA 模型的开发与迭代，包括模型接入、训练脚本开发、数据适配、推理流程优化和实验复现。",
 "new":{
  "1":O+"FluxVLA为开源codebase名称，未单列冻结项。",
  "2":[["V2_WORLD_MODEL","DUTY_OWN_USE","EXAMPLE"]],
  "3":[["V2_WORLD_MODEL","GENERAL","EXAMPLE"]],
  "4":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0573:4",
  "6":[["V2_WORLD_MODEL","PREFERRED","EXAMPLE"]],
  "7":O+"LIBERO评测套件未单列冻结项。","8":O+"RoboCasa仿真套件未单列冻结项。",
  "9":R+"LoRA不是量化蒸馏裁剪的充分证据。",
  "10":O+"Transformers库名保留目录外。",
  "11":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]]
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"Python / PyTorch斜线未解。"},
  "O2":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一斜线。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"参与 FluxVLA 开源 codebase 的开发、维护与工程化优化","description":"开源库维护是工程对象，不把库名写入冻结技能。"}],
 "notes":"主责VLA训练部署与开源工程。World Model为跟进方向示例。熟悉Git协作记Git技能。"
},
"N0572":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"EDGE_VLA_JETSON_RUNTIME",
 "secondary_task":"",
 "task_evidence":"负责 VLA 模型在边缘计算平台上的高效部署，针对仿真环境与真实机器人场景进行端到端推理链路优化",
 "new":{
  "1":O+"FluxVLA为开源codebase名称，未单列冻结项。",
  "2":[["V2_MODEL_COMPRESSION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_TRITON_COMPILER","DUTY_OWN_USE","CHOICE"]],
  "4":"DUPLICATE:N0572:3",
  "5":O+"cuBLAS未单列冻结项。",
  "6":[["V2_TENSORRT","DUTY_OWN_DEVELOP","CHOICE_AND_EXAMPLE"],["V2_VLLM","DUTY_OWN_DEVELOP","CHOICE_AND_EXAMPLE"]],
  "7":"DUPLICATE:N0572:6","8":"DUPLICATE:N0572:6",
  "9":[["V2_MODEL_COMPRESSION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "10":[["V2_NSIGHT","DUTY_OWN_USE","EXAMPLE"]],
  "11":"DUPLICATE:N0572:10",
  "12":O+"Ncu性能工具未单列冻结项。","13":O+"Omniperf未单列冻结项。",
  "14":[["V2_WORLD_MODEL","GENERAL","EXAMPLE"]],
  "15":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "16":"DUPLICATE:N0572:15",
  "17":[["V2_WORLD_MODEL","PREFERRED","EXAMPLE"]],
  "18":O+"LIBERO。","19":O+"RoboCasa。",
  "20":R+"LoRA不是量化蒸馏裁剪的充分证据。",
  "21":O+"Transformers库名保留目录外。",
  "22":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]]
 },
 "old_overrides":{
  "O2":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"Python / PyTorch斜线未解。"},
  "O3":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一斜线。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"负责具身大模型（VLA / WM / WAM）及多模态模型在 NVIDIA Jetson（Orin / Thor 系列） 等边缘平台上的深度适配","description":"WM/WAM未展开，不把WAM改写成世界模型；世界模型仅在理解/加分项编码。CUDA/Triton按编译器。"}],
 "notes":"主责端侧推理优化。INT8/INT4/FP8/FP4为量化方案。Triton与CUDA并列开发Kernel。"
},
"N0526":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"HUMANOID_FOUNDATION_SIM2REAL_INTERN",
 "secondary_task":"",
 "task_evidence":"参与具身智能基础模型相关算法研究，训练和部署人形机器人基础模型（Humanoid Foundation Model），应用于机器人产品。",
 "new":{
  "1":O+"BFM未单列冻结项。","2":O+"WBT未单列冻结项。",
  "3":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"负责sim2real部分工作，例如电机建模，通讯延迟模拟，噪声等","description":"电机建模/延迟/噪声是Sim2Real手段示例。"}],
 "notes":"实习基础模型加明确Sim2Real职责。BFM/WBT保留目录外。"
},
"N0313":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"POSTTRAIN_SIM2REAL_BUSINESS_TASKS",
 "secondary_task":"",
 "task_evidence":"负责预训练模型的后训练（Post-training）与指令微调，针对多任务、多构型场景进行模型适配。",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":O+"PPO为RL算法示例。","4":O+"SAC。"
 },
 "old_overrides":{
  "O2":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"Isaac Gym/Isaac Sim斜线未解。"},
  "O3":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一斜线。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"针对多任务、多构型场景进行模型适配。","description":"指令微调与后训练同句，记后训练职责不另扩未冻结适配目录。"}],
 "notes":"帕西尼后训练与业务优化。Sim2Real为并列主责。FAR规则不在本条编码范围。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
