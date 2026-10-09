from bootstrap import RUN,BASE,sha,REPO
import csv,json
HERE=REPO/'.b5repair'
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def save(n,obj):(HERE/n).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
