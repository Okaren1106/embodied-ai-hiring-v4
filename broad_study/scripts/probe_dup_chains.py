"""Find DUPLICATE actions that do not resolve to a retained list."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
bad = []
for p in sorted((root/'configs/Q_adjudications').glob('*.json')):
    data = json.loads(p.read_text(encoding='utf-8'))
    for store, a in data['ads'].items():
        new = a.get('new') or {}
        for ni, actions in new.items():
            if not isinstance(actions, str) or not actions.startswith('DUPLICATE:'):
                continue
            target = actions.split('DUPLICATE:', 1)[1]
            tni = target.split(':')[-1]
            dest = new.get(tni)
            if not isinstance(dest, list):
                bad.append('%s %s cand%s -> %s dest=%s' % (p.name, store, ni, actions, type(dest).__name__ if dest is not None else 'MISSING'))
out = Path(__file__).resolve().parents[1]/'notes/dup_chain_bad.txt'
out.write_text('\n'.join(bad) if bad else 'NONE', encoding='utf-8')
print('bad', len(bad))
