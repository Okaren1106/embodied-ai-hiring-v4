"""First-pass adjudication for software coding_order 161-181. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
def outside(n, extra):
 d={str(i):O+"未单列冻结项。" for i in range(1,n+1)}
 d.update(extra)
 return d
decisions={
"E0508":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"IT_OPS","secondary_task":"",
 "task_evidence":"Administrar cuentas, grupos y accesos de Google Workspace",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_GOOGLE_WORKSPACE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "4":R+"本句是Apple MDM，不是Google Workspace。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"IT运维（墨西哥城）。"
},
"N0918":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"ROBOT_SOFTWARE","secondary_task":"",
 "task_evidence":"Triage robotics system issues to ensure reliability of production robotics systems; help diagnose and resolve operational issues when they arise",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"C++不是C语言。",
  "3":O+"RTOS未单列冻结项。",
  "4":R+"办公地点office不是Microsoft Office。",
  "5":R+"Series C融资不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人软件。C++拒收C。"
},
"N0922":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"ROBOT_PLATFORM","secondary_task":"DEV_INFRA",
 "task_evidence":"Improve reliability and scalability through robust testing, observability, incident response, and performance tuning.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"C++不是C语言。",
  "3":O+"OpenTelemetry未单列冻结项。",
  "4":[["V2_AWS","GENERAL","UNCONDITIONAL"],["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0922:4","6":"DUPLICATE:N0922:4",
  "7":R+"Series C融资不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人平台软件。"
},
"N0927":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"MULTI_ROBOT","secondary_task":"",
 "task_evidence":"Triage and root-cause field issues reported from the Warehouse",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"C++不是C语言。",
  "4":[["V2_CI_CD","GENERAL","UNCONDITIONAL"],["V2_AWS","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0927:4","6":"DUPLICATE:N0927:4",
  "7":R+"Series C融资不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"多机协同软件。"
},
"N0925":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"BUSINESS_APP","fine_task":"CLOUD_LOGISTICS","secondary_task":"",
 "task_evidence":"As a Software Engineer II you will play a critical role in working with our world-class cross-functional team",
 "new":{
  "1":R+"Series C融资不是C语言。",
  "2":O+"WMS未单列冻结项。","3":O+"TMS未单列冻结项。","4":O+"OMS未单列冻结项。","5":O+"IMS未单列冻结项。",
  "6":R+"advanced不是精益方法。",
  "7":[["V2_CI_CD","GENERAL","UNCONDITIONAL"],["V2_AWS","GENERAL","UNCONDITIONAL"]],
  "8":O+"REST未单列冻结项。",
  "9":"DUPLICATE:N0925:7","10":"DUPLICATE:N0925:7",
  "11":[["V2_TERRAFORM","GENERAL","CHOICE"]],
  "12":"DUPLICATE:N0925:11",
  "13":[["V2_GITLAB_CI","GENERAL","UNCONDITIONAL"]],
  "14":"DUPLICATE:N0925:13",
  "15":O+"GraphQL未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"云物流业务系统。GitLab CI不记Git。"
},
"N0921":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"SRE_SECURITY","secondary_task":"",
 "task_evidence":"Define and improve incident response processes, including on-call practices, runbooks, postmortems, severity frameworks, and follow-up tracking.",
 "new":outside(28,{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_TYPESCRIPT","GENERAL","CHOICE"]],
  "4":"DUPLICATE:N0921:3",
  "6":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "9":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_AWS","GENERAL","CHOICE"]],
  "10":"DUPLICATE:N0921:9","11":"DUPLICATE:N0921:9",
  "14":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"]],
  "15":"DUPLICATE:N0921:14","16":"DUPLICATE:N0921:14","17":"DUPLICATE:N0921:14",
  "20":[["V2_PROMETHEUS","GENERAL","CHOICE"],["V2_GRAFANA","GENERAL","CHOICE"]],
  "22":"DUPLICATE:N0921:20","24":"DUPLICATE:N0921:20",
  "28":R+"Series C融资不是C语言。"
 }),
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"SRE与安全。C++拒收C。IAM/OTel/SOC2目录外。"
},
"N0913":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"NIMBLE_BRAIN","secondary_task":"",
 "task_evidence":"Create automated evaluation, and remote operations",
 "new":{"1":R+"Series C融资不是C语言。"},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Nimble Brain运行软件。融资Round C拒收C。"
},
"E0599":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"TELEOP_DEPLOY","secondary_task":"",
 "task_evidence":"Develop comfortable and precise interfaces for controlling robots with many degrees of freedom",
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
 "notes":"部署遥操。网络分析仪不记硬件仪表。"
},
"E0605":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"BUSINESS_APP","fine_task":"MFG_TEST_SOFTWARE","secondary_task":"DEV_INFRA",
 "task_evidence":"Build technician-friendly, step-by-step workflows for assembly, flashing, provisioning, calibration, and final test.",
 "new":{
  "1":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CALIBRATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_CALIBRATION","GENERAL","CHOICE"]],
  "4":[["V2_MES","GENERAL","CHOICE"]],
  "5":R+"project-management skills不是Microsoft Project。",
  "6":[["V2_BAZEL","PREFERRED","CHOICE"],["V2_CALIBRATION","PREFERRED","CHOICE"]]
 },
 "old_overrides":{
  "O11":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原hardware test短词定位为空，改为制造/硬件测试经验句。","quote":"5+ years of software engineering experience, preferably involving manufacturing, robotics, hardware test, embedded systems, or fleet operations."}
 },
 "additions":[],"outside_extra":[],
 "notes":"制造测试软件。英语You'll拒收CAN。"
},
"E0581":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"REALTIME_PIPELINES","secondary_task":"",
 "task_evidence":"Own Real-Time Pipelines: Engineer low-latency, high-reliability sensor and actuator pipelines across Linux, drivers, and middleware.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":[["V2_PERF","GENERAL","EXAMPLE"]],
  "3":"DUPLICATE:E0581:2"
 },
 "old_overrides":{
  "O20":{"metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","relation":"OWN_DEVELOP","reason":"原real-time短词定位为空，改为实时管线职责句。","quote":"Own Real-Time Pipelines: Engineer low-latency, high-reliability sensor and actuator pipelines across Linux, drivers, and middleware."}
 },
 "additions":[],"outside_extra":[],
 "notes":"实时管线。C++拒收C。网络分析仪不记。"
},
"E0585":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"BUILD_RELEASE","secondary_task":"",
 "task_evidence":"CI/CD Ownership: Design and operate GitHub-based CI/CD systems (GitHub Actions, checks, workflows) with a focus on reliability, speed, and signal quality.",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_BAZEL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"GitHub产品叙述不是Git协作。",
  "3":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_GITHUB_ACTIONS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_BAZEL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_TYPESCRIPT","DUTY_OWN_USE","CHOICE"]],
  "5":[["V2_TERRAFORM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":R+"GitHub集成工作流不是Git协作。",
  "7":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "9":[["V2_BAZEL","GENERAL","CHOICE"]],
  "10":[["V2_TERRAFORM","GENERAL","UNCONDITIONAL"]],
  "11":[["V2_BAZEL","PREFERRED","UNCONDITIONAL"]],
  "12":"DUPLICATE:E0585:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"构建发布。GitHub Actions记Actions。C++拒收C。"
},
"N0930":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"SOFTWARE_ARCHITECTURE","secondary_task":"",
 "task_evidence":"Design architectural solutions and develop scalable, reliable, and performant systems (Python and/or C++) that stay maintainable over the long term",
 "new":{
  "1":R+"C++不是C语言。",
  "2":R+"C++不是C语言。",
  "3":R+"英语can不是CAN总线协议。",
  "4":[["V2_ZENOH","PREFERRED","CHOICE"],["V2_DDS","PREFERRED","CHOICE"]],
  "5":"DUPLICATE:N0930:4","6":"DUPLICATE:N0930:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"软件架构。C++拒收C。"
},
"N0665":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"EMBEDDED_SECURITY","secondary_task":"",
 "task_evidence":"Conduct detailed threat modeling and security assessments of critical assets.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":O+"PHP未单列冻结项。",
  "3":R+"薪资USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"嵌入式安全。"
},
"N0706":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"DEPLOY_INFRA","secondary_task":"",
 "task_evidence":"Architect, build, and maintain deployment software infrastructure and back-end services (e.g., model training infrastructure, AI developer tools, metrics dashboards).",
 "new":{
  "1":R+"C++不是C语言。",
  "2":R+"薪资USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"部署基础设施。"
},
"N0692":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"MANIPULATION_SOFTWARE","secondary_task":"",
 "task_evidence":"Write and maintain production-level C++ and Python code for our robotic manipulation platforms.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":R+"薪资USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"操作软件。C++拒收C。"
},
"N0667":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"FULLSTACK_WEB","secondary_task":"",
 "task_evidence":"Develop and maintain server-side applications using NodeJS",
 "new":outside(26,{
  "1":[["V2_NODEJS","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0667:1",
  "6":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0667:6",
  "8":[["V2_JAVASCRIPT","GENERAL","UNCONDITIONAL"],["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0667:8","10":"DUPLICATE:N0667:8",
  "11":[["V2_REACT","GENERAL","UNCONDITIONAL"]],
  "12":"DUPLICATE:N0667:11",
  "13":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "14":"DUPLICATE:N0667:13",
  "18":[["V2_MONGODB","GENERAL","CHOICE"]],
  "20":"DUPLICATE:N0667:18",
  "22":[["V2_REACT","PREFERRED","CHOICE"]],
  "23":"DUPLICATE:N0667:22",
  "24":R+"Three.js不是JavaScript语言。",
  "25":[["V2_AWS","GENERAL","UNCONDITIONAL"]],
  "26":"DUPLICATE:N0667:25"
 }),
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"全栈Web。Three.js拒收JS。"
},
"N0693":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"MANIPULATION_CONTROLS","secondary_task":"",
 "task_evidence":"Write and maintain production-level C++ and Python code for our robotic manipulation platforms.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":R+"薪资USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"操作与控制软件。C++拒收C。"
},
"N0701":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"DEVOPS","secondary_task":"",
 "task_evidence":"Own and scale Bazel/Skylark build infrastructure from scratch, including custom rules, toolchains, and remote caching across a multi-language codebase.",
 "new":outside(25,{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_BAZEL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0701:2",
  "5":"DUPLICATE:N0701:2",
  "7":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_HIL","DUTY_OWN_USE","CHOICE"],["V2_JENKINS","DUTY_OWN_USE","CHOICE"]],
  "8":"DUPLICATE:N0701:7","9":"DUPLICATE:N0701:7",
  "14":[["V2_AWS","DUTY_OWN_USE","CHOICE"],["V2_GCP","DUTY_OWN_USE","CHOICE"],["V2_AZURE","DUTY_OWN_USE","CHOICE"]],
  "15":"DUPLICATE:N0701:14","16":"DUPLICATE:N0701:14","17":"DUPLICATE:N0701:14",
  "18":[["V2_TERRAFORM","DUTY_OWN_USE","UNCONDITIONAL"],["V2_ANSIBLE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "19":"DUPLICATE:N0701:18","20":"DUPLICATE:N0701:18",
  "21":[["V2_BAZEL","GENERAL","UNCONDITIONAL"]],
  "22":[["V2_HIL","GENERAL","CHOICE"],["V2_JENKINS","GENERAL","CHOICE"]],
  "23":[["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "24":"DUPLICATE:N0701:23",
  "25":R+"薪资USD不是Universal Scene Description。"
 }),
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"DevOps。SIL不记功能安全。HIL与Jenkins保留。"
},
"N0705":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"ROBOT_INFRA","secondary_task":"DEV_INFRA",
 "task_evidence":"Design, implement, and maintain production-grade C++ and Go running directly on robotic platforms.",
 "new":outside(17,{
  "1":R+"本句不是C语言。",
  "2":R+"C++不是C语言。",
  "5":R+"C++不是C语言。",
  "6":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"]],
  "7":"DUPLICATE:N0705:6","8":"DUPLICATE:N0705:6",
  "17":R+"薪资USD不是Universal Scene Description。"
 }),
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人边云基础设施。MQTT/OTA目录外。C++拒收C。"
},
"N0711":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"MFG_TEST","secondary_task":"BUSINESS_APP",
 "task_evidence":"Develop software to automate subassembly and full-system checkouts",
 "new":{
  "1":[["V2_HIL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_DAQ","DUTY_OWN_USE","EXAMPLE"],["V2_PLC","DUTY_OWN_USE","EXAMPLE"]],
  "3":"DUPLICATE:N0711:2","4":"DUPLICATE:N0711:2",
  "5":[["V2_MES","DUTY_OWN_USE","CHOICE"],["V2_PLM","DUTY_OWN_USE","CHOICE"]],
  "6":"DUPLICATE:N0711:5",
  "7":O+"OpenBOM未单列冻结项。",
  "8":"DUPLICATE:N0711:5",
  "9":[["V2_MES","SEPARATE","BACKGROUND"]],
  "10":R+"薪资USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"制造测试软件。职称背景记MES背景。"
},
"N0668":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"FRONTEND_ANDROID","secondary_task":"",
 "task_evidence":"Design and develop responsive, high-performance web and Android applications",
 "new":outside(24,{
  "2":[["V2_TYPESCRIPT","DUTY_OWN_USE","UNCONDITIONAL"],["V2_JAVASCRIPT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0668:2","4":"DUPLICATE:N0668:2",
  "5":[["V2_JAVASCRIPT","GENERAL","UNCONDITIONAL"],["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0668:5","7":"DUPLICATE:N0668:5",
  "8":[["V2_REACT","GENERAL","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0668:8",
  "10":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0668:10",
  "12":[["V2_JAVASCRIPT","PREFERRED","UNCONDITIONAL"],["V2_TYPESCRIPT","PREFERRED","UNCONDITIONAL"],["V2_REACT","PREFERRED","CHOICE"],["V2_VUE","PREFERRED","CHOICE"]],
  "13":"DUPLICATE:N0668:12","14":"DUPLICATE:N0668:12","15":"DUPLICATE:N0668:12",
  "17":[["V2_UNITY","PREFERRED","CHOICE"],["V2_UNREAL","PREFERRED","CHOICE"]],
  "20":R+"Three.js不是JavaScript语言。",
  "22":"DUPLICATE:N0668:17","23":"DUPLICATE:N0668:17"
 }),
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"前端与Android。Three.js拒收JS。JS ecosystems记JavaScript。"
}
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
