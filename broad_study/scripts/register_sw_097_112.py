"""First-pass adjudication for software coding_order 97-112. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
IK1='REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7618912754813356326|0a53605460bb7a278e8d991e671e6198d16f36e39f83aa0a78b00568c144e9d2'
IK2='REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7678252117044660543|0a53605460bb7a278e8d991e671e6198d16f36e39f83aa0a78b00568c144e9d2'
AGENT={
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"AGENT_SYSTEM",
 "secondary_task":"ROBOT_RUNTIME",
 "task_evidence":"1. Agent 系统开发。负责 Agent 应用系统的设计与开发,包括环境感知、任务规划、上下文管理、工具调用、多模态交互等核心模块,构建稳定、可靠、可持续演进的 Agent 系统。",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_AGENT_WORKFLOW","PREFERRED","CHOICE"]]
 },
 "old_overrides":{
  "O4":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为加分项ROS/ROS2句。","quote":"2. 熟悉 ROS/ROS2,具备机器人真机开发、部署、联调及问题定位经验,具备工业或商业场景下的机器人真机项目落地与交付经验;"},
  "O10":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原计算机视觉短词定位为空，改为学历相关经验句。","quote":"1. 本科及以上学历,计算机、人工智能、自动化、机器人等相关专业优先;具有计算机视觉、自然语言处理、大模型、机器人等相关研究或工程经验。"},
  "O11":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原大模型短词定位为空，改为学历相关经验句。","quote":"1. 本科及以上学历,计算机、人工智能、自动化、机器人等相关专业优先;具有计算机视觉、自然语言处理、大模型、机器人等相关研究或工程经验。"},
  "O14":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原计算机视觉短词定位为空，改为加分项视觉句。","quote":"5. 具备计算机视觉或多模态模型的实际应用经验,熟悉目标检测、识别、分割、视觉定位等常见视觉任务,并能通过微调提升特定场景性能;"},
  "O17":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原大模型短词定位为空，改为加分项研究方向句。","quote":"6. 具备机器人、具身智能、大模型或多模态方向的研究经验,有高水平论文、专利或开源项目经验。"}
 },
 "additions":[
  {"code":"V2_AGENT_WORKFLOW","metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","quote":"1. Agent 系统开发。负责 Agent 应用系统的设计与开发,包括环境感知、任务规划、上下文管理、工具调用、多模态交互等核心模块,构建稳定、可靠、可持续演进的 Agent 系统。","reason":"主责Agent系统设计开发。"}
 ],
 "outside_extra":[],
 "notes":"Agent系统。两条E0107同文不同岗位ID分别登记。泛称微调不记后训练。开源项目不记Git。"
}
decisions={
"E0235":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"TELEOP_INTEGRATION",
 "secondary_task":"",
 "task_evidence":"- 负责遥操作系统的集成与调试,优化数据交互逻辑与系统资源调度,解决部署中的同步、延迟与可靠性问题。",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":R+"C++/Python不是C语言。",
  "4":[["V2_DDS","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_ETHERCAT","PREFERRED","EXAMPLE"],["V2_CAN","PREFERRED","EXAMPLE"]],
  "6":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O3":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为ROS/ROS2及DDS句。","quote":"- 熟悉ROS/ROS2机器人操作系统及DDS中间件,具备通信延迟测量与优化经验。"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"遥操系统集成。C++拒收C。CANopen按CAN示例。"
},
"E0211":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"ROBOT_CLOUD_PLATFORM",
 "secondary_task":"DEV_INFRA",
 "task_evidence":"1. 平台架构与核心开发:负责机器人/AI业务全链路云平台系统的架构设计、核心模块开发与迭代,主导技术选型,构建稳定、高效、可扩展的技术底座,推动数据闭环的建立与优化;",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_SPARK","GENERAL","CHOICE"],["V2_CLICKHOUSE","GENERAL","CHOICE"]],
  "3":"DUPLICATE:E0211:2"
 },
 "old_overrides":{
  "O11":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原单元测试短词定位为空，改为工程素养句。","quote":"4. 工程素养与 Ownership:具备良好的编码规范、单元测试习惯和代码重构能力。既能独立完成从0到1的系统搭建,也善于在复杂现有系统中持续改进、优化与赋能业务;"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"机器人云平台。Spark/ClickHouse任选。"
},
"E0191":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"ONBOARD_CONTAINER_RUNTIME",
 "secondary_task":"",
 "task_evidence":"1. 负责机器人内部容器管理器及运行时核心组件的设计与优化,实现高性能、高可靠的容器化调度与编排;",
 "new":{
  "1":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_C","GENERAL","UNRESOLVED"]],
  "3":[["V2_GDB","GENERAL","EXAMPLE"],["V2_PERF","GENERAL","EXAMPLE"]],
  "4":"DUPLICATE:E0191:3",
  "5":O+"runc/crun及OCI/CRI未单列冻结项。"
 },
 "old_overrides":{
  "O2":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为内核机制句。","quote":"3.  熟悉 Linux 内核机制,尤其是内核网络、内存管理、IPC 与文件系统,有嵌入式/边缘 Linux 开发经验;"},
  "O6":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为ROS/ROS2容器化句。","quote":"8.  机器人操作系统(ROS/ROS2)下容器化经验,熟悉多节点容器编排与资源隔离;"},
  "O11":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原嵌入式短词定位为空，改为学历经验句。","quote":"1. 本科及以上学历,计算机、软件工程或机器人相关专业,3 年以上嵌入式/系统开发经验;"},
  "O12":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原嵌入式短词定位为空，改为学历经验句。","quote":"1. 本科及以上学历,计算机、软件工程或机器人相关专业,3 年以上嵌入式/系统开发经验;"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"端侧容器运行时。C/C++按C未解。"
},
"E0190":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"MIDDLEWARE",
 "secondary_task":"",
 "task_evidence":"1、负责机器人中间件的设计、开发、测试和部署,构建统一的软件通信与运行框架;",
 "new":{
  "1":[["V2_GDB","DUTY_OWN_USE","UNCONDITIONAL"],["V2_WIRESHARK","DUTY_OWN_USE","UNCONDITIONAL"],["V2_PERF","DUTY_OWN_USE","UNCONDITIONAL"],["V2_FTRACE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_C","GENERAL","UNRESOLVED"]],
  "3":[["V2_DDS","GENERAL","CHOICE"],["V2_ZENOH","GENERAL","CHOICE"]],
  "4":[["V2_PROMETHEUS","PREFERRED","EXAMPLE"],["V2_GRAFANA","PREFERRED","EXAMPLE"]],
  "5":"DUPLICATE:E0190:4",
  "6":[["V2_CI_CD","PREFERRED","UNCONDITIONAL"]],
  "7":"DUPLICATE:E0190:1"
 },
 "old_overrides":{
  "O3":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为C/C++或嵌入式Linux经验句。","quote":"2、熟练使用 C/C++、Rust 开发,具备 3 年以上机器人基础软件、机器人平台或嵌入式 Linux 系统开发经验。"},
  "O4":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为系统原理句。","quote":"3、熟悉 Linux 系统原理与开发,包括进程调度、内存管理、文件系统、网络编程。"},
  "O5":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为中间件任选句。","quote":"4、熟悉一种或多种机器人中间件或通信框架,如 ROS/ROS2、DDS(Cyclone DDS/FastDDS)、Zenoh、iceoryx2、dora-rs、copper-rs 等。"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"机器人中间件。C/C++按C未解。iceoryx等目录外。"
},
"E0177":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"CONTROL_FRAMEWORK",
 "secondary_task":"",
 "task_evidence":"1.负责机器人控制相关底层架构与接口抽象,搭建仿真器、实体机器人硬件统一接口,实现仿真与真机无缝切换。",
 "new":{
  "1":R+"现代C++不是C语言。",
  "2":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":[["V2_MODEL_COMPRESSION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":R+"C++17/20不是C语言。",
  "7":[["V2_SIM2REAL","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "9":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]],
  "10":R+"UDP不是TCP/IP。",
  "11":[["V2_MODEL_COMPRESSION","GENERAL","UNCONDITIONAL"]],
  "12":[["V2_TENSORRT","PREFERRED","CHOICE"],["V2_ONNX","PREFERRED","CHOICE"],["V2_ONNX_RUNTIME","PREFERRED","CHOICE"],["V2_MODEL_COMPRESSION","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O21":{"metric":"REQUIRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原仿真短词定位为空，改为统一接口职责句。","quote":"1.负责机器人控制相关底层架构与接口抽象,搭建仿真器、实体机器人硬件统一接口,实现仿真与真机无缝切换。"},
  "O33":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原仿真器短词定位为空，改为统一接口职责句。","quote":"1.负责机器人控制相关底层架构与接口抽象,搭建仿真器、实体机器人硬件统一接口,实现仿真与真机无缝切换。"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"控制框架与虚实接口。C++拒收C。量化蒸馏记压缩。TVM未单列。"
},
"E0174":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"TELEOP_AV",
 "secondary_task":"",
 "task_evidence":"1. 负责机器人遥操场景下实时音视频链路的架构设计、开发、集成和持续优化,覆盖机器人端、网络传输、云端服务及遥操端;",
 "new":{
  "1":[["V2_C","GENERAL","UNRESOLVED"]],
  "2":[["V2_WIRESHARK","GENERAL","EXAMPLE"],["V2_PERF","GENERAL","EXAMPLE"]],
  "3":O+"FFmpeg/GStreamer/WebRTC未单列冻结项。"
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为学历平台经验句。","quote":"1. 本科及以上学历,计算机、电子工程、通信工程、自动化等相关专业,具备3年及以上Linux平台音视频或实时通信开发经验;"},
  "O3":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为系统编程句。","quote":"2. 精通C/C++，具备扎实的Linux系统编程能力，熟悉多线程、进科程间通信、内存管理、网络编程、线程调度和性能优化；"}
 },
 "additions":[{"code":"V2_TELEOP","metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","quote":"1. 负责机器人遥操场景下实时音视频链路的架构设计、开发、集成和持续优化,覆盖机器人端、网络传输、云端服务及遥操端;","reason":"主责遥操音视频链路。"}],
 "outside_extra":[],
 "notes":"遥操音视频。C/C++按C未解。"
},
"E0158":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"SYSTEM_ARCHITECTURE",
 "secondary_task":"",
 "task_evidence":"主导具身智能整机软件和算法系统的需求分解与架构设计,确保系统高可用,高拓展性与高性能;",
 "new":{
  "1":[["V2_REQUIREMENTS_ENGINEERING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_DDS","GENERAL","CHOICE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"整机软件架构。dds/ros按DDS任选。"
},
"E0141":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"AGENT_SYSTEM",
 "secondary_task":"ROBOT_RUNTIME",
 "task_evidence":"1. Agent 系统开发。负责 Agent 应用系统的设计与开发,包括环境感知、任务规划、上下文管理、工具调用、多模态交互等核心模块,构建稳定、可靠、可持续演进的 Agent 系统。",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_AGENT_WORKFLOW","PREFERRED","CHOICE"]]
 },
 "old_overrides":{
  "O4":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为加分项ROS/ROS2句。","quote":"2. 熟悉 ROS/ROS2,具备机器人真机开发、部署、联调及问题定位经验,具备工业或商业场景下的机器人真机项目落地与交付经验;"},
  "O10":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原计算机视觉短词定位为空，改为学历相关经验句。","quote":"1. 本科及以上学历,计算机、人工智能、自动化、机器人等相关专业优先;具有计算机视觉、自然语言处理、大模型、机器人等相关研究或工程经验。"},
  "O11":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原大模型短词定位为空，改为学历相关经验句。","quote":"1. 本科及以上学历,计算机、人工智能、自动化、机器人等相关专业优先;具有计算机视觉、自然语言处理、大模型、机器人等相关研究或工程经验。"},
  "O14":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原计算机视觉短词定位为空，改为加分项视觉句。","quote":"5. 具备计算机视觉或多模态模型的实际应用经验,熟悉目标检测、识别、分割、视觉定位等常见视觉任务,并能通过微调提升特定场景性能;"},
  "O17":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原大模型短词定位为空，改为加分项研究方向句。","quote":"6. 具备机器人、具身智能、大模型或多模态方向的研究经验,有高水平论文、专利或开源项目经验。"}
 },
 "additions":[
  {"code":"V2_AGENT_WORKFLOW","metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","quote":"1. Agent 系统开发。负责 Agent 应用系统的设计与开发,包括环境感知、任务规划、上下文管理、工具调用、多模态交互等核心模块,构建稳定、可靠、可持续演进的 Agent 系统。","reason":"主责Agent系统设计开发。"}
 ],
 "outside_extra":[],
 "notes":"Agent应用。与E0107近同文不同身份。泛称微调不记后训练。"
},
"E0129":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DEV_INFRA",
 "fine_task":"AI_STORAGE",
 "secondary_task":"",
 "task_evidence":"1. 高性能存储方案调研、选型与深度定制:结合业务场景(具身智能训练/推理),评估并引入合适的存储技术(如 3FS、JuiceFS、Alluxio 等),进行深度二次开发与性能调优。重点优化 FUSE 客户端、元数据服务及存储引擎,完善基于对象存储的缓存机制,结合 IB/RoCE 高性能网络,实现低延迟、高吞吐的数据访问能力,消除 AI 场景下的 I/O 瓶颈。",
 "new":{
  "1":[["V2_C","GENERAL","UNRESOLVED"]],
  "2":[["V2_INCIDENT_SUPPORT","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O2":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原Rust短词定位为空，改为C/C++或Rust句。","quote":"1. 编程能力:精通 C/C++ 或 Rust(Rust 优先),熟练使用 Python/Go;扎实的计算机系统基础(操作系统、编译原理、计算机网络)。"},
  "O5":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Rust短词定位为空，改为C/C++或Rust句。","quote":"1. 编程能力:精通 C/C++ 或 Rust(Rust 优先),熟练使用 Python/Go;扎实的计算机系统基础(操作系统、编译原理、计算机网络)。"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"训练存储。C/C++按C未解。3FS等目录外。"
},
"E0119":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA",
 "fine_task":"SRE",
 "secondary_task":"",
 "task_evidence":"1. 负责 AICP 在云和 Kubernetes 上的可用性、性能、容量和灾备。",
 "new":{
  "1":[["V2_POSTGRESQL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_TCPIP","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_POSTGRESQL","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_PROMETHEUS","GENERAL","CHOICE"],["V2_GRAFANA","GENERAL","CHOICE"]],
  "6":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_ANSIBLE","GENERAL","CHOICE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"AI平台SRE。TCP/P按TCP/IP。Helm/Kustomize目录外。"
},
"E0115":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"ONBOARD_AUDIO",
 "secondary_task":"",
 "task_evidence":"1. 主导机器人端侧音频处理业务模块的需求分析、技术方案设计及核心代码开发,保障音频系统的稳定性与可扩展性;",
 "new":{
  "1":R+"C++/Python不是C语言。",
  "2":[["V2_TENSORRT","PREFERRED","CHOICE"],["V2_ONNX","PREFERRED","CHOICE"],["V2_ONNX_RUNTIME","PREFERRED","CHOICE"]]
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为学历经验句。","quote":"1. 本科及以上学历,计算机、电子、通信等相关专业,3年及以上Linux应用软件开发经验;"},
  "O4":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Linux短词定位为空，改为学历经验句。","quote":"1. 本科及以上学历,计算机、电子、通信等相关专业,3年及以上Linux应用软件开发经验;"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"端侧音频。C++拒收C。ONNX与ONNX Runtime分列。"
},
"E0114":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"XR_TELEOP",
 "secondary_task":"",
 "task_evidence":"1. 负责机器人VR遥操作应用的架构设计、核心功能开发、性能优化及长期维护。",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_UNITY","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_UNREAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_URDF","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_CALIBRATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":[["V2_UNITY","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_UNREAL","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_URDF","GENERAL","UNCONDITIONAL"]],
  "8":R+"C++不是C语言。",
  "9":[["V2_DDS","PREFERRED","EXAMPLE"]],
  "10":[["V2_CALIBRATION","PREFERRED","CHOICE"],["V2_CLASSICAL_CONTROL","PREFERRED","CHOICE"]],
  "11":[["V2_UNITY","PREFERRED","CHOICE"],["V2_SIM2REAL","PREFERRED","CHOICE"]],
  "12":[["V2_UNITY","PREFERRED","CHOICE"]],
  "13":"DUPLICATE:E0114:5",
  "14":"DUPLICATE:E0114:6"
 },
 "old_overrides":{
  "O8":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为加分项通信句。","quote":"1. 熟悉ROS/ROS2、DDS、rosbridge等机器人通信技术。"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"VR遥操。C#/C++拒收C。人体标定记标定。OpenXR目录外。"
},
"E0362":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"ROBOT_BEHAVIORS",
 "secondary_task":"",
 "task_evidence":"Own the design, implementation, and validation of complex humanoid robot behaviors.",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":R+"英语can不是CAN总线协议。",
  "3":R+"C++不是C语言。",
  "4":R+"薪资USD不是Universal Scene Description。",
  "5":R+"猎头免责声明不是人力资源专业职责。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"人形行为软件。C++拒收C。薪资与猎头模板拒收。"
},
"E0306":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DEV_INFRA",
 "fine_task":"CAD_PLM_ADMIN",
 "secondary_task":"",
 "task_evidence":"CAD Infrastructure Management",
 "new":{
  "1":[["V2_PLM","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_PLM","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_NETSUITE","PREFERRED","UNCONDITIONAL"]],
  "4":[["V2_PLM","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_PLM","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_PLM","GENERAL","UNCONDITIONAL"]],
  "7":R+"办公地点office不是Microsoft Office。",
  "8":R+"薪资USD不是Universal Scene Description。",
  "9":R+"猎头免责声明不是人力资源专业职责。",
  "10":"DUPLICATE:E0306:3"
 },
 "old_overrides":{
  "O10":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原Creo短词定位为空，改为Creo/Windchill经验句。","quote":"10-15 years of hands-on experience with Creo/ Windchill, including practical ownership of vault structure, workflows, permissions, metadata, custom properties, revision management, release processes,"},
  "O11":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原Windchill短词定位为空，改为PDM句。","quote":"Windchill PDM (lifecycle, data structures, multi-user environment)"},
  "O12":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Creo短词定位为空，改为培训句。","quote":"Continuous Creo/WC/Altium or equivalent ECAD coaching and training"},
  "O14":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Windchill短词定位为空，改为PDM句。","quote":"Windchill PDM (lifecycle, data structures, multi-user environment)"},
  "O16":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"原CAD短词定位为空，改为职责标题。","quote":"CAD Infrastructure Management"},
  "O17":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Creo短词定位为空，改为培训句。","quote":"Continuous Creo/WC/Altium or equivalent ECAD coaching and training"},
  "O18":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Windchill短词定位为空，改为PDM句。","quote":"Windchill PDM (lifecycle, data structures, multi-user environment)"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"CAD/PLM管理。办公地点与薪资拒收。NetSuite加分。"
}
}
# deepcopy AGENT for second identity
decisions[IK1]=dict(AGENT);decisions[IK2]=dict(AGENT)
decisions[IK1]['new']=dict(AGENT['new']);decisions[IK2]['new']=dict(AGENT['new'])
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
