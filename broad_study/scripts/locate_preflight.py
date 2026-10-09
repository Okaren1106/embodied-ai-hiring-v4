"""Locate task_evidence quotes for a register_* module."""
import importlib.util, sys
from pathlib import Path
from common import locate, jobs
jbyk = {j['identity_key']: j for j in jobs}
jsby = {j['reading_id']: j for j in jobs}
src = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location('reg', src)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
bad = []
for key, d in mod.decisions.items():
    j = jbyk.get(key) or jsby[key]
    loc = locate(j['identity_key'], dict(quote=d['task_evidence']))
    if loc['method'] == 'UNRESOLVED_LOCATION':
        bad.append(key + ' | ' + d['task_evidence'][:100])
        print('FAIL', key, d['task_evidence'][:100].encode('utf-8','replace').decode('ascii','replace'))
    else:
        print('OK', key, loc['method'], loc['field'])
    for oid, ov in (d.get('old_overrides') or {}).items():
        q = ov.get('quote') or ''
        ol = locate(j['identity_key'], dict(quote=q))
        if ol['method'] == 'UNRESOLVED_LOCATION':
            bad.append(key + ' ' + oid + ' | ' + q[:100])
            print('FAIL OV', key, oid, q[:100])
        else:
            print('OK OV', key, oid, ol['method'])
print('BAD', len(bad))
for b in bad:
    print(b)
