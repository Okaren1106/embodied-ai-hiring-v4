"""Check all ten manuscript Markdown tables against the locked numeric CSVs.

No manuscript or production data are edited. Every header and body cell is
checked, including continuation-row hierarchy, sample sizes and P/U order.
Reported decimals may differ by at most half a printed last-decimal unit.
"""
from pathlib import Path
from collections import Counter
from decimal import Decimal
import csv,json,re,hashlib

ROOT=Path(__file__).resolve().parents[2]
DEST=ROOT/'verification/manuscript_table_verification.json'
TASKS={'ROBOT_MODEL':('Python−PyTorch','Robot learning','Python / PyTorch'),
       'ROBOT_RUNTIME':('C++−Linux','Robotics software','C++ / Linux'),
       'BOARD_CIRCUIT':('Altium−EMC/SI/PI','Board circuitry','Altium / EMC/SI/PI')}
MEASURE_LABELS={'M':'Mention M','H_qualification_context':'Qualification context H','Q':'Unconditional Q',
                'Q_plus_example':'Q plus all recorded examples',
                'Q_plus_choice_example':'Q plus choices/all recorded examples'}
FILES={
 'main':'work/sol/Research_Working_Manuscript.md',
 'supplement':'work/sol/Research_Working_Supplement.md',
 'scope_contrasts':'analysis/paired/qualification_scope_contrasts.csv',
 'scope_summary':'analysis/paired/qualification_scope_summary.csv',
 'paired_summary':'analysis/paired/paired_summary.csv',
 'joint_states':'analysis/paired/paired_joint_states.csv',
 'local':'analysis/empirical/local_template_construct_contrasts.csv',
 'company_summary':'analysis/empirical/current_pair_summary.csv',
 'breakdown':'analysis/empirical/classification_breakdown_summary.csv',
 'admission':'analysis/example_increments/admission_rule_contrasts.csv',
 'framework':'extensions/framework_control/outputs/framework_contrasts.csv',
 'paired_ads':'analysis/paired/paired_advertisements.csv',
 'increment_ledger':'analysis/example_increments/example_increment_ledger.csv',
}

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def normalized(text):return text.replace('−','-').replace('–','-').strip()
def get(rows,**conditions):
    matches=[r for r in rows if all(str(r[k])==str(v) for k,v in conditions.items())]
    if len(matches)!=1:raise ValueError(('Nonunique source row',conditions,len(matches)))
    return matches[0]
def numeric(value):return ('numeric',value)
def pair(p,u):return ('pair',[p,u])
def interval(lo,hi):return ('interval',[lo,hi])
def fraction(count,total):return ('fraction',[count,total])

def parse_tables(path):
    lines=path.read_text(encoding='utf-8').splitlines();tables={};caption=None;i=0
    while i<len(lines):
        match=re.match(r'^\*\*((?:Supplementary )?Table (?:[IVX]+|S\d+))\.',lines[i])
        if match:caption=(match.group(1),lines[i],i+1)
        if lines[i].startswith('|'):
            if not caption:raise ValueError(('Missing table caption',path,i+1))
            start=i;block=[]
            while i<len(lines) and lines[i].startswith('|'):
                block.append([c.strip() for c in lines[i].strip().strip('|').split('|')]);i+=1
            assert len(block)>2 and all(re.fullmatch(r':?-+:?',c.replace(' ','')) for c in block[1])
            assert all(len(r)==len(block[0]) for r in block)
            assert caption[0] not in tables
            tables[caption[0]]={'caption':caption[1],'caption_line':caption[2],
                               'header':block[0],'rows':block[2:],'line':start+1}
            caption=None;continue
        i+=1
    return tables

