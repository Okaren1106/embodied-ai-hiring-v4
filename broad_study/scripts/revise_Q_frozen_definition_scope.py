"""Targeted frozen-definition audit; explicit researcher corrections, no keyword classification."""
from common import *
from copy import deepcopy
from datetime import datetime,timezone
revision_id='Q-M5-FROZEN-DEFINITION-20260916-08'
hp=ROOT/'notes'/f'{revision_id}.json';assert not hp.exists()
docs={p:json.loads(p.read_text(encoding='utf-8')) for p in sorted((ROOT/'configs/Q_adjudications').glob('*.json'))}
where={rid:p for p,d in docs.items() for rid in d['ads']};ads={rid:d['ads'][rid] for p,d in docs.items() for rid in d['ads']}
changed={}
def edit(rid,reason):
 if rid not in changed:changed[rid]={'before':deepcopy(ads[rid]),'reasons':[]}
 changed[rid]['reasons'].append(reason)
 a=ads[rid];a['updated_utc']=datetime.now(timezone.utc).isoformat();return a
for rid,n,m,b in [('N0465','23','PREFERRED','CHOICE'),('N0644','2','DUTY_OWN_USE','EXAMPLE'),('N0196','4','GENERAL','EXAMPLE'),('N0006','1','DUTY_OWN_USE','EXAMPLE'),('N0017','1','DUTY_OWN_USE','EXAMPLE')]:
 a=edit(rid,'冻结V2_RS485别名明示包含串口；按宽串口组计入，原词不改，不解释为确定RS485协议。')
 assert not any(x[0]=='V2_RS485' for x in a['new'][n])
 a['new'][n].append(['V2_RS485',m,b])
 if rid=='N0196':a['new']['6']='DUPLICATE:N0196:4'
a=edit('N0005','串口/SSH中的泛称串口属于冻结宽串口组，但斜线关系未决。')
a['new']['7']=[['V2_RS485','GENERAL','UNRESOLVED']]
a=edit('N0125','局部RS232/485斜线关系未决，其他逗号分隔协议仍为等示例。')
for x in a['new']['4']:
 if x[0]=='V2_RS485':x[2]='UNRESOLVED'
a=edit('E0182','不同协议由斜线并列，未明示全部或任选；未决优先于等示例。')
for x in a['new']['3']:
 if x[0] in ['V2_CAN','V2_RS485','V2_I2C','V2_SPI','V2_USB']:x[2]='UNRESOLVED'
a=edit('N0124','本广告已因明确485协议有串口组正例；补充说明泛称串口也在冻结别名内，不增加计数。')
for rid in ['N0465','N0644','N0196','N0124','N0006']:
 a=ads[rid]
 for old in ['泛称串口协议不自动映射RS485。','串口泛称不补RS485或UART。','串口不指定RS485。','串口泛称自身不作同义证据。','串口未明RS485不编码。']:
  a['notes']=a['notes'].replace(old,'')
a=edit('N0630','V2_MODEL_COMPRESSION名称含推理优化，但冻结定义限定量化/蒸馏/裁剪/低秩适配；职责只明示时延调优，不能当模型压缩开发。明确模型量化GENERAL保留。')
rm=[x for x in a['additions'] if x['code']=='V2_MODEL_COMPRESSION'];assert len(rm)==1
a['additions']=[x for x in a['additions'] if x['code']!='V2_MODEL_COMPRESSION']
a.setdefault('outside_extra',[]).append(dict(quote=rm[0]['quote'],description='推理调优职责本身没有明示压缩方法，V2_MODEL_COMPRESSION不作职责正例；保留TC_ML_SYSTEMS与工具。'))
a=edit('N0168','冻结V2_TELEOP允许遥操系统开发另判开发关系；明确遥操数采设备硬件架构设计属于开发，不是本人遥操作采集。')
rr=[x for x in a['additions'] if x['code']=='V2_TELEOP'];assert len(rr)==1
rr[0].update(metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',reason='明确遥操数采设备相关硬件架构设计，按冻结定义记录开发；不计本人操作/示教使用。')
a=edit('N0642','供应链导入流程不明示询报价、寻源、谈判或供货管理，删除过宽采购能力推断；质量流程知识另保留。')
rm=[x for x in a['additions'] if x['code']=='V2_PROCUREMENT'];assert len(rm)==1
a['additions']=[x for x in a['additions'] if x['code']!='V2_PROCUREMENT']
a.setdefault('outside_extra',[]).append(dict(quote=rm[0]['quote'],description='供应链导入流程未具体到冻结采购/供货管理方法，不据此补采购能力。'))
for rid,chg in changed.items():
 ads[rid]['notes']+=' 定向定义回查'+revision_id+'：'+'；'.join(chg['reasons'])
 chg['after']=deepcopy(ads[rid])
history=dict(revision_id=revision_id,reviewer='Astra',created_utc=datetime.now(timezone.utc).isoformat(),coded_ads_at_review=len(ads),scope='All currently coded serial-surface candidate decisions; all model-compression and teleoperation candidates/additions; two hardware procurement positives. This is not full second-pass QC.',changed_ads=changed,reviewed_kept={'N0515':'供应商管理能力明确，保留供货管理宽方法GENERAL，不解释为询报价谈判。','N0480':'硬件轻量化排除模型压缩。','N0274_N0263_N0268_E0059_E0025':'量化报告/指标/批量化生产不是模型量化，维持排除。','E0530':'分拣遥操工具包是对象处理，不是本人遥操作或开发，维持背景。'},frozen_catalog_changed=False,original_reference_changed=False)
hp.write_text(json.dumps(history,ensure_ascii=False,indent=2),encoding='utf-8')
for p,d in docs.items():p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print(revision_id,len(changed),'ads with recorded correction/clarification; frozen catalog unchanged')

