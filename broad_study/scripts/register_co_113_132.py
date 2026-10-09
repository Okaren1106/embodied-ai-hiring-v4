"""First-pass adjudication for corporate-support coding_order 113-132. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"N0982":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"FA_MANAGER","secondary_task":"",
 "task_evidence":"Responsible for leading a team that performs a range of accounting activities to ensure compliance with accounting standards",
 "new":{
  "1":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0982:1",
  "3":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "4":"DUPLICATE:N0982:3",
  "5":R+"Project management skills不是Microsoft Project。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"财务会计经理。"
},
"N0881":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"STAFF_ACCOUNTANT","secondary_task":"",
 "task_evidence":"Dexterity is seeking a detail-oriented Staff Accountant to join our Finance team",
 "new":{
  "1":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "2":R+"招聘启事seeking不是人力资源技能项。",
  "3":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_ADP","DUTY_OWN_USE","UNCONDITIONAL"],["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0881:6",
  "8":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "9":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "10":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "11":[["V2_HR","SEPARATE","COLLABORATION_OBJECT"]],
  "12":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "13":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "14":[["V2_NETSUITE","PREFERRED","CHOICE"],["V2_ADP","PREFERRED","CHOICE"]],
  "15":"DUPLICATE:N0881:14",
  "16":"DUPLICATE:N0881:14",
  "17":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "18":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"会计。工资单记人力。世界模型为公司产品背景。ADP/NetSuite保留。"
},
"N0849":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"CORP_DEV","secondary_task":"",
 "task_evidence":"work closely with the CFO on the company’s most important strategic initiatives",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"战略与企业发展。无新候选。"
},
"E0572":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"TECH_RECRUITER","secondary_task":"",
 "task_evidence":"Manage end-to-end recruitment across multiple concurrent requisitions spanning Commercial and other technical/operational functions",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。",
  "2":R+"人才寻访sourcing不是采购职责。",
  "3":R+"人才寻访sourcing不是采购职责。",
  "4":R+"人才寻访sourcing不是采购职责。",
  "5":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "7":R+"人才寻访sourcing不是采购职责。",
  "8":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "9":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "10":[["V2_HR","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术招聘。寻访不记采购。"
},
"E0454":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LEGAL","fine_task":"COMMERCIAL_AGC","secondary_task":"",
 "task_evidence":"Lead high-stakes negotiations and procurement agreements for global data center capacity, GPU compute, and complex technology licenses.",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。",
  "2":R+"English can is not Controller Area Network.",
  "3":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_LEGAL_CREDENTIAL","REQUIRED","UNCONDITIONAL"]],
  "6":"DUPLICATE:E0454:5",
  "7":O+"CIPP/US未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"商业副总法务。GPU采购协议记采购。律师资格保留。"
},
"E0473":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"FINANCE_MANAGER","secondary_task":"",
 "task_evidence":"Lead business units’ annual operating plan, budgeting, forecasting, and long-term financial planning processes.",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。"
 },
 "old_overrides":{
  "O3":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原Excel短词定位为空，改为Excel或Google Sheets句。","quote":"advanced proficiency in Excel or Google Sheets"}
 },
 "additions":[],"outside_extra":[],
 "notes":"财务经理。Excel继承改写。"
},
"E0470":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"FACILITIES_SP","secondary_task":"",
 "task_evidence":"você é o dono da operação predial da nossa unidade de São Paulo",
 "new":{},
 "old_overrides":{
  "O2":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"原葡萄牙语安全短词定位为空，改为职业安全文档职责句。","quote":"Estabelecer e manter as rotinas e a documentação de segurança do trabalho junto aos prestadores externos."}
 },
 "additions":[],"outside_extra":[],
 "notes":"圣保罗设施。职业安全继承改写。"
},
"E0532":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"PEOPLE_LEAD_SP","secondary_task":"",
 "task_evidence":"Conduzir operações de recrutamento em volume: pipelines, agendamento, experiência do candidato",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"圣保罗People Lead。无新候选。"
},
"E0469":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ADMIN_FACILITIES","fine_task":"FACILITIES_CDMX","secondary_task":"",
 "task_evidence":"eres el responsable de la operación predial de nuestra unidad de Ciudad de México",
 "new":{
  "1":R+"trabajar en campo不是C语言。"
 },
 "old_overrides":{
  "O2":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"原西班牙语安全短词定位为空，改为职业安全文档职责句。","quote":"Establecer y mantener las rutinas y la documentación de seguridad laboral junto a los contratistas externos."}
 },
 "additions":[],"outside_extra":[],
 "notes":"墨西哥城设施。职业安全继承改写。"
},
"E0531":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"PEOPLE_LEAD_CDMX","secondary_task":"",
 "task_evidence":"Liderar operaciones de reclutamiento en volumen: pipelines, agendamiento, experiencia del candidato",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"墨西哥城People。无新候选。"
},
"E0474":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"FINANCE_OPS_BR","secondary_task":"",
 "task_evidence":"você é o principal parceiro financeiro do time de operações no Brasil",
 "new":{
  "1":[["V2_ACCOUNTING_CREDENTIAL","PREFERRED","UNCONDITIONAL"]],
  "2":[["V2_SAP","GENERAL","CHOICE"],["V2_NETSUITE","GENERAL","CHOICE"]],
  "3":"DUPLICATE:E0474:1",
  "4":"DUPLICATE:E0474:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"巴西财务运营。CRC/NetSuite/SAP保留。"
},
"E0571":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"IT_SECURITY","fine_task":"SECURITY_TPM","secondary_task":"",
 "task_evidence":"Set the vision for data and access governance, ensuring alignment with Figure’s business objectives",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"安全与隐私TPM。"
},
"E0555":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"PEOPLE_OPS","secondary_task":"",
 "task_evidence":"Own the employee lifecycle end-to-end (onboarding, job changes, offboarding, records, verifications)",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。",
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_RIPPLING","PREFERRED","UNCONDITIONAL"]],
  "5":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "6":"DUPLICATE:E0555:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"People Ops。Rippling保留。"
},
"E0597":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"AI_RECRUITER","secondary_task":"",
 "task_evidence":"Own full lifecycle recruiting for technical roles from building heatmaps for frontier lab talent",
 "new":{
  "1":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"面试校准interviewer calibration不是传感器标定。",
  "4":R+"English can is not Controller Area Network.",
  "5":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "7":R+"人才寻访sourcing不是采购职责。",
  "8":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "9":[["V2_HR","PREFERRED","UNCONDITIONAL"]],
  "10":[["V2_HR","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"AI招聘。面试校准拒收标定。"
},
"E0607":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"PEOPLE_OPS","secondary_task":"",
 "task_evidence":"Own the end-to-end payroll process for hourly and exempt employees in Rippling",
 "new":{
  "1":[["V2_RIPPLING","DUTY_OWN_USE","UNCONDITIONAL"],["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_RIPPLING","DUTY_OWN_USE","UNCONDITIONAL"],["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_RIPPLING","GENERAL","UNCONDITIONAL"]],
  "4":"DUPLICATE:E0607:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"People Ops。Rippling保留。"
},
"E0582":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"BIZ_OPS","secondary_task":"",
 "task_evidence":"Drive data, compute, and infrastructure partnerships, from sourcing through negotiation and management.",
 "new":{
  "1":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"office expansion不是Microsoft Office。",
  "4":R+"cross-border project experience不是Microsoft Project。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"商务运营。算力采购记采购。"
},
"N0717":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"RECRUITING_COORD","secondary_task":"",
 "task_evidence":"2–5 years of recruiting coordination or recruiting operations experience",
 "new":{
  "1":R+"in-office role不是Microsoft Office。",
  "2":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "3":R+"English can is not Controller Area Network.",
  "4":R+"in-office 5 days不是Microsoft Office。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"招聘协调。现场办公拒收Office。"
},
"N0718":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"EDUCATION_POLICY","fine_task":"TECH_WRITER","secondary_task":"",
 "task_evidence":"We are seeking a highly skilled Technical Writer to translate complex robotic intelligence into clear, accurate, and user-friendly documentation.",
 "new":{
  "1":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"Python, C++ is not the C language.",
  "4":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "5":O+"Markdown未单列冻结项。",
  "6":"DUPLICATE:N0718:4",
  "7":[["V2_JIRA","GENERAL","CHOICE"],["V2_CONFLUENCE","GENERAL","CHOICE"],["V2_GOOGLE_WORKSPACE","GENERAL","CHOICE"]],
  "8":"DUPLICATE:N0718:7",
  "9":"DUPLICATE:N0718:7",
  "10":"DUPLICATE:N0718:7",
  "11":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"技术文档。Git/Jira/Confluence保留。C++拒收C。"
},
"N0716":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"HR","fine_task":"TECH_RECRUITER_IN","secondary_task":"",
 "task_evidence":"We're looking for a Technical Recruiter to build out our presence in India, owning full-cycle recruiting for technical and engineering roles",
 "new":{
  "1":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"面试校准calibrate on candidate bar不是传感器标定；寻访不是采购。",
  "4":R+"人才寻访sourcing不是采购职责。",
  "5":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_HR","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"印度技术招聘。寻访不记采购。"
},
"N0699":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FINANCE","fine_task":"SENIOR_ACCOUNTANT","secondary_task":"",
 "task_evidence":"The Senior Accountant will be the primary accounting resource for Skild AI's US and international operations",
 "new":{
  "1":R+"招聘启事不是人力资源技能项。",
  "2":O+"Rillet/Rootstock未单列冻结项。",
  "3":"DUPLICATE:N0699:2",
  "4":[["V2_QUICKBOOKS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0699:4",
  "6":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0699:6",
  "8":[["V2_QUICKBOOKS","DUTY_OWN_USE","UNCONDITIONAL"],["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "9":[["V2_ACCOUNTING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "10":"DUPLICATE:N0699:9",
  "11":"DUPLICATE:N0699:9",
  "12":[["V2_QUICKBOOKS","GENERAL","UNCONDITIONAL"]],
  "13":"DUPLICATE:N0699:12",
  "14":[["V2_ACCOUNTING","GENERAL","UNCONDITIONAL"]],
  "15":"DUPLICATE:N0699:14",
  "16":[["V2_HR","GENERAL","UNCONDITIONAL"]],
  "17":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"高级会计。QuickBooks保留。工资单记人力。"
}
}
if __name__=='__main__':
 register('RF_CORPORATE_SUPPORT', decisions, reader='grok4.6')
