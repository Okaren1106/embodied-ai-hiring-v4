"""First-pass adjudication for software coding_order 145-160. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
def outside(n, extra):
 d={str(i):O+"未单列冻结项。" for i in range(1,n+1)}
 d.update(extra)
 return d
decisions={
"N0813":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"IT_SECURITY_OPS","secondary_task":"",
 "task_evidence":"Own the full lifecycle of our macOS and Linux endpoint fleet through JumpCloud MDM",
 "new":outside(28,{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":O+"macOS未单列冻结项。",
  "3":O+"JumpCloud未单列冻结项。",
  "4":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":O+"CrowdStrike未单列冻结项。",
  "6":O+"SOC 2未单列冻结项。","7":O+"ISO 27001未单列冻结项。",
  "8":O+"systemd未单列冻结项。",
  "9":O+"macOS未单列冻结项。",
  "10":O+"JumpCloud未单列冻结项。",
  "11":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "12":O+"Sophos未单列冻结项。","13":O+"Ubiquiti未单列冻结项。","14":O+"Fortinet未单列冻结项。",
  "15":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"],["V2_AWS","GENERAL","UNCONDITIONAL"],["V2_JIRA","GENERAL","UNCONDITIONAL"]],
  "16":"DUPLICATE:N0813:15",
  "17":R+"GitHub产品管理不是Git协作。",
  "18":"DUPLICATE:N0813:15","19":"DUPLICATE:N0813:15",
  "20":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "21":O+"CrowdStrike未单列冻结项。",
  "22":O+"SOC 2未单列冻结项。","23":O+"ISO 27001未单列冻结项。",
  "24":[["V2_SHELL","PREFERRED","CHOICE"]],
  "25":"DUPLICATE:N0813:24",
  "26":O+"JumpCloud未单列冻结项。",
  "27":[["V2_INCIDENT_SUPPORT","PREFERRED","UNCONDITIONAL"]],
  "28":[["V2_PROCUREMENT","PREFERRED","UNCONDITIONAL"]]
 }),
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"IT安全运维。英语can与办公网络office拒收。GitHub管理不记Git。JumpCloud/CrowdStrike/SOC2/ISO/macOS目录外。"
},
"N0773":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"INFRA_SECURITY","secondary_task":"",
 "task_evidence":"Secure CI/CD systems, software supply chains, build pipelines, and deployment workflows",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0773:2",
  "4":O+"SRE未单列冻结项。",
  "5":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0773:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"基础设施安全。CI/CD保留。SRE目录外。"
},
"N0723":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"ARVR_HRI","secondary_task":"ROBOT_RUNTIME",
 "task_evidence":"Build interaction techniques for spatial input, visualization, teleoperation, task specification, and robot feedback.",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":O+"AR/VR未单列冻结项。",
  "3":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":R+"英语can不是CAN总线协议。",
  "5":R+"C#/C++不是C语言。",
  "6":[["V2_UNITY","GENERAL","UNCONDITIONAL"],["V2_UNREAL","GENERAL","UNCONDITIONAL"],["V2_GIT","GENERAL","UNCONDITIONAL"],["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0723:6","8":"DUPLICATE:N0723:6","9":"DUPLICATE:N0723:6",
  "10":O+"Meta Quest未单列冻结项。","11":O+"Apple未单列冻结项。","12":O+"Varjo未单列冻结项。",
  "13":[["V2_TELEOP","PREFERRED","CHOICE"]],
  "14":[["V2_UX_RESEARCH","PREFERRED","UNCONDITIONAL"]],
  "15":O+"haptics未单列冻结项。","16":O+"AR/VR未单列冻结项。","17":O+"ATAK未单列冻结项。",
  "18":R+"英语can不是CAN总线协议。","19":R+"英语can不是CAN总线协议。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"AR/VR交互。C++拒收C。git协作与CI保留。"
},
"N0845":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"WEB_PLATFORM","secondary_task":"",
 "task_evidence":"Develop backend services and APIs using Node.js (TypeScript) and Python where appropriate",
 "new":{
  "1":[["V2_NODEJS","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_TYPESCRIPT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0845:1","3":"DUPLICATE:N0845:1",
  "4":[["V2_REACT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0845:4",
  "6":[["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"],["V2_JAVASCRIPT","GENERAL","UNCONDITIONAL"],["V2_NODEJS","GENERAL","UNCONDITIONAL"],["V2_REACT","GENERAL","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0845:6","8":"DUPLICATE:N0845:6","9":"DUPLICATE:N0845:6","10":"DUPLICATE:N0845:6",
  "11":[["V2_MONGODB","GENERAL","CHOICE"],["V2_REDIS","GENERAL","CHOICE"]],
  "12":"DUPLICATE:N0845:11","13":"DUPLICATE:N0845:11",
  "14":[["V2_AWS","GENERAL","CHOICE"]],
  "15":"DUPLICATE:N0845:14",
  "16":R+"Nx前端单仓不是Siemens NX。",
  "17":O+"Lerna未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Web软件。Node.js句不单独记JavaScript。Nx拒收Siemens NX。"
},
"N0841":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"PRODUCT_WEB","secondary_task":"",
 "task_evidence":"Build scalable backend services using Node.js (Express) and Python",
 "new":{
  "1":[["V2_NODEJS","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":O+"Express未单列冻结项。",
  "3":"DUPLICATE:N0841:1",
  "4":[["V2_REACT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0841:4",
  "6":R+"Three.js不是JavaScript语言。",
  "7":O+"WebGL未单列冻结项。",
  "8":R+"Three.js不是JavaScript语言。",
  "9":[["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"],["V2_JAVASCRIPT","GENERAL","UNCONDITIONAL"],["V2_NODEJS","GENERAL","UNCONDITIONAL"],["V2_REACT","GENERAL","UNCONDITIONAL"]],
  "10":"DUPLICATE:N0841:9","11":"DUPLICATE:N0841:9","12":"DUPLICATE:N0841:9",
  "13":"DUPLICATE:N0841:9","14":"DUPLICATE:N0841:9",
  "15":[["V2_MONGODB","GENERAL","CHOICE"],["V2_REDIS","GENERAL","CHOICE"]],
  "16":"DUPLICATE:N0841:15","17":"DUPLICATE:N0841:15",
  "18":[["V2_AWS","GENERAL","UNCONDITIONAL"]],
  "19":"DUPLICATE:N0841:18",
  "20":O+"BIM未单列冻结项。",
  "21":R+"Three.js不是JavaScript语言。",
  "22":O+"WebGL未单列冻结项。",
  "23":R+"Nx前端单仓不是Siemens NX。",
  "24":O+"Lerna未单列冻结项。","25":O+"Revit未单列冻结项。","26":O+"APS未单列冻结项。","27":O+"Forge未单列冻结项。",
  "28":[["V2_AWS","PREFERRED","UNCONDITIONAL"]],
  "29":"DUPLICATE:N0841:28"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"产品Web。Three.js拒收JavaScript。Nx拒收Siemens NX。"
},
"N0730":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"DATA_PLATFORM","secondary_task":"",
 "task_evidence":"Manage everything as code: Terraform/IaC, GitOps workflows, and CI/CD for infrastructure and data services.",
 "new":{
  "1":[["V2_TERRAFORM","DUTY_OWN_USE","UNCONDITIONAL"],["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0730:1",
  "3":O+"GitOps未单列冻结项。",
  "4":"DUPLICATE:N0730:1",
  "5":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":R+"英语can不是CAN总线协议。",
  "7":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"]],
  "8":"DUPLICATE:N0730:7","9":"DUPLICATE:N0730:7",
  "10":[["V2_TERRAFORM","GENERAL","CHOICE"]],
  "11":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "12":[["V2_SPARK","PREFERRED","CHOICE"],["V2_DATABRICKS","PREFERRED","CHOICE"]],
  "13":"DUPLICATE:N0730:12","14":"DUPLICATE:N0730:12",
  "15":R+"办公地点office不是Microsoft Office。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据平台基础设施。GitOps不记Git。"
},
"N0782":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"REALTIME_NETWORK","secondary_task":"",
 "task_evidence":"Build low-latency, bidirectional audio/video streaming systems for telepresence and teleoperation",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":O+"QoS未单列冻结项。",
  "3":R+"TCP/UDP不是TCP/IP。",
  "4":"DUPLICATE:N0782:3",
  "5":R+"UDP不是TCP/IP。",
  "6":O+"RTP未单列冻结项。","7":O+"RTCP未单列冻结项。","8":O+"WebRTC未单列冻结项。",
  "9":O+"tcpdump未单列冻结项。","10":O+"iperf未单列冻结项。","11":O+"ss未单列冻结项。","12":O+"iw未单列冻结项。",
  "13":[["V2_TELEOP","PREFERRED","CHOICE"]],
  "14":O+"QoS未单列冻结项。","15":O+"WebRTC未单列冻结项。","16":O+"GStreamer未单列冻结项。","17":O+"RTP未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"实时网络。TCP/UDP不记TCP/IP。"
},
"E0563":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"STAFF_INFRA","secondary_task":"",
 "task_evidence":"Implement monitoring and alerting systems, and define incident response plans and runbooks.",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_AZURE","GENERAL","CHOICE"],["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"]],
  "4":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_ANSIBLE","GENERAL","CHOICE"]],
  "5":[["V2_PROMETHEUS","GENERAL","CHOICE"],["V2_GRAFANA","GENERAL","CHOICE"]],
  "6":[["V2_TCPIP","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "8":"DUPLICATE:E0563:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"基础设施。CloudFormation/Datadog未记。"
},
"E0549":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"APP_SECURITY","secondary_task":"",
 "task_evidence":"Conduct security assessments of applications, embedded systems, back-end services, and business integrations, as well as build tooling for a secure development lifecycle",
 "new":{
  "1":R+"办公地点office不是Microsoft Office。",
  "2":[["V2_C","GENERAL","UNRESOLVED"]]
 },
 "old_overrides":{
  "O20":{"metric":"UNKNOWN","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原application security短词定位为空，改为应用安全年限句；不记功能安全。","quote":"3+ years of experience in the field of application security or related security role"}
 },
 "additions":[],"outside_extra":[],
 "notes":"应用安全。C/C++按C未解。"
},
"E0484":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"ANDROID_APP","secondary_task":"",
 "task_evidence":"Own the Android app end to end, from architecture to Google Play release.",
 "new":{
  "1":R+"办公地点office不是Microsoft Office。",
  "2":[["V2_REACT","PREFERRED","CHOICE"]],
  "3":O+"Kotlin未单列冻结项。","4":O+"Jetpack Compose未单列冻结项。","5":O+"CameraX未单列冻结项。",
  "6":"DUPLICATE:E0484:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Android应用。React Native按React任选。"
},
"E0551":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"VULN_AUTOMATION","secondary_task":"",
 "task_evidence":"Identify, triage, and remediate vulnerabilities and misconfigurations for cloud infrastructure",
 "new":{
  "1":R+"办公地点office不是Microsoft Office。",
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_AZURE","GENERAL","CHOICE"],["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"]],
  "4":[["V2_C","GENERAL","UNRESOLVED"]]
 },
 "old_overrides":{
  "O11":{"metric":"UNKNOWN","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原SaaS Security短词定位为空，改为企业安全域句。","quote":"Experience in several of the following Enterprise Security Domains: Zero Trust/Beyond Corp, Endpoint Security, Cloud Security, Data Loss Prevention, Cryptography and PKI, SaaS Security."},
  "O16":{"metric":"UNKNOWN","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原SaaS Security短词定位为空，改为操作系统安全句。","quote":"OS Hardening (macOS, Windows, Linux, ChromeOS), SaaS Security or Assurance and Validation"},
  "O23":{"metric":"UNKNOWN","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原Enterprise短词定位为空，改为企业安全年限句。","quote":"6+ years of experience as an Enterprise/Cloud focused Security Engineer"}
 },
 "additions":[],"outside_extra":[],
 "notes":"漏洞管理自动化。C/C++按C未解。macOS目录外。"
},
"E0560":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"PRIVACY_GOVERNANCE","secondary_task":"",
 "task_evidence":"Design and implement new technical features that embed privacy controls and data minimization techniques into our product and tech stack (privacy-by-design)",
 "new":{
  "1":R+"办公地点office不是Microsoft Office。",
  "2":[["V2_C","GENERAL","UNRESOLVED"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"隐私与数据治理。C/C++按C未解。"
},
"E0561":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"HEAD_DISPLAY_GRAPHICS","secondary_task":"",
 "task_evidence":"Design, implement, and optimize the graphics rendering stack for robot head displays, from low-level GPU pipeline to high-level UI components.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":[["V2_UNREAL","PREFERRED","CHOICE"],["V2_UNITY","PREFERRED","CHOICE"]],
  "3":R+"Vulkan/OpenGL ES不是Unity/Unreal。"
 },
 "old_overrides":{
  "O9":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原embedded短词定位为空，改为嵌入式或资源约束系统句。","quote":"Proven track record developing on embedded or resource-constrained systems (limited RAM, GPU, thermal envelope)."}
 },
 "additions":[],"outside_extra":[],
 "notes":"头显图形。C++拒收C。"
},
"E0559":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"BUSINESS_APP","fine_task":"MFG_SOFTWARE","secondary_task":"",
 "task_evidence":"Implement improvements to our existing suite of manufacturing software.",
 "new":{
  "1":R+"办公地点office不是Microsoft Office。",
  "2":[["V2_MES","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_PLM","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_POSTGRESQL","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_GIT","GENERAL","UNCONDITIONAL"],["V2_PYTEST","GENERAL","EXAMPLE"],["V2_PLAYWRIGHT","GENERAL","EXAMPLE"]],
  "6":[["V2_AZURE","PREFERRED","UNCONDITIONAL"]],
  "7":[["V2_BAZEL","PREFERRED","CHOICE"],["V2_TERRAFORM","PREFERRED","CHOICE"]],
  "8":"DUPLICATE:E0559:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"制造软件。Vitest未单列。WMS走继承项。"
},
"E0496":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"XR_INTERFACE","secondary_task":"",
 "task_evidence":"Build and maintain XR products to interface with our robots and data-capture hardware - implementing features, fixing bugs, and ensuring reliability as we scale",
 "new":{
  "1":R+"办公地点office不是Microsoft Office。",
  "2":[["V2_UNITY","GENERAL","CHOICE"],["V2_UNREAL","GENERAL","CHOICE"]],
  "3":R+"C++不是C语言。",
  "4":"DUPLICATE:E0496:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"XR产品。C++拒收C。OpenXR/Godot/WebXR未单列。"
},
"E0509":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"IT_OPS","secondary_task":"",
 "task_evidence":"Administrar contas, grupos e acessos do Google Workspace em coordenação com o time de TI da matriz (HQ).",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_GOOGLE_WORKSPACE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "4":R+"本句是Apple MDM，不是Google Workspace。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"IT运维（圣保罗）。Jamf/macOS目录外。"
},
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
