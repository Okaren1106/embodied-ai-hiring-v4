"""Stage B repair r2 / step 0: marker files and pipeline entry."""
from __future__ import annotations

import json
import os
import platform
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import CODE_VERSION, RUN, WORK, write_json  # noqa: E402

MARKER = "TARGETED_COLLECTION_PENDING_ACCEPTANCE"

STEPS = [
    "s01_lock_inputs.py", "s02_build_facts.py", "s03_build_tables.py",
    "s05_grouping.py", "s03b_company_profile.py", "s09_search_log.py",
    "s04_verify.py", "s07_cards_and_html.py", "s06_rebuild_and_fault.py",
    "s11_release_gate.py",
]

def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    env = {
        "python": sys.version,
        "executable": sys.executable,
        "platform": platform.platform(),
        "encoding_default": sys.getdefaultencoding(),
        "run": RUN,
        "code_version": CODE_VERSION,
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    write_json(os.path.join(WORK, "env_probe.json"), env)

    with open(os.path.join(RUN, MARKER), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(
            "stage: B\n"
            "scope: TARGETED_COLLECTION_PENDING_ACCEPTANCE\n"
            "note: 定向补查完成，待独立验收；不是阶段 B 完成，不进入阶段 C。\n"
            "field_level_unknowns: 逐字段未查/查后未找到仍明确展示\n"
            f"code_version: {CODE_VERSION}\n"
            f"generated_at_utc: {env['generated_at_utc']}\n"
        )
    for stale_name in ("STAGE_B_COMPLETE", "PILOT_REPAIR_ONLY", "REPAIR_R2_PENDING_ACCEPTANCE"):
        stale = os.path.join(RUN, stale_name)
        if os.path.exists(stale):
            os.remove(stale)
    print(json.dumps({"marker": MARKER, "steps": STEPS, "run": RUN}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
