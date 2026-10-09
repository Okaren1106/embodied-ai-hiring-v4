"""Rewrite DUPLICATE-of-OUTSIDE/REJECT to the same terminal string so materialize can accept them."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
nfix = 0
for p in sorted((root/'configs/Q_adjudications').glob('*.json')):
    data = json.loads(p.read_text(encoding='utf-8'))
    changed = False
    for store, a in data['ads'].items():
        new = a.get('new') or {}
        def resolve(ni, seen=None):
            seen = set() if seen is None else seen
            if ni in seen:
                return None
            seen.add(ni)
            dest = new.get(ni)
            if isinstance(dest, list):
                return dest
            if isinstance(dest, str) and dest.startswith('DUPLICATE:'):
                tni = dest.split('DUPLICATE:', 1)[1].split(':')[-1]
                return resolve(tni, seen)
            return dest
        for ni, actions in list(new.items()):
            if not isinstance(actions, str) or not actions.startswith('DUPLICATE:'):
                continue
            tni = actions.split('DUPLICATE:', 1)[1].split(':')[-1]
            dest = resolve(tni)
            if isinstance(dest, str) and dest.startswith(('REJECT:', 'OUTSIDE:')):
                new[ni] = dest
                nfix += 1
                changed = True
    if changed:
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print('fixed', nfix)
