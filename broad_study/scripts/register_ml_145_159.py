"""First-pass adjudication for ML coding_order 145-159. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"E0495":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VIDEO_PRETRAIN_WORLD_MODEL",
 "secondary_task":"",
 "task_evidence":"Design and train large-scale video foundation models on diverse datasets spanning internet-scale video and robot-collected data",
 "new":{
  "1":R+"英语can与in-office不是CAN协议或Microsoft Office。",
  "2":[["V2_WORLD_MODEL","PREFERRED","CHOICE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"视频预训练。世界模型为加分任选。任务证据用要求句因职责未单独列出世界模型。"
},
"E0491":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"FOUNDATION_PRETRAIN",
 "secondary_task":"",
 "task_evidence":"Design and train large-scale foundation models across multimodal data (e.g., text, vision, and robot data)",
 "new":{
  "1":R+"英语can与in-office不是CAN协议或Microsoft Office。",
  "2":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "3":[["V2_POSTTRAINING","PREFERRED","EXAMPLE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责预训练。后训练为贡献/加分示例。"
},
"E0492":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"HELIX_RL",
 "secondary_task":"",
 "task_evidence":"Design and implement reinforcement learning algorithms for embodied agents operating in real-world and simulated environments",
 "new":{
  "1":R+"英语can与in-office不是CAN协议或Microsoft Office。"
 },
 "old_overrides":{
  "O13":{"metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","relation":"OWN_DEVELOP","reason":"原RL短词定位为空，改为online/offline句。","quote":"Work across online and offline RL settings, including learning from large-scale logged robot data"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责Helix强化学习。"
},
"E0489":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"HELIX_MODELING",
 "secondary_task":"",
 "task_evidence":"Design and develop model architectures for perception, reasoning, and action across multimodal inputs",
 "new":{
  "1":R+"英语can与in-office不是CAN协议或Microsoft Office。",
  "2":[["V2_WORLD_MODEL","PREFERRED","CHOICE"]]
 },
 "old_overrides":{
  "O11":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原vision-language短词定位为空，改为多模态句。","quote":"Experience with multimodal models (vision-language or vision-language-action systems)"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责Helix建模。世界模型为加分任选。"
},
"E0452":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"WBC_TRAIN_INFRA",
 "secondary_task":"",
 "task_evidence":"Own and scale the infrastructure used to train whole-body control policies (simulation, data pipelines, orchestration, visualizations)",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。",
  "2":R+"英语can不是CAN总线协议。",
  "3":[["V2_PHYSX","PREFERRED","EXAMPLE"]],
  "4":"DUPLICATE:E0452:3",
  "5":O+"Warp未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责全身控制训练基础设施。PhysX为仿真示例。"
},
"E0494":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"TRAINING_PERFORMANCE_KERNELS",
 "secondary_task":"",
 "task_evidence":"Optimize training performance for a 100B+ parameter models across 100k+ GPUs.",
 "new":{
  "1":[["V2_PROCUREMENT","SEPARATE","COLLABORATION_OBJECT"]],
  "2":[["V2_TRITON_COMPILER","DUTY_OWN_DEVELOP","UNRESOLVED"]],
  "3":[["V2_TRITON_COMPILER","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "4":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":[["V2_FSDP","DUTY_OWN_USE","EXAMPLE"]],
  "6":[["V2_NSIGHT","GENERAL","CHOICE_AND_EXAMPLE"]],
  "7":[["V2_NCCL","GENERAL","UNCONDITIONAL"]],
  "8":R+"CUDA/C++不是C语言。",
  "9":[["V2_VLLM","PREFERRED","EXAMPLE"],["V2_DEEPSPEED","PREFERRED","EXAMPLE"]],
  "10":"DUPLICATE:E0494:6"
 },
 "old_overrides":{
  "O5":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原PyTorch短词定位为空，改为Profiler句。","quote":"Proficiency with profiling tools (Nsight Systems/Compute, PyTorch Profiler, HTA, or similar) and ability to translate traces into concrete optimizations"},
  "O13":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原heterogeneous短词定位为空，改为多数据中心句。","quote":"Experience with heterogeneous or multi-datacenter training setups and cross-cluster orchestration"}
 },
 "additions":[],
 "outside_extra":[{"quote":"hardware procurement decisions","description":"采购为协作对象。Triton/CUDA按编译器未解。"}],
 "notes":"主责训练性能与kernel。Triton此处是编译器。"
},
"N0909":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"MTS_GENERAL",
 "secondary_task":"",
 "task_evidence":"We’re training robot AGI to power a proprietary generalist supply chain superhumanoid, the first robot in the world capable of performing thousands of tasks across the supply chain.",
 "new":{
  "1":R+"Series C融资轮次不是C语言。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"Nimble MTS。Series C假阳性。"
},
"N0895":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"AI_ROBOTICS_RESEARCH",
 "secondary_task":"",
 "task_evidence":"We’ve raised over $220M at over $1B valuation and formed a strategic alliance with FedEx to build a national network of autonomous warehouses capable of generating many billions in annual revenue.",
 "new":{
  "1":R+"Series C融资轮次不是C语言。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"Nimble研究工程。Series C假阳性。"
},
"N0709":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"AI_INFERENCE_RUNTIME",
 "secondary_task":"",
 "task_evidence":"We are looking for a Software Engineer to work at the forefront of deploying our cutting-edge AI models, enhancing the performance and capabilities of our embodied systems.",
 "new":{
  "1":"DUPLICATE:N0709:4",
  "2":O+"state machines未单列冻结项。",
  "3":O+"multi-agent systems未单列冻结项。",
  "4":[["V2_C","GENERAL","EXAMPLE"]],
  "5":O+"machine learning compilers未单列冻结项。",
  "6":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"C, C++, Rust, Go","description":"低级语言示例明确写出C，按示例编码。"}],
 "notes":"主责推理优化。显式C语言示例成立。"
},
"N0710":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"AI_TRAINING_INFRA",
 "secondary_task":"",
 "task_evidence":"We are looking for a Software Engineer to work at the forefront of developing and optimizing the software infrastructure and tools necessary for training cutting-edge AI models.",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":R+"Python, C++, or similar不是C语言。",
  "4":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"]],
  "5":"DUPLICATE:N0710:4","6":"DUPLICATE:N0710:4","7":"DUPLICATE:N0710:4",
  "8":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "9":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责训练基础设施。C++拒收C。云平台任选。"
},
"N0685":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RESEARCH_ENGINEER_GENERAL",
 "secondary_task":"",
 "task_evidence":"you'll work with researchers and engineers to implement state-of-the-art machine learning and robot systems.",
 "new":{
  "1":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"Skild研究工程。仅薪酬USD假阳性。"
},
"N0664":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"DL_MANIPULATION",
 "secondary_task":"",
 "task_evidence":"You will design, train, and deploy algorithms that enable robots to interact intelligently and adapt to their environments.",
 "new":{
  "1":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"操作深度学习。仅薪酬USD假阳性。"
},
"N0673":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_ROBOT_ENV",
 "secondary_task":"",
 "task_evidence":"designing and implementing cutting-edge reinforcement learning algorithms, conducting experiments, and optimizing these models to perform efficiently in real-world robotic environments.",
 "new":{
  "1":R+"Python, C++, or similar不是C语言。",
  "2":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"强化学习工程。C++拒收C。"
},
"N0662":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"CV_PERCEPTION_ROBOTICS",
 "secondary_task":"",
 "task_evidence":"design, build, and deploy advanced perception systems for real-world robotics and automation.",
 "new":{
  "1":R+"familiarity with C++ is a plus不是C语言。",
  "2":[["V2_BLENDER","PREFERRED","EXAMPLE"]],
  "3":"DUPLICATE:N0662:2",
  "4":O+"MLOps practices未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"视觉感知。Blender为仿真示例。C++加分拒收C。"
},
"N0663":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"CV_PERCEPTION_ROBOTICS",
 "secondary_task":"",
 "task_evidence":"design, build, and deploy advanced perception systems for real-world robotics and automation.",
 "new":{
  "1":R+"familiarity with C++ is a plus不是C语言。",
  "2":[["V2_BLENDER","PREFERRED","EXAMPLE"]],
  "3":"DUPLICATE:N0663:2",
  "4":O+"MLOps practices未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"与N0662近重复的视觉感知岗。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
