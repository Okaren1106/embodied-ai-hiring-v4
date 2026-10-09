from bootstrap import *
def edit(name,old,new):
 p=RUN/'scripts'/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new),encoding='utf-8')
edit('s05_grouping.py','    if fact["time_applicability"] in STRICT_COMPARABLE_TIME:','    if fact.get("assertion_kind") in ("RESEARCH_OUTPUT", "LONG_TERM_GOAL", "DATE_CONFLICT"):\n        return "BACKGROUND_DISPLAY_ONLY", "研究产物、长期目标或首发日期冲突不作当前商业产品/场景分组"\n    if fact["time_applicability"] in STRICT_COMPARABLE_TIME:')
edit('s07_cards_and_html.py','"snapshot": e["snapshot_text_path"], "snapshot_sha256": e["snapshot_sha256"],','"snapshot": e["snapshot_text_path"], "snapshot_sha256": e["snapshot_sha256"],\n                "capture_medium": e.get("capture_medium", ""), "raw": e.get("snapshot_raw_path", ""),\n                "raw_sha256": e.get("snapshot_raw_sha256", ""), "capture_record": e.get("capture_record_path", ""),')
edit('s07_cards_and_html.py',"+ ' ｜ 定位 '+esc(e.quote_locator)+' ｜ 快照 '+esc(e.snapshot||'—')","+ ' ｜ 定位 '+esc(e.quote_locator)+' ｜ 保存方式 '+esc(e.capture_medium||'历史记录')\n      + ' ｜ <a href=\"'+esc(e.snapshot||'#')+'\" target=\"_blank\">正文快照</a>'\n      + (e.raw ? ' ｜ <a href=\"'+esc(e.raw)+'\" target=\"_blank\">HTTP原件</a>' : ' ｜ 无HTTP原件')\n      + (e.capture_record ? ' ｜ <a href=\"'+esc(e.capture_record)+'\" target=\"_blank\">读取记录</a>' : '')")
edit('s07_cards_and_html.py',"f\"- 备注：{e['note']}\", \"\"]","f\"- 保存方式：{e.get('capture_medium', '')}；原件：{e.get('raw', '') or '未保存HTTP原件'}；原件哈希：{e.get('raw_sha256', '') or '不适用'}\",\n                      f\"- 备注：{e['note']}\", \"\"]")
# Actual proposition-level review outcomes, with explicit PAGE_REVIEW provenance.
ing=read(RUN/'work/supplement_ingestion.json')
with (RUN/'search_log.jsonl').open('a',encoding='utf-8') as f:
 for x in ing['claim_changes']:
  if x['new']['value_status']=='SEARCHED_NOT_FOUND':
   reviewed=[r['review_id'] for r in ing['cards'] if r['company_id']==x['company_id']]
   f.write(json.dumps({'ts_utc':ing['created_at'],'action':'PAGE_REVIEW','company_id':x['company_id'],'field':x['field'],'question':x['field'],'outcome':'REVIEWED_SOURCES_DO_NOT_ESTABLISH_CLAIM','review_cards':reviewed,'note':x['new']['decision_reason'],'timestamp_meaning':'review decision recorded, not a fabricated external search'},ensure_ascii=False)+'\n')
print('finish code applied')
