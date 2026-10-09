from astra_review_tools import *
done={r['identity_key'] for r in transactions() if r['review_mode']=='FULL_SOURCE_AND_CODING'}
records=[]; out=[]
for k in sorted(done,key=lambda k:AD[k]['reading_id']):
 rid=AD[k]['reading_id'];seen_groups=set()
 for field in ['full_description','duties','requirements']:
  lines=(RAW[k].get(field) or '').splitlines();occ=defaultdict(list)
  for n,line in enumerate(lines):
   if len(line.strip())>12:occ[line].append(n)
  for line,ns in occ.items():
   if len(ns)<2 or line in seen_groups:continue
   seen_groups.add(line)
   contexts=['\n'.join(f'{i+1} {lines[i]}' for i in range(max(0,n-2),min(len(lines),n+2))) for n in ns]
   records.append(dict(reading_id=rid,field=field,line=line,occurrences=[n+1 for n in ns],contexts=contexts))
   out += [f'## {rid} {field} lines {[n+1 for n in ns]}',*contexts]
save_json('verification/V3_repeated_source_contexts.json',records)
(ROOT/'review/repeated_source_contexts.md').write_text('\n\n'.join(out),encoding='utf-8')
print(js(dict(groups=len(records),ads=len({r['reading_id'] for r in records}),file=str(ROOT/'review/repeated_source_contexts.md'))))
print('\n\n'.join(out))
