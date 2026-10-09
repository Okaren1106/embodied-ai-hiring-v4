"""Verify the files identified by the non-self-referential public manifest."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(4*1024*1024),b''):h.update(block)
    return h.hexdigest()
manifest=json.loads((ROOT/'PUBLICATION_MANIFEST.json').read_text(encoding='utf-8'))
failures=[]
for row in manifest['files']:
    path=ROOT/row['path']
    if not path.is_file() or path.stat().st_size!=row['bytes'] or digest(path)!=row['sha256']:
        failures.append(row['path'])
print(json.dumps({'status':'PASS' if not failures else 'FAIL','files':len(manifest['files']),'failures':failures},ensure_ascii=False))
assert not failures
