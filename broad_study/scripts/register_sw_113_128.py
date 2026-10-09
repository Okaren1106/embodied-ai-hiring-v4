"""First-pass adjudication for software coding_order 113-128. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
RT={
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"REALTIME_CONTROLS","secondary_task":"",
 "task_evidence":"Deliver production-grade real-time C++ software infrastructure",
 "new":{
  "1":R+"C++不是C语言。",
  "2":[["V2_HIL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"现代C++不是C语言。",
  "5":[["V2_SYSID","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_CMAKE","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_EIGEN","GENERAL","CHOICE"]],
  "8":[["V2_HIL","GENERAL","CHOICE"]],
  "9":[["V2_GIT","GENERAL","EXAMPLE"]],
  "10":[["V2_PROJECT_METHOD","GENERAL","UNCONDITIONAL"]],
  "11":"DUPLICATE:E0423:6",
  "12":"DUPLICATE:E0423:7",
  "13":O+"Flatbuffers/BehaviorTree.CPP未单列冻结项。",
  "14":"DUPLICATE:E0423:9"
 },
 "old_overrides":{
  "O4":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS2短词定位为空，改为CMake+colcon句。","quote":"Comfortable in CMake + colcon ROS2 workspaces"},
  "O7":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS2短词定位为空，改为任选工具句。","quote":"Familiarity with at least some of: MuJoCo, Drake, Eigen, ROS2, Flatbuffers, BehaviorTree.CPP"}
 },
 "additions":[],"outside_extra":[],
 "notes":"实时运控。C++拒收C。HIL与仿真任选。"
}
RT24=dict(RT);RT24['new']=dict(RT['new'])
RT24['new']['11']='DUPLICATE:E0424:6'
RT24['new']['12']='DUPLICATE:E0424:7'
RT24['new']['14']='DUPLICATE:E0424:9'
RT24['old_overrides']=dict(RT['old_overrides'])
decisions={
"E0365":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"HARDWARE_INTERFACE","secondary_task":"",
 "task_evidence":"Own the design, development, and evolution of C++ software components that power our robots, interfacing with OS drivers and hardware to enable high-bandwidth, low-latency control",
 "new":{
  "1":R+"C++不是C语言。","2":R+"C++不是C语言。","3":R+"现代C++不是C语言。",
  "4":[["V2_HIL","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_ETHERCAT","PREFERRED","EXAMPLE"],["V2_CAN","PREFERRED","EXAMPLE"],["V2_PROFINET","PREFERRED","EXAMPLE"]],
  "6":R+"C++不是C语言。",
  "7":[["V2_GIT","GENERAL","EXAMPLE"],["V2_JIRA","GENERAL","EXAMPLE"],["V2_CI_CD","GENERAL","EXAMPLE"],["V2_PROJECT_METHOD","GENERAL","UNCONDITIONAL"]],
  "8":R+"办公地点office不是Microsoft Office。",
  "9":R+"薪资USD不是Universal Scene Description。",
  "10":R+"猎头免责声明不是人力资源专业职责。"
 },
 "old_overrides":{
  "O2":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原C++短词定位为空，改为modern C++句。","quote":"Strong expertise writing modern C++ (17, 20) for complex, performance-sensitive systems"},
  "O3":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为Linux编程句。","quote":"Proficient in using and programming for recent Linux systems"},
  "O4":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原C++短词定位为空，改为modern C++句。","quote":"Strong expertise writing modern C++ (17, 20) for complex, performance-sensitive systems"},
  "O8":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为Linux编程句。","quote":"Proficient in using and programming for recent Linux systems"}
 },
 "additions":[],"outside_extra":[],
 "notes":"硬件接口软件。C++拒收C。"
},
"E0339":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"SAFETY_SOFTWARE","secondary_task":"",
 "task_evidence":"Design & Develop:",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":R+"C++不是C语言。",
  "3":[["V2_SAFETY_STANDARDS","GENERAL","EXAMPLE"]],
  "4":[["V2_SAFETY_STANDARDS","GENERAL","EXAMPLE"]],
  "5":[["V2_QNX","GENERAL","CHOICE"]],
  "6":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "7":R+"薪资USD不是Universal Scene Description。",
  "8":R+"猎头免责声明不是人力资源专业职责。",
  "9":"DUPLICATE:E0339:5"
 },
 "old_overrides":{
  "O4":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS2短词定位为空，改为ROS 2应用句。","quote":"Experience architecting and building complex robotic applications using ROS 2."},
  "O15":{"metric":"REQUIRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原embedded短词定位为空，改为系统/嵌入式编程句。","quote":"of professional software engineering experience, with a focus on systems level or embedded systems programming (C++, C, or Rust)."}
 },
 "additions":[],"outside_extra":[],
 "notes":"安全软件。IEC/ISO记安全标准。C++拒收C。"
},
"E0418":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"CUSTOMER_SITE_SRE","secondary_task":"CUSTOMER_INTEGRATION",
 "task_evidence":"We are seeking an experienced Site Reliability Engineer to own and maintain the deployment of our cloud-based infrastructure to customer sites.",
 "new":{
  "1":[["V2_TERRAFORM","DUTY_OWN_DEVELOP","CHOICE"],["V2_ANSIBLE","DUTY_OWN_DEVELOP","CHOICE"]],
  "2":[["V2_TYPESCRIPT","DUTY_OWN_DEVELOP","CHOICE"]],
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_ANSIBLE","GENERAL","CHOICE"]],
  "5":[["V2_TYPESCRIPT","GENERAL","CHOICE"]],
  "6":[["V2_GRAFANA","GENERAL","UNCONDITIONAL"]],
  "7":"DUPLICATE:E0418:1",
  "8":"DUPLICATE:E0418:2",
  "9":"DUPLICATE:E0418:6",
  "10":O+"PagerDuty未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"客户现场云SRE。C++出现在任职要求时未进入保留C语言。Helm目录外。"
},
"E0416":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"SECURITY_ENGINEERING","secondary_task":"",
 "task_evidence":"Apptronik is seeking an experienced Senior Security Engineer to define and implement the security posture for our humanoid robotic deployments.",
 "new":{
  "1":[["V2_TERRAFORM","DUTY_OWN_USE","CHOICE"],["V2_ANSIBLE","DUTY_OWN_USE","CHOICE"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_ANSIBLE","GENERAL","CHOICE"]],
  "4":"DUPLICATE:E0416:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"部署安全工程。IaC任选。"
},
"E0387":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"PLATFORM_SOFTWARE","secondary_task":"",
 "task_evidence":"You will join a team developing state-of-the-art general-purpose robots designed to operate in human spaces and with human tools.",
 "new":{
  "1":R+"代码评审与文档不是CI/CD流水线。",
  "2":R+"C++不是C语言。",
  "3":R+"C++不是C语言。",
  "4":[["V2_CAN","GENERAL","EXAMPLE"],["V2_ETHERCAT","GENERAL","EXAMPLE"]],
  "5":"DUPLICATE:E0387:4"
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原C++短词定位为空，改为Linux环境C++句。","quote":"Proficiency in C++ within a Linux environment, with experience in system-level programming and an understanding of performance-sensitive code."}
 },
 "additions":[],"outside_extra":[],
 "notes":"平台软件。C++拒收C。"
},
"E0447":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"FLEET_CONNECT","secondary_task":"ROBOT_CLOUD_UI",
 "task_evidence":"Apptronik is seeking a full-stack Technical Lead Manager to lead the technical direction and delivery of the Interface team within Fleet Connect.",
 "new":{
  "1":[["V2_PLC","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_REACT","GENERAL","CHOICE"]],
  "4":[["V2_ETHERNET","GENERAL","CHOICE"],["V2_TCPIP","GENERAL","CHOICE"],["V2_PROFINET","GENERAL","CHOICE"],["V2_MODBUS","GENERAL","CHOICE"],["V2_PLC","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_KAFKA","PREFERRED","CHOICE"]],
  "6":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "7":"DUPLICATE:E0447:2",
  "8":"DUPLICATE:E0447:3",
  "9":"DUPLICATE:E0447:4",
  "10":"DUPLICATE:E0447:6"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"客户车队接口。C++加分未记C。OPC UA/MQTT目录外。"
},
"E0385":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"REALTIME_CONTROLS_INTERN","secondary_task":"",
 "task_evidence":"Support the development and testing of real-time C++ software modules that drive robot motion.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":[["V2_PROJECT_METHOD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"C++不是C语言。",
  "4":R+"现代C++不是C语言。",
  "5":R+"线性代数不是Linear项目管理工具。",
  "6":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "7":"DUPLICATE:E0385:6"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"运控实习。C++拒收C。"
},
"E0423":RT,
"E0424":RT24,
"E0373":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"ECAD_LIBRARY","secondary_task":"",
 "task_evidence":"We're looking for a detail-oriented ECAD Librarian to own and grow our Altium component library, ensuring every schematic symbol, PCB footprint, and 3D model is accurate, standardized, and manufacturable.",
 "new":{
  "1":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_DFM","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"],["V2_IPC_STANDARDS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_PLM","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":[["V2_ALLEGRO","PREFERRED","CHOICE"]],
  "7":[["V2_DFM","GENERAL","UNCONDITIONAL"],["V2_IPC_STANDARDS","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_PLM","GENERAL","CHOICE"]],
  "9":O+"Mentor/Xpedition未单列冻结项。",
  "10":O+"Arena未单列冻结项。",
  "11":O+"Perl未单列冻结项。"
 },
 "old_overrides":{
  "O8":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原PCB design短词定位为空，改为ECAD/PCB经验句。","quote":"2–5+ years of experience in ECAD library management, component engineering, or PCB design."}
 },
 "additions":[{"code":"SK_ALTIUM","metric":"GENERAL","branch":"UNCONDITIONAL","quote":"Hands-on expertise with Altium Designer; familiarity with other ECAD tools (Cadence Allegro, Mentor/Xpedition) a plus.","reason":"Altium为硬性工具，Allegro为加分任选。"}],
 "outside_extra":[],
 "notes":"ECAD库。Altium记SK_ALTIUM。JEDEC目录外。"
},
"N1042":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"AGENTIC_SYSTEMS","secondary_task":"ROBOT_RUNTIME",
 "task_evidence":"Stay at the forefront of agentic research and translate state-of-the-art techniques into production systems.",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":"DUPLICATE:N1042:2",
  "4":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":[["V2_AGENT_WORKFLOW","GENERAL","UNCONDITIONAL"]],
  "6":"DUPLICATE:N1042:5",
  "7":[["V2_AGENT_WORKFLOW","GENERAL","EXAMPLE"]],
  "8":[["V2_AGENT_WORKFLOW","GENERAL","UNCONDITIONAL"]],
  "9":[["V2_TYPESCRIPT","GENERAL","CHOICE"]],
  "10":"DUPLICATE:N1042:9"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Atlas智能体架构。C++拒收C，保留TypeScript任选。"
},
"N1019":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"FLEET_FULLSTACK","secondary_task":"",
 "task_evidence":"improving and maintaining our custom robot fleet management software.",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":[["V2_TYPESCRIPT","GENERAL","CHOICE"],["V2_JAVASCRIPT","GENERAL","CHOICE"],["V2_REACT","GENERAL","CHOICE"],["V2_NODEJS","GENERAL","CHOICE"],["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"]],
  "3":"DUPLICATE:N1019:2",
  "4":"DUPLICATE:N1019:2",
  "5":"DUPLICATE:N1019:2",
  "6":R+"Three.js不是JavaScript语言项的充分证据。",
  "7":"DUPLICATE:N1019:2",
  "8":"DUPLICATE:N1019:2",
  "9":O+"protobuf未单列冻结项。",
  "10":O+"Android未单列冻结项。",
  "11":R+"hobbyist project work不是Microsoft Project。",
  "12":O+"IoT未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"车队全栈。C++拒收C。Three.js拒收JS。"
},
"N1025":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"TELEOP_RESEARCH","secondary_task":"",
 "task_evidence":"Implement and evaluate novel teleoperation interfaces",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_MOCAP","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "4":O+"VR未单列冻结项。",
  "5":"DUPLICATE:N1025:3",
  "6":O+"可穿戴设备未单列冻结项。",
  "7":O+"混合现实未单列冻结项。",
  "8":R+"C++不是C语言。",
  "9":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "10":R+"C++不是C语言。",
  "11":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]],
  "12":O+"VR未单列冻结项。",
  "13":O+"AR未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"遥操研究。C++拒收C。"
},
"N1036":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"DEVOPS","secondary_task":"",
 "task_evidence":"Scale CI/CD and platform services.",
 "new":{
  "1":[["V2_GCP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_GCP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":[["V2_TERRAFORM","DUTY_OWN_DEVELOP","CHOICE"],["V2_ANSIBLE","DUTY_OWN_DEVELOP","CHOICE"]],
  "6":"DUPLICATE:N1036:5",
  "7":"DUPLICATE:N1036:5",
  "8":O+"Packer未单列冻结项。",
  "9":O+"metal-kubed未单列冻结项。",
  "10":O+"MAAS未单列冻结项。",
  "11":O+"Digital Rebar未单列冻结项。",
  "12":O+"GKE未单列冻结项。",
  "13":O+"EKS未单列冻结项。",
  "14":[["V2_GCP","GENERAL","CHOICE"],["V2_AWS","GENERAL","CHOICE"]],
  "15":"DUPLICATE:N1036:14",
  "16":"DUPLICATE:N1036:14",
  "17":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_ANSIBLE","GENERAL","CHOICE"]],
  "18":"DUPLICATE:N1036:17",
  "19":"DUPLICATE:N1036:17",
  "20":O+"Packer未单列冻结项。",
  "21":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "22":[["V2_CI_CD","GENERAL","EXAMPLE"],["V2_GITLAB_CI","GENERAL","EXAMPLE"]],
  "23":O+"BuildKite未单列冻结项。",
  "24":[["V2_GITLAB_CI","GENERAL","EXAMPLE"]],
  "25":O+"Artifactory未单列冻结项。",
  "26":O+"Nexus未单列冻结项。",
  "27":[["V2_SHELL","GENERAL","CHOICE"]],
  "28":"DUPLICATE:N1036:27",
  "29":R+"high-throughput遥测不是硬件在环。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"DevOps。GitLab CI不升Git。C++拒收C。Packer等目录外。"
},
"N1031":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"BUSINESS_APP","fine_task":"ATLASSIAN_ADMIN","secondary_task":"DEV_INFRA",
 "task_evidence":"As an Application Developer, you will support the design, development, implementation and testing of our Atlassian applications",
 "new":{
  "1":R+"project management不是Microsoft Project。",
  "2":[["V2_JIRA","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CONFLUENCE","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_JIRA","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":"DUPLICATE:N1031:3",
  "5":"DUPLICATE:N1031:3",
  "6":O+"Assets未单列冻结项。",
  "7":[["V2_CONFLUENCE","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "8":R+"英语can不是CAN总线协议。",
  "9":[["V2_LEAN","DUTY_OWN_USE","UNCONDITIONAL"]],
  "10":"DUPLICATE:N1031:9",
  "11":"DUPLICATE:N1031:9",
  "12":[["V2_JIRA","GENERAL","UNCONDITIONAL"],["V2_CONFLUENCE","GENERAL","UNCONDITIONAL"]],
  "13":"DUPLICATE:N1031:12",
  "14":"DUPLICATE:N1031:12",
  "15":"DUPLICATE:N1031:12",
  "16":O+"Assets未单列冻结项。",
  "17":"DUPLICATE:N1031:12",
  "18":R+"协作能力句没有Jira工具证据。",
  "19":[["V2_JIRA","GENERAL","UNCONDITIONAL"]],
  "20":O+"API integrations未单列冻结项。",
  "21":R+"can do态度不是CAN总线协议。",
  "22":[["V2_JIRA","PREFERRED","EXAMPLE"]],
  "23":O+"Atlassian Certified Professional未单列冻结项。",
  "24":"DUPLICATE:N1031:22",
  "25":[["V2_PROJECT_METHOD","GENERAL","CHOICE"],["V2_JIRA","GENERAL","UNCONDITIONAL"]],
  "26":"DUPLICATE:N1031:25",
  "27":"DUPLICATE:N1031:25",
  "28":"DUPLICATE:N1031:25",
  "29":O+"ITIL未单列冻结项。",
  "30":[["V2_JIRA","GENERAL","UNCONDITIONAL"]],
  "31":"DUPLICATE:N1031:30",
  "32":O+"Atlassian Plans未单列冻结项。",
  "33":O+"Groovy未单列冻结项。",
  "34":O+"JQL未单列冻结项。",
  "35":O+"AQL未单列冻结项。",
  "36":O+"Atlassian Forge未单列冻结项。",
  "37":R+"招聘隐私声明不是人力资源专业职责。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Atlassian业务系统。精益六西格玛按原文保留。can do拒收CAN。"
},
"N0882":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"INFRA_SRE","secondary_task":"",
 "task_evidence":"Build and maintain Infrastructure-as-Code using technologies such as Terraform, Salt, Python, and Git-based workflows.",
 "new":{
  "1":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "2":R+"英语叙述不是CAN总线协议。",
  "3":[["V2_TERRAFORM","DUTY_OWN_DEVELOP","EXAMPLE"],["V2_GIT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":"DUPLICATE:N0882:3",
  "5":O+"Salt未单列冻结项。",
  "6":"DUPLICATE:N0882:3",
  "7":O+"Ubuntu未单列冻结项。",
  "8":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "9":O+"Ubuntu未单列冻结项。",
  "10":[["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0882:10",
  "12":[["V2_TERRAFORM","GENERAL","CHOICE"]],
  "13":"DUPLICATE:N0882:12",
  "14":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"]],
  "15":"DUPLICATE:N0882:14",
  "16":"DUPLICATE:N0882:14",
  "17":"DUPLICATE:N0882:14",
  "18":O+"VLAN未单列冻结项。",
  "19":O+"DHCP未单列冻结项。",
  "20":O+"DNS未单列冻结项。",
  "21":[["V2_GIT","GENERAL","UNCONDITIONAL"],["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "22":"DUPLICATE:N0882:21",
  "23":"DUPLICATE:N0882:21",
  "24":O+"REST API未单列冻结项。",
  "25":O+"PXE boot未单列冻结项。",
  "26":O+"DHCP未单列冻结项。",
  "27":O+"TFTP未单列冻结项。",
  "28":O+"cloud-init未单列冻结项。",
  "29":O+"IPMI未单列冻结项。",
  "30":O+"Redfish未单列冻结项。",
  "31":O+"iDRAC未单列冻结项。",
  "32":O+"iLO未单列冻结项。",
  "33":O+"Salt未单列冻结项。",
  "34":[["V2_PROMETHEUS","PREFERRED","EXAMPLE"],["V2_GRAFANA","PREFERRED","EXAMPLE"]],
  "35":"DUPLICATE:N0882:34",
  "36":"DUPLICATE:N0882:34",
  "37":O+"ISO 27001未单列冻结项。",
  "38":O+"SOC 2未单列冻结项。",
  "39":R+"薪资USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"基础设施。公司World Model作背景提及。Git工作流记Git。"
}
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
