"""First-pass adjudication for mechanical coding_order 1-16. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"N0780":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"MECH_HW","secondary_task":"",
 "task_evidence":"Apply DFM, DFA, DFS principles throughout the design lifecycle.",
 "new":{
  "1":R+"airflow guides不是Apache Airflow。",
  "2":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0780:2",
  "4":"DUPLICATE:N0780:2",
  "5":O+"DFS可服务性设计未单列冻结项。",
  "6":R+"招募各职级不是人力资源技能项。",
  "7":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],
  "8":"DUPLICATE:N0780:7"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人硬件机械。DFM/CNC保留。气流导向不记Airflow。"
},
"N0670":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"COMPONENT_PROCESS","fine_task":"HW_BENGALURU","secondary_task":"",
 "task_evidence":"Utilize 3D printing and rapid prototyping techniques to develop and test hardware prototypes.",
 "new":{
  "1":[["V2_CNC_PROCESS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":O+"Arduino未单列冻结项。",
  "3":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"班加罗尔硬件。增材制造记成型工艺。"
},
"E0319":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"MECH_ENG","secondary_task":"",
 "task_evidence":"Own the 3D and 2D design of electromechanical components and subassemblies, including prototyping of parts and subsystems.",
 "new":{
  "1":R+"agile team不是项目计划方法项。",
  "2":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"与工业设计协作不是本人承担CMF。",
  "4":[["V2_JIRA","DUTY_OWN_USE","CHOICE"],["V2_CONFLUENCE","DUTY_OWN_USE","CHOICE"]],
  "5":R+"linear guides/lead screws不是Linear工具。",
  "6":[["V2_ONSHAPE","GENERAL","CHOICE"]],
  "7":"DUPLICATE:E0319:4",
  "8":[["V2_PLM","PREFERRED","UNCONDITIONAL"]],
  "9":R+"Fremont office不是Microsoft Office。",
  "10":R+"Salary USD is not Universal Scene Description.",
  "11":R+"第三方招聘免责声明不是人力资源技能项。",
  "12":"DUPLICATE:E0319:4",
  "13":"DUPLICATE:E0319:6"
 },
 "old_overrides":{
  "O5":{"metric":"GENERAL","branch":"CHOICE","relation":"SKILL_REQUIREMENT","reason":"原Creo短词不唯一，改为CAD任选句。","quote":"Expert CAD user and familiarity with either Solidworks, Siemens NX, Creo or Onshape."},
  "O6":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"SKILL_REQUIREMENT","reason":"原Creo短词不唯一，改为同一CAD任选句。","quote":"Expert CAD user and familiarity with either Solidworks, Siemens NX, Creo or Onshape."},
  "O18":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"SKILL_REQUIREMENT","reason":"原actuators短词不唯一，改为传动件句。","quote":"harmonic drive actuators, etc."},
  "O22":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"SKILL_REQUIREMENT","reason":"原actuator短词不唯一，改为同一传动件句。","quote":"gears, splines, lead screws, linear guides, harmonic drive actuators"}
 },
 "additions":[],"outside_extra":[],
 "notes":"机械工程师。Jira/Confluence/Onshape/PLM/DFM保留。Creo/执行器继承改写。"
},
"N0937":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"COMPONENT_PROCESS","fine_task":"MECH_DESIGN","secondary_task":"",
 "task_evidence":"designing machined, sheet metal, and welded parts (preferably in OnShape",
 "new":{
  "1":[["V2_ONSHAPE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0937:1",
  "3":O+"Arena未单列冻结项。",
  "4":[["V2_APQP_PPAP","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0937:4",
  "6":"DUPLICATE:N0937:4",
  "7":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],
  "8":"DUPLICATE:N0937:7",
  "9":"DUPLICATE:N0937:7",
  "10":R+"Charlestown office不是Microsoft Office。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"高级机械设计。Onshape/PPAP/CNC保留。"
},
"N0020":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"STRUCT_CAMPUS","secondary_task":"",
 "task_evidence":"负责零部件图纸、组件图纸、生产标准、作业指导书、工艺流程图、DFMA（设计制造可行性分析）等相关设计与生产资料的编制和管理",
 "new":{
  "1":[["V2_DFM","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0020:1",
  "3":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],
  "4":"DUPLICATE:N0020:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"校招结构。DFM/3D打印保留。"
},
"E0011":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"LEGGED_STRUCT","secondary_task":"",
 "task_evidence":"熟练使用制图软件进行产品机械设计,(包含运动机构传动设计,结构细节设计,材料的选用等)",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"双足/四足结构。无新候选。"
},
"N0955":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"MTS_MECH","secondary_task":"",
 "task_evidence":"Apply Design for Manufacturing (DFM) and Design for Assembly (DFA) principles to transition prototypes into scalable builds",
 "new":{
  "1":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_ONSHAPE","GENERAL","CHOICE"]],
  "3":"DUPLICATE:N0955:2",
  "4":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_ANSYS","PREFERRED","CHOICE"]],
  "6":"DUPLICATE:N0955:5",
  "7":[["V2_DFM","GENERAL","UNCONDITIONAL"]],
  "8":R+"project management of technical projects不是Microsoft Project。",
  "9":R+"洛杉矶县工作安全条款不是客户服务技能。",
  "10":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"前沿机械。DFM/Onshape/Ansys/排障保留。"
},
"E0062":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"CHASSIS_STRUCT","secondary_task":"",
 "task_evidence":"负责人形机器人移动底盘及本体的结构设计工作",
 "new":{
  "1":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_AUTOCAD","GENERAL","CHOICE"],["V2_OFFICE","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机械设计。SOP/AutoCAD/Office办公软件保留。"
},
"E0456":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"COMPONENT_PROCESS","fine_task":"CONNECTOR","secondary_task":"",
 "task_evidence":"Own 3D CAD modeling and 2D detailed drawings for custom connectors, overmolds, and electromechanical interfaces",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_EMC_SIPI","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_PLM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "7":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],
  "8":[["V2_PLM","GENERAL","UNCONDITIONAL"]],
  "9":O+"Enovia未单列冻结项。",
  "10":R+"Oracle Agile PLM名称不是敏捷项目管理方法。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"连接器设计。DFM/EMC/采购/PLM/成型/排障保留。"
},
"E0145":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"THERMAL","fine_task":"THERMAL_ENG","secondary_task":"",
 "task_evidence":"负责关节模组、电机、驱动器、电池、计算平台和整机散热方案",
 "new":{},
 "old_overrides":{
  "O23":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原热设计短词不唯一，改为加分项整句。","quote":"做过电机热设计、汽车热管理、服务器散热、逆变器/电控散热、机器人关节热设计。"}
 },
 "additions":[],"outside_extra":[],
 "notes":"热管理。热设计继承改写。"
},
"N0235":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ACTUATOR_GEAR","fine_task":"JOINT_MODULE","secondary_task":"",
 "task_evidence":"负责机器人关节模组减速器和关节传动系统的研发工作",
 "new":{
  "1":[["V2_ANSYS","GENERAL","CHOICE"],["V2_KISSSOFT","GENERAL","CHOICE"]],
  "2":"DUPLICATE:N0235:1",
  "3":"DUPLICATE:N0235:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"关节模组。Ansys/KISSsoft保留。"
},
"E0587":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"COMPONENT_PROCESS","fine_task":"MECH_DESIGN","secondary_task":"",
 "task_evidence":"Drive all design decisions around 3D CAD, 2D drawings, material selection, and manufacturability",
 "new":{
  "1":[["V2_CNC_PROCESS","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_HALT_HASS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_EMC_SIPI","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_DOE_MSA","PREFERRED","CHOICE"],["V2_HALT_HASS","PREFERRED","CHOICE"]],
  "7":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],
  "8":"DUPLICATE:E0587:6"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机械设计。成型/HALT/EMC/DFM/DOE保留。"
},
"N0260":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"STRUCT_EXPERT","secondary_task":"",
 "task_evidence":"机器人结构方案设计与开发，包括关节结构、传动机构、末端执行器外围设备等",
 "new":{
  "1":[["V2_ANSYS","GENERAL","UNCONDITIONAL"]],
  "2":[["SK_CREO","GENERAL","CHOICE"]],
  "3":[["SK_NX","GENERAL","CHOICE"]],
  "4":"DUPLICATE:N0260:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"结构专家。Ansys/Proe/UG保留。"
},
"N0655":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"STRUCT_ENG","secondary_task":"",
 "task_evidence":"独立负责机器人整机或机械臂或灵巧手核心模块的结构设计",
 "new":{
  "1":R+"与工业设计协作不是本人承担CMF。",
  "2":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0655:2",
  "4":"DUPLICATE:N0655:2",
  "5":[["SK_CREO","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],
  "7":[["V2_ANSYS","PREFERRED","CHOICE"],["V2_ABAQUS","PREFERRED","CHOICE"]],
  "8":"DUPLICATE:N0655:7",
  "9":"DUPLICATE:N0655:7"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"结构工程师。DFM/Creo/成型/Ansys/Abaqus保留。"
},
"N0916":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"SENIOR_MECH","secondary_task":"",
 "task_evidence":"Produce production-grade engineering drawings with GD&T (ASME Y14.5)",
 "new":{
  "1":R+"Series C funding is not the C language.",
  "2":[["V2_GD_STANDARD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0916:2",
  "4":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0916:4",
  "6":"DUPLICATE:N0916:4",
  "7":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "8":O+"VA/VE未单列冻结项。",
  "9":[["V2_GD_STANDARD","GENERAL","UNCONDITIONAL"]],
  "10":"DUPLICATE:N0916:9",
  "11":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],
  "12":[["V2_INCIDENT_SUPPORT","PREFERRED","UNCONDITIONAL"]],
  "13":O+"MBD未单列冻结项。",
  "14":O+"VA/VE未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"高级机械。GD&T/DFM/采购/成型保留。英文can不记CAN。"
},
"E0095":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_STRUCTURE","fine_task":"MECH_ENG","secondary_task":"",
 "task_evidence":"机器人机械结构设计,新工艺尝试",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机械工程师。无新候选。"
}
}
if __name__=='__main__':
 register('RF_MECHANICAL_MECHATRONICS', decisions, reader='grok4.6')
