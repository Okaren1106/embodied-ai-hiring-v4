"""First-pass adjudication for corporate-support coding_order 17-32. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"N0721":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"WORKPLACE_MANAGER","secondary_task":"",
 "task_evidence":"Own daily workplace operations for the San Mateo office, ensuring the office is clean, organized, stocked, functional, welcoming, and guest-ready.",
 "new":{
  "1":R+"Workplace office operations are not Microsoft Office.",
  "2":[["V2_HR","SEPARATE","COLLABORATION_OBJECT"]],
  "3":R+"Office activity is not Microsoft Office.",
  "4":R+"Office operations are not Microsoft Office.",
  "5":R+"Office communications are not Microsoft Office.",
  "6":R+"Office supplies are not Microsoft Office.",
  "7":R+"Office supplies vendors are not Microsoft Office.",
  "8":[["V2_HR","SEPARATE","COLLABORATION_OBJECT"]],
  "9":R+"Office access logistics are not Microsoft Office.",
  "10":R+"Office organization is not Microsoft Office.",
  "11":R+"Office standards are not Microsoft Office.",
  "12":R+"Office issues are not Microsoft Office.",
  "13":R+"Office management experience is not Microsoft Office.",
  "14":R+"Office operations experience is not Microsoft Office.",
  "15":R+"Office activity is not Microsoft Office.",
  "16":R+"Office supplies experience is not Microsoft Office.",
  "17":[["V2_GOOGLE_WORKSPACE","GENERAL","EXAMPLE"],["V2_JIRA","GENERAL","CHOICE"]],
  "18":"DUPLICATE:N0721:17",
  "19":O+"Slack未单列冻结项。",
  "20":"DUPLICATE:N0721:17",
  "21":O+"Freshservice未单列冻结项。",
  "22":O+"ServiceNow未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"职场经理。办公场所不记MS Office。Jira/Google Workspace保留。"
},
"E0067":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"TECH_POLICY_INTERN","secondary_task":"",
 "task_evidence":"深度调研具身智能、人形机器人领域的全球技术趋势，为公司参与政府科技规划、政策建言提供专业的技术支撑与情报分析。",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术研判实习。无新候选。"
},
"N0985":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"EA_LEGAL_PEOPLE","secondary_task":"",
 "task_evidence":"Provides comprehensive administrative and operational support to Chief Legal Officer and Chief People Officer.",
 "new":{
  "1":[["V2_OFFICE","GENERAL","CHOICE"],["V2_GOOGLE_WORKSPACE","GENERAL","CHOICE"]],
  "2":"DUPLICATE:N0985:1",
  "3":"DUPLICATE:N0985:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"高管商务伙伴。正文写明Microsoft Office Suite。"
},
"N0248":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"GOV_PROJECTS","secondary_task":"",
 "task_evidence":"负责统筹组织公司在科技创新、专项补贴、平台载体、人才认定等各类政府项目的策划和申报",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"项目申报经理。无新候选。"
},
"N0422":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"FUNDRAISING_DIRECTOR","secondary_task":"",
 "task_evidence":"负责集团体系公司及生态企业融资的整体规划与落地",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"融资总监。无新候选。"
},
"N0420":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"GOV_AFFAIRS","secondary_task":"",
 "task_evidence":"维护和拓展中央部委及上海市行业主管部门的政府关系。",
 "new":{
  "1":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"政府事务。toG品牌记营销。"
},
"N0416":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"OVERSEAS_GOVREL","secondary_task":"",
 "task_evidence":"维护和拓展欧美国家属地政府的关系，包括不限于科技、工业、信息化等专业部门。",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"海外政府关系。无新候选。"
},
"N0415":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"PE_OPS_ASSIST","secondary_task":"",
 "task_evidence":"支持已投企业的投后和运营管理工作，定期收集已投企业的业务与财务数据",
 "new":{
  "1":R+"学历中的法律知识储备不是法务专业职责。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"投后管理助理。法律专业拒收。"
},
"N0402":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"FUNDRAISING_MANAGER","secondary_task":"",
 "task_evidence":"支持集团体系公司及生态企业融资，包括融资材料准备、路演支持、投资人对接、尽调推进等",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"融资经理。无新候选。"
},
"N0392":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"MNA","secondary_task":"LEGAL",
 "task_evidence":"独立执行并购全交易流程，涵盖投资逻辑分析、财务模型搭建、交易架构设计、尽调组织协调、法律协议起草谈判及项目交割等核心环节。",
 "new":{
  "1":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"学历中的法律专业不是法务专业职责。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"并购。协议起草记法务职责。"
},
"N0391":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"PE_OPS","secondary_task":"",
 "task_evidence":"跟进投后项目的运营情况，与企业保持高频互动，收集业务与财务相关数据。",
 "new":{
  "1":[["V2_ACCOUNTING","PREFERRED","UNCONDITIONAL"]],
  "2":[["V2_LEGAL","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"投后运营。法律条款处理记法务优先。"
},
"N0385":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"STRATEGY","secondary_task":"",
 "task_evidence":"机器人行业政策研究及商业模式研究，跟踪行业趋势及竞品策略，输出行业研究报告",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"战略规划专家。无新候选。"
},
"N0383":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"COMPLIANCE_RISK","secondary_task":"LEGAL",
 "task_evidence":"全面负责财务风控，包括专户监管、出资核查、报酬计提核算、估值、分配测算、资金流水穿透核查",
 "new":{
  "1":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"],["V2_ACCOUNTING_CREDENTIAL","PREFERRED","CHOICE"]],
  "4":"DUPLICATE:N0383:3",
  "5":"DUPLICATE:N0383:3",
  "6":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"],["V2_LEGAL","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"合规风控总监。"
},
"N0370":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"TRAINING_DIRECTOR","secondary_task":"",
 "task_evidence":"设计对标岗位胜任力的课程体系与认证标准，主导课程开发与课堂管理",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"服务培训部总监。无新候选。"
},
"N0233":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LEGAL","fine_task":"LEGAL_SPECIALIST","secondary_task":"",
 "task_evidence":"起草、审核和修改各类合同及法律文件",
 "new":{
  "1":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":[["V2_LEGAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "8":[["V2_LEGAL","GENERAL","UNCONDITIONAL"],["V2_LEGAL_CREDENTIAL","REQUIRED","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0233:8",
  "10":[["V2_LEGAL","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"法务专员。法律职业资格记资质。"
},
"N0213":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"HRBP_RECRUITING","secondary_task":"",
 "task_evidence":"负责对接业务团队全流程招聘，保障关键岗位人才供应",
 "new":{
  "1":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_HR","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"招聘向HRBP。"
}
}
if __name__=='__main__':
 register('RF_CORPORATE_SUPPORT', decisions, reader='grok4.6')
