"""First-pass adjudication for data-infra coding_order 33-48. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"N0135":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"OLAP_MINING","secondary_task":"ANALYTICS",
 "task_evidence":"面向AI 模型数据挖掘、样本筛选、特征探查场景，搭建数据挖掘服务平台",
 "new":{
  "1":O+"OLAP引擎研发经验未单列冻结项。",
  "2":[["V2_CLICKHOUSE","PREFERRED","CHOICE"]],
  "3":O+"Apache Doris未单列冻结项。",
  "4":O+"StarRocks未单列冻结项。",
  "5":"DUPLICATE:N0135:2",
  "6":O+"Trino未单列冻结项。",
  "7":O+"Iceberg未单列冻结项。",
  "8":R+"Java/go/C++不是单独C语言项。",
  "9":[["V2_SPARK","PREFERRED","UNCONDITIONAL"],["V2_FLINK","PREFERRED","UNCONDITIONAL"]],
  "10":O+"湖仓一体架构表述未单列冻结项。",
  "11":"DUPLICATE:N0135:9",
  "12":"DUPLICATE:N0135:9"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"OLAP研发。ClickHouse/Spark/Flink保留。"
},
"N0094":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"DATA_SDK","secondary_task":"",
 "task_evidence":"将质量校验、清洗、标注、配比等业务逻辑抽象为单一职责的数据处理算子，集成至 Airflow / Ray 等调度框架",
 "new":{
  "1":[["V2_POSTTRAINING","SEPARATE","BACKGROUND"]],
  "2":[["V2_AWS","SEPARATE","BACKGROUND"]],
  "3":O+"类SQL或DSL未单列冻结项。",
  "4":"DUPLICATE:N0094:2",
  "5":[["V2_AIRFLOW","DUTY_OWN_USE","CHOICE"]],
  "6":"DUPLICATE:N0094:5",
  "7":[["V2_MCAP","DUTY_OWN_USE","CHOICE"],["V2_ROSBAG","DUTY_OWN_USE","CHOICE"]],
  "8":"DUPLICATE:N0094:7",
  "9":"DUPLICATE:N0094:7",
  "10":O+"HDF5未单列冻结项。",
  "11":O+"DSL未单列冻结项。",
  "12":[["V2_MCAP","GENERAL","CHOICE"],["V2_ROSBAG","GENERAL","CHOICE"]],
  "13":"DUPLICATE:N0094:12",
  "14":"DUPLICATE:N0094:12",
  "15":O+"HDF5未单列冻结项。",
  "16":R+"C++关键路径不是单独C语言项。",
  "17":O+"dataclass未单列冻结项。",
  "18":O+"asyncio未单列冻结项。",
  "19":[["V2_AIRFLOW","GENERAL","CHOICE"]],
  "20":"DUPLICATE:N0094:19",
  "21":O+"Open-X-Embodiment未单列冻结项。",
  "22":O+"DROID未单列冻结项。",
  "23":[["V2_CALIBRATION","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据SDK。Airflow/MCAP/rosbag/传感器标定保留。AWS ARN为类比对象。"
},
"N0309":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"COLLECTION_PLANT","secondary_task":"",
 "task_evidence":"全面负责数据采集工厂的日常运营，对数据采集任务的交付质量、效率、成本及安全负最终责任",
 "new":{
  "1":[["V2_RCA","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0309:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数采厂长。RCA保留。"
},
"N0305":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"SCENE_DESIGN","secondary_task":"",
 "task_evidence":"主导多模态具身智能数据采集的场景架构设计",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"场景设计。无新候选。"
},
"E0072":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"BIGDATA_ENGINE","secondary_task":"",
 "task_evidence":"负责具身智能大数据平台/引擎架构设计与核心组件开发",
 "new":{
  "1":[["V2_SPARK","GENERAL","CHOICE"],["V2_FLINK","GENERAL","CHOICE"],["V2_KAFKA","GENERAL","CHOICE"]],
  "2":[["V2_CLICKHOUSE","GENERAL","CHOICE"]],
  "3":"DUPLICATE:E0072:1"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"大数据平台。Spark/Flink/Kafka/ClickHouse保留。"
},
"E0065":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"DATA_QC_ALGO","secondary_task":"",
 "task_evidence":"负责多模态(视觉、触觉、语言、Action)数据的清洗算法研发",
 "new":{
  "1":R+"数据多样性量化分析不是模型压缩。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据模型算法。量化分析拒收压缩。"
},
"E0027":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"DATA_QC_TEST","secondary_task":"",
 "task_evidence":"搭建具身智能多模态采集数据的质检体系与量化标准",
 "new":{
  "1":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"质检测试。传感器标定保留。量化标准不记压缩。"
},
"E0081":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"MM_PIPELINE","secondary_task":"",
 "task_evidence":"设计高吞吐量数据流水线,用于摄取、验证和转换机器人多模态数据",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据管线。无新候选。"
},
"E0083":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ANALYTICS","fine_task":"DATA_EVAL","secondary_task":"",
 "task_evidence":"设计并实现机器人多模态交互数据的分布建模与处理体系,对大规模具身数据进行价值评估",
 "new":{
  "1":R+"数据质量与模型性能量化指标不是模型压缩。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据评估。量化指标拒收压缩。"
},
"E0297":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"MM_GT","secondary_task":"",
 "task_evidence":"您将深度参与下一代多模态大模型 (语言-视觉-动作) 的数据真值构建与评测工作",
 "new":{
  "1":R+"数据分布量化不是模型压缩。",
  "2":[["V2_PANDAS","GENERAL","UNCONDITIONAL"]],
  "3":O+"PCA/t-SNE未单列冻结项。",
  "4":"DUPLICATE:E0297:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"多模态数据真值。Pandas保留。"
},
"E0202":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"OUTSOURCE_OPS","secondary_task":"",
 "task_evidence":"负责采集团队日常管理:人员排班、任务分配、目标拆解、过程督导与绩效考核",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"数据运营外包。无新候选。"
},
"E0201":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DATA_OPERATIONS","fine_task":"EMBODIED_DATA_OPS","secondary_task":"",
 "task_evidence":"负责机器人训练数据的采集、清洗、标注、质检、交付全流程项目管理",
 "new":{
  "1":[["V2_PROCUREMENT","DUTY_OWN_USE","UNCONDITIONAL"],["V2_TELEOP","SEPARATE","BACKGROUND"],["V2_MOCAP","SEPARATE","BACKGROUND"]],
  "2":[["V2_SOP_OPERATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_CURSOR","PREFERRED","CHOICE"],["V2_CLAUDE_CODE","PREFERRED","CHOICE"]],
  "4":"DUPLICATE:E0201:3"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"具身数据运营。供应商管理记采购。SOP/Cursor/Claude Code保留。遥操动捕为供应商对象。"
},
"E0171":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"TACTILE_INFRA","secondary_task":"",
 "task_evidence":"负责多模态触觉数据采集与推理基础设施建设",
 "new":{
  "1":R+"Python / C++不是C语言。"
 },
 "old_overrides":{
  "O3":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为Python/C++与ROS/ROS2句。","quote":"熟悉 Python / C++，熟悉 ROS / ROS2"}
 },
 "additions":[],"outside_extra":[],
 "notes":"触觉Infra。ROS继承改写。"
},
"E0162":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"LLM_DATA_PLATFORM","secondary_task":"",
 "task_evidence":"负责机器人/多模态数据湖仓与高并发数据闭环平台建设",
 "new":{
  "1":[["V2_ROSBAG","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_ROSBAG","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_SPARK","GENERAL","CHOICE"],["V2_FLINK","GENERAL","CHOICE"],["V2_CLICKHOUSE","GENERAL","CHOICE"]],
  "5":[["V2_SQL_MYSQL","GENERAL","CHOICE"],["V2_POSTGRESQL","GENERAL","CHOICE"],["V2_KAFKA","GENERAL","CHOICE"]],
  "6":[["V2_CI_CD","PREFERRED","UNCONDITIONAL"]],
  "7":[["V2_CALIBRATION","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原Python短词定位为空，改为Python或Go句。","quote":"熟练 Python 或 Go，具备高并发服务、并发编程、异步任务、工程化开发和测试经验"},
  "O2":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原Go短词定位为空，改为同一Python或Go句。","quote":"熟练 Python 或 Go，具备高并发服务、并发编程、异步任务、工程化开发和测试经验"},
  "O3":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Python短词定位为空，改为双栈优先句。","quote":"Python/Go 双栈优先"},
  "O4":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Go短词定位为空，改为双栈优先句。","quote":"Python/Go 双栈优先"},
  "O6":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为ROS/ROS2和rosbag句。","quote":"熟悉 ROS/ROS2 和 rosbag，具备机器人多源数据解析、转换、同步或性能优化经验"}
 },
 "additions":[],"outside_extra":[],
 "notes":"大模型数据平台。rosbag/Spark/Kafka/CI/标定保留。"
},
"E0118":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"DATA_PIPELINE","fine_task":"MM_GT","secondary_task":"",
 "task_evidence":"您将深度参与下一代多模态大模型 (语言-视觉-动作) 的数据真值构建与评测工作",
 "new":{
  "1":R+"数据分布量化不是模型压缩。",
  "2":[["V2_PANDAS","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O7":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原多模态大模型短词定位为空，改为了解范式句。","quote":"了解多模态大模型范式，熟悉多模态数据的清洗/标注/统计方式"},
  "O9":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原多模态大模型短词定位为空，改为训练经验加分句。","quote":"有实际多模态大模型训练经验"}
 },
 "additions":[],"outside_extra":[],
 "notes":"多模态数据真值。Pandas保留。大模型继承改写。"
},
"E0307":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ANALYTICS","fine_task":"CI_ANALYST","secondary_task":"",
 "task_evidence":"Own process improvement initiatives end-to-end using a structured, DMAIC style approach",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_LEAN","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"English can is not Controller Area Network.",
  "4":[["V2_JIRA","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":R+"English can is not Controller Area Network.",
  "6":[["V2_LEAN","PREFERRED","UNCONDITIONAL"]],
  "7":[["V2_VISIO","GENERAL","CHOICE"],["V2_MIRO","GENERAL","CHOICE"]],
  "8":R+"English can is not Controller Area Network.",
  "9":R+"English can is not Controller Area Network.",
  "10":R+"English can is not Controller Area Network.",
  "11":[["V2_JIRA","PREFERRED","CHOICE"],["V2_MS_PROJECT","PREFERRED","CHOICE"]],
  "12":[["V2_POWERBI","PREFERRED","UNCONDITIONAL"]],
  "13":R+"Salem office不是Microsoft Office。",
  "14":R+"Salary USD is not Universal Scene Description.",
  "15":R+"第三方招聘免责声明不是人力资源技能项。",
  "16":"DUPLICATE:E0307:6",
  "17":"DUPLICATE:E0307:7",
  "18":"DUPLICATE:E0307:11",
  "19":"DUPLICATE:E0307:12"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"持续改进分析。Lean/Jira/Visio/Miro/PowerBI保留。MS Project未单记。"
}
}
if __name__=='__main__':
 register('RF_DATA_INFRA_OPERATIONS', decisions, reader='grok4.6')
