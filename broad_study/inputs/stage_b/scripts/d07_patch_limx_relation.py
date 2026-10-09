"""One-off patch: add the second-channel relation for the LimX pre-IPO event."""
import io
import json

P = r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_b_repair\run_20260914T231644Z\work\research\authored_CN_LIMX.json"
q = chr(34)
src = io.open(P, encoding="utf-8").read()
target = q + "fact" + q + ": " + q + "capital_event_limx_pre_ipo" + q + ", " + q + "evidence" + q + ": " + q + "B_CN_LIMX_002" + q
idx = src.index(target)
line_end = src.index("\n", idx)
extra = (",\n    {" + q + "fact" + q + ": " + q + "capital_event_limx_pre_ipo" + q
         + ", " + q + "evidence" + q + ": " + q + "B_CN_LIMX_003" + q
         + ", " + q + "role" + q + ": " + q + "SUPPORTS" + q
         + ", " + q + "review_note" + q + ": " + q + "Pre-IPO 事件来源（独立第二渠道，含具体宣布日）" + q + "}")
src = src[:line_end] + extra + src[line_end:]
io.open(P, "w", encoding="utf-8", newline="\n").write(src)
json.load(io.open(P, encoding="utf-8"))
print("patched, json valid")
