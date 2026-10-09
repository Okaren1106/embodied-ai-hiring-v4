from astra_review_tools import *
p=ROOT/'review/astra_reviews.jsonl';tx=transactions();audit=[]
old='熟悉电机、减速器、轴承、编码器、力矩传感器、制动器和嵌入式软件的基本原理及相互影响'
new='熟悉电机、减速器、轴承、编码器、力矩传感器、制动器、驱动控制器和嵌入式软件的基本原理及相互影响'
for t in tx:
 for ch in t.get('evidence_overrides',[]):
  if t['reading_id']=='E0125' and ch.get('quote')==old:
   audit.append(dict(reading_id='E0125',evidence_id=ch['evidence_id'],before=old,after=new,reason='修订事务引文抄写漏驱动控制器，核对源文后修正；不改变判读。'))
   ch['quote']=new
assert len(audit)==2
save_json('review/quote_transcription_corrections.json',audit)
p.write_text(''.join(js(t)+'\n' for t in tx),encoding='utf-8')
