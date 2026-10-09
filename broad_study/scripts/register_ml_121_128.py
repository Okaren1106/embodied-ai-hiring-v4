"""First-pass adjudication for ML coding_order 121-128. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"E0341":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"ML_PLATFORM_CICD",
 "secondary_task":"",
 "task_evidence":"Implement the CI/CD lifecycle for ML that enable continuous retraining, automated testing, and seamless model delivery to production environments",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_AIRFLOW","GENERAL","EXAMPLE"]],
  "4":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"],["V2_TERRAFORM","GENERAL","EXAMPLE"]],
  "5":R+"薪酬USD不是Universal Scene Description。",
  "6":R+"第三方招聘免责声明不是HR专业职责。",
  "7":"DUPLICATE:E0341:4",
  "8":"DUPLICATE:E0341:4"
 },
 "old_overrides":{
  "O13":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原ML infrastructure短词定位为空，改为年限句。","quote":"at least 2+ years working on ML infrastructure, data platforms or MLOps systems in production environments."},
  "O18":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原ML infrastructure短词定位为空，改为开源加分句。","quote":"Contributions to open-source ML infrastructure or MLOps tooling a plus."}
 },
 "additions":[],
 "outside_extra":[{"quote":"Kubeflow","description":"编排工具等列保留目录外项。"}],
 "notes":"主责ML平台CI/CD。云平台任选。薪酬与招聘免责拒收。"
},
"N0957":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"MANIP_LEARNING_FRONTIER",
 "secondary_task":"",
 "task_evidence":"Design and implement robot learning algorithms for manipulation",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":[["V2_MOCAP","PREFERRED","CHOICE"]],
  "3":"DUPLICATE:N0957:2",
  "4":R+"洛杉矶郡通用雇佣条款不是客户服务职责。",
  "5":R+"招聘伙伴联系说明不是HR专业职责。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"操作学习岗。动捕为加分任选。CAN/客服/HR为假阳性。"
},
"N0954":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"CLOUD_DATA_INFRA_FAR",
 "secondary_task":"",
 "task_evidence":"design and operate the distributed infrastructure that enables our researchers and engineers to train foundation models",
 "new":{
  "1":R+"e.g. Go, Java, C++不是C语言；示例保持示例。",
  "2":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"]],
  "3":"DUPLICATE:N0954:2","4":"DUPLICATE:N0954:2","5":"DUPLICATE:N0954:2",
  "6":O+"ETL未单列冻结项。",
  "7":[["V2_SPARK","PREFERRED","EXAMPLE"],["V2_FLINK","PREFERRED","EXAMPLE"]],
  "8":"DUPLICATE:N0954:7","9":"DUPLICATE:N0954:7",
  "10":R+"洛杉矶郡通用雇佣条款不是客户服务职责。",
  "11":R+"招聘伙伴联系说明不是HR专业职责。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"Ray","description":"Ray与Spark/Flink同列示例。FAR实体整司均值排除，本条仍编码。"}],
 "notes":"FAR基础设施岗。云平台任选。C++示例拒收C。"
},
"E0414":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_HUMANOID_RETARGET",
 "secondary_task":"",
 "task_evidence":"Develop and refine motion retargeting pipelines to translate human demonstration data (mocap, teleoperation) into robust reference trajectories for reinforcement learning.",
 "new":{
  "1":R+"英语can/key不是CAN总线协议。",
  "2":[["V2_TELEOP","DUTY_OWN_USE","EXAMPLE"],["V2_MOCAP","DUTY_OWN_USE","EXAMPLE"]],
  "3":R+"C++不是C语言。",
  "4":[["V2_SIM2REAL","GENERAL","EXAMPLE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责人形RL。动捕/遥操服务重定向。C++拒收C。"
},
"E0435":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"MLOPS_PLATFORM_ONROBOT",
 "secondary_task":"",
 "task_evidence":"Apptronik is seeking a Staff MLOps Engineer to own the technical direction of our MLOps platform — the system of record for datasets, experiments, model artifacts, and serving paths that connects teleoperation data collection on one side to deployed autonomy on Apollo on the other.",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"can be traced不是CAN总线协议。",
  "3":[["V2_ONNX","DUTY_OWN_USE","EXAMPLE"],["V2_TENSORRT","DUTY_OWN_USE","EXAMPLE"]],
  "4":R+"Go, Rust, or C++不是C语言；示例保持示例。",
  "5":[["V2_GIT","GENERAL","UNCONDITIONAL"],["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"],["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_ONNX_RUNTIME","PREFERRED","EXAMPLE"],["V2_TENSORRT","PREFERRED","EXAMPLE"],["V2_ONNX","PREFERRED","EXAMPLE"]],
  "7":[["V2_TELEOP","PREFERRED","CHOICE"]],
  "8":"DUPLICATE:E0435:3",
  "9":O+"DVC/LakeFS/Delta未单列冻结项。",
  "10":O+"Determined未单列冻结项。",
  "11":O+"BentoML/KServe未单列冻结项。"
 },
 "old_overrides":{
  "O6":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原MLflow短词定位为空，改为实验跟踪句。","quote":"experiment tracking (MLflow, W&B, Determined)"},
  "O12":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原MLflow短词定位为空，改为平台交付句。","quote":"Proven experience owning and delivering an MLOps platform end-to-end — dataset lifecycle, experiment tracking, model registry, evaluation, and serving — at a company that ships models to production"},
  "O21":{"metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","relation":"OWN_DEVELOP","reason":"原MLOps platform短词定位为空，改为技术方向句。","quote":"own the technical direction of our MLOps platform"},
  "O23":{"metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","relation":"OWN_DEVELOP","reason":"原evaluation短词定位为空，改为harness句。","quote":"evaluation harnesses"},
  "O27":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原ML models短词定位为空，改为评测框架句。","quote":"evaluation and qualification frameworks for ML models where the cost of a regression is high (robotics, safety-critical, or production-customer-facing)"},
  "O29":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原ML models短词定位为空，改为边缘部署句。","quote":"Experience deploying ML models to edge or embedded targets (on-device inference, ONNX Runtime, TensorRT, robot fleets)"}
 },
 "additions":[],
 "outside_extra":[{"quote":"teleoperation data collection","description":"遥操是数据侧对象，MLOps岗使用而非开发遥操产品。"}],
 "notes":"主责MLOps平台。Git明确工具。ONNX≠ONNX Runtime，两条分别编码。"
},
"E0415":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_HUMANOID_RETARGET",
 "secondary_task":"",
 "task_evidence":"Develop and refine motion retargeting pipelines to translate human demonstration data (mocap, teleoperation) into robust reference trajectories for reinforcement learning.",
 "new":{
  "1":R+"英语can/key不是CAN总线协议。",
  "2":[["V2_TELEOP","DUTY_OWN_USE","EXAMPLE"],["V2_MOCAP","DUTY_OWN_USE","EXAMPLE"]],
  "3":R+"C++不是C语言。",
  "4":[["V2_SIM2REAL","GENERAL","EXAMPLE"]],
  "5":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"与E0414近重复，薪酬句额外拒收USD。"
},
"N1044":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VLA_ATLAS",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"Build large-scale imitation learning pipelines that learn from human demonstrations, teleoperation, and simulation data.",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"Python and C++不是C语言。",
  "3":R+"C++ or Python不是C语言。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责Atlas VLA。遥操服务模仿学习数据。"
},
"N1014":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_STACK_SIM2REAL",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"you'll own the RL stack, including massively parallel simulation, domain randomization, policy optimization, and on-robot deployment.",
 "new":{
  "1":[["V2_DOMAIN_RANDOMIZATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":O+"RSL-RL未单列冻结项。","4":O+"CleanRL未单列冻结项。","5":O+"RLlib未单列冻结项。","6":O+"Stable Baselines未单列冻结项。","7":O+"MjWarp未单列冻结项。","8":O+"MjLab未单列冻结项。",
  "9":[["V2_ONNX","GENERAL","CHOICE"],["V2_TENSORRT","GENERAL","CHOICE"]],
  "10":"DUPLICATE:N1014:9",
  "11":R+"推理运行时Triton更可能是Inference Server，不是GPU编译器的充分证据。",
  "12":"DUPLICATE:N1014:9",
  "13":[["V2_BAZEL","GENERAL","UNCONDITIONAL"],["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "14":"DUPLICATE:N1014:13","15":"DUPLICATE:N1014:13",
  "16":[["V2_SYSID","PREFERRED","CHOICE"],["V2_SIM2REAL","PREFERRED","CHOICE"],["V2_DOMAIN_RANDOMIZATION","PREFERRED","CHOICE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"Triton","description":"与ONNX/TensorRT并列的inference runtimes，不按Triton编译器编码。"}],
 "notes":"主责RL栈与Sim2Real。ONNX/TensorRT为推理运行时任选。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
