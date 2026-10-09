from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0190':'中间件运行框架；测试执行与评测开发分开，具体工具含等。',
'E0177':'控制框架与推理管线；必备段与优先段分别定位，压缩既有策略网络不等于开发学习方法。',
'E0174':'机器人遥操音视频，原码成立；实时体验另有明确任职证据。',
'E0158':'整机架构，DDS/ROS未解，技能列表等字保留。',
'E0141':'Agent应用与视觉微调；优先段一项或多项覆盖各条，资格不引用职责。',
'E0129':'AI存储明确边界；技术与上下游用途未混同，未知语言保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('E0190','O12','本人测试中间件，未明设计评测方法或平台。',metric='DUTY_OWN_USE')
for e in ['1:0','1:1','1:2','1:3']:ov('E0190',e,'调试工具以等列举。',branch='EXAMPLE')
for e in ['3:0','3:1']:ov('E0190',e,'一种或多种与如/等同时作用。',branch='CHOICE_AND_EXAMPLE')
ov('E0190','6:0','量产、端云或CI/CD经验明确或。',branch='CHOICE')
ov('E0177','O2','C++一般资格改锚F14，原为职责。',metric='GENERAL',quote=ln('E0177',14))
for e in ['O6','O7','O8']:ov('E0177',e,'仿真器二次开发或自研引擎且等，具体仿真器继承两层关系。',branch='CHOICE_AND_EXAMPLE')
ov('E0177','O11','开发加速模块实现神经网络推理，使用模型而非研发学习模型，功能以等列举。',metric='DUTY_OWN_USE',branch='EXAMPLE')
for e in ['O15','O16']:ov('E0177',e,'RL/IL是待压缩部署的策略网络来源，未明本人研发或运用学习方法。',metric='SEPARATE',branch='MODEL_PROCESSING_OBJECT')
ov('E0177','O21','必备经历中的仿真到实机证据改锚F22，原职责不作资格。',metric='REQUIRED',quote=ln('E0177',22))
ov('E0177','O22','安全保护等实际问题为必备经验举例。',branch='EXAMPLE')
for e in ['O27','O28']:ov('E0177',e,'优先经历中的RL/IL是已训练网络类型，保留处理对象；原锚职责也不适当。',metric='SEPARATE',branch='MODEL_PROCESSING_OBJECT',quote=ln('E0177',32))
ov('E0177','O33','优先仿真经验改锚真实优先条F35，原职责不作资格。',metric='PREFERRED',quote=ln('E0177',35))
for e in ['2:0','5:0']:ov('E0177',e,'完成/解决虚实迁移及验证，未明研发迁移方法本身。',metric='DUTY_OWN_USE')
ov('E0177','4:0','借助既有量化、蒸馏压缩策略网络，属于应用压缩方法。',metric='DUTY_OWN_USE')
for e in ['8:0','9:0']:ov('E0177',e,'位于必备经历段。',metric='REQUIRED')
ov('E0177','11:0','F32位于优先考虑段。',metric='PREFERRED')
ov('E0177','12:1','原文明示ONNX Runtime，不推导ONNX格式能力。',metric='SEPARATE',branch='RUNTIME_NOT_FORMAT')
for e in ['12:0','12:2']:ov('E0177',e,'至少一种且等的具体推理框架。',branch='CHOICE_AND_EXAMPLE')
add('E0174','TC_REALTIME','GENERAL','UNCONDITIONAL',13,'明确理解视频参数对实时体验影响。')
for e in ['O2','O3','O5']:ov('E0158',e,'技能列表以等结尾。',branch='EXAMPLE')
ov('E0158','2:0','dds/ros裸斜线未解。',branch='UNRESOLVED')
for e in ['O1','O2']:ov('E0141',e,'ROS/ROS2职责版本关系未解。',branch='UNRESOLVED')
ov('E0141','O5','ROS2优先资格改锚F20，原职责不作资格。',metric='PREFERRED',quote=ln('E0141',20))
ov('E0141','O6','模块在包括等列表内。',branch='EXAMPLE')
for e in ['O10','O11']:ov('E0141',e,'一般经验清单以等结尾，无任选词。',branch='EXAMPLE')
ov('E0141','O12','VLA优先经验改锚任职字段第12行，原职责不作优先资格。',metric='PREFERRED',quote=RAW[RID['E0141']]['requirements'].splitlines()[11])
ov('E0141','O15','多模态模型优先经验改锚任职字段第13行，原职责不作优先资格。',metric='PREFERRED',quote=RAW[RID['E0141']]['requirements'].splitlines()[12])
R['E0141']['additions'].append(dict(code='TC_PERCEPTION',metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',quote=RAW[RID['E0141']]['duties'].splitlines()[5],reason='本人视觉检测识别分割适配微调，明确开发感知方法。'))
register(list(R.values()),'Astra_v3_boundary_sw_k')
