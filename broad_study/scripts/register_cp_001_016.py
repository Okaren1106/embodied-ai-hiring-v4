"""First-pass adjudication for control-planning coding_order 1-16. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
decisions={
"N0652":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"MOTOR_FOC","secondary_task":"",
 "task_evidence":"参与永磁同步电机（PMSM）或无刷直流电机（BLDC）的磁场定向控制（FOC）算法开发",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CAN","DUTY_OWN_USE","EXAMPLE"],["V2_SPI","DUTY_OWN_USE","EXAMPLE"],["V2_UART","DUTY_OWN_USE","EXAMPLE"]],
  "3":O+"MCU平台未单列冻结项。",
  "4":"DUPLICATE:N0652:3",
  "5":"DUPLICATE:N0652:3",
  "6":"DUPLICATE:N0652:2",
  "7":"DUPLICATE:N0652:2",
  "8":"DUPLICATE:N0652:2",
  "9":[["V2_C","GENERAL","UNRESOLVED"]],
  "10":"DUPLICATE:N0652:9",
  "11":O+"ARM Cortex-M MCU未单列冻结项。",
  "12":O+"STM32未单列冻结项。",
  "13":O+"TI C2000未单列冻结项。",
  "14":O+"Infineon未单列冻结项。",
  "15":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]],
  "16":[["V2_FREE_RTOS","PREFERRED","CHOICE"],["V2_RT_THREAD","PREFERRED","CHOICE"]],
  "17":O+"泛称RTOS未单列冻结项。",
  "18":"DUPLICATE:N0652:16",
  "19":"DUPLICATE:N0652:16"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"电机控制实习。C/C++按C未解。真CAN/SPI/UART保留。"
},
"N0441":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"FORCE_CONTROL","secondary_task":"",
 "task_evidence":"负责机器人力控相关算法开发与调试，包括且不仅限于干扰观测器、碰撞检测、虚拟墙、零空间优化、导纳/阻抗控制、力位混合控制",
 "new":{
  "1":[["V2_SYSID","GENERAL","UNCONDITIONAL"]],
  "2":[["V2_C","GENERAL","UNRESOLVED"],["V2_BULLET","GENERAL","CHOICE"]],
  "3":"DUPLICATE:N0441:2",
  "4":"DUPLICATE:N0441:2",
  "5":O+"Mujoco/Webots/Gazebo/CoppeliaSim/Isaac未在本句单列冻结项。",
  "6":"DUPLICATE:N0441:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"力控算法专家。C/C++按C未解。Bullet保留。"
},
"N0799":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"FIELD_MANIPULATION","secondary_task":"",
 "task_evidence":"Experience with manipulation planning and control, such as trajectory optimization or model predictive control (MPC)",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"],["V2_PATH_SEARCH","GENERAL","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0799:2",
  "4":R+"Python and/or C++ is not the C language.",
  "5":[["V2_TELEOP","GENERAL","UNCONDITIONAL"]],
  "6":[["V2_TENSORRT","GENERAL","EXAMPLE"],["V2_ONNX","GENERAL","EXAMPLE"],["V2_ONNX_RUNTIME","GENERAL","EXAMPLE"]],
  "7":"DUPLICATE:N0799:6",
  "8":"DUPLICATE:N0799:6",
  "9":[["V2_SIM2REAL","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FieldAI操作自主。英语can拒收。"
},
"E0050":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LOCOMOTION_WBC","fine_task":"WHEELED_HUMANOID_RL","secondary_task":"",
 "task_evidence":"协同完成RL算法与WBC、MPC等传统运控算法的融合",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"Python/C++不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"运控算法工程师。WBC/MPC记经典控制。"
},
"N0495":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LOCOMOTION_WBC","fine_task":"PERCEPTION_FUSED_GAIT","secondary_task":"NAV_PLANNING",
 "task_evidence":"通过融合激光雷达、深度相机等外部感知信息生成的高度图/深度图，实时规划与执行步态",
 "new":{
  "1":O+"PPO未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"感控融合。PPO目录外。"
},
"N0045":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"MOBILE_MANIP_INTERN","secondary_task":"",
 "task_evidence":"协助参与机器人与人工智能算法研发，应用于室内移动操作算法。",
 "new":{},
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"移动操作实习。无新候选。"
},
"N0447":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LOCOMOTION_WBC","fine_task":"WBC_INTERN","secondary_task":"",
 "task_evidence":"参与机器人全身协同运动规划与控制算法开发工作",
 "new":{
  "1":R+"Python、C++不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"运动控制实习。"
},
"E0294":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"HUMANOID_CONTROL_SW","secondary_task":"",
 "task_evidence":"负责人形机器人系统级软件开发,构建高实时性、模块化的软件架构",
 "new":{
  "1":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CAN","DUTY_OWN_DEVELOP","EXAMPLE"],["V2_ETHERCAT","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "3":R+"C++不是C语言。",
  "4":[["V2_CAN","GENERAL","EXAMPLE"],["V2_ETHERCAT","GENERAL","EXAMPLE"]],
  "5":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "6":O+"ros2_control未单列冻结项。",
  "7":O+"SOEM/IgH未单列冻结项。",
  "8":"DUPLICATE:E0294:5"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"控制系统工程师。GitLab记Git协作。真CAN/EtherCAT保留。"
},
"N0604":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LOCOMOTION_WBC","fine_task":"WBC_RESEARCH_INTERN","secondary_task":"",
 "task_evidence":"研究人形机器人全身控制前沿算法，鼓励探索与创新",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"WBC研究实习。"
},
"N0855":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"WAREHOUSE_CONTROLS","secondary_task":"",
 "task_evidence":"Familiarity with communications protocols commonly used in mechatronics and robotic systems (EtherCAT, CAN bus, etc.).",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":R+"English can is not Controller Area Network.",
  "3":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_CAN","GENERAL","EXAMPLE"],["V2_ETHERCAT","GENERAL","EXAMPLE"]],
  "5":"DUPLICATE:N0855:4",
  "6":"DUPLICATE:N0855:4"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Dexterity Controls Engineer。英语can拒收。真CAN bus保留。"
},
"E0348":{
 "inherited":"REVIEWED_ACCEPT_WITH_DERIVED_OVERRIDES_RETAINED_UNKNOWN",
 "task":"NAV_PLANNING","fine_task":"WHOLE_BODY_MOTION_PLANNING","secondary_task":"MANIPULATION",
 "task_evidence":"Design, implement, test, and deploy motion planning and trajectory optimization algorithms for humanoid robots",
 "new":{
  "1":[["V2_PATH_SEARCH","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"],["V2_PATH_SEARCH","GENERAL","UNCONDITIONAL"]],
  "3":R+"C++17/20 is not the C language.",
  "4":[["V2_PATH_SEARCH","PREFERRED","UNCONDITIONAL"]],
  "5":[["V2_PATH_SEARCH","PREFERRED","UNCONDITIONAL"]],
  "6":R+"Salary USD is not Universal Scene Description.",
  "7":R+"Third-party recruiting boilerplate is not HR professional duty."
 },
 "old_overrides":{
  "O1":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原C++短词定位为空，改为C++17/20经验句。","quote":"Expertise in modern C++ (C++17/20) and Python for high-performance, multithreaded, real-time robotics applications"},
  "O17":{"metric":"GENERAL","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原planning短词定位为空，改为样本规划与轨迹优化句。","quote":"Proven expertise in sample-based motion planning, trajectory optimization, and model predictive control (MPC) with a track record of shipping these algorithms to production"},
  "O18":{"metric":"DUTY_OWN_USE","branch":"UNCONDITIONAL","relation":"OWN_USE","reason":"原control短词定位为空，改为规划栈与控制集成句。","quote":"Architect motion planning systems for modularity, observability, and clean integration with perception, state estimation, and control"},
  "O20":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原manipulation短词定位为空，改为高自由度操作算法经验句。","quote":"Experience developing and deploying manipulation algorithms on high-DOF robots"},
  "O26":{"metric":"PREFERRED","branch":"UNCONDITIONAL","relation":"EXPERIENCE_REQUIREMENT","reason":"原motion planning短词定位为空，改为离线轨迹优化加速在线规划句。","quote":"Experience leveraging machine learning or offline trajectory optimization to accelerate online planning"}
 },
 "additions":[],"outside_extra":[],
 "notes":"Agility运动规划。继承短词改写。"
},
"E0583":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"HUMANOID_CONTROLS","secondary_task":"",
 "task_evidence":"Design & implement control algorithms: PID, LQR, MPC, inverse dynamics, and feedforward controllers.",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_CAN","DUTY_OWN_USE","EXAMPLE"],["V2_ETHERNET","DUTY_OWN_USE","EXAMPLE"],["V2_I2C","DUTY_OWN_USE","EXAMPLE"],["V2_SPI","DUTY_OWN_USE","EXAMPLE"]],
  "3":R+"Python and C++ is not the C language.",
  "4":[["V2_CAN","GENERAL","EXAMPLE"],["V2_ETHERNET","GENERAL","EXAMPLE"],["V2_I2C","GENERAL","EXAMPLE"],["V2_SPI","GENERAL","EXAMPLE"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Apptronik Controls Engineer。真CAN/SPI/I2C/Ethernet保留。"
},
"E0006":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"ARM_LOWLEVEL","secondary_task":"",
 "task_evidence":"负责六轴或七轴机械臂运动规划算法的研发与优化",
 "new":{
  "1":[["V2_DDS","GENERAL","CHOICE"]],
  "2":R+"C++不是C语言。",
  "3":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"],["V2_KALMAN_FACTOR","GENERAL","UNCONDITIONAL"]],
  "4":O+"IF-Fast未单列冻结项。",
  "5":[["SK_ZEROMQ","GENERAL","CHOICE"],["SK_LCM","GENERAL","CHOICE"],["V2_DDS","GENERAL","CHOICE"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"机械臂底层运控。UDP不记TCP/IP。"
},
"N0356":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"DUAL_ARM_PLANNING","secondary_task":"NAV_PLANNING",
 "task_evidence":"攻克Sim2Real Gap难题，确保算法在真机上的稳定迁移。",
 "new":{
  "1":[["V2_SIM2REAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"Python/C++不是C语言。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"规控算法。Sim2Real/标定保留。"
},
"E0378":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"DEXTEROUS_SW","secondary_task":"",
 "task_evidence":"The Lead Software Engineer - Dexterous Manipulation is a core contributor to our robot",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_SIM2REAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"C++/Python is not the C language.",
  "5":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_CALIBRATION","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"灵巧操作软件负责人。英语can未单记CAN。"
},
"N0926":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"FLEET_PLANNING","fine_task":"FLEET_OPTIMIZATION","secondary_task":"",
 "task_evidence":"Own software infrastructure, continuous integration, production debugging, and on-call support for components you build.",
 "new":{
  "1":R+"Company boilerplate is not the C language.",
  "2":R+"Series C funding is not the C language.",
  "3":[["V2_CI_CD","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"C++ as an alternative to Rust is not the C language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Nimble车队优化。C轮融资拒收C。"
}
}
if __name__=='__main__':
 register('RF_CONTROL_PLANNING', decisions, reader='grok4.6')
