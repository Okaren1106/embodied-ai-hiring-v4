from pathlib import Path
import csv,json,hashlib
HERE=Path(__file__).resolve().parent
BASE=HERE.parent.parent.parent
RUN=HERE.parent
def rows(p):return list(csv.DictReader(p.open(encoding="utf-8-sig",newline="")))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,obj):(HERE/n).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")
