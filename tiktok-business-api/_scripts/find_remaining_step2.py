import re
import os
import sys
from collections import Counter

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)
sys.path.insert(0, _SCRIPT_DIR)

from test_engine import new_text

new_parts = new_text.split("```")
new_prose = "\n".join([new_parts[k] for k in range(0, len(new_parts), 2)])

lines = []
for l in new_prose.splitlines():
    ls = l.strip()
    if not ls or ls.startswith("<a id=") or ls.startswith("<!-- doc_id:"):
        continue
    words = re.findall(r"\b[A-Za-z]{3,}\b", ls)
    allowed = {
        "tiktok", "curl", "post", "json", "http", "https", "true", "false", "null", "none",
        "objective_type", "campaign_type", "budget_mode", "budget", "advertiser_id", "campaign_name",
        "adgroup_name", "optimization_goal", "billing_event", "bid_type", "bid_price", "pixel_id"
    }
    filtered = [w for w in words if w.lower() not in allowed]
    if len(filtered) >= 3:
        lines.append(ls)

counts = Counter(lines)
print(f"Remaining lines with >= 3 English words: {len(lines)}, unique: {len(counts)}")
with open(os.path.join(ROOT, "_work/remaining_step2.txt"), "w", encoding="utf-8") as f:
    for l, c in counts.most_common():
        f.write(f"{c:4d}\t{l}\n")

print("\nTop 40 remaining lines:")
for l, c in counts.most_common(40):
    print(f"{c:3d}: {l[:100]}")
