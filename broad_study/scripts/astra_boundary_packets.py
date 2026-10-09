"""Display cited clauses, adjacent context and headings. Never auto-accept a record.

These packets support BOUNDARY_CONTEXTS only. Omitted lines are disclosed; use the
full compact reader if a task, absence, scope or paragraph cannot be settled.
"""
from astra_review_tools import *
import re

HEAD=re.compile(r'职责|任职|资格|要求|加分|条件|必需|必须|必备|我们能提供|Qualifications|Requirements|Responsibilities|Skills|What You|What you|About You|About you|You bring|Nice to have|Bonus|Preferred|Required|Extras|Sets? You Apart|You Will|you will|You’ll|You.ll|In This Role|我们希望|你将获得|Benefits|福利|Compensation',re.I)

def pending(role=''):
 done={t['identity_key'] for t in transactions() if t['review_mode'] in ['FULL_SOURCE_AND_CODING','BOUNDARY_CONTEXTS']}
 return [k for k in MAND if k not in done and (not role or AD[k]['role']==role)]

def boundary(keys):
 out=[]
 for k in keys:
  # Compact is a presentation of all original lines; we then select all evidence
  # and candidate source lines and their neighboring lines, not search results.
  lines=compact_packet([k]).splitlines(); source={}; evidence=[]
  for line in lines:
   m=re.match(r'^([FDR]\d+) ',line)
   if m:source[m.group(1)]=line
   elif line.startswith(('EV ','CAND ')):evidence.append(line)
  wanted=set()
  for line in evidence:
   if ' @' in line:wanted.update(re.findall(r'[FDR]\d+',line.split(' @',1)[1]))
  for key,line in source.items():
   if int(key[1:])<=3 or (len(line)<=100 and HEAD.search(line)):wanted.add(key)
  selected=set(wanted)
  for key in wanted:
   for dn in [-1,1]:
    other=key[0]+str(int(key[1:])+dn)
    if other in source:selected.add(other)
  out += [line for line in lines if line.startswith(('## ','TASK ','REVIEW '))]
  out.append('SCOPE BOUNDARY_CONTEXTS: all coded/candidate clauses + adjacent lines + visible headings; omitted lines are not certified read.')
  skip=[]
  for key,line in source.items():
   if key in selected:
    if skip:out.append('[未在本包显示 '+','.join(skip)+']');skip=[]
    out.append(line)
   else:skip.append(key)
  if skip:out.append('[未在本包显示 '+','.join(skip)+']')
  out.extend(evidence)
  out.extend('OLD_NOTES '+line[6:] for line in lines if line.startswith('NOTES '))
  txs=[t for t in transactions() if t['identity_key']==k]
  if txs:
   # Do not let baseline evidence hide earlier corrections.
   out.append('PRIOR_TRANSACTIONS '+js(txs))
 return '\n'.join(out)

if __name__=='__main__':
 if sys.argv[1]=='next':
  print(js([dict(reading_id=AD[k]['reading_id'],role=AD[k]['role'],title=J[k]['title'],reasons=MAND[k]['reasons']) for k in pending(sys.argv[2] if len(sys.argv)>2 else '')]))
 else:
  ids=sys.argv[1:]; result=boundary([RID[r] for r in ids]);(ROOT/'review'/('boundary_'+'_'.join(ids)+'.md')).write_text(result,encoding='utf-8');print(result)
