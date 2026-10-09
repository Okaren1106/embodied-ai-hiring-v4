"""First-pass adjudication for mechanical coding_order 81-91. Reader: grok4.6."""
from register_Q_decisions import register
O='OUTSIDE:';R='REJECT:';RC='REVIEWED_ACCEPT_RETAINED_UNKNOWN'
FIG={
 "inherited":RC,"task":"ROBOT_STRUCTURE","fine_task":"MECH","secondary_task":"",
 "task_evidence":"Generate accurate 2D drawings using GD&T per ASME Y14.5",
 "new":{"1":R+"industrial design form factor不是本人承担CMF。","2":[["V2_GD_STANDARD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]]},
 "old_overrides":{},"additions":[],"outside_extra":[],"notes":"Figure机械。GD&T保留。外形约束不记CMF。"
}
def fig(rid, extra=None, evidence=None, notes=None, task=None, fine=None):
 d=dict(FIG); d['new']=dict(FIG['new'])
 if extra: d['new'].update(extra)
 if evidence: d['task_evidence']=evidence
 if notes: d['notes']=notes
 if task: d['task']=task
 if fine: d['fine_task']=fine
 return d
decisions={
"E0519":fig("E0519"),
"E0554":fig("E0554", fine="CHARGING", evidence="Concept to production ownership of the mechanical and thermal components"),
"E0523":fig("E0523", fine="ECOSYSTEM"),
"E0524":{"inherited":RC,"task":"SOFT_GOODS","fine_task":"SOFTGOODS","secondary_task":"","task_evidence":"Own the industrial design robot buck, keep up to date with latest files from our engineers and communicate with suppliers","new":{"1":R+"company office boilerplate不是Microsoft Office。","2":R+"industrial design form factor不是本人承担CMF。","3":[["V2_CMF_DESIGN","DUTY_OWN_USE","UNCONDITIONAL"]],"4":[["V2_GD_STANDARD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],"5":[["V2_CMF_DESIGN","GENERAL","UNCONDITIONAL"]],"6":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]]},"old_overrides":{},"additions":[],"outside_extra":[],"notes":"软体/塑料。ID buck记CMF。GD&T/注塑保留。"},
"E0520":{"inherited":RC,"task":"ACTUATOR_GEAR","fine_task":"HANDS","secondary_task":"","task_evidence":"Generate accurate 2D drawings using GD&T in accordance with ASME Y14.5","new":{"1":R+"company office boilerplate不是Microsoft Office。","2":R+"industrial design requirements不是本人承担CMF。","3":[["V2_GD_STANDARD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],"4":[["V2_DOE_MSA","GENERAL","UNCONDITIONAL"]],"5":"DUPLICATE:E0520:4"},"old_overrides":{},"additions":[],"outside_extra":[],"notes":"灵巧手机械。GD&T/DOE保留。"},
"E0522":{"inherited":RC,"task":"COMPONENT_PROCESS","fine_task":"INTEG_TEST","secondary_task":"","task_evidence":"Cradle to grave ownership of prototype integration and test equipment","new":{"1":R+"company office boilerplate不是Microsoft Office。","2":[["V2_GD_STANDARD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]]},"old_overrides":{},"additions":[],"outside_extra":[],"notes":"集成测试机械。GD&T保留。"},
"E0525":{"inherited":RC,"task":"ROBOT_STRUCTURE","fine_task":"HAND_STRUCT","secondary_task":"","task_evidence":"Design structural parts and assemblies in 3D CAD that meet load, durability, manufacturability, and packaging requirements","new":{"1":R+"company office boilerplate不是Microsoft Office。","2":[["V2_GD_STANDARD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]]},"old_overrides":{},"additions":[],"outside_extra":[],"notes":"手部结构。GD&T保留。"},
"E0521":{"inherited":RC,"task":"SOFT_GOODS","fine_task":"HAND_COMPLIANT","secondary_task":"","task_evidence":"specific focus on flexible substrates, overmolding, and skin/grip interfaces","new":{"1":R+"company office boilerplate不是Microsoft Office。","2":[["V2_CNC_PROCESS","DUTY_OWN_USE","UNCONDITIONAL"]],"3":R+"industrial design requirements不是本人承担CMF。","4":[["V2_GD_STANDARD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],"5":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],"6":R+"FEA for non-linear materials不是Linear工具。","7":[["V2_DOE_MSA","GENERAL","UNCONDITIONAL"]],"8":"DUPLICATE:E0521:7"},"old_overrides":{},"additions":[],"outside_extra":[],"notes":"柔性手部。成型/GD&T/DOE保留。"},
"E0552":{"inherited":RC,"task":"ACTUATOR_GEAR","fine_task":"GEAR","secondary_task":"","task_evidence":"Own gear design end-to-end: system-level sizing, macro and micro geometry definition, rating and life analysis","new":{"1":R+"company office boilerplate不是Microsoft Office。","2":[["V2_KISSSOFT","DUTY_OWN_USE","UNCONDITIONAL"]],"3":[["V2_DFM","DUTY_OWN_USE","UNCONDITIONAL"]],"4":[["V2_GD_STANDARD","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],"5":[["V2_KISSSOFT","GENERAL","UNCONDITIONAL"]],"6":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],"7":[["V2_DOE_MSA","PREFERRED","UNCONDITIONAL"]],"8":"DUPLICATE:E0552:5"},"old_overrides":{},"additions":[],"outside_extra":[],"notes":"齿轮设计。KISSsoft/DFM/GD&T/成型/DOE保留。"},
"E0606":{"inherited":RC,"task":"COMPONENT_PROCESS","fine_task":"PROTOTYPE","secondary_task":"","task_evidence":"Rapidly design and fabricate mechanical, electrical, and sensor prototypes to support research experiments","new":{"1":R+"English can is not Controller Area Network.","2":[["V2_INCIDENT_SUPPORT","DUTY_OWN_USE","UNCONDITIONAL"]],"3":[["V2_ONSHAPE","GENERAL","CHOICE"],["V2_FUSION360","GENERAL","CHOICE"]],"4":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]]},"old_overrides":{},"additions":[],"outside_extra":[],"notes":"原型工程师。Onshape/Fusion/成型/排障保留。"},
"N0677":{"inherited":RC,"task":"COMPONENT_PROCESS","fine_task":"MECH_DESIGN","secondary_task":"","task_evidence":"create and fabricate robotic systems for teleoperation, human-robot interaction and data collection","new":{"1":[["V2_TELEOP","DUTY_OWN_DEVELOP","UNCONDITIONAL"]],"2":[["V2_CNC_PROCESS","DUTY_OWN_USE","UNCONDITIONAL"]],"3":[["V2_ONSHAPE","GENERAL","CHOICE"]],"4":"DUPLICATE:N0677:3","5":O+"Arduino未单列冻结项。","6":[["V2_CNC_PROCESS","GENERAL","UNCONDITIONAL"]],"7":[["V2_TELEOP","PREFERRED","UNCONDITIONAL"]],"8":R+"Salary USD is not Universal Scene Description."},"old_overrides":{},"additions":[],"outside_extra":[],"notes":"机械设计。遥操/3D打印/Onshape保留。"}
}
if __name__=='__main__':
 register('RF_MECHANICAL_MECHATRONICS', decisions, reader='grok4.6')
