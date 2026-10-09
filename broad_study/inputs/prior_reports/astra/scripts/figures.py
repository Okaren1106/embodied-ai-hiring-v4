import argparse,sys,os
p=argparse.ArgumentParser();p.add_argument('--plot-deps');args=p.parse_args()
if args.plot_deps:sys.path.insert(0,args.plot_deps)
from common import *
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
font=FontProperties(fname=r'C:\Windows\Fonts\msyh.ttc')
plt.rcParams.update({'font.family':font.get_name(),'axes.unicode_minus':False,'font.size':10,'svg.hashsalt':'Astra-stage-D-v1','axes.spines.top':False,'axes.spines.right':False})
BLUE='#285A83';ORANGE='#D17B37';GRAY='#B6BEC5'
(ROOT/'charts').mkdir(exist_ok=True)
def save(fig,name):
 fig.savefig(ROOT/'charts'/f'{name}.png',dpi=180,bbox_inches='tight',facecolor='white',metadata={'Software':'Astra Stage D v1'})
 fig.savefig(ROOT/'charts'/f'{name}.svg',bbox_inches='tight',facecolor='white',metadata={'Date':None,'Creator':'Astra Stage D v1'})
 plt.close(fig)

h=[r for r in read(ROOT/'tables/H1_cross_function_sensitivity.csv') if r['scope']=='WHOLE23' and r['denominator']=='ALL_ACTIVITY_POSITIVE']
h=sorted(h,key=lambda r:['ACT_RESEARCH','ACT_DEPLOYMENT','ACT_QUALITY'].index(r['activity']))
fig,ax=plt.subplots(figsize=(9,3.1));left=np.zeros(3)
for field,label,color in [('dedicated','对应专门职能',GRAY),('other_concrete','其他具体职能',BLUE),('structural','复合/任选结构',ORANGE),('unclear_primary','主职能不明','#757575')]:
 vals=np.array([int(r[field])/int(r['N'])*100 for r in h]);ax.barh(range(3),vals,left=left,label=label,color=color,height=.55)
 for i,(v,l) in enumerate(zip(vals,left)):
  if v>8:ax.text(l+v/2,i,f'{int(h[i][field])}',ha='center',va='center',color='white' if field=='other_concrete' else '#111')
 left+=vals
ax.set_yticks(range(3),[f'{AN[r["activity"]]}（{r["N"]}条）' for r in h]);ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xlabel('该活动本人承担广告的主职能构成（%）');ax.legend(ncol=2,loc='upper center',bbox_to_anchor=(.5,-.28),frameon=False)
fig.tight_layout();save(fig,'F1_activity_roles');dump('F1_chart_data.csv',h)

stand=read(ROOT/'tables/case_standardization_sensitivity.csv');points=read(ROOT/'tables/case_activity_sensitivity.csv')
fig,axs=plt.subplots(1,2,figsize=(9,3.3),sharey=True);chart=[]
for ax,a,title in zip(axs,['ACT_ENGINEERING','ACT_DEPLOYMENT'],['工程实现','现场部署/运行维护']):
 rows=[r for r in stand if r['case_id']=='CASE1' and r['scope']=='MAIN' and r['activity']==a]
 ss={r['weight']:r for r in rows}
 # All-company points calculated from the frozen activity denominator.
 rates=[]
 for c in ['CN_AGIBOT','CN_GALBOT']:
  ii=ids([c],True);rates.append(len(ii&OWN[a])/len(ii))
 values=[rates]+[[float(ss[w]['rate1']),float(ss[w]['rate2'])] for w in ['OWN_K','EQUAL_K','POOLED_K']]
 for j,(c,label,color) in enumerate([('CN_AGIBOT','智元',BLUE),('CN_GALBOT','银河通用',ORANGE)]):
  vv=[v[j]*100 for v in values];bars=ax.bar(np.arange(4)+(-.18 if j==0 else .18),vv,width=.34,label=label,color=color)
  for bar,v in zip(bars,vv):ax.text(bar.get_x()+bar.get_width()/2,v+1,f'{v:.1f}',ha='center',fontsize=8)
  chart += [{'activity':a,'company':c,'variant':v,'rate':x/100} for v,x in zip(['ALL_ACTIVITY_ELIGIBLE','OWN_K','EQUAL_K','POOLED_K'],vv)]
 ax.set_title(title);ax.set_xticks(range(4),['全公司\n可读广告','同K\n自有权重','同K\n等权','同K\n合并权重']);ax.set_ylim(0,76);ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
