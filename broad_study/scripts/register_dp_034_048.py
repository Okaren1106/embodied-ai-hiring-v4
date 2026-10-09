"""First-pass adjudication for deployment coding_order 34-48. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
TSE={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"TECH_SUPPORT_ENG","secondary_task":"",
 "task_evidence":"Helps establish, document, and assist in principled technical support processes",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "5":R+"Python/C++ is not the C language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术支持。故障排查保留。C++拒收C。"
}
def tse(rid):
 d=dict(TSE); d['new']=dict(TSE['new'])
 return d
decisions={
"E0187":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"HUMANOID_REPAIR","secondary_task":"",
 "task_evidence":"负责人形机器人整机及核心部件(机械臂、线束、传感器、软件等)故障维修、拆机检测、问题定位",
 "new":{
  "1":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_SOP_OPERATION","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"人形维修。SOP/故障排查保留。"
},
"E0131":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"JOINT_TEST","secondary_task":"",
 "task_evidence":"负责模组试验台架的搭建,包括机械安装、水电气连接、高低压线束连接",
 "new":{
  "1":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_LEAN","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_HAND_METROLOGY","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"关节模组测试。计量校准/5S/卡尺保留。"
},
"E0105":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"SERVICEABILITY","secondary_task":"",
 "task_evidence":"主导产品可服务性(DFS)全周期管理",
 "new":{
  "1":R+"轻量化问题分析工具不是模型压缩。",
  "2":[["V2_CUSTOMER_SERVICE","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"产品应用。客户服务保留。"
},
"E0340":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"SERVICE_TECH_II","secondary_task":"",
 "task_evidence":"Support the service operations for all robots, including troubleshooting and repairing both robots and their peripherals",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CUSTOMER_SERVICE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_MES","PREFERRED","UNCONDITIONAL"]],
  "5":[["V2_JIRA","PREFERRED","CHOICE"],["V2_CONFLUENCE","PREFERRED","CHOICE"]],
  "6":R+"project improvement methodologies不是Microsoft Project。",
  "7":[["V2_GOOGLE_WORKSPACE","PREFERRED","UNCONDITIONAL"]],
  "8":R+"physical demands of this office role不是Microsoft Office。",
  "9":R+"Salem office不是Microsoft Office。",
  "10":R+"Salary USD is not Universal Scene Description.",
  "11":R+"第三方招聘免责声明不是人力资源技能项。",
  "12":"DUPLICATE:E0340:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"高级服务技师。MES/Jira/Confluence/Google Suite保留。"
},
"N1043":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"FLEET_CAPTAIN","secondary_task":"",
 "task_evidence":"The Fleet Operations Robot Captain is the mission lead for robot health, uptime, and utilization.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_JIRA","GENERAL","CHOICE"],["V2_TABLEAU","GENERAL","CHOICE"]],
  "6":"DUPLICATE:N1043:5",
  "7":"DUPLICATE:N1043:5",
  "8":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "9":R+"project success不是Microsoft Project。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"车队Robot Captain。Jira/Tableau/故障分诊保留。"
},
"N0989":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"RMAC_APP_LEAD","secondary_task":"",
 "task_evidence":"you will lead the primary engineering team at the Robotic Mobile Application Center (RMAC)",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"Python, C++, or scripting is not the C language.",
  "3":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_JIRA","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0989:4",
  "6":[["V2_TABLEAU","GENERAL","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0989:6"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"RMAC应用负责人。Jira/Tableau保留。"
},
"N1026":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"STAFF_FAE","secondary_task":"",
 "task_evidence":"you will spearhead the delivery of our Enterprise Robotics Integration Program model for Boston Dynamics",
 "new":{
  "1":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "2":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "3":R+"CMMS不是三坐标CMM。",
  "4":R+"CMMS不是三坐标CMM。",
  "5":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":R+"ensuring alignment不是Microsoft Project。",
  "7":R+"Python or C++ APIs is not the C language.",
  "8":O+"VLANs未单列冻结项。",
  "9":O+"VPNs未单列冻结项。",
  "10":R+"English can is not Controller Area Network."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Staff FAE。销售协作保留。CMMS不记CMM。"
},
"N0997":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SERVICE_LEADERSHIP","fine_task":"PROTOTYPE_FLEET_DIR","secondary_task":"",
 "task_evidence":"responsible for the full lifecycle of the Atlas robot fleet after it leaves the production line",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_LEAN","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0997:5",
  "7":R+"English can is not Controller Area Network.",
  "8":R+"English can is not Controller Area Network.",
  "9":[["V2_LEAN","GENERAL","UNCONDITIONAL"]],
  "10":"DUPLICATE:N0997:9"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"原型车队维修总监。Lean/故障流程保留。"
},
"N0992":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"FIELD_REPAIR_2ND","secondary_task":"",
 "task_evidence":"troubleshoot, test, and repair complex robotic systems for our on-site Atlas fleet",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":O+"hand tools and torque wrenches未单列冻结项。",
  "3":"DUPLICATE:N0992:2",
  "4":[["V2_SHELL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0992:4",
  "6":O+"Ubuntu未单列冻结项。",
  "7":O+"Debian未单列冻结项。",
  "8":[["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0992:8",
  "10":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"现场维修二班。BASH保留。"
},
"N1028":tse("N1028"),
"N1018":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"FAE_FR","secondary_task":"",
 "task_evidence":"The Senior Field Application Engineer serves as a key technical resource for Boston Dynamics' Certified Integrator initiative.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":O+"BD APIs/SDKs未单列冻结项。",
  "3":"DUPLICATE:N1018:2",
  "4":R+"project managers不是Microsoft Project。",
  "5":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "6":R+"Technical Project Management不是Microsoft Project。",
  "7":O+"firewalls未单列冻结项。",
  "8":O+"VPNs未单列冻结项。",
  "9":O+"VLANs未单列冻结项。",
  "10":O+"routers未单列冻结项。",
  "11":O+"switches未单列冻结项。",
  "12":O+"Linux Ubuntu systems management未单列冻结项。",
  "13":[["V2_TYPESCRIPT","GENERAL","CHOICE"]],
  "14":"DUPLICATE:N1018:13",
  "15":O+"Kotlin未单列冻结项。",
  "16":[["V2_AUTOCAD","PREFERRED","UNCONDITIONAL"]],
  "17":"DUPLICATE:N1018:16"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"法语FAE。TypeScript/AutoCAD/故障排查保留。C++拒收C。"
},
"N1030":tse("N1030"),
"N1029":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"FLEET_APP_ENG","secondary_task":"",
 "task_evidence":"Perform rapid system-level troubleshooting across controls, software, hardware, networking, sensors, power systems, and infrastructure.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "8":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "9":R+"English can is not Controller Area Network.",
  "10":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "11":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "12":[["V2_JIRA","GENERAL","CHOICE"]],
  "13":"DUPLICATE:N1029:12",
  "14":O+"ServiceNow未单列冻结项。",
  "15":[["V2_INCIDENT_SUPPORT","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"车队应用工程师。故障响应与Jira保留。"
},
"N1033":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"OPS_TECH_IV","secondary_task":"",
 "task_evidence":"Lead troubleshooting across mechanical, electrical, and software systems.",
 "new":{
  "1":R+"Infrastructure & Project Ownership不是Microsoft Project。",
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"project and operational documentation不是Microsoft Project。",
  "4":[["V2_AUTOCAD","PREFERRED","UNCONDITIONAL"]],
  "5":"DUPLICATE:N1033:4",
  "6":O+"command-line systems未单列冻结项。",
  "7":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "8":O+"driver’s license未单列冻结项。",
  "9":[["V2_ADOBE_CREATIVE","PREFERRED","UNCONDITIONAL"]],
  "10":"DUPLICATE:N1033:9",
  "11":O+"Forklift未单列冻结项。",
  "12":O+"scissor lift certification未单列冻结项。",
  "13":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"运营技师。AutoCAD/Adobe/故障排查保留。"
},
"N1006":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"RMAC_INTEGRATION","secondary_task":"",
 "task_evidence":"you will serve as the engineering resource driving the transition of the Atlas humanoid robot into production-level",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_JIRA","GENERAL","UNCONDITIONAL"]],
  "4":"DUPLICATE:N1006:3",
  "5":[["V2_TABLEAU","GENERAL","UNCONDITIONAL"]],
  "6":"DUPLICATE:N1006:5",
  "7":R+"Python, C++, or scripting is not the C language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"RMAC集成。Jira/Tableau保留。"
}
}
if __name__=='__main__':
 register('RF_DEPLOYMENT_FIELD_SERVICE', decisions, reader='grok4.6')
