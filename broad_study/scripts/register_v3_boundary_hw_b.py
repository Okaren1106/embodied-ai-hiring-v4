from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0635':'ISP驱动：SLAM/识别为所服务对象；畸变校正与标定不是自动同义，未明参数校准保留未知；C/C++仅加分。',
'N0172':'MCU开发：接口等例示及控制算法如示例均有明确边界；泛RTOS不推具体FreeRTOS，OTA不推CI/CD。',
'E0232':'板级布局：SK_PCB是设计方法使用，不把PCB成品开发写成方法本身开发；生产分析为支持。',
'N0581':'BSP内核：明确Linux内核裁剪开发与一般系统知识分别保留；接口斜杠未知，外部技术沟通不当采购。',
}.items()}
R['N0635']['evidence_overrides'].append(dict(evidence_id='N0635:ADD1',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'],reason='畸变校正可能使用既有参数做图像校正；未明确传感器参数标定或校准，不能直接等同。'))
R['E0232']['evidence_overrides'].append(dict(evidence_id='E0232:O1',metric='DUTY_OWN_USE',reason='SK_PCB为工程设计方法；具体设计输出板卡，不是研发该方法。'))
register(list(R.values()),'Astra_v3_boundary_hw_b')
