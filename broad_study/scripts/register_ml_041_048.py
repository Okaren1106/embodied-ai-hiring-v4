"""First-pass adjudication for ML coding_order 41-48. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"N0486":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"DRL_LEGGED_WHEELED_MOTION_CONTROL",
 "secondary_task":"",
 "task_evidence":"利用强化学习和深度学习技术，开发适用于腿足/轮足式机器人平台的敏捷鲁棒控制算法；",
 "new":{
  "1":O+"PPO为RL算法示例。","2":O+"SAC。","3":O+"DQN。","4":O+"DDPG。","5":O+"A3C。",
  "6":R+"Python/C++不是C语言；斜线保持未解。",
  "7":O+"RaiSim仿真器未单列冻结项。",
  "8":[["V2_TELEOP","PREFERRED","UNRESOLVED"]]
 },
 "old_overrides":{
  "O5":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"PyTorch/TensorFlow等同时任选示例。"},
  "O6":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一框架斜线加等。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"有模仿学习、强化学习、遥操作、具身智能、多模态大模型（VLM、VLA）项目经验者优先","description":"遥操作在优先项目经验列举中，不证明本人开发遥操系统。"}],
 "notes":"标题为具身运控，主责仍是腿足/轮足DRL控制算法。与同司运动控制算法工程师按本条全文独立编码。"
},
"N0460":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"CAMPUS_VLA_ALGORITHM",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"参与具身智能 VLA（Vision-Language-Action）模型的算法研发，探索视觉、语言与机器人动作之间的理解、推理与决策能力。",
 "new":{"1":R+"C++不是C语言；Python与优先C++分句，不记C。"},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"有深度学习模型训练、微调或相关项目经验。","description":"泛称微调不自动记后训练目录。"}],
 "notes":"校招VLA算法。与软件/感知/控制/数据/Infra协作，不把协作对象写成本人主责。"
},
"N0467":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"MANIPULATION_POSTTRAIN_TRUE_ROBOT",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"参与人形机器人 Manipulation 策略的训练、后训练与真机部署。",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","EXAMPLE"]]
 },
 "old_overrides":{
  "O4":{"metric":"DUTY_OWN_DEVELOP","branch":"EXAMPLE","relation":"OWN_DEVELOP","reason":"VLA、Diffusion Policy、Flow Matching等为策略示例。"},
  "O5":{"metric":"DUTY_OWN_DEVELOP","branch":"EXAMPLE","relation":"OWN_DEVELOP","reason":"同一策略等列表。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"探索真机 RL、Online Learning、Human-in-the-loop 等机器人策略 Post-training 方法。","description":"Human-in-the-loop是后训练方法示例，不是硬件在环HIL。"}],
 "notes":"主责操作策略训练与后训练。L6为探索方法，记后训练示例分支。"
},
"N0469":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VLA_ALGORITHM_GENERAL",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"参与具身智能 VLA（Vision-Language-Action）模型的算法研发，探索视觉、语言与机器人动作之间的理解、推理与决策能力。",
 "new":{"1":R+"C++不是C语言；Python与优先C++分句，不记C。"},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"有深度学习模型训练、微调或相关项目经验。","description":"泛称微调不自动记后训练目录。"}],
 "notes":"与同司2027届校招VLA算法工程师正文高度相近，按本条全文独立编码。"
},
"N0458":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"CAMPUS_VLA_TRAIN_INFER_INFRA",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"参与具身智能大模型（VLA/VLM 等）的训练、推理及部署基础设施建设，支撑算法模型高效运行。",
 "new":{"1":R+"Python / C++不是C语言；斜线保持未解。"},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"对大模型、具身智能、机器人、VLA/VLM等方向有浓厚兴趣","description":"兴趣与优先经历不是本人训练基础模型算法。"}],
 "notes":"校招Infra。VLA/VLM是支撑对象，主任务是训练推理基础设施。"
},
"N0451":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"MANIPULATION_POSTTRAIN_INTERNSHIP",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"参与人形机器人 Manipulation 策略的训练、后训练与真机部署。",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","EXAMPLE"]]
 },
 "old_overrides":{
  "O4":{"metric":"DUTY_OWN_DEVELOP","branch":"EXAMPLE","relation":"OWN_DEVELOP","reason":"VLA、Diffusion Policy、Flow Matching等为策略示例。"},
  "O5":{"metric":"DUTY_OWN_DEVELOP","branch":"EXAMPLE","relation":"OWN_DEVELOP","reason":"同一策略等列表。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"探索真机 RL、Online Learning、Human-in-the-loop 等机器人策略 Post-training 方法。","description":"Human-in-the-loop是后训练方法示例，不是硬件在环HIL。"}],
 "notes":"实习生文本与同司具身智能算法工程师职责相近，按本条独立编码。"
},
"N0621":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VLA_PRETRAIN_ARCHITECTURE_INTERNSHIP",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责VLA模型的预训练架构设计与优化，基于现有VLM增强空间理解和推理能力，探索视觉-动作对齐的预训练方案",
 "new":{
  "1":O+"EDP开发平台为公司产品背景，未单列冻结项。",
  "2":[["V2_AGENT_WORKFLOW","DUTY_OWN_USE","EXAMPLE"]],
  "3":[["V2_WORLD_MODEL","GENERAL","EXAMPLE"]],
  "4":R+"Python/C++不是C语言；斜线保持未解。"
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"PyTorch、TensorFlow等同时任选示例。"},
  "O2":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一框架等列表。"},
  "O21":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"了解世界模型、因果推理、规划与推理的应用，不是世界模型研发职责。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"星海图，作为具身智能赛道百亿级独角兽","description":"公司宣传背景，不计入本人任务。"}],
 "notes":"主责VLA预训练架构与数据pipeline。AI Agent仅出现在前沿跟踪列举。"
},
"N0618":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"DISTRIBUTED_TRAINING_ONBOARD_INFERENCE_RUNTIME",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"主导大规模分布式训练集群的系统架构设计与性能优化，覆盖通信、存储、调度全栈，支撑千亿级参数VLA/WAM模型的稳定高效训练；",
 "new":{
  "1":[["V2_ETHERCAT","DUTY_OWN_USE","CHOICE"],["V2_CAN","DUTY_OWN_USE","CHOICE"]],
  "2":[["V2_TENSORRT","DUTY_OWN_DEVELOP","CHOICE_AND_EXAMPLE"],["V2_VLLM","DUTY_OWN_DEVELOP","CHOICE_AND_EXAMPLE"],["V2_SGLANG","DUTY_OWN_DEVELOP","CHOICE_AND_EXAMPLE"],["V2_ONNX_RUNTIME","DUTY_OWN_DEVELOP","CHOICE_AND_EXAMPLE"]],
  "3":"DUPLICATE:N0618:2","4":"DUPLICATE:N0618:2","5":"DUPLICATE:N0618:2",
  "6":"DUPLICATE:N0618:2",
  "7":R+"C++不是C语言。",
  "8":[["V2_NCCL","REQUIRED","CHOICE"]],
  "9":"DUPLICATE:N0618:8",
  "10":O+"eBPF未单列冻结项。",
  "11":[["V2_TRITON_COMPILER","PREFERRED","CHOICE"]],
  "12":O+"LLVM未单列冻结项。","13":O+"MLIR未单列冻结项。","14":O+"TVM未单列冻结项。",
  "15":"DUPLICATE:N0618:11",
  "16":O+"PREEMPT_RT未单列冻结项。","17":O+"Xenomai未单列冻结项。",
  "18":[["V2_DDS","PREFERRED","CHOICE"]],
  "19":[["V2_ETHERCAT","PREFERRED","CHOICE"],["V2_CAN","PREFERRED","CHOICE"]],
  "20":[["V2_VLLM","PREFERRED","CHOICE"],["V2_SGLANG","PREFERRED","CHOICE"]],
  "21":"DUPLICATE:N0618:20","22":"DUPLICATE:N0618:20"
 },
 "old_overrides":{
  "O14":{"metric":"SEPARATE","branch":"COLLABORATION_OBJECT","relation":"COLLABORATION_OBJECT","reason":"VLA/WAM是训练集群支撑对象；WAM未展开，不改写成世界模型。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"基于TensorRT/vLLM/SGLang/ONNX Runtime等框架进行定制化改造","description":"ONNX Runtime不自动等于ONNX格式。Triton与TVM并列，按编译器而非Inference Server。"}],
 "notes":"主责分布式训练集群与端侧推理引擎。实时控制为并列职责，不改ML主任务。底层系统须至少三项，NCCL落在分布式任选项。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
