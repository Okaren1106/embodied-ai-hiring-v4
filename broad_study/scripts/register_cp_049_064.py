"""First-pass adjudication for control-planning coding_order 49-64. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
SIM={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"DUAL_ARM_PLANNING","secondary_task":"NAV_PLANNING",
 "task_evidence":"攻克Sim2Real Gap难题",
 "new":{
  "1":[["V2_SIM2REAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"Python/C++不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"规控双臂模板。"
}
decisions={
"N0273":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"DUAL_ARM_PLANNING","secondary_task":"",
 "task_evidence":"负责机器人全身和双臂操作规控算法研发和前沿技术的研究",
 "new":{"1":R+"C++不是C语言。"},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"规控算法。C++拒收C。"
},
"N0346":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LOCOMOTION_WBC","fine_task":"WHEELED_HUMANOID_WBC","secondary_task":"MANIPULATION",
 "task_evidence":"负责轮式人形机器人的全身运动控制（WBC）及模型预测控制（MPC）算法的研发与部署",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_SIM2REAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"C++不是C语言。",
  "4":[["V2_OSQP","GENERAL","CHOICE"],["V2_IPOPT","GENERAL","CHOICE"]],
  "5":O+"RBDL未单列冻结项。",
  "6":"DUPLICATE:N0346:4",
  "7":"DUPLICATE:N0346:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"运控WBC/MPC。OSQP/Ipopt保留。"
},
"N0329":dict(SIM, new={
  "1":[["V2_SIM2REAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"Python/C++不是C语言。",
  "4":O+"Gbzeao未单列冻结项。"
}, notes="规控。Gbzeao目录外。"),
"N0324":dict(SIM, task_evidence="完成算法在真机上的部署、标定、调试与性能优化。"),
"N0352":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"FORCE_VIBRATION","secondary_task":"",
 "task_evidence":"负责机器人力反馈控制、振动抑制等算法的设计和实现",
 "new":{
  "1":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_C","GENERAL","UNRESOLVED"]],
  "3":"DUPLICATE:N0352:2"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"运动控制。C/C++按C未解。"
},
"E0102":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"MECHATRONIC_CONTROL","secondary_task":"",
 "task_evidence":"机电控制系统开发,控制相关嵌入式软件开发,控制相关传感器、结构等的开发",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"高级机电控制。无新候选。"
},
"E0090":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"BLDC_EMBEDDED","secondary_task":"",
 "task_evidence":"无刷电机(BLDC)、永磁同步电机(PMSM)控制程序的开发",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"嵌入式电机控制。无新候选。"
},
"E0295":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"LOCOMOTION_WBC","fine_task":"WBC_OPTIMAL","secondary_task":"",
 "task_evidence":"应用操作空间控制（Operational Space Control）的方法，实现全身控制（Whole-Body Control）",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CLASSICAL_CONTROL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_SYSID","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_CLASSICAL_CONTROL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":R+"变分法不是有限元拓扑优化。",
  "6":[["V2_DDP","GENERAL","EXAMPLE"],["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]],
  "7":R+"C++/Python不是C语言。"
 },
 "old_overrides":{
  "O3":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为ROS/ROS2工具句。","quote":"了解 ROS/ROS2、Pinocchio、CasADi 等生态工具"}
 },
 "additions":[],"outside_extra":[],
 "notes":"运动控制。DDP/WBC保留。变分法拒收拓扑。"
},
"E0276":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"JOINT_MOTOR","secondary_task":"",
 "task_evidence":"负责机器人关节电机高性能控制器的方案设计、建模仿真",
 "new":{
  "1":[["V2_C","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_CALIBRATION","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O8":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"原电机短词定位为空，改为关节电机控制器职责句。","quote":"负责机器人关节电机高性能控制器的方案设计、建模仿真、并于嵌入式合作完成软件开发"},
  "O10":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原电机控制算法短词定位为空，改为FOC算法经验句。","quote":"精通PMSM、步进电机等电机控制算法，如有感、无感FOC算法、MTPA、死区补偿/优化等"},
  "O13":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原无刷电机短词定位为空，改为无刷电机传感器标定句。","quote":"熟悉无刷电机常用传感器特性及相应的标定标定算法"}
 },
 "additions":[],"outside_extra":[],
 "notes":"关节电机控制。正文写明C语言。"
},
"E0274":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"NAV_PLANNING","fine_task":"MOBILE_NAV","secondary_task":"",
 "task_evidence":"负责优化动态路径规划算法（如改进A*、RRT*、DWA等），解决低矮障碍物、狭窄通道等高难度场景的避障问题",
 "new":{
  "1":[["V2_PATH_SEARCH","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":R+"C++不是C语言。",
  "3":[["V2_C","GENERAL","UNRESOLVED"]],
  "4":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O2":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS1短词定位为空，改为Linux/ROS1句。","quote":"熟悉Linux系统，以及ROS1、ROS2、C++、Python等"},
  "O3":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS2短词定位为空，改为同一工具句。","quote":"熟悉Linux系统，以及ROS1、ROS2、C++、Python等"},
  "O4":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原C++短词定位为空，改为同一工具句。","quote":"熟悉Linux系统，以及ROS1、ROS2、C++、Python等"},
  "O7":{"metric":"GENERAL","branch":"EXAMPLE","relation":"EXPERIENCE_REQUIREMENT","reason":"原C++短词定位为空，改为C/C++/python句。","quote":"熟练掌握C、C++及python等语言编程开发，有较强的逻辑分析能力及良好的编程习惯"},
  "O9":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS1短词定位为空，改为ROS1或ROS2系统搭建句。","quote":"熟悉ROS1或ROS2系统搭建，熟悉机器人规划控制相关算法，包括全局规划、局部规划、轨迹优化、障碍处理等"},
  "O10":{"metric":"GENERAL","branch":"CHOICE","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS2短词定位为空，改为同一系统搭建句。","quote":"熟悉ROS1或ROS2系统搭建，熟悉机器人规划控制相关算法，包括全局规划、局部规划、轨迹优化、障碍处理等"}
 },
 "additions":[],"outside_extra":[],
 "notes":"导航算法。C与C++并列按C未解。ROS继承改写。"
},
"E0236":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"TELEOP_CONTROL","secondary_task":"",
 "task_evidence":"负责人形机器人遥操作核心算法的开发与优化，包括轨迹优化与重定向、柔顺控制、力位混合控制与自适应策略等",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"C++/Python不是C语言。",
  "4":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]],
  "6":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O5":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为ROS/ROS2仿真句。","quote":"熟悉C++/Python，有ROS/ROS2、Gazebo、Isaac Sim等机器人仿真与实验经验。"}
 },
 "additions":[],"outside_extra":[],
 "notes":"遥操作控制。ROS继承改写。"
},
"E0183":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"EMBEDDED_FOC","secondary_task":"",
 "task_evidence":"负责伺服电机 FOC 参数适配、力矩观测与滤",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"Python与C++不是C语言。",
  "3":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"],["V2_KALMAN_FACTOR","GENERAL","UNCONDITIONAL"]],
  "4":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_URDF","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O3":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为Ubuntu/ROS句。","quote":"熟练掌握Python与C++编程，精通Ubuntu, ROS/ROS2"}
 },
 "additions":[],"outside_extra":[],
 "notes":"嵌入式控制。URDF/FOC/卡尔曼保留。"
},
"E0143":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"FORCE_FEEDBACK","secondary_task":"",
 "task_evidence":"负责力反馈控制算法开发与优化,包括阻抗控制、导纳控制、力反射、虚拟墙、接触检测、力限幅及稳定性控制等",
 "new":{
  "1":[["V2_TELEOP","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","GENERAL","UNCONDITIONAL"]],
  "3":[["V2_TELEOP","GENERAL","UNCONDITIONAL"]],
  "4":R+"C++或Python不是C语言。",
  "5":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{
  "O4":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为Linux/ROS中间件句。","quote":"熟练使用 C++ 或 Python，具备 Linux、ROS/ROS2、实时控制或机器人中间件开发经验。"}
 },
 "additions":[],"outside_extra":[],
 "notes":"力反馈。遥操作经验保留。"
},
"E0123":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"FORCE_CONTROL","secondary_task":"",
 "task_evidence":"负责阻抗控制、导纳控制、力位混合控制、碰撞检测等力控与柔顺控制算法的开发和优化。",
 "new":{
  "1":[["V2_SYSID","GENERAL","UNCONDITIONAL"]],
  "2":R+"C++不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"力控算法。系统辨识保留。"
},
"E0342":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"NAV_PLANNING","fine_task":"LOCOMOTION_NAV","secondary_task":"LOCOMOTION_WBC",
 "task_evidence":"Design, implement, and deploy 3D motion planning algorithms for locomotion, with an emphasis on whole-body collision-aware motion execution in real-time.",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"],["V2_PATH_SEARCH","GENERAL","UNCONDITIONAL"]],
  "2":R+"C++17/20 is not the C language.",
  "3":[["V2_CERES","GENERAL","EXAMPLE"],["V2_OSQP","GENERAL","EXAMPLE"],["V2_IPOPT","GENERAL","EXAMPLE"],["V2_DDS","GENERAL","EXAMPLE"]],
  "4":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_KALMAN_FACTOR","GENERAL","UNCONDITIONAL"]],
  "6":R+"Salary USD is not Universal Scene Description.",
  "7":R+"Third-party recruiting boilerplate is not HR professional duty.",
  "8":"DUPLICATE:E0342:3"
 },
 "old_overrides":{
  "O4":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原C++短词定位为空，改为C++17/20经验句。","quote":"Expert proficiency in modern C++ (C++17/20), with a proven track record of writing high-performance, multithreaded code for robotics applications."},
  "O5":{"metric":"GENERAL","branch":"UNRESOLVED","relation":"EXPERIENCE_REQUIREMENT","reason":"原ROS短词定位为空，改为ROS/ROS2与DDS句。","quote":"Experience with common robotics frameworks (e.g., ROS/ROS2, DDS) and hands-on experience with modern optimization libraries relevant to motion planning (e.g., Ceres, IPOPT, OSQP)."},
  "O19":{"metric":"DUTY_OWN_DEVELOP","branch":"UNCONDITIONAL","relation":"OWN_DEVELOP","reason":"原motion planning短词定位为空，改为三维运动规划职责句。","quote":"Design, implement, and deploy 3D motion planning algorithms for locomotion, with an emphasis on whole-body collision-aware motion execution in real-time."},
  "O20":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原motion planning短词定位为空，改为采样/优化规划经验句。","quote":"Deep technical understanding of locomotion-specific path and motion planning algorithms, including sampling-based planners (RRT/PRM), optimization-based methods (MPC/LQR), and hybrid A*."},
  "O22":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原perceived environment data短词定位为空，改为感知数据接入规划句。","quote":"Proven ability to systematically test and debug systems on physical robots, and integrate perceived environment data (LiDAR, camera, depth sensing) into the planner."}
 },
 "additions":[],"outside_extra":[],
 "notes":"Agility导航。Ceres/OSQP/IPOPT/DDS保留。"
},
"E0322":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"LEARNED_MANIP","secondary_task":"",
 "task_evidence":"Familiarity with at least some of the following: grasp planning, imitation learning, reinforcement learning, force control, teleoperation",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"English can is not Controller Area Network.",
  "3":[["V2_TELEOP","GENERAL","UNCONDITIONAL"]],
  "4":R+"Salary USD is not Universal Scene Description.",
  "5":R+"Third-party recruiting boilerplate is not HR professional duty."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Agility操作软件。英语can拒收。"
}
}
if __name__=='__main__':
 register('RF_CONTROL_PLANNING', decisions, reader='grok4.6')
