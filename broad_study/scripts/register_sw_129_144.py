"""First-pass adjudication for software coding_order 129-144. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
def devops(rid):
 return {
  "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
  "task":"DEV_INFRA","fine_task":"DEVOPS","secondary_task":"",
  "task_evidence":"Build and maintain CI/CD pipelines across robotics, AI, and software systems using tools such as GitHub Actions.",
  "new":{
   "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_GITHUB_ACTIONS","DUTY_OWN_USE","EXAMPLE"]],
   "2":f"DUPLICATE:{rid}:1","3":f"DUPLICATE:{rid}:1",
   "4":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
   "5":f"DUPLICATE:{rid}:4",
   "6":[["V2_SHELL","GENERAL","CHOICE"]],
   "7":f"DUPLICATE:{rid}:6",
   "8":[["V2_TERRAFORM","PREFERRED","CHOICE"]],
   "9":f"DUPLICATE:{rid}:8",
   "10":O+"Helm未单列冻结项。","11":O+"ArgoCD未单列冻结项。",
   "12":O+"CKA未单列冻结项。","13":O+"CKAD未单列冻结项。","14":O+"CKS未单列冻结项。"
  },
  "old_overrides":{},"additions":[],"outside_extra":[],
  "notes":"DevOps。GitHub Actions不升Git。Helm/ArgoCD/认证目录外。"
 }
decisions={
"N0860":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"PLM_DOCUMENT_CONTROL","secondary_task":"",
 "task_evidence":"In this role, you will manage all aspects of Engineering Change Order (ECO) and Bill of Material (BOM) management, ensuring that these critical documents are accurate, up-to-date, and complete.",
 "new":{
  "1":R+"英语can不是CAN总线协议。","2":R+"英语can不是CAN总线协议。",
  "3":R+"project management skills不是Microsoft Project。",
  "4":[["V2_PLM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_PLM","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":[["V2_PLM","DUTY_OWN_USE","CONDITIONAL"]],
  "7":"DUPLICATE:N0860:6",
  "8":[["V2_PLM","GENERAL","UNCONDITIONAL"]],
  "9":[["V2_PLM","GENERAL","UNCONDITIONAL"]],
  "10":R+"project management skills不是Microsoft Project。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"制造文档/PLM。英语can与项目管理技能拒收。"
},
"N0846":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"FEDERAL_INTEGRATION","secondary_task":"CUSTOMER_INTEGRATION",
 "task_evidence":"Drive strategic integration, debugging, and rapid capability development while providing essential software support",
 "new":{
  "1":[["V2_C","GENERAL","UNRESOLVED"]],
  "2":"DUPLICATE:N0846:1",
  "3":[["V2_PROJECT_METHOD","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_JIRA","PREFERRED","CHOICE"],["V2_CONFLUENCE","PREFERRED","CHOICE"]],
  "5":"DUPLICATE:N0846:4",
  "6":O+"Wrike未单列冻结项。",
  "7":"DUPLICATE:N0846:4",
  "8":R+"C.F.R/Citizen不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"联邦平台集成。C/C++按C未解。Wrike目录外。"
},
"N0838":devops("N0838"),
"N0837":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"DEVELOPER_INFRA","secondary_task":"",
 "task_evidence":"Own and improve monorepo build systems, file structure, and documentation",
 "new":{
  "1":[["V2_BAZEL","PREFERRED","CHOICE"]],
  "2":"DUPLICATE:N0837:1",
  "3":R+"Nx JS monorepo不是Siemens NX。",
  "4":[["V2_CI_CD","PREFERRED","UNCONDITIONAL"],["V2_GITHUB_ACTIONS","PREFERRED","EXAMPLE"]],
  "5":"DUPLICATE:N0837:4","6":"DUPLICATE:N0837:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"开发者基础设施。Nx拒收Siemens NX。GitHub Actions不升Git。"
},
"N0732":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"WEB_DEVOPS","secondary_task":"",
 "task_evidence":"Own and improve CI/CD pipelines for web services and applications (Node.js, React)",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_NODEJS","DUTY_OWN_USE","EXAMPLE"],["V2_REACT","DUTY_OWN_USE","EXAMPLE"]],
  "2":"DUPLICATE:N0732:1","3":"DUPLICATE:N0732:1",
  "4":[["V2_AWS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0732:4",
  "6":[["V2_AWS","GENERAL","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0732:6",
  "8":[["V2_CI_CD","GENERAL","UNCONDITIONAL"],["V2_GITHUB_ACTIONS","GENERAL","EXAMPLE"]],
  "9":"DUPLICATE:N0732:8",
  "10":[["V2_NODEJS","GENERAL","UNCONDITIONAL"],["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"],["V2_REACT","GENERAL","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0732:10","12":"DUPLICATE:N0732:10","13":"DUPLICATE:N0732:10",
  "14":[["V2_MONGODB","PREFERRED","CHOICE"]],
  "15":"DUPLICATE:N0732:14"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Web平台DevOps。Node.js/React不升JavaScript。GitHub Actions不升Git。"
},
"N0832":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"BEHAVIOR_INTERACTION","secondary_task":"",
 "task_evidence":"Own the behavior and mission layer that operationalizes autonomy: design and build the software that turns core autonomy capabilities into repeatable, reliable, customer-facing missions.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":[["V2_TELEOP","GENERAL","CHOICE_AND_EXAMPLE"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"行为与交互软件。C++拒收C。遥操为操作员系统任选示例。"
},
"N0726":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"AI_SOLUTIONS","secondary_task":"",
 "task_evidence":"Build and ship production AI features that deliver measurable customer value.",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","GENERAL","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0726:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"客户AI解决方案。Agent工作流为任职要求。"
},
"N0801":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"SAFETY_SOFTWARE","secondary_task":"",
 "task_evidence":"Own and evolve the safety layer that runs independently of perception, planning, and learned policies, and extend it to new wheeled, legged, and humanoid platforms",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":[["V2_HIL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"C++不是C语言。",
  "4":[["V2_SAFETY_STANDARDS","GENERAL","EXAMPLE"]],
  "5":"DUPLICATE:N0801:4","6":"DUPLICATE:N0801:4","7":"DUPLICATE:N0801:4"
 },
 "old_overrides":{},
 "additions":[{"code":"V2_SAFETY_ANALYSIS","metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","quote":"Lead hazard analysis and safety case development for new platforms and new deployments","reason":"主责危害分析与安全论证。"}],
 "outside_extra":[],
 "notes":"安全层软件。HIL成立、不升仿真。C++拒收C。ISO示例记安全标准。"
},
"N0807":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"PRODUCT_SECURITY","secondary_task":"",
 "task_evidence":"Design and improve the security architecture of autonomous robotic systems operating in real-world environments",
 "new":{
  "1":[["V2_DDS","PREFERRED","CHOICE"]],
  "2":"DUPLICATE:N0807:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人产品安全。ROS或DDS加分任选。"
},
"N0842":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"PRODUCT_INFRA","secondary_task":"",
 "task_evidence":"Design, deploy, and operate cloud infrastructure on AWS using infrastructure-as-code tooling such as AWS CDK and Terraform",
 "new":{
  "1":[["V2_AWS","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_TERRAFORM","DUTY_OWN_USE","EXAMPLE"]],
  "2":"DUPLICATE:N0842:1","3":"DUPLICATE:N0842:1","4":"DUPLICATE:N0842:1",
  "5":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_GIT","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_GITHUB_ACTIONS","DUTY_OWN_USE","EXAMPLE"]],
  "6":"DUPLICATE:N0842:5","7":"DUPLICATE:N0842:5",
  "8":O+"ArgoCD未单列冻结项。",
  "9":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "10":[["V2_AWS","GENERAL","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0842:10",
  "12":O+"IAM未单列冻结项。",
  "13":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_AWS","GENERAL","CHOICE"]],
  "14":"DUPLICATE:N0842:13","15":"DUPLICATE:N0842:13",
  "16":O+"CloudFormation未单列冻结项。",
  "17":[["V2_TYPESCRIPT","GENERAL","CHOICE"]],
  "18":"DUPLICATE:N0842:17",
  "19":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "20":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "21":"DUPLICATE:N0842:20",
  "22":O+"ArgoCD未单列冻结项。",
  "23":[["V2_PROMETHEUS","PREFERRED","EXAMPLE"],["V2_GRAFANA","PREFERRED","EXAMPLE"]],
  "24":"DUPLICATE:N0842:23","25":"DUPLICATE:N0842:23",
  "26":O+"OpenTelemetry未单列冻结项。","27":O+"Datadog未单列冻结项。",
  "28":[["V2_KAFKA","PREFERRED","CHOICE"],["V2_POSTGRESQL","PREFERRED","CHOICE"],["V2_REDIS","PREFERRED","CHOICE"]],
  "29":"DUPLICATE:N0842:28","30":"DUPLICATE:N0842:28","31":"DUPLICATE:N0842:28",
  "32":O+"KEDA未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"产品基础设施。GitOps记Git。ArgoCD/IAM/CloudFormation/KEDA目录外。"
},
"N0834":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"ROBOTICS_PLATFORM","secondary_task":"",
 "task_evidence":"Architect the software platform for physical AI",
 "new":{
  "1":R+"英语can不是CAN总线协议。","2":R+"英语can不是CAN总线协议。",
  "3":R+"英语can不是CAN总线协议。","4":R+"英语can不是CAN总线协议。",
  "5":R+"英语can不是CAN总线协议。",
  "6":R+"现代C++不是C语言。",
  "7":R+"英语can不是CAN总线协议。",
  "8":[["V2_DDS","GENERAL","CHOICE"],["V2_ZENOH","GENERAL","CHOICE"]],
  "9":"DUPLICATE:N0834:8","10":"DUPLICATE:N0834:8",
  "11":O+"MQTT未单列冻结项。",
  "12":[["V2_HIL","GENERAL","UNCONDITIONAL"]],
  "13":"DUPLICATE:N0834:12"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人平台。英语can与C++拒收。SIL不记功能安全。HIL不升仿真。MQTT目录外。"
},
"N0847":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"MISSION_AUTONOMY","secondary_task":"",
 "task_evidence":"Develop and integrate a semantic scene graph world model to enable real-time spatial reasoning, context-aware mission planning, and natural language-driven robotic navigation.",
 "new":{
  "1":[["V2_WORLD_MODEL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0847:2",
  "4":R+"C++不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"任务自主。世界模型成立。Git版本工具成立。C++拒收C。"
},
"N0809":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"ROBOT_INTEGRATION","secondary_task":"",
 "task_evidence":"Bring up and integrate new robotic platforms into Field AI\u2019s software stack, including legged, wheeled-legged, wheeled, and humanoid systems",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":R+"project work不是Microsoft Project。",
  "3":R+"C++不是C语言。",
  "4":O+"Boston Dynamics Spot未单列冻结项。","5":O+"Unitree未单列冻结项。","6":O+"ANYbotics未单列冻结项。",
  "7":[["V2_CAN","PREFERRED","EXAMPLE"],["V2_ETHERCAT","PREFERRED","EXAMPLE"]],
  "8":"DUPLICATE:N0809:7","9":"DUPLICATE:N0809:7",
  "10":R+"UDP/TCP不是TCP/IP。",
  "11":[["V2_CALIBRATION","PREFERRED","UNCONDITIONAL"]],
  "12":[["V2_HIL","PREFERRED","CHOICE"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"本体集成。真CAN/EtherCAT成立。UDP不升TCP/IP。HIL不升仿真。"
},
"N0839":devops("N0839"),
"N0731":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"RESEARCH_DEVOPS","secondary_task":"",
 "task_evidence":"You will be the first dedicated infrastructure hire inside FAIRI. You will build the CI/CD, data pipelines, and IaC that let a small research team ship reliably",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":O+"ECR未单列冻结项。",
  "5":[["V2_GITHUB_ACTIONS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0731:5",
  "7":O+"REST未单列冻结项。",
  "8":[["V2_AIRFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0731:8",
  "10":[["V2_ROSBAG","DUTY_OWN_USE","UNCONDITIONAL"],["V2_MCAP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0731:10","12":"DUPLICATE:N0731:10","13":"DUPLICATE:N0731:10","14":"DUPLICATE:N0731:10",
  "15":[["V2_AWS","DUTY_OWN_USE","UNCONDITIONAL"],["V2_POSTGRESQL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "16":O+"MoCapDB未单列冻结项。","17":O+"ECS Fargate未单列冻结项。",
  "18":"DUPLICATE:N0731:15","19":"DUPLICATE:N0731:15",
  "20":O+"S3未单列冻结项。",
  "21":[["V2_AWS","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "22":"DUPLICATE:N0731:21",
  "23":O+"ECR未单列冻结项。","24":O+"S3未单列冻结项。","25":O+"IAM未单列冻结项。",
  "26":O+"VPC未单列冻结项。","27":O+"EKS未单列冻结项。","28":O+"SOC 2未单列冻结项。",
  "29":[["V2_HIL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "30":O+"VPN未单列冻结项。","31":O+"Tailscale未单列冻结项。",
  "32":R+"英语can不是CAN总线协议。",
  "33":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "34":[["V2_AWS","GENERAL","CHOICE"]],
  "35":"DUPLICATE:N0731:34",
  "36":O+"ECR未单列冻结项。","37":O+"S3未单列冻结项。","38":O+"IAM未单列冻结项。",
  "39":O+"VPC未单列冻结项。","40":O+"EKS未单列冻结项。","41":O+"Batch未单列冻结项。",
  "42":O+"ECS/Fargate未单列冻结项。",
  "43":[["V2_TERRAFORM","GENERAL","CHOICE"]],
  "44":"DUPLICATE:N0731:43",
  "45":O+"CDK未单列冻结项。","46":O+"Pulumi未单列冻结项。",
  "47":[["V2_CI_CD","GENERAL","CHOICE"],["V2_GITHUB_ACTIONS","GENERAL","EXAMPLE"]],
  "48":"DUPLICATE:N0731:47",
  "49":O+"BuildKit未单列冻结项。","50":O+"Buildah未单列冻结项。","51":O+"Kaniko未单列冻结项。",
  "52":[["V2_AIRFLOW","GENERAL","CHOICE"]],
  "53":"DUPLICATE:N0731:52",
  "54":[["V2_SHELL","GENERAL","CHOICE"]],
  "55":"DUPLICATE:N0731:54",
  "56":R+"英语can不是CAN总线协议。","57":R+"英语can不是CAN总线协议。",
  "58":[["V2_ROSBAG","PREFERRED","CHOICE"],["V2_MCAP","PREFERRED","CHOICE"],["V2_FOXGLOVE","PREFERRED","CHOICE"]],
  "59":"DUPLICATE:N0731:58",
  "60":[["V2_HIL","PREFERRED","UNCONDITIONAL"]],
  "61":O+"SOC 2未单列冻结项。",
  "62":R+"英语can不是CAN总线协议。","63":R+"英语can不是CAN总线协议。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FAIRI研发DevOps。GitHub Actions不升Git。C++阅读拒收C。HIL成立。AWS子服务与SOC2目录外。MoCapDB不记动作捕捉。"
},
"N0833":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"ROS_AUTONOMY","secondary_task":"",
 "task_evidence":"Develop and maintain ROS/ROS2 packages for robotic autonomy, including navigation, mapping, and control.",
 "new":{
  "1":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"C++不是C语言。",
  "3":R+"C++不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"ROS自主软件。传感器标定成立。C++拒收C。"
}
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
