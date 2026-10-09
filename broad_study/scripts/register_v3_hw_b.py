from astra_review_tools import *
JUD={
'N0541':'固件本人开发、驱动校验明确，现场调试仅支持。STM32或类似MCU均是嵌入式，上位概念存在不随芯片选择而未知；Git一般，RTOS优先。',
'E0009':'完整来源标题称软件而职责明确六层板设计，保留BOARD_CIRCUIT和原冻结主类；没有Cadence要求，不能由相近E0010补入。',
'E0010':'完整来源与E0009职责相同但资格增加Cadence，保留两条广告及不同技术表达。PCB实际设计明确，未推出其他EDA品牌。',
'N0257':'原理图本人设计、PCB Layout指导别人，资格本人PCB设计经验独立存在。EMI/EMC外另有明确兼容与信号完整性分析，不乱扩U；仪器、电源分析仪不误成电源负载。',
'E0070':'采集装备/机器人本体硬件、电路PCB开发明确。接口协议斜线保持U；DSP/ARM/FPGA平台任选无冻结独立项，不从FPGA推出具体工具。',
'E0286':'按系统需求拆解与设计评审归电气系统架构细任务，原文未写具体线束。保持SE子对象，不把同宽任务当完全相同工作或猜PCB工具。',
'E0279':'关节电机电磁本体设计超出预设四任务，OTHER有明确细任务而非缺读。测试验收方案及分析是应用评测，无工具开发证据；FEA软件未指定品牌。',
'E0262':'单板闭环与原理图设计，Layout交付是与他人沟通；本人测试方案及执行不直接说明评测工具开发。硬件问题改善支持可靠性开发目标。',
'E0133':'线束图纸本人设计，测试和量产亦出现。客户现场走线优化是技术支持，不推出运行排障；CAD/CREO保持原具体写法与例示，无更多命名工具。',
}
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment=j,evidence_overrides=[]) for r,j in JUD.items()}
for eid in ['N0541:O5','N0541:O6']:R['N0541']['evidence_overrides'].append(dict(evidence_id=eid,branch='UNCONDITIONAL',reason='STM32或类似MCU均属同一嵌入式概念，概念知识本身明确。'))
for r,e in [('E0279','E0279:O3'),('E0262','E0262:O2')]:R[r]['evidence_overrides'].append(dict(evidence_id=e,metric='DUTY_OWN_USE',reason='制定执行测试方案及结果分析，未明示可复用测试工具或方法开发。'))
register(list(R.values()),'Astra_v3_hw_b')
