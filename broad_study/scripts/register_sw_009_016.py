"""First-pass adjudication for software coding_order 9-16. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"E0609":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"ANNOTATION_FULLSTACK",
 "secondary_task":"DEV_INFRA",
 "task_evidence":"Own annotation tooling: Build the platform and workflows for annotation generation, from the interfaces annotators work in to the pipelines behind them, and translate requirements from researchers into an actionable plan and the software to execute it.",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":[["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"],["V2_REACT","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_POSTGRESQL","GENERAL","EXAMPLE"],["V2_CLICKHOUSE","GENERAL","EXAMPLE"]],
  "4":[["V2_GCP","GENERAL","EXAMPLE"]],
  "5":[["V2_TYPESCRIPT","PREFERRED","UNCONDITIONAL"],["V2_REACT","PREFERRED","UNCONDITIONAL"],["V2_POSTGRESQL","PREFERRED","UNCONDITIONAL"],["V2_CLICKHOUSE","PREFERRED","UNCONDITIONAL"],["V2_GCP","PREFERRED","UNCONDITIONAL"]],
  "6":"DUPLICATE:E0609:2"
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Python短词定位为空，改为React/TypeScript句。","quote":"especially with React, TypeScript, and Python."},
  "O2":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原Kubernetes短词定位为空，改为GCP句。","quote":"Familiarity with cloud and containerized environments such as GCP and Kubernetes."},
  "O3":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Python短词定位为空，改为具体技术栈句。","quote":"Experience with our specific stack: React, TypeScript, Python, Postgres, ClickHouse, GCP, and Kubernetes."},
  "O4":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Kubernetes短词定位为空，改为具体技术栈句。","quote":"Experience with our specific stack: React, TypeScript, Python, Postgres, ClickHouse, GCP, and Kubernetes."}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责标注工具全栈。英语can拒收CAN。"
},
"E0018":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"ROS2_MIDDLEWARE",
 "secondary_task":"",
 "task_evidence":"1.负责机器人ROS2 中间件体系的建设、优化与量产化落地",
 "new":{
  "1":[["V2_DDS","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_DDS","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_DDS","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_DDS","GENERAL","UNCONDITIONAL"]],
  "5":R+"C++不是C语言。",
  "6":[["V2_DDS","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O5":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原C++短词定位为空，改为对象模型句。","quote":"6.具备较强的 C++ 开发和源码分析能力，对 C++ 对象模型、STL 等有深入理解"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责ROS2中间件。Fast DDS按DDS编码。C++拒收C。"
},
"E0192":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DEV_INFRA",
 "fine_task":"EDGE_DEVOPS_CICD",
 "secondary_task":"",
 "task_evidence":"1、搭建和优化机器人研发全流程 CI/CD 流水线，实现算法、控制程序、固件及 ROS/ROS2 代码的自动化构建、测试、打包和端侧部署；",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"],["V2_JENKINS","DUTY_OWN_USE","EXAMPLE"],["V2_GITLAB_CI","DUTY_OWN_USE","EXAMPLE"]],
  "3":"DUPLICATE:E0192:2",
  "4":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_SHELL","GENERAL","CHOICE"]],
  "7":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "8":R+"GitLab Registry不是Git工具项的充分证据。",
  "9":O+"Harbor/Nexus/GitLab Registry未单列冻结项。"
 },
 "old_overrides":{
  "O10":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为流水线句。","quote":"1、搭建和优化机器人研发全流程 CI/CD 流水线，实现算法、控制程序、固件及 ROS/ROS2 代码的自动化构建、测试、打包和端侧部署；"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责端侧CI/CD。GitLab按GitLab CI编码，Registry拒收Git。"
},
"N0143":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"ONBOARD_APP_AGENT",
 "secondary_task":"ROBOT_CLOUD_UI",
 "task_evidence":"1、参与具身智能机器人本体侧应用软件开发，接入并集成语音识别、语音合成、大模型、多模态模型等 AI 能力，实现机器人对话、主动交互、任务理解、情绪反馈等功能。",
 "new":{
  "1":R+"Python 和 C++不是C语言。",
  "2":[["V2_TYPESCRIPT","PREFERRED","UNCONDITIONAL"],["V2_NODEJS","PREFERRED","EXAMPLE"]],
  "3":"DUPLICATE:N0143:2",
  "4":"DUPLICATE:N0143:2",
  "5":O+"ALSA未单列冻结项。","6":O+"PulseAudio未单列冻结项。","7":O+"PipeWire未单列冻结项。","8":O+"PCM未单列冻结项。",
  "9":[["V2_AGENT_WORKFLOW","PREFERRED","UNCONDITIONAL"]],
  "10":[["V2_CI_CD","PREFERRED","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0143:10"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责本体应用与Agent。Node.js不升JavaScript。C++拒收C。"
},
"N0946":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"HW_SW_RUNTIME_STACK",
 "secondary_task":"",
 "task_evidence":"Help us build the software stack underneath Frontier AI & Robotics: the layer between hardware and the AI policies running on it.",
 "new":{
  "1":R+"该句未出现DDS或USB。",
  "2":[["V2_DDS","DUTY_OWN_USE","EXAMPLE"]],
  "3":"DUPLICATE:N0946:2",
  "4":R+"英语can不是CAN总线协议。",
  "5":R+"C++/Python不是C语言。",
  "6":[["V2_I2C","GENERAL","EXAMPLE"],["V2_SPI","GENERAL","EXAMPLE"],["V2_USB","GENERAL","EXAMPLE"],["V2_CAN","GENERAL","EXAMPLE"]],
  "7":"DUPLICATE:N0946:6","8":"DUPLICATE:N0946:6","9":"DUPLICATE:N0946:6",
  "10":O+"MIPI未单列冻结项。",
  "11":"DUPLICATE:N0946:6",
  "12":[["V2_DDS","GENERAL","UNCONDITIONAL"]],
  "13":"DUPLICATE:N0946:12",
  "14":O+"shared memory IPC未单列冻结项。",
  "15":O+"asyncio未单列冻结项。","16":O+"multiprocessing未单列冻结项。","17":O+"GIL未单列冻结项。",
  "18":R+"洛杉矶县安全合作声明不是客户服务专业职责。",
  "19":R+"招聘联系人说明不是人力资源专业职责。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责硬件到策略运行栈。协议列表按示例编码。英语can与页脚拒收。"
},
"N0999":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION",
 "fine_task":"CUSTOMER_SOFTWARE_CONSULTING",
 "secondary_task":"",
 "task_evidence":"The Senior Consultant works directly with external clients and project leadership on paid engagements to execute the development and delivery of software integrations and tools, an",
 "new":{
  "1":R+"project leadership不是Microsoft Project。",
  "2":R+"Project Directors不是Microsoft Project。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责客户软件集成咨询。项目职务拒收MS Project。"
},
"E0363":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"TELEOP_ARCHITECTURE",
 "secondary_task":"",
 "task_evidence":"Architect from the Ground Up: Own the end-to-end software architecture of our data collection and teleoperation systems, ensuring highly modular, scalable, and predictable behavior",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":R+"英语can不是CAN总线协议。",
  "3":R+"modern C++ or Rust不是C语言。",
  "4":[["V2_MOCAP","GENERAL","CHOICE"]],
  "5":[["V2_UNITY","PREFERRED","EXAMPLE"],["V2_UNREAL","PREFERRED","EXAMPLE"]],
  "6":[["V2_3D_RECONSTRUCTION","PREFERRED","EXAMPLE"]],
  "7":R+"薪资USD不是Universal Scene Description。",
  "8":R+"第三方招聘机构说明不是人力资源专业职责。",
  "9":"DUPLICATE:E0363:5"
 },
 "old_overrides":{
  "O11":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原real-time systems短词定位为空，改为年限句。","quote":"7+ years of experience in software engineering for robotics, real-time systems, or highly complex hardware-software integrations."},
  "O12":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原real-time systems短词定位为空，改为C++/Rust句。","quote":"Demonstrated experience in modern C++ or Rust, with a strong track record of building and optimizing low-latency, real-time systems (Python proficiency is a strong plus)."}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责遥操数据采集架构。薪资USD与页脚拒收。"
},
"N0840":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA",
 "fine_task":"INFRA_TOOLS",
 "secondary_task":"",
 "task_evidence":"Design, build, and maintain core infrastructure components such as CI/CD pipelines, build systems, monitoring tools, and deployment frameworks.",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_ANSIBLE","DUTY_OWN_USE","EXAMPLE"]],
  "3":"DUPLICATE:N0840:2",
  "4":[["V2_TYPESCRIPT","GENERAL","CHOICE_AND_EXAMPLE"]],
  "5":"DUPLICATE:N0840:4",
  "6":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"]],
  "7":"DUPLICATE:N0840:6","8":"DUPLICATE:N0840:6","9":"DUPLICATE:N0840:6",
  "10":[["V2_AWS","GENERAL","EXAMPLE"]],
  "11":"DUPLICATE:N0840:10",
  "12":[["V2_PROMETHEUS","PREFERRED","EXAMPLE"],["V2_GRAFANA","PREFERRED","EXAMPLE"]],
  "13":"DUPLICATE:N0840:12","14":"DUPLICATE:N0840:12",
  "15":O+"Sentry未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责基础设施与工具。云平台任选。Sentry目录外。"
}
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
