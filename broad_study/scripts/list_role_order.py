from common import *
from collections import OrderedDict
frame=read(ROOT/'tables/Q3_coding_frame.csv')
rows=[]
for r in frame:
    key=(int(r['role_order']), r['role'])
    rows.append(key)
seen=OrderedDict()
for o,role in rows:
    seen.setdefault((o,role),0)
    seen[(o,role)]+=1
for (o,role),n in seen.items():
    print(f'{o:02d} {role} {n}')
print('total',len(frame))
