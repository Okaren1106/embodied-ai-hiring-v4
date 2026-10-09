from pathlib import Path
import subprocess,json,hashlib,datetime,concurrent.futures
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parent/'new_sources'
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ['script','style','noscript']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style','noscript']:self.skip=max(0,self.skip-1)
  if t in ['p','div','h1','h2','h3','li','tr','section','br']:self.parts.append('\n')
 def handle_data(self,d):
  if not self.skip:self.parts.append(d)
def fetch(p):
 j=json.loads(p.read_text(encoding='utf-8'));eid=j['id']
 # Earlier tool calls recorded the collection day; do not invent request timestamps.
 if j.get('retrieved_at')=='2026-09-15T07:28:00Z':
  j['retrieved_at']='2026-09-15';j['retrieval_precision']='DAY';p.write_text(json.dumps(j,ensure_ascii=False,indent=2),encoding='utf-8')
 raw=ROOT/(eid+'.html');started=datetime.datetime.now(datetime.timezone.utc).isoformat()
 proc=subprocess.run(['curl.exe','-L','--connect-timeout','10','--max-time','35','-sS','-o',str(raw),'-w','%{http_code}\n%{url_effective}',j['url']],capture_output=True,text=True,encoding='utf-8',errors='replace')
 lines=proc.stdout.splitlines();code=int(lines[0]) if lines and lines[0].isdigit() else 0
 meta={'id':eid,'url':j['url'],'started_at':started,'exit_code':proc.returncode,'http_code':code,'effective_url':lines[-1] if lines else '', 'stderr':proc.stderr,'raw_bytes':raw.stat().st_size if raw.exists() else 0}
 if raw.exists():
  b=raw.read_bytes();meta['raw_sha256']=hashlib.sha256(b).hexdigest()
  t=Text();t.feed(b.decode('utf-8',errors='replace'));txt='\n'.join(s.strip() for s in ''.join(t.parts).splitlines() if s.strip());(ROOT/(eid+'.raw.txt')).write_text(txt,encoding='utf-8');meta['text_chars']=len(txt)
 (ROOT/(eid+'.fetch.json')).write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
 return {k:meta[k] for k in ['id','http_code','exit_code','raw_bytes','text_chars'] if k in meta}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
  for result in ex.map(fetch,sorted(ROOT.glob('*.web.json'))):print(json.dumps(result),flush=True)
