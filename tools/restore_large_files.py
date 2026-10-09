"""Restore original bytes from the seven losslessly compressed research files."""
from pathlib import Path
import gzip
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(4*1024*1024), b''): h.update(block)
    return h.hexdigest()

def restore():
    rows = json.loads((ROOT/'COMPRESSION_MANIFEST.json').read_text(encoding='utf-8'))
    for row in rows:
        dest = (ROOT/row['path']).resolve()
        assert dest.is_relative_to(ROOT), row['path']
        if dest.exists():
            assert dest.stat().st_size==row['bytes'] and sha(dest)==row['sha256'], 'Existing file differs: '+row['path']
            print('ALREADY VERIFIED', row['path'], flush=True)
            continue
        temporary = dest.with_name(dest.name + '.restoring')
        assert not temporary.exists(), 'A prior partial restore exists: '+str(temporary)
        with gzip.open(ROOT/row['compressed_path'], 'rb') as src, temporary.open('xb') as out:
            shutil.copyfileobj(src, out, 4*1024*1024)
        assert temporary.stat().st_size==row['bytes'] and sha(temporary)==row['sha256'], row['path']
        temporary.rename(dest)
        print('RESTORED AND VERIFIED', row['path'], flush=True)

if __name__ == '__main__': restore()
