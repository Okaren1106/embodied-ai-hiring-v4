"""First-pass adjudication for data-infra coding_order 1-16. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
PIPE={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"FIELD_DATA_PLATFORM","secondary_task":"",
 "task_evidence":"Design and build the data platform, frameworks, and developer tooling that power ingestion across Field AI.",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":O+"REST/gRPC/webhooks未单列冻结项。",
  "3":"DUPLICATE:RID:2",
  "4":"DUPLICATE:RID:2",
  "5":O+"CDC未单列冻结项。",
  "6":R+"C++ is not the C language.",
  "7":O+"Scala未单列冻结项。",
  "8":[["V2_KAFKA","GENERAL","CHOICE"]],
  "9":"DUPLICATE:RID:8",
  "10":O+"Kinesis未单列冻结项。",
  "11":O+"Pub/Sub未单列冻结项。",
  "12":[["V2_AIRFLOW","GENERAL","CHOICE"]],
  "13":"DUPLICATE:RID:12",
  "14":O+"Dagster未单列冻结项。",
  "15":[["V2_SNOWFLAKE","GENERAL","CHOICE"],["V2_DATABRICKS","GENERAL","CHOICE"]],
  "16":O+"BigQuery未单列冻结项。",
  "17":"DUPLICATE:RID:15",
  "18":"DUPLICATE:RID:15",
  "19":O+"Redshift未单列冻结项。",
  "20":O+"ELT未单列冻结项。",
  "21":O+"Fivetran未单列冻结项。",
  "22":O+"Airbyte未单列冻结项。",
  "23":O+"Debezium未单列冻结项。",
  "24":[["V2_INCIDENT_SUPPORT","GENERAL","UNCONDITIONAL"]],
  "25":[["V2_MCAP","GENERAL","CHOICE"],["V2_ROSBAG","GENERAL","CHOICE"]],
  "26":"DUPLICATE:RID:25",
  "27":"DUPLICATE:RID:25"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FieldAI数据平台。Kafka/Airflow/Snowflake/Databricks/MCAP/rosbag保留。"
}
def pipe(rid, extra=None, n=27, evidence=None, notes=None, task_ft=None):
 d=dict(PIPE); d['new']=dict(PIPE['new'])
 for i in (3,4,9,13,17,18,26,27):
  src={3:2,4:2,9:8,13:12,17:15,18:15,26:25,27:25}[i]
  d['new'][str(i)]='DUPLICATE:%s:%s'%(rid,src)
 if extra: d['new'].update(extra)
 if evidence: d['task_evidence']=evidence
 if notes: d['notes']=notes
 if task_ft: d['fine_task']=task_ft
 return d
decisions={
"N0205":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"COLLECTION_SITE_OPS","secondary_task":"",
 "task_evidence":"作为数采场经营管理第一责任人，对数采场有效产能、数据质量和项目交付负责",
 "new":{
  "1":[["V2_PROCUREMENT","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数采场运营。外包供应商管理记采购优先。"
},
"N0728":pipe("N0728"),
"N0571":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"EGO_DATA_ALGO","secondary_task":"",
 "task_evidence":"探索 EgoCentric 数据在具身大模型中的应用，推动其在机器人学习、任务理解与策略训练中的落地",
 "new":{
  "1":[["V2_WORLD_MODEL","SEPARATE","BACKGROUND"]],
  "2":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_WORLD_MODEL","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0571:4",
  "6":[["V2_WORLD_MODEL","PREFERRED","UNCONDITIONAL"]],
  "7":O+"LIBERO未单列冻结项。",
  "8":O+"RoboCasa未单列冻结项。",
  "9":R+"LoRA/分布式训练不是模型压缩。",
  "10":O+"Transformers未单列冻结项。",
  "11":R+"LoRA不是模型压缩。",
  "12":O+"FluxVLA开源codebase未单列冻结项。",
  "13":[["V2_WORLD_MODEL","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Ego数据算法。World Model保留。LoRA不记压缩。Git协作保留。"
},
"N0404":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"AUTO_LABEL_VLM","secondary_task":"",
 "task_evidence":"负责基于 VLM 的具身智能数据预标注体系建设",
 "new":{
  "1":[["V2_POSTTRAINING","GENERAL","UNCONDITIONAL"]],
  "2":O+"CLIP未单列冻结项。",
  "3":O+"LLaVA未单列冻结项。",
  "4":"DUPLICATE:N0404:1",
  "5":"DUPLICATE:N0404:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据标注。SFT/RLHF保留。"
},
"E0364":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"FLEET_DATA_PLATFORM","secondary_task":"",
 "task_evidence":"Design and implement scalable data pipelines for ingesting and processing telemetry, logs and sensor data from our fleet of robots",
 "new":{
  "1":[["V2_SPARK","DUTY_OWN_USE","CHOICE"],["V2_KAFKA","DUTY_OWN_USE","CHOICE"]],
  "2":[["V2_AWS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_AWS","GENERAL","CHOICE"],["V2_GCP","GENERAL","CHOICE"],["V2_AZURE","GENERAL","CHOICE"]],
  "4":[["V2_SPARK","GENERAL","CHOICE"],["V2_FLINK","GENERAL","CHOICE"],["V2_KAFKA","GENERAL","CHOICE"]],
  "5":[["V2_PARQUET","GENERAL","EXAMPLE"]],
  "6":[["V2_PROMETHEUS","GENERAL","EXAMPLE"]],
  "7":[["V2_DATABRICKS","PREFERRED","CHOICE"],["V2_UNITY","PREFERRED","CHOICE"]],
  "8":[["V2_DATABRICKS","PREFERRED","UNCONDITIONAL"]],
  "9":[["V2_BAZEL","PREFERRED","UNCONDITIONAL"]],
  "10":R+"C++ is not the C language.",
  "11":[["V2_MCAP","PREFERRED","UNCONDITIONAL"]],
  "12":R+"Salary USD is not Universal Scene Description.",
  "13":R+"第三方招聘免责声明不是人力资源技能项。",
  "14":O+"fluentbit/OpenTelemetry未单列冻结项。",
  "15":[["V2_AWS","PREFERRED","EXAMPLE"]],
  "16":"DUPLICATE:E0364:4",
  "17":"DUPLICATE:E0364:7"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据平台。Spark/Kafka/云/Databricks/MCAP保留。Unity Catalog记Unity。"
},
"E0170":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"UMI_PIPELINE","secondary_task":"",
 "task_evidence":"负责开源无本体数据集与真实机器人自采数据的采集、筛选、清洗及规范化处理",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_GIT","GENERAL","UNCONDITIONAL"],["V2_PANDAS","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"UMI数据管线。后训练保留。WAM未写明世界动作模型不记世界模型。"
},
"N0101":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"MM_DATA_LOOP","secondary_task":"",
 "task_evidence":"设计并落地从数据清洗、标注、筛选、验证到入库的数据处理体系",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_POSTTRAINING","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_PANDAS","GENERAL","CHOICE"],["V2_SPARK","GENERAL","CHOICE"]],
  "4":"DUPLICATE:N0101:3",
  "5":"DUPLICATE:N0101:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"多模态数据算法。SFT/RLHF与Pandas/Spark保留。"
},
"E0073":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"DATA_FACTORY_PLATFORM","secondary_task":"",
 "task_evidence":"负责数据工厂平台的业务流程开发,实现数据采集任务派发、人员/设备调度、数据标注、质量监控等全流程管理功能",
 "new":{
  "1":[["V2_SQL_MYSQL","GENERAL","CHOICE"],["V2_POSTGRESQL","GENERAL","CHOICE"],["V2_MONGODB","GENERAL","CHOICE"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"AI平台。MySQL/PostgreSQL/MongoDB保留。"
},
"E0556":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"SHIFT_COORD_SP","secondary_task":"",
 "task_evidence":"Atuar em parceria com os Project Coordinators e o time de Data Quality para identificar e resolver problemas no momento da criação dos dados.",
 "new":{
  "1":R+"Project Coordinators不是Microsoft Project。",
  "2":[["V2_MOCAP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数创班次协调。动捕经验保留。"
},
"E0591":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"SHIFT_LEAD","secondary_task":"",
 "task_evidence":"Provide daily boots-on-the-ground leadership to drive data collection",
 "new":{
  "1":R+"English can is not Controller Area Network."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数采班组长。"
},
"N0510":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"AUTO_LABEL_NAV","secondary_task":"",
 "task_evidence":"负责具身导航数据自动标注算法研发与体系建设，提升标注效率，降低标注成本",
 "new":{
  "1":[["V2_MCAP","PREFERRED","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0510:1",
  "3":O+"OpenDrive未单列冻结项。",
  "4":O+"Apollo未单列冻结项。",
  "5":O+"Autoware未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"自动标注。MCAP保留。"
},
"N0991":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_OPS_SUPERVISOR","secondary_task":"",
 "task_evidence":"Oversee contractors and internal employees responsible for ML annotation tasks, robot teleoperation, and building data assets.",
 "new":{
  "1":[["V2_TELEOP","SEPARATE","BACKGROUND"]],
  "2":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_JIRA","GENERAL","UNCONDITIONAL"]],
  "4":"DUPLICATE:N0991:3",
  "5":O+"VR未单列冻结项。",
  "6":[["V2_JIRA","PREFERRED","CHOICE"],["V2_GOOGLE_WORKSPACE","PREFERRED","CHOICE"]],
  "7":"DUPLICATE:N0991:6",
  "8":"DUPLICATE:N0991:6"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据运营主管。遥操作监管保留。Jira/Google Workspace保留。"
},
"N0715":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PRODUCT","fine_task":"ANNOTATION_PM","secondary_task":"",
 "task_evidence":"Technical Product Manager - Data Annotation & Labelling",
 "new":{
  "1":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"标注产品经理。标题作任务证据因职责段为公司介绍。"
},
"N0956":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PRODUCT","fine_task":"DATA_STRATEGY_PM","secondary_task":"",
 "task_evidence":"Product Manager, Data Strategy & Physical AI to define and execute the long-term product vision",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":O+"privacy/legal/security pipelines未单列冻结项。",
  "3":"DUPLICATE:N0956:2",
  "4":R+"dataset pruning/token curation不是模型压缩。",
  "5":R+"English can is not Controller Area Network.",
  "6":O+"MLOps未单列冻结项。",
  "7":R+"洛杉矶县安全合作条款不是客服技能项。",
  "8":R+"招聘联系人不是人力资源技能项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FAR数据策略PM。"
},
"E0079":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"ROBOT_DATA_OPS","secondary_task":"",
 "task_evidence":"负责机器人数据工程的全流程实施,包括数据采集、清洗、审核、标注、归档、上传等",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机器人数据运营。无新候选。"
},
"N0316":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"EMBODIED_DATA_ALGO","secondary_task":"",
 "task_evidence":"构建高质量数据获取与管理流程，支撑具身智能模型训练与迭代",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"Python / C++不是C语言。",
  "4":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"具身数据算法。遥操作采集保留。"
}
}
if __name__=='__main__':
 register('RF_DATA_INFRA_OPERATIONS', decisions, reader='grok4.6')
