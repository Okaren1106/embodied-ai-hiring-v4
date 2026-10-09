from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0550':'设备安全：总体嵌入式安全领域内任选子方向不改变上位安全/嵌入式要求；应用/硬件安全同一安全上位。',
'E0466':'电气实习：本人Design and test明确，PCB设计方法使用；Bonus和preferably的局部优先保留。',
'E0475':'固件：职责C或C++与一般C、C++、Python并列有别；Serial按已冻结宽串口组补录。',
'E0477':'固件实习：职责明确承担，CI/CD协作与优先分列；Serial按冻结别名补入，不把实习身份当技术关系。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O7','O8','O9','O10','O11','O12','O15','O16']:ov('E0550',e,'选项处于明确嵌入式安全领域或安全经验上位内，上位概念不再任选或未知。',branch='UNCONDITIONAL')
ov('E0466','O1','PCB设计方法用于实体板卡设计。',metric='DUTY_OWN_USE')
for r,n in [('E0475',15),('E0477',14)]:
 R[r]['additions'].append(dict(code='V2_RS485',metric='GENERAL',branch='CHOICE_AND_EXAMPLE',quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason='Serial匹配冻结宽串口组；like与or分别保留示例和任选，不解为明确RS485。'))
register(list(R.values()),'Astra_v3_boundary_hw_r')
