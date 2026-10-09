from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0549':'应用安全要求按安全上层类别合并；同一类别内部任选不转为未知，职责和资格重新定位。',
'E0484':'Android移动端；React Native为优先项中的任选，Kotlin等不扩目录。',
'E0551':'漏洞管理与企业安全；优先云平台与一般语言要求分开，安全方法同类替代不削弱上层类别。',
'E0560':'隐私数据治理；要求条款与职责严格分开，软件工程年限可替代隐私背景。',
'E0561':'机器人显示图形栈；Qt和Linux资格改锚真实要求，嵌入式任选和游戏引擎优先示例保留。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
def ln(r,n):return RAW[RID[r]]['full_description'].splitlines()[n-1]
for e in ['O8','O9','O12','O13','O14','O17','O18','O19','O21']:
 ov('E0549',e,'不同下位安全方法均属于冻结安全类别。',branch='UNCONDITIONAL')
ov('E0549','O10','原锚职责，安全领域资格见F10。',metric='GENERAL',branch='UNCONDITIONAL',quote=ln('E0549',10))
ov('E0549','O11','原锚职责；资格中的安全评估只是several domains的一项。',metric='GENERAL',branch='CHOICE',quote=ln('E0549',10))
ov('E0549','O20','相关安全岗位仍在安全类别，明确一般经验要求。',metric='GENERAL',branch='UNCONDITIONAL')
ov('E0551','O5','操作系统出现在several alternatives内部，括号本身不是示例。',branch='CHOICE')
for e in ['O7','O8','O9','O10','O14','O15','O17','O19','O20','O21','O22','O24']:
 ov('E0551',e,'同类别安全方法或角色替代，上层安全要求明确。',branch='UNCONDITIONAL')
for e in ['O11','O16','O23']:ov('E0551',e,'同类别安全方法或角色替代，上层安全要求明确。',metric='GENERAL',branch='UNCONDITIONAL')
for e in ['3:0','3:1','3:2']:ov('E0551',e,'原文preferably one of云平台为优先任选。',metric='PREFERRED',branch='CHOICE')
ov('E0560','O6','隐私服务including数据保留删除，具体数据处理属于例举。',branch='EXAMPLE')
for e,n in [('O8',11),('O20',13),('O21',11)]:ov('E0560',e,'资格证据移至隐私安全资格条款，原锚职责。',metric='GENERAL',branch='UNCONDITIONAL',quote=ln('E0560',n))
ov('E0560','O9','数据处理方法只是隐私领域资格的一个可选方向，原锚职责。',metric='GENERAL',branch='CHOICE',quote=ln('E0560',11))
for e in ['O10','O12','O16','O17','O18']:ov('E0560',e,'隐私安全下位方向任选不改变上层安全类别。',branch='UNCONDITIONAL')
ov('E0560','O11','上位several domains限定仍适用数据处理方法。',branch='CHOICE')
for e in ['O15','O19']:ov('E0560',e,'资格移至data governance or privacy control原句，保留数据治理的任选。',metric='GENERAL',branch='CHOICE',quote=ln('E0560',13))
ov('E0561','O3','Qt资格见Requirements下expert proficiency，原为职责。',metric='GENERAL',quote=ln('E0561',15))
ov('E0561','O5','Linux资格见Requirements，原为职责。',metric='GENERAL',quote=ln('E0561',19))
ov('E0561','O9','embedded or resource-constrained明确可替代。',branch='CHOICE')
for e in ['2:0','2:1']:ov('E0561',e,'such as与or同时出现。',branch='CHOICE_AND_EXAMPLE')
R['E0561']['additions'].append(dict(code='V2_CI_CD',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote=ln('E0561',11),reason='本人建立开发测试及CI集成实践。'))
register(list(R.values()),'Astra_v3_boundary_sw_q')
