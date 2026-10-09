"""First-pass adjudication for software coding_order 161-176. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"E0508":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"SITE_IT_OPS","secondary_task":"",
 "task_evidence":"Como IT Coordinator (Coordinador/a de TI), eres el responsable de la TI de nuestra unidad de São Paulo: soporte al usuario, flota de dispositivos y red de la oficina, todo construido desde cero y operado con autonomía, en coordinación con el equipo de TI de Figure en EE. UU.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_GOOGLE_WORKSPACE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "4":R+"macOS/MDM句不是Google Workspace。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"驻场IT。Google Workspace主责成立；MDM句拒收Workspace。"
},
"N0918":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"ROBOT_BEHAVIORS","secondary_task":"",
 "task_evidence":"Lead design and implementation of robot behaviors and task-level intelligence across the full robotics stack, integrating perception, planning and control into reliable end-to-end execution.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"C++不是C语言。",
  "3":O+"RTOS未单列冻结项。",
  "4":R+"办公地点in-office不是Microsoft Office。",
  "5":R+"Series C融资轮次不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"生产机器人行为软件。C++拒收C。融资轮次与驻场办公拒收。"
},
"N0922":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"ROBOTICS_PLATFORM","secondary_task":"DEV_INFRA",
 "task_evidence":"You will design and ship reliable services, APIs, and operational tooling.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"C++不是C语言。",
  "3":O+"OpenTelemetry未单列冻结项。",
  "4":[["V2_AWS","PREFERRED","UNCONDITIONAL"],["V2_CI_CD","PREFERRED","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0922:4","6":"DUPLICATE:N0922:4",
  "7":R+"Series C融资轮次不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人平台后端。C++拒收C。AWS/CI/CD为加分项。"
},
"N0927":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"MULTI_ROBOT_COORD","secondary_task":"CUSTOMER_INTEGRATION",
 "task_evidence":"Design and develop well-architected production-level software systems for robot coordination, multi-robot simulations, system state management, and operational workflows",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"C++不是C语言。",
  "4":[["V2_AWS","GENERAL","UNCONDITIONAL"],["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0927:4","6":"DUPLICATE:N0927:4",
  "7":R+"Series C融资轮次不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"多机协调与仓内集成。C++拒收C。WMS已在继承项。"
},
"N0925":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"BUSINESS_APP","fine_task":"CLOUD_LOGISTICS","secondary_task":"CUSTOMER_INTEGRATION",
 "task_evidence":"Nimble’s Cloud Logistics software team builds the in-house suite of cloud-native solutions that drive Nimble’s operations and customer integrations.",
 "new":{
  "1":R+"Series C融资轮次不是C语言。",
  "2":O+"TMS/OMS/WMS/IMS/RMS未单列冻结项。",
  "3":"DUPLICATE:N0925:2","4":"DUPLICATE:N0925:2","5":"DUPLICATE:N0925:2",
  "6":R+"play a critical role/lean team不是精益六西格玛。",
  "7":[["V2_AWS","GENERAL","UNCONDITIONAL"],["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "8":O+"REST未单列冻结项。",
  "9":"DUPLICATE:N0925:7","10":"DUPLICATE:N0925:7",
  "11":[["V2_TERRAFORM","PREFERRED","UNCONDITIONAL"]],
  "12":"DUPLICATE:N0925:11",
  "13":[["V2_GITLAB_CI","PREFERRED","UNCONDITIONAL"]],
  "14":"DUPLICATE:N0925:13",
  "15":O+"GraphQL未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"云履单业务系统。Gitlab CI仅记CI，Git未明示。WMS已在继承项。"
},
"N0921":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"SRE_SECURITY","secondary_task":"",
 "task_evidence":"Own and drive the infrastructure roadmap for secure, reliable, and scalable software services, robotics products, embedded systems, cloud infrastructure, and corporate systems.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_TYPESCRIPT","GENERAL","CHOICE"]],
  "4":"DUPLICATE:N0921:3",
  "5":O+"IAM未单列冻结项。",
  "6":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "7":O+"RBAC未单列冻结项。","8":O+"ACL未单列冻结项。",
  "9":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_AWS","GENERAL","CHOICE"]],
  "10":"DUPLICATE:N0921:9","11":"DUPLICATE:N0921:9",
  "12":O+"Pulumi未单列冻结项。","13":O+"CloudFormation未单列冻结项。",
  "14":[["V2_AWS","PREFERRED","CHOICE"],["V2_GCP","PREFERRED","CHOICE"],["V2_AZURE","PREFERRED","CHOICE"]],
  "15":"DUPLICATE:N0921:14","16":"DUPLICATE:N0921:14","17":"DUPLICATE:N0921:14",
  "18":O+"CSPM未单列冻结项。","19":O+"CWPP未单列冻结项。",
  "20":[["V2_PROMETHEUS","PREFERRED","CHOICE"],["V2_GRAFANA","PREFERRED","CHOICE"]],
  "21":O+"OpenTelemetry未单列冻结项。",
  "22":"DUPLICATE:N0921:20",
  "23":O+"VictoriaMetrics未单列冻结项。",
  "24":"DUPLICATE:N0921:20",
  "25":O+"Datadog未单列冻结项。",
  "26":O+"ISO 27001未单列冻结项。","27":O+"SOC 2未单列冻结项。",
  "28":R+"Series C融资轮次不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"基础设施SRE。C++拒收C。TypeScript任选。IaC任选。"
},
"N0913":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"NIMBLE_BRAIN_RUNTIME","secondary_task":"",
 "task_evidence":"This is a rare opportunity to help define the software foundation of industry-leading intelligent robots and contribute to the long-term vision of generalized robotic autonomy at scale.",
 "new":{"1":R+"Series C融资轮次不是C语言。"},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"端侧运行软件。仅融资轮次假阳性。"
},
"E0599":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"TELEOP_INTERFACES","secondary_task":"",
 "task_evidence":"- Design remote teleoperation interfaces: Develop comfortable and precise interfaces for controlling robots with many degrees of freedom",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":R+"C++不是C语言。",
  "6":[["V2_PERF","GENERAL","EXAMPLE"]],
  "7":[["V2_TELEOP","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_TELEOP","PREFERRED","CHOICE"]],
  "9":O+"WebRTC未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"部署遥操界面。英语can拒收CAN。C++拒收C。network analyzers不记网络分析仪。"
},
"E0605":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"MFG_SOFTWARE_PLATFORM","secondary_task":"",
 "task_evidence":"- Own the architecture and development of PI’s manufacturing software platform.",
 "new":{
  "1":[["V2_CALIBRATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CALIBRATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_CALIBRATION","GENERAL","CHOICE"]],
  "4":[["V2_MES","GENERAL","CHOICE"]],
  "5":R+"项目管理技能不是Microsoft Project。",
  "6":[["V2_BAZEL","PREFERRED","CHOICE"],["V2_CALIBRATION","PREFERRED","CHOICE"]]
 },
 "old_overrides":{
  "O11":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原hardware test短词定位为空，改为年限经验任选句。","quote":"5+ years of software engineering experience, preferably involving manufacturing, robotics, hardware test, embedded systems, or fleet operations."}
 },
 "additions":[],"outside_extra":[],
 "notes":"制造软件平台。英语can拒收CAN。MES/ERP任选。OTA无独立项。"
},
"E0581":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"REALTIME_PIPELINES","secondary_task":"",
 "task_evidence":"-Own Real-Time Pipelines: Engineer low-latency, high-reliability sensor and actuator pipelines across Linux, drivers, and middleware.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":[["V2_PERF","GENERAL","EXAMPLE"]],
  "3":"DUPLICATE:E0581:2"
 },
 "old_overrides":{
  "O20":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原real-time短词定位为空，改为实时/近实时背景句。","quote":"Background in real-time or near–real-time systems, VR/AR, video pipelines, 3D engines, or streaming systems where latency budgets are strict."}
 },
 "additions":[],"outside_extra":[],
 "notes":"实时管线。C++拒收C。perf成立。network analyzers不记网络分析仪。"
},
"E0585":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"BUILD_RELEASE","secondary_task":"",
 "task_evidence":"- CI/CD Ownership: Design and operate GitHub-based CI/CD systems (GitHub Actions, checks, workflows) with a focus on reliability, speed, and signal quality.",
 "new":{
  "1":[["V2_GIT","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_BAZEL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_GIT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_GIT","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_GITHUB_ACTIONS","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":[["V2_TYPESCRIPT","DUTY_OWN_DEVELOP","EXAMPLE"],["V2_BAZEL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":[["V2_TERRAFORM","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":[["V2_GIT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "7":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "9":[["V2_BAZEL","GENERAL","EXAMPLE"]],
  "10":[["V2_TERRAFORM","GENERAL","UNCONDITIONAL"]],
  "11":[["V2_BAZEL","PREFERRED","UNCONDITIONAL"]],
  "12":"DUPLICATE:E0585:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"构建发布。GitHub工作流记Git。C++拒收C。Actions短词并入职责句。"
},
"N0930":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"ROBOT_BACKEND_ARCH","secondary_task":"",
 "task_evidence":"We're looking for a Backend Software Engineer to join our Software Architecture team and build the scalable systems that support robotic workflows.",
 "new":{
  "1":R+"Python and/or C++不是C语言。",
  "2":R+"C++不是C语言。",
  "3":R+"英语can不是CAN总线协议。",
  "4":[["V2_DDS","PREFERRED","EXAMPLE"],["V2_ZENOH","PREFERRED","EXAMPLE"]],
  "5":"DUPLICATE:N0930:4","6":"DUPLICATE:N0930:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人后端架构。C++拒收C。中间件示例成立。"
},
"N0665":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"EMBEDDED_SECURITY","secondary_task":"",
 "task_evidence":"We are seeking a proficient Embedded Security Engineer to join our team and contribute to the protection of our models deployed on robotic hardware.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":O+"PHP未单列冻结项。",
  "3":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"嵌入式安全。C++拒收C。薪酬USD拒收。"
},
"N0706":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"DEPLOY_BACKEND","secondary_task":"",
 "task_evidence":"You will design, implement, and maintain software systems for deployment in real-world robotic products.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"部署后端基础设施。C++拒收C。"
},
"N0692":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"MANIPULATION_SW","secondary_task":"",
 "task_evidence":"Write controllers and perception stacks for real-world robotic deployment.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"操作软件。C++拒收C。"
},
"N0667":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"FULLSTACK_ROBOT_WEB","secondary_task":"",
 "task_evidence":"We are seeking a Full Stack Developer to help build and maintain our cloud infrastructure and web applications.",
 "new":{
  "1":[["V2_NODEJS","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0667:1",
  "3":O+"WebSockets未单列冻结项。",
  "4":O+"WebRTC未单列冻结项。",
  "5":O+"WebXR未单列冻结项。",
  "6":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0667:6",
  "8":[["V2_JAVASCRIPT","GENERAL","UNCONDITIONAL"],["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0667:8","10":"DUPLICATE:N0667:8",
  "11":[["V2_REACT","GENERAL","UNCONDITIONAL"]],
  "12":"DUPLICATE:N0667:11",
  "13":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "14":"DUPLICATE:N0667:13",
  "15":O+"MERN未单列冻结项。",
  "16":O+"WebRTC未单列冻结项。",
  "17":O+"Socket.IO未单列冻结项。",
  "18":[["V2_MONGODB","PREFERRED","EXAMPLE"]],
  "19":O+"NoSQL未单列冻结项。",
  "20":"DUPLICATE:N0667:18",
  "21":O+"WebXR未单列冻结项。",
  "22":[["V2_REACT","PREFERRED","CHOICE"]],
  "23":"DUPLICATE:N0667:22",
  "24":R+"Three.js不是JavaScript语言项的充分证据。",
  "25":[["V2_AWS","PREFERRED","UNCONDITIONAL"]],
  "26":"DUPLICATE:N0667:25"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人控制全栈。Three.js拒收JS。React Three Fiber按React任选。"
}
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