def main():
    paths={k:ROOT/v for k,v in FILES.items()};hashes={k:sha(p) for k,p in paths.items()}
    data={k:read(p) for k,p in paths.items() if p.suffix=='.csv'}
    drafts={k:parse_tables(paths[k]) for k in ['main','supplement']}
    cells=[];headers=[];structural=[];tables=[];failures=[];prose_flags=[]
    def fail(where,observed,expected,detail):
        failures.append({'where':where,'observed':observed,'expected':expected,'detail':detail})
    def table(name,doc,header,expected,source):
        t=drafts[doc].get(name)
        if t is None:fail(name,None,'present','Missing expected table');return
        if len(t['rows'])!=len(expected):fail(name,len(t['rows']),len(expected),'Row count')
        if len(t['header'])!=len(header):fail(name,len(t['header']),len(header),'Column count')
        for c,(seen,want) in enumerate(zip(t['header'],header)):
            ok=seen==want;headers.append({'table':name,'column':c+1,'observed':seen,'expected':want,'pass':ok})
            if not ok:fail(name+' header '+str(c+1),seen,want,'Construct/state/header order mismatch')
        numeric_cells=0;numeric_scalars=0
        for i,(seen_row,expected_row) in enumerate(zip(t['rows'],expected)):
            assert len(expected_row)==len(header)
            for c,(seen,want) in enumerate(zip(seen_row,expected_row)):
                record={'table':name,'row':i+1,'column':c+1,'manuscript_line':t['line']+2+i,'observed':seen,'source':source}
                if isinstance(want,tuple):
                    kind,target=want;numeric_cells+=1
                    target=[target] if kind=='numeric' else target
                    split={'numeric':None,'pair':'/','interval':' to ','fraction':' of '}[kind]
                    tokens=[normalized(seen)] if split is None else normalized(seen).split(split)
                    record.update(kind=kind,expected=target)
                    ok=len(tokens)==len(target);components=[]
                    for token,v in zip(tokens,target):
                        token=token.strip()
                        if not re.fullmatch(r'[+-]?\d+(?:\.\d+)?',token):
                            ok=False;components.append({'printed':token,'expected':v,'pass':False});continue
                        decimal_places=len(token.split('.')[1]) if '.' in token else 0
                        tolerance=Decimal(5).scaleb(-decimal_places-1) if decimal_places else Decimal(0)
                        error=abs(Decimal(token)-Decimal(str(v)))
                        valid=error<=tolerance+Decimal('1e-10')
                        ok=ok and valid;numeric_scalars+=1
                        components.append({'printed':token,'expected':v,'printed_decimals':decimal_places,
                                           'allowed_absolute_rounding':str(tolerance),'absolute_error':str(error),'pass':valid})
                    record.update(components=components,pass_=ok)
                else:
                    ok=seen==want;record.update(kind='label_or_hierarchy',expected=want,pass_=ok)
                cells.append(record)
                if not ok:fail(name+f' row {i+1} column {c+1}',seen,want,'Cell value/precision/hierarchy mismatch')
        tables.append({'document':doc,'table':name,'caption_line':t['caption_line'],'rows':len(t['rows']),
                       'columns':len(t['header']),'body_cells_checked':len(t['rows'])*len(t['header']),
                       'numeric_cells_checked':numeric_cells,'numeric_components_checked':numeric_scalars,'source':source})

    # Main I: full task denominator; displayed A and B are positive counts.
    expected=[]
    measures=['M','H_qualification_context','Q','Q_plus_example','Q_plus_choice_example']
    for task in TASKS:
        for j,m in enumerate(measures if task=='ROBOT_MODEL' else measures[:3]):
            r=get(data['scope_contrasts'],task=task,subset='all_ads',measure=m)
            expected.append([f"{TASKS[task][0]}, {r['ads']} ads" if j==0 else '',MEASURE_LABELS[m],
                             numeric(r['a_P']),numeric(r['b_P']),numeric(r['confirmed_gap_pp']),
                             interval(r['difference_lo_pp'],r['difference_hi_pp'])])
    table('Table I','main',['Task and contrast A−B','Construct','A','B','Gap pp','Difference range pp'],expected,FILES['scope_contrasts'])
    # Main II: both-mentioned subset; blank labels must retain the preceding group.
    expected=[]
    selected={'ROBOT_MODEL':measures[1:],'ROBOT_RUNTIME':['H_qualification_context','Q','Q_plus_choice_example'],
              'BOARD_CIRCUIT':['H_qualification_context','Q','Q_plus_example']}
    for task,mm in selected.items():
        for j,m in enumerate(mm):
            r=get(data['scope_contrasts'],task=task,subset='both_mentioned',measure=m)
            label='H' if m=='H_qualification_context' else 'Q' if m=='Q' else MEASURE_LABELS[m]
            if task=='BOARD_CIRCUIT' and m=='Q_plus_example':label='Q plus examples'
            expected.append([TASKS[task][0] if j==0 else '',numeric(r['ads']) if j==0 else '',label,
                             numeric(r['a_P']),numeric(r['b_P']),numeric(r['confirmed_gap_pp']),
                             interval(r['difference_lo_pp'],r['difference_hi_pp'])])
    table('Table II','main',['Contrast','Ads','Construct','A','B','Gap pp','Difference range pp'],expected,FILES['scope_contrasts'])
    # Company classifications and adversarial distances.
    classifications=['SUPPORTED_RETENTION','SUPPORTED_REVERSAL','CONDITIONAL_REVERSAL_OVERLAP',
                     'CONDITIONAL_RETENTION_OVERLAP','CONDITIONAL_TIE_OVERLAP']
    company_expected=[];main_company=[]
    for threshold in [10,5]:
        c=get(data['company_summary'],threshold=threshold,label_code='ALL')
        b=get(data['breakdown'],threshold=threshold,mode='fixed_mentions',category='ALL')
        row=[numeric(threshold),numeric(c['pairs'])]+[numeric(c[k]) for k in classifications]
        company_expected.append(row)
        one=fraction(b['one_edit_loses_support'],b['supported_all_readings']) if threshold==5 else numeric(b['one_edit_loses_support'])
        two=fraction(b['two_or_fewer_edits_lose_support'],b['supported_all_readings']) if threshold==5 else numeric(b['two_or_fewer_edits_lose_support'])
        main_company.append(row+[one,two])
    chead=['Pairs','Supported retention','Supported reversal','Conditional reversal overlap','Conditional retention overlap','Conditional tie overlap']
    table('Table III','main',['Minimum N']+chead+['One edit from loss','≤2 edits from loss'],main_company,[FILES['company_summary'],FILES['breakdown']])
    # Supplement S1: same target/task ordering and construct-specific P/U counts.
    targets=[('ROBOT_MODEL','SK_PYTHON','Python'),('ROBOT_MODEL','SK_PYTORCH','PyTorch'),
             ('ROBOT_RUNTIME','SK_CPP','C++'),('ROBOT_RUNTIME','SK_LINUX','Linux'),
             ('BOARD_CIRCUIT','SK_ALTIUM','Altium'),('BOARD_CIRCUIT','V2_EMC_SIPI','EMC/SI/PI')]
    expected=[]
    for task,label,name in targets:
        r=get(data['scope_summary'],task=task,label_code=label)
        expected.append([TASKS[task][1],name,numeric(r['ads']),numeric(r['M']),numeric(r['H']),
                         pair(r['Q_P'],r['Q_U']),pair(r['Q_plus_example_P'],r['Q_plus_example_U']),
                         pair(r['Q_plus_choice_example_P'],r['Q_plus_choice_example_U'])])
        valid=int(r['Q_P'])<=int(r['Q_plus_example_P'])<=int(r['Q_plus_choice_example_P'])<=int(r['H'])<=int(r['M'])<=int(r['ads'])
        valid=valid and all(int(r[m+'_P'])+int(r[m+'_U'])<=int(r['ads']) for m in ['Q','Q_plus_example','Q_plus_choice_example'])
        structural.append({'check':'Scope count nesting and construct-specific P/U capacity','target':label,'pass':valid})
        if not valid:fail('Scope hierarchy '+label,r,'Nested counts and capacity','Source and table interpretation')
    table('Supplementary Table S1','supplement',['Task','Target','Ads','M','H','Q P / U','Q+E P / U','Q+C+E P / U'],expected,FILES['scope_summary'])
    # Supplement S2: full block text weighting, not local parent weighting.
    expected=[]
    for subset,label in [('all_ads','All robot-learning ads'),('both_mentioned','Both mentioned')]:
        for j,(weight,name) in enumerate([('ad_equal','Advertisement'),('firm_equal','Firm equal'),('firm_template_equal','Firm × exact text')]):
            r=get(data['paired_summary'],task='ROBOT_MODEL',subset=subset,weighting=weight)
            expected.append([label if j==0 else '',name,numeric(r['ads']),numeric(r['firms']),
                             numeric(r['confirmed_gap_pp']),interval(r['Q_difference_lo_pp'],r['Q_difference_hi_pp'])])
    table('Supplementary Table S2','supplement',['Sample','Weight','Ads','Firms','Confirmed Python−PyTorch pp','Outer range pp'],expected,FILES['paired_summary'])
    # Supplement S3: local target parent groups; different weighting estimand.
    expected=[]
    for subset,label in [('all_ads','All 105 advertisements'),('both_mentioned','Both mentioned, 66')]:
        for j,m in enumerate(measures if subset=='all_ads' else measures[1:]):
            r=get(data['local'],task='ROBOT_MODEL',subset=subset,weighting='firm_local_target_equal',measure=m)
            name='H' if m=='H_qualification_context' else m if m in ['M','Q'] else MEASURE_LABELS[m]
            expected.append([label if j==0 else '',name,numeric(r['confirmed_gap_pp']),interval(r['difference_lo_pp'],r['difference_hi_pp'])])
            intended_ads=105 if subset=='all_ads' else 66
            valid=int(r['ads'])==intended_ads
            structural.append({'check':'S3 labelled sample denominator','subset':subset,'pass':valid})
            if not valid:fail('S3 sample label',r['ads'],intended_ads,'Label denominator')
    table('Supplementary Table S3','supplement',['Sample','Construct','Confirmed Python−PyTorch pp','Outer range pp'],expected,FILES['local'])
    # Supplement S4: exhaustive nine-state counts including zero cells.
    expected=[];state_headers=[a+'/'+b for a in ['P','Z','U'] for b in ['P','Z','U']]
    for task in TASKS:
        total=0;numbers=[]
        for a in ['P','Z','U']:
            for b in ['P','Z','U']:
                matches=[r for r in data['joint_states'] if r['task']==task and r['subset']=='both_mentioned' and r['Q_a']==a and r['Q_b']==b]
                assert len(matches)<=1
                value=int(matches[0]['ads']) if matches else 0;total+=value;numbers.append(numeric(value))
        expected.append([TASKS[task][2]]+numbers+[numeric(total)])
        raw=Counter((r['Q_a'],r['Q_b']) for r in data['paired_ads'] if r['task']==task and r['both_mentioned']=='1')
        valid=sum(raw.values())==total and all(raw[a,b]==int(numbers[j][1]) for j,(a,b) in enumerate(( (a,b) for a in ['P','Z','U'] for b in ['P','Z','U'] )))
        structural.append({'check':'Joint-state table exhaustiveness and paired-advertisement source','task':task,'pass':valid})
        if not valid:fail('S4 joint-state '+task,total,dict(raw),'Joint-state recomputation')
    table('Supplementary Table S4','supplement',['Pair']+state_headers+['Total'],expected,[FILES['joint_states'],FILES['paired_ads']])
    # Supplement S5: latest admission-rule identifier and both sample strata.
    rule_labels=[('Q','Narrow Q'),('Q_plus_explicit_nonexhaustive_cues','Q plus 17 clear-cue cases'),
                 ('Q_plus_examples_excluding_bare_parentheses','Q plus recorded examples except bare parentheses'),
                 ('Q_plus_admitted_example_scope','Q plus all recorded examples')]
    expected=[]
    for rule,label in rule_labels:
        values=[label]
        for subset,n in [('all_ads',105),('both_mentioned',66)]:
            r=get(data['admission'],subset=subset,admission_rule=rule)
            valid=int(r['ads'])==n
            structural.append({'check':'Admission-rule subset denominator','rule':rule,'subset':subset,'pass':valid})
            if not valid:fail('S5 sample '+rule,r['ads'],n,'Admission sample')
            values.extend([pair(r['python_P'],r['python_U']),pair(r['pytorch_P'],r['pytorch_U']),interval(r['lower_pp'],r['upper_pp'])])
        expected.append(values)
    clear=sum(r['cue_family'] in ['EN_SUCH_AS','EN_EG','EXPLICIT_CHINESE_RU'] for r in data['increment_ledger'])
    structural.append({'check':'S5 explicit 17-clear-cue label against increment ledger','actual':clear,'pass':clear==17})
    if clear!=17:fail('S5 clear-cue label',17,clear,'Cue-class count')
    table('Supplementary Table S5','supplement',['Admission rule','Full sample Python P/U','Full sample PyTorch P/U','Full range pp','Both-mentioned Python P/U','Both-mentioned PyTorch P/U','Both-mentioned range pp'],expected,[FILES['admission'],FILES['increment_ledger']])
    # Supplement S6: framework-control subset, five distinct construct states.
    expected=[]
    for m,label in [('M','M'),('H','H'),('Q','Q'),('Q_plus_example','Q plus examples'),('Q_plus_choice_example','Q plus choices/examples')]:
        r=get(data['framework'],version='harmonized_framework_control',subset='both_mentioned',measure=m)
        assert int(r['ads'])==26
        expected.append([label,pair(r['a_P'],r['a_U']),pair(r['b_P'],r['b_U']),numeric(r['confirmed_gap_pp']),interval(r['difference_lo_pp'],r['difference_hi_pp'])])
    table('Supplementary Table S6','supplement',['Construct','PyTorch P/U','TensorFlow P/U','Confirmed gap pp','Outer range pp'],expected,FILES['framework'])
    table('Supplementary Table S7','supplement',['N']+chead,company_expected,FILES['company_summary'])
    expected_tables={'main':{'Table I','Table II','Table III'},'supplement':{f'Supplementary Table S{i}' for i in range(1,8)}}
    for doc,keys in expected_tables.items():
        if set(drafts[doc])!=keys:fail(doc+' table inventory',sorted(drafts[doc]),sorted(keys),'Missing or additional unchecked table')
    # Relevant table-cross-reference regression check, without rewriting prose.
    supp=paths['supplement'].read_text(encoding='utf-8')
    for i,line in enumerate(supp.splitlines(),1):
        if 'full-sample reversal appears' in line and 'class is admitted' in line and 'Table S5' not in line:
            prose_flags.append({'document':'supplement','line':i,'detail':'Admission-rule result should point to Table S5, not joint-state Table S4.','text':line})
    final_hashes={k:sha(p) for k,p in paths.items()}
    unchanged=hashes==final_hashes
    if not unchanged:fail('input hashes','changed','unchanged','Input changed during verification; rerun required')
    report={'status':'PASS' if not failures and not prose_flags else 'FAIL',
            'tables_checked':len(tables),'main_tables':len(drafts['main']),'supplement_tables':len(drafts['supplement']),
            'body_cells_checked':len(cells),'header_cells_checked':len(headers),
            'numeric_body_cells_checked':sum(t['numeric_cells_checked'] for t in tables),
            'numeric_components_checked':sum(t['numeric_components_checked'] for t in tables),
            'label_and_hierarchy_cells_checked':sum(c['kind']=='label_or_hierarchy' for c in cells),
            'structural_checks':structural,'tables':tables,'failures':failures,'table_reference_flags':prose_flags,
            'rounding_policy':'Integer counts must match exactly. A decimal may differ from its unrounded CSV value by no more than half a last printed unit (plus 1e-10 numeric tolerance); this admits conventional half-up and half-even rounding.',
            'scope':'Every body cell and header in the main three and supplementary seven tables is checked. This is numeric, state-label, denominator and grouping verification; prose beyond the named table-reference check and visual layout are outside scope.',
            'source_manuscript_hashes':{FILES[k]:hashes[k] for k in ['main','supplement']},
            'source_table_hashes':{FILES[k]:hashes[k] for k in FILES if k not in ['main','supplement']},
            'all_inputs_unchanged_during_verification':unchanged,'cell_checks':cells,'header_checks':headers}
    DEST.parent.mkdir(parents=True,exist_ok=True)
    DEST.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','tables_checked','body_cells_checked','header_cells_checked','numeric_body_cells_checked','numeric_components_checked','label_and_hierarchy_cells_checked','failures','table_reference_flags','source_manuscript_hashes']},ensure_ascii=False,indent=2))
    if failures or prose_flags:raise SystemExit(1)

if __name__=='__main__':main()
