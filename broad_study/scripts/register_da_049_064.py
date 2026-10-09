"""First-pass adjudication for data-infra coding_order 49-64. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
OPS= {
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_OPS_SUPERVISOR","secondary_task":"",
 "task_evidence":"Oversee contractors and internal employees responsible for ML annotation tasks, robot teleoperation, and building data assets.",
 "new":{
  "1":[["V2_TELEOP","SEPARATE","BACKGROUND"]],
  "2":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_JIRA","GENERAL","UNCONDITIONAL"]],
  "4":"DUPLICATE:RID:3",
  "5":O+"VR未单列冻结项。",
  "6":[["V2_JIRA","PREFERRED","CHOICE"],["V2_GOOGLE_WORKSPACE","PREFERRED","CHOICE"]],
  "7":"DUPLICATE:RID:6",
  "8":"DUPLICATE:RID:6"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据运营主管。遥操作监管保留。"
}
def ops(rid):
 d=dict(OPS); d['new']=dict(OPS['new'])
 d['new']['4']='DUPLICATE:%s:3'%rid
 d['new']['7']='DUPLICATE:%s:6'%rid
 d['new']['8']='DUPLICATE:%s:6'%rid
 return d
decisions={
"E0344":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ANALYTICS","fine_task":"ROBOT_DS","secondary_task":"",
 "task_evidence":"Build models that predict MTBF and remaining useful life for specific components",
 "new":{
  "1":[["V2_RCA","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":R+"English can is not Controller Area Network.",
  "3":R+"Salary USD is not Universal Scene Description.",
  "4":R+"第三方招聘免责声明不是人力资源技能项。"
 },
 "old_overrides":{
  "O3":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原survival analysis短词定位为空，改为可靠性与生存分析句。","quote":"PhD and coursework/experience in reliability engineering, survival analysis, or applied statistics preferred"},
  "O4":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原survival analysis短词定位为空，改为同一可靠性与生存分析句。","quote":"PhD and coursework/experience in reliability engineering, survival analysis, or applied statistics preferred"},
  "O17":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"OWN_USE","reason":"原reliability短词定位为空，改为预测性维护与硬件可靠性句。","quote":"Predictive maintenance & hardware reliability"}
 },
 "additions":[],"outside_extra":[],
 "notes":"机器人数据科学家。RCA保留。生存分析继承改写。"
},
"N0959":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"FAR_DATA_PLATFORM","secondary_task":"",
 "task_evidence":"you will build and maintain the data infrastructure that powers our robotics manipulation research",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_TYPESCRIPT","DUTY_OWN_USE","UNCONDITIONAL"],["V2_REACT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_TYPESCRIPT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_REACT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":R+"English can is not Controller Area Network.",
  "6":O+"ETL processes未单列冻结项。",
  "7":R+"洛杉矶县安全合作条款不是客服技能项。",
  "8":R+"招聘联系人不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FAR数据平台。TypeScript/React保留。"
},
"N1022":ops("N1022"),
"N1020":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"ATLAS_DATA_TPM","secondary_task":"",
 "task_evidence":"to own data quality and annotation operations for Atlas",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Atlas数据运营TPM。无新候选。标题若无法定位将改写。"
},
"N0812":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_OPS_ENG","secondary_task":"",
 "task_evidence":"Run motion capture, teleoperation, and human-subjects data collection sessions yourself",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"],["V2_MOCAP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_MOCAP","GENERAL","EXAMPLE"]],
  "3":O+"Vicon未单列冻结项。",
  "4":O+"OptiTrack未单列冻结项。",
  "5":R+"3D scanning and 3D printing不是CNC工艺。",
  "6":O+"IRB/consent未单列冻结项。",
  "7":[["V2_BLENDER","PREFERRED","CHOICE"],["V2_UNITY","PREFERRED","CHOICE"]],
  "8":"DUPLICATE:N0812:7",
  "9":"DUPLICATE:N0812:7",
  "10":R+"English can is not Controller Area Network.",
  "11":R+"English can is not Controller Area Network.",
  "12":R+"English can is not Controller Area Network."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据运营工程师。遥操/动捕/Blender/Unity保留。"
},
"N0836":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"DATA_ENG","secondary_task":"",
 "task_evidence":"Build reliable ingestion, transformation, and orchestration workflows using tools such as Airflow.",
 "new":{
  "1":[["V2_AIRFLOW","DUTY_OWN_USE","EXAMPLE"]],
  "2":"DUPLICATE:N0836:1",
  "3":[["V2_AWS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":"DUPLICATE:N0836:3",
  "5":[["V2_AIRFLOW","GENERAL","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0836:5",
  "7":[["V2_AWS","GENERAL","EXAMPLE"]],
  "8":O+"S3未单列冻结项。",
  "9":O+"Lambda未单列冻结项。",
  "10":O+"ECS未单列冻结项。",
  "11":O+"EC2未单列冻结项。",
  "12":O+"RDS未单列冻结项。",
  "13":O+"Redshift未单列冻结项。",
  "14":O+"Glue未单列冻结项。",
  "15":O+"Athena未单列冻结项。",
  "16":O+"SQS未单列冻结项。",
  "17":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "18":[["V2_AWS","PREFERRED","CHOICE"],["V2_TERRAFORM","PREFERRED","CHOICE"]],
  "19":"DUPLICATE:N0836:18",
  "20":"DUPLICATE:N0836:18",
  "21":O+"CloudFormation未单列冻结项。",
  "22":[["V2_SNOWFLAKE","PREFERRED","CHOICE"],["V2_DATABRICKS","PREFERRED","CHOICE"]],
  "23":O+"Redshift未单列冻结项。",
  "24":"DUPLICATE:N0836:22",
  "25":O+"BigQuery未单列冻结项。",
  "26":"DUPLICATE:N0836:22",
  "27":O+"Athena未单列冻结项。",
  "28":[["V2_CI_CD","PREFERRED","UNCONDITIONAL"]],
  "29":"DUPLICATE:N0836:28"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据工程。Airflow/AWS/Terraform/Snowflake/Databricks/CI保留。"
},
"E0486":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"HELIX_DATA_INFRA","secondary_task":"",
 "task_evidence":"Design, build, and maintain tools and software components that offload, store, manipulate and provide access to robot data",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。",
  "2":[["V2_SQL_MYSQL","GENERAL","CHOICE"],["V2_POSTGRESQL","GENERAL","CHOICE"],["V2_REDIS","GENERAL","CHOICE"]],
  "3":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"]],
  "4":[["V2_SLURM","GENERAL","CHOICE"]],
  "5":[["V2_TERRAFORM","GENERAL","CHOICE"],["V2_ANSIBLE","GENERAL","CHOICE"]],
  "6":"DUPLICATE:E0486:2",
  "7":"DUPLICATE:E0486:4",
  "8":"DUPLICATE:E0486:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Helix数据基建。数据库/云/Slurm/Terraform/Ansible保留。"
},
"E0458":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_STRATEGY_ASSOC","secondary_task":"",
 "task_evidence":"Own end-to-end execution of running robot data collection in diverse residential homes",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。",
  "2":R+"program/project management不是Microsoft Project。",
  "3":[["V2_GOOGLE_WORKSPACE","GENERAL","UNCONDITIONAL"]],
  "4":R+"English can is not Controller Area Network.",
  "5":"DUPLICATE:E0458:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据策略助理。Google Workspace保留。"
},
"E0511":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DQ_PARTNERSHIPS","secondary_task":"",
 "task_evidence":"Own the full external vendor portfolio for Data Quality: sourcing, evaluation, onboarding, and offboarding of data labeling and review partners.",
 "new":{
  "1":R+"you'll/project/calibration不是MS Project或传感器标定。",
  "2":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"Project Coordinators不是Microsoft Project。",
  "4":R+"vendor calibration/golden set不是传感器标定。",
  "5":R+"project timelines不是Microsoft Project。",
  "6":R+"which projects rotate不是Microsoft Project。",
  "7":R+"audit or calibration processes不是传感器标定。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据质量合作。供应商组合记采购。"
},
"E0537":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_CREATORS_PC","secondary_task":"",
 "task_evidence":"Own a data collection project end to end, from setup through delivery, against timeline and quality targets.",
 "new":{
  "1":R+"English can is not Controller Area Network; data collection project不是Microsoft Project。",
  "2":R+"data collection project不是Microsoft Project。",
  "3":R+"your project不是Microsoft Project。",
  "4":R+"your project's data不是Microsoft Project。",
  "5":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "6":R+"your project type不是Microsoft Project。",
  "7":R+"ownership of a project不是Microsoft Project。",
  "8":R+"keeping a project on schedule不是Microsoft Project。",
  "9":R+"contact for a project不是Microsoft Project。",
  "10":[["V2_MOCAP","PREFERRED","UNCONDITIONAL"]],
  "11":[["V2_MOCAP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数创项目协调。动捕保留。项目管理不记MS Project。SOP保留。"
},
"E0538":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_QUALITY_PC","secondary_task":"",
 "task_evidence":"Own review guidelines and acceptance criteria for your project; handle escalated edge cases that fall outside existing guidance.",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。",
  "2":R+"English can is not Controller Area Network; project lifecycle不是Microsoft Project。",
  "3":R+"your project不是Microsoft Project。",
  "4":R+"your project type不是Microsoft Project。",
  "5":R+"project-level audit不是Microsoft Project。",
  "6":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "7":R+"project-specific training/calibration不是传感器标定或Microsoft Project。",
  "8":R+"project-level vendor coordination不是Microsoft Project。",
  "9":R+"project-level clarifications不是Microsoft Project。",
  "10":R+"ownership of a project不是Microsoft Project。",
  "11":R+"training or calibration programs不是传感器标定。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据质量项目协调。SOP保留。标注校准拒收传感器标定。"
},
"E0510":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"GLOBAL_EXPANSION","secondary_task":"",
 "task_evidence":"you will own Figure’s data operations expansion: the strategy for where we go next and the team that gets us there",
 "new":{
  "1":R+"公司介绍不是Microsoft Office。",
  "2":R+"project management instincts不是Microsoft Project。",
  "3":R+"in-office collaboration不是Microsoft Office。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据运营全球拓展。"
},
"E0457":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"COLLECTION_QC","secondary_task":"",
 "task_evidence":"Review data collection sessions against established quality standards",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数采质量支持。无新候选。"
},
"E0451":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"AI_DATA_OPS_MGR","secondary_task":"",
 "task_evidence":"you will own a meaningful piece of Figure's data collection operation",
 "new":{
  "1":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"project management instincts不是Microsoft Project。",
  "3":R+"in-office collaboration不是Microsoft Office。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"AI数据运营经理。本地供应商记采购。"
},
"E0539":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_CREATORS_CDMX","secondary_task":"",
 "task_evidence":"Trabajar en conjunto con los Project Coordinators y el equipo de Data Quality para identificar y resolver problemas en el momento de la creación",
 "new":{
  "1":R+"construyendo/base de datos不是C语言。",
  "2":R+"Project Coordinators不是Microsoft Project。",
  "3":[["V2_MOCAP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"墨西哥城数创。动捕保留。"
},
"N0897":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"COLLECTION_MGR","secondary_task":"",
 "task_evidence":"Hire at volume in partnership with recruiting: run working interviews, make offer decisions for operators and supervisors",
 "new":{
  "1":R+"Series C funding不是C语言。",
  "2":[["V2_HR","DUTY_OWN_USE","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数采经理。与招聘配合招人记人力职责。"
}
}
if __name__=='__main__':
 register('RF_DATA_INFRA_OPERATIONS', decisions, reader='grok4.6')
