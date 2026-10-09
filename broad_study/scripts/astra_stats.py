"""Pure counting functions. Explicit excluded states never enter B or N."""
from statistics import mean

def point(company,total,counts):
 p,u,na,sx=(counts.get(s,0) for s in ['P','U','NA','SOURCE_EXCLUDED'])
 z=total-p-u-na-sx
 assert min(p,u,na,sx,z)>=0,(company,total,counts)
 n=p+z;b=n+u
 return dict(company_id=company,total_ads=total,P=p,U=u,Z=z,NA=na,SOURCE_EXCLUDED=sx,B=b,N=n,
   share=p/n if n else None,small_n='YES' if 0<n<10 else 'NO',
   unknown_low=p/b if b else None,unknown_high=(p+u)/b if b else None)

def aggregate(points):
 a={s:sum(p[s] for p in points) for s in ['total_ads','P','U','Z','NA','SOURCE_EXCLUDED','B','N']}
 pp=[p for p in points if p['N']>0];bp=[p for p in points if p['B']>0]
 a.update(n_companies=len(pp),n_positive_companies=sum(p['P']>0 for p in points),
  gate='EXPLORATORY_SUMMARY' if len(pp)>=3 and a['N']>=20 else 'POINTS_ONLY',
  small_n_companies=sum(p['small_n']=='YES' for p in points))
 eligible=a['gate']=='EXPLORATORY_SUMMARY'
 a['share_ad_weighted']=a['P']/a['N'] if eligible else None
 a['share_company_equal']=mean(p['share'] for p in pp) if eligible else None
 # Sensitivity intervals are scenario bounds, not sampling confidence intervals.
 a['unknown_low_ad']=a['P']/a['B'] if eligible and a['B'] else None
 a['unknown_high_ad']=(a['P']+a['U'])/a['B'] if eligible and a['B'] else None
 a['unknown_low_company']=mean(p['unknown_low'] for p in bp) if eligible and bp else None
 a['unknown_high_company']=mean(p['unknown_high'] for p in bp) if eligible and bp else None
 for s,name in [('P','positive'),('N','denominator')]:
  v=max((p[s] for p in points),default=0)
  a['max_'+name+'_companies']=[p['company_id'] for p in points if p[s]==v] if v else []
  a['max_'+name+'_count']=v
  a['max_'+name+'_contribution']=v/a[s] if a[s] else None
 a['dominance_warning']='YES' if (a['max_positive_contribution'] or 0)>.5 else 'NO'
 return a

def tests():
 # Effective N, excluded records, and zero-denominator company retention.
 p=point('a',13,{'P':2,'U':4,'NA':1,'SOURCE_EXCLUDED':1})
 assert (p['Z'],p['N'],p['B'],p['small_n'])==(5,7,11,'YES')
 z=point('zero',3,{'U':3});assert z['share'] is None and z['N']==0
 # Different weights, exact gate, and all max ties must survive.
 pp=[point('a',10,{'P':2}),point('b',5,{'P':2}),point('c',5,{'P':0}),z]
 a=aggregate(pp)
 assert a['gate']=='EXPLORATORY_SUMMARY' and a['n_companies']==3 and a['N']==20
 assert abs(a['share_company_equal']-.2)<1e-12 and a['share_ad_weighted']==.2
 assert a['max_positive_companies']==['a','b']
 pp=[point('a',20,{'P':10}),point('b',5,{}),point('c',5,{})]
 a=aggregate(pp);assert abs(a['share_company_equal']-1/6)<1e-12 and a['share_ad_weighted']==1/3
 assert aggregate(pp[:2])['gate']=='POINTS_ONLY'
 try:point('bad',1,{'P':2})
 except AssertionError:pass
 else:raise AssertionError('Impossible counts silently clamped')
 return 8

if __name__=='__main__':print('PASS',tests(),'substantive arithmetic checks')
