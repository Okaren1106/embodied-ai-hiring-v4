"""Stage B repair / step 7: company cards, the overview page and its data payload.

Cards and the page are rendered from the same generated tables the checks read, so a
number on the page cannot come from a different source than the number in the CSV.
Each fact on the page carries its subject, scope, event or period, its value status,
its time qualification, the relations behind it and the snapshot the quote came from;
unknowns are shown as unknown, and background-only material is marked as such instead
of being mixed into comparable companies.
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import CORE_FIELDS, RUN, WORK, load_companies, read_csv, write_json  # noqa: E402

BUCKET_LABEL = {
    "STRICT_COMPARABLE": "合格比较",
    "BACKGROUND_DISPLAY_ONLY": "仅背景展示",
    "EXCLUDED_UNKNOWN": "退出比较（未确立/不适用）",
    "NOT_RESEARCHED": "未查证",
}


def stable_cards(companies, facts_by_company, evidence_by_company, gaps_by_company,
                 groups_by_company, caps_by_company, researched) -> list[dict]:
    cards = []
    for c in companies:
        cid = c["company_id"]
        facts = sorted(facts_by_company.get(cid, []), key=lambda f: (f["field"], f["fact_seq"]))
        evidence = sorted(evidence_by_company.get(cid, []), key=lambda e: e["evidence_id"])
        gaps = sorted(gaps_by_company.get(cid, []), key=lambda g: g["orig_gap_id"])
        groups = sorted(groups_by_company.get(cid, []), key=lambda g: (g["dimension"], g["group_value"]))
        caps = sorted(caps_by_company.get(cid, []), key=lambda x: x["capital_event_id"])
        obs_dates = sorted({f["observation_date"] for f in facts}) or \
            sorted(k for k in c["waves_from_jobs"].keys() if k)
        cards.append({
            "company_id": cid,
            "company_name": c["company_name"],
            "country": c["country"],
            "researched": cid in researched,
            "observation_date": obs_dates[-1] if obs_dates else "",
            "n_ads": c["n_ads"],
            "scope": c["entity_scope_inherited"] or c["hiring_scope_inherited"],
            "n_facts": len(facts),
            "n_evidence": len(evidence),
            "n_gaps": len(gaps),
            "n_open_gaps": sum(1 for g in gaps if g["open_at_stage_b_end"] == "YES"),
            "n_strict": sum(1 for f in facts if f["time_applicability"] in
                            ("USABLE_AT_OBSERVATION", "NOT_TIME_SENSITIVE")
                            and f["value_status"] in ("SUPPORTED_EXTERNAL", "COMPANY_SELF_REPORT",
                                                      "MEDIA_STATEMENT", "COUNTERPARTY_CONFIRMATION",
                                                      "CONFLICT_RESOLVED_BY_SEPARATION",
                                                      "MIXED_SEE_EVIDENCE")),
            "n_unknown_fields": sum(1 for f in facts if f["value_status"] in
                                    ("NOT_YET_SEARCHED", "SEARCHED_NOT_FOUND", "ACCESS_BLOCKED")),
            "facts": [{
                "field": f["field"], "fact_id": f["fact_id"], "seq": int(f["fact_seq"] or 1),
                "assertion_kind": f["assertion_kind"],
                "subject": f["subject_entity"], "scope": f["product_or_business_scope"],
                "period": f["event_or_period"],
                "value": f["value"], "value_status": f["value_status"],
                "research_status": f["research_status"],
                "time": f["time_applicability"], "time_reason": f["time_reason"],
                "event_date": f["event_date"], "publication_date": f["publication_date"],
                "evidence": f["evidence_ids"].split("|") if f["evidence_ids"] else [],
                "date_basis": f["time_basis_evidence_ids"].split("|") if f["time_basis_evidence_ids"] else [],
                "decision_reason": f["decision_reason"],
                "note": f["note"],
                "checked_in_stage_b": f["checked_in_stage_b"],
            } for f in facts],
            "evidence": [{
                "evidence_id": e["evidence_id"], "field": e["field"], "claim": e["claim"],                "quote": e["quote"], "quote_locator": e["quote_locator"],
                "title": e["source_title"], "publisher": e["publisher"],
                "nature": e["source_nature"], "claim_nature": e["claim_nature"],
                "url": e["url"], "access": e["access_status"],
                "publication_date": e["publication_date"], "event_date": e["event_date"],
                "snapshot": e["snapshot_text_path"], "snapshot_sha256": e["snapshot_sha256"],
                "capture_medium": e.get("capture_medium", ""), "raw": e.get("snapshot_raw_path", ""),
                "raw_sha256": e.get("snapshot_raw_sha256", ""), "capture_record": e.get("capture_record_path", ""),
                "relation_to_inherited": e["relation_to_inherited"], "note": e["note"],
            } for e in evidence],
            "gaps": [{
                "orig_gap_id": g["orig_gap_id"], "fact_field": g["fact_field"],
                "gap_type": g["gap_type_inherited"], "inherited_value": g["inherited_value"],
                "status": g["stage_b_status"], "result": g["stage_b_result"],
                "facts": g["new_fact_ids"].split("|") if g["new_fact_ids"] else [],
                "evidence": g["new_evidence_ids"].split("|") if g["new_evidence_ids"] else [],
                "closure_reason": g["closure_reason"],
                "open": g["open_at_stage_b_end"],
            } for g in gaps],
            "groups": [{
                "dimension": g["dimension"], "group_value": g["group_value"],
                "bucket": g["comparison_bucket"], "bucket_label": BUCKET_LABEL.get(g["comparison_bucket"], g["comparison_bucket"]),
                "strength": g["evidence_strength"], "time": g["time_applicability"],
                "included": g["included_in_comparison"], "exclusion": g["exclusion_reason"],
                "basis": g["basis_fact_ids"],
            } for g in groups],
            "capital": [{
                "capital_event_id": c2["capital_event_id"], "event_type": c2["event_type"],
                "round": c2["round_or_deal"], "amount": c2["amount_original"],
                "currency": c2["currency"], "unit": c2["amount_unit"], "scope": c2["amount_scope"],
                "valuation": c2["post_money_valuation_original"],
                "event_date": c2["event_date"], "publication_date": c2["publication_date"],
                "availability": c2["at_observation_availability"],
                "evidence": c2["evidence_ids"].split("|") if c2["evidence_ids"] else [],
                "note": c2["note"], "conflict_note": c2["conflict_note"],
            } for c2 in caps],
        })
    return cards


def build_html(cards: list[dict], meta: dict) -> str:
    data = json.dumps(cards, ensure_ascii=False, separators=(",", ":"))
    meta_json = json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
    return """<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>阶段 B 返修版公司事实与证据总览</title>
