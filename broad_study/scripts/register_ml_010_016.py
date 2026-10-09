"""First-pass adjudication for ML coding_order 10-16. Reader: grok4.6."""
from register_Q_decisions import register

decisions={
"N0830":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"GPU_MLOPS_PIPELINES",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"Design, build, and maintain GPU based infrastructure for machine learning pipelines, including data processing, training, evaluation, inference and deployment workflows.",
 "new":{
  "1":[["V2_AWS","GENERAL","CHOICE_AND_EXAMPLE"]],
  "2":"DUPLICATE:N0830:1",
  "3":"OUTSIDE:SageMaker为AWS云ML服务示例，未单列冻结项。",
  "4":"OUTSIDE:S3为AWS存储示例，未单列冻结项。",
  "5":[["V2_ROSBAG","PREFERRED","EXAMPLE"]],
  "6":"DUPLICATE:N0830:5"
 },
 "old_overrides":{
  "O3":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"such as AWS(...) Kubernetes etc.同时任选与示例。"},
  "O24":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"experiment tracking, model versioning, or dataset versioning tools为或任选。"}
 },
 "additions":[],
 "outside_extra":[
  {"quote":"Our Field Foundational Models™ set a new standard in perception, planning, localization, and manipulation","description":"公司产品背景，不是本MLOps岗位本人开发基础模型。"}
 ],
 "notes":"主责GPU训练/推理/部署流水线与MLOps，不是本人训练机器人策略。与机器人团队合作的边缘部署是基础设施，不记客户现场运维。"
},
"E0384":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_LOCOMANIPULATION_POLICIES",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"Implement and deploy state-of-the-art RL algorithms to achieve ambitious, world-class performance on dynamic locomotion and manipulation tasks with physical hardware.",
 "new":{
  "1":[["V2_MOCAP","DUTY_OWN_USE","EXAMPLE"],["V2_TELEOP","DUTY_OWN_USE","EXAMPLE"]],
  "2":"REJECT:C++不是C语言。",
  "3":[["V2_SIM2REAL","GENERAL","EXAMPLE"]]
 },
 "old_overrides":{
  "O2":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"e.g. PyTorch, JAX同时示例任选。"},
  "O3":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一框架e.g.列表。"},
  "O4":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"e.g. MuJoCo, IsaacGym同时示例任选。"},
  "O5":{"metric":"GENERAL","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"同一仿真器e.g.列表。"},
  "O12":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"在仿真中原型并迁移，不是开发仿真器本身。"}
 },
 "additions":[],
 "outside_extra":[
  {"quote":"from prototyping in simulation to robustly transferring and fine-tuning policies on the robot.","description":"真机fine-tuning泛称，不自动记后训练/对齐目录。"}
 ],
 "notes":"主责全身locomanipulation的RL策略；训练管线与动捕/遥操数据重定向为支撑。遥操是示教数据来源，不是开发遥操作系统。"
},
"N0941":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"GRASP_POLICY_PRODUCTION",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"Take end-to-end ownership of the intelligence driving our robots' physical interactions, dynamically determining optimal gripper configurations and tool selections for diverse, complex objects.",
 "new":{
  "1":"OUTSIDE:AI coding assistants为开发辅助工作流，不是冻结ML技术目录项。",
  "2":[["V2_GCP","PREFERRED","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0941:2",
  "4":"OUTSIDE:AI coding assistants优先工作流，同上。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[
  {"quote":"Collaborate closely with perception and motion planning experts","description":"感知与运动规划为协作对象，已由继承SEPARATE/COLLABORATION_OBJECT覆盖。"}
 ],
 "notes":"主责抓取与工具选择策略，并自建评测与仿真验证。现场遥测改进不等于客户现场运维岗位。"
},
"N0949":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"DISTRIBUTED_TRAINING_COMPILER_OPT",
 "secondary_task":"",
 "task_evidence":"Design, implement, and optimize distributed training systems that scale across thousands of GPUs and nodes for large-scale training workloads.",
 "new":{
  "1":"REJECT:can为普通助动词，不是CAN总线。",
  "2":"OUTSIDE:NVIDIA acceleration stack泛称工具链，具体TensorRT另登。",
  "3":[["V2_TENSORRT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":"DUPLICATE:N0949:3",
  "5":"OUTSIDE:NVIDIA profiling tools未单列冻结项。",
  "6":[["V2_TENSORRT","GENERAL","CHOICE"]],
  "7":"DUPLICATE:N0949:6",
  "8":"OUTSIDE:Megatron训练框架未在冻结ML细目录中。",
  "9":"OUTSIDE:TorchTitan未在冻结ML细目录中。",
  "10":[["V2_ONNX_RUNTIME","PREFERRED","CHOICE_AND_EXAMPLE"]],
  "11":"DUPLICATE:N0949:10",
  "12":"OUTSIDE:TVM编译器示例，未单列冻结项。",
  "13":"REJECT:洛杉矶县公平机会条例中的customer service套话，不是岗位客户服务职责。",
  "14":"REJECT:旧金山公平机会雇佣套话，不是人力资源岗位技能。"
 },
 "old_overrides":{
  "O7":{"metric":"PREFERRED","branch":"CHOICE_AND_EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"such as Pytorch, Megatron, TorchTitan etc.同时任选示例。"},
  "O11":{"metric":"SEPARATE","branch":"BACKGROUND","relation":"BACKGROUND","reason":"训练系统的security/maintainability标准，不是功能安全完整性。"},
  "O12":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"在大模型与机器人交叉处做性能优化，协作科学家构建，不单独记本人基础模型算法研发。"},
  "O19":{"metric":"SEPARATE","branch":"BACKGROUND","relation":"BACKGROUND","reason":"县条例工作安全套话，不是技术安全职责。"}
 },
 "additions":[],
 "outside_extra":[
  {"quote":"Experience with ML compilers (ONNX Runtime, TVM, etc.)","description":"ONNX Runtime已编码；未把ONNX格式与ONNX Runtime等同。"}
 ],
 "notes":"FAR团队切片，主责大规模分布式训练与编译优化。Manage pre/post training runs是训练作业阶段，不是模型后训练对齐目录。"
},
"E0093":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"DRL_LEGGED_DECISION_PLANNING",
 "secondary_task":"",
 "task_evidence":"研发适用于多自由度机器人、双足、四足仿生机器人决策规划的深度强化学习算法",
 "new":{},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"仅两句职责、无任职资格栏。对象为多自由度/双足/四足决策规划的深度RL，不是导航专项。无新增候选。"
},
"E0588":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"JAX_DISTRIBUTED_TRAINING_INFRA",
 "secondary_task":"",
 "task_evidence":"Own training/inference infrastructure: Design, implement, and maintain systems for large-scale model training, including scheduling, job management, checkpointing, and metrics/logging.",
 "new":{
  "1":"REJECT:can为普通助动词，不是CAN总线。",
  "2":[["V2_SLURM","GENERAL","CHOICE_AND_EXAMPLE"],["V2_GCP","GENERAL","CHOICE_AND_EXAMPLE"],["V2_AWS","GENERAL","CHOICE_AND_EXAMPLE"]],
  "3":"DUPLICATE:E0588:2"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[
  {"quote":"Experience managing training workloads on cloud platforms (e.g., SLURM, Kubernetes, GCP TPU/GKE, AWS).","description":"Kubernetes已由继承覆盖；GKE不另映射为独立目录项。"}
 ],
 "notes":"主责训练/推理基础设施与JAX训练代码演进。JAX (preferred), PyTorch斜线/并列保持继承未解。Evolve model code是支撑新架构的训练代码，不是本人提出新机器人策略。"
},
"N0874":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"LEARNED_MANIPULATION_CONTROL",
 "secondary_task":"",
 "task_evidence":"Train models for robotic manipulation, force control, servoing etc.",
 "new":{
  "1":"REJECT:can为普通助动词，不是CAN总线。",
  "2":"REJECT:can为普通助动词，不是CAN总线。",
  "3":"REJECT:C++不是C语言。",
  "4":[["V2_GIT","PREFERRED","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0874:4"
 },
 "old_overrides":{
  "O13":{"metric":"SEPARATE","branch":"CONDITIONAL","relation":"OWN_DEVELOP","reason":"you may work on sensor fusion，条件性可能任务，不记无条件感知开发。"},
  "O14":{"metric":"SEPARATE","branch":"CONDITIONAL","relation":"OWN_DEVELOP","reason":"同一句may work；状态估计不自动等于SLAM无条件职责。"}
 },
 "additions":[
  {"code":"V2_CI_CD","metric":"PREFERRED","branch":"UNCONDITIONAL","quote":"Experience with Git and modern CI pipelines.","reason":"Nice to have中的现代CI流水线，与Git同句。"}
 ],
 "outside_extra":[
  {"quote":"stay abreast of the latest progress in reinforcement learning, motion planning and controls","description":"跟踪进展不是本人RL/规划职责，继承SEPARATE已覆盖。"}
 ],
 "notes":"主责学习型操作与力控制。Required Skills下multiple of the following为任选组。Docker and Kubernetes优先且同句并列，继承未改。"
}
}

if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
