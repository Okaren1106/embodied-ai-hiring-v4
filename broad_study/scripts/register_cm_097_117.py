"""First-pass adjudication for commercial coding_order 97-117. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
PRE={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"PRE_SALES","secondary_task":"",
 "task_evidence":"挖掘潜在机会。",
 "new":{
  "1":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_SALES_CRM","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_CUSTOMER_SERVICE","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"售前解决方案模板。"
}
decisions={
"E0194":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MARKETING","fine_task":"PRODUCT_PR","secondary_task":"",
 "task_evidence":"制定从产品预热到首发上市的端到端(End-to-End)产品公关策略。",
 "new":{
  "1":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"],["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "3":R+"技术演示包装不是CMF设计。",
  "4":[["V2_MARKETING","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_PROJECT_METHOD","GENERAL","UNCONDITIONAL"],["V2_PM_CREDENTIAL","PREFERRED","UNCONDITIONAL"]],
  "6":"DUPLICATE:E0194:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"公关专家。世界模型为传播对象。C未命中编程。包装拒收CMF。"
},
"E0181":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_SUCCESS","fine_task":"VOC","secondary_task":"",
 "task_evidence":"负责搭建VOC体系及运营",
 "new":{
  "1":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"VOC管理。证据保留原文空格。"
},
"E0159":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"STRATEGY","fine_task":"STRATEGIC_BP","secondary_task":"",
 "task_evidence":"围绕具身智能核心方向，开展问题导向型研究，为专项推进提供决策依据。",
 "new":{
  "1":[["V2_PROCUREMENT","SEPARATE","BACKGROUND"]],
  "2":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"战略分析师。sourcing是项目寻源不是采购岗。"
},
"E0140":dict(PRE, fine_task="INDUSTRIAL_PRE_SALES", notes="工业制造售前架构师。"),
"E0135":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_SUCCESS","fine_task":"VOC_INSIGHT","secondary_task":"",
 "task_evidence":"从 0 搭建并运营用户之声(VoC)体系",
 "new":{
  "1":[["V2_UX_RESEARCH","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_UX_RESEARCH","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"用户洞察专家。"
},
"E0134":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MARKETING","fine_task":"USER_OPS","secondary_task":"",
 "task_evidence":"制定整体社区规划与玩法策略",
 "new":{
  "1":[["V2_MARKETING","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"用户运营专家。"
},
"E0126":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ECOSYSTEM","fine_task":"OSS_COMMUNITY","secondary_task":"MARKETING",
 "task_evidence":"负责公司开源模型生态的运营与建设",
 "new":{
  "1":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "2":[["V2_HUGGINGFACE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_HUGGINGFACE","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_MARKETING","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"开源生态运营。GitHub社区运营不记Git协作。"
},
"E0120":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"LOGISTICS_PRE_SALES","secondary_task":"",
 "task_evidence":"挖掘潜在机会。",
 "new":{
  "1":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"物流售前技术专家。"
},
"E0106":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"LOGISTICS_KA","secondary_task":"",
 "task_evidence":"识别并锁定行业内具有标杆效应和规模化复制潜力的头部客户",
 "new":{
  "1":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_SALES_CRM","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_SALES_CRM","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"物流行业大客户经理。"
},
"E0337":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MARKETING","fine_task":"PRODUCT_MARKETING","secondary_task":"",
 "task_evidence":"Lead GTM planning and high-profile product announcements.",
 "new":{
  "1":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_MARKETING","GENERAL","UNCONDITIONAL"]],
  "7":R+"English can is not Controller Area Network.",
  "8":[["V2_MARKETING","PREFERRED","UNCONDITIONAL"]],
  "9":R+"English can is not Controller Area Network.",
  "10":R+"Salary USD is not Universal Scene Description.",
  "11":R+"Third-party recruiting boilerplate is not HR professional duty."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Agility产品营销经理。"
},
"E0308":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MARKETING","fine_task":"EDITORIAL","secondary_task":"",
 "task_evidence":"Define our global editorial strategy: Position our brand as the definitive authority on humanoid robotics",
 "new":{
  "1":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_MARKETING","GENERAL","UNCONDITIONAL"]],
  "4":R+"English can is not Controller Area Network.",
  "5":R+"Salary USD is not Universal Scene Description.",
  "6":R+"Third-party recruiting boilerplate is not HR professional duty."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Agility内容主编。"
},
"N1016":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"SPOT_SALES","secondary_task":"",
 "task_evidence":"We are seeking a sales professional to develop and maintain a sales pipeline for our cutting edge technology for our Spot Product Line.",
 "new":{
  "1":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"English can is not Controller Area Network.",
  "3":[["V2_MARKETING","PREFERRED","UNCONDITIONAL"]],
  "4":R+"Recruiting process boilerplate is not HR professional duty."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"BD Associate Sales Executive。"
},
"N1004":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MARKETING","fine_task":"ATLAS_PMM","secondary_task":"",
 "task_evidence":"As a Product Marketing Manager for Atlas, you will be an integral part of our world-class product team",
 "new":{
  "1":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"English can is not Controller Area Network.",
  "3":[["V2_MARKETING","GENERAL","UNCONDITIONAL"]],
  "4":R+"English can is not Controller Area Network.",
  "5":[["V2_PHOTOSHOP","PREFERRED","CHOICE"]],
  "6":O+"InDesign未单列冻结项。",
  "7":"DUPLICATE:N1004:5",
  "8":O+"Canva未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Atlas产品营销。Photoshop保留。"
},
"N1038":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"SDR","secondary_task":"MARKETING",
 "task_evidence":"We are seeking an Outbound Sales Development Representative (SDR) to develop and support a sales pipeline for our Industrial team.",
 "new":{
  "1":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"],["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CRM","PREFERRED","CHOICE"],["V2_SALESFORCE","PREFERRED","CHOICE"]],
  "3":"DUPLICATE:N1038:2",
  "4":"DUPLICATE:N1038:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"SDR。Salesforce/CRM保留。"
},
"N0880":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CUSTOMER_SUCCESS","fine_task":"CS_MANAGER","secondary_task":"",
 "task_evidence":"The Sr. Manager, Customer Success role at Dexterity is a critical position responsible for ensuring customer satisfaction and retention.",
 "new":{
  "1":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"English can is not Controller Area Network.",
  "3":R+"English can is not Controller Area Network.",
  "4":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":R+"Program manager for deployment is not Microsoft Project.",
  "7":R+"English can is not Controller Area Network.",
  "8":[["V2_CUSTOMER_SERVICE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "9":[["V2_SALES_CRM","GENERAL","UNCONDITIONAL"]],
  "10":R+"Office location is not Microsoft Office."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Dexterity客户成功负责人。"
},
"N0861":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MARKETING","fine_task":"MARKETING_LEAD","secondary_task":"",
 "task_evidence":"You will serve as Dexterity's overall marketing lead.",
 "new":{
  "1":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "4":"DUPLICATE:N0861:3",
  "5":[["V2_MARKETING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_SALES_CRM","SEPARATE","COLLABORATION_OBJECT"]],
  "7":R+"Recruiting materials in a message framework are not HR professional duty.",
  "8":O+"AI-driven workflows未单列冻结项。",
  "9":[["V2_MARKETING","GENERAL","UNCONDITIONAL"]],
  "10":[["V2_MARKETING","GENERAL","UNCONDITIONAL"]],
  "11":R+"English can is not Controller Area Network.",
  "12":O+"Generic AI tools未单列冻结项。",
  "13":[["V2_MARKETING","PREFERRED","UNCONDITIONAL"]],
  "14":[["V2_MARKETING","PREFERRED","UNCONDITIONAL"]],
  "15":[["V2_MARKETING","GENERAL","UNCONDITIONAL"]],
  "16":R+"Salary USD is not Universal Scene Description.",
  "17":R+"Hiring-process AI notice is not HR professional duty."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Dexterity市场负责人。世界模型为产品传播对象。"
},
"N0724":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"CONSTRUCTION_AE","secondary_task":"",
 "task_evidence":"drive growth within the construction industry by helping customers adopt autonomous robotics solutions",
 "new":{
  "1":R+"Construction project selling is not Microsoft Project.",
  "2":R+"Construction project stakeholders are not Microsoft Project.",
  "3":R+"Project execution selling is not Microsoft Project."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FieldAI建筑客户AE。"
},
"N0742":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"CONSTRUCTION_EAE","secondary_task":"",
 "task_evidence":"drive growth within the construction industry by helping customers adopt autonomous robotics solutions",
 "new":{
  "1":R+"Construction project selling is not Microsoft Project.",
  "2":R+"Construction project stakeholders are not Microsoft Project.",
  "3":R+"Project execution selling is not Microsoft Project."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FieldAI建筑企业AE。与N0724同类误触发。"
},
"N0744":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"INDUSTRIAL_EAE","secondary_task":"",
 "task_evidence":"Build and manage a healthy sales pipeline and accurate forecasts.",
 "new":{
  "1":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_SALES_CRM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"C-level executives are not the C programming language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FieldAI工业企业AE。"
},
"N0681":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"SALES","fine_task":"WAREHOUSE_SE","secondary_task":"",
 "task_evidence":"Deep knowledge of warehouse operations: order fulfillment workflows, labor management, WMS/WCS architecture",
 "new":{
  "1":O+"WMS/WCS未单列冻结项。",
  "2":O+"WCS未单列冻结项。",
  "3":O+"AutoMod未单列冻结项。",
  "4":O+"Emulate3D未单列冻结项。",
  "5":O+"FlexSim未单列冻结项。",
  "6":O+"EDI未单列冻结项。",
  "7":O+"SOAP未单列冻结项。",
  "8":O+"REST未单列冻结项。",
  "9":[["V2_AUTOCAD","GENERAL","UNCONDITIONAL"]],
  "10":"DUPLICATE:N0681:9",
  "11":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Skild仓储备售工程师。AutoCAD保留。"
},
"N0700":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MARKETING","fine_task":"BRAND_IDENTITY","secondary_task":"",
 "task_evidence":"lead the visual design of a full 360 brand campaign",
 "new":{
  "1":R+"A project in a portfolio note is not Microsoft Project."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"品牌视觉设计师。标题作任务证据。"
}
}
if __name__=='__main__':
 register('RF_COMMERCIAL_CUSTOMER', decisions, reader='grok4.6')
