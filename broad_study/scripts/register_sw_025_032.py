"""First-pass adjudication for software coding_order 25-32. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"N0393":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"GOLANG_BACKEND",
 "secondary_task":"",
 "task_evidence":"1. 设计、开发和维护基于 Golang 的后端服务，确保系统的高性能和可靠性；",
 "new":{
  "1":R+"Github开源项目不是Git工具项的充分证据。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责Golang后端。GitHub社区活跃拒收Git。"
},
"N0390":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"OPEN_PLATFORM_GATEWAY",
 "secondary_task":"",
 "task_evidence":"1. 负责企业级开放平台与 API Gateway 相关系统的设计、开发与维护，支撑机器人云平台能力对内、对外开放。",
 "new":{
  "1":O+"OAuth2未单列冻结项。","2":O+"JWT未单列冻结项。","3":O+"IAM未单列冻结项。",
  "4":O+"REST API未单列冻结项。","5":O+"WebSocket未单列冻结项。","6":O+"OAuth2未单列冻结项。","7":O+"JWT未单列冻结项。","8":O+"API Key未单列冻结项。",
  "9":[["V2_SQL_MYSQL","GENERAL","EXAMPLE"],["V2_REDIS","GENERAL","EXAMPLE"]],
  "10":"DUPLICATE:N0390:9","11":"DUPLICATE:N0390:9",
  "12":O+"MQ未单列冻结项。",
  "13":[["V2_CI_CD","PREFERRED","UNCONDITIONAL"]],
  "14":"DUPLICATE:N0390:13",
  "15":O+"OpenTelemetry未单列冻结项。",
  "16":O+"IAM未单列冻结项。","17":O+"OAuth2未单列冻结项。","18":O+"OIDC未单列冻结项。",
  "19":O+"Kong未单列冻结项。","20":O+"APISIX未单列冻结项。","21":O+"Envoy未单列冻结项。",
  "22":O+"Nginx未单列冻结项。","23":O+"Istio未单列冻结项。","24":O+"Spring Cloud Gateway未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责开放平台与网关。MySQL/Redis/CI/CD成立，其余目录外。"
},
"N0504":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"LEGGED_ROBOT_SOFTWARE",
 "secondary_task":"",
 "task_evidence":"1. 负责足式机器人软件系统的设计与实现，覆盖运动控制、传感器融合、自主决策与人机交互。",
 "new":{
  "1":R+"C++不是C语言。",
  "2":[["V2_SHELL","GENERAL","UNCONDITIONAL"],["V2_CMAKE","GENERAL","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0504:2","4":"DUPLICATE:N0504:2",
  "5":O+"IPC未单列冻结项。",
  "6":[["V2_CAN","GENERAL","EXAMPLE"],["V2_SPI","GENERAL","EXAMPLE"],["V2_UART","GENERAL","EXAMPLE"],["V2_RS485","GENERAL","EXAMPLE"]],
  "7":O+"瑞芯微未单列冻结项。","8":O+"全志未单列冻结项。","9":O+"STM32未单列冻结项。",
  "10":"DUPLICATE:N0504:6","11":"DUPLICATE:N0504:6","12":"DUPLICATE:N0504:6","13":"DUPLICATE:N0504:6",
  "14":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "15":"DUPLICATE:N0504:14",
  "16":[["V2_DDS","PREFERRED","UNCONDITIONAL"],["V2_USB","PREFERRED","UNCONDITIONAL"]],
  "17":"DUPLICATE:N0504:16","18":"DUPLICATE:N0504:16",
  "19":O+"MIPI未单列冻结项。","20":O+"蓝牙未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责足式机器人软件。git使用经验成立。C++拒收C。"
},
"N0511":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"ROBOT_AGENT_ALGO",
 "secondary_task":"",
 "task_evidence":"我们正在寻找机器人智能体算法工程师，负责大模型智能体、任务规划、技能调度和异常处理相关算法与系统研发，推动智能体能力在真实作业场景中的落地。",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","GENERAL","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0511:1",
  "3":O+"Tool Use未单列冻结项。",
  "4":"DUPLICATE:N0511:1",
  "5":O+"行为树未单列冻结项。","6":O+"状态机未单列冻结项。",
  "7":R+"C++不是C语言。",
  "8":[["V2_AGENT_WORKFLOW","PREFERRED","UNCONDITIONAL"]],
  "9":O+"Agent框架未单列冻结项。",
  "10":"DUPLICATE:N0511:8"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责机器人智能体算法。C++拒收C。"
},
"N0452":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"AGENT_INTERN",
 "secondary_task":"",
 "task_evidence":"1、参与 AI Agent 应用的开发和优化，包括任务规划、工具调用、记忆管理、工作流编排等",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":O+"OpenAI未单列冻结项。","3":O+"Claude未单列冻结项。","4":O+"Gemini未单列冻结项。",
  "5":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":R+"c++不是C语言。",
  "7":[["V2_AGENT_WORKFLOW","GENERAL","CHOICE"]],
  "8":[["V2_GIT","GENERAL","EXAMPLE"]],
  "9":O+"HTTP未单列冻结项。","10":O+"REST API未单列冻结项。",
  "11":"DUPLICATE:N0452:8"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"实习Agent应用。Git工具成立。模型API目录外。"
},
"N0483":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"OS_MIDDLEWARE_DDS",
 "secondary_task":"",
 "task_evidence":"架构与中间件设计：负责具身智能机器人软件架构设计，主导基于 ROS 2 / DDS 的通信中间件开发与优化，构建模块化、可扩展的系统框架。",
 "new":{
  "1":[["V2_DDS","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0483:1",
  "3":R+"C++不是C语言。",
  "4":[["V2_DDS","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0483:4",
  "6":[["V2_DDS","PREFERRED","CHOICE_AND_EXAMPLE"]],
  "7":"DUPLICATE:N0483:6",
  "8":O+"Iceoryx未单列冻结项。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责ROS2/DDS中间件。Iceoryx目录外。C++拒收C。"
},
"N0461":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI",
 "fine_task":"AGENT_CAMPUS_HIRE",
 "secondary_task":"",
 "task_evidence":"1. 参与 AI Agent 应用的开发和优化，包括任务规划、工具调用、记忆管理、工作流编排等；",
 "new":{
  "1":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":O+"OpenAI未单列冻结项。","3":O+"Claude未单列冻结项。","4":O+"Gemini未单列冻结项。",
  "5":[["V2_AGENT_WORKFLOW","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":R+"c++不是C语言。",
  "7":[["V2_AGENT_WORKFLOW","GENERAL","CHOICE"]],
  "8":[["V2_GIT","GENERAL","EXAMPLE"]],
  "9":O+"HTTP未单列冻结项。","10":O+"REST API未单列冻结项。",
  "11":"DUPLICATE:N0461:8"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"校招Agent开发。Git工具成立。"
},
"N0473":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME",
 "fine_task":"APP_MODULE_INTEGRATION",
 "secondary_task":"",
 "task_evidence":"1. 负责机器人端应用功能开发、维护及持续迭代，保障机器人软件稳定运行。",
 "new":{
  "1":R+"C++ 或 Python不是C语言。",
  "2":[["V2_DDS","GENERAL","CHOICE"],["V2_TCPIP","GENERAL","CHOICE"]],
  "3":"DUPLICATE:N0473:2","4":"DUPLICATE:N0473:2",
  "5":O+"HTTP未单列冻结项。","6":O+"WebSocket未单列冻结项。",
  "7":"DUPLICATE:N0473:2",
  "8":[["V2_GIT","GENERAL","UNCONDITIONAL"],["V2_CMAKE","GENERAL","UNCONDITIONAL"],["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0473:8","10":"DUPLICATE:N0473:8","11":"DUPLICATE:N0473:8"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责端侧应用集成。TCP/UDP按TCP/IP任选。C++/Python拒收C。"
}
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
