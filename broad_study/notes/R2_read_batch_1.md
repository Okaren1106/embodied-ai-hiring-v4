## E0248 CN_XSQUARE 机器人软件开发工程师

identity REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_XSQUARE|feishu|7591412518296406310|d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34

TREE {"schema_version": 1, "rationale": "正文并列负责应用UI/SDK、专用模型推理和版本化RL数据Pipeline，未说明后二者从属。旧理由写了主线，但没有对应的原文主次证据。", "expression": {"id": "E0248:root", "relation": "ALL", "scope": "JOB_RESPONSIBILITIES", "rationale": "正文并列负责应用UI/SDK、专用模型推理和版本化RL数据Pipeline，未说明后二者从属。旧理由写了主线，但没有对应的原文主次证据。", "evidence": [{"record_id": "CN_XSQUARE|feishu|7591412518296406310", "text_version_hash": "d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34", "field": "full_description", "start": 7, "end": 26, "quote": "负责 UI 采数与模型推理交互模块开发"}], "children": [{"id": "E0248:ui", "relation": "ROLE", "value": "RF_ROBOTICS_SOFTWARE", "surface": "负责 UI 采数与模型推理交互模块开发", "evidence": [{"record_id": "CN_XSQUARE|feishu|7591412518296406310", "text_version_hash": "d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34", "field": "full_description", "start": 7, "end": 68, "quote": "负责 UI 采数与模型推理交互模块开发：基于 ROS2 实现数据获取、机器人控制、采集任务配置、实时可视化展示与模型交互。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责 UI 采数与模型推理交互模块开发：基于 ROS2 实现数据获取、机器人控制、采集任务配置、实时可视化展示与模型交互。", "evidence": [{"record_id": "CN_XSQUARE|feishu|7591412518296406310", "text_version_hash": "d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34", "field": "full_description", "start": 7, "end": 68, "quote": "负责 UI 采数与模型推理交互模块开发：基于 ROS2 实现数据获取、机器人控制、采集任务配置、实时可视化展示与模型交互。"}]}, {"summary": "基于内部机器人 SDK 平台开发，抽象多机型统一接口与组件化能力，沉淀可复用模块、示例工程与二次开发文档。", "evidence": [{"record_id": "CN_XSQUARE|feishu|7591412518296406310", "text_version_hash": "d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34", "field": "full_description", "start": 277, "end": 330, "quote": "基于内部机器人 SDK 平台开发，抽象多机型统一接口与组件化能力，沉淀可复用模块、示例工程与二次开发文档。"}]}]}, {"id": "E0248:inf", "relation": "ROLE", "value": "RF_ML_AI_ENGINEERING", "surface": "负责模型推理工程化集成与部署", "evidence": [{"record_id": "CN_XSQUARE|feishu|7591412518296406310", "text_version_hash": "d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34", "field": "full_description", "start": 121, "end": 168, "quote": "负责模型推理工程化集成与部署：对接内部模型推理框架，实现批量实时推理、模型传输与模型版本更新。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责模型推理工程化集成与部署：对接内部模型推理框架，实现批量实时推理、模型传输与模型版本更新。", "evidence": [{"record_id": "CN_XSQUARE|feishu|7591412518296406310", "text_version_hash": "d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34", "field": "full_description", "start": 121, "end": 168, "quote": "负责模型推理工程化集成与部署：对接内部模型推理框架，实现批量实时推理、模型传输与模型版本更新。"}]}]}, {"id": "E0248:pipe", "relation": "ROLE", "value": "RF_DATA_INFRA_OPERATIONS", "surface": "根据强化学习（RL）训练/评测流程开发数据 Pipeline", "evidence": [{"record_id": "CN_XSQUARE|feishu|7591412518296406310", "text_version_hash": "d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34", "field": "full_description", "start": 171, "end": 274, "quote": "根据强化学习（RL）训练/评测流程开发数据 Pipeline：trajectory/episode 构建（obs/action/reward）、数据集切分与版本化、离线评测指标统计与回归验证（仿真/实机）。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "根据强化学习（RL）训练/评测流程开发数据 Pipeline：trajectory/episode 构建（obs/action/reward）、数据集切分与版本化、离线评测指标统计与回归验证（仿真/实机）。", "evidence": [{"record_id": "CN_XSQUARE|feishu|7591412518296406310", "text_version_hash": "d2a74e197dab91878a17f32e8ad5638ea95f547340593fae2f86923e9cda8d34", "field": "full_description", "start": 171, "end": 274, "quote": "根据强化学习（RL）训练/评测流程开发数据 Pipeline：trajectory/episode 构建（obs/action/reward）、数据集切分与版本化、离线评测指标统计与回归验证（仿真/实机）。"}]}]}]}}

ACT_DEPLOYMENT [{"end": 130, "field": "duties", "method": "UNIQUE_EXACT_QUOTE", "quote": "负责模型推理工程化集成与部署", "start": 116}]

ACT_ENGINEERING [{"end": 21, "field": "duties", "method": "UNIQUE_EXACT_QUOTE", "quote": "负责 UI 采数与模型推理交互模块开发", "start": 2}]

ACT_QUALITY [{"end": 76, "field": "duties", "method": "UNIQUE_EXACT_QUOTE", "quote": "负责校验数据采集系统", "start": 66}]

DUTIES

- 负责 UI 采数与模型推理交互模块开发:基于 ROS2 实现数据获取、机器人控制、采集任务配置、实时可视化展示与模型交互。
- 负责校验数据采集系统:多传感器数据接入与时间同步、rosbag2 录包与回放、数据质量校验等。
- 负责模型推理工程化集成与部署:对接内部模型推理框架,实现批量实时推理、模型传输与模型版本更新。
- 根据强化学习(RL)训练/评测流程开发数据 Pipeline:trajectory/episode 构建(obs/action/reward)、数据集切分与版本化、离线评测指标统计与回归验证(仿真/实机)。
- 基于内部机器人 SDK 平台开发,抽象多机型统一接口与组件化能力,沉淀可复用模块、示例工程与二次开发文档。

REQUIREMENTS

- 本科及以上,计算机/自动化/机器人相关专业。
- 熟练 C++,掌握数据结构、计算机网络、操作系统等基础知识,具备良好工程化能力与代码质量意识。
- 熟悉 Linux 开发环境与常用命令,具备调试与性能分析能力。
- 熟悉 ROS2等生命周期管理,可独立完成模块化节点设计与系统集成。
- 具备 AI 推理落地能力:了解深度学习基础与端侧部署要点,能完成模型导出与推理集成。
- 理解 RL 基本流程与数据形态,能围绕训练/评测闭环构建数据采集、回放复现、数据集管理与指标体系。
- 理解设计模式与接口抽象,能够在复杂系统中进行模块解耦与可维护架构设计。
- 有RL经验/顶会论文/竞赛经历(Robomaster/Robocon)者优先。

FULL_DESCRIPTION

岗位职责
- 负责 UI 采数与模型推理交互模块开发：基于 ROS2 实现数据获取、机器人控制、采集任务配置、实时可视化展示与模型交互。
- 负责校验数据采集系统：多传感器数据接入与时间同步、rosbag2 录包与回放、数据质量校验等。
- 负责模型推理工程化集成与部署：对接内部模型推理框架，实现批量实时推理、模型传输与模型版本更新。
- 根据强化学习（RL）训练/评测流程开发数据 Pipeline：trajectory/episode 构建（obs/action/reward）、数据集切分与版本化、离线评测指标统计与回归验证（仿真/实机）。
- 基于内部机器人 SDK 平台开发，抽象多机型统一接口与组件化能力，沉淀可复用模块、示例工程与二次开发文档。

任职要求
- 本科及以上，计算机/自动化/机器人相关专业。
- 熟练 C++，掌握数据结构、计算机网络、操作系统等基础知识，具备良好工程化能力与代码质量意识。
- 熟悉 Linux 开发环境与常用命令，具备调试与性能分析能力。
- 熟悉 ROS2等生命周期管理，可独立完成模块化节点设计与系统集成。
- 具备 AI 推理落地能力：了解深度学习基础与端侧部署要点，能完成模型导出与推理集成。
- 理解 RL 基本流程与数据形态，能围绕训练/评测闭环构建数据采集、回放复现、数据集管理与指标体系。
- 理解设计模式与接口抽象，能够在复杂系统中进行模块解耦与可维护架构设计。
- 有RL经验/顶会论文/竞赛经历（Robomaster/Robocon）者优先。

## N0109 CN_GALBOT 产测工程师

identity REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_GALBOT|moka|7f2d4260-eb00-421d-bd86-8f499f0c8c1d|1761ca1b57e0c62374cced04d00b6c60dd39f8ec512a0afc5bdedef26654d35a

TREE {"schema_version": 1, "rationale": "同一人开发可反复使用的产测设备，又承担新产品试产测试及问题闭环；后者超过对自己工具的验收自测。", "expression": {"id": "N0109:root", "relation": "ALL", "scope": "JOB_RESPONSIBILITIES", "rationale": "同一人开发可反复使用的产测设备，又承担新产品试产测试及问题闭环；后者超过对自己工具的验收自测。", "evidence": [{"record_id": "CN_GALBOT|moka|7f2d4260-eb00-421d-bd86-8f499f0c8c1d", "text_version_hash": "1761ca1b57e0c62374cced04d00b6c60dd39f8ec512a0afc5bdedef26654d35a", "field": "full_description", "start": 69, "end": 80, "quote": "负责产测设备、工装开发"}], "children": [{"id": "N0109:tool", "relation": "ROLE", "value": "RF_SIMULATION_EVALUATION", "surface": "负责产测设备、工装开发", "evidence": [{"record_id": "CN_GALBOT|moka|7f2d4260-eb00-421d-bd86-8f499f0c8c1d", "text_version_hash": "1761ca1b57e0c62374cced04d00b6c60dd39f8ec512a0afc5bdedef26654d35a", "field": "full_description", "start": 69, "end": 81, "quote": "负责产测设备、工装开发。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责产测设备、工装开发。", "evidence": [{"record_id": "CN_GALBOT|moka|7f2d4260-eb00-421d-bd86-8f499f0c8c1d", "text_version_hash": "1761ca1b57e0c62374cced04d00b6c60dd39f8ec512a0afc5bdedef26654d35a", "field": "full_description", "start": 69, "end": 81, "quote": "负责产测设备、工装开发。"}]}, {"summary": "负责制定新产品标定及产测流程，输出产测SOP。", "evidence": [{"record_id": "CN_GALBOT|moka|7f2d4260-eb00-421d-bd86-8f499f0c8c1d", "text_version_hash": "1761ca1b57e0c62374cced04d00b6c60dd39f8ec512a0afc5bdedef26654d35a", "field": "full_description", "start": 42, "end": 65, "quote": "负责制定新产品标定及产测流程，输出产测SOP。"}]}]}, {"id": "N0109:qual", "relation": "ROLE", "value": "RF_MANUFACTURING_QUALITY_SUPPLY", "surface": "负责新产品试产测试部分", "evidence": [{"record_id": "CN_GALBOT|moka|7f2d4260-eb00-421d-bd86-8f499f0c8c1d", "text_version_hash": "1761ca1b57e0c62374cced04d00b6c60dd39f8ec512a0afc5bdedef26654d35a", "field": "full_description", "start": 101, "end": 153, "quote": "负责新产品试产测试部分，包含产线测试环境搭建、测试跟进、测试问题解决，输出试产测试问题点列表和改善建议。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责新产品试产测试部分，包含产线测试环境搭建、测试跟进、测试问题解决，输出试产测试问题点列表和改善建议。", "evidence": [{"record_id": "CN_GALBOT|moka|7f2d4260-eb00-421d-bd86-8f499f0c8c1d", "text_version_hash": "1761ca1b57e0c62374cced04d00b6c60dd39f8ec512a0afc5bdedef26654d35a", "field": "full_description", "start": 101, "end": 153, "quote": "负责新产品试产测试部分，包含产线测试环境搭建、测试跟进、测试问题解决，输出试产测试问题点列表和改善建议。"}]}]}]}}

ACT_ENGINEERING [{"end": 81, "field": "full_description", "method": "RECOVER_END_FROM_QUOTE", "quote": "负责产测设备、工装开发。", "start": 69}]

ACT_QUALITY [{"end": 97, "field": "full_description", "method": "RECOVER_END_FROM_QUOTE", "quote": "负责产测工具验证和验收。", "start": 85}]

DUTIES

职责：

1.参与新产品测试评审，提出产测工具需求，推动相关部门开发和改善。

2.负责制定新产品标定及产测流程，输出产测SOP。

3.负责产测设备、工装开发。

4.负责产测工具验证和验收。

5.负责新产品试产测试部分，包含产线测试环境搭建、测试跟进、测试问题解决，输出试产测试问题点列表和改善建议。

6.持续推动产测效率提升。




任职要求：

1.本科及以上学历，机械、自动化、测控、计算机等相关专业，工业和消费电子行业3年以上、机器人行业1年以上产测工程师经验；

2.了解机器人标定，熟悉产线测试（含板端和整机）全流程；

3.具备一定的硬件和软件功底 ，有能力对标定和产测问题做基础分析和定位。

4.工作认真负责，具备较强的协调沟通能力与抗压能力；

## N0312 CN_PAXINI 初级具身智能算法工程师

identity REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_PAXINI|zhiye|48deb1a8-bb0a-4d7b-bc3c-38160be12b40|b83ef2a17be429bfc9f027c0e767caadc0d2b335e4d90a549eb6737354f02bd4

TREE {"schema_version": 1, "rationale": "数据工程、跨场景构型Benchmark、训练专用环境维护均写负责。协助训练不等于本人独立训练模型；但训练系统运维本身是ML工程交付。初级职位不是不能复合的理由。", "expression": {"id": "N0312:root", "relation": "ALL", "scope": "JOB_RESPONSIBILITIES", "rationale": "数据工程、跨场景构型Benchmark、训练专用环境维护均写负责。协助训练不等于本人独立训练模型；但训练系统运维本身是ML工程交付。初级职位不是不能复合的理由。", "evidence": [{"record_id": "CN_PAXINI|zhiye|48deb1a8-bb0a-4d7b-bc3c-38160be12b40", "text_version_hash": "b83ef2a17be429bfc9f027c0e767caadc0d2b335e4d90a549eb6737354f02bd4", "field": "full_description", "start": 5, "end": 11, "quote": "1.数据工程"}], "children": [{"id": "N0312:data", "relation": "ROLE", "value": "RF_DATA_INFRA_OPERATIONS", "surface": "1.数据工程", "evidence": [{"record_id": "CN_PAXINI|zhiye|48deb1a8-bb0a-4d7b-bc3c-38160be12b40", "text_version_hash": "b83ef2a17be429bfc9f027c0e767caadc0d2b335e4d90a549eb6737354f02bd4", "field": "full_description", "start": 5, "end": 52, "quote": "1.数据工程： 负责海量机器人遥操作数据的采集、清洗、标注及标准化处理，搭建高效的数据流水线。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "1.数据工程： 负责海量机器人遥操作数据的采集、清洗、标注及标准化处理，搭建高效的数据流水线。", "evidence": [{"record_id": "CN_PAXINI|zhiye|48deb1a8-bb0a-4d7b-bc3c-38160be12b40", "text_version_hash": "b83ef2a17be429bfc9f027c0e767caadc0d2b335e4d90a549eb6737354f02bd4", "field": "full_description", "start": 5, "end": 52, "quote": "1.数据工程： 负责海量机器人遥操作数据的采集、清洗、标注及标准化处理，搭建高效的数据流水线。"}]}]}, {"id": "N0312:bench", "relation": "ROLE", "value": "RF_SIMULATION_EVALUATION", "surface": "负责在多场景、多构型下", "evidence": [{"record_id": "CN_PAXINI|zhiye|48deb1a8-bb0a-4d7b-bc3c-38160be12b40", "text_version_hash": "b83ef2a17be429bfc9f027c0e767caadc0d2b335e4d90a549eb6737354f02bd4", "field": "full_description", "start": 76, "end": 112, "quote": "负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建。", "evidence": [{"record_id": "CN_PAXINI|zhiye|48deb1a8-bb0a-4d7b-bc3c-38160be12b40", "text_version_hash": "b83ef2a17be429bfc9f027c0e767caadc0d2b335e4d90a549eb6737354f02bd4", "field": "full_description", "start": 76, "end": 112, "quote": "负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建。"}]}]}, {"id": "N0312:env", "relation": "ROLE", "value": "RF_ML_AI_ENGINEERING", "surface": "负责训练环境的维护", "evidence": [{"record_id": "CN_PAXINI|zhiye|48deb1a8-bb0a-4d7b-bc3c-38160be12b40", "text_version_hash": "b83ef2a17be429bfc9f027c0e767caadc0d2b335e4d90a549eb6737354f02bd4", "field": "full_description", "start": 121, "end": 165, "quote": "负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。", "evidence": [{"record_id": "CN_PAXINI|zhiye|48deb1a8-bb0a-4d7b-bc3c-38160be12b40", "text_version_hash": "b83ef2a17be429bfc9f027c0e767caadc0d2b335e4d90a549eb6737354f02bd4", "field": "full_description", "start": 121, "end": 165, "quote": "负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。"}]}]}]}}

ACT_DEPLOYMENT [{"end": 165, "field": "full_description", "method": "RECOVER_END_FROM_QUOTE", "quote": "3.环境运维： 负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。", "start": 113}]

ACT_ENGINEERING [{"end": 111, "field": "full_description", "method": "RECOVER_END_FROM_QUOTE", "quote": "负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建", "start": 76}]

DUTIES

1.数据工程： 负责海量机器人遥操作数据的采集、清洗、标注及标准化处理，搭建高效的数据流水线。
2.训练与评测： 协助高级工程师进行模型训练，负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建。
3.环境运维： 负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。
4.实验跟踪： 详细记录实验过程与结果，协助进行模型推理加速和部署脚本的开发。

REQUIREMENTS

1.硬性背景： 本科及以上学历，计算机、电子信息、自动化等相关专业。
2.代码能力： 精通Python，熟悉Linux开发环境，代码规范，具备良好的Debug能力。
3.工具链： 熟悉PyTorch；了解Isaac Sim/Mujoco等物理仿真平台的基本使用。
4.软素质： 自驱力强，能吃苦（需配合真机实验进度），具备优秀的团队协作精神，愿意投身一线工程落地。

FULL_DESCRIPTION

工作职责
1.数据工程： 负责海量机器人遥操作数据的采集、清洗、标注及标准化处理，搭建高效的数据流水线。
2.训练与评测： 协助高级工程师进行模型训练，负责在多场景、多构型下进行模型性能的自动化评测与Benchmark构建。
3.环境运维： 负责训练环境的维护、Bug排查及日志分析，解决训练过程中的环境崩溃和显存溢出等周边问题。
4.实验跟踪： 详细记录实验过程与结果，协助进行模型推理加速和部署脚本的开发。

任职资格
1.硬性背景： 本科及以上学历，计算机、电子信息、自动化等相关专业。
2.代码能力： 精通Python，熟悉Linux开发环境，代码规范，具备良好的Debug能力。
3.工具链： 熟悉PyTorch；了解Isaac Sim/Mujoco等物理仿真平台的基本使用。
4.软素质： 自驱力强，能吃苦（需配合真机实验进度），具备优秀的团队协作精神，愿意投身一线工程落地。

## N0331 CN_PAXINI 计量校准工程师​ ​

identity REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_PAXINI|zhiye|c2ea496f-3f9b-4b59-9f50-dc31f0df506a|bb1f1bc08e8593c9d23a2f604feaccde11c184231266865b88659c80ea87995a

TREE {"schema_version": 1, "rationale": "可复用计量标准/方法与周期校准/溯源/质量体系均为持续本人交付；实验室合规属于计量质量结果，不是独立企业治理岗。", "expression": {"id": "N0331:root", "relation": "ALL", "scope": "JOB_RESPONSIBILITIES", "rationale": "可复用计量标准/方法与周期校准/溯源/质量体系均为持续本人交付；实验室合规属于计量质量结果，不是独立企业治理岗。", "evidence": [{"record_id": "CN_PAXINI|zhiye|c2ea496f-3f9b-4b59-9f50-dc31f0df506a", "text_version_hash": "bb1f1bc08e8593c9d23a2f604feaccde11c184231266865b88659c80ea87995a", "field": "full_description", "start": 23, "end": 43, "quote": "负责建立、维护和完善实验室的计量标准装置"}], "children": [{"id": "N0331:std", "relation": "ROLE", "value": "RF_SIMULATION_EVALUATION", "surface": "负责建立、维护和完善实验室的计量标准装置", "evidence": [{"record_id": "CN_PAXINI|zhiye|c2ea496f-3f9b-4b59-9f50-dc31f0df506a", "text_version_hash": "bb1f1bc08e8593c9d23a2f604feaccde11c184231266865b88659c80ea87995a", "field": "full_description", "start": 23, "end": 56, "quote": "负责建立、维护和完善实验室的计量标准装置及配套设备（力学、磁学）。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责建立、维护和完善实验室的计量标准装置及配套设备（力学、磁学）。", "evidence": [{"record_id": "CN_PAXINI|zhiye|c2ea496f-3f9b-4b59-9f50-dc31f0df506a", "text_version_hash": "bb1f1bc08e8593c9d23a2f604feaccde11c184231266865b88659c80ea87995a", "field": "full_description", "start": 23, "end": 56, "quote": "负责建立、维护和完善实验室的计量标准装置及配套设备（力学、磁学）。"}]}, {"summary": "对关键测量过程进行不确定度评定与监控，保障检测/校准结果的的准确可靠。", "evidence": [{"record_id": "CN_PAXINI|zhiye|c2ea496f-3f9b-4b59-9f50-dc31f0df506a", "text_version_hash": "bb1f1bc08e8593c9d23a2f604feaccde11c184231266865b88659c80ea87995a", "field": "full_description", "start": 173, "end": 208, "quote": "对关键测量过程进行不确定度评定与监控，保障检测/校准结果的的准确可靠。"}]}]}, {"id": "N0331:cal", "relation": "ROLE", "value": "RF_MANUFACTURING_QUALITY_SUPPLY", "surface": "规划并实施实验室设备的周期检定/校准计划", "evidence": [{"record_id": "CN_PAXINI|zhiye|c2ea496f-3f9b-4b59-9f50-dc31f0df506a", "text_version_hash": "bb1f1bc08e8593c9d23a2f604feaccde11c184231266865b88659c80ea87995a", "field": "full_description", "start": 95, "end": 132, "quote": "规划并实施实验室设备的周期检定/校准计划，确保量值可溯源至国家或国际标准。"}], "duties_status": "DESCRIBED", "duties": [{"summary": "规划并实施实验室设备的周期检定/校准计划，确保量值可溯源至国家或国际标准。", "evidence": [{"record_id": "CN_PAXINI|zhiye|c2ea496f-3f9b-4b59-9f50-dc31f0df506a", "text_version_hash": "bb1f1bc08e8593c9d23a2f604feaccde11c184231266865b88659c80ea87995a", "field": "full_description", "start": 95, "end": 132, "quote": "规划并实施实验室设备的周期检定/校准计划，确保量值可溯源至国家或国际标准。"}]}, {"summary": "参与内部审核、管理评审及CNAS现场评审，负责计量相关内容的准备与整改。", "evidence": [{"record_id": "CN_PAXINI|zhiye|c2ea496f-3f9b-4b59-9f50-dc31f0df506a", "text_version_hash": "bb1f1bc08e8593c9d23a2f604feaccde11c184231266865b88659c80ea87995a", "field": "full_description", "start": 292, "end": 328, "quote": "参与内部审核、管理评审及CNAS现场评审，负责计量相关内容的准备与整改。"}]}]}]}}

ACT_ENGINEERING [{"end": 56, "field": "full_description", "method": "RECOVER_END_FROM_QUOTE", "quote": "负责建立、维护和完善实验室的计量标准装置及配套设备（力学、磁学）。", "start": 23}]

ACT_QUALITY [{"end": 328, "field": "full_description", "method": "RECOVER_END_FROM_QUOTE", "quote": "规划并实施实验室设备的周期检定/校准计划，确保量值可溯源至国家或国际标准。\n负责内部校准工作的开展及外部溯源机构的对接与管理。\n3.测量过程控制与技术支撑\n对关键测量过程进行不确定度评定与监控，保障检测/校准结果的的准确可靠。\n为实验室的检测/校准活动提供计量技术咨询与支持，参参与解决复杂技术问题。\n4.体系合规与评审准备\n依据CNAS-CL01及相关准则要求，维护实验室计量领域的合规性。\n参与内部审核、管理评审及CNAS现场评审，负责计量相关内容的准备与整改。", "start": 95}]

DUTIES

岗位职责：
1.计量标准建设与管理
负责建立、维护和完善实验室的计量标准装置及配套设备（力学、磁学）。
组织编写计量标准技术报告、操作规程及相关管理体系文件。
2.量值溯源与校准
规划并实施实验室设备的周期检定/校准计划，确保量值可溯源至国家或国际标准。
负责内部校准工作的开展及外部溯源机构的对接与管理。
3.测量过程控制与技术支撑
对关键测量过程进行不确定度评定与监控，保障检测/校准结果的的准确可靠。
为实验室的检测/校准活动提供计量技术咨询与支持，参参与解决复杂技术问题。
4.体系合规与评审准备
依据CNAS-CL01及相关准则要求，维护实验室计量领域的合规性。
参与内部审核、管理评审及CNAS现场评审，负责计量相关内容的准备与整改。
培训与指导
对实验室技术人员进行计量基础、仪器操作及不确定度评定等方面的培训与指导。
完成领导安排的其他相关任务。

REQUIREMENTS

任职资格：
1.本科及以上学历，计量、检测、仪器仪表、机械、电子、自动化、材料、土木工程等等相关专业；1年以上计量检定、校准或相关领域工作经验，有CNAS/CMA实验室工作经验者优先。
2.熟悉计量法律法规、计量标准管理体系及CNAS认可准则，熟悉计量标准考核规范(JJF1033)及测量不确定度评定方法((JJF 1059)；有计量检定员证或注册计量师资格证者优先。
3.熟练操作力学/磁学类仪器操作，具备扎实的专业基础知识和较强的动手能力。
4.具备较强的技术文件编写能力和数据分析能力。
5.具备良好的问题解决能力，能快速识别并解决方法验证过程中的技术难题与合规风险。
6.沟通协调能力强，可与实验室检测人员、设备工程师、体系工程师高效协作，推动验证工作落地。

FULL_DESCRIPTION

工作职责
岗位职责：
1.计量标准建设与管理
负责建立、维护和完善实验室的计量标准装置及配套设备（力学、磁学）。
组织编写计量标准技术报告、操作规程及相关管理体系文件。
2.量值溯源与校准
规划并实施实验室设备的周期检定/校准计划，确保量值可溯源至国家或国际标准。
负责内部校准工作的开展及外部溯源机构的对接与管理。
3.测量过程控制与技术支撑
对关键测量过程进行不确定度评定与监控，保障检测/校准结果的的准确可靠。
为实验室的检测/校准活动提供计量技术咨询与支持，参参与解决复杂技术问题。
4.体系合规与评审准备
依据CNAS-CL01及相关准则要求，维护实验室计量领域的合规性。
参与内部审核、管理评审及CNAS现场评审，负责计量相关内容的准备与整改。
培训与指导
对实验室技术人员进行计量基础、仪器操作及不确定度评定等方面的培训与指导。
完成领导安排的其他相关任务。

任职资格
任职资格：
1.本科及以上学历，计量、检测、仪器仪表、机械、电子、自动化、材料、土木工程等等相关专业；1年以上计量检定、校准或相关领域工作经验，有CNAS/CMA实验室工作经验者优先。
2.熟悉计量法律法规、计量标准管理体系及CNAS认可准则，熟悉计量标准考核规范(JJF1033)及测量不确定度评定方法((JJF 1059)；有计量检定员证或注册计量师资格证者优先。
3.熟练操作力学/磁学类仪器操作，具备扎实的专业基础知识和较强的动手能力。
4.具备较强的技术文件编写能力和数据分析能力。
5.具备良好的问题解决能力，能快速识别并解决方法验证过程中的技术难题与合规风险。
6.沟通协调能力强，可与实验室检测人员、设备工程师、体系工程师高效协作，推动验证工作落地。

## N0355 CN_PAXINI 具身智能算法工程师

identity REFERENCE1654_USER_ACCEPTED_2026_09_14_V1|CN_PAXINI|zhiye|914eb9f2-492f-403a-b443-58f439589621|be41a157a1101c016bf76ffda4fbad1fa232e8446a382e69c83acb575daefb15

TREE {"schema_version": 1, "rationale": "模型大规模并行训练和明确的运动/力控/规划算法开发同时由本人负责，已足以建立跨职能复合。感知融合、采集存储及清洗等原文职责仍须保存于正文，尚不据这些配套句推定独立感知产品或全公司数据生产所有权。", "expression": {"id": "N0355:root", "relation": "ALL", "scope": "JOB_RESPONSIBILITIES", "rationale": "模型大规模并行训练和明确的运动/力控/规划算法开发同时由本人负责，已足以建立跨职能复合。感知融合、采集存储及清洗等原文职责仍须保存于正文，尚不据这些配套句推定独立感知产品或全公司数据生产所有权。", "evidence": [{"record_id": "CN_PAXINI|zhiye|914eb9f2-492f-403a-b443-58f439589621", "text_version_hash": "be41a157a1101c016bf76ffda4fbad1fa232e8446a382e69c83acb575daefb15", "field": "full_description", "start": 126, "end": 140, "quote": "负责操作中的控制，决策和规划"}], "children": [{"id": "N0355:ml", "relation": "ROLE", "value": "RF_ML_AI_ENGINEERING", "surface": "负责模仿学习和强化学习算法大规模并行训练", "evidence": [{"record_id": "CN_PAXINI|zhiye|914eb9f2-492f-403a-b443-58f439589621", "text_version_hash": "be41a157a1101c016bf76ffda4fbad1fa232e8446a382e69c83acb575daefb15", "field": "full_description", "start": 211, "end": 245, "quote": "负责模仿学习和强化学习算法大规模并行训练，验证和部署至实际的系统中；"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责模仿学习和强化学习算法大规模并行训练，验证和部署至实际的系统中；", "evidence": [{"record_id": "CN_PAXINI|zhiye|914eb9f2-492f-403a-b443-58f439589621", "text_version_hash": "be41a157a1101c016bf76ffda4fbad1fa232e8446a382e69c83acb575daefb15", "field": "full_description", "start": 211, "end": 245, "quote": "负责模仿学习和强化学习算法大规模并行训练，验证和部署至实际的系统中；"}]}]}, {"id": "N0355:cp", "relation": "ROLE", "value": "RF_CONTROL_PLANNING", "surface": "负责操作中的控制，决策和规划", "evidence": [{"record_id": "CN_PAXINI|zhiye|914eb9f2-492f-403a-b443-58f439589621", "text_version_hash": "be41a157a1101c016bf76ffda4fbad1fa232e8446a382e69c83acb575daefb15", "field": "full_description", "start": 126, "end": 177, "quote": "负责操作中的控制，决策和规划，包括但不限于运动控制、轨迹规划、正逆运动学、动力学、力控等相关算法开发；"}], "duties_status": "DESCRIBED", "duties": [{"summary": "负责操作中的控制，决策和规划，包括但不限于运动控制、轨迹规划、正逆运动学、动力学、力控等相关算法开发；", "evidence": [{"record_id": "CN_PAXINI|zhiye|914eb9f2-492f-403a-b443-58f439589621", "text_version_hash": "be41a157a1101c016bf76ffda4fbad1fa232e8446a382e69c83acb575daefb15", "field": "full_description", "start": 126, "end": 177, "quote": "负责操作中的控制，决策和规划，包括但不限于运动控制、轨迹规划、正逆运动学、动力学、力控等相关算法开发；"}]}]}]}}

ACT_DEPLOYMENT [{"end": 245, "field": "full_description", "method": "RECOVER_END_FROM_QUOTE", "quote": "5. 负责模仿学习和强化学习算法大规模并行训练，验证和部署至实际的系统中；", "start": 208}]

ACT_ENGINEERING [{"end": 245, "field": "full_description", "method": "RECOVER_END_FROM_QUOTE", "quote": "5. 负责模仿学习和强化学习算法大规模并行训练，验证和部署至实际的系统中；", "start": 208}]

DUTIES

1. 负责跟进最新的机器人（机械臂，灵巧手等）操作技术和具身智能技术，并将前沿的模仿学习，强化学习方法落地到机器人操作中，提升机器人在复杂任务中的能力和多场景中的高精度与稳定性；
2. 负责操作中多传感器融合感知与操作结合的算法开发；
3. 负责操作中的控制，决策和规划，包括但不限于运动控制、轨迹规划、正逆运动学、动力学、力控等相关算法开发；
4. 针对特定问题进行算法功能调研，开发，快速验证和优化；
5. 负责模仿学习和强化学习算法大规模并行训练，验证和部署至实际的系统中；
6. 负责数据采集设备数据储存，相关功能和算法开发，数据处理，清洗，分析等；

REQUIREMENTS

1. 本科以上学历，机器人，自动化、计算机、电子、电气等相关专业，具有至少3年的学术研究以及工程开发经验；
2. 精通C++， Python，熟练掌握ROS，Pytorch, TensorFlow，且有良好的编码规范和质量意识
3. 熟悉Isaac, V-Rep、GAZEBO、MuJoCo、PyBullet等仿真软件
4. 了解机器人操控的传统与机器学习方法，具有机械操控算法开发经验，能够解决操作算法中的复杂问题。
5. 具有扎实机器人运动学与动力学、自动控制原理等相关领域知识基础
6. 熟悉深度学习、强化学习、机器人学习的训练和部署经验
7. 具有较强的文献研究，代码转换和项目实施能力
8.  具备良好的分析解决问题和故障排查能力
9.具备创新思维，能够提供创新的解决方案和改进机器人系统性能.10- 具备10.良好的自我驱动能力和强烈的责任感，良好的沟通能力和团队合作精神
加分项:
11 在机器人操作控制中的应用有相关研究或项目背景或在RSS、CoRL、ICRA、IROS机器人会议上或ICML、NeurIPS、ICLR等人工智能会议发表过论文者优先。

FULL_DESCRIPTION

工作职责
1. 负责跟进最新的机器人（机械臂，灵巧手等）操作技术和具身智能技术，并将前沿的模仿学习，强化学习方法落地到机器人操作中，提升机器人在复杂任务中的能力和多场景中的高精度与稳定性；
2. 负责操作中多传感器融合感知与操作结合的算法开发；
3. 负责操作中的控制，决策和规划，包括但不限于运动控制、轨迹规划、正逆运动学、动力学、力控等相关算法开发；
4. 针对特定问题进行算法功能调研，开发，快速验证和优化；
5. 负责模仿学习和强化学习算法大规模并行训练，验证和部署至实际的系统中；
6. 负责数据采集设备数据储存，相关功能和算法开发，数据处理，清洗，分析等；

任职资格
1. 本科以上学历，机器人，自动化、计算机、电子、电气等相关专业，具有至少3年的学术研究以及工程开发经验；
2. 精通C++， Python，熟练掌握ROS，Pytorch, TensorFlow，且有良好的编码规范和质量意识
3. 熟悉Isaac, V-Rep、GAZEBO、MuJoCo、PyBullet等仿真软件
4. 了解机器人操控的传统与机器学习方法，具有机械操控算法开发经验，能够解决操作算法中的复杂问题。
5. 具有扎实机器人运动学与动力学、自动控制原理等相关领域知识基础
6. 熟悉深度学习、强化学习、机器人学习的训练和部署经验
7. 具有较强的文献研究，代码转换和项目实施能力
8.  具备良好的分析解决问题和故障排查能力
9.具备创新思维，能够提供创新的解决方案和改进机器人系统性能.10- 具备10.良好的自我驱动能力和强烈的责任感，良好的沟通能力和团队合作精神
加分项:
11 在机器人操作控制中的应用有相关研究或项目背景或在RSS、CoRL、ICRA、IROS机器人会议上或ICML、NeurIPS、ICLR等人工智能会议发表过论文者优先。