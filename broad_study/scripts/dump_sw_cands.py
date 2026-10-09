from pathlib import Path
import json
notes = Path(__file__).resolve().parents[1] / 'notes'
out = []
for name in ['Q_sum_04_145_160.json', 'Q_sum_04_161_176.json', 'Q_sum_04_177_181.json']:
    data = json.loads((notes / name).read_text(encoding='utf-8'))
    for ad in data:
        out.append('==== %s %s nC=%s nI=%s empty=%s' % (
            ad['order'], ad['rid'], len(ad['cands']), ad.get('n_inherited'), ad.get('empty')))
        out.append('TITLE ' + ad['title'])
        for c in ad['cands']:
            codes = ','.join(c.get('codes') or ['-'])
            q = (c.get('quote') or '').replace('\n', ' ')[:160]
            out.append('%s %s | %s' % (c['id'], codes, q))
        out.append('')
p = notes / 'sw_145_181_cands.txt'
p.write_text('\n'.join(out), encoding='utf-8')
print('wrote', p, 'ads', sum(1 for x in out if x.startswith('====')), 'lines', len(out))
