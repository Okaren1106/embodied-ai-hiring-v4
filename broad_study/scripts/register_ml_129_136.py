"""First-pass adjudication for ML coding_order 129-136. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"N0984":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_SPOT_LAST_MILE",
 "secondary_task":"",
 "task_evidence":"Design, implement, train, and deploy state-of-the-art ML/RL algorithms for complex last-mile delivery challenges",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":R+"Python and/or C++不是C语言。",
  "3":R+"Python or C++不是C语言。",
  "4":O+"modern AI coding tools未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责Spot末公里ML/RL。C++任选拒收C。"
},
"N1034":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"INDUSTRIAL_INSPECTION_FOUNDATION",
 "secondary_task":"",
 "task_evidence":"Be a lead on a team of ~5 machine learning engineers.",
 "new":{},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"候选队列为空。Orbit工业巡检基础模型，属其他模型应用管理岗。"
},
"N0868":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"CV_SEGMENTATION_WAREHOUSE",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"you will be working on writing Computer Vision code and building Machine Learning models for computer vision.",
 "new":{
  "1":R+"语义分割句不含C语言。",
  "2":R+"低延迟推理不是运行排障/事件升级。",
  "3":R+"英语can不是CAN总线协议。",
  "4":R+"英语can不是CAN总线协议。",
  "5":[["V2_OPEN3D","GENERAL","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0868:5",
  "7":R+"Modern C++不是C语言。",
  "8":R+"NVIDIA Triton serving architecture不是GPU编译器的充分证据。",
  "9":R+"NVIDIA Triton serving architecture不是GPU编译器的充分证据。",
  "10":O+"TorchServe未单列冻结项。",
  "11":O+"Tensorflow Serving按服务栈，不单列冻结项。",
  "12":O+"Flask未单列冻结项。",
  "13":[["V2_AWS","GENERAL","EXAMPLE"],["V2_GCP","GENERAL","EXAMPLE"],["V2_AZURE","GENERAL","EXAMPLE"]],
  "14":"DUPLICATE:N0868:13","15":"DUPLICATE:N0868:13","16":"DUPLICATE:N0868:13",
  "17":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "18":"DUPLICATE:N0868:17"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"NVIDIA Triton","description":"与TorchServe并列的serving architecture，不按Triton编译器编码。Git明确工具。"}],
 "notes":"主责仓储视觉分割。Open3D成立。Git成立。"
},
"N0859":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"CV_ML_LEADERSHIP",
 "secondary_task":"",
 "task_evidence":"At Dexterity, we believe robots can positively transform the world.",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":R+"英语can不是CAN总线协议。",
  "3":R+"Modern C++不是C语言。",
  "4":[["V2_AWS","GENERAL","EXAMPLE"],["V2_GCP","GENERAL","EXAMPLE"],["V2_AZURE","GENERAL","EXAMPLE"]],
  "5":"DUPLICATE:N0859:4","6":"DUPLICATE:N0859:4","7":"DUPLICATE:N0859:4",
  "8":R+"英语can/interested不是CAN总线协议。",
  "9":R+"RGBD/point clouds句既不是C语言也不是运行排障。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"视觉ML负责人格。云平台示例。C++拒收C。"
},
"N0878":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"ML_WAREHOUSE_POLICY",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"You will also work closely with the data platform, physics simulation, and robot operations teams",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":R+"英语can不是CAN总线协议。",
  "3":[["V2_WORLD_MODEL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"Python (and C++ where required)不是C语言。",
  "5":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"]],
  "6":"DUPLICATE:N0878:5","7":"DUPLICATE:N0878:5","8":"DUPLICATE:N0878:5",
  "9":[["V2_GIT","GENERAL","UNCONDITIONAL"],["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "10":"DUPLICATE:N0878:9","11":"DUPLICATE:N0878:9",
  "12":R+"NVIDIA Triton serving stack不是GPU编译器的充分证据。",
  "13":R+"NVIDIA Triton serving stack不是GPU编译器的充分证据。",
  "14":O+"TorchServe未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"internal world model","description":"内部世界模型按世界模型使用编码。"}],
 "notes":"仓储ML工程。Git/CI/CD成立。Triton按服务栈拒收编译器。"
},
"N0876":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"AI_ALGORITHMS_WAREHOUSE",
 "secondary_task":"",
 "task_evidence":"Our systems are software-driven and hardware-agnostic and have already picked 100+ million goods in production.",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":R+"英语can不是CAN总线协议。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"算法岗简介CAN假阳性。候选仅2条。"
},
"N0798":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"LOCOMOTION_RL_SIM2REAL",
 "secondary_task":"",
 "task_evidence":"Design policy architectures, training curricula, and domain randomization strategies that close the sim-to-real gap",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_DOMAIN_RANDOMIZATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":R+"agile locomotion不是项目计划与风险管理方法。",
  "4":[["V2_SIM2REAL","GENERAL","UNCONDITIONAL"]],
  "5":R+"Python and/or C++不是C语言。",
  "6":[["V2_ONNX_RUNTIME","PREFERRED","EXAMPLE"],["V2_TENSORRT","PREFERRED","EXAMPLE"],["V2_ONNX","PREFERRED","EXAMPLE"]],
  "7":"DUPLICATE:N0798:6","8":"DUPLICATE:N0798:6",
  "9":[["V2_CLASSICAL_CONTROL","PREFERRED","CHOICE"]],
  "10":"DUPLICATE:N0798:9",
  "11":[["V2_TELEOP","PREFERRED","CHOICE"],["V2_MOCAP","PREFERRED","CHOICE"]],
  "12":[["V2_SIM2REAL","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责足式/人形运动RL。ONNX Runtime与ONNX分开保留。MPC记经典控制。"
},
"N0725":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"AGENTIC_MULTIMODAL_RAG",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"Build and optimize\nMulti-VectorRAG pipelines\nwith\nvector DBs and knowledge graphs\n.",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0725:1",
  "3":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":"DUPLICATE:N0725:3",
  "5":"DUPLICATE:N0725:3",
  "6":O+"knowledge graphs未单列冻结项。",
  "7":[["V2_AWS","GENERAL","CHOICE"]],
  "8":"DUPLICATE:N0725:7",
  "9":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "10":[["V2_HUGGINGFACE","GENERAL","EXAMPLE"],["V2_DEEPSPEED","GENERAL","EXAMPLE"],["V2_VLLM","GENERAL","EXAMPLE"],["V2_FSDP","GENERAL","EXAMPLE"],["V2_MODEL_COMPRESSION","GENERAL","EXAMPLE"]],
  "11":"DUPLICATE:N0725:10","12":"DUPLICATE:N0725:10","13":"DUPLICATE:N0725:10","14":"DUPLICATE:N0725:10",
  "15":"DUPLICATE:N0725:10","16":"DUPLICATE:N0725:10",
  "17":[["V2_MODEL_COMPRESSION","GENERAL","EXAMPLE"]],
  "18":"DUPLICATE:N0725:17",
  "19":[["V2_AGENT_WORKFLOW","PREFERRED","UNCONDITIONAL"]],
  "20":"DUPLICATE:N0725:19",
  "21":[["V2_AGENT_WORKFLOW","PREFERRED","EXAMPLE"]],
  "22":"DUPLICATE:N0725:21","23":"DUPLICATE:N0725:21",
  "24":O+"LlamaIndex未单列冻结项。","25":O+"OpenSearch未单列冻结项。","26":O+"FAISS未单列冻结项。","27":O+"Pinecone未单列冻结项。",
  "28":"DUPLICATE:N0725:17",
  "29":[["V2_AGENT_WORKFLOW","PREFERRED","EXAMPLE"]],
  "30":"DUPLICATE:N0725:29",
  "31":O+"scene graphs未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"LoRA/QLoRA","description":"目录压缩项含低秩适配。quantization明确压缩。"}],
 "notes":"主责agentic/RAG多模态。LoRA按压缩示例。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
