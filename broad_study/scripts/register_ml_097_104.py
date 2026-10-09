"""First-pass adjudication for ML coding_order 97-104. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"E0288":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"TRAIN_INFER_INFRA",
 "fine_task":"CLOUD_NATIVE_AI_PLATFORM",
 "secondary_task":"",
 "task_evidence":"负责云原生技术架构设计、推理场景系统优化、云原生AI套件等开发工作。",
 "new":{
  "1":[["V2_C","GENERAL","UNRESOLVED"]],
  "2":O+"Kubeflow/volcano/RunC/Kata未单列冻结项。"
 },
 "old_overrides":{
  "O10":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原大模型短词定位为空，改为推理引擎句。","quote":"对大模型推理引擎、K8s、容器、网络、分布式、GPU架构、云原生AI等有深入研究；"},
  "O11":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原推理引擎短词定位为空，改为框架句。","quote":"熟悉主流深度学习框架、推理引擎框架，以及Kubeflow、volcano，了解底层实现，有模型训练或推理性能优化实操经验；"}
 },
 "additions":[],
 "outside_extra":[{"quote":"Kubeflow、volcano","description":"调度与容器运行时示例保留目录外。C/C++斜线记C未解。"}],
 "notes":"主责云原生AI平台与推理基础设施。C/C++明确写出C，按未解编码。"
},
"E0284":{
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
  "O14":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA短词定位为空，改为后训练经验句。","quote":"具备VLA或具身大模型的微调/后训练经验，能够独立完成从数据准备到模型训练再到真机验证的全流程；"},
  "O15":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原具身大模型短词定位为空，改为后训练经验句。","quote":"3.具备VLA或具身大模型的微调/后训练经验，能够独立完成从数据准备到模型训练再到真机验证的全流程；"},
  "O19":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原具身大模型短词定位为空，改为加分模型句。","quote":"熟悉具身大模型（VLA / World Action Model）相关模型，如OpenVLA、π系列、WALL-OSS、Dream-Zero等；"},
  "O20":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA短词定位为空，改为加分模型句。","quote":"熟悉具身大模型（VLA / World Action Model）相关模型"},
  "O23":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原机器人操作短词定位为空，改为落地经验句。","quote":"有机器人操作（抓取、装配、分拣等）算法的真实场景落地经验；"}
 },
 "additions":[],
 "outside_extra":[{"quote":"World Action Model","description":"WAM按世界动作模型理解，不默认记世界模型。"}],
 "notes":"主责商业化场景后训练交付。团队介绍句记背景。Python/C++拒收C。"
},
"E0275":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"NAV_TRAJECTORY_MULTIMODAL",
 "secondary_task":"TRAIN_INFER_INFRA",
 "task_evidence":"负责机器人系统中多模态局部轨迹规划模型的设计与研发，聚焦传感器融合感知与轨迹生成的端到端建模，实现闭环自主决策；",
 "new":{
  "1":[["V2_TENSORRT","DUTY_OWN_USE","CHOICE_AND_EXAMPLE"],["V2_ONNX","DUTY_OWN_USE","CHOICE_AND_EXAMPLE"]],
  "2":R+"Python/C++不是C语言；斜线保持未解。",
  "3":[["V2_SIM2REAL","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_OPEN3D","GENERAL","EXAMPLE"],["V2_PCL","GENERAL","EXAMPLE"]],
  "5":[["V2_TENSORRT","PREFERRED","CHOICE_AND_EXAMPLE"],["V2_ONNX","PREFERRED","CHOICE_AND_EXAMPLE"]],
  "6":"DUPLICATE:E0275:4"
 },
 "old_overrides":{
  "O7":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为系统架构句。","quote":"熟悉 ROS/ROS2 系统架构"}
 },
 "additions":[],
 "outside_extra":[{"quote":"Webots","description":"Webots为仿真平台示例，未写入本条新编码。"}],
 "notes":"主责导航局部规划模型。部署工具链记ONNX/TensorRT。候选6并入4。"
},
"E0266":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"RL_MANIP_LOCO_CONTROL",
 "secondary_task":"",
 "task_evidence":"负责机器人领域的强化学习算法研究与开发，包括机械臂、灵巧手、机器人全身运动控制等核心技能训练；",
 "new":{
  "1":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_SIM2REAL","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O29":{"metric":"PREFERRED","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原强化学习短词定位为空，改为项目经验句。","quote":"有机械臂+灵巧手或足式机器人的强化学习/模仿学习项目经验者优先；"},
  "O34":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原强化学习短词定位为空，改为论文句。","quote":"机器人学习、强化学习相关顶级会议论文发表经历或相关比赛获奖经历者优先考虑；"}
 },
 "additions":[],
 "outside_extra":[],
 "notes":"主责运控强化学习。蒸馏部署服务RL，不另建压缩项。"
},
"E0258":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"OTHER_MODEL",
 "fine_task":"STEREO_DEPTH_ESTIMATION",
 "secondary_task":"",
 "task_evidence":"负责双目深度估计的模型研发，包括网络结构设计、损失函数设计、cost volume 模型、Transformer/Attention 模型等。",
 "new":{
  "1":"DUPLICATE:E0258:3",
  "2":"DUPLICATE:E0258:3",
  "3":[["V2_TENSORRT","GENERAL","EXAMPLE"],["V2_ONNX","GENERAL","EXAMPLE"]]
 },
 "old_overrides":{},
 "additions":[],
 "outside_extra":[{"quote":"加速推理优化（FP16、INT8、卷积优化）","description":"FP16/INT8出现在落地经验列表，未单独升为压缩职责。"}],
 "notes":"主责双目深度估计，属其他模型应用。TensorRT/ONNX为落地示例。"
},
"E0251":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"VLA_OPENSOURCE_EVAL",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责 VLA 模型训练与效果优化，验证对齐模型效果；",
 "new":{
  "1":[["V2_HUGGINGFACE","DUTY_OWN_USE","EXAMPLE"]]
 },
 "old_overrides":{
  "O7":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA模型短词定位为空，改为原理句。","quote":"掌握常见VLA模型（例如PI系列、OpenVLA、diffusion policy等）原理；"},
  "O12":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA模型短词定位为空，改为上机经验句。","quote":"有VLA模型训练优化和实际上机部署执行经验；"},
  "O15":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA短词定位为空，改为架构句。","quote":"有LLM、Diffusion、Flow、MoE、VLA等大模型架构的分布式训练经验；"},
  "O16":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原分布式训练短词定位为空，改为架构句。","quote":"有LLM、Diffusion、Flow、MoE、VLA等大模型架构的分布式训练经验；"}
 },
 "additions":[],
 "outside_extra":[{"quote":"github/huggingface","description":"GitHub社区托管不是Git协作。只记Hugging Face社区。"}],
 "notes":"主责VLA训练评测与开源库。github按托管平台，不记Git。"
},
"E0230":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"DEXTEROUS_VLA_RL",
 "secondary_task":"",
 "task_evidence":"负责灵巧手算法研发，包括具身智能场景下的VLA、强化学习（Reinforcement Learning）等方向；",
 "new":{
  "1":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]],
  "3":O+"robomimic/Octo未单列冻结项。"
 },
 "old_overrides":{
  "O16":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA短词定位为空，改为项目经验句。","quote":"具备灵巧手的VLA，模仿学习或强化学习项目经验"}
 },
 "additions":[],
 "outside_extra":[{"quote":"robomimic","description":"开源基准库保留目录外。"}],
 "notes":"主责灵巧手VLA/RL。遥操作数据采集为加分。"
},
"E0217":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"ROBOT_MODEL",
 "fine_task":"EMBODIED_POSTTRAIN_SCENE_DELIVERY",
 "secondary_task":"DATA_EVAL_FOR_ML",
 "task_evidence":"负责具身大模型在具体商业化场景（物流、制造、家庭服务、医疗等）中的后训练与落地交付",
 "new":{
  "1":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_POSTTRAINING","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":R+"Python/C++不是C语言；斜线保持未解。",
  "4":[["V2_POSTTRAINING","GENERAL","CHOICE"]]
 },
 "old_overrides":{
  "O10":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA短词定位为空，改为后训练经验句。","quote":"具备VLA或具身大模型的微调/后训练经验，能够独立完成从数据准备到模型训练再到真机验证的全流程；"},
  "O16":{"metric":"PREFERRED","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原VLA短词定位为空，改为加分模型句。","quote":"熟悉具身大模型（VLA / World Action Model）相关模型"},
  "O19":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原机器人操作短词定位为空，改为落地经验句。","quote":"有机器人操作（抓取、装配、分拣等）算法的真实场景落地经验；"}
 },
 "additions":[],
 "outside_extra":[{"quote":"World Action Model","description":"不默认记世界模型。"}],
 "notes":"场景后训练岗。Python/C++拒收C。"
}
}
if __name__=='__main__':
 register('RF_ML_AI_ENGINEERING', decisions, reader='grok4.6')