<style>
:root{--bg:#0f1216;--panel:#161b22;--line:#26303b;--ink:#e6edf3;--dim:#9aa7b4;--accent:#4bb3a5;
--strict:#2f7d6b;--bgonly:#7a6a2f;--excl:#5a4a4a;--none:#3a3f46;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.6 "Segoe UI","Microsoft YaHei",system-ui,sans-serif}
header{padding:18px 22px;border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(15,18,22,.96);z-index:5}
h1{margin:0 0 6px;font-size:17px;letter-spacing:.3px}
.meta{color:var(--dim);font-size:12px}
.wrap{display:grid;grid-template-columns:280px 1fr;min-height:calc(100vh - 70px)}
aside{border-right:1px solid var(--line);padding:14px;overflow:auto;max-height:calc(100vh - 70px)}
input,select{width:100%;padding:8px;background:var(--panel);color:var(--ink);border:1px solid var(--line);border-radius:6px;margin-bottom:10px}
button{width:100%;text-align:left;padding:8px 10px;margin-bottom:6px;background:var(--panel);color:var(--ink);
border:1px solid var(--line);border-radius:6px;cursor:pointer;font:inherit}
button:hover{border-color:var(--accent)}
button.active{border-color:var(--accent);background:#1b2530}
main{padding:18px 22px;overflow:auto;max-height:calc(100vh - 70px)}
h2{font-size:16px;margin:22px 0 8px;padding-bottom:6px;border-bottom:1px solid var(--line)}
h3{font-size:14px;margin:16px 0 6px;color:var(--accent)}
table{width:100%;border-collapse:collapse;font-size:13px;margin:8px 0}
th,td{border:1px solid var(--line);padding:6px 8px;vertical-align:top;text-align:left}
th{background:#1a212a;color:var(--dim);font-weight:600}
code{background:#1a212a;padding:1px 5px;border-radius:4px;font-size:12px}
.pill{display:inline-block;padding:1px 7px;border-radius:10px;font-size:11px;border:1px solid var(--line)}
.s-strict{background:var(--strict)}.s-bg{background:var(--bgonly)}.s-excl{background:var(--excl)}
.s-none{background:var(--none)}
.dim{color:var(--dim)}
.q{white-space:pre-wrap;background:#12181f;border-left:3px solid var(--accent);padding:8px 10px;margin:6px 0;font-size:12.5px}
.card{border:1px solid var(--line);border-radius:8px;padding:12px;margin:10px 0;background:var(--panel)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px}
.kv{font-size:12.5px}
.unknown{color:#c9a227}
a{color:#6cc7ff}
</style></head><body>
<header>
  <h1>阶段 B 返修版：24 家公司事实、证据与缺口总览</h1>
  <div class="meta" id="meta"></div>
</header>
<div class="wrap">
  <aside>
    <input id="q" placeholder="搜索公司 / 字段 / 证据 ID / 缺口 ID">
    <select id="filter">
      <option value="all">全部 24 家</option>
      <option value="has_unknown">含未查或查后未找到字段</option>
      <option value="no_unknown">本轮字段均已给出非未查状态</option>
    </select>
    <div id="list"></div>
  </aside>
  <main id="main"></main>
</div>
<script>
const META = __META__;
const DATA = __DATA__;
const shortId = c => c.replace(/^([A-Z]{2})_/, '$1 ');function el(id){return document.getElementById(id);}
document.getElementById('meta').textContent =
  META.note + ' ｜ 自检 ' + META.self_check + ' ｜ 输入摘要 ' + META.input_digest.slice(0,16) + '… ｜ 代码 ' + META.code_version;
const list = el('list');
function matches(c, q){
  if(!q) return true;
  const blob = [c.company_id, c.company_name, c.scope,
    ...c.facts.map(f=>f.field+' '+f.value),
    ...c.evidence.map(e=>e.evidence_id+' '+e.title),
    ...c.gaps.map(g=>g.orig_gap_id+' '+g.inherited_value)].join(' ').toLowerCase();
  return blob.includes(q.toLowerCase());
}
function renderList(){
  const q = el('q').value.trim();
  const f = el('filter').value;
  list.innerHTML = '';
  DATA.filter(c => {
      const unknown = (c.n_unknown_fields||0) > 0;
      const okFilter = f==='all' || (f==='has_unknown'&&unknown) || (f==='no_unknown'&&!unknown)
        || (f==='researched'&&c.researched) || (f==='unsearched'&&!c.researched);
      return okFilter && matches(c,q);
    })
    .forEach(c => {
      const b = document.createElement('button');
      b.textContent = c.company_id + ((c.n_unknown_fields||0) ? ' · 含未查字段' : ' · 已有记录')
        + ' (' + c.n_facts + '事实/' + c.n_open_gaps + '开放缺口)';
      b.onclick = () => { renderMain(c); [...list.children].forEach(x=>x.classList.remove('active')); b.classList.add('active'); };
      list.appendChild(b);
    });
}
function esc(s){return (s==null?'':String(s)).replace(/[&<>]/g, m=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[m]));}
function bucketPill(b){
  const cls = {'STRICT_COMPARABLE':'s-strict','BACKGROUND_DISPLAY_ONLY':'s-bg',
               'EXCLUDED_UNKNOWN':'s-excl','NOT_RESEARCHED':'s-none'}[b] || 's-none';
  return '<span class="pill '+cls+'">'+esc(b)+'</span>';
}
function renderFacts(c){
  let h = '<h2>事实（'+c.n_facts+' 行，含主体、范围与事件/时期）</h2>'
    + '<table><tr><th>字段</th><th>主体 / 范围 / 事件</th><th>值</th><th>证据性质</th><th>时点适用性</th><th>日期依据</th><th>关联证据</th></tr>';
  c.facts.forEach(f=>{
    const val = f.value ? esc(f.value) : '<span class="unknown">未确立（'+esc(f.value_status)+'）</span>';
    h += '<tr><td><code>'+esc(f.field)+'</code>'+(f.seq>1?' #'+f.seq:'')+'</td>'
      + '<td class="kv">'+esc(f.subject)+'<br><span class="dim">'+esc(f.scope||'—')+'</span><br><span class="dim">'+esc(f.period||'—')+'</span></td>'
      + '<td>'+val+'</td><td>'+esc(f.value_status)+'</td>'
      + '<td>'+esc(f.time)+'<br><span class="dim">'+esc(f.time_reason)+'</span></td>'
      + '<td class="kv">'+esc(f.event_date||'—')+' / '+esc(f.publication_date||'—')+'<br><span class="dim">'+esc((f.date_basis||[]).join(', ')||'无合格依据')+'</span></td>'
      + '<td class="kv">'+esc((f.evidence||[]).join(', '))+'</td></tr>';
  });
  return h + '</table>';
}
function renderEvidence(c){
  let h = '<h2>证据与原文（'+c.n_evidence+' 条）</h2>';
  c.evidence.forEach(e=>{
    h += '<div class="card"><b>'+esc(e.evidence_id)+'</b> <span class="dim">'+esc(e.field)+' ｜ '
      + esc(e.nature)+' ｜ '+esc(e.claim_nature)+' ｜ 访问 '+esc(e.access)+'</span>'
      + '<div class="kv">'+esc(e.title)+' ｜ '+esc(e.publisher)+'</div>'
      + '<div class="kv"><a href="'+esc(e.url)+'" target="_blank">'+esc(e.url)+'</a></div>'
      + '<div class="kv dim">发布 '+esc(e.publication_date||'—')+' ｜ 事件 '+esc(e.event_date||'—')
      + ' ｜ 定位 '+esc(e.quote_locator)+' ｜ 保存方式 '+esc(e.capture_medium||'历史记录')
      + ' ｜ <a href="'+esc(e.snapshot||'#')+'" target="_blank">正文快照</a>'
      + (e.raw ? ' ｜ <a href="'+esc(e.raw)+'" target="_blank">HTTP原件</a>' : ' ｜ 无HTTP原件')
      + (e.capture_record ? ' ｜ <a href="'+esc(e.capture_record)+'" target="_blank">读取记录</a>' : '')
      + '<br>正文哈希 sha256 '+esc((e.snapshot_sha256||'').slice(0,24))+'…</div>'
      + '<div class="q">'+esc((e.quote||'').slice(0,700))+'</div>'
      + '<div class="kv dim">'+esc(e.note||'')+'</div></div>';
  });
  return h;
}
function renderGroups(c){
  let h = '<h2>分组与比较资格</h2><table><tr><th>维度</th><th>组</th><th>桶</th><th>证据强度</th><th>时点</th><th>是否入比较</th><th>理由</th></tr>';
  c.groups.forEach(g=>{
    h += '<tr><td><code>'+esc(g.dimension)+'</code></td><td>'+esc(g.group_value)+'</td><td>'+bucketPill(g.bucket)+'</td>'
      + '<td>'+esc(g.strength||'—')+'</td><td>'+esc(g.time||'—')+'</td><td>'+esc(g.included)+'</td><td class="dim">'+esc(g.exclusion||'')+'</td></tr>';
  });
  return h + '</table>';
}
function renderCapital(c){
  if(!c.capital.length) return '<h2>资本事件</h2><p class="dim">本轮未取得该主体的融资或并购事件；不补造金额。</p>';
  let h = '<h2>资本事件</h2><table><tr><th>事件</th><th>轮次/交易</th><th>金额</th><th>估值</th><th>事件日</th><th>发布日</th><th>时点</th><th>来源</th></tr>';
  c.capital.forEach(x=>{
    h += '<tr><td><code>'+esc(x.capital_event_id)+'</code></td><td>'+esc(x.round)+'</td>'
      + '<td>'+esc(x.amount||'未披露')+' '+esc(x.currency)+' '+esc(x.unit)+' <span class="dim">'+esc(x.scope)+'</span></td>'
      + '<td>'+esc(x.valuation||'—')+'</td><td>'+esc(x.event_date||'—')+'</td><td>'+esc(x.publication_date||'—')+'</td>'
      + '<td>'+esc(x.availability)+'</td><td class="kv">'+esc((x.evidence||[]).join(', '))+'</td></tr>'
      + (x.note ? '<tr><td colspan="8" class="dim">'+esc(x.note)+'</td></tr>' : '');
  });
  return h + '</table>';
}
function renderGaps(c){
  let h = '<h2>继承缺口逐项结果（'+c.n_gaps+' 项，未查项保留原文）</h2>'
    + '<table><tr><th>缺口 ID</th><th>继承字段</th><th>继承值</th><th>本轮状态</th><th>结果</th><th>是否仍开放</th></tr>';
  c.gaps.forEach(g=>{
    h += '<tr><td><code>'+esc(g.orig_gap_id)+'</code></td><td>'+esc(g.fact_field)+'</td>'
      + '<td class="kv">'+esc((g.inherited_value||'').slice(0,160))+'</td><td>'+esc(g.status)+'</td>'
      + '<td class="kv">'+esc((g.result||'').slice(0,200))+'</td><td>'+esc(g.open)+'</td></tr>';
  });
  return h + '</table>';
}
function renderMain(c){
  let h = '<h2>'+esc(c.company_name||c.company_id)+' <span class="dim">('+esc(c.company_id)+')</span></h2>'
    + '<div class="grid">'
    + '<div class="card kv"><b>招聘观察日</b><br>'+esc(c.observation_date||'—')+'</div>'
    + '<div class="card kv"><b>广告数（继承）</b><br>'+esc(c.n_ads)+'</div>'
    + '<div class="card kv"><b>研究主体范围</b><br>'+esc(c.scope||'—')+'</div>'
    + '<div class="card kv"><b>本轮状态</b><br>'+(c.researched?'已查证':'未查证（保留待查）')+'</div>'
    + '<div class="card kv"><b>合格比较事实</b><br>'+c.n_strict+' 行</div>'
    + '<div class="card kv"><b>仍未关闭缺口</b><br>'+c.n_open_gaps+' 项</div>'
    + '</div>';
  if(!c.researched){
    h += '<p class="dim">该公司本轮未研究：缺口全部保留未查状态，不参与比较，也不代填任何结果。</p>';
  }
  h += renderFacts(c) + renderGroups(c) + renderCapital(c) + renderEvidence(c) + renderGaps(c);
  el('main').innerHTML = h;
}
el('q').addEventListener('input', renderList);
el('filter').addEventListener('change', renderList);
renderList();
renderMain(DATA.filter(x=>x.researched)[0] || DATA[0]);
</script></body></html>
""".replace("__DATA__", data).replace("__META__", meta_json)


def main() -> int:
    companies = load_companies()
    facts = read_csv(os.path.join(RUN, "company_facts.csv"))
    evidence = read_csv(os.path.join(RUN, "company_evidence.csv"))
    gaps = read_csv(os.path.join(RUN, "company_gaps.csv"))
    groups = read_csv(os.path.join(RUN, "company_group_mapping.csv"))
    caps = read_csv(os.path.join(RUN, "capital_events.csv"))
    links = read_csv(os.path.join(RUN, "evidence_links.csv"))
    lock = json.load(open(os.path.join(WORK, "input_lock.json"), encoding="utf-8"))

    by = lambda rows, key: _group(rows, key)
    facts_by_company = by(facts, "company_id")
    evidence_by_company = by(evidence, "company_id")
    gaps_by_company = by(gaps, "company_id")
    groups_by_company = by(groups, "company_id")
    caps_by_company = by(caps, "company_id")
    researched = {f["company_id"] for f in facts}

    cards = stable_cards(companies, facts_by_company, evidence_by_company, gaps_by_company,
                         groups_by_company, caps_by_company, researched)

    # per-company markdown card
    cards_dir = os.path.join(RUN, "company_cards")
    os.makedirs(cards_dir, exist_ok=True)
    for card in cards:
        lines = [
            f"# {card['company_name'] or card['company_id']}（{card['company_id']}）公司卡（返修版）",
            "",
            f"- 招聘观察日：{card['observation_date'] or '—'}；继承广告数：{card['n_ads']}",
            f"- 研究主体范围：{card['scope'] or '—'}",
            f"- 本轮状态：已有公司记录；含未查/查后未找到字段 {(card.get('n_unknown_fields') or 0)} 项（24 家有记录 ≠ 每字段已查完）",
            f"- 事实行：{card['n_facts']}；证据：{card['n_evidence']}；继承缺口：{card['n_gaps']}（仍未关闭 {card['n_open_gaps']}）",
            f"- 合格比较事实：{card['n_strict']}",
            "",
            "## 事实",
            "",
        ]
        if card["researched"]:
            lines += ["| 字段 | 主体 / 范围 / 事件 | 值 | 证据性质 | 时点 | 日期依据 |", "|---|---|---|---|---|---|"]
            for f in card["facts"]:
                lines.append("| `{}`{} | {} / {} / {} | {} | {} | {} | {} |".format(
                    f["field"], f" #{f['seq']}" if f["seq"] > 1 else "", f["subject"],
                    f["scope"] or "—", f["period"] or "—", (f["value"] or "未确立").replace("|", "/"),
                    f["value_status"], f["time"], ", ".join(f["date_basis"]) or "无合格依据"))
        else:
            lines.append("（本轮未研究该公司，无新事实行）")
        lines += ["", "## 分组与比较资格", "", "| 维度 | 组 | 桶 | 强度 | 入比较 | 理由 |", "|---|---|---|---|---|---|"]
        for g in card["groups"]:
            lines.append(f"| `{g['dimension']}` | {g['group_value']} | {g['bucket_label']} | {g['strength'] or '—'} | {g['included']} | {g['exclusion'] or ''} |")
        lines += ["", "## 资本事件", ""]
        if card["capital"]:
            lines += ["| 事件 | 轮次 | 金额 | 估值 | 事件日 | 发布日 | 时点 | 来源 |", "|---|---|---|---|---|---|---|---|"]
            for x in card["capital"]:
                lines.append(f"| `{x['capital_event_id']}` | {x['round']} | {x['amount'] or '未披露'} | {x['valuation'] or '—'} | {x['event_date'] or '—'} | {x['publication_date'] or '—'} | {x['availability']} | {', '.join(x['evidence'])} |")
        else:
            lines.append("（本轮未取得资本事件；不补造金额）")
        lines += ["", "## 证据", ""]
        for e in card["evidence"]:
            lines += [f"### {e['evidence_id']}", "",
                      f"- {e['title']} ｜ {e['publisher']} ｜ {e['nature']} ｜ {e['claim_nature']}",
                      f"- 链接：{e['url']}",
                      f"- 发布 {e['publication_date'] or '—'}；事件 {e['event_date'] or '—'}；访问 {e['access']}；快照 `{e['snapshot'] or '—'}`",
                      f"- 定位：{e['quote_locator']}",
                      "", "> " + (e["quote"] or "").replace("\n", "\n> "), "",
                      f"- 保存方式：{e.get('capture_medium', '')}；原件：{e.get('raw', '') or '未保存HTTP原件'}；原件哈希：{e.get('raw_sha256', '') or '不适用'}",
                      f"- 备注：{e['note']}", ""]
        lines += ["", "## 继承缺口逐项结果", "", "| 缺口 ID | 字段 | 本轮状态 | 结果 | 仍开放 |", "|---|---|---|---|---|"]
        for g in card["gaps"]:
            lines.append(f"| `{g['orig_gap_id']}` | {g['fact_field']} | {g['status']} | {(g['result'] or '').replace('|','/')[:120]} | {g['open']} |")
        with open(os.path.join(cards_dir, f"{card['company_id']}.md"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(lines) + "\n")

    meta = {
        "note": ("补充版：原修复包已通过独立验收；本版按用户授权新增公司证据，补充后验证与独立验收分开。阶段B业务组尚未固定。"),
        "self_check": "",
        "input_digest": lock["input_root_digest"],
        "code_version": lock["code_version"],
        "n_companies": len(cards),
        "n_researched": sum(1 for c in cards if c["researched"]),
        "n_facts": len(facts),
        "n_evidence": len(evidence),
        "n_links": len(links),
        "n_gaps": len(gaps),
        "n_open_gaps": sum(1 for g in gaps if g["open_at_stage_b_end"] == "YES"),
        "n_capital": len(caps),
    }
    ver_path = os.path.join(RUN, "verification.json")
    if os.path.exists(ver_path):
        ver = json.load(open(ver_path, encoding="utf-8"))
        meta["self_check"] = f"{ver['n_pass']}/{ver['n_checks']}"

    html = build_html(cards, meta)
    with open(os.path.join(RUN, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)

    checks = {
        "cards": len(cards),
        "bytes": len(html.encode("utf-8")),
        "has_chinese": "公司" in html and "证据" in html,
        "has_search": "id=\"q\"" in html and "function renderList" in html,
        "has_evidence_links": html.count("href=\"http") >= 1,
        "has_unsearched_note": "未查或查后未找到" in html or "含未查字段" in html,
        "n_facts_in_payload": sum(len(c["facts"]) for c in cards),
        "n_gaps_in_payload": sum(len(c["gaps"]) for c in cards),
        "n_capital_in_payload": sum(len(c["capital"]) for c in cards),
        "meta": meta,
    }
    write_json(os.path.join(WORK, "html_checks.json"), checks)
    write_json(os.path.join(WORK, "overview_payload.json"), {"meta": meta, "n_cards": len(cards)})
    from s00_common import sha256_file  # noqa: WPS433
    card_files = {}
    for name in sorted(os.listdir(cards_dir)):
        if not name.endswith(".md"):
            continue
        rel = f"company_cards/{name}"
        card_files[rel] = {"sha256": sha256_file(os.path.join(cards_dir, name))}
    write_json(os.path.join(WORK, "card_manifest.json"), {
        "input_root_digest": lock["input_root_digest"],
        "n_files": len(card_files),
        "files": card_files,
    })
    import subprocess
    js = os.path.join(RUN, "scripts", "s08_html_runtime_check.js")
    node = subprocess.run(["node", js, RUN], cwd=RUN, capture_output=True, text=True, timeout=60)
    print(json.dumps({"cards": checks["cards"], "html_bytes": checks["bytes"],
                      "facts": checks["n_facts_in_payload"], "gaps": checks["n_gaps_in_payload"],
                      "capital": checks["n_capital_in_payload"],
                      "node_exit": node.returncode}, ensure_ascii=False, indent=2))
    return 0 if node.returncode == 0 else 1


def _group(rows: list[dict], key: str) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        out[r[key]].append(r)
    return out


if __name__ == "__main__":
    raise SystemExit(main())
