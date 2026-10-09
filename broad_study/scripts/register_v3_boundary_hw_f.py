from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0503':'嵌入式开发：MCU与SoC经验在同上位概念内；Linux与实时系统跨类任选保留，测试方案开发与执行分别成立。',
'N0496':'板卡设计：PCB设计方法使用成立；STM32 ARM或类似处理器均为嵌入式上位要求。',
'N0515':'电池BMS：本人交付电池及供电系统，关节和运动控制是匹配对象；任务OTHER具体对象保留。',
'N0480':'硬件架构：明确本人PCB评审与技术实现；末尾追踪技术趋势不等同本人使用执行器或嵌入式。',
'N0466':'校招硬件：参与设计与本人仪器测试分列；PCB类型和CAN协议变体在各自同一上位条目内。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['O9','O10']:ov('N0503',e,'MCU与SoC软件开发均属同一嵌入式概念。',branch='UNCONDITIONAL')
ov('N0496','O7','处理器选项全部属嵌入式开发。',branch='UNCONDITIONAL')
ov('N0515','O8','电池与关节电气匹配不能证明本人执行器机械使用或开发。',metric='SEPARATE',branch='MATCHING_OBJECT')
for e in ['O14','O15']:ov('N0480',e,'追踪发展趋势和推动落地尚未明确本人实施的工具或技术任务。',metric='SEPARATE',branch='TECHNOLOGY_WATCH')
for e in ['O10','O11','O12']:ov('N0466',e,'多层、高速与大电流均为PCB设计知识。',branch='UNCONDITIONAL')
ov('N0466','9:3','CAN与CAN FD同属冻结CAN总线族。',branch='EXAMPLE')
ov('N0466','17:0','列举的隔离、接地、ESD、浪涌、EMC和完整性设计均为冻结兼容/完整性方法族。',branch='UNCONDITIONAL')
register(list(R.values()),'Astra_v3_boundary_hw_f')
