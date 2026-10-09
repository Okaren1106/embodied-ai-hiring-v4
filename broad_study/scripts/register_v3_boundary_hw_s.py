from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0576':'线束：PLM版本管理、CAD能力和EMC方法应用明确；供应商DFM协调不当本人独立制造方法使用。',
'E0476':'制造固件：Minimum技术要求与Preferred脚本分列；电源系统是固件验证的被测对象，非本人电力电子方法开发。',
'N0920':'嵌入式Linux：展开at least one语言句；BSP驱动和固件升级任务明确，供应商内核驱动按上下文定位。',
'N0660':'相机软件：展开所有重复技术句；明确Linux驱动开发、本人标定，优先工具及协议细项区别可确定和任选。',
'N0702':'电气：Preferred全段保持优先；EMC/EMI同族，上位明确，屏蔽接地设计为方法应用。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
ov('E0476','O7','软件验证电源系统是测试对象，不能等同本人使用电力电子设计技术。',metric='SEPARATE',branch='TEST_OBJECT')
ov('N0702','9:0','EMC和EMI在同一冻结方法族。',branch='UNCONDITIONAL')
ov('N0702','ADD2','定义屏蔽接地方案应用EMC方法。',metric='DUTY_OWN_USE')
register(list(R.values()),'Astra_v3_boundary_hw_s')
