"""First-pass adjudication for corporate-support coding_order 1-16. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"N1007":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"FACILITIES_MAINT","secondary_task":"",
 "task_evidence":"Responsible for providing high-level maintenance, repair, inspection, and modification of complex building systems",
 "new":{
  "1":O+"plumbing/electrical/HVAC未单列冻结项。",
  "2":R+"楼宇设备校准不是传感器与系统标定。",
  "3":O+"computerized maintenance systems未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"设施维修技师。"
},
"N0272":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"SHOWROOM_GUIDE","secondary_task":"MARKETING",
 "task_evidence":"负责总部展厅及重要接待区的日常接待与讲解工作",
 "new":{
  "1":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"展厅讲解。物料采购记采购职责。"
},
"N0547":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"IT_SECURITY","fine_task":"INFOSEC_LEAD","secondary_task":"",
 "task_evidence":"制定年度审计计划，定期审计账号权限、代码仓库、办公系统、云服务、开发环境、终端设备及第三方服务",
 "new":{
  "1":[["V2_PROCUREMENT","SEPARATE","BACKGROUND"]],
  "2":[["V2_PROCUREMENT","SEPARATE","BACKGROUND"]],
  "3":O+"DLP及终端安全能力未单列冻结项。",
  "4":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_AGENT_WORKFLOW","PREFERRED","UNCONDITIONAL"]],
  "6":O+"ISO 27001未单列冻结项。",
  "7":O+"等级保护未单列冻结项。",
  "8":[["V2_SECURITY_CREDENTIAL","PREFERRED","CHOICE"]],
  "9":"DUPLICATE:N0547:8",
  "10":"DUPLICATE:N0547:8",
  "11":"DUPLICATE:N0547:8",
  "12":"DUPLICATE:N0547:6",
  "13":"DUPLICATE:N0547:8"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"信息安全主管。供应商为评估对象。认证保留。"
},
"N0775":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LEGAL","fine_task":"COMMERCIAL_COUNSEL","secondary_task":"",
 "task_evidence":"We are seeking a Legal Counsel - Commercial to join our Legal team and drive the commercial legal strategy that enables our rapid customer expansion.",
 "new":{
  "1":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "2":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "3":[["V2_PROCUREMENT","PREFERRED","UNCONDITIONAL"]],
  "4":R+"Onsite work philosophy is not Microsoft Office."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"商业法务。政府合同采购经验记采购优先。"
},
"E0543":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"RECRUITING_COORD","secondary_task":"",
 "task_evidence":"Coordinate complex interview schedules across engineering, operations, and manufacturing teams",
 "new":{
  "1":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"人才寻访sourcing不是采购职责。",
  "4":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_HR","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "8":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "9":[["V2_HR","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"招聘协调。sourcing拒收采购。"
},
"E0178":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"IT_SECURITY","fine_task":"IT_SECURITY_DIRECTOR","secondary_task":"",
 "task_evidence":"主导公司信息安全体系搭建与落地,覆盖网络、系统、数据、权限等全维度安全治理",
 "new":{
  "1":[["V2_FEISHU","DUTY_OWN_USE","CHOICE"],["V2_KINGDEE","DUTY_OWN_USE","CHOICE"]],
  "2":[["V2_FEISHU","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"信息化与安全总监。飞书/金蝶保留。"
},
"N0364":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"CAPITAL_COMMS","secondary_task":"",
 "task_evidence":"撰写中英文新闻稿，主导公司业绩发布、业务更新等信息的官方传播",
 "new":{
  "1":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_MARKETING","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"资本内容总经理。"
},
"E0395":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"EXEC_ASSISTANT","secondary_task":"",
 "task_evidence":"Apptronik is seeking an experienced Senior Executive Assistant to provide on-site support for the Chief Product Officer, Chief Commercial Officer, and Vice President of Software.",
 "new":{
  "1":R+"On-site office support is not Microsoft Office.",
  "2":[["V2_SAP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"Calendar priority triage is not incident support.",
  "4":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_SAP","GENERAL","UNCONDITIONAL"]],
  "6":R+"Multi-office logistics is not Microsoft Office.",
  "7":R+"C-suite executives are not the C language.",
  "8":"DUPLICATE:E0395:2",
  "9":"DUPLICATE:E0395:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"高管助理。SAP Concur/Google Workspace保留。"
},
"N0083":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"TECH_RECRUITER","secondary_task":"",
 "task_evidence":"独立统筹并落地全流程招聘工作，高效完成岗位招聘交付",
 "new":{
  "1":[["V2_HR","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"],["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "7":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_HR","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"招聘专家。雇主品牌记营销职责。"
},
"E0305":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LEGAL","fine_task":"CORP_COUNSEL","secondary_task":"",
 "task_evidence":"Support Board of Directors and committee governance, including preparation of Board materials and resolutions",
 "new":{
  "1":[["V2_LEGAL","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_LEGAL_CREDENTIAL","REQUIRED","UNCONDITIONAL"]],
  "4":[["V2_LEGAL","PREFERRED","UNCONDITIONAL"]],
  "5":R+"Salary USD is not Universal Scene Description.",
  "6":R+"Third-party recruiting boilerplate is not HR professional duty.",
  "7":"DUPLICATE:E0305:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"公司律师。执照记法律资质。"
},
"N0456":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"FINANCE_ROTATION","secondary_task":"",
 "task_evidence":"参与财务各模块轮岗（会计核算、报表编制、税务、资金、财务分析、内控等），系统掌握财务全流程",
 "new":{
  "1":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"],["V2_ACCOUNTING_CREDENTIAL","PREFERRED","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0456:4",
  "6":[["V2_ACCOUNTING_CREDENTIAL","PREFERRED","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0456:6",
  "8":[["V2_KINGDEE","PREFERRED","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0456:8"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"财务管培。金蝶/会计职称保留。"
},
"N0931":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"PEOPLE_OPS_DIRECTOR","secondary_task":"",
 "task_evidence":"Lead Talent Acquisition and manage a team of recruiters and People Operations partners",
 "new":{
  "1":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":O+"agent-based automations未单列冻结项。",
  "3":[["V2_LEVER","PREFERRED","CHOICE"],["V2_ADP","PREFERRED","CHOICE"]],
  "4":"DUPLICATE:N0931:3",
  "5":O+"Lattice未单列冻结项。",
  "6":"DUPLICATE:N0931:3",
  "7":O+"Vestwell未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"People Ops负责人。Lever/ADP保留。"
},
"N0659":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"ADMIN_LEAD","secondary_task":"",
 "task_evidence":"统筹公司多地办公区（北京、苏州等）行政体系，协调各区域行政事务",
 "new":{
  "1":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"行政主管。行政采购记采购。"
},
"N0192":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"HRBP_RD","secondary_task":"",
 "task_evidence":"负责研发类岗位的全流程招聘",
 "new":{
  "1":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_HR","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"研发HRBP。"
},
"N0875":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"TA_PEOPLE_PARTNER","secondary_task":"",
 "task_evidence":"The primary focus of this role is Talent Acquisition.",
 "new":{
  "1":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "8":[["V2_HR","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "9":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "10":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "11":R+"Proactive sourcing is not procurement.",
  "12":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "13":[["V2_LEVER","GENERAL","CHOICE"],["V2_ADP","GENERAL","CHOICE"]],
  "14":"DUPLICATE:N0875:13",
  "15":O+"UKG未单列冻结项。",
  "16":"DUPLICATE:N0875:13",
  "17":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "18":R+"English can is not Controller Area Network.",
  "19":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "20":R+"English can is not Controller Area Network.",
  "21":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "22":[["V2_HR","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Dexterity人才伙伴。世界模型为公司产品背景。"
},
"E0596":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"RECRUITING_COORD","secondary_task":"",
 "task_evidence":"Run Ashby as the system of record: maintain pipeline hygiene, ensure stages/dispositions are accurate",
 "new":{
  "1":[["V2_ASHBY","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_HR","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_ASHBY","GENERAL","UNCONDITIONAL"]],
  "6":R+"English can is not Controller Area Network.",
  "7":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_ASHBY","PREFERRED","UNCONDITIONAL"]],
  "9":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "10":"DUPLICATE:E0596:1",
  "11":"DUPLICATE:E0596:5",
  "12":"DUPLICATE:E0596:8"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"PI招聘协调。Ashby保留。面试calibration不记传感器标定。"
}
}
if __name__=='__main__':
 register('RF_CORPORATE_SUPPORT', decisions, reader='grok4.6')
