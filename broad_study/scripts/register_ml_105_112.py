"""First-pass adjudication for ML coding_order 105-112. Reader: grok4.6."""
from register_Q_decisions import register

R='REJECT:'
decisions={
"E0209":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"DEXTEROUS_POLICY_SIM",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"设计、训练、评估并部署面向灵巧手精细操作任务的运动策略（System 1 / System 0）。",
 "new":{
  "1":[["V2_SIM2REAL","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O15":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原灵巧手短词定位为空，改为平台经验句。","quote":"包括但不限于灵巧手、人形机器人、机械臂、无人机等。"},
  "O18":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原强化学习短词定位为空，改为学习方法句。","quote":"熟悉行为克隆、强化学习等机器人学习方法。"},
  "O26":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原灵巧手短词定位为空，改为论文实习句。","quote":"在灵巧手相关领域有论文发表记录或相关公司实习经验"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责灵巧手运动策略。sim2real为加分。"
},
"E0208":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"SYSTEM0_MOBILE_MANIP_POLICY",
 "secondary_task":"",
 "task_evidence":"设计、训练、评估并部署面向机器人移动操作任务的运动策略（System 1 / System 0）。",
 "new":{
  "1":[["V2_SIM2REAL","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"sim-to-real gap","description":"加分写的是处理gap的传感器信号经验，按Sim2Real优先编码。"}],
 "notes":"主责System 0移动操作策略。"
},
"E0206":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"DEXTEROUS_VLA_IL_RL",
 "secondary_task":"",
 "task_evidence":"参与灵巧手在具身场景下的算法研发（VLA / 模仿学习 / RL / Sim2Real），从实验设计到真机验证的全流程。",
 "new":{
  "1":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNRESOLVED"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"短岗。VLA/IL/RL/Sim2Real斜线任选，Sim2Real记未解职责。"
},
"E0205":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"DEXTEROUS_MODEL_LOOP",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"灵巧手相关模型的数据、训练、评测与落地迭代；仿真与真机侧工程闭环。",
 "new":{},
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"候选队列为空。主责灵巧手模型数据训练评测闭环。"
},
"E0195":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"FAST_SLOW_VLA_WAM",
 "secondary_task":"",
 "task_evidence":"负责面向家居、养老等高动态人机交互场景（如抱扶、护理、协作操作）的 System 1 / System 0 分层操作策略研发",
 "new":{
  "1":[["V2_SIM2REAL","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O3":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为系统开发句。","quote":"具备 ROS / ROS2 或机器人系统开发经验"}
 },
 "additions":[],
 "outside_extra":[{"quote":"VLA / WAM","description":"WAM按世界动作模型，不默认记世界模型。"}],
 "notes":"主责快慢系统分层操作策略。sim-to-real gap记一般要求。"
},
"E0175":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"MOBILE_MANIP_VLA_VLN",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"研究和落地前沿的移动操作大模型架构，探索VLN与VLA的融合策略或导航与操作一体化的统一策略学习框架",
 "new":{
  "1":R+"目标定位不是传感器/系统标定。",
  "2":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_WORLD_MODEL","GENERAL","EXAMPLE"]],
  "4":R+"Python/C++不是C语言；斜线保持未解。",
  "5":[["V2_POSTTRAINING","PREFERRED","EXAMPLE"]],
  "6":[["V2_SIM2REAL","PREFERRED","UNCONDITIONAL"]],
  "7":R+"GitHub托管和开源代码贡献不是Git协作。",
  "8":R+"Habitat Challenge/ManiSkill Challenge是竞赛名，不是仿真工具使用证据。"
 },
 "old_overrides":{
  "O6":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为加分句。","quote":"熟悉ROS/ROS2，有仿真平台的使用和Sim2Real落地经验；"}
 },
 "additions":[],
 "outside_extra":[{"quote":"GitHub","description":"开源托管不等于Git。世界模型出现在跟踪列表，按示例。"}],
 "notes":"主责移动操作大模型。标定候选为假阳性。后训练为加分示例。"
},
"E0169":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"EMBODIED_POSTTRAIN_SCENE_DELIVERY",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"1.负责具身大模型在具体商业化场景（物流、制造、家庭服务、医疗等）中的后训练与落地交付，从数据、模型、算法等多维度提升模型在目标场景下的任务成功率与执行效率；",
 "new":{
  "1":[["V2_POSTTRAINING","SEPARATE","BACKGROUND"]],
  "2":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "4":[["V2_POSTTRAINING","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":R+"Python/C++不是C语言；斜线保持未解。",
  "6":[["V2_POSTTRAINING","GENERAL","CHOICE"]]
 },
 "old_overrides":{
  "O19":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原具身大模型短词定位为空，改为加分模型句。","quote":"熟悉具身大模型（VLA / World Action Model）相关模型，如OpenVLA、π系列、WALL-OSS、Dream-Zero等；"},
  "O20":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原机器人操作短词定位为空，改为落地经验句。","quote":"有机器人操作（抓取、装配、分拣等）算法的真实场景落地经验；"}
 },
 "additions":[],
 "outside_extra":[{"quote":"World Action Model","description":"不默认记世界模型。"}],
 "notes":"与E0284同结构的产品落地后训练岗。"
},
"E0168":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"TACTILE_RL_FINETUNE_FORCE",
 "secondary_task":"",
 "task_evidence":"负责触觉/力觉反馈驱动的真机强化微调、模仿学习或策略优化算法研发。",
 "new":{
  "1":R+"Python/C++不是C语言；斜线保持未解。"
 },
 "old_overrides":{
  "O3":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为加分句。","quote":"熟悉 ROS/ROS2、机器人 SDK、策略部署接口或阻抗/导纳控制基础。"},
  "O14":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原强化学习短词定位为空，改为方法句。","quote":"熟悉强化学习、强化微调、模仿学习或机器人学习中的一种或多种方法。"},
  "O18":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原控制基础短词定位为空，改为运动学句。","quote":"了解机器人运动学、动力学以及控制基础"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责触觉驱动真机强化微调。Python/C++拒收C。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
