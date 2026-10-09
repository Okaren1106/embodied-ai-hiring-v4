from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='BOUNDARY_CONTEXTS',judgment=j,evidence_overrides=[],additions=[]) for r,j in {
'N0513':'数据引擎：格式之间斜杠未明确任选，ROS和文件格式保持独立未知；训练/评测服务对象不加本人训练。',
'N0507':'数据平台：参与架构设计不独立承担；另句本人闭环建设保留，数据平台多个场景同上位。',
'N0151':'数采全栈：回读各缩略句；知识用于采集建设可保留，配合真机故障排查不独立承担。',
'N0161':'数采管理：调研导入平台或供应商可支持寻源任选；向供应商提技术改进意见不等于采购。',
'N0089':'数据质量：FMEA/SPC等职责编码例示；格式所在前半熟悉要求不能被最后一个了解具身数据者优先整体吞并。',
'N0135':'OLAP：Spark/Flink在一般技术要求，后半项目经验才加分；ClickHouse斜杠未解。',
'N0094':'数据SDK：类SQL、类AWS资源标识为接口设计参照；调度与文件格式的斜杠未明；至少两种格式的要求明确任选。',
}.items()}
def ov(r,e,why,**f):R[r]['evidence_overrides'].append(dict(evidence_id=r+':'+e,reason=why,**f))
for e in ['2:0','2:1','2:2']:ov('N0513',e,'rosbag/MCAP、Parquet/Arrow仅斜杠未确定任选关系。',branch='UNRESOLVED')
ov('N0507','O4','明确参与服务层架构建设，另条本人闭环能力独立保留。',metric='SEPARATE',branch='PARTICIPATION')
for e in ['O10','O11']:ov('N0507',e,'标注/自动驾驶/具身/大模型数据平台均数据上位；多模态数据处理也明确。',branch='UNCONDITIONAL')
ov('N0151','1:0','配合整机联调、故障排查，非独立承担。',metric='SEPARATE',branch='COLLABORATION')
ov('N0161','1:0','导入平台或供应商，供应商寻源是任选分支。',branch='CHOICE')
ov('N0161','2:0','向供应商反馈数据平台问题，不是寻源/谈判/供货管理。',metric='SEPARATE',branch='SUPPLIER_TECHNICAL_FEEDBACK')
for e in ['3:0','3:1']:ov('N0161',e,'unreal/blender等仅举例。',branch='EXAMPLE')
for e in ['O1','O2']:ov('N0089',e,'FMEA/SPC等质量方法论是例示。',branch='EXAMPLE')
for e in ['2:0','2:1']:ov('N0089',e,'前半熟悉格式为一般要求，最后了解具身逻辑才优先；斜杠仍未解。',metric='GENERAL',branch='UNRESOLVED')
ov('N0135','2:0','StarRocks/ClickHouse/Trino/Iceberg斜杠无明确任选。',branch='UNRESOLVED')
for e in ['9:0','9:1']:ov('N0135',e,'分号前是一般技术知识，分号后项目经验才加分。',metric='GENERAL')
for e in ['O2','O5']:ov('N0094',e,'原文明说类SQL或DSL接口，不据类比直接认定使用SQL语言。',metric='SEPARATE',branch='SQL_LIKE_INTERFACE')
for e in ['O3','O4','5:0','7:0','7:1']:ov('N0094',e,'Airflow/Ray或各数据格式斜杠，没有任选或兼具明示。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE','DUTY_OWN_USE_CHOICE','DUTY_OWN_USE_EXAMPLE','DUTY_OWN_USE_CHOICE_AND_EXAMPLE'])
for e in ['O9','19:0']:ov('N0094',e,'Airflow/Ray等的相互关系未明。',branch='UNRESOLVED')
for e in ['O6','12:0','12:1']:ov('N0094',e,'至少两种且等，兼有任选与例示。',branch='CHOICE_AND_EXAMPLE')
for e in ['O14','O15','O16','O17','O20']:ov('N0094',e,'各格式和工程经验选项均数据处理上位，数据能力明确。',branch='UNCONDITIONAL')
ov('N0094','23:0','加分项内标定，不是一般要求。',metric='PREFERRED')
register(list(R.values()),'Astra_v3_boundary_data_b')
