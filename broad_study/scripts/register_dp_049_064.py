"""First-pass adjudication for deployment coding_order 49-64. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
FSE={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"FIELD_SERVICE_ENG","secondary_task":"",
 "task_evidence":"you will work to support our advanced Stretch Robotics in the field at",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"English can is not Controller Area Network.",
  "3":[["V2_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":"DUPLICATE:RID:3",
  "5":O+"power tools未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"现场服务工程师。CRM保留。"
}
def fse(rid, extra=None, evidence=None):
 d=dict(FSE); d['new']=dict(FSE['new'])
 d['new']['4']='DUPLICATE:%s:3'%rid
 if extra: d['new'].update(extra)
 if evidence: d['task_evidence']=evidence
 return d
FDE={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"FDE","secondary_task":"",
 "task_evidence":"Proficiency in Python, C++, Git, ROS.",
 "new":{
  "1":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "2":"DUPLICATE:RID:1",
  "3":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_JIRA","GENERAL","CHOICE"],["V2_CONFLUENCE","GENERAL","CHOICE"]],
  "5":"DUPLICATE:RID:4",
  "6":O+"Wrike未单列冻结项。",
  "7":"DUPLICATE:RID:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"前沿部署。Git/Jira/Confluence/故障排查保留。C++拒收C。"
}
def fde(rid, extra=None, evidence=None, n=7, notes=None):
 d=dict(FDE); d['new']=dict(FDE['new'])
 d['new']['2']='DUPLICATE:%s:1'%rid
 d['new']['5']='DUPLICATE:%s:4'%rid
 d['new']['7']='DUPLICATE:%s:4'%rid
 if extra: d['new'].update(extra)
 if evidence: d['task_evidence']=evidence
 if notes: d['notes']=notes
 return d
decisions={
"N1032":fse("N1032"),
"N1013":fse("N1013", extra={"5":O+"Windows未单列冻结项。","6":O+"power tools未单列冻结项。"}),
"N0857":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"FSE_DEX","secondary_task":"",
 "task_evidence":"peak performance in live customer warehouse environments",
 "new":{
  "1":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "2":"DUPLICATE:N0857:1",
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_RCA","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":O+"Linux/UNIX CLI未单列冻结项。",
  "7":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "8":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "9":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "10":O+"UNIX未单列冻结项。",
  "11":[["V2_INCIDENT_SUPPORT","PREFERRED","UNCONDITIONAL"]],
  "12":R+"GitHub寻访/托管不是Git协作。",
  "13":[["V2_JIRA","PREFERRED","CHOICE"],["V2_GOOGLE_WORKSPACE","PREFERRED","CHOICE"],["V2_ZENDESK","PREFERRED","CHOICE"]],
  "14":"DUPLICATE:N0857:13",
  "15":"DUPLICATE:N0857:13",
  "16":"DUPLICATE:N0857:13",
  "17":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Dexterity现场服务。世界模型为产品背景。GitHub不记Git。"
},
"N0853":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"APP_SUPPORT","secondary_task":"",
 "task_evidence":"Own and execute NPI software commissioning at customer sites, including tooling setup, system testing, and calibration.",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"English can is not Controller Area Network.",
  "3":R+"Redwood City office不是Microsoft Office。",
  "4":[["V2_GRAFANA","DUTY_OWN_USE","CHOICE"],["V2_FOXGLOVE","DUTY_OWN_USE","CHOICE"],["V2_KIBANA","DUTY_OWN_USE","CHOICE"]],
  "5":O+"Portal/ArgoCD未单列冻结项。",
  "6":"DUPLICATE:N0853:4",
  "7":"DUPLICATE:N0853:4",
  "8":O+"ArgoCD未单列冻结项。",
  "9":"DUPLICATE:N0853:4",
  "10":[["V2_JIRA","DUTY_OWN_USE","CHOICE"],["V2_ZENDESK","DUTY_OWN_USE","CHOICE"]],
  "11":O+"SQL/NoSQL/container metrics未单列冻结项。",
  "12":"DUPLICATE:N0853:10",
  "13":"DUPLICATE:N0853:10",
  "14":[["V2_SHELL","DUTY_OWN_USE","UNCONDITIONAL"],["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "15":"DUPLICATE:N0853:14",
  "16":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "17":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"],["V2_TCPIP","GENERAL","UNCONDITIONAL"],["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "18":"DUPLICATE:N0853:17",
  "19":O+"VLANs未单列冻结项。",
  "20":O+"VPNs未单列冻结项。",
  "21":"DUPLICATE:N0853:17",
  "22":"DUPLICATE:N0853:17",
  "23":"DUPLICATE:N0853:17",
  "24":[["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "25":"DUPLICATE:N0853:24",
  "26":[["V2_GRAFANA","GENERAL","CHOICE"],["V2_FOXGLOVE","GENERAL","CHOICE"],["V2_KIBANA","GENERAL","CHOICE"]],
  "27":"DUPLICATE:N0853:26",
  "28":"DUPLICATE:N0853:26",
  "29":"DUPLICATE:N0853:26",
  "30":O+"ArgoCD未单列冻结项。",
  "31":[["V2_CALIBRATION","GENERAL","UNCONDITIONAL"]],
  "32":O+"RESTAPI未单列冻结项。",
  "33":[["V2_GIT","PREFERRED","UNCONDITIONAL"],["V2_GITHUB_ACTIONS","PREFERRED","CHOICE"],["V2_CI_CD","PREFERRED","UNCONDITIONAL"]],
  "34":"DUPLICATE:N0853:33",
  "35":O+"ArgoCD未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"应用支持。Grafana/Foxglove/Kibana/Jira/Zendesk/云/TCPIP/GitHub Actions保留。"
},
"N0879":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SERVICE_LEADERSHIP","fine_task":"PRODUCT_SERVICE_MGR","secondary_task":"",
 "task_evidence":"Lead issue triage across electrical, mechanical, and electromechanical subsystems with support from HQ engineering.",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"English can is not Controller Area Network.",
  "3":R+"Redwood City office不是Microsoft Office。",
  "4":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"],["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "7":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_JIRA","GENERAL","CHOICE"],["V2_ZENDESK","GENERAL","CHOICE"]],
  "9":"DUPLICATE:N0879:8",
  "10":"DUPLICATE:N0879:8",
  "11":[["V2_GRAFANA","GENERAL","CHOICE"],["V2_FOXGLOVE","GENERAL","CHOICE"],["V2_KIBANA","GENERAL","CHOICE"]],
  "12":"DUPLICATE:N0879:11",
  "13":"DUPLICATE:N0879:11",
  "14":"DUPLICATE:N0879:11",
  "15":O+"ArgoCD未单列冻结项。",
  "16":[["V2_ETHERCAT","PREFERRED","UNCONDITIONAL"]],
  "17":"DUPLICATE:N0879:16",
  "18":O+"Beckhoff未单列冻结项。",
  "19":O+"Elmo未单列冻结项。",
  "20":[["V2_CALIBRATION","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"产品服务经理。EtherCAT/Jira/Zendesk/观测工具保留。"
},
"N0767":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"FSE_IRVINE","secondary_task":"",
 "task_evidence":"you will be a key technical link between FieldAI’s robotics platform, our customers, and our engineering team",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_SHELL","GENERAL","UNCONDITIONAL"],["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "7":O+"SSH未单列冻结项。",
  "8":"DUPLICATE:N0767:6",
  "9":O+"RMAs未单列冻结项。",
  "10":[["V2_JIRA","PREFERRED","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0767:10"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Irvine现场服务。标定/Shell/Jira保留。"
},
"N0752":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"FAE_JP","secondary_task":"",
 "task_evidence":"This role serves as a primary technical point of contact between customers, field operations, and engineering teams.",
 "new":{
  "1":R+"technical point of contact不是Microsoft Project。",
  "2":R+"deployment plans/project timelines不是Microsoft Project。",
  "3":R+"successful project outcomes不是Microsoft Project。",
  "4":R+"project status discussions不是Microsoft Project。",
  "5":R+"Python, C++, or similar is not the C language.",
  "6":R+"Project Management标题不是Microsoft Project。",
  "7":R+"Strong project management skills不是Microsoft Project。",
  "8":R+"project updates不是Microsoft Project。",
  "9":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"日本FAE。项目管理不记MS Project。"
},
"N0756":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"FAE_SG","secondary_task":"",
 "task_evidence":"Field Application Engineer to support the deployment, testing, and client-facing operations",
 "new":{
  "1":R+"Office-Based不是Microsoft Office。",
  "2":R+"Field Application Engineer不是Microsoft Project。",
  "3":R+"Singapore office不是Microsoft Office。",
  "4":R+"Python, C++, or similar is not the C language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"新加坡FAE。"
},
"N0770":fde("N0770", extra={"8":R+"U.S. government project不是C语言。","9":R+"onsite collaboration不是Microsoft Office。"}),
"N0811":fde("N0811", extra={"8":R+"U.S. government project不是C语言。"}, evidence="Proficiency in Python, C++, Git, ROS/ROS2"),
"N0768":fde("N0768"),
"N0805":fde("N0805", extra={"8":R+"U.S. government project不是C语言。","9":R+"onsite collaboration不是Microsoft Office。"}, evidence="Proficiency in Python, C++, Git, ROS."),
"N0794":fde("N0794", extra={"8":R+"U.S. government project不是C语言。","9":R+"onsite collaboration不是Microsoft Office。"}),
"N0765":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"FAE_TOKYO","secondary_task":"",
 "task_evidence":"Basic coding/scripting skills (Python, C++, or similar).",
 "new":{
  "1":R+"Python, C++, or similar is not the C language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"东京FAE。"
},
"N0769":fde("N0769"),
"N0783":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"NETWORK_SOLUTIONS","secondary_task":"",
 "task_evidence":"own the network backbone that keeps our robots online, mission-ready, and connected",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":O+"Wi-Fi未单列冻结项。",
  "5":O+"DFS未单列冻结项。",
  "6":O+"LTE未单列冻结项。",
  "7":O+"5G未单列冻结项。",
  "8":O+"APN未单列冻结项。",
  "9":O+"subnets/VLANs未单列冻结项。",
  "10":O+"DHCP未单列冻结项。",
  "11":O+"DNS未单列冻结项。",
  "12":O+"NAT未单列冻结项。",
  "13":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "14":O+"SSH未单列冻结项。",
  "15":[["V2_SHELL","PREFERRED","UNCONDITIONAL"]],
  "16":"DUPLICATE:N0783:15"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"网络方案。故障排查/Bash保留。DFS是动态频率选择不记可测试性。"
}
}
if __name__=='__main__':
 register('RF_DEPLOYMENT_FIELD_SERVICE', decisions, reader='grok4.6')
