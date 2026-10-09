"""Environment, input check receipt, and publish manifest."""
from common import *
from datetime import datetime, timezone
import os,sys,platform,hashlib
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(ROOT).as_posix()
    if rel.startswith('inputs/'): continue  # inputs already in input_manifest
    if '/__pycache__/' in '/'+rel: continue
    files.append(dict(path=rel,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
save_json('publish_manifest.json', dict(created_utc=datetime.now(timezone.utc).isoformat(),n=len(files),files=files))
save_json('verification/environment.json', dict(
    python=sys.executable, version=sys.version, platform=platform.platform(),
    cwd=str(ROOT), input_files=lock_check(),
    note='Cursor session has no Codex quota query tool',
    created_utc=datetime.now(timezone.utc).isoformat()))
print('publish', len(files), 'env ok')
