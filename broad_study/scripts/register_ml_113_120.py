"""First-pass adjudication for ML coding_order 113-120. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"E0167":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"TACTILE_REPRESENTATION",
 "secondary_task":"",
 "task_evidence":"负责触觉信号表征学习、触觉 encoder 建模及相关算法研发。",
 "new":{
  "1":R+"材质/材料感知不是工业外观CMF设计。",
  "2":[["V2_WORLD_MODEL","DUTY_OWN_DEVELOP","CHOICE"]],
  "3":[["V2_WORLD_MODEL","PREFERRED","EXAMPLE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"世界模型或动作模型","description":"世界模型为操作策略建模任选之一。"}],
 "notes":"主责触觉表征。材质是触觉对象不是CMF。"
},
"E0164":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"HRI_WBC_RL",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责开发、训练和部署具身智能机器人全身控制的强化学习算法，集成避障，柔顺力控，安全保护等多项功能机制",
 "new":{
  "1":[["V2_MOCAP","DUTY_OWN_USE","EXAMPLE"]],
  "2":[["V2_SIM2REAL","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O7":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原RL短词定位为空，改为原理句。","quote":"熟悉 RL 的原理，掌握常见的 RL 算法，如 PPO，TD3, SAC 等"}
 },
 "additions":[{"code":"V2_TELEOP","metric":"DUTY_OWN_USE","branch":"EXAMPLE","quote":"清洗并提高多来源（动捕 / 视频 / 遥操等）的数据的质量","reason":"遥操与动捕同为数据来源示例。"}],
 "outside_extra":[],
 "notes":"主责人机交互全身RL。动捕/遥操服务数据闭环。"
},
"E0161":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"MANIP_VLA_WAM_FULLSTACK",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责机器人操作策略从数据到部署的全链路工作，包括数据处理、模型训练与真机验证。",
 "new":{
  "1":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"VLA / WAM","description":"WAM按世界动作模型，不默认记世界模型。"}],
 "notes":"主责操作策略全链路。遥操为加分背景。"
},
"E0157":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"EMBODIED_POSTTRAIN_SCENE_DELIVERY",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责具身大模型在物流、制造、家庭服务、医疗等商业化场景的后训练与落地交付，从数据、模型、算法维度提升任务成功率与执行效率；",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":R+"Python/C++不是C语言；斜线保持未解。",
  "4":[["V2_POSTTRAINING","GENERAL","CHOICE"]]
 },
 "old_overrides":{
  "O18":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原机器人操作短词定位为空，改为落地经验句。","quote":"机器人操作（抓取、装配、分拣等）算法的真实场景落地经验；"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"场景后训练岗。Python/C++拒收C。"
},
"E0139":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VLA_OPENSOURCE_EVAL",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责 VLA 模型训练与效果优化，验证对齐模型效果；",
 "new":{
  "1":[["V2_HUGGINGFACE","DUTY_OWN_USE","EXAMPLE"]]
 },
 "old_overrides":{
  "O7":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA模型短词定位为空，改为原理句。","quote":"掌握常见VLA模型（例如PI系列、OpenVLA、diffusion policy等）原理；"}
 },
 "additions":[],
 "outside_extra":[{"quote":"github/huggingface","description":"GitHub社区托管不是Git协作。"}],
 "notes":"与E0251同结构。只记Hugging Face社区。"
},
"E0121":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"GPU_CLUSTER_OPS",
 "secondary_task":"",
 "task_evidence":"负责大规模GPU集群从服务器到 Kubernetes 资源池的全生命周期运维。",
 "new":{
  "1":[["V2_NCCL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_NCCL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_PROCUREMENT","SEPARATE","COLLABORATION_OBJECT"]],
  "4":[["V2_NCCL","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_NCCL","GENERAL","CHOICE_AND_EXAMPLE"]],
  "6":[["V2_SHELL","GENERAL","CHOICE"],["V2_ANSIBLE","GENERAL","CHOICE"],["V2_SOP_OPERATION","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O3":{"metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","relation":"OWN_DEVELOP","reason":"原Kubernetes短词定位为空，改为资源池运维句。","quote":"负责大规模GPU集群从服务器到 Kubernetes 资源池的全生命周期运维。"},
  "O5":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原Kubernetes短词定位为空，改为控制面句。","quote":"深入理解 Kubernetes 控制面、调度、网络、存储和节点故障定位。"}
 },
 "additions":[],
 "outside_extra":[{"quote":"供应商协同","description":"供应商协同记采购协作对象，不是本人商务寻源主责。"}],
 "notes":"主责智算集群运维。NCCL训练网络成立。Shell/Ansible/SOP为自动化能力任选。"
},
"E0328":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"AI_LEADERSHIP_HUMANOID",
 "secondary_task":"",
 "task_evidence":"The Senior Director of AI will be a pivotal leader within our cutting-edge humanoid robotics company, driving the strategic direction and execution of all artificial intelligence and machine learning initiatives.",
 "new":{
  "1":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"薪酬USD不是Universal Scene Description。",
  "4":R+"第三方招聘免责声明不是HR专业职责。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责人形AI方向管理。Sim2Real与遥操数据飞轮进入职责。"
},
"E0326":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_LOCO_MANIP_WBC",
 "secondary_task":"",
 "task_evidence":"Design, train, and deploy robust RL policies for locomotion, manipulation, whole body control, and dynamic interactions with the environment.",
 "new":{
  "1":[["V2_SIM2REAL","GENERAL","UNCONDITIONAL"]],
  "2":R+"薪酬USD不是Universal Scene Description。",
  "3":R+"第三方招聘免责声明不是HR专业职责。"
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[],
 "notes":"主责强化学习策略。sim-to-real为熟悉项。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
