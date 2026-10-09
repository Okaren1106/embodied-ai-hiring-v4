"""First-pass adjudication for control-planning coding_order 65-75. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:'
HUMANOID={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"LOCOMOTION_WBC","fine_task":"HUMANOID_CONTROLS_STAFF","secondary_task":"MANIPULATION",
 "task_evidence":"Proven expertise in whole-body control (WBC/OSC, QP-based control, or MPC) for floating-base (legged) or mobile (wheeled) systems.",
 "new":{
  "1":R+"Company boilerplate is not teleoperation duty.",
  "2":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_TELEOP","SEPARATE","COLLABORATION_OBJECT"]],
  "4":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"]],
  "5":[["V2_TELEOP","GENERAL","UNCONDITIONAL"]],
  "6":R+"C++ and Python is not the C language.",
  "7":[["V2_SAFETY_STANDARDS","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Apptronik人形控制。WBC/MPC保留。"
}
PLANLIB={
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"NAV_PLANNING","fine_task":"FIELD_PLANNING_CONTROL","secondary_task":"",
 "task_evidence":"Familiarity with motion planning libraries like OMPL, MoveIt, Nav2 stack etc",
 "new":{
  "1":[["V2_MOVEIT","GENERAL","EXAMPLE"],["V2_NAV2","GENERAL","EXAMPLE"],["V2_OMPL","GENERAL","EXAMPLE"]],
  "2":"DUPLICATE:RID:1",
  "3":"DUPLICATE:RID:1",
  "4":"DUPLICATE:RID:1",
  "5":R+"C++ and Python is not the C language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FieldAI规划控制。OMPL/MoveIt/Nav2保留。"
}
def plan(rid, extra=None):
 d=dict(PLANLIB); d['new']=dict(PLANLIB['new'])
 d['new']['2']='DUPLICATE:%s:1'%rid
 d['new']['3']='DUPLICATE:%s:1'%rid
 d['new']['4']='DUPLICATE:%s:1'%rid
 if extra: d['new'].update(extra)
 return d
decisions={
"E0425":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"CONTROL_RUNTIME","fine_task":"WHEELED_CONTROLS","secondary_task":"LOCOMOTION_WBC",
 "task_evidence":"Design, implement, and tune whole-body controllers that coordinate wheeled base motion with upper-body manipulation.",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_KALMAN_FACTOR","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_SAFETY_STANDARDS","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"C++ is not the C language.",
  "4":R+"C++ is not the C language.",
  "5":R+"C++14/17/20 is not the C language.",
  "6":[["V2_SYSID","GENERAL","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"轮式控制。功能安全速度监控保留。"
},
"E0421":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"DEXTEROUS_SW","secondary_task":"",
 "task_evidence":"Translate state-of-the-art methods (RL / imitation policies, human-to-robot motion retargeting) into production-grade C++/Python.",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":R+"C++/Python is not the C language.",
  "3":[["V2_SIM2REAL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_DOMAIN_RANDOMIZATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "5":R+"Python and working C++ is not the C language.",
  "6":[["V2_CALIBRATION","PREFERRED","UNCONDITIONAL"],["V2_TELEOP","PREFERRED","UNCONDITIONAL"]]
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"灵巧操作。域随机化/Sim2Real保留。"
},
"E0439":dict(HUMANOID),
"E0440":dict(HUMANOID, new=dict(HUMANOID['new'], **{"8":R+"Salary USD is not Universal Scene Description."}), notes="Apptronik人形控制。薪酬USD拒收。"),
"E0379":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"DEXTEROUS_LEAD","secondary_task":"",
 "task_evidence":"Experience with the initial calibration and tuning of high-DOF robotic end-effectors.",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":[["V2_SIM2REAL","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"C++/Python is not the C language.",
  "5":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "6":[["V2_CALIBRATION","GENERAL","UNCONDITIONAL"]],
  "7":R+"Salary USD is not Universal Scene Description."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"灵巧操作负责人。英语can未单记CAN。"
},
"N0771":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"MANIPULATION","fine_task":"HUMANOID_MANIP","secondary_task":"",
 "task_evidence":"Support teleoperation, data collection, and human-in-the-loop workflows for improving manipulation performance",
 "new":{
  "1":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "2":[["V2_TELEOP","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":[["V2_CALIBRATION","DUTY_OWN_USE","UNCONDITIONAL"]],
  "4":R+"C++ is not the C language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FieldAI人形操作。"
},
"N0800":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"NAV_PLANNING","fine_task":"FIELD_PLANNING_CONTROL","secondary_task":"",
 "task_evidence":"Experience in classical planning and control, such as path planning, trajectory optimization, and model predictive control (MPC)",
 "new":{
  "1":[["V2_CLASSICAL_CONTROL","GENERAL","UNCONDITIONAL"],["V2_PATH_SEARCH","GENERAL","UNCONDITIONAL"]],
  "2":"DUPLICATE:N0800:1",
  "3":R+"C++ and Python is not the C language.",
  "4":[["V2_TENSORRT","GENERAL","EXAMPLE"],["V2_ONNX","GENERAL","EXAMPLE"],["V2_ONNX_RUNTIME","GENERAL","EXAMPLE"]],
  "5":"DUPLICATE:N0800:4",
  "6":"DUPLICATE:N0800:4",
  "7":R+"Onsite role is not Microsoft Office."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"FieldAI规划控制。TensorRT/ONNX保留。办公室拒收Office。"
},
"N0803":plan("N0803"),
"N0804":plan("N0804", extra={
  "6":R+"US government project is not Microsoft Project.",
  "7":R+"Company/team boilerplate is not the C language."
}),
"N0934":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"NAV_PLANNING","fine_task":"MOTION_PLANNING_PRINCIPAL","secondary_task":"MANIPULATION",
 "task_evidence":"Take on the hardest algorithmic problems in planning and control",
 "new":{
  "1":R+"English can is not Controller Area Network.",
  "2":[["V2_PATH_SEARCH","DUTY_OWN_USE","UNCONDITIONAL"]],
  "3":R+"Python and C++ is not the C language.",
  "4":[["V2_PATH_SEARCH","GENERAL","UNCONDITIONAL"]],
  "5":"DUPLICATE:N0934:2",
  "6":[["V2_GIT","GENERAL","UNCONDITIONAL"]],
  "7":"DUPLICATE:N0934:6",
  "8":O+"testing/CI benchmarking未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Pickle运动规划负责人。Git协作保留。"
},
"N0935":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"NAV_PLANNING","fine_task":"ROBOT_SW","secondary_task":"",
 "task_evidence":"Write production-grade software with Python and C++, meeting strict reliability, latency, and timing requirements for safety-critical operation",
 "new":{
  "1":R+"Python and C++ is not the C language.",
  "2":R+"C++ as a bonus is not the C language."
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"Pickle机器人软件。C++拒收C。"
}
}
if __name__=='__main__':
 register('RF_CONTROL_PLANNING', decisions, reader='grok4.6')