axs[0].set_ylabel('本人承担活动占比（%）');axs[1].legend(frameon=False,loc='upper right');fig.tight_layout();save(fig,'F2_case1_weights');dump('F2_chart_data.csv',chart)

q=[r for r in read(ROOT/'tables/case_Q2_audience_template_unknown.csv') if r['scope']=='MAIN']
items=[('TC_ML_SYSTEMS','训练/推理系统开发','DUTY_OWN_DEVELOP'),('TC_FOUNDATION_MODEL','基础模型开发','DUTY_OWN_DEVELOP'),('TC_DATA_PIPELINE','数据管线开发','DUTY_OWN_DEVELOP'),('SK_PYTHON','Python一般要求','GENERAL'),('SK_PYTORCH','PyTorch一般要求','GENERAL')]
fig,ax=plt.subplots(figsize=(9,4.1));chart=[]
for j,(c,label,color) in enumerate([('CN_AGIBOT','智元 ML（B=12）',BLUE),('CN_GALBOT','银河通用 ML（B=24）',ORANGE)]):
 for i,(code,name,metric) in enumerate(items):
  r=next(r for r in q if r['company_id']==c and r['role_code']=='RF_ML_AI_ENGINEERING' and r['label_code']==code and r['metric_bucket']==metric and r['branch_bucket']=='UNCONDITIONAL')
  p,n,b,u=[int(r[k]) for k in ['P','N','B','U']];v=p/n*100;lo=p/b*100;hi=(p+u)/b*100;y=i+(-.14 if j==0 else .14)
  ax.plot([lo,hi],[y,y],color=color,lw=3,alpha=.6);ax.scatter(v,y,color=color,s=35,label=label if i==0 else None,zorder=3)
  ax.text(102,y,f'{p}/{n}；U={u}',va='center',fontsize=9,color=color)
  chart.append({'company':c,'label':code,'context':metric,'P':p,'N':n,'B':b,'U':u,'rate':p/n,'low':lo/100,'high':hi/100})
ax.set_yticks(range(5),[x[1] for x in items]);ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xticks([0,25,50,75,100]);ax.set_xlabel('点：P/N；线：未知全负至全正的 P/B—(P+U)/B（%），非置信区间');ax.grid(axis='x',alpha=.2);ax.legend(loc='upper center',bbox_to_anchor=(.5,-.23),frameon=False,ncol=2);ax.text(102,-.6,'P/N；未知数',fontsize=9);fig.tight_layout();save(fig,'F3_case1_q2');dump('F3_chart_data.csv',chart)

# Categorical responsibility summary: states are not a maturity score.
labels=[['公司参与','双方共担','双方共担','客户主责','双方参与*'],['公司研发','未知','实际使用\n执行者未知','实际使用\n责任未知','未来计划'],['公司研发','未知','所选自有中心\n不适用','公司提供\n履单服务','未知'],['公司研发','联合项目\n计划','合资公司参与\n现场验证','验证以外未知','未知']]
states=[[2,2,2,2,2],[2,0,0,0,1],[2,0,3,2,0],[2,1,2,0,0]]
colors={0:'#E5E8EB',1:'#F2DBC5',2:'#C5D9E8',3:'#F6F6F6'}
fig,ax=plt.subplots(figsize=(9,3.4));ax.set_xlim(0,5);ax.set_ylim(0,4)
for i in range(4):
 for j in range(5):
  ax.add_patch(plt.Rectangle((j,3-i),1,1,facecolor=colors[states[i][j]],edgecolor='white',lw=2));ax.text(j+.5,3.5-i,labels[i][j],ha='center',va='center',fontsize=9)
ax.set_xticks(np.arange(5)+.5,['开发','集成','客户现场部署','持续运行','维护支持']);ax.xaxis.tick_top();ax.set_yticks(np.arange(4)+.5,['Dexterity','Nimble','银河通用','智元']);ax.tick_params(length=0);[s.set_visible(False) for s in ax.spines.values()]
fig.text(.13,.01,'蓝：有主体分工证据；橙：计划；灰：责任未知。*联合维护体系不等于合同责任已明确。',fontsize=9);fig.tight_layout(rect=(0,.05,1,1));save(fig,'F4_responsibility')
dump('F4_chart_data.csv',[{'company':c,'stage':stage,'summary':labels[i][j],'category':states[i][j],'source':'T5_responsibility_long.csv'} for i,c in enumerate(['CN_AGIBOT','CN_GALBOT','US_NIMBLE','US_DEXTERITY']) for j,stage in enumerate(['开发','集成','客户现场部署','持续运行','维护支持'])])
print('four figures, PNG and SVG, with source tables')
