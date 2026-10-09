"""First-pass adjudication for corporate-support coding_order 97-112. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"E0314":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"FP_A_MANAGER","secondary_task":"",
 "task_evidence":"The Financial Planning and Analysis Manager will be responsible for developing insightful analyses",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_OFFICE","GENERAL","UNCONDITIONAL"],["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "3":R+"Salary USD is not Universal Scene Description.",
  "4":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{
  "O2":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Excel短词定位为空，改为Excel与Google Sheets句。","quote":"including expertise in Excel & Google Sheets"}
 },
 "additions":[],"outside_extra":[],
 "notes":"FP&A经理。Microsoft Office/Google Suite保留。"
},
"E0304":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"ACCOUNTANT_III","secondary_task":"",
 "task_evidence":"Drive the monthly and year-end financial close processes",
 "new":{
  "1":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"Fremont office location is not Microsoft Office.",
  "3":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_NETSUITE","PREFERRED","UNCONDITIONAL"]],
  "6":R+"Salary USD is not Universal Scene Description.",
  "7":R+"第三方招聘免责声明不是人力资源技能项。",
  "8":"DUPLICATE:E0304:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"会计师。NetSuite/Google Sheets保留。"
},
"E0324":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"SENIOR_EA","secondary_task":"",
 "task_evidence":"Manage complex calendars, meetings, travel, and communications with precision, discretion, and foresight.",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_ASANA","GENERAL","UNCONDITIONAL"],["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "3":R+"Salary USD is not Universal Scene Description.",
  "4":R+"第三方招聘免责声明不是人力资源技能项。",
  "5":"DUPLICATE:E0324:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"高级行政助理。Asana/Google Workspace保留。"
},
"E0315":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"IR_HEAD","secondary_task":"MARKETING",
 "task_evidence":"Develop and lead the company’s overall investor relations strategy",
 "new":{
  "1":[["V2_MARKETING","SEPARATE","COLLABORATION_OBJECT"]],
  "2":[["V2_ACCOUNTING_CREDENTIAL","PREFERRED","CHOICE"]],
  "3":R+"Salary USD is not Universal Scene Description.",
  "4":R+"第三方招聘免责声明不是人力资源技能项。",
  "5":"DUPLICATE:E0315:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"IR负责人。CFA优先。市场法务为协作对象。"
},
"E0353":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"TECH_SOURCER","secondary_task":"",
 "task_evidence":"Own sourcing strategy and execution for software, hardware, robotics, and AI engineering roles.",
 "new":{
  "1":R+"人才寻访sourcing不是采购职责。",
  "2":R+"人才寻访sourcing不是采购职责。",
  "3":R+"面试校准candidate profiles不是传感器标定；寻访不是采购。",
  "4":R+"GitHub寻访渠道不是Git协作；寻访不是采购。",
  "5":R+"人才寻访sourcing不是采购职责。",
  "6":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":R+"人才寻访sourcing不是采购职责。",
  "8":R+"人才寻访sourcing不是采购职责。",
  "9":R+"人才寻访sourcing不是采购职责。",
  "10":R+"GitHub寻访渠道不是Git协作；寻访不是采购。",
  "11":R+"人才寻访sourcing不是采购职责。",
  "12":R+"人才寻访sourcing不是采购职责。",
  "13":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "14":R+"人才寻访sourcing不是采购职责。",
  "15":R+"Salary USD is not Universal Scene Description.",
  "16":R+"第三方招聘免责声明不是人力资源技能项。",
  "17":R+"GitHub寻访渠道不是Git协作。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术寻访。寻访不记采购，GitHub不记Git。"
},
"E0352":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"TECH_RECRUITER","secondary_task":"",
 "task_evidence":"Manage full-cycle recruiting for software and hardware engineering roles, from intake through offer acceptance.",
 "new":{
  "1":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"人才寻访sourcing不是采购职责。",
  "5":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_HR","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "7":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "9":R+"人才寻访sourcing不是采购职责。",
  "10":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "11":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "12":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "13":R+"Salary USD is not Universal Scene Description.",
  "14":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术招聘。寻访不记采购。"
},
"E0309":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"TECHNICAL_ACCOUNTING_DIR","secondary_task":"",
 "task_evidence":"Serve as the subject matter expert on key areas including revenue recognition (ASC 606), leases (ASC 842), stock-based compensation (ASC 718)",
 "new":{
  "1":[["V2_NETSUITE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_NETSUITE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_NETSUITE","DUTY_OWN_USE","UNCONDITIONAL"],["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "8":R+"业务部门招人不是人力资源技能项。",
  "9":[["V2_NETSUITE","PREFERRED","UNCONDITIONAL"]],
  "10":R+"Fremont office location is not Microsoft Office.",
  "11":R+"Salary USD is not Universal Scene Description.",
  "12":R+"第三方招聘免责声明不是人力资源技能项。",
  "13":"DUPLICATE:E0309:9"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术会计总监。NetSuite保留。"
},
"E0316":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"ACCOUNTING_MANAGER","secondary_task":"",
 "task_evidence":"We are seeking an experienced Accounting Manager to lead the general accounting function",
 "new":{
  "1":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_OFFICE","GENERAL","UNCONDITIONAL"]],
  "5":R+"Fremont office location is not Microsoft Office.",
  "6":R+"Salary USD is not Universal Scene Description.",
  "7":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"会计经理。Microsoft Excel/Office保留。"
},
"E0372":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"TOTAL_REWARDS_DIR","secondary_task":"",
 "task_evidence":"Lead compensation cycles (merit, equity refresh, promotions), including modeling, calibration, and manager communications",
 "new":{
  "1":R+"薪酬校准calibration不是传感器标定。",
  "2":O+"Radford未单列冻结项。",
  "3":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"C-suite不是C语言。",
  "5":[["V2_HR_CREDENTIAL","PREFERRED","CHOICE"]],
  "6":"DUPLICATE:E0372:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"总薪酬总监。HR认证保留。"
},
"E0450":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"WORKPLACE_XP","secondary_task":"",
 "task_evidence":"The Workplace Experience Manager owns the day-to-day experience and operation of Apptronik's Sunnyvale site",
 "new":{
  "1":R+"办公场地与C-suite不是Microsoft Office或C语言。",
  "2":[["V2_HR","SEPARATE","COLLABORATION_OBJECT"]],
  "3":R+"前台办公场地不是Microsoft Office。",
  "4":R+"C-suite不是C语言。",
  "5":[["V2_JIRA","GENERAL","EXAMPLE"]],
  "6":R+"workplace/office administration不是Microsoft Office。",
  "7":R+"move throughout the office不是Microsoft Office。",
  "8":R+"office supplies不是Microsoft Office。",
  "9":O+"Envoy/VMS未单列冻结项。",
  "10":"DUPLICATE:E0450:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"职场体验经理。Jira保留。办公场地拒收Office。"
},
"E0400":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"TECHNICAL_ACCOUNTING_SM","secondary_task":"",
 "task_evidence":"Serve as the Company's subject matter expert on U.S. GAAP and lead the research, interpretation, and application of complex accounting standards",
 "new":{
  "1":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_ACCOUNTING","REQUIRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术会计高级经理。CPA记会计。"
},
"E0370":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"TAX_MANAGER","secondary_task":"",
 "task_evidence":"previous experience in preparation of federal income tax provisions",
 "new":{
  "1":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "2":O+"Avatax未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"税务经理。"
},
"E0449":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"TECH_SOURCER","secondary_task":"",
 "task_evidence":"lead sourcing strategy and execution for our fast-paced hiring needs across software, hardware, and product teams",
 "new":{
  "1":R+"人才寻访sourcing不是采购职责。",
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"人才寻访sourcing不是采购职责。",
  "4":R+"GitHub寻访渠道不是Git协作；寻访不是采购。",
  "5":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":R+"人才寻访sourcing不是采购职责。",
  "7":R+"人才寻访sourcing不是采购职责。",
  "8":R+"人才寻访sourcing不是采购职责。",
  "9":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "10":[["V2_ASHBY","GENERAL","CHOICE"],["V2_LEVER","GENERAL","CHOICE"]],
  "11":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "12":R+"人才寻访sourcing不是采购职责。",
  "13":R+"satellite office不是Microsoft Office。",
  "14":R+"GitHub寻访渠道不是Git协作。",
  "15":"DUPLICATE:E0449:10"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术寻访。Ashby/Lever保留。办公场地拒收Office。"
},
"N1035":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"HRBP_CORP","secondary_task":"",
 "task_evidence":"We are seeking a strategic and experienced Senior Staff HR Business Partner to support our corporate functions",
 "new":{
  "1":[["V2_MARKETING","SEPARATE","COLLABORATION_OBJECT"]],
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"],["V2_MARKETING","SEPARATE","COLLABORATION_OBJECT"]],
  "4":[["V2_HR_CREDENTIAL","PREFERRED","CHOICE"]],
  "5":"DUPLICATE:N1035:4",
  "6":"DUPLICATE:N1035:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"公司职能HRBP。销售市场为服务对象。"
},
"N1023":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"ATLAS_TRAINER","secondary_task":"",
 "task_evidence":"Boston Dynamics is seeking a highly organized Technical Trainer to design, deliver, and manage training and documentation for the Atlas Data Operations",
 "new":{
  "1":[["V2_TELEOP","SEPARATE","BACKGROUND"]],
  "2":O+"BD产品线API未单列冻结项。",
  "3":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":R+"project status不是Microsoft Project。",
  "5":O+"VR systems未单列冻结项。",
  "6":[["V2_MOCAP","GENERAL","UNCONDITIONAL"]],
  "7":O+"VR headsets未单列冻结项。",
  "8":"DUPLICATE:N1023:6",
  "9":O+"handheld VR controllers未单列冻结项。",
  "10":R+"English can is not Controller Area Network.",
  "11":R+"English can is not Controller Area Network."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Atlas培训。遥操为培训对象。动捕保留。"
},
"N0994":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"TREASURY","secondary_task":"",
 "task_evidence":"responsible for the efficient management of the firm's liquidity position, funding and debt management",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"project cash flows不是Microsoft Project。",
  "3":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "4":"DUPLICATE:N0994:3",
  "5":"DUPLICATE:N0994:3",
  "6":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0994:6",
  "8":[["V2_ACCOUNTING_CREDENTIAL","PREFERRED","CHOICE"]],
  "9":"DUPLICATE:N0994:8",
  "10":O+"FRM未单列冻结项。",
  "11":O+"CTP未单列冻结项。",
  "12":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"资金专员。CFA保留。FRM/CTP目录外。"
}
}
if __name__=='__main__':
 register('RF_CORPORATE_SUPPORT', decisions, reader='grok4.6')
