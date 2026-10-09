from astra_review_tools import *
R=[
dict(reading_id='E0468',review_mode='FULL_SOURCE_AND_CODING',judgment='手动铣床车床一般知识与CNC优先分开；设备预防维修明确属于实际运行维护。泛fabrication不补具体加工类型，CATIA/Jira均优先。'),
dict(reading_id='N0903',review_mode='FULL_SOURCE_AND_CODING',judgment='本人修改Python测试脚本支持评测开发，同时HIL开发仅支持。测试仪器、Google Sheets与Linux要求明确；结构化执行和高保真记录的操作质量方法需补。',additions=[
dict(code='V2_SOP_OPERATION',metric='DUTY_OWN_USE',branch='UNCONDITIONAL',quote='Maintain meticulous data logging in Google Sheets and internal databases so engineering teams have accurate results for design iteration.',reason='明确执行测试数据记录规范和质量流程。'),
dict(code='V2_SOP_OPERATION',metric='GENERAL',branch='UNCONDITIONAL',quote='Comfortable executing structured test plans and logging high-fidelity data.',reason='明确流程执行与测试数据质量能力要求。')]),
dict(reading_id='E0594',review_mode='FULL_SOURCE_AND_CODING',judgment='道具班次管理，SOP执行明确且设计属于另一岗位；本人少量实操仅条件，不把物理道具识别成机器人操纵方法。雇佣试岗和工时管理支持HR职责。'),
dict(reading_id='E0577',review_mode='FULL_SOURCE_AND_CODING',judgment='制造工艺、装配及测试夹具设计明确；测试开发证据应定位本人设计测试夹具，非笼统实施质量体系。ERP/MRP内部关系U，质量体系知识是上位明确要求。',evidence_overrides=[
dict(evidence_id='E0577:8:0',branch='UNCONDITIONAL',reason='quality systems上位类别经验直接被要求，ISO9001只为其具体子型。'),
dict(evidence_id='E0577:O9',metric='DUTY_OWN_DEVELOP',quote='You will design assembly and test fixtures',reason='用明确本人设计测试夹具原句支持评测工具开发，避免仅由实施质量控制系统推断开发。')],additions=[
dict(code='TC_EVALUATION',metric='DUTY_OWN_USE',branch='EXAMPLE',quote='Implement quality control systems including inspection criteria, test protocols, and acceptance standards.',reason='本人实施质量系统下的测试协议为例示应用，与设计夹具开发分列。')]),
dict(reading_id='N0676',review_mode='FULL_SOURCE_AND_CODING',judgment='低量复杂制造执行、流程维护与新平台夹具开发成立。全部资格是Preferred；BOM数据层职责依个人长处may为条件，不计无条件。Python/Apps Script/REST明确任选且目录外保留。')]
register(R,'Astra_v3_mfg_i')
