"""First-pass adjudication for deployment coding_order 1-16. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"E0388":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"APOLLO_DEMO","secondary_task":"",
 "task_evidence":"you will own the full lifecycle of Apollo demonstrations at our California office and at events worldwide",
 "new":{
  "1":R+"California office不是Microsoft Office。",
  "2":R+"satellite office不是Microsoft Office。",
  "3":R+"Application Engineering team office processes不是Microsoft Office。",
  "4":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"],["V2_MARKETING","SEPARATE","COLLABORATION_OBJECT"]],
  "5":R+"English can is not Controller Area Network.",
  "6":R+"English can is not Controller Area Network.",
  "7":R+"California office demonstration environment不是Microsoft Office。",
  "8":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "9":R+"C-suite visitors不是C语言。",
  "10":R+"English can is not Controller Area Network.",
  "11":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "12":R+"C++ is not the C language.",
  "13":[["V2_MARKETING","SEPARATE","COLLABORATION_OBJECT"]],
  "14":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"演示应用工程师。故障恢复保留。办公场地拒收Office。"
},
"E0245":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"MECH_CUSTOMIZATION","secondary_task":"",
 "task_evidence":"负责机器人产品的客户落地对接",
 "new":{
  "1":[["V2_CNC_PROCESS","GENERAL","CHOICE"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机械结构工程落地。CNC成型工艺保留。"
},
"N0181":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"FIELD_SUPPORT_BJ","secondary_task":"",
 "task_evidence":"支持具身智能机器人外场演示，现场场景搭建和软硬件调试，现场解决机器人问题",
 "new":{
  "1":[["V2_SHELL","GENERAL","CHOICE"]],
  "2":"DUPLICATE:N0181:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"现场支持。Shell保留。C++优先不记C。"
},
"N0689":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"APP_ENGINEER","secondary_task":"",
 "task_evidence":"Proficiency in Python and C++; strong working knowledge of ROS/ROS2.",
 "new":{
  "1":R+"Python and C++ is not the C language.",
  "2":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"应用工程师。C++拒收C。"
},
"N0776":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SERVICE_LEADERSHIP","fine_task":"FIELD_OPS_MGR","secondary_task":"",
 "task_evidence":"Develop repeatable processes, playbooks, tools, and operating standards for deployment readiness, commissioning, testing, troubleshooting",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "3":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"现场运营经理。故障排查保留。"
},
"N0885":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"FIELD_TECH","secondary_task":"",
 "task_evidence":"Conduct routine and incident maintenance for our Robot Fleet.",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":O+"wire and pcb soldering未单列冻结项。",
  "4":O+"electrical terminal crimping tools未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"现场服务技师。"
},
"N0943":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"FAR_MAINT","secondary_task":"",
 "task_evidence":"Troubleshoot and repair control systems including PLCs, motor controllers, embedded electronics, and sensor arrays",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_PLC","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0943:2",
  "4":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":R+"project teams不是Microsoft Project。",
  "6":R+"weekly priorities/assigning work不是Microsoft Project。",
  "7":R+"Develop project plans不是Microsoft Project。",
  "8":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "9":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "10":R+"project managers不是Microsoft Project。",
  "11":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "12":[["V2_PLC","PREFERRED","UNCONDITIONAL"]],
  "13":"DUPLICATE:N0943:12",
  "14":R+"洛杉矶县安全合作条款不是客服技能项。",
  "15":R+"招聘联系人不是人力资源技能项。",
  "16":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FAR维修专家。PLC/标定/故障排查保留。"
},
"N0858":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"FDE","secondary_task":"",
 "task_evidence":"Own and execute NPI software commissioning at customer sites, including tooling setup, system testing, and calibration.",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"English can is not Controller Area Network.",
  "3":R+"English can is not Controller Area Network.",
  "4":R+"Redwood City office不是Microsoft Office。",
  "5":[["V2_GRAFANA","DUTY_OWN_USE","CHOICE"],["V2_FOXGLOVE","DUTY_OWN_USE","CHOICE"],["V2_KIBANA","DUTY_OWN_USE","CHOICE"]],
  "6":O+"Portal/ArgoCD未单列冻结项。",
  "7":"DUPLICATE:N0858:5",
  "8":"DUPLICATE:N0858:5",
  "9":O+"ArgoCD未单列冻结项。",
  "10":"DUPLICATE:N0858:5",
  "11":[["V2_JIRA","DUTY_OWN_USE","CHOICE"],["V2_ZENDESK","DUTY_OWN_USE","CHOICE"]],
  "12":O+"SQL/NoSQL/container metrics未单列冻结项。",
  "13":"DUPLICATE:N0858:11",
  "14":"DUPLICATE:N0858:11",
  "15":[["V2_SHELL","DUTY_OWN_USE","UNCONDITIONAL"],["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "16":"DUPLICATE:N0858:15",
  "17":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "18":R+"Python or C++ is not the C language; large project不是Microsoft Project。",
  "19":[["V2_GRAFANA","GENERAL","CHOICE"],["V2_FOXGLOVE","GENERAL","CHOICE"],["V2_KIBANA","GENERAL","CHOICE"]],
  "20":"DUPLICATE:N0858:19",
  "21":"DUPLICATE:N0858:19",
  "22":"DUPLICATE:N0858:19",
  "23":O+"ArgoCD未单列冻结项。",
  "24":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"],["V2_TCPIP","GENERAL","UNCONDITIONAL"],["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "25":"DUPLICATE:N0858:24",
  "26":O+"VLANs未单列冻结项。",
  "27":O+"VPNs未单列冻结项。",
  "28":"DUPLICATE:N0858:24",
  "29":"DUPLICATE:N0858:24",
  "30":"DUPLICATE:N0858:24",
  "31":O+"RESTAPI未单列冻结项。",
  "32":[["V2_GIT","PREFERRED","UNCONDITIONAL"],["V2_GITHUB_ACTIONS","PREFERRED","CHOICE"],["V2_CI_CD","PREFERRED","UNCONDITIONAL"]],
  "33":"DUPLICATE:N0858:32",
  "34":O+"ArgoCD未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"前沿部署。Grafana/Foxglove/Kibana/Jira/Zendesk/云/TCPIP/GitHub Actions保留。"
},
"N0993":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"FIELD_REPAIR","secondary_task":"",
 "task_evidence":"troubleshoot, test, and repair complex robotic systems for our on-site Atlas fleet",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":O+"hand tools and torque wrenches未单列冻结项。",
  "3":"DUPLICATE:N0993:2",
  "4":[["V2_SHELL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0993:4",
  "6":O+"Ubuntu未单列冻结项。",
  "7":O+"Debian未单列冻结项。",
  "8":[["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0993:8",
  "10":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"现场维修。BASH保留。"
},
"E0453":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"APPRENTICE_RST","secondary_task":"",
 "task_evidence":"Perform routine maintenance and inspections of the humanoid robot fleet",
 "new":{
  "1":[["V2_TELEOP","SEPARATE","BACKGROUND"]],
  "2":[["V2_INCIDENT_SUPPORT","PREFERRED","UNCONDITIONAL"]],
  "3":R+"English can is not Controller Area Network.",
  "4":[["V2_GOOGLE_WORKSPACE","PREFERRED","UNCONDITIONAL"]],
  "5":[["V2_JIRA","PREFERRED","CHOICE"],["V2_CONFLUENCE","PREFERRED","CHOICE"]],
  "6":O+"torque tools未单列冻结项。",
  "7":"DUPLICATE:E0453:4",
  "8":"DUPLICATE:E0453:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"学徒维修。遥操为安全对象。Jira/Confluence/Google Suite保留。"
},
"N0907":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"MAINT_TECH","secondary_task":"",
 "task_evidence":"Read and interpret specifications, diagrams, manuals and other documentation such as standard operating procedures",
 "new":{
  "1":[["V2_SOP_OPERATION","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0907:2",
  "4":O+"Slack未单列冻结项。",
  "5":O+"Microsoft Visual Studio未单列冻结项。",
  "6":O+"Click Up未单列冻结项。",
  "7":R+"Series C funding不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"旧金山维修技师。SOP/Google Suite保留。"
},
"N0368":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SERVICE_LEADERSHIP","fine_task":"OVERSEAS_SERVICE_DIR","secondary_task":"",
 "task_evidence":"负责海外交付、售后服务与培训支持的整体运作",
 "new":{
  "1":[["V2_SOP_OPERATION","DUTY_OWN_USE","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"海外服务总监。SOP保留。"
},
"E0343":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"SOLUTIONS_ENG","secondary_task":"",
 "task_evidence":"Architect and execute complex integrations across robotic systems, customer APIs, sensors, and software",
 "new":{
  "1":[["V2_PLC","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"C++ is not the C language.",
  "3":R+"Salem office不是Microsoft Office。",
  "4":R+"Salary USD is not Universal Scene Description.",
  "5":R+"第三方招聘免责声明不是人力资源技能项。",
  "6":[["V2_TYPESCRIPT","GENERAL","CHOICE"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"方案工程师。PLC/TypeScript保留。"
},
"E0584":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"FDE_TRIAGE","secondary_task":"",
 "task_evidence":"Manage incoming fleet issue ticket queue, prioritize based on fleet-wide implications and operational goals",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_SHELL","GENERAL","CHOICE"]],
  "4":"DUPLICATE:E0584:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"前沿部署机器人。故障分诊与Bash保留。"
},
"N0498":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"AFTERSALES_REPAIR","secondary_task":"",
 "task_evidence":"负责四足机器人及相关配件的售后检测、故障诊断、维修处理和出厂测试工作",
 "new":{
  "1":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":R+"串口调试不是RS485。",
  "3":R+"串口不是RS485。",
  "4":O+"网口调试未单列冻结项。",
  "5":[["V2_CALIBRATION","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"售后维修。SOP/标零校准保留。串口不记RS485。"
},
"E0085":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"TECH_SUPPORT","secondary_task":"",
 "task_evidence":"负责对客户进行产品软硬件培训(硬件操作、软件使用以及二次开发等),完成设备交付",
 "new":{
  "1":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "2":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术支持。销售为协作对象。"
}
}
if __name__=='__main__':
 register('RF_DEPLOYMENT_FIELD_SERVICE', decisions, reader='grok4.6')
