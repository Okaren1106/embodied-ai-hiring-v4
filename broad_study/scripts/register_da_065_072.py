"""First-pass adjudication for data-infra coding_order 65-72. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"N0899":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"ANNOTATION_MGR","secondary_task":"",
 "task_evidence":"3+ years in data operations, annotation/labeling operations, or data collection QA for ML systems",
 "new":{
  "1":R+"Series C funding不是C语言。",
  "2":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]],
  "3":O+"BI tools未单列冻结项。",
  "4":O+"AI-assisted未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据质量标注经理。遥操作数据经验保留。"
},
"N0898":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"COLLECTION_SUPERVISOR","secondary_task":"",
 "task_evidence":"Coordinate with on-site technicians to keep rigs running — triage issues fast, minimize downtime",
 "new":{
  "1":R+"Series C funding不是C语言。",
  "2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_MOCAP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数采主管。故障排查与动捕保留。"
},
"E0578":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"ML_DATA_SYSTEMS","secondary_task":"",
 "task_evidence":"Design and build high-throughput pipelines that validate, transform, and featurize raw multimodal data",
 "new":{
  "1":[["V2_SPARK","GENERAL","CHOICE"],["V2_FLINK","GENERAL","CHOICE"],["V2_CLICKHOUSE","GENERAL","CHOICE"]],
  "2":"DUPLICATE:E0578:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"ML Infra数据系统。ClickHouse/Flink/Spark保留。"
},
"E0603":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"ANNOTATION_LEAD","secondary_task":"",
 "task_evidence":"Own annotation operations end-to-end: throughput, quality, cost, and on-time delivery across all annotation types.",
 "new":{
  "1":R+"annotator calibration不是传感器标定。",
  "2":R+"project leads不是Microsoft Project。"
 },
 "old_overrides":{
  "O7":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原ML短词定位为空，改为自动标注与模型辅助标注句。","quote":"Experience integrating autolabeling and model-based annotation into human workflows"}
 },
 "additions":[],"outside_extra":[],
 "notes":"标注负责人。ML继承改写。"
},
"E0608":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_QA_ENG","secondary_task":"",
 "task_evidence":"Build and run the end-to-end QA process for multimodal data ingested from third-party vendors and partners",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据质量软件。无新候选。"
},
"N0703":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"MASTER_ANNOTATOR","secondary_task":"",
 "task_evidence":"This role will act as the gold standard authority for labeling tasks, own Inter-Annotator Agreement (IAA) measurement, train and calibrate annotators",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"calibrate annotators不是传感器标定。",
  "3":O+"Inter-Annotator Agreement/kappa未单列冻结项。",
  "4":"DUPLICATE:N0703:3",
  "5":O+"Cohen’s/Fleiss’ kappa未单列冻结项。",
  "6":R+"structured calibration sessions不是传感器标定。",
  "7":O+"Inter-Annotator Agreement methodologies未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"主标注员。标注校准拒收传感器标定。"
},
"N0679":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_INFRA_PM_IN","secondary_task":"",
 "task_evidence":"Operations Program Manager – Data Infrastructure to design and scale operational processes that power our robotics foundation mod",
 "new":{
  "1":R+"公司/办公介绍不是Microsoft Office。",
  "2":[["V2_LEAN","GENERAL","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0679:2",
  "4":"DUPLICATE:N0679:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"印度数据基建运营PM。Lean/Six Sigma保留。"
},
"N0682":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"COLLECTION_PM_IN","secondary_task":"",
 "task_evidence":"Drive end-to-end program management for egocentric/UMI/teleops data collection and annotation workflows",
 "new":{
  "1":O+"egocentric/UMI/teleops program management未把项目管理记为Microsoft Project。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"印度数采标注PM。目录外项目管理表述。"
}
}
if __name__=='__main__':
 register('RF_DATA_INFRA_OPERATIONS', decisions, reader='grok4.6')
