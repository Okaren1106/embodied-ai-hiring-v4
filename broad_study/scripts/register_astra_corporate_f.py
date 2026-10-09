from astra_review_tools import *
R={r:dict(reading_id=r,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for r in ['E0572','E0470','E0532','E0531','E0582']}
def ov(r,e,why,**v):R[r]['evidence_overrides'].append(dict(evidence_id=e,reason=why,**v))
def add(r,c,m,b,q,why):R[r]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=why))
R['E0572']['judgment']='本人招聘多个职能，不等于掌握这些职能技术。Bonus下技术招聘知识为优先，行业和机构经历or分支需保留；面试流程改进是明确本人招聘方法开发。'
ov('E0572','E0572:9:0','此条位于Bonus Qualifications。',metric='PREFERRED')
for eid in ['E0572:8:0','E0572:10:0']:ov('E0572',eid,'局部行业/机构路径明确or。',branch='CHOICE')
add('E0572','V2_HR','DUTY_OWN_DEVELOP','UNCONDITIONAL','Drive improvements to the technical interview process','本人推动面试流程改进，不是泛化应聘说明。')
R['E0470']['judgment']='葡语设施管理全文有供应商合同/SLA、工单升级和操作手册，不应只计职业安全。运行对象为办公设施，不归机器人客户现场；优先职业安全规范知识与职责分开。'
add('E0470','V2_PROCUREMENT','DUTY_OWN_USE','UNCONDITIONAL','Ser o dono dos contratos de fornecedores, SLAs (acordos de nível de serviço) e chamados','本人供应商合同、服务水平与履约管理。')
add('E0470','V2_PROCUREMENT','GENERAL','UNCONDITIONAL','Experiência gerenciando fornecedores e prestadores terceirizados com autonomia.','明确独立管理外包供应服务经验。')
add('E0470','V2_INCIDENT_SUPPORT','DUTY_OWN_USE','UNCONDITIONAL','definir rotinas de escalação e conduzir os problemas até a resolução.','设施在役工单升级与问题闭环；保留设施具体对象。')
add('E0470','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','Construir o playbook (manual de processos) de facilities','明确编制设施运行流程手册。')
add('E0470','TC_SAFETY','PREFERRED','UNCONDITIONAL','Familiaridade com as Normas Regulamentadoras (NRs) de segurança do trabalho.','Diferenciais即加分项，明示职业安全规范知识；不判断现行法规内容。')
R['E0532']['judgment']='葡语明确人力全流程、CLT劳动关系与制度设计；原仅HRIS为重大漏项。招聘/薪酬供应商为服务对象，不能从工种推研发技能。本人承担与一般经验均补原文。'
add('E0532','V2_HR','DUTY_OWN_USE','UNCONDITIONAL','Conduzir operações de recrutamento em volume: pipelines, agendamento, experiência do candidato, coordenação com agências e logística de ofertas.','本人执行批量招聘运营。')
add('E0532','V2_HR','DUTY_OWN_DEVELOP','UNCONDITIONAL','Construir os processos, políticas e ferramentas de People conforme o time escala.','本人建立人力流程、制度和工具。')
add('E0532','V2_HR','GENERAL','UNCONDITIONAL','4-8 anos em RH com atuação generalista, cobrindo o ciclo completo do colaborador.','4至8年人力通才经验的一般要求。')
add('E0532','V2_HR','GENERAL','CHOICE','Experiência apoiando ou conduzindo processos de recrutamento','支持或主持招聘流程经验任选，不混同未来本人承担。')
add('E0532','V2_LEGAL','DUTY_OWN_USE','UNCONDITIONAL','Ser o responsável pelos registros dos colaboradores e pela conformidade com a legislação trabalhista brasileira.','本人负责雇佣记录与巴西劳动法律合规。')
add('E0532','V2_LEGAL','GENERAL','UNCONDITIONAL','Domínio das rotinas de CLT: admissão, ponto, férias, desligamentos e benefícios.','明确法定雇佣管理流程知识。')
R['E0531']['judgment']='西语明确招聘、人力制度及墨西哥劳动关系，与只保留HRIS明显不符。标题/墨西哥法律和正文巴西/圣保罗地点存在模板冲突；不修源、不据此作工作地点结论，HR方法仍可识别。'
add('E0531','V2_HR','DUTY_OWN_USE','UNCONDITIONAL','Liderar operaciones de reclutamiento en volumen: pipelines, agendamiento, experiencia del candidato, coordinación con agencias y logística de ofertas.','本人主持批量招聘。')
add('E0531','V2_HR','DUTY_OWN_DEVELOP','UNCONDITIONAL','Construir desde cero los procesos, políticas y herramientas de People conforme el equipo crece.','本人从零建立人力流程。')
add('E0531','V2_HR','GENERAL','UNCONDITIONAL','4+ años en RR. HH. con actuación generalista, cubriendo el ciclo completo del colaborador.','明确人力通才工作经验。')
add('E0531','V2_HR','GENERAL','CHOICE','Experiencia apoyando o liderando procesos de reclutamiento','支持或主持招聘经验任选。')
add('E0531','V2_LEGAL','DUTY_OWN_USE','UNCONDITIONAL','Ser el responsable de los registros de los colaboradores y del cumplimiento de la legislación laboral mexicana.','本人负责雇佣记录及明确劳动法律合规，地域冲突另作来源限制。')
R['E0582']['judgment']='商业运营的数据算力合作与供方谈判明确，不能从采购对象推数据管线。部署opportunities可能是客户机会，不能必然计采购；补商业经营、供方优先谈判和明确项目计划应用。'
ov('E0582','E0582:2:0','sourcing opportunities在deployment商业语境中买方/卖方关系未明，不把一切sourcing当采购。',metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['DUTY_OWN_USE'])
add('E0582','V2_PROCUREMENT','PREFERRED','CHOICE','Experience negotiating vendor, data, or infrastructure agreements.','明确供方/数据/基础设施协议谈判经验任选。')
add('E0582','V2_SALES_CRM','DUTY_OWN_USE','UNCONDITIONAL','Plug into deployment efforts: sourcing opportunities, structuring contracts, pricing, and operational setup.','本人负责部署商业机会、合同、定价和运营设置；不推测客户现场机器人维护。')
add('E0582','V2_PROJECT_METHOD','DUTY_OWN_USE','UNCONDITIONAL','structuring them into executable plans, and driving them to measurable outcomes with minimal founder involvement.','本人把跨职能业务问题转为可执行计划并推动结果。')
register(list(R.values()),'Astra_corporate_fullread_f')
