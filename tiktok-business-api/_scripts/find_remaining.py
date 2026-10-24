import re
import os
import sys
from collections import Counter

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)
sys.path.insert(0, _SCRIPT_DIR)

from u101_dict_structural import DOC_TITLES, BREADCRUMBS, HEADING_RULES
from u101_dict_tables import TABLE_PHRASE_RULES
from u101_dict_prose import PROSE_RULES

path = os.path.join(ROOT, "docs/08-use-cases/use-case-tao-chien-dich-p1.md")
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

parts = text.split("```")
prose_parts = [parts[i] for i in range(0, len(parts), 2)]
t = "\n".join(prose_parts)

for pattern, repl in HEADING_RULES:
    t = re.sub(pattern, repl, t, flags=re.MULTILINE)
for pattern, repl in TABLE_PHRASE_RULES:
    t = re.sub(pattern, repl, t)
for pattern, repl in PROSE_RULES:
    t = re.sub(pattern, repl, t)

# Extract remaining lines with English
remaining_lines = []
for line in t.splitlines():
    ls = line.strip()
    if not ls or ls.startswith("<a id=") or ls.startswith("<!-- doc_id:"):
        continue
    # check english words
    words = re.findall(r"\b[A-Za-z]{3,}\b", ls)
    allowed = {
        "tiktok", "curl", "post", "json", "http", "https", "true", "false", "null", "none",
        "objective_type", "campaign_type", "budget_mode", "budget", "advertiser_id", "campaign_name",
        "adgroup_name", "optimization_goal", "billing_event", "bid_type", "bid_price", "pixel_id"
    }
    filtered = [w for w in words if w.lower() not in allowed]
    if len(filtered) >= 3:
        remaining_lines.append(ls)

counts = Counter(remaining_lines)
print(f"Remaining distinct lines: {len(counts)}, total lines: {len(remaining_lines)}")
with open(os.path.join(ROOT, "_work/remaining_en.txt"), "w", encoding="utf-8") as f:
    for l, c in counts.most_common():
        f.write(f"{c:4d}\t{l}\n")
print("Top 40 remaining:")
for l, c in counts.most_common(40):
    print(f"{c:3d}: {l[:100]}")
