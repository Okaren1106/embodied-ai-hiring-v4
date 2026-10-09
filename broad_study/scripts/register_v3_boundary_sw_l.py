from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0115':'端侧模型部署是模型使用，ONNX Runtime不补ONNX格式。',
'E0114':'VR应用使用Unity/UE，MuJoCo数据来源与实际引擎使用区分；资格定位修复。',
'E0306':'CAD基础设施管理，工具集成不是工具本体开发，Bonus段不能当一般资格。',
'E0339':'功能安全软件，Minimum/Preferred段分开，真正任职证据重新定位，显式C补齐。',
'E0418':'SRE用IaC工具写配置，语言/平台裸斜线未解；生产事件支持改用明确停机条款。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
def add(r,c,m,b,n,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=ln(r,n),reason=why))
ov('E0115','O8','模型本地部署、推理加速及维护是使用模型，未明训练研发模型。',metric='DUTY_OWN_USE')
ov('E0115','2:1','只明确ONNX Runtime，不推ONNX格式。',metric='SEPARATE',branch='RUNTIME_NOT_FORMAT')
for e in ['2:0','2:2']:ov('E0115',e,'或与如等共同作用。',branch='CHOICE_AND_EXAMPLE')
ov('E0114','O3','对接MuJoCo仿真数据未明实际运行引擎。',metric='SEPARATE',branch='DATA_SOURCE')
for e,n in [('O4',14),('O5',16),('O6',17),('O7',19)]:ov('E0114',e,'资格要求改锚真实任职句，原引用职责。',metric='GENERAL',quote=ln('E0114',n))
ov('E0114','O10','MuJoCo优先资格改锚F28，原为职责。',metric='PREFERRED',quote=ln('E0114',28))
ov('E0114','O15','VR/AR或实时3D经验明确任选。',branch='CHOICE')
for e in ['O21','O22']:ov('E0114',e,'优先经验原句各选项均为仿真相关项目，上层仿真非任选，修复职责锚点。',metric='PREFERRED',branch='UNCONDITIONAL',quote=ln('E0114',28))
for e in ['2:0','3:0']:ov('E0114',e,'基于引擎开发应用/场景是引擎使用。',metric='DUTY_OWN_USE')
for e in ['11:0','12:0']:ov('E0114',e,'Unity/UE裸斜线未解。',branch='UNRESOLVED')
for n in [28,29]:add('E0114','V2_UNREAL','PREFERRED','UNRESOLVED',n,'UE明确别名，但Unity/UE关系未解。')
ov('E0306','O3','维护工具集成并非开发Altium本体，or equivalent明确任选。',metric='DUTY_OWN_USE',branch='CHOICE')
ov('E0306','O4','与ERP集成为使用ERP，不是开发ERP本体。',metric='DUTY_OWN_USE')
ov('E0306','O11','Windchill一般经验引用F31，原为职责。',metric='GENERAL',quote=ln('E0306',31))
ov('E0306','O12','Creo一般经验引用F32，原为培训职责。',metric='GENERAL',quote=ln('E0306',32))
for e in ['O14','O17','O18']:ov('E0306',e,'优先工具经验引用F46，原为职责/培训。',metric='PREFERRED',quote=ln('E0306',46))
ov('E0306','O15','like与or similar兼具。',branch='CHOICE_AND_EXAMPLE')
for e in ['2:0','4:0','5:0','6:0']:ov('E0306',e,'F40起Bonus Points段，无新的一般要求标题。',metric='PREFERRED',branch='CHOICE' if e=='4:0' else 'UNCONDITIONAL')
ov('E0339','O5','Linux优先经验改锚F46，原引用职责。',metric='PREFERRED',quote=ln('E0339',46))
ov('E0339','O14','systems level或embedded systems明确任选。',branch='CHOICE')
ov('E0339','O15','另条明确嵌入式架构要求，改锚F22。',metric='REQUIRED',quote=ln('E0339',22))
ov('E0339','O16','F23只是追求质量可靠性的内在动机，非可靠性技术资格；原为测试职责。',metric='SEPARATE',branch='SOFT_VALUE',quote=ln('E0339',23))
ov('E0339','O20','可靠性优先经验改锚Linux定制F46，原为职责。',metric='PREFERRED',quote=ln('E0339',46))
ov('E0339','O21','实时系统优先经验改锚F48至F50完整句。',metric='PREFERRED',quote='\n'.join(RAW[RID['E0339']]['full_description'].splitlines()[47:50]))
ov('E0339','O19','数据采集/管理是including子项。',branch='EXAMPLE')
for e in ['3:0','4:0']:ov('E0339',e,'标准位于Preferred段，such as标准列表，同一安全标准类别内部or。',metric='PREFERRED',branch='EXAMPLE',quote='\n'.join(RAW[RID['E0339']]['full_description'].splitlines()[33:40]))
for e in ['5:0','6:0']:ov('E0339',e,'QNX及CI/CD均位于Preferred段。',metric='PREFERRED')
add('E0339','V2_C','REQUIRED','CHOICE',21,'显式C与C++/Rust为不同语言候选。')
add('E0339','TC_PERCEPTION','PREFERRED','UNCONDITIONAL',30,'优先感知系统要求明确相机/LiDAR输出解释。')
ov('E0418','O1','Python/Typescript裸斜线未解。',branch='UNRESOLVED')
ov('E0418','O4','一般Python要求改锚F16，原为职责。',metric='GENERAL',quote=ln('E0418',16))
ov('E0418','O11','安全问题排查是使用，未明开发安全方法。',metric='DUTY_OWN_USE')
for e in ['1:0','1:1']:ov('E0418',e,'用IaC工具写配置，工具括号并列无任选。',metric='DUTY_OWN_USE',branch='UNCONDITIONAL')
ov('E0418','2:0','用Typescript写代码是语言使用，斜线未解。',metric='DUTY_OWN_USE',branch='UNRESOLVED')
ov('E0418','3:0','生产停机/值班支持证据改用F11。',metric='DUTY_OWN_USE',quote=ln('E0418',11))
for e in ['4:0','4:1']:ov('E0418',e,'工具括号并列无任选词。',branch='UNCONDITIONAL')
ov('E0418','5:0','任职工具和语言裸斜线未解。',branch='UNRESOLVED')
register(list(R.values()),'Astra_v3_boundary_sw_l')
