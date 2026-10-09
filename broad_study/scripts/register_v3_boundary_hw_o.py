from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'E0427':'Compute架构：算法是服务对象；明确PCB方法使用，功能安全标准上位要求确定，IEC仅具体标准示例。',
'E0428':'Compute架构：与另一身份逐条核对；架构、热管理、测试开发与一般要求区分不变。',
'E0429':'末端电子：PCB/PCBA、PMSM/BLDC、FET/GaN在各自上位内不再未知；硬件/固件仍跨对象不确定。',
'E0393':'Senior FPGA：重新完整回读包中被截断部分；本人子系统设计有效，架构和电源为协作；仿真上位确定，具体品牌目录缺口保留。',
'E0394':'Senior FPGA：独立身份保留，与同文广告统一上位仿真和协议不清关系；指导布局不虚构EDA品牌。',
'E0431':'Staff FPGA：整板架构与PLM本人使用明确；仿真工具任选不影响仿真概念，上位与细协议分别判。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for r in R:ov(r,'O1','PCB设计为工程方法，设计实体板卡属于方法使用。',metric='DUTY_OWN_USE')
for r in ['E0427','E0428']:ov(r,'4:0','明示功能安全标准能力；IEC61508仅是标准族的例子。',branch='UNCONDITIONAL')
for e in ['O8','O19','O20','O22']:ov('E0429',e,'斜线两端在相应PCB/执行器/控制/功率电子上位概念内。',branch='UNCONDITIONAL')
for r in ['E0393','E0394','E0431']:
 ov(r,'O12','明确simulation，无该上位概念的示例或任选；具体仿真器为可替代选择。',branch='UNCONDITIONAL')
 R[r]['additions'].append(dict(code='V2_GMSL',metric='DUTY_OWN_USE',branch='UNRESOLVED',quote=RAW[RID[r]]['full_description'].splitlines()[8],reason='本人接口设计中明示GMSL2，但与FPD-Link/PoC斜线关系不清，保留职责使用未知。'))
for r,n in [('E0429',15),('E0431',15)]:
 R[r]['additions'].append(dict(code='V2_PROCUREMENT',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote=RAW[RID[r]]['full_description'].splitlines()[n-1],reason='明确本人供应商及合同制造关系管理。'))
register(list(R.values()),'Astra_v3_boundary_hw_o')
