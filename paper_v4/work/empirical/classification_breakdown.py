"""Exploratory finite-corpus classification-error breakdown analysis.

No model for error probabilities, sampling inference, independent coding, or
causal effect is asserted. V4-derived states and the 128 inherited admissible
readings are read without modification. Adversarial flips concern Q states,
not source rewrites. Company eligibility is rebuilt before this module runs.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict, Counter
import csv, hashlib, itertools, json

ROOT = Path(__file__).resolve().parents[2]
V3 = ROOT / 'source_snapshot'
OUT = ROOT / 'analysis/empirical'
INPUTS = {
    'current': ROOT / 'analysis/v4_ad_technology_current.csv',
    'diagnostic': V3 / 'source_v2/analysis/diagnostic_comparison.csv',
    'policy': V3 / 'data/sensitivity_policy.json',
    'pairs': OUT / 'current_firm_pairs.csv',
    'reading_pairs': OUT / 'admissible_reading_pairs.csv',
}

def read(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write(name, rows):
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / name).open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

def union(g, r):
    return 'P' if 'P' in (g, r) else 'Z' if g == r == 'Z' else 'U'

def key(r):
    return r['identity_key'], r['label_code']

def pairkey(r):
    return int(r['threshold']), r['task'], r['label_code'], r['company_a'], r['company_b']

def cells(rows):
    grouped = defaultdict(list)
    for r in rows:
        grouped[r['task'], r['label_code'], r['company_id']].append(r)
    return grouped

def stats(rows):
    c = Counter(r['Q'] for r in rows)
    return len(rows), c['P'], c['Z'], c['U']

def interval(a, b):
    na, pa, za, ua = stats(a)
    nb, pb, zb, ub = stats(b)
    return F(pa, na) - F(pb + ub, nb), F(pa + ua, na) - F(pb, nb)

def minimum_edits(high, low, endpoint, restricted=True):
    """Min resolved edits to make endpoint <=0; exhaustive integer search.

    A P->Z and B Z->P each reduce every difference endpoint. Keeping all U
    assignments in play means lo<=0 loses strict support; hi<0 strictly forces
    an opposite ordering. The caller chooses the endpoint; equality is allowed
    in the returned count and is separately named as opposite-or-tie for hi.
    """
    nh, ph, zh, uh = stats(high)
    nl, pl, zl, ul = stats(low)
    drops = sorted((r for r in high if r['Q'] == 'P'), key=lambda r: r['identity_key'])
    adds = sorted((r for r in low if r['Q'] == 'Z' and (not restricted or int(r['M']))),
                  key=lambda r: r['identity_key'])
    if endpoint <= 0:
        return {'count': 0, 'drop': 0, 'add': 0, 'residual': endpoint,
                'candidate_drop': len(drops), 'candidate_add': len(adds), 'witness': []}
    feasible = [(i + j, i, j) for i in range(len(drops) + 1)
                for j in range(len(adds) + 1) if F(i, nh) + F(j, nl) >= endpoint]
    if not feasible:
        return None
    count, drop, add = min(feasible)
    residual = endpoint - F(drop, nh) - F(add, nl)
    # Independent greedy lower bound: each edit is additive and all costs are 1.
    weights = sorted([F(1, nh)] * len(drops) + [F(1, nl)] * len(adds), reverse=True)
    total = F(0)
    greedy = None
    for n, weight in enumerate(weights, 1):
        total += weight
        if total >= endpoint:
            greedy = n
            break
    assert greedy == count
    assert residual <= 0
    assert count == 0 or sum(weights[:count - 1], F(0)) < endpoint
    witness = [(r, 'P', 'Z') for r in drops[:drop]] + [(r, 'Z', 'P') for r in adds[:add]]
    return {'count': count, 'drop': drop, 'add': add, 'residual': residual,
            'candidate_drop': len(drops), 'candidate_add': len(adds), 'witness': witness}

def run():
    hashes = {k: hashlib.sha256(p.read_bytes()).hexdigest() for k, p in INPUTS.items()}
    current = read(INPUTS['current'])
    diagnostic = read(INPUTS['diagnostic'])
    policy = json.loads(INPUTS['policy'].read_text(encoding='utf-8'))
    existing = read(INPUTS['pairs'])
    byid = {r['audit_id']: r for r in diagnostic}
    expected_readings = {(r['reading'], pairkey(r)): r for r in read(INPUTS['reading_pairs'])}
    assert len(current) == len({key(r) for r in current}) == 496
    assert len({r['identity_key'] for r in current}) == 248
    assert all(r['Q'] == 'Z' or int(r['M']) for r in current)
    base = cells(current)
    pk = sorted({pairkey(r) for r in existing})
    names = {r['company_id']: r['company_name'] for r in current}
    primary = {}
    for k in pk:
        a, b = base[k[1:3] + (k[3],)], base[k[1:3] + (k[4],)]
        lo, hi = interval(a, b)
        primary[k] = (1 if lo > 0 else -1 if hi < 0 else 0)
    output, witnesses = [], []
    state_changes = 0
    interval_validations = 0
    for bits in itertools.product([0, 1], repeat=7):
        reading = 'READING_' + ''.join(map(str, bits))
        switches = {key(byid[a]): byid[a] for g, bit in zip(policy['groups'], bits) if bit for a in g['audit_ids']}
        rows = []
        for original in current:
            r = dict(original)
            if key(r) in switches:
                d = switches[key(r)]
                r.update(G=d['G_fresh'], R=d['R_fresh'])
                r['Q'] = union(r['G'], r['R'])
            assert r['Q'] == 'Z' or int(r['M'])
            state_changes += r['Q'] != original['Q']
            rows.append(r)
        grouped = cells(rows)
        for k in pk:
            a, b = grouped[k[1:3] + (k[3],)], grouped[k[1:3] + (k[4],)]
            lo, hi = interval(a, b)
            e = expected_readings[reading, k]
            assert abs(float(lo * 100) - float(e['Q_difference_lo_pp'])) < 1e-10
            assert abs(float(hi * 100) - float(e['Q_difference_hi_pp'])) < 1e-10
            interval_validations += 2
            direction = primary[k]
            if not direction:
                high, low = a, b
                margin, upper = lo, hi
            elif direction == 1:
                high, low = a, b
                margin, upper = lo, hi
            else:
                high, low = b, a
                margin, upper = -hi, -lo
            nh, ph, zh, uh = stats(high)
            nl, pl, zl, ul = stats(low)
            meta = dict(reading=reading, threshold=k[0], task=k[1], label_code=k[2],
                        company_a=k[3], company_b=k[4], name_a=names[k[3]], name_b=names[k[4]],
                        primary_supported_direction=direction, high_company=high[0]['company_id'],
                        low_company=low[0]['company_id'], high_B=nh, low_B=nl,
                        high_P=ph, high_U=uh, low_P=pl, low_U=ul,
                        high_M=sum(int(r['M']) for r in high), low_M=sum(int(r['M']) for r in low),
                        resolved_pairs=nh + nl - uh - ul,
                        oriented_lower_pp=float(100 * margin), oriented_upper_pp=float(100 * upper))
            for mode, restricted in [('fixed_mentions', True), ('joint_detection_error', False)]:
                lose = minimum_edits(high, low, margin, restricted) if direction else None
                opposite = minimum_edits(high, low, upper, restricted) if direction else None
                result = {**meta, 'mode': mode,
                          'support_loss_edits': lose['count'] if lose else '',
                          'support_loss_drop_P': lose['drop'] if lose else '',
                          'support_loss_add_P': lose['add'] if lose else '',
                          'candidate_drop_P': lose['candidate_drop'] if lose else '',
                          'candidate_add_P': lose['candidate_add'] if lose else '',
                          'support_loss_residual_pp': float(100 * lose['residual']) if lose else '',
                          'opposite_or_tie_all_U_edits': opposite['count'] if opposite else '',
                          'support_loss_fraction_resolved': lose['count'] / meta['resolved_pairs'] if lose else ''}
                output.append(result)
                if lose and (reading == 'READING_0000000' or lose['count'] <= 1):
                    for r, before, after in lose['witness']:
                        witnesses.append({**{c: result[c] for c in ['reading','threshold','task','label_code','company_a','company_b','mode']},
                                          'identity_key':r['identity_key'],'reading_id':r['reading_id'],
                                          'company_id':r['company_id'],'M':r['M'],
                                          'Q_before':before,'Q_hypothetical_after':after,
                                          'interpretation':'Adversarial witness only; this record is not alleged to be miscoded.'})
    envelopes = []
    originals = {pairkey(r): r for r in existing}
    for k in pk:
        for mode in ['fixed_mentions', 'joint_detection_error']:
            rs = [r for r in output if pairkey(r) == k and r['mode'] == mode]
            assert len(rs) == 128
            usable = [r for r in rs if r['support_loss_edits'] != '']
            baseline = next(r for r in rs if r['reading'] == 'READING_0000000')
            best = min(usable, key=lambda r:(r['support_loss_edits'],r['reading'])) if usable else None
            worst = max(usable, key=lambda r:r['support_loss_edits']) if usable else None
            lo = min(r['oriented_lower_pp'] for r in rs)
            summary = {**{c: baseline[c] for c in ['threshold','task','label_code','company_a','company_b','name_a','name_b','primary_supported_direction','high_company','low_company','high_B','low_B']},
                       'mode':mode,'primary_classification': originals[k]['classification'],
                       'readings':128,'direction_supported_all_readings':int(bool(primary[k]) and lo > 0),
                       'smallest_supporting_margin_pp':lo if primary[k] else '',
                       'baseline_support_loss_edits':baseline['support_loss_edits'],
                       'minimum_support_loss_edits':best['support_loss_edits'] if best else '',
                       'maximum_support_loss_edits':worst['support_loss_edits'] if worst else '',
                       'minimum_reading':best['reading'] if best else '',
                       'minimum_drop_P':best['support_loss_drop_P'] if best else '',
                       'minimum_add_P':best['support_loss_add_P'] if best else '',
                       'minimum_loss_fraction_resolved':best['support_loss_fraction_resolved'] if best else '',
                       'minimum_opposite_or_tie_all_U_edits':min(r['opposite_or_tie_all_U_edits'] for r in usable) if usable else ''}
            envelopes.append(summary)
    summaries = []
    for threshold in [5,10]:
        for mode in ['fixed_mentions','joint_detection_error']:
            for category in ['ALL','SUPPORTED_RETENTION','SUPPORTED_REVERSAL']:
                rows = [r for r in envelopes if r['threshold'] == threshold and r['mode'] == mode
                        and (category == 'ALL' or r['primary_classification'] == category)]
                supported = [r for r in rows if r['direction_supported_all_readings']]
                count = Counter(r['minimum_support_loss_edits'] for r in supported)
                summaries.append({'threshold':threshold,'mode':mode,'category':category,
                                  'all_comparisons':len(rows),'supported_all_readings':len(supported),
                                  'one_edit_loses_support':count[1],
                                  'two_or_fewer_edits_lose_support':sum(v for k,v in count.items() if k<=2),
                                  'three_or_fewer_edits_lose_support':sum(v for k,v in count.items() if k<=3),
                                  'edit_histogram':json.dumps(dict(sorted(count.items())),sort_keys=True),
                                  'distinct_firms':len({r[c] for r in rows for c in ['company_a','company_b']})})
    write('classification_breakdown_readings.csv', output)
    write('classification_breakdown_envelopes.csv', envelopes)
    write('classification_breakdown_summary.csv', summaries)
    write('classification_breakdown_witnesses.csv', witnesses)
    assert hashes == {k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in INPUTS.items()}
    checks = {'advertisement_technology_rows':496,'advertisements':248,'readings':128,
              'pair_keys_across_two_thresholds':len(pk),'exact_interval_endpoint_validations':interval_validations,
              'hypothetical_scenarios':len(output),'witness_rows':len(witnesses),
              'original_input_hashes_unchanged':True,'integer_search_crosschecked_against_greedy':True,
              'interpretation':'Post hoc adversarial finite-state distances, not estimated errors or confidence intervals.',
              'inputs':{k:{'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashes[k]} for k,p in INPUTS.items()},
              'summaries':summaries}
    (OUT/'classification_breakdown_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'summaries':summaries,'main':[r for r in envelopes if r['threshold']==10 and r['mode']=='fixed_mentions']},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    run()
