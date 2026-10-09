"""Stage D publication figures."""
import sys,argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--deps');a=p.parse_args()
if a.deps:sys.path.insert(0,a.deps)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
from analyze import ROOT,T,read,table,dump
font=Path('C:/Windows/Fonts/msyh.ttc')
if font.exists():font_manager.fontManager.addfont(str(font));fontname=font_manager.FontProperties(fname=str(font)).get_name()
else:fontname='DejaVu Sans'
plt.rcParams.update({'font.family':fontname,'font.size':10,'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold','figure.facecolor':'white','savefig.facecolor':'white','svg.hashsalt':'stage-d-v1','svg.fonttype':'path','axes.labelcolor':'#344356','text.color':'#213247','xtick.color':'#344356','ytick.color':'#344356'})
C=ROOT/'charts';C.mkdir(exist_ok=True)
BLUE='#286793';ORANGE='#CD7A2F';GREEN='#3E7A5A';TEAL='#3D6E7A'
short={'CN_GALBOT':'银河通用','US_FIGURE':'Figure','US_AGILITY':'Agility','US_NIMBLE':'Nimble','CN_XSQUARE':'自变量','US_FIELD_AI':'Field AI','US_BOSTON_DYNAMICS':'Boston Dynamics','US_AMAZON_FTR':'FAR团队'}
def cn(c,name):return short.get(c,name)
figs=[]
def save(fig,id,title,caption,rows,source):
 fig.savefig(C/(id+'.png'),dpi=180,bbox_inches='tight');fig.savefig(C/(id+'.svg'),bbox_inches='tight',metadata={'Date':None});plt.close(fig)
 table(id+'_plot_data.csv',rows)
 figs.append(dict(id=id,title=title,caption=caption,png='charts/'+id+'.png',svg='charts/'+id+'.svg',plot_data='tables/'+id+'_plot_data.csv',source_table=source))

head=read(T/'D2_headline_cross_split.csv')
cross=[r for r in read(T/'D2_role_activity_bidirectional.csv') if r['scope']=='ALL24' and r['relation']=='OWNED']
acts=['ACT_RESEARCH','ACT_DEPLOYMENT','ACT_QUALITY']
actn={'ACT_RESEARCH':'研究探索','ACT_DEPLOYMENT':'部署与维护','ACT_QUALITY':'质量验证'}
# top roles by share of each activity
fig,axs=plt.subplots(1,3,figsize=(16,8),sharey=False)
plot_rows=[]
for ax,act in zip(axs,acts):
 rows=[r for r in cross if r['activity_code']==act and r['share_role_given_activity']!='']
 rows.sort(key=lambda r:float(r['share_role_given_activity']),reverse=True)
 rows=rows[:8];rows.reverse()
 yy=np.arange(len(rows))
 cols=[]
 for r in rows:
  k=r['class_kind']
  cols.append(BLUE if k=='concrete' else (ORANGE if k=='structure' else '#8A94A0'))
 ax.barh(yy,[float(r['share_role_given_activity'])*100 for r in rows],color=cols)
 ax.set_yticks(yy,[r['primary_name'] for r in rows],fontsize=9)
 h=next(x for x in head if x['activity_code']==act)
 ax.set_title(f"{actn[act]}\n同名之外 {float(h['share_outside_namesake'])*100:.1f}%  · n={h['n_owned']}",loc='left',fontsize=12)
 ax.set_xlabel('占该活动正向广告（%）');ax.set_xlim(0,55);ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
 for r in rows:
  plot_rows.append(dict(figure='F1',activity=act,primary=r['primary_name'],kind=r['class_kind'],share=r['share_role_given_activity'],n=r['n_activity_in_role']))
fig.suptitle('Q3  本人承担活动落在哪些主职能',x=.02,ha='left',fontsize=16)
fig.text(.02,.02,'颜色：蓝=具体职能，橙=结构类，灰=未明确。同名职能与活动不是同一测量。',fontsize=9)
fig.subplots_adjust(left=.22,right=.98,top=.82,bottom=.1,wspace=.55)
save(fig,'F1_cross_function_activity','跨职能活动分布','本人承担研究/部署/质量活动按主职能拆分。结构类与未明确单列。',plot_rows,'D2_role_activity_bidirectional.csv')

