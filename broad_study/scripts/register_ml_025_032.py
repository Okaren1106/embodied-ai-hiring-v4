"""First-pass adjudication for ML coding_order 25-32. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"N0401":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"MULTIMODAL_ONDEVICE_INFERENCE",
 "secondary_task":"",
 "task_evidence":"部署并维护多模态感知算法/模型； 平台化推理与加速适配；",
 "new":{
  "1":O+"DMABUF零拷贝接口未单列冻结项。",
  "2":O+"DMA未单列冻结项。",
  "3":"DUPLICATE:N0401:4",
  "4":[["V2_C","GENERAL","UNRESOLVED"],["V2_CMAKE","GENERAL","EXAMPLE"]],
  "5":"DUPLICATE:N0401:4",
  "6":[["V2_QNX","GENERAL","CHOICE"]],
  "7":"DUPLICATE:N0401:6",
  "8":O+"NDK/驱动/多媒体管线调试未单列冻结项。",
  "9":[["V2_TENSORRT","GENERAL","CHOICE"],["V2_MODEL_COMPRESSION","GENERAL","EXAMPLE"]],
  "10":O+"RKNN工具链未单列冻结项。",
  "11":"DUPLICATE:N0401:9",
  "12":O+"Jetson AGX Orin架构优先了解，未单列冻结项。",
  "13":R+"接口定义与单测不是需求工程岗位技能。",
  "14":[["V2_CALIBRATION","PREFERRED","CHOICE"]],
  "15":O+"GStreamer多媒体栈示例。",
  "16":O+"V4L2。","17":O+"MediaCodec。","18":O+"AAudio。",
  "19":O+"OpenGL。","20":O+"Vulkan。","21":O+"OpenCL。",
  "22":[["V2_PERF","PREFERRED","CHOICE"],["V2_NSIGHT","PREFERRED","CHOICE"]],
  "23":"DUPLICATE:N0401:22",
  "24":O+"atrace。","25":O+"systrace。","26":O+"VTune。",
  "27":"DUPLICATE:N0401:22"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"精通 C/C++","description":"本句明确包含C语言，与仅写C++的广告区分。"}],
 "notes":"主责端侧多模态推理部署，不是训练机器人策略。C/C++斜线未解但C有独立表面。Linux/QNX任选。"
},
"N0399":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"EMBODIED_FOUNDATION_PRETRAIN_POSTTRAIN",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"参与具身智能基础模型研发，覆盖 VLM/VLA/VideoGen 预训练、后训练与强化学习等关键环节，打造可跨不同机器人平台泛化的通用模型。",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "2":[["V2_POSTTRAINING","GENERAL","CHOICE"]],
  "3":O+"PPO为RL算法示例。",
  "4":O+"SAC为RL算法示例。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"如 π系列等","description":"π系列不映射为OpenPi训练框架。"}],
 "notes":"预训练、后训练与RL并列关键环节；后训练记示例分支，不等于岗位只有对齐。VideoGen保留在基础模型职责句，不另建未冻结目录。"
},
"N0395":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"DISTILL_COMPRESS_ONDEVICE",
 "secondary_task":"",
 "task_evidence":"搭建与维护多模态模型训练 Pipeline（涵盖数据预处理、实验追踪、Checkpoint 管理与回归评测）",
 "new":{
  "1":[["V2_MODEL_COMPRESSION","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_ONNX","DUTY_OWN_USE","CHOICE"],["V2_TENSORRT","DUTY_OWN_USE","CHOICE"]],
  "2":"DUPLICATE:N0395:1","3":"DUPLICATE:N0395:1","4":"DUPLICATE:N0395:1","5":"DUPLICATE:N0395:1",
  "6":"DUPLICATE:N0395:8","7":"DUPLICATE:N0395:8",
  "8":[["V2_ONNX","REQUIRED","UNRESOLVED"],["V2_TENSORRT","REQUIRED","UNRESOLVED"],["V2_MODEL_COMPRESSION","REQUIRED","UNCONDITIONAL"]],
  "9":[["V2_FSDP","PREFERRED","UNRESOLVED"],["V2_DDP","PREFERRED","UNRESOLVED"],["V2_DEEPSPEED","PREFERRED","UNRESOLVED"]],
  "10":"DUPLICATE:N0395:9","11":"DUPLICATE:N0395:9","12":"DUPLICATE:N0395:9"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"PTQ/QAT、量化感知训练、剪枝与 KV/Cache 优化","description":"PTQ/QAT为压缩子型，由V2_MODEL_COMPRESSION覆盖，不另建目录。"}],
 "notes":"主责训练管线、蒸馏与端侧压缩部署。ONNX/TensorRT斜线未解。交互语义建模为兼顾项，不改主任务。"
},
"N0387":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"SPEECH_SYNCED_GESTURE_GENERATION",
 "secondary_task":"",
 "task_evidence":"结合TTS（文本转语音）的韵律特征（音素时长、基频、能量），生成与语音同步的口型、头部姿态、手势等副语言动作",
 "new":{str(i):O+"动作/语音生成具体方法或资产未单列冻结项。" for i in range(1,18)},
 "old_overrides":{},
 "additions":[{"code":"TC_GENERATIVE_POLICY","metric":"GENERAL","branch":"EXAMPLE","quote":"有生成模型（Diffusion、VAE、GAN、Flow-based）的实际项目经验","reason":"生成模型经验列表示例；不把语音口型生成写成机器人动作策略主责。"}],
 "outside_extra":[{"quote":"熟悉MotionGPT、HumanML3D、MotionDiffusion、PhysDiff、ASE等代表性工作","description":"人体动作生成文献保留目录外。"}],
 "notes":"副语言动作生成与TTS同步，属其他模型应用，不是机器人操作策略。生成模型示例不升为Diffusion Policy职责。"
},
"N0386":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"OMNI_STREAMING_INTERACTION",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"主导/参与 Any-to-Any / Omni-to-Omni 原生多模态交互大模型的架构设计与核心策略研发。",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_DEEPSPEED","GENERAL","EXAMPLE"],["V2_VLLM","GENERAL","EXAMPLE"],["V2_CODEX","GENERAL","UNRESOLVED"]],
  "3":O+"Megatron-LM未单列冻结项。",
  "4":"DUPLICATE:N0386:2","5":"DUPLICATE:N0386:2",
  "6":O+"claude为AI辅助编程工具，未单列冻结项。",
  "7":"DUPLICATE:N0386:2"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"结合流式多模态感知与Agentic OS","description":"Agentic OS按智能体工作流编码；不是上层业务Agent编排专岗的充分证明。"}],
 "notes":"主责原生多模态全双工交互模型。对齐优先经验不自动变成后训练主责。claude/codex为提效工具。"
},
"N0384":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"ONDEVICE_MULTIMODAL_RUNTIME",
 "secondary_task":"",
 "task_evidence":"负责机器人端侧/边缘侧多模态模型运行系统的设计、开发与性能优化",
 "new":{
  "1":R+"轻量化适配不是量化蒸馏裁剪的充分证据。",
  "2":R+"轻量化适配不是量化蒸馏裁剪的充分证据。",
  "3":O+"gRPC双向流协议。","4":O+"WebSocket协议。",
  "5":O+"gRPC优先经验。","6":O+"WebSocket优先经验。",
  "7":[["V2_TENSORRT","DUTY_OWN_USE","CHOICE"],["V2_VLLM","DUTY_OWN_USE","CHOICE"],["V2_SGLANG","DUTY_OWN_USE","CHOICE"],["V2_ONNX_RUNTIME","DUTY_OWN_USE","CHOICE"],["V2_MODEL_COMPRESSION","DUTY_OWN_USE","EXAMPLE"]],
  "8":"DUPLICATE:N0384:7","9":"DUPLICATE:N0384:7","10":"DUPLICATE:N0384:7","11":"DUPLICATE:N0384:7","12":"DUPLICATE:N0384:7",
  "13":"DUPLICATE:N0384:19","14":"DUPLICATE:N0384:19","15":"DUPLICATE:N0384:19","16":"DUPLICATE:N0384:19","17":"DUPLICATE:N0384:19",
  "18":R+"C++不是C语言。",
  "19":[["V2_TENSORRT","GENERAL","CHOICE"],["V2_VLLM","GENERAL","CHOICE"],["V2_SGLANG","GENERAL","CHOICE"],["V2_ONNX_RUNTIME","GENERAL","CHOICE"],["V2_TRITON_SERVER","GENERAL","CHOICE"]],
  "20":"DUPLICATE:N0384:19",
  "21":O+"Qwen-Omni模型名保留目录外。",
  "22":O+"RTC。","23":O+"Realtime API。",
  "24":[["V2_MODEL_COMPRESSION","PREFERRED","EXAMPLE"],["V2_TENSORRT","PREFERRED","CHOICE"]],
  "25":O+"FP8为量化位宽示例。","26":O+"INT8为量化位宽示例。","27":O+"INT4为量化位宽示例。",
  "28":"DUPLICATE:N0384:24"
 },
 "old_overrides":{
  "O6":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"统一接入并运行LLM/VLM，不是本人研发基础模型算法。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"不负责上层 Agent 业务编排和机器人交互状态机。","description":"原文排除Agent编排，不补V2_AGENT_WORKFLOW职责。"}],
 "notes":"主责端侧推理运行时。L23的Triton与推理后端并列，按Inference Server而非编译器。ONNX Runtime不自动等于ONNX格式。"
},
"N0379":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"AUDIOVISUAL_TARGET_SPEECH",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责多模目标语音提取、多模态语音分离、唇动识别等语音前端与多模态感知算法",
 "new":{
  "1":R+"过拟合不是市场营销。",
  "2":O+"MLP。","3":O+"CNN。","4":O+"RNN。","5":O+"LSTM。","6":O+"GRU。","7":O+"TCN。","8":O+"Attention网络结构示例。"
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"PyTorch、TensorFlow等至少一种，任选示例。"},
  "O2":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一框架任选。"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"语音前端与视听融合，属其他模型应用。部署优化为职责之一，主任务仍是语音/唇动融合算法。"
},
"N0199":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VLA_WORLD_POSTTRAIN_RL",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"负责具身大模型（VLA/世界模型）后训练中的分布式系统架构设计、吞吐量和效率优化、多机多卡多核scaling。",
 "new":{
  "1":[["V2_WORLD_MODEL","DUTY_OWN_DEVELOP","UNRESOLVED"],["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_WORLD_MODEL","DUTY_OWN_DEVELOP","UNRESOLVED"],["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":O+"ENPIRE为autoresearch算法名，未单列冻结项。",
  "5":[["V2_GENESIS","DUTY_OWN_USE","EXAMPLE"],["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0199:5","7":"DUPLICATE:N0199:5",
  "8":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0199:10",
  "10":[["V2_C","GENERAL","UNRESOLVED"]],
  "11":[["V2_AGENT_WORKFLOW","PREFERRED","UNCONDITIONAL"]],
  "12":O+"vibe coding未单列冻结项。",
  "13":"DUPLICATE:N0199:11","14":"DUPLICATE:N0199:11",
  "15":O+"skill未单列冻结项。","16":O+"agent team未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"熟悉Isaac/genesis world/MuJoCo等业界SOTA","description":"仿真器斜线未解；Genesis已编码。"}],
 "notes":"后训练分布式系统、真机RL与仿真器并列为职责。VLA/世界模型斜线未解。C/C++中C有独立表面。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
