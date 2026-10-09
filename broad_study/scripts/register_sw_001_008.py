"""First-pass adjudication for software coding_order 1-8. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"E0441":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"RAAS_PLATFORM_ARCHITECTURE",
 "secondary_task":"CUSTOMER_INTEGRATION",
 "task_evidence":"We’re hiring a Senior Systems Engineer to help drive architectural clarity across our Robot-as-a-Service (RaaS) platform — the edge and cloud software that connects our humanoid robots to operators, customer systems, and the broader fleet.",
 "new":{
  "1":R+"英语can不是CAN总线协议。",
  "2":R+"英语can不是CAN总线协议。",
  "3":R+"modern C++不是C语言。",
  "4":R+"英语can不是CAN总线协议。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责RaaS平台架构接口。C++拒收C。"
},
"N0200":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA",
 "fine_task":"DATA_PLATFORM_FULLSTACK",
 "secondary_task":"",
 "task_evidence":"负责大数据生态相关产品的全栈开发，包括数据平台、数据开发工具、数据治理平台、湖仓管理平台、任务调度系统、可视化管理后台等。",
 "new":{
  "1":[["V2_CLAUDE_CODE","DUTY_OWN_USE","EXAMPLE"],["V2_CODEX","DUTY_OWN_USE","EXAMPLE"]],
  "2":"DUPLICATE:N0200:1","3":"DUPLICATE:N0200:1",
  "4":O+"FastAPI未单列冻结项。","5":O+"Flask未单列冻结项。","6":O+"Django未单列冻结项。","7":O+"Spring Boot未单列冻结项。",
  "8":[["V2_REACT","GENERAL","CHOICE_AND_EXAMPLE"],["V2_VUE","GENERAL","CHOICE_AND_EXAMPLE"],["V2_TYPESCRIPT","GENERAL","CHOICE_AND_EXAMPLE"]],
  "9":"DUPLICATE:N0200:8","10":"DUPLICATE:N0200:8","11":"DUPLICATE:N0200:8",
  "12":O+"Next.js未单列冻结项。",
  "13":[["V2_CLAUDE_CODE","GENERAL","EXAMPLE"],["V2_CODEX","GENERAL","EXAMPLE"]],
  "14":"DUPLICATE:N0200:13","15":"DUPLICATE:N0200:13",
  "16":[["V2_SQL_MYSQL","GENERAL","EXAMPLE"],["V2_POSTGRESQL","GENERAL","EXAMPLE"],["V2_REDIS","GENERAL","EXAMPLE"]],
  "17":"DUPLICATE:N0200:16","18":"DUPLICATE:N0200:16","19":"DUPLICATE:N0200:16",
  "20":O+"RESTful API未单列冻结项。",
  "21":[["V2_SPARK","PREFERRED","EXAMPLE"],["V2_FLINK","PREFERRED","EXAMPLE"],["V2_KAFKA","PREFERRED","EXAMPLE"],["V2_AIRFLOW","PREFERRED","EXAMPLE"]],
  "22":O+"Hadoop未单列冻结项。","23":O+"Hive未单列冻结项。",
  "24":"DUPLICATE:N0200:21","25":"DUPLICATE:N0200:21","26":"DUPLICATE:N0200:21",
  "27":O+"Presto/Trino未单列冻结项。","28":O+"Iceberg未单列冻结项。","29":O+"Hudi未单列冻结项。","30":O+"Delta Lake未单列冻结项。",
  "31":"DUPLICATE:N0200:21",
  "32":O+"DolphinScheduler未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"Next.js","description":"Next.js不是JavaScript语言项。"}],
 "notes":"主责数据平台全栈。Claude Code/Codex、前端任选、库与大数据示例成立。"
},
"N0643":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"APP_DEVICE_COMM_INTERN",
 "secondary_task":"",
 "task_evidence":"协助开发机器人应用，支持机械臂、灵巧手等设备的功能交互与演示；",
 "new":{
  "1":O+"EDP开发平台未单列冻结项。",
  "2":R+"串口/网口不是RS-485的充分证据。",
  "3":O+"WiFi未单列冻结项。","4":O+"蓝牙未单列冻结项。",
  "5":R+"Python/C++等不是C语言；斜线保持未解。",
  "6":R+"串口通信不是RS-485的充分证据。",
  "7":O+"Socket未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"实习应用开发。串口不升RS485。"
},
"N0406":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"AGENT_CONTROL_PLANE_JAVA",
 "secondary_task":"",
 "task_evidence":"主要负责灵心平台的后端开发(机器人交互的控制面)，机器人Agent的二开SDK",
 "new":{},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"候选队列为空。灵心控制面后端。"
},
"N0501":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"ROBOT_AGENT_WORKFLOW",
 "secondary_task":"",
 "task_evidence":"参与机器人智能体系统研发，构建任务规划、技能调度、记忆管理和异常处理等核心能力。",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","GENERAL","UNCONDITIONAL"]],
  "2":O+"Function Calling未单列冻结项。","3":O+"Tool Use未单列冻结项。",
  "4":"DUPLICATE:N0501:1",
  "5":O+"行为树未单列冻结项。","6":O+"状态机未单列冻结项。",
  "7":R+"C++不是C语言。",
  "8":[["V2_AGENT_WORKFLOW","PREFERRED","UNCONDITIONAL"]],
  "9":O+"Agent框架未单列冻结项。",
  "10":"DUPLICATE:N0501:8"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责机器人智能体工作流。C++拒收C。"
},
"N0929":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"AUTONOMY_BACKEND",
 "secondary_task":"",
 "task_evidence":"We're looking for a Backend Software Engineer to join our autonomy team and build the scalable systems behind task planning and robotic workflows.",
 "new":{
  "1":O+"task planning未单列冻结项。",
  "2":R+"Python (and C++ where needed)不是C语言。",
  "3":R+"C++ or another strongly typed language不是C语言。",
  "4":[["V2_KAFKA","GENERAL","EXAMPLE"]],
  "5":"DUPLICATE:N0929:4"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"自主后端服务。Kafka为消息框架示例。"
},
"N0543":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"NAV_CONTROL_PERCEPT_INTEGRATION",
 "secondary_task":"CUSTOMER_INTEGRATION",
 "task_evidence":"负责机器人导航系统、运动控制、感知模块的软件集成与联调。",
 "new":{
  "1":[["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0543:1",
  "3":R+"Python 或 C++不是C语言。",
  "4":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0543:4"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"现场软件集成。Git明确协作工具。Shell成立。"
},
"N0684":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"REACT_NATIVE_ROBOT_CONTROL",
 "secondary_task":"",
 "task_evidence":"Develop and maintain our React Native mobile applications",
 "new":{
  "1":[["V2_REACT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0684:1","3":"DUPLICATE:N0684:1",
  "4":[["V2_REACT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0684:4",
  "6":O+"WebSocket未单列冻结项。",
  "7":[["V2_REACT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "8":"DUPLICATE:N0684:7","9":"DUPLICATE:N0684:7",
  "10":[["V2_JAVASCRIPT","GENERAL","UNRESOLVED"],["V2_TYPESCRIPT","GENERAL","UNRESOLVED"]],
  "11":"DUPLICATE:N0684:10","12":"DUPLICATE:N0684:10",
  "13":[["V2_REACT","GENERAL","CHOICE"]],
  "14":O+"WebSocket未单列冻结项。",
  "15":[["V2_REACT","PREFERRED","CHOICE"]],
  "16":R+"Three.js不是JavaScript语言项的充分证据。",
  "17":O+"WebRTC未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责机器人控制监测移动端。React Native按React编码。JS/TS斜线未解。"
}
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
