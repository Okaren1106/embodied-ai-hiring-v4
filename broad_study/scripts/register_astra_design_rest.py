from astra_review_tools import *
ids=['N0327','N0485','N0178','E0149','N0216','E0122','N0275','N0310','N0303','N0719','N0817','N0720','N0704']
R={rid:dict(reading_id=rid,review_mode='FULL_SOURCE_AND_CODING',judgment='',evidence_overrides=[],additions=[]) for rid in ids}
for rid in ['N0478','E0419','N0772']:
 R[rid]=dict(reading_id=rid,review_mode='FOLLOWUP',judgment='按全职能一致规则补查方法漏编与局部分支，不改冻结主分类。',evidence_overrides=[],additions=[])
def ov(rid,eid,reason,**fields):R[rid]['evidence_overrides'].append(dict(evidence_id=eid,reason=reason,**fields))
def add(rid,c,m,b,q,reason):R[rid]['additions'].append(dict(code=c,metric=m,branch=b,quote=q,reason=reason))
for rid,eid in [('N0327','N0327:2:0'),('N0485','N0485:4:0'),('N0178','N0178:2:0'),('E0149','E0149:3:0')]:
 ov(rid,eid,'工业设计学历/专业字段不替代工业外观或CMF方法能力要求。',metric='SEPARATE',branch='EDUCATION_FIELD')
R['N0327']['judgment']='工业外观、CMF实现任务成立；斜线软件关系继续未知，其余等软件与Blender等是示例；学历和经验能力分开。'
for e in EB[RID['N0327']]:
 if e['code'] in ['V2_PHOTOSHOP','V2_KEYSHOT','V2_ILLUSTRATOR','V2_BLENDER']:ov('N0327',e['evidence_id'],'等列举例子，不含明确or。',branch='EXAMPLE')
 if e['code']=='V2_RHINO':ov('N0327',e['evidence_id'],'Rhino反斜线Alias关系未解决。',branch='UNRESOLVED')
R['N0485']['judgment']='本人外观与CMF设计明确；没有具体建模软件不补值。DFM位于加分项，斜线关系未解决；工艺能力及职责分别有明确依据。'
ov('N0485','N0485:5:0','加分项标题支配DFM/DFA；斜线关系未确定。',metric='PREFERRED',branch='UNRESOLVED')
add('N0485','V2_CNC_PROCESS','GENERAL','UNRESOLVED','熟悉塑料/金属成型工艺、表面处理及装配结构','塑料/金属斜线材料对象的分支未解决；保留普通要求。')
add('N0485','V2_CMF_DESIGN','GENERAL','UNCONDITIONAL','熟悉3D建模软件，具备优秀的手绘/数字草图能力','明确外观表现能力；手绘/数字草图仅具体手段未解决，不由此推断具名工具。')
R['N0178']['judgment']='任务为机器人外观/CMF，参与职责与明确能力分开；手段不限且等软件同时保留选择空间和示例；OC/Vray仍目录外。'
ov('N0178','N0178:1:0','此句明确参与CMF设计，未明确本人承担或主导设计交付。',metric='SEPARATE',branch='COLLABORATION_OBJECT')
for e in EB[RID['N0178']]:
 if e['code'] in ['V2_PHOTOSHOP','V2_KEYSHOT','V2_ILLUSTRATOR','SK_NX','SK_SOLIDWORKS']:
  ov('N0178',e['evidence_id'],'手段不限提供替代空间，等列举示例；新旧命名工具采用同一分支。',branch='CHOICE_AND_EXAMPLE')