f2_order=['ACT_ENGINEERING','ACT_QUALITY','ACT_DEPLOYMENT','ACT_MANUFACTURING','ACT_RESEARCH']
uw=[r for r in read(T/'D3_unified_weight_cases.csv') if r['group_id']=='CASE_G1_MANUFACTURING_OBSERVED' and r['status']=='RESTRICTED_TO_K' and r['activity_code'] in f2_order]
uw=sorted(uw,key=lambda r:f2_order.index(r['activity_code']))
fig,ax=plt.subplots(figsize=(11,6))
labels=[r['activity_name'] for r in uw];x=np.arange(len(labels));w=.18
own_a=[float(r['own_weight_a'])*100 for r in uw];own_b=[float(r['own_weight_b'])*100 for r in uw]
eq_a=[float(r['equal_weight_a'])*100 for r in uw];eq_b=[float(r['equal_weight_b'])*100 for r in uw]
ax.bar(x-1.5*w,own_a,w,color=BLUE,label='银河通用 · K内自身职能权重')
ax.bar(x-0.5*w,own_b,w,color=ORANGE,label='Figure · K内自身职能权重')
ax.bar(x+0.5*w,eq_a,w,color=BLUE,alpha=.45,label='银河通用 · K内职能等权')
ax.bar(x+1.5*w,eq_b,w,color=ORANGE,alpha=.45,label='Figure · K内职能等权')
ax.set_xticks(x,labels);ax.set_ylabel('K 内活动率（%）');ax.set_ylim(0,70);ax.legend(frameon=False,ncol=2,fontsize=9)
ax.set_title('同职能比较：银河通用与 Figure 的共同职能 K',loc='left',fontsize=15)
ax.text(0,1.02,'K = 公司支持、制造质量供应、ML/AI工程、软件与平台。覆盖约 48%/48% 可判读广告。物流组未达门槛，不在此图。',transform=ax.transAxes,fontsize=9)
ax.grid(axis='y',alpha=.2);ax.set_axisbelow(True)
fig.subplots_adjust(top=.82,bottom=.12)
save(fig,'F2_same_function_galbot_figure','共同职能内活动率','仅共同覆盖且每职能至少10条可判读广告。统一权重不替代全公司结果。',[{'activity':r['activity_name'],'own_galbot':r['own_weight_a'],'own_figure':r['own_weight_b'],'equal_galbot':r['equal_weight_a'],'equal_figure':r['equal_weight_b'],'n_galbot':r['n_a'],'n_figure':r['n_b']} for r in uw],'D3_unified_weight_cases.csv')

dep=read(T/'D3_deployment_composition.csv');t1=read(T.parent.parent/'inputs'/'stage_c'/'tables'/'T1_company_sample.csv') if False else None
t1=read(ROOT/'inputs'/'stage_c'/'tables'/'T1_company_sample.csv');cb={r['company_id']:r for r in t1}
case={'CN_GALBOT','US_FIGURE','US_AGILITY','US_NIMBLE'}
fig,ax=plt.subplots(figsize=(11,8))
for r in dep:
 c=r['company_id']
 x=float(r['share_deployment_function'])*100;y=float(r['share_deployment_activity'])*100
 if r['share_deployment_function']=='' or r['share_deployment_activity']=='':continue
 color=ORANGE if c in case else BLUE
 ax.scatter(x,y,s=70 if c in case else 36,color=color,zorder=3 if c in case else 2)
 ax.annotate(cn(c,r['company_name']),(x,y),textcoords='offset points',xytext=(5,4),fontsize=8 if c in case else 7,color='#213247' if c in case else '#5B6A78')
 ax.plot([0,20],[0,20],color='#D0D5DA',lw=1)
ax.set_xlabel('部署与现场服务主职能占比（活动可判读广告，%）')
ax.set_ylabel('本人承担部署与维护活动率（%）')
ax.set_xlim(-0.5,20);ax.set_ylim(0,60)
ax.set_title('业务责任对照：部署职能构成与部署活动',loc='left',fontsize=15)
ax.text(0,1.02,'橙色为入选案例。对角线表示活动率等于职能占比。点在线上方表示构成不能解释全部活动。',transform=ax.transAxes,fontsize=9)
ax.grid(alpha=.2);ax.set_axisbelow(True)
fig.subplots_adjust(top=.86)
save(fig,'F3_deployment_composition_vs_activity','部署职能与部署活动','FAR 在全24中展示。整公司解释以23家为主。',[{'company_id':r['company_id'],'company_name':r['company_name'],'function_share':r['share_deployment_function'],'activity_share':r['share_deployment_activity'],'outside_function':r['share_deployment_activity_outside_deployment_function'],'case':'YES' if r['company_id'] in case else 'NO'} for r in dep],'D3_deployment_composition.csv')

dump(ROOT/'figure_manifest.json',figs)
dump(ROOT/'verification'/'plot_environment.json',{'matplotlib':matplotlib.__version__,'numpy':np.__version__,'font':fontname,'font_path':str(font),'figures':len(figs),'researcher':'Cursor Grok 4.6'})
print(len(figs))
