"""First-pass adjudication for deployment coding_order 65-85. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
RST={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"ROBOT_SVC_TECH","secondary_task":"",
 "task_evidence":"Proficient in troubleshooting mechanical, electrical and software-based issues",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_DAQ","PREFERRED","UNCONDITIONAL"]],
  "4":[["V2_JIRA","PREFERRED","CHOICE"],["V2_CONFLUENCE","PREFERRED","CHOICE"]],
  "5":"DUPLICATE:RID:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"人形服务技师。DAQ/Google Suite/Jira/Confluence保留。"
}
def rst(rid, extra=None, notes=None):
 d=dict(RST); d['new']=dict(RST['new']); d['new']['5']='DUPLICATE:%s:4'%rid
 if extra: d['new'].update(extra)
 if notes: d['notes']=notes
 return d
NIM={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FACILITY","fine_task":"MAINT_TECH","secondary_task":"",
 "task_evidence":"Read and interpret specifications, diagrams, manuals and other documentation such as standard operating procedures",
 "new":{
  "1":[["V2_SOP_OPERATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "3":"DUPLICATE:RID:2",
  "4":O+"Slack未单列冻结项。",
  "5":O+"Microsoft Visual Studio未单列冻结项。",
  "6":O+"Click Up未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Nimble维护技师。SOP/Google Suite保留。"
}
def nim(rid, extra=None, n=6):
 d=dict(NIM); d['new']=dict(NIM['new']); d['new']['3']='DUPLICATE:%s:2'%rid
 if extra: d['new'].update(extra)
 return d
decisions={
"N0778":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_INTEGRATION","fine_task":"MAPPING_SOLUTIONS","secondary_task":"",
 "task_evidence":"owning deployment, integration, and ongoing performance in the field",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"English can is not Controller Area Network.",
  "3":R+"C++ and Python is not the C language.",
  "4":O+"ICP未单列冻结项。",
  "5":O+"NDT未单列冻结项。",
  "6":[["V2_PCL","GENERAL","CHOICE"],["V2_OPEN3D","GENERAL","CHOICE"]],
  "7":"DUPLICATE:N0778:6",
  "8":"DUPLICATE:N0778:6",
  "9":O+"PCD未单列冻结项。",
  "10":O+"PLY未单列冻结项。",
  "11":O+"E57未单列冻结项。",
  "12":O+"LAS未单列冻结项。",
  "13":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "14":"DUPLICATE:N0778:13",
  "15":O+"Ubuntu未单列冻结项。",
  "16":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "17":[["V2_CALIBRATION","PREFERRED","UNCONDITIONAL"]],
  "18":O+"CloudCompare未单列冻结项。",
  "19":O+"Leica Cyclone未单列冻结项。",
  "20":O+"Faro Scene未单列冻结项。",
  "21":O+"Trimble RealWorks未单列冻结项。",
  "22":[["V2_JIRA","PREFERRED","CHOICE"],["V2_CONFLUENCE","PREFERRED","CHOICE"]],
  "23":"DUPLICATE:N0778:22",
  "24":O+"Wrike未单列冻结项。",
  "25":"DUPLICATE:N0778:22",
  "26":R+"English can is not Controller Area Network."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"测绘方案。PCL/Open3D/Git/Jira/Confluence/标定保留。项目管理工具不记MS Project。"
},
"E0547":rst("E0547"),
"E0515":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FACILITY","fine_task":"MFG_EQUIP_TECH","secondary_task":"",
 "task_evidence":"Provide technician-level support for all manufacturing equipment",
 "new":{
  "1":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_DOE_MSA","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":O+"Forklift certification未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"制造设备技师。SOP/gauge R&R保留。"
},
"E0545":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"REMAN_TECH","secondary_task":"",
 "task_evidence":"Repairing full robots and smaller sub-assemblies for F.03 high volume manufacturing",
 "new":{
  "1":R+"corporate or in-home tasks不是Microsoft Office。",
  "2":[["V2_GOOGLE_WORKSPACE","GENERAL","CHOICE"],["V2_CONFLUENCE","GENERAL","CHOICE"],["V2_JIRA","GENERAL","CHOICE"]],
  "3":"DUPLICATE:E0545:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"再制造技师。Google Suite/Jira/Confluence保留。"
},
"E0471":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FACILITY","fine_task":"FACILITIES_TECH","secondary_task":"",
 "task_evidence":"Perform routine inspections, maintenance, and repairs on building systems such as HVAC, electrical, plumbing, and fire safety systems.",
 "new":{
  "1":R+"corporate or in-home tasks不是Microsoft Office。",
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_OFFICE","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:E0471:3",
  "6":O+"EPA Universal/HVAC certifications未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"设施技师。Microsoft Office Suite保留。"
},
"E0546":rst("E0546"),
"E0548":rst("E0548"),
"E0564":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"STAGING_SPECIALIST","secondary_task":"",
 "task_evidence":"Set up and configure collection home environments, including furniture arrangement, prop placement, and scene staging",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":O+"Forklift certification未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"采集布景专员。"
},
"E0557":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SERVICE_LEADERSHIP","fine_task":"SITE_LEAD","secondary_task":"",
 "task_evidence":"Daily onsite production operations",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"商用现场主管。无新候选。"
},
"E0472":rst("E0472", extra={
  "5":"DUPLICATE:E0472:2",
  "6":O+"Current Probes未单列冻结项。",
  "7":O+"PCB Rework未单列冻结项。",
  "8":"DUPLICATE:E0472:4"
}, notes="商用现场服务技师。DAQ/Google Suite/Jira/Confluence保留。"),
"E0462":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"DEPLOY_ENG_DATA","secondary_task":"",
 "task_evidence":"Provide hands-on support to collection team to unblock technical issues",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_SALES_CRM","PREFERRED","UNCONDITIONAL"]],
  "5":[["V2_JIRA","GENERAL","CHOICE"],["V2_CONFLUENCE","GENERAL","CHOICE"]],
  "6":"DUPLICATE:E0462:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据采集部署工程师。故障排查/Jira/Confluence保留。项目管理软件不记MS Project。"
},
"E0570":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"TECH_COORD_SP","secondary_task":"",
 "task_evidence":"Fazer o troubleshooting (diagnóstico e resolução de falhas) de primeira linha em problemas de hardware e captura",
 "new":{
  "1":R+"葡萄牙语正文匹配不是C语言。",
  "2":R+"采集设备维护不是功能安全分析，也不是C语言。",
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CALIBRATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "5":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_MOCAP","PREFERRED","UNCONDITIONAL"]],
  "8":R+"CMMS不是三坐标CMM。",
  "9":"DUPLICATE:E0570:8"
 },
 "old_overrides":{
  "O4":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原库存短词不唯一，改为CMMS/库存系统整句。","quote":"Experiência construindo ou operando sistemas de inventário, controle de ativos ou gestão de manutenção (CMMS)."},
  "O5":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原资产控制短词不唯一，改为CMMS/库存系统整句。","quote":"operando sistemas de inventário, controle de ativos ou gestão de manutenção (CMMS)"},
  "O9":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"SKILL_REQUIREMENT","reason":"原firmware短词多处出现，改为分层排障句。","quote":"capacidade de isolar falhas entre as camadas de hardware, cabeamento, firmware e software."}
 },
 "additions":[],"outside_extra":[],
 "notes":"圣保罗数据技术协调。动捕/SOP/标定保留。CMMS不记CMM。库存与固件继承改写。"
},
"E0558":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SERVICE_LEADERSHIP","fine_task":"SITE_LEAD_NIGHT","secondary_task":"",
 "task_evidence":"Onsite humanoid fleet service & maintenance",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"夜班现场主管。无新候选。"
},
"E0569":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"TECH_COORD_CDMX","secondary_task":"",
 "task_evidence":"Realizar el troubleshooting (diagnóstico y resolución de fallas) de primera línea en problemas de hardware y captura",
 "new":{
  "1":R+"西班牙语正文匹配不是C语言。",
  "2":R+"西班牙语正文匹配不是C语言。",
  "3":R+"采集设备维护不是功能安全分析，也不是C语言。",
  "4":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CALIBRATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "8":R+"西班牙语正文匹配不是C语言。",
  "9":[["V2_MOCAP","PREFERRED","UNCONDITIONAL"]],
  "10":R+"CMMS不是三坐标CMM。",
  "11":"DUPLICATE:E0569:10"
 },
 "old_overrides":{
  "O4":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原库存短词不唯一，改为CMMS/库存系统整句。","quote":"Experiencia construyendo u operando sistemas de inventario, control de activos o gestión de mantenimiento (CMMS)."},
  "O5":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原资产控制短词不唯一，改为CMMS/库存系统整句。","quote":"operando sistemas de inventario, control de activos o gestión de mantenimiento (CMMS)"},
  "O9":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"SKILL_REQUIREMENT","reason":"原firmware短词多处出现，改为分层排障句。","quote":"capacidad de aislar fallas entre las capas de hardware, cableado, firmware y software."}
 },
 "additions":[],"outside_extra":[],
 "notes":"墨西哥城数据技术协调。动捕/SOP/标定保留。CMMS不记CMM。库存与固件继承改写。"
},
"N0906":nim("N0906"),
"N0908":nim("N0908", extra={
  "6":O+"command prompts未单列冻结项。",
  "7":O+"Click Up未单列冻结项。",
  "8":R+"Series C funding is not the C language."
}),
"N0904":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SERVICE_LEADERSHIP","fine_task":"MAINT_SUPERVISOR","secondary_task":"",
 "task_evidence":"Enforce strict adherence to safety procedures, OSHA codes, and standard operating procedures (SOPs)",
 "new":{
  "1":R+"Series C funding is not the C language.",
  "2":[["V2_SOP_OPERATION","DUTY_OWN_USE","UNCONDITIONAL"],["V2_SAFETY_OPERATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0904:2",
  "4":R+"English can is not Controller Area Network.",
  "5":[["V2_PLC","PREFERRED","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0904:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"自动化履约维护主管。SOP/作业安全/PLC保留。"
},
"N0905":nim("N0905"),
"E0600":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"ROBOTICS_TECH","secondary_task":"",
 "task_evidence":"Proficiency in troubleshooting and repairing electrical systems (AC/DC motors, wiring, controllers) and mechanical components",
 "new":{
  "1":R+"整机电源维修不是测试电源与负载。",
  "2":[["V2_NOTION","DUTY_OWN_USE","CHOICE"],["V2_LINEAR","DUTY_OWN_USE","CHOICE"]],
  "3":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_PLC","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:E0600:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人技师。Notion/Linear/PLC/排障保留。"
},
"E0598":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LAB_DEMO","fine_task":"APPLIED_RESEARCH_DEPLOY","secondary_task":"",
 "task_evidence":"Deploy and debug learned policies on physical robots, diagnosing failures across the full stack",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"应用研究员现场部署。无新候选。"
},
"N0695":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_SERVICE","fine_task":"ROBOTICS_TECH","secondary_task":"",
 "task_evidence":"Communicate technical findings clearly and contribute to documentation, repair manuals, and troubleshooting guides.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_LOOKER","DUTY_OWN_DEVELOP","CHOICE"],["V2_TABLEAU","DUTY_OWN_DEVELOP","CHOICE"]],
  "3":"DUPLICATE:N0695:2",
  "4":"DUPLICATE:N0695:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人技师。Looker/Tableau/排障文档保留。"
}
}
if __name__=='__main__':
 register('RF_DEPLOYMENT_FIELD_SERVICE', decisions, reader='grok4.6')