R['E0149']['judgment']='机器人外观/包覆件/CMF有据；外观方法输出与方法创新分开，供应商打样不当采购谈判；材料工艺要求保留or任选。'
ov('E0149','E0149:2:0','输出CMF方案是运用工业外观方法的交付成果，未明示开发新设计方法体系。',metric='DUTY_OWN_USE')
ov('E0149','E0149:4:0','具体工艺列表有或，保留任选。',branch='CHOICE')
ov('E0149','E0149:5:0','供应商打样没有明示询报价、寻源、商务谈判或供货管理。',metric='SEPARATE',branch='SUPPLIER_COLLABORATION')
add('E0149','V2_CMF_DESIGN','GENERAL','CHOICE','具备消费级硬件、智能硬件、机器人或车载产品外观设计经验','原文外观设计经验明确；物品领域由or连接，保留分支。')
R['N0216']['judgment']='设计工具用于代码落地，但Cursor/Claude Code斜线关系无法直接判任选；对标Linear/Vercel/Notion不是本人使用。补明确体验/交互设计方法。'
for e in EB[RID['N0216']]:ov('N0216',e['evidence_id'],'Claude Code / Cursor等原文未解决斜线关系；收窄证据到实际一般要求句，不能用整篇含多个标题判断分支。',branch='UNRESOLVED',quote='能熟练用 Claude Code / Cursor 等工具把设计落到代码里，独立产出可上线成果')
add('N0216','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','主导产品的交互与界面设计，从需求洞察到设计落地全流程','明确用户体验与交互方法的本人应用。')
add('N0216','V2_UX_RESEARCH','GENERAL','UNCONDITIONAL','交互设计扎实：信息架构、状态、反馈、流程都拿得起','明确交互方法能力，无需关键词user research命中。')
R['E0122']['judgment']='服务体验流程为主任务；销售为协作对象保留。方法要求有后半段独立说明，SOP不只靠斜线；补本人服务方法应用与操作标准制定。'
add('E0122','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','设计全触点体验流程与标准（售前 / 售中 / 售后 / 使用中）','上位全触点体验流程明示，括号细分环节不替代上位本人方法。')
add('E0122','V2_SOP_OPERATION','DUTY_OWN_DEVELOP','UNCONDITIONAL','建立体验巡检体系与”超预期时刻”设计','本人编制可巡检的服务质量体系，后文有可执行标准的完整定义。')
R['N0275']['judgment']='穿戴外观与CMF、用户需求研究明确；工具斜线不推任选，工艺列举为示例能力且本人跟进试制另有工作语境；CERO的既有CREO纠错只保留在原目录别名范围。'
for e in EB[RID['N0275']]:
 if e['code'] in ['V2_PHOTOSHOP','V2_RHINO','V2_KEYSHOT','V2_ILLUSTRATOR','SK_CREO']:ov('N0275',e['evidence_id'],'多个斜线工具组没有明确任选词，统一保留未解决。',branch='UNRESOLVED')
ov('N0275','N0275:3:0','熟悉注塑等工艺是能力陈述；等是示例关系，不能仅因位于职责栏即计工具方法本人使用。',metric='GENERAL',branch='EXAMPLE')
R['N0310']['judgment']='机器人服装款式、制版、面料和成型为实际设计对象；目录容许外观/材料与成型方法，不能只留下工具命中。命名软件为等示例，供应商评估管理符合采购定义。'
for e in EB[RID['N0310']]:
 if e['code'] in ['V2_AUTOCAD','V2_PHOTOSHOP','V2_ILLUSTRATOR']:ov('N0310',e['evidence_id'],'等服装设计软件为示例，没有or。',branch='EXAMPLE')
add('N0310','V2_CMF_DESIGN','DUTY_OWN_USE','UNCONDITIONAL','与设计部门协同完成机器人衣服款式设计与制版','本人共同完成款式与版型交付，不是仅与设计部门沟通。')
add('N0310','V2_CNC_PROCESS','GENERAL','UNCONDITIONAL','熟悉服装成型及三维纺织全链路工艺流程','冻结定义包含明确成型方法，不局限CNC金属加工。')
add('N0310','V2_CNC_PROCESS','DUTY_OWN_USE','UNCONDITIONAL','可以熟练操作各类服装成型设备及工艺，完成试制工作','职责明示操作成型设备完成试制；保留服装工艺具体子型，不和金属加工视为同任务。')
R['N0303']['judgment']='包装外观/结构设计有据；色彩校准不是传感器标定，PS/AI/ID普通并列不是任选。补包装法规与合规实际检查，避免只靠法规缩写匹配。'
for e in EB[RID['N0303']]:
 if e['code'] in ['V2_PHOTOSHOP','V2_ILLUSTRATOR']:ov('N0303',e['evidence_id'],'精通软件冒号后普通并列，无或/等/如。',branch='UNCONDITIONAL')
