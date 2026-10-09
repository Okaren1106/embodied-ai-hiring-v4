"""Deterministic publication figures from Stage C result tables."""
import sys,argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--deps');a=p.parse_args()
if a.deps:sys.path.insert(0,a.deps)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager,colors
import numpy as np
from analyze import ROOT,R,T,read,table,dump
font=Path('C:/Windows/Fonts/msyh.ttc')
if font.exists():font_manager.fontManager.addfont(str(font));fontname=font_manager.FontProperties(fname=str(font)).get_name()
else:fontname='DejaVu Sans'
plt.rcParams.update({'font.family':fontname,'font.size':10,'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,'axes.titleweight':'bold','figure.facecolor':'white','savefig.facecolor':'white','svg.hashsalt':'stage-c-v1','svg.fonttype':'path','axes.labelcolor':'#344356','text.color':'#213247','xtick.color':'#344356','ytick.color':'#344356'})
C=ROOT/'charts';C.mkdir(exist_ok=True)
BLUE='#286793';ORANGE='#CD7A2F';BG='#F3F6F8'
cs=read(T/'T1_company_sample.csv');cb={r['company_id']:r for r in cs};order=list(cb)
short={'CN_AGIBOT':'智元','CN_ASTRIBOT':'星尘智能','CN_DEEPROBOTICS':'云深处','CN_FOURIER':'傅利叶','CN_GALAXEA':'星海图','CN_GALBOT':'银河通用','CN_LIMX':'逐际动力','CN_NOETIX':'松延动力','CN_PAXINI':'帕西尼','CN_SPIRITAI':'千寻智能','CN_UNITREE':'宇树','CN_XSQUARE':'自变量','US_AMAZON_FTR':'Amazon FAR（团队）','US_PHYSICAL_INTELLIGENCE':'Physical Intelligence','US_BOSTON_DYNAMICS':'Boston Dynamics','US_FIELD_AI':'Field AI'}
def cn(c):return short.get(c,cb[c]['company_name'])
figs=[]
def save(fig,id,title,caption,rows,source):
 fig.savefig(C/(id+'.png'),dpi=180,bbox_inches='tight');fig.savefig(C/(id+'.svg'),bbox_inches='tight',metadata={'Date':None});plt.close(fig)
 table(id+'_plot_data.csv',rows)
 figs.append(dict(id=id,title=title,caption=caption,png='charts/'+id+'.png',svg='charts/'+id+'.svg',plot_data='tables/'+id+'_plot_data.csv',source_table=source))
def heat(ax,data,xlabels,ylabels,vmax,annot=None,fs=8):
 im=ax.imshow(np.ma.masked_invalid(data),aspect='auto',cmap='Blues',vmin=0,vmax=vmax)
 ax.set_xticks(range(len(xlabels)),xlabels,rotation=45,ha='right',fontsize=fs+1);ax.set_yticks(range(len(ylabels)),ylabels,fontsize=fs+1)
 ax.tick_params(length=0);ax.set_xticks(np.arange(-.5,len(xlabels),1),minor=True);ax.set_yticks(np.arange(-.5,len(ylabels),1),minor=True);ax.grid(which='minor',color='white',linewidth=1);ax.tick_params(which='minor',bottom=False,left=False)
 for i in range(len(ylabels)):
  for j in range(len(xlabels)):
   v=data[i,j];tx='NA' if np.isnan(v) else annot[i][j] if annot else f'{v:.0f}'
   ax.text(j,i,tx,ha='center',va='center',fontsize=fs,color='white' if not np.isnan(v) and v>vmax*.58 else '#263B4D')
 return im
q=read(T/'T2_company_primary_roles.csv');codes=list(dict.fromkeys(r['class_code'] for r in q));names={r['class_code']:r['class_name'] for r in q}
names.update({'RF_SIMULATION_EVALUATION':'仿真/评测/测量工具链','RF_SYSTEMS_ENGINEERING_INTEGRATION':'系统工程与集成','RF_ALTERNATIVE_DIRECTIONS':'多方向招聘（任选）'})
lookup={(r['company_id'],r['class_code']):r for r in q}
data=np.array([[float(lookup[c,k]['share_all'])*100 for k in codes] for c in order]);anno=[[lookup[c,k]['n_ads'] if lookup[c,k]['n_ads']!='0' else '·' for k in codes] for c in order]
fig,ax=plt.subplots(figsize=(19,11));im=heat(ax,data,[names[k] for k in codes],[f'{cn(c)}  n={cb[c]["n_ads"]}' for c in order],50,anno,7)
ax.axvline(16.5,color=ORANGE,lw=1.5);ax.axvline(18.5,color=ORANGE,lw=1.5)
fig.suptitle('Q1  24 家公司的公开招聘职能组合',x=.02,ha='left',fontsize=17)
ax.set_title('格内为广告数；颜色为公司内占比（%），超过 50% 使用最深色。每行全部 22 类合计 100%。',loc='left',fontsize=10,pad=16)
fig.colorbar(im,ax=ax,shrink=.55,pad=.02,label='公司内占比（%）',extend='max');fig.subplots_adjust(left=.20,bottom=.22,top=.9)
save(fig,'F1_q1_company_roles','公司主职能构成','全部 1,654 条认可广告。每条仅归入一个主类或未明确状态；FAR 保留团队标记。零值用点表示，来源不足仍在分母。',q,'T2_company_primary_roles.csv')
rows=[r for r in read(T/'T2_aggregates.csv') if r['scope']=='WHOLE23' and r['denominator_basis']=='ALL'];rows.sort(key=lambda r:-float(r['share_company_equal']))
fig,ax=plt.subplots(figsize=(11,10));yy=np.arange(len(rows));eq=np.array([float(r['share_company_equal'])*100 for r in rows]);aw=np.array([float(r['share_ad_weighted'])*100 for r in rows]);ax.hlines(yy,np.minimum(eq,aw),np.maximum(eq,aw),color='#B8C5CF',lw=2);ax.scatter(eq,yy,color=BLUE,label='公司等权',s=42);ax.scatter(aw,yy,color=ORANGE,marker='s',label='广告加权',s=28)
for i,r in enumerate(rows):ax.text(14.4,i,f'{eq[i]:.1f} / {aw[i]:.1f}',va='center',fontsize=9)
ax.set_yticks(yy,[names[r['class_code']] for r in rows]);ax.invert_yaxis();ax.set_xlim(0,17);ax.set_xlabel('占比（%）');ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True);ax.legend(loc='upper center',bbox_to_anchor=(.55,-.08),ncol=2);ax.set_title('Q1  公司等权与广告加权',loc='left',pad=30,fontsize=16);ax.text(0,1.015,'23 家整公司范围，1,630 条广告。右侧为等权 / 加权百分比。',transform=ax.transAxes,fontsize=10)
fig.subplots_adjust(left=.31,top=.89,bottom=.08)
save(fig,'F2_q1_weighting','主职能的两种权重','公司等权先计算各公司比例后平均；广告加权合并广告计数。FAR 的 24 条退出整公司平均，全部 24 个主体结果另存 T2。',rows,'T2_aggregates.csv')
ag=read(T/'T3_aggregates.csv');sel=read(R/'q2_display_selection.csv')
metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED'];ml={'DUTY_OWN_USE':'职责中使用','DUTY_OWN_DEVELOP':'职责中开发','REQUIRED':'硬性要求','GENERAL':'一般要求','PREFERRED':'优先要求'};branches=['UNCONDITIONAL','CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE'];bl={'UNCONDITIONAL':'独立','CHOICE':'任选','EXAMPLE':'示例','CHOICE_AND_EXAMPLE':'任选且示例'}
role_names={'RF_ML_AI_ENGINEERING':'ML/AI 工程','RF_ROBOTICS_SOFTWARE':'软件与平台'}
for role in role_names:
 for dim in ['skills','technical_concepts']:
  labels=[r for r in sel if r['role_code']==role and r['dimension']==dim and r['main_display']=='YES'];labels.sort(key=lambda r:int(r['eligible_rank']))
  rr=[r for r in ag if r['group']=='WHOLE23' and r['role_code']==role and r['dimension']==dim and r['main_display']=='YES'];lk={(r['label_code'],r['metric_bucket'],r['branch_bucket']):r for r in rr}
  fig,axs=plt.subplots(1,2,figsize=(18,max(7,len(labels)*.57+2.3)),gridspec_kw={'width_ratios':[5,9]})
  for ax,slices in zip(axs,[[(m,'UNCONDITIONAL') for m in metrics],[(m,b) for m in metrics[2:] for b in branches[1:]]]):
   dat=np.array([[float(lk[r['label_code'],m,b]['share_ad_weighted'])*100 if lk[r['label_code'],m,b]['share_ad_weighted']!='' else np.nan for m,b in slices] for r in labels]);an=[[f"{lk[r['label_code'],m,b]['n_positive']}/{lk[r['label_code'],m,b]['n_interpretable']}" for m,b in slices] for r in labels]
   heat(ax,dat,[ml[m]+'\n'+bl[b] for m,b in slices],[r['label_name'] for r in labels],60,an,8)
  axs[0].set_title('独立条目：本人承担与要求强度',fontsize=12,pad=16);axs[1].set_title('要求中的条件分支：每一格保留原关系',fontsize=12,pad=16)
  fig.suptitle(f'Q2  {role_names[role]}的'+('具体技能' if dim=='skills' else '技术概念'),x=.03,ha='left',fontsize=17)
  fig.text(.03,.905,'格内为正向广告数 / 本格可解释广告数。颜色为广告加权占比（0—60%，超过 60% 使用最深色）。',fontsize=10)
  fig.text(.03,.035,'基础范围为整公司该职能广告；关系未知只退出受影响的格。格与格可重叠，禁止相加为总需求。完整公司等权、分母及小样本标记见 T3。',fontsize=10)
  fig.subplots_adjust(left=.1,right=.98,top=.81,bottom=.24,wspace=.36)
  ident=('F3_q2_ml_skills' if role=='RF_ML_AI_ENGINEERING' else 'F4_q2_software_skills') if dim=='skills' else ('A1_q2_ml_technical' if role=='RF_ML_AI_ENGINEERING' else 'A2_q2_software_technical')
  save(fig,ident,role_names[role]+('技能语境' if dim=='skills' else '技术语境'),'按已固定总体覆盖排序选择标签。硬性、一般、优先与任选、示例互相区分。背景、否定、未解决提及另存附表，零格仅表示未记录到该正向语境。',rr,'T3_aggregates.csv')
aq=read(T/'T4_activity_company.csv');al=list(dict.fromkeys(r['label_code'] for r in aq));an={r['label_code']:r['label_name'] for r in aq}
lk={(r['company_id'],r['label_code'],r['relation']):r for r in aq};fig,axs=plt.subplots(1,2,figsize=(17,12),sharey=True)
for ax,rel,title in zip(axs,['OWNED','PARTICIPATES'],['本人承担','参与协作']):
 dat=np.array([[float(lk[c,k,rel]['share'])*100 for k in al] for c in order]);im=heat(ax,dat,[an[k] for k in al],[f'{cn(c)}  n={lk[c,al[0],rel]["n_assessable"]}' for c in order],100,fs=8);ax.set_title(title,fontsize=13,pad=14)
axs[1].tick_params(axis='y',labelleft=False);fig.suptitle('Q3  8 类工作活动的公司分布',x=.02,ha='left',fontsize=17);fig.text(.02,.918,'格内为可判读广告中的占比（%），左右同一色标 0—100%。活动可重叠。',fontsize=10);fig.subplots_adjust(left=.22,right=.98,bottom=.2,top=.88,wspace=.08)
save(fig,'F5_q3_activity_company','公司工作活动分布','活动维度可判读 1,623 条，来源不足 31 条退出。NOT_MENTIONED 的 5 条保留。左右关系不能直接相加；并集另存 T4。',aq,'T4_activity_company.csv')
st=read(T/'T4_role_structure_company.csv');fig,axs=plt.subplots(1,2,figsize=(15,10),gridspec_kw={'width_ratios':[1.35,1]});ax=axs[0];yy=np.arange(len(st));co=[int(r['n_compound']) for r in st];alt=[int(r['n_alternative']) for r in st];ax.barh(yy-.18,co,.34,color=BLUE,label='复合承担（19 条）');ax.barh(yy+.18,alt,.34,color=ORANGE,label='多方向任选（11 条）')
for i in yy:
 if co[i]:ax.text(co[i]+.08,i-.18,str(co[i]),va='center',fontsize=9)
 if alt[i]:ax.text(alt[i]+.08,i+.18,str(alt[i]),va='center',fontsize=9)
ax.set_yticks(yy,[f'{cn(r["company_id"])}  n={r["n_all_ads"]}' for r in st],fontsize=9);ax.invert_yaxis();ax.set_xlabel('结构广告数（条）');ax.set_xticks(range(0,max(co+alt)+2));ax.legend(loc='lower right');ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
ax=axs[1];ax.axis('off');ax.text(.02,.93,'30 条广告仍然只计 30 条',fontsize=15,weight='bold',va='top');ax.text(.02,.85,'19 条复合承担：A × B\n11 条多方向任选：A 或 B\n其中 1 条包含嵌套组合。',fontsize=13,linespacing=2,va='top')
ax.text(.02,.64,'智元 N0396 的原有结构',fontsize=13,weight='bold',va='top');ax.text(.02,.56,'“可选择以下一个或多个方向深入参与”\n\n方向 1 或 方向 2 或 方向 3 或\n（模型推理 × 自动化评测）或 方向 5',fontsize=11,linespacing=1.8,va='top',bbox=dict(boxstyle='round,pad=1',facecolor=BG,edgecolor='#DEE6EB'))
ax.text(.02,.29,'保留 30 棵原树与 87 个职能节点。\n节点是组成或招聘分支的提及，\n不能加总为人数，也不进入 Q2 主类分母。',fontsize=11,linespacing=1.8,va='top')
fig.suptitle('Q3  复合职能与多方向招聘',x=.02,ha='left',fontsize=17);fig.subplots_adjust(left=.21,right=.98,top=.92,bottom=.08,wspace=.22)
save(fig,'F6_q3_role_structures','职责组合与任选方向','全部 1,654 条中，结构类 30 条（1.81%）。图中 n 为公司全部广告数，横轴为结构广告计数；零条不证明公司没有复合分工。',st,'T4_role_structure_company.csv')
# Companion company-level skill view: one explicit metric, all 24 entities, per-cell denominator.
qc=read(T/'T3_company_context.csv')
for role,ident in [('RF_ML_AI_ENGINEERING','A3_q2_ml_company_general'),('RF_ROBOTICS_SOFTWARE','A4_q2_software_company_general')]:
 labels=[r for r in sel if r['role_code']==role and r['dimension']=='skills' and r['main_display']=='YES'];labels.sort(key=lambda r:int(r['eligible_rank']))
 rr=[r for r in qc if r['role_code']==role and r['dimension']=='skills' and r['main_display']=='YES' and r['metric_bucket']=='GENERAL' and r['branch_bucket']=='UNCONDITIONAL'];lk={(r['company_id'],r['label_code']):r for r in rr}
 dat=np.array([[float(lk[c,r['label_code']]['share'])*100 if lk[c,r['label_code']]['share']!='' else np.nan for r in labels] for c in order]);anno=[[f"{lk[c,r['label_code']]['n_positive']}/{lk[c,r['label_code']]['n_interpretable']}"+('*' if lk[c,r['label_code']]['small_n_under10']=='YES' else '') if lk[c,r['label_code']]['n_interpretable']!='0' else 'NA' for r in labels] for c in order]
 fig,ax=plt.subplots(figsize=(13,12));im=heat(ax,dat,[r['label_name'] for r in labels],[cn(c) for c in order],100,anno,8);fig.suptitle(f'Q2  {role_names[role]}：公司技能点值',x=.02,ha='left',fontsize=16);ax.set_title('一般要求·独立条目。格内为分子/分母；颜色为占比 0—100%；* 分母少于 10 条；NA 零分母。',loc='left',fontsize=9,pad=17);fig.subplots_adjust(left=.25,bottom=.16,top=.89,right=.97)
 save(fig,ident,role_names[role]+'公司技能点值','单一语境的补充视图，不是全部技能要求汇总。FAR 点值单列，其他语境的全部公司格见 T3。',rr,'T3_company_context.csv')
dump(ROOT/'figure_manifest.json',figs);dump(ROOT/'verification/plot_environment.json',{'matplotlib':matplotlib.__version__,'numpy':np.__version__,'font':fontname,'font_path':str(font),'font_sha256':__import__('hashlib').sha256(font.read_bytes()).hexdigest() if font.exists() else None,'figures':len(figs)})
print('Figures:',len(figs))
