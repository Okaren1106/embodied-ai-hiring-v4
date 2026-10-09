"""Paper figures from verified finite-corpus statistics.

Audience: internal research manuscript, publication-style editable vector assets.
Fig 1 asks how mention, qualification context and unconditional specification
differ on each fixed task denominator. Fig 2 asks how construct choice changes
Python minus PyTorch ordering. No sample interval or causality is encoded.
Okabe-Ito blue and vermillion plus gray; shapes also identify constructs.
Inputs preserve the approved sample. Output PDF/SVG plus PNG preview.
"""
from pathlib import Path
import csv,json,hashlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'analysis/paired';OUT=ROOT/'release/figures'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':12,
                     'axes.labelsize':10,'pdf.fonttype':42,'svg.fonttype':'none',
                     'axes.spines.top':False,'axes.spines.right':False})
def read(name):
    with (DATA/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def export(fig,stem):
    for ext in ['pdf','svg','png']:
        fig.savefig(OUT/(stem+'.'+ext),dpi=240,metadata={'Creator':'Deterministic matplotlib research script'} if ext=='pdf' else None)
    plt.close(fig)
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    rows={r['label_code']:r for r in read('qualification_scope_summary.csv')}
    order=['SK_PYTHON','SK_PYTORCH','SK_CPP','SK_LINUX','SK_ALTIUM','V2_EMC_SIPI']
    labels=['Python · robot learning','PyTorch · robot learning','C++ · robotics software',
            'Linux · robotics software','Altium · board circuitry','EMC/SI/PI · board circuitry']
    fig,ax=plt.subplots(figsize=(8.4,5.0))
    fig.subplots_adjust(left=.32,right=.98,top=.84,bottom=.19)
    for y,code in enumerate(order):
        r=rows[code];b=int(r['ads'])
        m,h,p,u=[100*int(r[k])/b for k in ['M','H','Q_P','Q_U']]
        assert p<=p+u<=h<=m
        ax.plot([p,m],[y,y],color='#d1d1d1',lw=1.5,zorder=1)
        ax.errorbar(p,y-.13,xerr=[[0],[u]],color='#D55E00',fmt='s',ms=5.5,lw=2,capsize=3,zorder=4)
        ax.plot(h,y,'D',color='#0072B2',ms=5.8,zorder=3)
        ax.plot(m,y+.13,'o',mfc='white',mec='#444444',ms=6,zorder=3)
    ax.set_yticks(range(6),[f'{l}\nN = {rows[c]["ads"]}' for l,c in zip(labels,order)],fontsize=9)
    ax.invert_yaxis();ax.set_xlim(0,100);ax.set_xticks(range(0,101,20))
    ax.set_xlabel('Share of task advertisements (%)')
    ax.grid(axis='x',color='#e5e5e5',lw=.6);ax.set_axisbelow(True)
    legend=[Line2D([],[],marker='o',mfc='white',mec='#444444',ls='',label='Any mention M'),
            Line2D([],[],marker='D',color='#0072B2',ls='',label='Qualification context H'),
            Line2D([],[],marker='s',color='#D55E00',ls='',label='Unconditional expression Q')]
    fig.legend(handles=legend,loc='upper center',bbox_to_anchor=(.54,.95),ncol=1,frameon=False,fontsize=9)
    fig.text(.02,.045,'Source: captured advertisements and recorded context coding. Q bars assign recorded unknowns;\nthese are not confidence intervals. H includes qualification examples, choices and unresolved operators.',fontsize=8)
    export(fig,'Figure_1_qualification_scope')

    allrows=read('qualification_scope_contrasts.csv')
    cue_path=ROOT/'analysis/example_increments/admission_rule_contrasts.csv'
    with cue_path.open(encoding='utf-8-sig',newline='') as f:cue_rows=list(csv.DictReader(f))
    for r in cue_rows:
        if r['admission_rule']=='Q_plus_explicit_nonexhaustive_cues':
            allrows.append({'task':'ROBOT_MODEL','subset':r['subset'],'measure':r['admission_rule'],
                'confirmed_gap_pp':r['confirmed_gap_pp'],'difference_lo_pp':r['lower_pp'],'difference_hi_pp':r['upper_pp']})
    measures=['M','H_qualification_context','Q','Q_plus_explicit_nonexhaustive_cues','Q_plus_example','Q_plus_choice_example']
    names=['Any mention M','Qualification context H','Unconditional expression Q',
           'Q plus clear example cues only','Q plus example-admissible relations','Q plus choice/example-admissible relations']
    fig,axes=plt.subplots(1,2,figsize=(9.2,5.4),sharey=True)
    fig.subplots_adjust(left=.32,right=.98,top=.83,bottom=.23,wspace=.16)
    for ax,subset,title in zip(axes,['all_ads','both_mentioned'],['All robot-learning ads\nN = 105','Both technologies mentioned\nN = 66']):
        for y,measure in enumerate(measures):
            r=next(r for r in allrows if r['task']=='ROBOT_MODEL' and r['subset']==subset and r['measure']==measure)
            p,lo,hi=[float(r[k]) for k in ['confirmed_gap_pp','difference_lo_pp','difference_hi_pp']]
            color='#D55E00' if measure=='Q' else '#0072B2'
            ax.errorbar(p,y,xerr=[[max(0,p-lo)],[max(0,hi-p)]],fmt='s' if measure=='Q' else 'o',color=color,capsize=3,lw=1.8,ms=5)
        ax.axvline(0,color='#666666',lw=.9,ls='--');ax.set_xlim(-35,55);ax.set_xticks([-30,0,30,50])
        ax.grid(axis='x',color='#e6e6e6');ax.set_title(title,fontsize=10,pad=12)
        ax.set_xlabel('Python minus PyTorch (pp)',fontsize=9)
    axes[0].set_yticks(range(len(measures)),names,fontsize=9);axes[0].invert_yaxis()
    fig.text(.02,.06,'Source: captured sample, declared v4 corrections and complete example-increment source review.\nClear cues are “such as”, “e.g.” or Chinese “ru”; the broader rule also admits “deng” and two ambiguous lists.\nPoints count confirmed expressions; bars assign recorded unknowns, not sampling uncertainty.',fontsize=8)
    export(fig,'Figure_2_construct_comparison')
    inputs=['qualification_scope_summary.csv','qualification_scope_contrasts.csv']
    manifest={'inputs':[{'path':'analysis/paired/'+n,'sha256':hashlib.sha256((DATA/n).read_bytes()).hexdigest()} for n in inputs]+[{'path':str(cue_path.relative_to(ROOT)),'sha256':hashlib.sha256(cue_path.read_bytes()).hexdigest()}],
              'outputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(OUT.glob('Figure_*'))],
              'not_sampling_intervals':True,'statistical_inputs_generated_from_real_corpus':True}
    (OUT/'figure_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print('Created two figures in PDF, SVG and PNG.')
if __name__=='__main__':main()
