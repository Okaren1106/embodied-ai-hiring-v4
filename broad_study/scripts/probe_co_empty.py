from common import RAW, jobs
ids = ['E0470','E0469','E0473','E0314','E0532','E0531','E0474']
jsby = {j['reading_id']: j for j in jobs}
lines = []
for rid in ids:
    j = jsby[rid]
    k = j['identity_key']
    r = RAW[k]
    text = '\n---DUTY---\n' + (r.get('duties') or '') + '\n---REQ---\n' + (r.get('requirements') or '') + '\n---FULL---\n' + (r.get('full_description') or '')
    open('../notes/probe_%s.txt' % rid, 'w', encoding='utf-8').write(text)
    lines.append('%s duty=%s req=%s full=%s' % (rid, len(r.get('duties') or ''), len(r.get('requirements') or ''), len(r.get('full_description') or '')))
    for needle in ['segurança','seguridad','Excel','Google Sheets','NR-','CIPA','HSE','EHS','SST','trabalho','laboral']:
        low = text.lower(); nlow = needle.lower(); start = 0; seen = 0
        while nlow in low[start:] and seen < 3:
            i = low.index(nlow, start); seen += 1
            lines.append('  %s @%s %s' % (needle, i, text[max(0,i-90):i+140].replace('\n',' ')))
            start = i + len(needle)
open('../notes/probe_co_empty_hits.txt','w',encoding='utf-8').write('\n'.join(lines))
print('wrote hits', len(lines))
