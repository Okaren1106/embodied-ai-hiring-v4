from common import *
import unicodedata
def norm(s):
 return ''.join(c for c in unicodedata.normalize('NFKC',s) if not c.isspace() and unicodedata.category(c)[0] not in ('P','Z'))
pilot=read(ROOT/'tables/Q_calibration_sample.csv');seen={};out=[];ledger=[]
for r in pilot:
 k=r['identity_key'];z=RAW[k];known=norm((z.get('duties') or '')+(z.get('requirements') or ''))
 extras=[];dups=[]
 for line in (z.get('full_description') or '').splitlines():
  t=norm(line)
  if not t or t in known:continue
  if t in seen:dups.append(seen[t]);continue
  seen[t]=r['reading_id'];extras.append(line)
 ledger.append(dict(identity_key=k,reading_id=r['reading_id'],new_lines=len(extras),repeated_refs=js(sorted(set(dups)))))
 if extras:out.append(dict(reading_id=r['reading_id'],title=r['title'],lines=extras))
save_json('notes/Q_pilot_full_description_new.json',out)
dump('notes/Q_pilot_full_description_audit.csv',ledger)
print('new ads',len(out),'chars',sum(len('\n'.join(r['lines'])) for r in out))