add('N0303','V2_ENV_COMPLIANCE','DUTY_OWN_USE','UNCONDITIONAL','负责包装合规检查：文案、条码、标准号、生产信息、法规要求、电商平台规范等','本人产品包装合规检查，属于产品法规知识与应用，不评价法律是否现行。')
R['N0719']['judgment']='数字UI/UX任务与用户研究有据；Figma有or，Blender/React经验位于Preferred；React Three Fiber作为已冻结React相关工具提及保留具体对象，不从Three.js补JavaScript。'
ov('N0719','N0719:8:0','Figma or similar design tools明确任选。',branch='CHOICE')
for eid in ['N0719:10:0','N0719:12:0']:ov('N0719',eid,'位于Preferred Qualifications。',metric='PREFERRED')
add('N0719','V2_UX_RESEARCH','GENERAL','UNCONDITIONAL','Strong portfolio demonstrating UI/UX design skills','明确界面及用户体验设计能力要求；不等价于每个用研子方法都必备。')
add('N0719','V2_UX_RESEARCH','PREFERRED','UNCONDITIONAL','Understanding of 3D visualization and interaction patterns','优先段明确交互模式方法知识。')
R['N0817']['judgment']='数字平台体验与设计系统是本人任务；Figma一般要求有据，行业愿景不归本人模型开发。补被无关键词策略漏掉的用户研究、体验路径及设计系统方法。'
add('N0817','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL',"Champion the user through research, feedback, and advocacy — whether they're field operators, site managers, or enterprise decision-makers",'本人通过研究与反馈理解用户，受众是用户而非岗位申请者。')
add('N0817','V2_UX_RESEARCH','GENERAL','UNCONDITIONAL','An understanding of Human-Robot Interaction (HRI)','明示人机交互方法知识，上位理解要求明确，获得经验的路径另列不改此总括。')
add('N0817','V2_UX_RESEARCH','PREFERRED','UNCONDITIONAL','Background in platform-level UX where information architecture, navigation patterns, and scalability are as important as any individual screen','优先段的信息架构与导航体验方法。')
R['N0720']['judgment']='车队交互设计任务成立；告警界面不计本人运行排障，控制界面不推本人控制算法，所有经验条款位于Preferred或Bonus，补实际用户研究方法。'
add('N0720','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','Lead customer interviews, usability studies, and rapidly prototyping.','本人主导访谈和可用性研究。')
add('N0720','V2_UX_RESEARCH','PREFERRED','UNCONDITIONAL','Comfort leading customer research and translating insight into product decisions.','明确优先用户研究能力。')
R['N0704']['judgment']='动画及机器人表达任务有据，Maya/Blender任选保留。动捕的清理编辑与重定向是已采数据处理，不证明亲自穿戴/操作采集；知识条款均在Preferred，控制/动力学/仿真斜线保留未知。'
ov('N0704','N0704:8:0','Preferred段描述已捕获动作数据的清理、编辑与重定向，属于数据处理对象；冻结V2_MOCAP测量本人动作捕捉/示范采集。',metric='SEPARATE',branch='MOCAP_DATA_PROCESSING')
add('N0478','V2_UX_RESEARCH','DUTY_OWN_USE','UNCONDITIONAL','主导人形机器人操控软件的用户体验设计，完成从用户需求分析、信息架构到交互原型、视觉落地的全流程设计','用户体验方法明确，首次抽查未发现此漏项，本轮全职能回查补正。')
add('N0478','V2_UX_RESEARCH','GENERAL','UNCONDITIONAL','至少2-3年UXUI设计经验，独立负责过完整功能模块设计','明示体验/交互设计经验而非相关专业学历。')
# Follow-up additions are addressed by their transaction identifier rather than source eid.
R['E0419']['transaction_overrides']=[dict(target_batch='Astra_design_seeded_fullread',target_addition_index=4,branch='CHOICE',reason='service design, workflow design, or cross-touchpoint experience的局部分支必须保留，不因上位方法类覆盖多个选项而消除or。')]
ov('N0772','N0772:17:0','DFM/DFA斜线关系未明，统一与其他同词使用未解决分支。',branch='UNRESOLVED')
register(list(R.values()),'Astra_design_all23_completed')
