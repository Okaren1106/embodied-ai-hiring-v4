"""First-pass adjudication for software coding_order 177-181. Reader: grok4.6."""
from register_Q_decisions import register

O='OUTSIDE:';R='REJECT:'
decisions={
"N0693":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_RUNTIME","fine_task":"MANIPULATION_CONTROLS_SW","secondary_task":"",
 "task_evidence":"Write controllers, planners, and perception stacks for real-world robotic deployment",
 "new":{
  "1":R+"C++不是C语言。",
  "2":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"操作与控制软件。C++拒收C。"
},
"N0701":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"DEVOPS_HIL","secondary_task":"",
 "task_evidence":"You will own the systems that let our engineering teams move fast — from build tooling and CI/CD pipelines to cross-platform hardware-in-the-loop testing infrastructure.",
 "new":{
  "1":[["V2_HIL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_BAZEL","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0701:2",
  "4":O+"Skylark未单列冻结项。",
  "5":"DUPLICATE:N0701:2",
  "6":"DUPLICATE:N0701:4",
  "7":[["V2_JENKINS","DUTY_OWN_USE","EXAMPLE"],["V2_HIL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CI_CD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "8":"DUPLICATE:N0701:7","9":"DUPLICATE:N0701:7",
  "10":O+"ARM/aarch64未单列冻结项。",
  "11":"DUPLICATE:N0701:10","12":"DUPLICATE:N0701:10","13":"DUPLICATE:N0701:10",
  "14":[["V2_AWS","DUTY_OWN_USE","CHOICE"],["V2_GCP","DUTY_OWN_USE","CHOICE"],["V2_AZURE","DUTY_OWN_USE","CHOICE"]],
  "15":"DUPLICATE:N0701:14","16":"DUPLICATE:N0701:14","17":"DUPLICATE:N0701:14",
  "18":[["V2_TERRAFORM","DUTY_OWN_USE","UNCONDITIONAL"],["V2_ANSIBLE","DUTY_OWN_USE","UNCONDITIONAL"]],
  "19":"DUPLICATE:N0701:18","20":"DUPLICATE:N0701:18",
  "21":[["V2_BAZEL","GENERAL","UNCONDITIONAL"]],
  "22":[["V2_JENKINS","PREFERRED","EXAMPLE"],["V2_HIL","PREFERRED","UNCONDITIONAL"]],
  "23":[["V2_SHELL","GENERAL","UNCONDITIONAL"]],
  "24":"DUPLICATE:N0701:23",
  "25":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"DevOps与HIL。SIL/HIL只记HIL，拒收功能安全分析。Skylark/ARM目录外。"
},
"N0705":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"EDGE_CLOUD_FLEET","secondary_task":"ROBOT_RUNTIME",
 "task_evidence":"We are seeking a versatile Robotics Infrastructure Engineer to build the edge-to-cloud systems that connect, manage, update, and monitor our robot fleet at scale.",
 "new":{
  "1":R+"C++不是C语言。",
  "2":R+"C++不是C语言。",
  "3":O+"edge-to-cloud data pipelines未单列冻结项。",
  "4":O+"OTA未单列冻结项。",
  "5":R+"C++不是C语言。",
  "6":[["V2_AWS","PREFERRED","EXAMPLE"],["V2_GCP","PREFERRED","EXAMPLE"]],
  "7":"DUPLICATE:N0705:6","8":"DUPLICATE:N0705:6",
  "9":O+"EC2未单列冻结项。","10":O+"S3未单列冻结项。","11":O+"Lambda未单列冻结项。",
  "12":O+"MQTT未单列冻结项。","13":O+"WebSockets未单列冻结项。","14":O+"gRPC未单列冻结项。",
  "15":O+"OTA未单列冻结项。","16":O+"OTA未单列冻结项。",
  "17":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"端云车队基础设施。C++拒收C。OTA/MQTT/gRPC目录外。"
},
"N0711":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"DEV_INFRA","fine_task":"MFG_TEST_SOFTWARE","secondary_task":"",
 "task_evidence":"We're hiring a zero-to-one software engineer to build the manufacturing test and production systems for our robot assembly line.",
 "new":{
  "1":[["V2_HIL","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_CALIBRATION","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "2":[["V2_PLC","DUTY_OWN_USE","EXAMPLE"],["V2_DAQ","DUTY_OWN_USE","EXAMPLE"]],
  "3":"DUPLICATE:N0711:2","4":"DUPLICATE:N0711:2",
  "5":[["V2_MES","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_PLM","DUTY_OWN_DEVELOP","EXAMPLE"]],
  "6":"DUPLICATE:N0711:5",
  "7":O+"OpenBOM未单列冻结项。",
  "8":"DUPLICATE:N0711:5",
  "9":R+"任职头衔中的MES不是MES系统使用。",
  "10":R+"薪酬USD不是Universal Scene Description。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"制造测试软件。HIL/标定主责。OpenBOM目录外。头衔MES拒收。"
},
"N0668":{
 "inherited":"REVIEWED_ACCEPT_RETAINED_UNKNOWN",
 "task":"ROBOT_CLOUD_UI","fine_task":"FLEET_UI_ANDROID","secondary_task":"",
 "task_evidence":"You will be responsible for designing and implementing high-performance applications that render real-time 3D environments, telemetry, and maps.",
 "new":{
  "1":O+"Android未单列冻结项。",
  "2":[["V2_JAVASCRIPT","DUTY_OWN_DEVELOP","UNCONDITIONAL"],["V2_TYPESCRIPT","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],
  "3":"DUPLICATE:N0668:2","4":"DUPLICATE:N0668:2",
  "5":[["V2_JAVASCRIPT","GENERAL","UNCONDITIONAL"],["V2_TYPESCRIPT","GENERAL","UNCONDITIONAL"]],
  "6":"DUPLICATE:N0668:5","7":"DUPLICATE:N0668:5",
  "8":[["V2_REACT","GENERAL","UNCONDITIONAL"]],
  "9":"DUPLICATE:N0668:8",
  "10":[["V2_CI_CD","GENERAL","UNCONDITIONAL"]],
  "11":"DUPLICATE:N0668:10",
  "12":[["V2_JAVASCRIPT","PREFERRED","UNCONDITIONAL"],["V2_TYPESCRIPT","PREFERRED","UNCONDITIONAL"],["V2_REACT","PREFERRED","CHOICE"],["V2_VUE","PREFERRED","CHOICE"]],
  "13":"DUPLICATE:N0668:12","14":"DUPLICATE:N0668:12","15":"DUPLICATE:N0668:12",
  "16":O+"Android未单列冻结项。",
  "17":[["V2_UNITY","PREFERRED","CHOICE"],["V2_UNREAL","PREFERRED","CHOICE"]],
  "18":O+"WebGL未单列冻结项。","19":O+"Pixi未单列冻结项。",
  "20":R+"Three.js不是JavaScript语言项的充分证据。",
  "21":O+"OpenGL未单列冻结项。",
  "22":"DUPLICATE:N0668:17","23":"DUPLICATE:N0668:17",
  "24":O+"CRDTs未单列冻结项。"
 },
 "old_overrides":{},"additions":[],"outside_extra":[],
 "notes":"车队前端。Android/CRDTs目录外。Three.js拒收JS。Unity/Unreal任选。"
}
}
if __name__=='__main__':
 register('RF_ROBOTICS_SOFTWARE', decisions, reader='grok4.6')
