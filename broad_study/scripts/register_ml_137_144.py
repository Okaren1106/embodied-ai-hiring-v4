"""First-pass adjudication for ML coding_order 137-144. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"N0814":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"E2E_NAV_LEARNING",
 "secondary_task":"",
 "task_evidence":"Design, train, and deploy state-of-the-art machine learning models for end-to-end learning based navigation stack.",
 "new":{
  "1":R+"working knowledge of C++不是C语言。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责端到端导航学习栈。C++拒收C。"
},
"N0815":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"ML_PLATFORM_IAC",
 "secondary_task":"",
 "task_evidence":"Design and manage scalable ML infrastructure\nwith IaC tools (Terraform, CloudFormation).",
 "new":{
  "1":[["V2_TERRAFORM","DUTY_OWN_USE","EXAMPLE"]],
  "2":O+"CloudFormation未单列冻结项。",
  "3":"DUPLICATE:N0815:1",
  "4":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_TYPESCRIPT","GENERAL","UNRESOLVED"]],
  "6":"DUPLICATE:N0815:5",
  "7":[["V2_AWS","PREFERRED","UNCONDITIONAL"]],
  "8":"DUPLICATE:N0815:7",
  "9":O+"EKS未单列冻结项。",
  "10":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0815:10",
  "12":"DUPLICATE:N0815:1",
  "13":"DUPLICATE:N0815:1",
  "14":O+"CloudFormation未单列冻结项。",
  "15":[["V2_AIRFLOW","PREFERRED","EXAMPLE"]],
  "16":O+"Kubeflow未单列冻结项。",
  "17":"DUPLICATE:N0815:15",
  "18":O+"OpenSearch未单列冻结项。","19":O+"Pinecone未单列冻结项。","20":O+"Weaviate未单列冻结项。",
  "21":[["V2_DEEPSPEED","PREFERRED","EXAMPLE"],["V2_FSDP","PREFERRED","EXAMPLE"],["V2_DDP","PREFERRED","EXAMPLE"]],
  "22":O+"Horovod未单列冻结项。",
  "23":"DUPLICATE:N0815:21","24":"DUPLICATE:N0815:21","25":"DUPLICATE:N0815:21",
  "26":O+"Karpenter未单列冻结项。","27":O+"SageMaker未单列冻结项。","28":O+"EKS未单列冻结项。",
  "29":[["V2_AGENT_WORKFLOW","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"Python/TypeScript","description":"斜线语言记TypeScript未解。"}],
 "notes":"主责ML平台与IaC。Terraform/CI/CD/Airflow/AWS成立。"
},
"N0848":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"DISTRIBUTED_ML_SYSTEMS",
 "secondary_task":"",
 "task_evidence":"We are seeking a Staff ML Systems Engineer to architect and build the distributed infrastructure that powers large-scale machine learning workflows across the organization.",
 "new":{
  "1":[["V2_SPARK","GENERAL","EXAMPLE"],["V2_FLINK","GENERAL","EXAMPLE"]],
  "2":"DUPLICATE:N0848:1",
  "3":O+"Dask未单列冻结项。",
  "4":"DUPLICATE:N0848:1",
  "5":[["V2_DDP","GENERAL","EXAMPLE"],["V2_FSDP","GENERAL","EXAMPLE"],["V2_DEEPSPEED","GENERAL","EXAMPLE"]],
  "6":"DUPLICATE:N0848:5","7":"DUPLICATE:N0848:5","8":"DUPLICATE:N0848:5"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"Ray","description":"与Spark/Flink同列分布式框架示例。"}],
 "notes":"主责分布式ML系统。"
},
"N0722":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"POINTCLOUD_3D_ML",
 "secondary_task":"",
 "task_evidence":"Design and implement scalable machine learning pipelines for large-scale 3D spatial data processing for point cloud analysis, object detection, segmentation, and scene understanding.",
 "new":{
  "1":[["V2_AWS","DUTY_OWN_USE","EXAMPLE"]],
  "2":"DUPLICATE:N0722:1",
  "3":O+"SageMaker未单列冻结项。","4":O+"EC2未单列冻结项。",
  "5":"DUPLICATE:N0722:1",
  "6":O+"SageMaker未单列冻结项。","7":O+"SageMaker未单列冻结项。",
  "8":O+"BIM未单列冻结项。",
  "9":[["V2_PCL","GENERAL","UNCONDITIONAL"]],
  "10":"DUPLICATE:N0722:9",
  "11":[["V2_AWS","GENERAL","EXAMPLE"]],
  "12":O+"BIM data未单列冻结项。","13":O+"digital twins未单列冻结项。","14":O+"GIS systems未单列冻结项。","15":O+"Kubeflow未单列冻结项。",
  "16":[["V2_3D_RECONSTRUCTION","PREFERRED","EXAMPLE"]],
  "17":"DUPLICATE:N0722:16",
  "18":O+"Occupancy Networks未单列冻结项。",
  "19":[["V2_OPEN3D","PREFERRED","EXAMPLE"]],
  "20":"DUPLICATE:N0722:19",
  "21":O+"Torch-Points3D未单列冻结项。","22":O+"PyG未单列冻结项。","23":O+"MMDetection3D未单列冻结项。","24":O+"SparseConvNet未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"NeRF","description":"NeRF按三维重建示例。Open3D-ML按Open3D生态示例。"}],
 "notes":"主责三维点云ML，属其他模型应用。PCL/Open3D/AWS/NeRF成立。"
},
"N0821":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"LEARNED_MANIP_HUMANOID",
 "secondary_task":"",
 "task_evidence":"building, training, testing, and refining large-scale learned manipulation models and capabilities that accelerate autonomous control and loco-manipulation on humanoid robots.",
 "new":{
  "1":R+"英语can/unique不是CAN总线协议。",
  "2":R+"英语can不是CAN总线协议。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"操作研究工程岗。候选仅CAN假阳性。"
},
"E0493":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"HELIX_VISUOMOTOR_VLA",
 "secondary_task":"",
 "task_evidence":"Design, train, evaluate, and deploy\nlearning-based visuomotor policies\nfor humanoid robot manipulation",
 "new":{
  "1":R+"Python and/or C++不是C语言。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"Helix机器人学习。C++任选拒收C。"
},
"E0544":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_WBC",
 "secondary_task":"",
 "task_evidence":"Develop, train, and deploy reinforcement learning algorithms for whole body control",
 "new":{
  "1":R+"公司介绍/in-office不是Microsoft Office。",
  "2":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_DOMAIN_RANDOMIZATION","GENERAL","EXAMPLE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责全身控制RL。Office假阳性。"
},
"E0487":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"GENERATIVE_WORLD_MODEL",
 "secondary_task":"",
 "task_evidence":"Design, train, and deploy large-scale generative models, with a focus on diffusion-based approaches for vision, video, and multimodal data",
 "new":{
  "1":R+"英语can与in-office不是CAN协议或Microsoft Office。",
  "2":[["V2_WORLD_MODEL","GENERAL","CHOICE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责生成式模型。世界模型为熟悉任选。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
